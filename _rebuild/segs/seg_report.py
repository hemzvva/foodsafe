# ----------------------------------------------------------------------------- B-25 / B-26 problem report and event log
# The text a person can send from S-19 and the event log it reads (03-ENGINEERING/FIELD-QUALITY.md). Everything here is integer
# arithmetic and string handling on Unicode scalars, so that the Swift twin can match it byte for byte.
REPORT_FIRST_LINE = "FOODSAFE-REPORT 1"
REPORT_ATTACHMENT_MAX_BYTES = 262144  # 256 KiB: what the report attaches at most
REPORT_EVENT_LINES = 40               # the newest event lines a report carries
REPORT_NOTE_MAX = 500                 # scalars of the note
REPORT_FACT_MAX = 60                  # scalars of a fact
LOG_MAX_LINES = 200                   # the newest lines the log on the phone keeps
EVENT_DETAIL_MAX = 64                 # scalars of the detail of an event
REPORT_CHANNELS = ("appstore", "testflight", "development")

# B-26: the closed list of event codes: (code, written when, detail). A code outside this list is never written.
EVENT_CODES = [
    ("app.launch", "the app process started and the first scene became active", "none"),
    ("app.memory", "the system sent a memory warning", "none"),
    ("store.open.fail", "the data store could not be opened (S-18 is shown)", "the error domain, a colon and the error code"),
    ("store.save.fail", "saving a change failed", "the operation word, a colon, the error domain, a colon and the error code"),
    ("content.load.fail", "the bundled recipe data failed to load or to validate (S-18 is shown)", "the name of the `ContentError` case"),
    ("starter.apply", "the starter list added rows", "`n=` and the number of rows"),
    ("cook.start", "a cooking session opened", "the recipe id"),
    ("cook.finish", "cook-complete was confirmed", "`used=` and the number of rows that were reduced or removed"),
    ("cook.discard", "a cooking session was dropped by the six-hour rule", "none"),
    ("timer.start", "a step timer started", "the step number"),
    ("timer.extend", "a step timer got one more minute", "the step number"),
    ("timer.finish", "the app saw a step timer reach zero", "the step number"),
    ("alarm.auth", "the alarm permission was read or asked", "`authorized`, `denied` or `notDetermined`"),
    ("alarm.schedule", "a system alarm was scheduled", "`ok`, or the error domain, a colon and the error code"),
    ("alarm.cancel", "a system alarm was cancelled", "`ok`, or the error domain, a colon and the error code"),
    ("digest.auth", "the notification permission was read or asked", "`authorized`, `denied` or `notDetermined`"),
    ("digest.schedule", "the requests of the daily reminder were replaced", "`n=` and the number of requests, or the error domain, a colon and the error code"),
    ("diag.received", "MetricKit delivered a diagnostic payload and it was saved", "`crash=`, `hang=`, `cpu=` or `disk=` and the count"),
    ("report.open", "S-19 was opened", "none"),
    ("report.mail", "the mail composer closed", "`sent`, `saved`, `cancelled`, `failed` or `unavailable`"),
    ("state.invalid", "the code met a state that the rules say cannot exist", "a short word that names the check that failed"),
]
EVENT_CODE_NAMES = [c_[0] for c_ in EVENT_CODES]
_DETAIL_OK = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._:=-")


def utc_text(epoch: int) -> str:
    """B-26: epoch seconds as `2026-04-18T09:21:07Z` (UTC). Valid from 0 to 253402300799 (the year 9999); any other value reads `unknown`."""
    if not 0 <= epoch <= 253402300799:
        return "unknown"
    t = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=epoch)
    return "%04d-%02d-%02dT%02d:%02d:%02dZ" % (t.year, t.month, t.day, t.hour, t.minute, t.second)


def detail_text(raw: str) -> str:
    """B-26: the detail of an event keeps ASCII letters, digits and `. _ : = -`; every other scalar becomes `-`; at most 64 scalars."""
    return "".join(ch if ch in _DETAIL_OK else "-" for ch in raw)[:EVENT_DETAIL_MAX]


def event_line(epoch: int, code: str, detail: str = "") -> Optional[str]:
    """B-26: one line of the log, `2026-04-18T09:21:07Z alarm.schedule ok`. None for a code outside the closed list: nothing is written."""
    if code not in EVENT_CODE_NAMES:
        return None
    d = detail_text(detail)
    return "%s %s%s" % (utc_text(epoch), code, " " + d if d else "")


