PERMISSION_WORDS = ("authorized", "denied", "notDetermined")  # the three states of a system permission (alarms, notifications)


def alarm_title(step_title: str, recipe_title: str) -> str:
    """The title of the system alarm of a timed step: the step, a middle dot, the recipe."""
    return "%s · %s" % (step_title, recipe_title)


def alarm_plan(timers: List[AlarmTimer], now: F, system: List[SysAlarm], authorization: str) -> List[tuple]:
    """B-22: the calls that make the system's set of alarms equal the set of running timers. The plan is a list of steps, always in
    this order: ("request",); ("cancel", id) by id; ("forget", stepPosition) by step; ("schedule", stepPosition, fireDate, title) by step.

    A timer is running when endsAt is after now, finished otherwise. A timer owns the alarm its alarmId names when the system has that
    alarm and no timer with a lower step position owns it already.
    - A running timer whose owned alarm has a fixed fire date less than ALARM_SYNC_TOLERANCE_SECONDS from endsAt needs no call. Any
      other running timer gets its owned alarm (if it has one) cancelled and, unless authorization is `denied`, a new alarm scheduled
      at endsAt; when authorization is `denied`, the alarmId it carries is forgotten.
    - A finished timer keeps the alarm it owns (the alarm is alerting or about to); an alarmId that names no alarm is forgotten.
    - Every system alarm that no timer owns is cancelled.
    - `request` comes first when authorization is `notDetermined` and at least one schedule is planned. The caller drops every
      schedule when the answer is not `authorized`, and forgets the alarmId of those timers.
    The plan performs no call itself; the schedule step carries the step position so that the new alarm id can be stored."""
    if authorization not in PERMISSION_WORDS:
        raise ValueError(authorization)
    by_id = {a.id: a for a in system}
    owned: set = set()
    cancels: set = set()
    forgets: List[int] = []
    schedules: List[tuple] = []
    for tm in sorted(timers, key=lambda x: x.step):
        alarm = None
        if tm.alarm is not None and tm.alarm not in owned and tm.alarm in by_id:
            owned.add(tm.alarm)
            alarm = by_id[tm.alarm]
        if tm.ends <= now:
            if tm.alarm is not None and alarm is None:
                forgets.append(tm.step)
            continue
        if alarm is not None and alarm.fire is not None and abs(alarm.fire - tm.ends) < ALARM_SYNC_TOLERANCE_SECONDS:
            continue
        if alarm is not None:
            cancels.add(alarm.id)
        if authorization == "denied":
            if tm.alarm is not None:
                forgets.append(tm.step)
        else:
            schedules.append(("schedule", tm.step, tm.ends, tm.title))
    cancels |= {a.id for a in system if a.id not in owned}
    plan: List[tuple] = []
    if authorization == "notDetermined" and schedules:
        plan.append(("request",))
    plan += [("cancel", i) for i in sorted(cancels)]
    plan += [("forget", s) for s in sorted(forgets)]
    return plan + schedules


def _aid(n: int) -> str:
    return "00000000-0000-4000-9000-%012d" % n


_A1, _A2, _A9 = _aid(1), _aid(2), _aid(9)
_PASTA = alarm_title("Cook the pasta", "Tomato Pasta")
_SAUTE = alarm_title("Sauté", "Lentil Soup")
_LENTIL = alarm_title("Add lentils & broth", "Lentil Soup")


def _t(step: int, ends, alarm: Optional[str], title: str) -> AlarmTimer:
    return AlarmTimer(step, F(ends), alarm, title)


def _s(alarm_id: str, fire) -> SysAlarm:
    return SysAlarm(alarm_id, None if fire is None else F(fire))


