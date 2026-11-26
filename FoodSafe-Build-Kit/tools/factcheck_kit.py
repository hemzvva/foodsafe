#!/usr/bin/env python3
"""Fact-check script for the FoodSafe Build Kit documents.

Usage
  python3 -I tools/factcheck_kit.py [--kit DIR] [FILE.md ...]   check files (default: every kit .md)
  python3 -I tools/factcheck_kit.py --list-ids                  print every defined id
  python3 -I tools/factcheck_kit.py --self-test                 prove every rule fires

Exit code 0 only when there are no errors and no warnings. The last line is
`factcheck: N error(s), M warning(s)`.

Rules
  ERROR  ID-UNDEFINED      an id of a known family is cited but defined nowhere in the kit
  ERROR  STRING-UNKNOWN    a «guillemet» string is not a verbatim mockup string (tools/replica-texts.json)
  ERROR  STRING-ILLEGIBLE  a «guillemet» string is one the mockup does not show legibly
  ERROR  SHOWN-MALFORMED   a SHOWN tag is not `NN:element-id` or `«verbatim string»`
  ERROR  SHOWN-UNKNOWN     `NN:element-id` is not an element or text run of mockup screen NN
  ERROR  REASON-SHORT      a DERIVED or NECESSARY tag has a reason under 15 characters
  ERROR  TAG-MALFORMED     a DERIVED, NECESSARY, DECISION or REMOVED tag has the wrong shape
  ERROR  EMAIL             an e-mail-shaped string that is not a reserved example
  WARN   VAGUE             hedging wording (TBD, probably, maybe, "and so on", ...)
  WARN   DATE              an ISO date outside a "read on" provenance line
  WARN   PRESSURE          time-pressure wording (deadline, ASAP, ...)

Conventions
  * Fenced blocks and `inline code` are skipped for strings, tags and warnings. Ids and e-mail shapes are
    still checked inside a plain fence. A fence whose info string contains `nocheck` is skipped entirely.
  * A line ending in `<!-- fc:ignore -->` is exempt from the three warnings.
  * An id is DEFINED where a line, table row, heading or bullet starts with it and the id is followed by
    the end of the line, `|`, `:`, `.`, `(`, a dash, or a capitalised word. Task ids are also defined by
    the file name of their card (`T-09-core-types.md` defines T-09).
"""
import json
import re
import sys
import tempfile
from pathlib import Path

ID_FAMILIES = [
    r"D-X-\d+", r"D-\d\d-\d+", r"R-\d\d-\d+", r"A-\d\d-\d+", r"B-\d\d", r"I-\d\d", r"V-\d+", r"U-\d+",
    r"TB-\d+", r"N-\d\d", r"J-\d+", r"M-\d\d", r"DM-\d+", r"MI-\d\d", r"E-\d\d", r"S-\d\d", r"BL-\d\d",
    r"RC-\d\d", r"T-\d\d[a-z]?", r"C-\d+",
]
ID_BODY = "(?:" + "|".join(ID_FAMILIES) + ")"
ID_RE = re.compile(r"(?<![A-Za-z0-9-])" + ID_BODY + r"(?![A-Za-z0-9])")
ID_AT_START = re.compile(ID_BODY + r"(?![A-Za-z0-9])")
DEF_FOLLOW = re.compile(r"^(?:$|\s*[|:.(—–-]|\s+[A-Z*\[`«])")
DECISION_RE = re.compile(r"^(?:D-X-\d+|D-\d\d-\d+)$")

