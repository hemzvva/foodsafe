    for servings_, texts_ in want.items():
        c.eq("B-04 B-05 Tomato Pasta for %d servings" % servings_,
             [amount_text(scaled(ln.amount, servings_, pasta.base), ln.unit) for ln in pasta.lines], texts_)
    # B-04: multiply first, divide last; the amount that is written is the exact value rounded half up
    c.eq("B-04 10 g x 4 / 3 is 13.33 and is written 13 g", amount_text(scaled(F(10), 4, 3), "g"), "13 g")
    c.eq("B-04 the base servings change nothing", scaled(F("3.25"), 3, 3), F("3.25"))
    c.eq("B-04 one serving of three is a third", scaled(F(300), 1, 3), F(100))
    # B-05: a tie goes up at the last digit that is written (computed by hand, one case for each unit)
    for v_, unit_, want_ in [("3.25", "g", "3.3 g"), ("0.25", "g", "0.3 g"), ("9.95", "g", "10 g"), ("9.94", "g", "9.9 g"),
                             ("10.5", "g", "11 g"), ("10.4", "g", "10 g"), ("0.05", "g", "0.1 g"), ("250", "ml", "250 ml"),
                             ("0.125", "L", "0.13 L"), ("0.97", "L", "0.97 L"), ("1", "L", "1 L"), ("1.25", "pcs", "1.5 pcs"),
                             ("2.25", "pcs", "2.5 pcs"), ("2.75", "pcs", "3 pcs"), ("2.24", "pcs", "2 pcs"), ("2.5", "cloves", "2.5 cloves")]:
        c.eq("B-05 %s %s" % (v_, unit_), amount_text(F(v_), unit_), want_)
    c.eq("B-05 3.25 g x 3 / 3 is exactly 3.25, a tie, and goes up (dividing first would give 3.2 g)", amount_text(scaled(F("3.25"), 3, 3), "g"), "3.3 g")
    c.eq("B-05 the decimal text of a short fraction", [dec(F(5, 4)), dec(F(7)), dec(F(1, 8)), dec(F(-1, 2))], ["1.25", "7", "0.125", "-0.5"])
    c.raises("B-05 a third is not a short decimal", lambda: dec(F(1, 3)), ValueError)

    # B-06
    c.eq("B-06 grams and millilitres are not comparable", comparable("g", "ml"), False)
    c.eq("B-06 millilitres and litres are", comparable("ml", "L"), True)
    c.eq("B-06 pieces and cloves are not", comparable("pcs", "cloves"), False)
    c.eq("B-06 1 L is 1000 ml", convert(F(1), "L", "ml"), F(1000))
    c.eq("B-06 250 ml is 0.25 L", convert(F(250), "ml", "L"), F(1, 4))
    c.raises("B-06 grams to millilitres is refused", lambda: convert(F(1), "g", "ml"), AssertionError)

    # B-07: the line is tomatoes 400 g of a recipe for 3 servings (computed by hand; 400 x 4 / 3 = 533.33 is written 533 g)
    def tomato_row(n, q, u, exp="2026-04-25"):
        return _item(60 + n, "tomato", content, q, u, "fridge", D(exp))
    custom_tomatoes_ = Item("00000000-0000-4000-8000-000000000098", None, "Tomatoes", F(500), F(500), "g", "fridge", D("2026-04-25"), 98)
    for label_, rows_, servings_, want_ in [
            ("450 g, 3 servings: 400 g are needed", [tomato_row(1, 450, "g")], 3, True),
            ("450 g, 4 servings: 533 g are needed", [tomato_row(1, 450, "g")], 4, False),
            ("533 g, 4 servings: exactly what is written", [tomato_row(1, 533, "g")], 4, True),
            ("532 g, 4 servings: one gram short", [tomato_row(1, 532, "g")], 4, False),
            ("two rows, 200 g and 250 g, add up", [tomato_row(1, 200, "g"), tomato_row(2, 250, "g")], 3, True),
            ("a row that expired yesterday does not count", [tomato_row(1, 450, "g", "2026-04-17")], 3, False),
            ("a row that expires today counts", [tomato_row(1, 450, "g", "2026-04-18")], 3, True),
            ("a row in pieces makes the line present", [tomato_row(1, 2, "pcs")], 3, True),
            ("100 g and 2 pcs: the row in another kind makes the line present", [tomato_row(1, 100, "g"), tomato_row(2, 2, "pcs")], 3, True),
            ("a custom row named Tomatoes is not the ingredient", [custom_tomatoes_], 3, False),
            ("no row", [], 3, False)]:
        c.eq("B-07 " + label_, available("tomato", scaled(F(400), servings_, 3), "g", rows_, t), want_)
    c.eq("B-07 450.01 g is written 450 g, so 450 g in stock is enough", available("tomato", F("450.01"), "g", kit["K7"], t), True)
    c.eq("B-07 1001 ml against 1 L: 1000 ml are short", available("olive-oil", F(1001), "ml", kit["K7"], t), False)
    c.eq("B-07 1000 ml against 1 L is enough", available("olive-oil", F(1000), "ml", kit["K7"], t), True)
    c.eq("B-07 garlic in pieces answers a line in cloves", available("garlic", F(2), "cloves", kit["K7"], t), True)
    c.eq("B-07 no chicken in K6", available("chicken", F(200), "g", kit["K6"], t), False)

    # B-08 on the kitchens (computed by hand from the recipes and rows of C1; a swap is written swap:<ingredient>)
    def shape(m_):
        return m_.tier, [s_ if sub_ is None else "swap:%s" % sub_ for s_, sub_ in m_.status], status_line(content, m_)

    def match_of(kname_, rid_, servings_=None):
        r_ = next(x for x in content.recipes if x.id == rid_)
        return match_recipe(content, r_, servings_ or r_.base, kit[kname_], t)
    for kname_, rid_, want_ in [
            ("K5", "tomato-pasta", ("readyNow", ["have"] * 7, "All ingredients available")),
            ("K5", "chicken-stir-fry", ("readyNow", ["have"] * 5 + ["missingOptional"], "Missing: soy sauce (optional)")),
            ("K5", "vegetable-curry", (None, ["missing", "have", "missing", "have", "missingOptional"], "Missing: potatoes, onion")),
            ("K5", "lentil-soup", (None, ["have", "missing", "missing", "missing", "have", "have"], "Missing: onion, carrots, vegetable broth")),
            ("K6", "tomato-pasta", (None, ["missing"] * 4 + ["missingOptional", "have", "have"], "Missing: pasta, tomatoes, olive oil and 1 more")),
            ("K6", "chicken-stir-fry", (None, ["swap:lentil"] + ["missing"] * 4 + ["missingOptional"], "Missing: rice, broccoli, garlic and 1 more")),
            ("K6", "vegetable-curry", (None, ["missing", "missing", "have", "missing", "missingOptional"], "Missing: potatoes, tomatoes, garlic")),
            ("K6", "lentil-soup", ("smartSwap", ["swap:lentil"] + ["have"] * 5, "Swap: chicken breast → lentils")),
            ("K7", "tomato-pasta", ("readyNow", ["have"] * 7, "All ingredients available")),
            ("K7", "chicken-stir-fry", (None, ["missing"] * 3 + ["have", "have", "missingOptional"], "Missing: chicken breast, rice, broccoli")),
            ("K7", "vegetable-curry", (None, ["missing", "have", "missing", "have", "missingOptional"], "Missing: potatoes, onion")),
            ("K7", "lentil-soup", (None, ["missing"] * 4 + ["have", "have"], "Missing: chicken breast, onion, carrots and 1 more")),
            ("K8", "tomato-pasta", ("almostReady", ["have"] * 4 + ["missingOptional", "have", "missing"], "Missing: pepper, basil (optional)")),
            ("K8", "chicken-stir-fry", ("readyNow", ["have"] * 5 + ["missingOptional"], "Missing: soy sauce (optional)"))]:
        c.eq("B-08 %s %s" % (kname_, rid_), shape(match_of(kname_, rid_)), want_)
    c.eq("B-08 K5 tomato pasta for 4 servings: 533 g of tomatoes are not there", shape(match_of("K5", "tomato-pasta", 4)),
         ("almostReady", ["have", "missing"] + ["have"] * 5, "Missing: tomatoes"))
    c.eq("B-08 K5 tomato pasta for 2 servings", match_of("K5", "tomato-pasta", 2).tier, "readyNow")
    c.eq("B-08 an optional line never changes the tier (D-X-69)", (match_of("K8", "chicken-stir-fry").tier, match_of("K8", "chicken-stir-fry").n_optional), ("readyNow", 1))
    c.eq("B-08 one missing required line is Almost Ready, two are not", (match_of("K8", "tomato-pasta").n_missing, match_of("K5", "vegetable-curry").n_missing),
         (1, 2))
    lentil_soup = next(r for r in content.recipes if r.id == "lentil-soup")

