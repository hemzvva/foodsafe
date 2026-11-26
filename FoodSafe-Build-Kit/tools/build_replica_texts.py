#!/usr/bin/env python3
"""Build tools/replica-texts.json: every verbatim UI string of the 13 mockup screens.

Usage:  python3 -I tools/build_replica_texts.py <design-package-dir> [out.json]

Sources (inside the design package):
  reference/SCREEN-TEXT-RUNS.json          text runs measured from the mockup
  reference/SCREEN-COORDINATE-MASTER.json  element ids per screen

The measured runs contain a few reading mistakes. Each one was checked by eye
against reference/rectified/NN-*.jpg and is listed in CORRECTIONS below with the
reason. Strings whose characters cannot be read at the source size are listed in
ILLEGIBLE: the fact-check script refuses to let a document quote them as shown.
"""
import json
import sys
from pathlib import Path

# (screen number, run id) -> (string as measured, string as read on the rectified image, reason)
CORRECTIONS = [
    ("01", "support-1", "Your Kitchen.", "Your kitchen.",
     "rectified 01-welcome.jpg shows a small k; design.md writes it the same way"),
    ("05", "chicken-missing", "Missing: Soy Sauce (optional)", "Missing: soy sauce (optional)",
     "rectified 05-recipe-suggestions.jpg shows lower case, like the curry line on screen 10"),
    ("09", "why-1", "✓ Similar acidity and flavor profile.", "Similar acidity and flavor profile.",
     "the check mark is an icon, not text"),
    ("09", "why-2", "✓ Works in the same type of recipes.", "Works in the same type of recipes.",
     "the check mark is an icon, not text"),
]

# (screen number, run id, reason): characters are not readable at the source size.
ILLEGIBLE = [
    ("04", "tomato-meta", "amount digits unreadable; the measured run and design.md disagree"),
    ("04", "spinach-meta", "amount unreadable; design.md reads it as a multiplication, the run as pcs"),
    ("04", "pasta-meta", "amount digits unreadable"),
    ("04", "chicken-meta", "amount digits unreadable; the run reads 400 g, design.md reads 40 g"),
    ("10", "tab-almost", "count unreadable; design.md says 3, the run says 1"),
    ("10", "tab-smart", "count unreadable"),
]

# Multi-line texts: run ids joined with one space into the sentence the reader sees.
JOINED = [
    ("01", ["tagline-1", "tagline-2"]),
    ("01", ["support-1", "support-2", "support-3"]),
    ("03", ["notes-label", "notes-optional"]),
    ("07", ["instruction-1", "instruction-2", "instruction-3", "instruction-4"]),
    ("12", ["alert-line1", "alert-line2"]),
    ("12", ["tips-line1", "tips-line2"]),
]


def main():
    pkg = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_name("replica-texts.json")
    runs = json.loads((pkg / "reference/SCREEN-TEXT-RUNS.json").read_text(encoding="utf-8"))
    master = json.loads((pkg / "reference/SCREEN-COORDINATE-MASTER.json").read_text(encoding="utf-8"))
    elements = {s["id"]: [e["id"] for e in s.get("elements", [])] for s in master["screens"]}

    fixes = {(n, i): new for n, i, _old, new, _why in CORRECTIONS}
    olds = {(n, i): old for n, i, old, _new, _why in CORRECTIONS}
    illegible = {(n, i): why for n, i, why in ILLEGIBLE}

    if len(runs["screens"]) != len(master["screens"]):
        sys.exit("text-run file and coordinate master list a different number of screens")
    screens, allowed = {}, set()
    illegible_out, corrections_out = [], []
    # Both files list the 13 screens in the same order (01..13); the ids differ in spelling.
    for s, m in zip(runs["screens"], master["screens"]):
        n = m["id"][:2]
        text_ids, strings, by_id = [], [], {}
        for r in s["text_runs"]:
            text = fixes.get((n, r["id"]), r["text"])
            if (n, r["id"]) in olds and olds[(n, r["id"])] != r["text"]:
                sys.exit(f"correction {n}:{r['id']} does not match the measured run: {r['text']!r}")
            by_id[r["id"]] = text
            text_ids.append(r["id"])
            if (n, r["id"]) in illegible:
                illegible_out.append({"screen": n, "id": r["id"], "run": text, "why": illegible[(n, r["id"])]})
                continue
            strings.append(text)
        screens[n] = {"slug": m["id"], "title": m["title"], "text_ids": text_ids,
                      "element_ids": elements.get(m["id"], []), "strings": strings}
        allowed.update(strings)
        screens[n]["_by_id"] = by_id

    joined = []
    for n, ids in JOINED:
        by_id = screens[n]["_by_id"]
        text = " ".join(by_id[i] for i in ids)
        joined.append({"screen": n, "ids": ids, "text": text})
        allowed.add(text)
    for sc in screens.values():
        del sc["_by_id"]

    for n, i, old, new, why in CORRECTIONS:
        corrections_out.append({"screen": n, "id": i, "measured": old, "read": new, "why": why})

    doc = {
        "schema": 1,
        "source": "design package reference/SCREEN-TEXT-RUNS.json, checked by eye against reference/rectified/*.jpg",
        "rule": "Only strings in 'allowed' may appear inside guillemets in the kit documents. "
                "Strings in 'illegible' must not be quoted as shown.",
        "screens": screens,
        "joined": joined,
        "corrections": corrections_out,
        "illegible": illegible_out,
        "allowed": sorted(allowed),
    }
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {out}: {len(screens)} screens, {len(allowed)} allowed strings, "
          f"{len(corrections_out)} corrections, {len(illegible_out)} illegible")


if __name__ == "__main__":
    main()