GUILLEMET_RE = re.compile("«([^»]*)»")
SHOWN_RE = re.compile(r"\[SHOWN:([^\]]*)\]")
SHOWN_TOKEN = re.compile(r"(\d\d):([a-z0-9][a-z0-9-]*)|«[^»]+»")
REASON_RE = re.compile(r"\[(DERIVED|NECESSARY):([^\]]*)\]")
OTHER_TAG_RE = re.compile(r"\[(DERIVED|NECESSARY|DECISION|REMOVED)\b([^\]]*)\]")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,})")
IMAGE_SCALE_RE = re.compile(r"@[23]x\.")
RESERVED_DOMAINS = ("example.com", "example.org", "example.net")
RESERVED_SUFFIXES = (".invalid", ".test", ".example", ".example.com", ".example.org", ".example.net")
DATE_RE = re.compile(r"\b20\d\d-\d\d-\d\d\b")
VAGUE_RE = re.compile(
    r"\b(TBD|TODO|FIXME|probably|maybe|presumably|perhaps|and so on|and so forth|should be fine|"
    r"roughly the same|something like|approximately the same|etc\.)(?![A-Za-z])", re.IGNORECASE)
PRESSURE_RE = re.compile(
    r"\b(deadline|ASAP|urgent|urgently|hurry|by tomorrow|this week|next week|end of day)\b", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```+|~~~+)(.*)$")
SKIP_DIRS = {"design-package", "__pycache__", ".git", "node_modules", "field-inbox", "private", "FoodSafe-Project"}

# line modes produced by split_lines
PROSE, FENCE, SKIP = "prose", "fence", "skip"


# ---------------------------------------------------------------- reading

def kit_markdown_files(kit):
    files = []
    for p in sorted(kit.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.relative_to(kit).parts):
            continue
        files.append(p)
    return files


def blank_inline_code(line):
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)


def split_lines(text):
    """Yield (lineno, raw, prose, mode). mode: PROSE (all rules), FENCE (ids and e-mails only), SKIP."""
    in_fence, nocheck, fence_char = False, False, ""
    for n, raw in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(raw)
        if m and not in_fence:
            in_fence, fence_char, nocheck = True, m.group(1)[0], "nocheck" in m.group(2)
            yield n, raw, "", SKIP
            continue
        if m and in_fence and m.group(1)[0] == fence_char:
            in_fence = False
            yield n, raw, "", SKIP
            continue
        if in_fence:
            yield n, raw, "", (SKIP if nocheck else FENCE)
        else:
            yield n, raw, blank_inline_code(raw), PROSE


def definition_ids(raw):
    """Ids this line defines. The line starts with the id (after a heading mark, bullet or table pipe)."""
    s = raw.strip()
    s = re.sub(r"^#{1,6}\s+", "", s)
    s = re.sub(r"^[-*+]\s+", "", s)
    s = re.sub(r"^\|\s*", "", s)
    found = []
    while True:
        s = re.sub(r"^(?:\*\*|__|`)+", "", s)
        m = ID_AT_START.match(s)
        if not m:
            return []
        found.append(m.group(0))
        s = re.sub(r"^(?:\*\*|__|`)+", "", s[m.end():])
        chain = re.match(r"^\s*(?:,|/|&|and)\s*(?=(?:\*\*|__|`)*" + ID_BODY + ")", s)
        if not chain:
            break
        s = s[chain.end():]
    return found if DEF_FOLLOW.match(s) else []


def collect_definitions(kit):
    defined = set()
    for p in kit_markdown_files(kit):
        m = re.match(r"^(T-\d\d[a-z]?)(?![A-Za-z0-9])", p.name)
        if m:
            defined.add(m.group(1))
        for _n, raw, _prose, mode in split_lines(p.read_text(encoding="utf-8")):
            if mode == PROSE:
                defined.update(definition_ids(raw))
    return defined


def load_replica(kit):
    path = kit / "tools" / "replica-texts.json"
    if not path.exists():
        return None
    doc = json.loads(path.read_text(encoding="utf-8"))
    return {
        "allowed": set(doc["allowed"]),
        "illegible": {x["run"] for x in doc.get("illegible", [])},
        "screens": {n: set(v["text_ids"]) | set(v["element_ids"]) for n, v in doc["screens"].items()},
    }


