    # The cases that close the holes found by the mistake check. Each is computed by hand and fails when its rule is written wrongly.
    # B-12: the whole order, (days left, the name without regard to capital letters, addedAt, id)
    def crow_(n, name, expiry, added):
        return Item("00000000-0000-4000-8000-%012d" % n, None, name, F(1), F(1), "pcs", "pantry", D(expiry), added)
    for label_, rows_, want_ in [
            ("names are ordered without regard to capital letters",
             [crow_(31, "cherries", "2026-05-01", 1), crow_(32, "Banana", "2026-05-01", 2), crow_(33, "apple", "2026-05-01", 3)], [33, 32, 31]),
            ("the same name and day: the earlier addedAt first, even with the larger id",
             [crow_(40, "Eggs", "2026-05-01", 9), crow_(41, "eggs", "2026-05-01", 5)], [41, 40]),
            ("the same name, day and addedAt: the smaller id first",
             [crow_(51, "eggs", "2026-05-01", 7), crow_(50, "eggs", "2026-05-01", 7)], [50, 51]),
            ("fewer days left first, so an expired row comes before today's rows",
             [crow_(61, "Apple", "2026-04-18", 1), crow_(62, "Zucchini", "2026-04-17", 2), crow_(63, "banana", "2026-04-18", 3)], [62, 61, 63])]:
        c.eq("B-12 " + label_, [int(r.id[-12:]) for r in sort_items(rows_, t)], want_)

    # B-27: "in" is inside Spinach (a name that contains), and inside the alias "mince" of Ground Beef (an alias that contains)
    c.eq("B-27 a name that contains comes before an alias that contains", catalog_search(content, "in"), ["spinach", "ground-beef"])

    # B-24: below the smallest step there is no way down
    c.eq("B-24 0.15 L has no step down", stepper_down(F("0.15"), "L"), None)
    c.eq("B-24 0.2 L steps down to the smallest", stepper_down(F("0.2"), "L"), F(1, 10))
    c.eq("B-24 0.7 pcs has no step down", stepper_down(F("0.7"), "pcs"), None)
    c.eq("B-24 0.15 L steps up to 0.25 L", stepper_up(F("0.15"), "L"), F(1, 4))
    c.eq("B-24 0.7 pcs steps up to 1.2 pcs", stepper_up(F("0.7"), "pcs"), F(6, 5))

    # B-17: the plan covers 14 days; a row 15 days away is in the text of the last planned day only
    far_egg = [_item(1, "egg", content, 1, "pcs", "fridge", D("2026-05-03"))]
    c.eq("B-17 a row 15 days away: one request, on day 13", digest_schedule(far_egg, t, 540),
         [("digest-2026-05-01", "Use these first", "Close to its date: Eggs.")])

    # B-18: the last second of April counts April of this year only; used on the last day counts as in time
    now_end_ = datetime(2026, 4, 30, 23, 59, 59)
    ev_end_ = [("used", 0, datetime(2026, 4, 1, 0, 0, 0)), ("used", 1, datetime(2025, 4, 15, 10, 0, 0)), ("thrownAway", -1, datetime(2025, 4, 15, 11, 0, 0)),
               ("thrownAway", 5, datetime(2026, 4, 30, 23, 59, 0)), ("used", -1, datetime(2026, 4, 12, 9, 0, 0)), ("used", 2, datetime(2026, 3, 31, 23, 59, 59))]
    c.eq("B-18 the last second of April", tally(ev_end_, now_end_), (1, 1))

    # B-21: three rescued ingredients are named as two and "1 more"
    rescue_rows_ = [replace(r, expiry=t + timedelta(days=1)) if r.ingredient in ("pasta", "tomato", "garlic") else r for r in kit["K5"]]
    cn_ = cook_next(suggestions(content, rescue_rows_, t))
    c.eq("B-21 cook next with three rescued ingredients", (cn_.recipe.id, cook_next_line(content, cn_)), ("tomato-pasta", "Uses your pasta, tomatoes and 1 more"))

    # B-16: four servings of a three-serving recipe propose 533 g; rows with one expiry go by addedAt before id; presence takes the soonest row
    four_ = replace(pasta, lines=(L("tomato", 400, "g"),))
    row600_ = [_item(1, "tomato", content, 600, "g", "fridge", D("2026-05-20"))]
    props_ = propose_deductions(content, four_, 4, {}, row600_, t)
    c.eq("B-16 four servings: 533 g are proposed, not 533.33 g", [(p.amount, p.stock) for p in props_], [(F(533), F(600))])
    after_, ev_ = apply_deductions(row600_, props_, [], t)
    c.eq("B-16 four servings: 67 g are left and the starting quantity is unchanged", [(r.qty, r.start) for r in after_], [(F(67), F(600))])
    one_line_ = replace(pasta, lines=(L("tomato", 300, "g"),))
    tie_x_ = replace(_item(22, "tomato", content, 200, "g", "fridge", D("2026-04-20")), added=3)
    tie_y_ = replace(_item(21, "tomato", content, 250, "g", "fridge", D("2026-04-20")), added=9)
    props_ = propose_deductions(content, one_line_, 3, {}, [tie_y_, tie_x_], t)
    after_, ev_ = apply_deductions([tie_y_, tie_x_], props_, [], t)
    c.eq("B-16 one expiry: the earlier addedAt is used first, although its id is larger", ([(r.id[-2:], r.qty) for r in after_], [(e.qty, e.unit) for e in ev_]),
         ([("21", F(150))], [(F(200), "g")]))
    garlic_rows_ = [_item(4, "garlic", content, 1, "pcs", "pantry", D("2026-05-18")), _item(14, "garlic", content, 1, "pcs", "pantry", D("2026-05-08")),
                    _item(3, "garlic", content, 3, "pcs", "pantry", D("2026-04-17"))]
    rows_ = [r for r in kit["K7"] if r.ingredient != "garlic"] + garlic_rows_
    props_ = propose_deductions(content, pasta, 3, {}, rows_, t)
    gp_ = next(p for p in props_ if p.kind == "presence")
    c.eq("B-16 presence: the row that expires first is offered", gp_.row, garlic_rows_[1].id)
    c.eq("B-16 presence: an expired row is not in the stock line", stock_line(gp_, rows_, t), "You have 2 pcs")

    # B-22: fractional seconds, long durations, and a timer that ends exactly now
    c.eq("B-22 0.75 s left reads one second", timer_label(start_timer(1000, 480), F("1479.25")), "00:01 left")
    c.eq("B-22 379.5 s left reads 06:20", timer_label(start_timer(1000, 480), F("1100.5")), "06:20 left")
    c.eq("B-22 an hour and a half", timer_label(start_timer(0, 5400), 0), "1:30:00 left")
    c.eq("B-22 two hours", timer_label(start_timer(0, 7200), 0), "2:00:00 left")
    c.eq("B-22 a timer that ends exactly now does not keep the session", session_discarded(0, -7 * 3600, [Timer(0, 1, 0)]), True)
    c.raises("B-22 alarm plan: a permission word outside the list is refused", lambda: alarm_plan([], F(0), [], "maybe"), ValueError)

    # B-23: a swapped line is never in the share text
    c.eq("B-23 a swapped line is not listed", share_text(content, pasta, 3, ["have", "swap", "have", "have", "missingOptional", "have", "have"]),
         "For Tomato Pasta (3 servings):\n• Basil — 10 g (optional)")
    c.eq("B-23 nothing but a swapped line: nothing to share", share_text(content, pasta, 3, ["have", "swap"] + ["have"] * 5), None)

    # B-08 and B-09 on C3 (the recipes and rows are in the generated tables of TESTING.md)
    c3_, c3n_ = build_c3(), build_c3(False)

    def c3row_(n, ing, qty, unit, expiry="2026-06-01"):
        return _item(n, ing, c3_, qty, unit, c3_.ings[ing].zone, D(expiry))
    pantry3_ = [c3row_(1, "pasta", 500, "g"), c3row_(2, "salt", 500, "g")]

    def c3shape(cont, rid_, rows_):
        m_ = match_recipe(cont, next(r for r in cont.recipes if r.id == rid_), 2, rows_, t)
        return m_.tier, [s_ if sub_ is None else "swap:%s" % sub_ for s_, sub_ in m_.status], len(m_.rescue), status_line(cont, m_)
    c.eq("B-08 C3 two lines swapped to one use-first vinegar: it is rescued once",
         c3shape(c3_, "sour-pasta", pantry3_ + [c3row_(3, "vinegar", 250, "ml", "2026-04-19")]),
         ("smartSwap", ["have", "swap:vinegar", "swap:vinegar", "have"], 1, "Swap: lemons → white vinegar, limes → white vinegar"))
    c.eq("B-08 C3 an expired row does not make the pasta use-first; the fresh row has the line",
         c3shape(c3_, "plain-pasta", [c3row_(1, "pasta", 500, "g", "2026-04-17"), c3row_(4, "pasta", 500, "g")] + pantry3_[1:]),
         ("readyNow", ["have", "have"], 0, "All ingredients available"))
    c.eq("B-08 C3 without factors the first member (vinegar) is skipped and the second (lemon) is offered",
         c3shape(c3n_, "lime-pasta", pantry3_ + [c3row_(3, "lemon", 2, "pcs")]), ("smartSwap", ["have", "swap:lemon", "have"], 0, "Swap: limes → lemons"))
    c.eq("B-09 C3 titles are compared in lower case, and a missing optional line counts as a missing line",
         [m.recipe.id for m in suggestions(c3_, pantry3_, t)],
         ["fresh-pasta", "plain-pasta", "herb-pasta", "lemon-pasta", "lime-pasta", "garlic-pasta", "sour-pasta"])
    c.eq("B-09 C3 Almost Ready comes before Smart Swap",
         [m.recipe.id for m in suggestions(c3_, pantry3_ + [c3row_(3, "vinegar", 250, "ml")], t)],
         ["fresh-pasta", "plain-pasta", "herb-pasta", "garlic-pasta", "lemon-pasta", "lime-pasta", "sour-pasta"])

    # B-26 the event log: the closed list, the date text, the lines
    c.eq("B-26 the closed list has 21 event codes", len(EVENT_CODES), 21)
    c.eq("B-26 event codes are unique", len(set(EVENT_CODE_NAMES)), len(EVENT_CODE_NAMES))
    c.eq("B-26 event codes are lowercase words joined by dots", all(re.fullmatch(r"[a-z]+(\.[a-z]+)+", n_) is not None for n_ in EVENT_CODE_NAMES), True)
    for epoch_, want_ in [(0, "1970-01-01T00:00:00Z"), (86399, "1970-01-01T23:59:59Z"), (951782400, "2000-02-29T00:00:00Z"),
                          (1709164800, "2024-02-29T00:00:00Z"), (1776504067, "2026-04-18T09:21:07Z"), (4107542399, "2100-02-28T23:59:59Z"),
                          (4107542400, "2100-03-01T00:00:00Z"), (253402300799, "9999-12-31T23:59:59Z"), (-1, "unknown"),
                          (253402300800, "unknown")]:
        c.eq("B-26 date text of %d" % epoch_, utc_text(epoch_), want_)
    c.eq("B-26 detail keeps letters, digits and . _ : = -", detail_text("NSCocoaErrorDomain:134030"), "NSCocoaErrorDomain:134030")
    c.eq("B-26 detail: a space and a line feed become one - each", detail_text("a b\nc"), "a-b-c")
    c.eq("B-26 detail: a letter with an accent is one scalar and becomes one -", detail_text("café"), "caf-")
    c.eq("B-26 detail: a bar cannot enter a line", detail_text("a|b"), "a-b")
    c.eq("B-26 detail is cut at 64 scalars", len(detail_text("x" * 100)), 64)
    c.eq("B-26 an event line", event_line(1776504067, "alarm.schedule", "ok"), "2026-04-18T09:21:07Z alarm.schedule ok")
    c.eq("B-26 an event line without a detail has no space at its end", event_line(1776504067, "app.launch"), "2026-04-18T09:21:07Z app.launch")
    c.eq("B-26 an event line with a cleaned detail", event_line(1776504067, "cook.finish", "used=7"), "2026-04-18T09:21:07Z cook.finish used=7")
    c.eq("B-26 a code outside the list is not written", event_line(1776504067, "cook.explode"), None)
    c.eq("B-26 a date outside the range reads unknown", event_line(-1, "app.launch"), "unknown app.launch")
    c.eq("B-26 the log keeps its newest lines", log_keep(["a", "b", "c", "d", "e"], 3), ["c", "d", "e"])
    c.eq("B-26 a short log is kept whole", log_keep(["a", "b"], 3), ["a", "b"])
    c.eq("B-26 the log of the phone keeps 200 lines", (len(log_keep(["l%d" % k for k in range(250)])), log_keep(["l%d" % k for k in range(250)])[0]), (200, "l50"))

    # B-25 the problem report: the facts, the limits, the attachment
    c.eq("B-25 a fact: control characters become spaces, the ends are trimmed", fact_text("  iPhone\t16 \n"), "iPhone 16")
    c.eq("B-25 an empty fact reads unknown", [fact_text(""), fact_text(None), fact_text("   ")], ["unknown"] * 3)
    c.eq("B-25 a fact is cut at 60 scalars", len(fact_text("x" * 100)), 60)
    c.eq("B-25 the note: CRLF is one line end, the ends are trimmed", note_text("  hello\r\nworld \r\n"), "hello\nworld")
    c.eq("B-25 an empty note reads none", [note_text(""), note_text(None), note_text("\r"), note_text(" \t\n ")], ["none"] * 4)
    c.eq("B-25 the note is cut at 500 scalars", len(note_text("y" * 600)), 500)
    for sizes_, limit_, want_ in [([], 100, ("none", 0, 0)), ([100], 100, ("included", 1, 100)), ([101], 100, ("too-large", 0, 0)),
                                  ([60, 40, 30], 100, ("included", 2, 100)), ([60, 50, 10], 100, ("included", 1, 60)),
                                  ([0], 0, ("included", 1, 0)), ([200000, 62144, 1], REPORT_ATTACHMENT_MAX_BYTES, ("included", 2, 262144))]:
        c.eq("B-25 attachment %r within %d" % (sizes_, limit_), attachment_plan(sizes_, limit_), want_)
    c.eq("B-25 the limit is 256 KiB", REPORT_ATTACHMENT_MAX_BYTES, 256 * 1024)
    c.eq("B-25 the full example report", build_report(REPORT_EXAMPLE), "\n".join([
        "FOODSAFE-REPORT 1", "App: 1.0.0 (57)", "Channel: testflight", "Device: iPhone16,2", "System: iOS 26.1 (23B85)", "Calendar: gregorian",
        "Time zone: UTC+01:00", "Notifications: authorized", "Alarms: denied", "Reminder: on 18:00", "Text size: large", "Reduce Motion: off",
        "Low Power Mode: on", "Storage free: 812 MB", "Items: 23", "Diagnostics: included (2 files, 27432 bytes)", "Events: 3",
        "2026-04-18T09:21:07Z app.launch", "2026-04-18T09:21:09Z alarm.auth denied", "2026-04-18T09:22:31Z timer.finish 2",
        "Note: The timer did not ring."]))
    c.eq("B-25 the empty record: every fact reads unknown", build_report({}), "\n".join([
        "FOODSAFE-REPORT 1", "App: unknown (unknown)", "Channel: unknown", "Device: unknown", "System: iOS unknown (unknown)", "Calendar: unknown",
        "Time zone: unknown", "Notifications: unknown", "Alarms: unknown", "Reminder: off", "Text size: unknown", "Reduce Motion: unknown",
        "Low Power Mode: unknown", "Storage free: unknown", "Items: unknown", "Diagnostics: none", "Events: 0", "Note: none"]))
    many_ = ["2026-04-18T09:%02d:00Z app.launch" % k for k in range(55)]
    text_ = build_report(dict(REPORT_EXAMPLE, eventLines=many_)).split("\n")
    c.eq("B-25 55 event lines: the newest 40 are carried and the head says so", (text_[16], text_[17], text_[56], len(text_)),
         ("Events: 40 of 55", "2026-04-18T09:15:00Z app.launch", "2026-04-18T09:54:00Z app.launch", 58))
    c.eq("B-25 diagnostics that do not fit say so", build_report(dict(REPORT_EXAMPLE, diagnosticSizes=[300000, 10])).split("\n")[15],
         "Diagnostics: too large (300000 bytes)")
    c.eq("B-25 one file reads file, not files", build_report(dict(REPORT_EXAMPLE, diagnosticSizes=[5])).split("\n")[15], "Diagnostics: included (1 file, 5 bytes)")
    for extra_, line_, want_ in [({"tzOffsetMinutes": -210}, 6, "Time zone: UTC-03:30"), ({"tzOffsetMinutes": 345}, 6, "Time zone: UTC+05:45"),
                                 ({"tzOffsetMinutes": 0}, 6, "Time zone: UTC+00:00"), ({"tzOffsetMinutes": 841}, 6, "Time zone: unknown"),
                                 ({"reminderMinute": 0}, 9, "Reminder: on 00:00"), ({"reminderMinute": 1439}, 9, "Reminder: on 23:59"),
                                 ({"reminderMinute": 1440}, 9, "Reminder: unknown"), ({"reminderMinute": None}, 9, "Reminder: off"),
                                 ({"channel": "beta"}, 2, "Channel: unknown"), ({"notifications": "provisional"}, 7, "Notifications: unknown"),
                                 ({"items": True}, 14, "Items: unknown"), ({"items": -1}, 14, "Items: unknown"), ({"freeMB": 1.5}, 13, "Storage free: unknown"),
                                 ({"reduceMotion": True}, 11, "Reduce Motion: on")]:
        c.eq("B-25 %r" % extra_, build_report(dict(REPORT_EXAMPLE, **extra_)).split("\n")[line_], want_)
    return c.n