def log_keep(lines: List[str], n: int = LOG_MAX_LINES) -> List[str]:
    """B-26: the log keeps its newest n lines (200 on the phone)."""
    return lines[len(lines) - n:] if len(lines) > n else list(lines)


def fact_text(raw: Optional[str]) -> str:
    """B-25: a fact of the report. Control scalars (below U+0020, and U+007F) become spaces, spaces are trimmed from both ends, at most
    60 scalars are kept; an empty result reads `unknown`."""
    s = "".join(" " if (ord(ch) < 32 or ord(ch) == 127) else ch for ch in (raw or "")).strip(" ")[:REPORT_FACT_MAX]
    return s if s else "unknown"


def note_text(raw: Optional[str]) -> str:
    """B-25: the note of the person. CRLF and CR become LF, space, tab, LF and CR are trimmed from both ends, at most 500 scalars are
    kept; an empty result reads `none`."""
    s = (raw or "").replace("\r\n", "\n").replace("\r", "\n").strip(QUERY_TRIM)[:REPORT_NOTE_MAX]
    return s if s else "none"


def attachment_plan(sizes: List[int], limit: int = REPORT_ATTACHMENT_MAX_BYTES) -> Tuple[str, int, int]:
    """B-25: which saved diagnostic files the report attaches. `sizes` lists the files in bytes, newest first. Files are taken in that
    order while their total stays within `limit`; the first file that does not fit ends the selection (an older, smaller file never
    takes its room). Returns (state, number of files, total bytes): `none` without files, `too-large` when the newest file alone does
    not fit, otherwise `included`."""
    if not sizes:
        return "none", 0, 0
    total, n = 0, 0
    for s in sizes:
        if total + s > limit:
            break
        total += s
        n += 1
    if n == 0:
        return "too-large", 0, 0
    return "included", n, total


def _word(v, allowed) -> str:
    return v if v in allowed else "unknown"


def _on_off(v) -> str:
    return "on" if v is True else "off" if v is False else "unknown"


def _whole(v, low: int, high: Optional[int] = None) -> Optional[int]:
    """An integer that is not a boolean and lies in [low, high]; None otherwise."""
    if type(v) is not int or v < low or (high is not None and v > high):
        return None
    return v