# ---------------------------------------------------------------- checking

def norm(s):
    return re.sub(r"\s+", " ", s.strip())


def email_ok(domain):
    d = domain.lower()
    return d in RESERVED_DOMAINS or d.endswith(RESERVED_SUFFIXES)


def check_shown(body, replica):
    """Return a list of (code, message) for one SHOWN tag body."""
    tokens = list(SHOWN_TOKEN.finditer(body))
    rest = SHOWN_TOKEN.sub("", body)
    if not tokens or re.sub(r"[;,\s]", "", rest) != "":
        return [("SHOWN-MALFORMED",
                 f"SHOWN tag body {body.strip()!r} must be `NN:element-id` or a «verbatim mockup string» "
                 "(never write the tag literally in prose)")]
    out = []
    for t in tokens:
        if t.group(1) is None or replica is None:
            continue
        nn, el = t.group(1), t.group(2)
        if nn not in replica["screens"]:
            out.append(("SHOWN-UNKNOWN", f"mockup screen {nn} does not exist (01..13)"))
        elif el not in replica["screens"][nn]:
            out.append(("SHOWN-UNKNOWN", f"{nn}:{el} is not an element or text run of mockup screen {nn}"))
    return out


def check_text(text, name, defined, replica):
    issues = []

    def add(n, level, code, msg):
        issues.append((name, n, level, code, msg))

    for n, raw, prose, mode in split_lines(text):
        if mode == SKIP:
            continue
        for m in ID_RE.finditer(raw):
            if m.group(0) not in defined:
                add(n, "ERROR", "ID-UNDEFINED", f"{m.group(0)} is cited but defined nowhere in the kit")
        for m in EMAIL_RE.finditer(raw):
            if IMAGE_SCALE_RE.search(m.group(0)) or email_ok(m.group(1)):
                continue
            add(n, "ERROR", "EMAIL",
                f"e-mail-shaped string {m.group(0)!r}; only example.com/.org/.net, .invalid, .test and .example are allowed")
        if mode != PROSE:
            continue

        for m in SHOWN_RE.finditer(prose):
            for code, msg in check_shown(m.group(1), replica):
                add(n, "ERROR", code, msg)
        for m in REASON_RE.finditer(prose):
            reason = m.group(2).strip()
            if len(reason) < 15:
                add(n, "ERROR", "REASON-SHORT",
                    f"{m.group(1)} tag needs a reason of at least 15 characters (has {len(reason)})")
        for m in OTHER_TAG_RE.finditer(prose):
            kind, rest = m.group(1), m.group(2)
            if kind in ("DERIVED", "NECESSARY"):
                if not rest.startswith(":"):
                    add(n, "ERROR", "TAG-MALFORMED", f"{kind} tag needs a colon and a reason: [{kind}: reason]")
            elif not rest.startswith(" ") or not all(DECISION_RE.match(x.strip()) for x in rest.split(",")):
                add(n, "ERROR", "TAG-MALFORMED",
                    f"{kind} tag must hold decision ids (D-X-nn or D-NN-k), got {m.group(0)!r}")

        scrubbed = prose
        for m in GUILLEMET_RE.finditer(prose):
            s = norm(m.group(1))
            if replica is not None:
                if s in replica["illegible"]:
                    add(n, "ERROR", "STRING-ILLEGIBLE",
                        f"«{s}» is not legible in the mockup; describe the value as derived instead")
                elif s not in replica["allowed"]:
                    hint = ""
                    if "..." in s and s.replace("...", "…") in replica["allowed"]:
                        hint = " (the mockup uses the single character …)"
                    add(n, "ERROR", "STRING-UNKNOWN", f"«{s}» is not a verbatim string of the mockup{hint}")
            scrubbed = scrubbed.replace(m.group(0), " " * len(m.group(0)))

        if raw.rstrip().endswith("<!-- fc:ignore -->"):
            continue
        for m in VAGUE_RE.finditer(scrubbed):
            add(n, "WARN", "VAGUE",
                f"hedging wording {m.group(0)!r}: state the fact, or mark it `confirm` and list it as an open item")
        if DATE_RE.search(scrubbed) and "read on" not in scrubbed.lower():
            add(n, "WARN", "DATE", "date outside a 'read on <date>' provenance line (the kit carries no dates)")
        for m in PRESSURE_RE.finditer(scrubbed):
            add(n, "WARN", "PRESSURE", f"time-pressure wording {m.group(0)!r} (the kit carries no deadlines)")
    return issues


