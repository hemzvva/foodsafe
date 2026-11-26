    def ident(i):
        return "none" if i is None else short.get(i, i)

    def step_text(s):
        if s[0] == "request":
            return "request the permission"
        if s[0] == "cancel":
            return "cancel %s" % ident(s[1])
        if s[0] == "forget":
            return "forget the alarm id of step %d" % s[1]
        return "schedule step %d at %s: %s" % (s[1], dec(s[2]), s[3])

    out = [ALARM_BEGIN, "",
           "Times are epoch seconds. Alarm ids are written A1 = `%s`, A2 = `%s` and A9 = `%s`. A plan lists its calls in the order they are made; `-` is an empty list." % (_A1, _A2, _A9), "",
           "| # | Case | Now | Running timers: step, endsAt, alarm id | System alarms: id, fire date | Permission | Plan |",
           "|---|---|---|---|---|---|---|"]
    for n, (name, now_, timers_, system_, auth_, _want) in enumerate(ALARM_CASES, 1):
        t_text = "<br>".join("step %d, %s, %s" % (x.step, dec(x.ends), ident(x.alarm)) for x in timers_) or "-"
        s_text = "<br>".join("%s, %s" % (ident(a.id), "no fixed date" if a.fire is None else dec(a.fire)) for a in system_) or "-"
        p_text = "<br>".join("%d. %s" % (k, step_text(s)) for k, s in enumerate(alarm_plan(timers_, F(now_), system_, auth_), 1)) or "-"
        out.append("| %d | %s | %s | %s | %s | %s | %s |" % (n, name, dec(F(now_)), t_text, s_text, auth_, p_text))
    out += ["", "The title of an alarm is the step title, ` · `, the recipe title:", "",
            "| Step title | Recipe title | Alarm title |", "|---|---|---|"]
    for st_, rt_, want_ in ALARM_TITLE_CASES:
        out.append("| %s | %s | %s |" % (st_, rt_, want_))
    out += ["", ALARM_END]
    return "\n".join(out)
