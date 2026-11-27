# FoodSafe Build Kit: state at the moment the workspace was lost

Written after the sandbox reset. It is the one file to read to continue the work. Everything here comes from the session summary; nothing in it was re-verified after the loss.

## 1. What the project is
FoodSafe: a 13-screen iPhone app (from the owner's mockup). The deliverable is ONE zip, "FoodSafe Build Kit", for an AI coding agent (OpenCode). The agent only codes; the kit holds every decision, spec, task card and prompt. A short master prompt is delivered in chat, outside the zip.

Surviving inputs (in this repo): `FoodSafe-Project/` (design package of Oct 25, 211 files) and `reference-attachments/` (design.md, three text files, the mockup PNG). Published pages: "FoodSafe UI Replica Spec" and "FoodSafe Replica Check".

## 2. Owner rules (all still in force)
- No sub-agents; do the work directly.
- No dates, deadlines or time pressure in the kit. No size limit. Include everything, no compressing.
- Be precise and fact-checked. Mark anything unverified as "confirm". Do not invent.
- Brief: preserve the mockup's visual identity but treat it as a reference; architecture, tabs, hierarchy, button placement, functionality and interactions may be improved. Aim for Apple Design Award craft: intuitive, distinctive, fun, meaningful animation. Think critically; no roleplay.
- Production art must never be pasted crops of the mockup.
- Never write the owner's e-mail, finances, country or other personal details into the kit. The support address is a build variable `FS_SUPPORT_EMAIL`.
- The owner's Mac is a 2015 MacBook Air and cannot run current Xcode. Builds run on a GitHub Actions macOS runner.
- Terse, direct, honest communication. Push every stage to this repo and send a zip.

## 3. Decisions in force
iPhone only; iOS 26.1 minimum; portrait; light only; English only; free; no network, accounts or third-party code. SwiftUI + SwiftData; AlarmKit for timers; UserNotifications for one daily digest only; XcodeGen; Swift 6 with zero warnings. Banned: `DispatchQueue.main.async`, `Task.detached`.
Layers: `FoodSafeCore <- Data <- Services <- Features <- App`.
Three tabs: Home, Inventory, Recipes. Settings is a gear sheet.
Surfaces: S-01 Welcome, S-14 Starter picker, S-02 Home, S-17 This-month card, S-04 Inventory, S-03 Item sheet, S-15 Add picker, S-12 Use First, S-05 Recipe suggestions, S-06 Recipe detail, S-08 Servings, S-09 Swaps, S-07 Cooking, S-16 Cook-complete, S-13 Settings, S-18 Data problem, S-19 Report a problem.
Features: about 30 recipes with step-by-step cooking and real timers/alarms; cook-and-deduct from stock; used/thrown-away log; starter picker; optional daily reminder; accessible text colours and Dynamic Type; Apple-only diagnostics; user-sent problem report; privacy label answers. Removed as valueless: Offline Mode toggle, sign-in, export/import, timer pause, use-by/best-before switch.
Other calls: optional ingredients never change a recipe's tier (D-X-69); report retention 90 days; attachment limit 256 KiB; empty values read `unknown`.

## 4. Rule semantics to re-derive (B-01..B-27)
Key ones: B-08 per recipe line: available -> have; else optional -> missingOptional; else first available cluster member (authored order, skip self, skip members with no swap factor) -> swap; else missing. Tier is computed over required lines only. B-09 sort key: tier, more rescued ingredients, fewer missing, minutes, lower-case title, id. B-16 cook-and-deduct: proposals use the amount shown on screen; deduct from the soonest-to-expire row (ties by addedAt then id); starting quantity never changes; zero removes the row. B-17 digest covers 14 days; a row is listed on days where days-left is 0..2. B-18 monthly tally by calendar month and year. B-22 timer label rounds seconds up. B-24 steppers have a smallest step per unit. B-27 catalog search: starts-with, then contains, then alias-contains.
Conventions: value types, no decimal literals with a point, one rounding helper (half up), no clock or locale reads inside Core, total orderings, no traps.

## 5. Planned kit layout
00-READ-FIRST, 01-PRODUCT (surface specs, business rules, data model, decisions, recipe content spec), 02-DESIGN (design system, motion, art brief), 03-ENGINEERING (architecture, Core API, testing, field quality, coding standards, accessibility, performance), 04-APP-STORE, 05-PLAN (plan + 33 task cards T-00..T-26 with sub-cards), 06-PROMPTS (master, phase prompts, reviewers), tools (rule oracle, test vectors, mutation check, fact-check scripts), `design-package/`.

## 6. Progress at the time of loss
Done: toolchain; mockup segmentation; per-screen docs; cross-screen docs; information architecture and surface specs; rules/data-model/decisions update; platform facts; rule oracle with 571 hand-checked cases; test vectors; mutation tool (144 mistakes, all caught); task cards T-00, T-01, T-02, T-03, T-03b, T-03c.
Not started or unfinished: task cards T-04..T-26 (T-09, T-10, T-10b next); mission, ground rules, glossary; owner setup guide; root README/AGENTS.md/opencode.json; motion and delight docs; contrast audit, art brief, style lock; accessibility, coding standards, performance, slop-prevention, research basis; App Store docs; planning working files; prompts; lint/check tools; final review, zip and master prompt.

## 7. Simplified rebuild order (each stage: commit, push, send zip)
1. Core: rules + oracle + vectors + mutation check; task cards T-09, T-10, T-10b.
2. Product: business rules, data model, surface specs, recipe content spec.
3. Plan: task cards T-04..T-26, PLAN, AGENTS.md, opencode.json, README.
4. Engineering and design docs (architecture, testing, motion, accessibility, coding standards).
5. App Store docs and owner guide.
6. Prompts, checks, final zip, master prompt.
Keep it lean: one precise doc per topic, no duplicated rules, every id defined once.

## 8. Added after the rebuild began (read this too)
Owner messages received during the rebuild, in force:
- "recheck every prompt i sent u beside the continuation messages for any rules and other stuff i told u, mark them intelligently into a file in github" -> write `OWNER-RULES.md` (repo root). The earliest prompts no longer exist verbatim; the ledger is rebuilt from notes, summaries, memory and this repo, and says so.
- The owner attached a zip, "test_for_foodsafe.zip", made on another iOS app-builder platform: "i liked the things it generated so much, learn from it, use it if u can or want". It is mostly ART (22 watercolor dish illustrations, 64 transparent cutouts, a paper texture) plus 7 text files of SwiftUI/Python code (sketch UI shapes, a drawn icon set, ingredient catalog, 22 recipes, swap groups, SwiftData models, an art-generation script). Unzipped copy: `reference-attachments/test-for-foodsafe/`. Review notes: `_rebuild/review/`.
- The owner wants a variety of fonts, not one: Patrick Hand Regular, Caveat Brush Regular, Kalam Regular, Kalam Light, Kalam Bold. Fetched from Google's font repository (SIL OFL 1.1, embedding allowed) into `FoodSafe-Build-Kit/assets/fonts/` with licences; facts in `_rebuild/review/fonts/probe.json`. The mockup font (Purisa) is replaced.
- "upload everything into github, with zip unzipped, and push everything u made": every zip that is received or built also lives unzipped in this repo. Push after every finished group.
- "resume with doubt driven development for better quality content": write each doubt before the claim, give it a test (run it, read a primary source, compile it) or mark the claim `confirm`, and log it in `DOUBT-LOG.md` (repo root). Distilled results go to the kit's facts file.
State: Stage 0 done and pushed. Stage 1 (rules oracle) has its segments in `_rebuild/segs/` (not yet stitched or run). Tasks #66 (rules ledger) and #67 (test-app and fonts review) are in progress. The kit has no zip yet.