def build_report(r: dict) -> str:
    """B-25: the text of the problem report, format 1. `r` is the record of FIELD-QUALITY.md; every key may be missing, and a missing
    or invalid value reads `unknown`. One fact per line in a fixed order, then the newest 40 event lines, then the note."""
    minute = r.get("reminderMinute")
    reminder = "off" if minute is None else ("on %02d:%02d" % divmod(minute, 60) if _whole(minute, 0, 1439) is not None else "unknown")
    tz = _whole(r.get("tzOffsetMinutes"), -720, 840)
    if tz is None:
        zone = "unknown"
    else:
        zone = "UTC%s%02d:%02d" % ("-" if tz < 0 else "+", abs(tz) // 60, abs(tz) % 60)
    free = _whole(r.get("freeMB"), 0)
    items = _whole(r.get("items"), 0)
    sizes = [x for x in (r.get("diagnosticSizes") or [])]
    state, n_files, n_bytes = attachment_plan(sizes)
    if state == "none":
        diag = "none"
    elif state == "included":
        diag = "included (%d %s, %d bytes)" % (n_files, _plural(n_files, "file", "files"), n_bytes)
    else:
        diag = "too large (%d bytes)" % sizes[0]
    lines = list(r.get("eventLines") or [])
    shown = log_keep(lines, REPORT_EVENT_LINES)
    head = "Events: %d" % len(shown) if len(shown) == len(lines) else "Events: %d of %d" % (len(shown), len(lines))
    out = [REPORT_FIRST_LINE,
           "App: %s (%s)" % (fact_text(r.get("appVersion")), fact_text(r.get("build"))),
           "Channel: " + _word(r.get("channel"), REPORT_CHANNELS),
           "Device: " + fact_text(r.get("deviceModel")),
           "System: iOS %s (%s)" % (fact_text(r.get("osVersion")), fact_text(r.get("osBuild"))),
           "Calendar: " + fact_text(r.get("calendar")),
           "Time zone: " + zone,
           "Notifications: " + _word(r.get("notifications"), PERMISSION_WORDS),
           "Alarms: " + _word(r.get("alarms"), PERMISSION_WORDS),
           "Reminder: " + reminder,
           "Text size: " + fact_text(r.get("textSize")),
           "Reduce Motion: " + _on_off(r.get("reduceMotion")),
           "Low Power Mode: " + _on_off(r.get("lowPower")),
           "Storage free: " + ("unknown" if free is None else "%d MB" % free),
           "Items: " + ("unknown" if items is None else str(items)),
           "Diagnostics: " + diag,
           head] + shown + ["Note: " + note_text(r.get("note"))]
    return "\n".join(out)


REPORT_EXAMPLE = {
    "appVersion": "1.0.0", "build": "57", "channel": "testflight", "deviceModel": "iPhone16,2", "osVersion": "26.1", "osBuild": "23B85",
    "calendar": "gregorian", "tzOffsetMinutes": 60, "notifications": "authorized", "alarms": "denied", "reminderMinute": 1080,
    "textSize": "large", "reduceMotion": False, "lowPower": True, "freeMB": 812, "items": 23, "diagnosticSizes": [18432, 9000],
    "eventLines": ["2026-04-18T09:21:07Z app.launch", "2026-04-18T09:21:09Z alarm.auth denied", "2026-04-18T09:22:31Z timer.finish 2"],
    "note": "The timer did not ring.",
}


def report_cases() -> List[Tuple[str, dict]]:
    """The records of the B-25 vectors: the full example, the empty record, the limits and every `unknown` path."""
    many = ["2026-04-18T09:%02d:00Z app.launch" % k for k in range(55)]
    return [
        ("a full report", REPORT_EXAMPLE),
        ("an empty record reads unknown", {}),
        ("55 event lines: the newest 40 are carried", dict(REPORT_EXAMPLE, eventLines=many)),
        ("exactly 40 event lines are all carried", dict(REPORT_EXAMPLE, eventLines=many[:40])),
        ("no event line", dict(REPORT_EXAMPLE, eventLines=[])),
        ("the newest diagnostic file does not fit", dict(REPORT_EXAMPLE, diagnosticSizes=[300000, 10])),
        ("the newest two files fill the limit exactly", dict(REPORT_EXAMPLE, diagnosticSizes=[200000, 62144, 1])),
        ("one file only", dict(REPORT_EXAMPLE, diagnosticSizes=[5])),
        ("no diagnostic file", dict(REPORT_EXAMPLE, diagnosticSizes=[])),
        ("control characters and a long value in a fact", dict(REPORT_EXAMPLE, deviceModel="  iPhone\t16,2\n", textSize="x" * 100)),
        ("a note of 600 scalars with CRLF line ends is cut at 500", dict(REPORT_EXAMPLE, note="  line one\r\nline two\r" + "y" * 600)),
        ("an empty note reads none", dict(REPORT_EXAMPLE, note="  \r\n ")),
        ("words outside the closed lists read unknown", dict(REPORT_EXAMPLE, channel="beta", notifications="provisional", alarms="yes")),
        ("a reminder at midnight and a zone west of UTC", dict(REPORT_EXAMPLE, reminderMinute=0, tzOffsetMinutes=-210)),
        ("the last minute of the day and a zone with 45 minutes", dict(REPORT_EXAMPLE, reminderMinute=1439, tzOffsetMinutes=345)),
        ("a reminder and a zone out of range", dict(REPORT_EXAMPLE, reminderMinute=1440, tzOffsetMinutes=841)),
        ("a reminder that is off and the zone at the west end", dict(REPORT_EXAMPLE, reminderMinute=None, tzOffsetMinutes=-720)),
        ("a negative count and a fractional size read unknown", dict(REPORT_EXAMPLE, items=-1, freeMB=1.5)),
        ("a boolean is not a count", dict(REPORT_EXAMPLE, items=True)),
    ]


REPORT_BEGIN = "<!-- BEGIN GENERATED REPORT EXAMPLE (python3 tools/rules_reference.py --print-report-example) -->"
REPORT_END = "<!-- END GENERATED REPORT EXAMPLE -->"
CODES_BEGIN = "<!-- BEGIN GENERATED EVENT CODES (python3 tools/rules_reference.py --print-event-codes) -->"
CODES_END = "<!-- END GENERATED EVENT CODES -->"


def report_example_markdown() -> str:
    return "\n".join([REPORT_BEGIN, "", "```text", build_report(REPORT_EXAMPLE), "```", "", REPORT_END])


def event_codes_markdown() -> str:
    out = [CODES_BEGIN, "", "| Code | Written when | Detail |", "|---|---|---|"]
    out += ["| `%s` | %s | %s |" % c_ for c_ in EVENT_CODES]
    out += ["", CODES_END]
    return "\n".join(out)