# (name, now, running timers, system alarms, authorization, the plan): the plan is typed by hand, never taken from alarm_plan
ALARM_CASES = [
    ("nothing running and nothing scheduled", 1000, [], [], "authorized", []),
    ("a new timer gets an alarm at endsAt", 1000, [_t(2, 1480, None, _PASTA)], [], "authorized",
     [("schedule", 2, F(1480), _PASTA)]),
    ("an alarm at endsAt needs no call", 1000, [_t(2, 1480, _A1, _PASTA)], [_s(_A1, 1480)], "authorized", []),
    ("an alarm half a second off is in sync", 1000, [_t(2, 1480, _A1, _PASTA)], [_s(_A1, "1480.5")], "authorized", []),
    ("an alarm one second late is stale", 1000, [_t(2, 1480, _A1, _PASTA)], [_s(_A1, 1481)], "authorized",
     [("cancel", _A1), ("schedule", 2, F(1480), _PASTA)]),
    ("an alarm one second early is stale", 1000, [_t(2, 1480, _A1, _PASTA)], [_s(_A1, 1479)], "authorized",
     [("cancel", _A1), ("schedule", 2, F(1480), _PASTA)]),
    ("one minute added: the old alarm is replaced", 1258, [_t(2, 1540, _A1, _PASTA)], [_s(_A1, 1480)], "authorized",
     [("cancel", _A1), ("schedule", 2, F(1540), _PASTA)]),
    ("the alarm is gone from the system: scheduled again", 1000, [_t(2, 1480, _A1, _PASTA)], [], "authorized",
     [("schedule", 2, F(1480), _PASTA)]),
    ("an alarm without a fixed date is replaced", 1000, [_t(2, 1480, _A1, _PASTA)], [_s(_A1, None)], "authorized",
     [("cancel", _A1), ("schedule", 2, F(1480), _PASTA)]),
    ("an alarm that no timer names is cancelled", 1000, [], [_s(_A9, 2000)], "authorized", [("cancel", _A9)]),
    ("a finished timer whose alarm is gone forgets its alarm id", 1500, [_t(2, 1480, _A1, _PASTA)], [], "authorized",
     [("forget", 2)]),
    ("a finished timer whose alarm is still there is left alone", 1500, [_t(2, 1480, _A1, _PASTA)], [_s(_A1, 1480)], "authorized", []),
    ("a timer that ends exactly now is finished", 1480, [_t(2, 1480, None, _PASTA)], [], "authorized", []),
    ("a timer that ends exactly now with a lost alarm forgets its alarm id", 1480, [_t(2, 1480, _A1, _PASTA)], [], "authorized",
     [("forget", 2)]),
    ("half a second before the end the timer still runs", "1479.5", [_t(2, 1480, None, _PASTA)], [], "authorized",
     [("schedule", 2, F(1480), _PASTA)]),
    ("two timers: one in sync, one new", 1000, [_t(2, 1480, _A1, _PASTA), _t(5, 2200, None, _SAUTE)], [_s(_A1, 1480)], "authorized",
     [("schedule", 5, F(2200), _SAUTE)]),
    ("schedules are made in step order", 1000, [_t(5, 2200, None, _SAUTE), _t(2, 1480, None, _PASTA)], [], "authorized",
     [("schedule", 2, F(1480), _PASTA), ("schedule", 5, F(2200), _SAUTE)]),
    ("cancels by id come before schedules", 1000, [_t(1, 1300, None, _PASTA)], [_s(_A9, 5000), _s(_A2, 6000)], "authorized",
     [("cancel", _A2), ("cancel", _A9), ("schedule", 1, F(1300), _PASTA)]),
    ("two timers name one alarm: the lower step keeps it", 1000, [_t(2, 1480, _A1, _PASTA), _t(5, 2200, _A1, _SAUTE)], [_s(_A1, 1480)],
     "authorized", [("schedule", 5, F(2200), _SAUTE)]),
    ("a finished and a running timer, both alarms in sync", 1500, [_t(2, 1480, _A1, _PASTA), _t(5, 2200, _A2, _SAUTE)],
     [_s(_A1, 1480), _s(_A2, 2200)], "authorized", []),
    ("two timers of one recipe", 1000, [_t(2, 1300, None, _SAUTE), _t(3, 2800, None, _LENTIL)], [], "authorized",
     [("schedule", 2, F(1300), _SAUTE), ("schedule", 3, F(2800), _LENTIL)]),
    ("denied: nothing is scheduled", 1000, [_t(2, 1480, None, _PASTA)], [], "denied", []),
    ("denied: a stale alarm is cancelled and its alarm id forgotten", 1000, [_t(2, 1540, _A1, _PASTA)], [_s(_A1, 1480)], "denied",
     [("cancel", _A1), ("forget", 2)]),
    ("denied: cancels first, then forgets by step", 1000, [_t(5, 2200, _A2, _SAUTE), _t(2, 1540, _A1, _PASTA)],
     [_s(_A1, 1480), _s(_A9, 7000)], "denied", [("cancel", _A1), ("cancel", _A9), ("forget", 2), ("forget", 5)]),
    ("not asked yet: ask first, then schedule", 1000, [_t(2, 1480, None, _PASTA)], [], "notDetermined",
     [("request",), ("schedule", 2, F(1480), _PASTA)]),
    ("not asked yet and nothing to schedule: no question", 1000, [], [], "notDetermined", []),
    ("not asked yet and only a cancel: no question", 1000, [], [_s(_A9, 2000)], "notDetermined", [("cancel", _A9)]),
]

ALARM_TITLE_CASES = [
    ("Cook the pasta", "Tomato Pasta", "Cook the pasta · Tomato Pasta"),
    ("Sauté", "Lentil Soup", "Sauté · Lentil Soup"),
    ("Add lentils & broth", "Lentil Soup", "Add lentils & broth · Lentil Soup"),
    ("Simmer", "Vegetable Curry", "Simmer · Vegetable Curry"),