def check_files(files, kit, display_root=None):
    defined = collect_definitions(kit)
    replica = load_replica(kit)
    issues = []
    for p in files:
        try:
            name = str(p.relative_to(display_root or kit))
        except ValueError:
            name = str(p)
        issues.extend(check_text(p.read_text(encoding="utf-8"), name, defined, replica))
    return issues


def report(issues):
    errors = sum(1 for i in issues if i[2] == "ERROR")
    warns = sum(1 for i in issues if i[2] == "WARN")
    for name, n, level, code, msg in issues:
        print(f"{name}:{n}: {level} [{code}] {msg}")
    print(f"factcheck: {errors} error(s), {warns} warning(s)")
    return errors, warns


# ---------------------------------------------------------------- self-test
# Each entry is (one line of a document, [codes the checker must report on that line]).

SELF_REPLICA = {
    "screens": {
        "01": {"text_ids": ["tagline-1"], "element_ids": ["wordmark"]},
        "05": {"text_ids": ["based-on"], "element_ids": []},
    },
    "illegible": [{"run": "50 g · Fridge"}],
    "allowed": ["Good food.", "Based on your kitchen", "Search ingredients…"],
}

SELF_DEFS = [
    "| D-X-01 | a decision |",
    "### S-01 Welcome",
    "- **B-01**: rounding rule",
    "- A-01-1 — accepted",
    "| **R-05-2** | a rule |",
    "B-02, B-03 and I-01 — grouped definition",
]

SELF_GOOD = [
    ("Uses D-X-01 and `B-01` in S-01 for T-09; acceptance A-01-1, rules R-05-2, B-02, B-03, I-01.", []),
    ("[SHOWN: «Good food.»] [SHOWN: 01:wordmark] [SHOWN: 05:based-on] [SHOWN: 01:tagline-1; 01:wordmark]", []),
    ("[DERIVED: the count comes from the rows] [NECESSARY: the store requires it] [DECISION D-X-01] [REMOVED D-X-01]", []),
    ("Contact: person@example.com, a@b.invalid, c@d.test and logo@2x.png; `[SHOWN: ...]` in code is fine.", []),
    ("Mockup text «Search ingredients…» and «Good   food.» are verbatim.", []),
    ("```text", []),
    ("[SHOWN: ...] and probably maybe TBD inside a plain fence", []),
    ("```", []),
    ("```text nocheck", []),
    ("D-X-98 person@gmail.com", []),
    ("```", []),
    ("The word maybe is exempt here. <!-- fc:ignore -->", []),
    ("Provenance: read on 2026-01-01.", []),
]

