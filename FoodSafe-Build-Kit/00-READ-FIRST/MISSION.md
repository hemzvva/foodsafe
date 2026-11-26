# FoodSafe: mission

## What you are building

FoodSafe is a free iPhone app that answers one question: what can I cook with what I have, and what should I use up first?

The user keeps a list of what is in their fridge, pantry and freezer. The app shows what is about to expire, suggests recipes from that stock (ready now, almost ready, ready with a swap), walks the user through cooking with real timers and alarms, takes the used ingredients out of the stock when the user finishes, and keeps a small log of food used in time versus thrown away. Everything runs on the phone. There is no account, no server, no network use and no third-party code.

The owner drew a 13-screen mockup: hand-drawn paper look, one handwritten typeface, warm cream with green and terracotta. It is in `design-package/`. It is the visual identity of the app and a reference for the experience. It is not a specification. The documents in this kit decide structure and behaviour.

## Who does what

- **The owner** is the product director. The owner sets the vision, makes design and product calls, and does not write code. The owner holds the Apple developer account and the signing secrets.
- **You** (OpenCode) write all the code, tests and project files from this kit. You never need the owner's Mac: it cannot run current Xcode, so every build runs on a GitHub Actions macOS runner (`03-ENGINEERING/BUILD-ENVIRONMENT.md`).
- **This kit** holds every decision. A task card says what to build, which documents to read, which tests must pass and what not to do. Nothing the kit already decides is left for you to guess.

## The owner's brief (verbatim)

> Understand the product, the materials I provided, and the experience I'm aiming for before making decisions. Think critically, weigh alternatives, and challenge weak choices rather than blindly following instructions. No fictional debates or roleplay. Preserve the mockup's visual identity and design language. However, treat it as a reference, not an untouchable specification. Everything beyond its visual design should be open to improvement: code architecture, navigation and tabs, page hierarchy and structure, button placement, functionality, and interactions. Make independent decisions where they lead to a better product. The result should feel like a cohesive, carefully architected indie app, built by someone with years of product experience. Make it intuitive, distinctive, fun, emotionally engaging, and interactive, with meaningful animations, thoughtful transitions, and delightful details. Aim for the level of craftsmanship and attention to detail worthy of an Apple Design Award.

How this brief applies to you:

- The kit already improved on the mockup (for example three tabs instead of five, cook-and-deduct, a used/thrown-away log). Those calls are written down with their reasons. Read the reasons before you judge them.
- You may challenge any decision. Write the challenge in `05-PLAN/QUESTIONS.md`: the decision id, what is weak about it, the alternative, the evidence. Keep building the documented default while the challenge is open. When the alternative is clearly better, change it in the same commit as every document, test and fixture that the change touches, and log the call. Never leave the kit and the code disagreeing.
- Rules with numbers in them (the business rules) have a single source of truth: the Python oracle in `tools/rules_reference.py` and its vectors. You change a rule by changing the oracle and the vectors first, then the Swift.
- Do not role-play or stage debates. Decide, write down why in one paragraph, and move on.

## What done means

1. Every control on every surface does what its label says, on real data. No inert buttons, no placeholder handlers, no screens that only look right.
2. The app is alive: about 30 recipes with step-by-step cooking, real timers that survive the app being closed, an inventory that really changes when the user cooks, a starter list so the first launch is never empty.
3. The rules pass the oracle vectors, all tests pass, and the code compiles under Swift 6 with zero warnings.
4. All art is original production art in the mockup's style. A crop of the mockup is never production art.
5. Accessibility is built in: Dynamic Type, VoiceOver, accessible text colours, Reduce Motion.
6. The App Store pack is complete. The owner only presses the final buttons.
7. The app feels like one coherent indie product: meaningful motion, small moments of delight, no template look.

## Hard limits (they never bend)

- iPhone only, portrait, light appearance, English only, free, no ads.
- No network use, no accounts, no analytics, no third-party code in the app.
- No photography anywhere. Illustration only.
- Never write the owner's e-mail address, finances, country or any other personal detail into any file. The support address is the build variable `FS_SUPPORT_EMAIL`.
- Anything this kit marks `confirm` is unverified. Verify it from a primary source before you rely on it, and record what you found. Do not guess.

## What the kit does not contain

The Xcode project (XcodeGen generates it from `project.yml`), the final production art, signing certificates and keys, and the Apple developer account. The owner supplies the last two; the art and the project are tasks in `05-PLAN/`.

## Where to go next

`../AGENTS.md` for the working rules, then `05-PLAN/PLAN.md` for the order of the task cards.