SELF_BAD = [
    ("Cites D-X-99.", ["ID-UNDEFINED"]),
    ("Cites «Not a mockup string».", ["STRING-UNKNOWN"]),
    ("Cites «50 g · Fridge».", ["STRING-ILLEGIBLE"]),
    ("Cites «Search ingredients...».", ["STRING-UNKNOWN"]),
    ("[SHOWN: ...]", ["SHOWN-MALFORMED"]),
    ("[SHOWN: 01:wordmark and more]", ["SHOWN-MALFORMED"]),
    ("[SHOWN: 01:nothing]", ["SHOWN-UNKNOWN"]),
    ("[SHOWN: 14:wordmark]", ["SHOWN-UNKNOWN"]),
    ("[DERIVED: short]", ["REASON-SHORT"]),
    ("[NECESSARY: tiny]", ["REASON-SHORT"]),
    ("[DECISION foo]", ["TAG-MALFORMED"]),
    ("[REMOVED]", ["TAG-MALFORMED"]),
    ("[DERIVED no colon]", ["TAG-MALFORMED"]),
    ("Write to person@gmail.com.", ["EMAIL"]),
    ("This is probably fine, TBD.", ["VAGUE", "VAGUE"]),
    ("Done on 2026-03-04.", ["DATE"]),
    ("Needed by tomorrow, no deadline.", ["PRESSURE", "PRESSURE"]),
    ("```text", []),
    ("D-X-97", ["ID-UNDEFINED"]),
    ("```", []),
    ("D-X-96 is cited at the start of a line without a delimiter.", ["ID-UNDEFINED"]),
    ("S-10 never exists, so a line that starts with it (lower-case word next) does not define it.", ["ID-UNDEFINED"]),
    ("See S-10.", ["ID-UNDEFINED"]),
]


def self_test():
    ok = True
    with tempfile.TemporaryDirectory() as td:
        kit = Path(td)
        (kit / "tools").mkdir()
        (kit / "tools" / "replica-texts.json").write_text(
            json.dumps(SELF_REPLICA, ensure_ascii=False), encoding="utf-8")
        (kit / "DEFS.md").write_text("\n".join(SELF_DEFS) + "\n", encoding="utf-8")
        (kit / "T-09-core.md").write_text("task card\n", encoding="utf-8")
        for name, rows in (("good.md", SELF_GOOD), ("bad.md", SELF_BAD)):
            (kit / name).write_text("\n".join(r[0] for r in rows) + "\n", encoding="utf-8")
        issues = check_files([kit / "good.md", kit / "bad.md"], kit)
        for name, rows in (("good.md", SELF_GOOD), ("bad.md", SELF_BAD)):
            want = sorted((i + 1, c) for i, (_t, codes) in enumerate(rows) for c in codes)
            got = sorted((n, code) for f, n, _lv, code, _m in issues if f == name)
            if got != want:
                ok = False
                print(f"self-test FAILED for {name}\n  missing  {sorted(set(want) - set(got))}"
                      f"\n  extra    {sorted(set(got) - set(want))}")
        defined = collect_definitions(kit)
        for must in ("D-X-01", "S-01", "B-01", "A-01-1", "R-05-2", "B-02", "B-03", "I-01", "T-09"):
            if must not in defined:
                ok = False
                print(f"self-test FAILED: {must} should be defined")
        for must_not in ("D-X-99", "D-X-96", "S-10", "D-X-98"):
            if must_not in defined:
                ok = False
                print(f"self-test FAILED: {must_not} should not be defined")
        if definition_ids("T-09 must pass first.") != []:
            ok = False
            print("self-test FAILED: a sentence that starts with an id must not define it")
    print("factcheck self-test: " + ("OK" if ok else "FAILED"))
    return 0 if ok else 1


# ---------------------------------------------------------------- main

def main(argv):
    args = list(argv)
    kit = Path(__file__).resolve().parent.parent
    if "--kit" in args:
        i = args.index("--kit")
        kit = Path(args[i + 1]).resolve()
        del args[i:i + 2]
    if "--self-test" in args:
        return self_test()
    if "--list-ids" in args:
        for i in sorted(collect_definitions(kit)):
            print(i)
        return 0
    files = [Path(a).resolve() for a in args] if args else kit_markdown_files(kit)
    missing = [str(f) for f in files if not f.is_file()]
    if missing:
        print("factcheck: file not found: " + ", ".join(missing))
        return 2
    issues = check_files(files, kit, display_root=Path.cwd() if args else kit)
    errors, warns = report(issues)
    return 1 if (errors or warns) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
