FoodSafe: the complete build plan, A to Z
Status: plan only. No app code is written until you approve it.

How to read this: each part opens with a one-line summary in bold, then the details. Part 0 is the whole plan on one page.

Part 0. The whole plan on one page
What FoodSafe is: an offline iPhone app that keeps track of the food in your kitchen and tells you what you can cook with it right now, using up the food that expires soonest.

The loop the whole app serves:

You add groceries: what it is, how much, where it lives (pantry, fridge, freezer), when it expires.
The app shows what you have and what needs using soon.
The app matches your stock against a built-in recipe book and sorts recipes into three tiers: Ready Now, Almost Ready, Smart Swap.
You pick a recipe. It scales to the amount of food you actually have.
You cook step by step, with timers.
When you finish, the app takes what you used out of your inventory.
Suggestions update. Repeat.
What we build it with: native SwiftUI, data stored on the phone (SwiftData), no server, no account, no internet.

What it looks like: your mockup. Warm cream paper, deep green buttons, hand-printed lettering, watercolor food art, ink-drawn icons. Your mockup is the visual source of truth. The reference docs and ZIP fill in what the mockup doesn't show.

How we build it: 12 stages, from preparing assets to the final polish. Four of them end in a checkpoint where you look at the simulator and approve before I continue.

Part 1. What I received and what I'll use
In short: the ZIP art is excellent and becomes the base of the app's look. The ZIP code is a useful draft that I'll rewrite, not paste.

1.1 The ZIP (reference-attachments/test-for-foodsafe/)

What	How many	Quality	What I'll do
Watercolor dish paintings on wooden boards (960 x 717)	22	Very good, consistent, appetising	Use them as recipe art
Transparent ingredient cutouts (360 px)	56 + 1 empty jar	Good. The milk, mozzarella, tofu and empty jar are very pale	Use them. Regenerate the pale ones
Category subjects (broccoli bunch, apple, milk, wheat, beans, spice jar)	6	Good	Use for the category tiles
Spot art: copper pot, empty shelf, bulb, bell, soup with heart, smiling grocery tote	6	Good. The tote is almost exactly the mockup's welcome art	Use for Welcome, empty states, Tips, alerts
Paper texture	1	Fine	Keep in reserve. You rejected visible paper texture before
Ingredient catalog (57 items, shelf life per zone)	1 file	Solid	Starting point for catalog.json
Recipes (22, with core/garnish/seasoning and {ingredient} tokens in the steps)	1 file	Solid, a few errors	Starting point for recipes.json. Fix and extend to 30
Swap groups (14, with portion ratios like 1 lemon = 1.5 limes)	1 file	Very good idea	Starting point for swaps.json
SwiftData models, palette, hand-drawn shapes, 50 pen-drawn icons, art-generation script	5 files	Good drafts	Rewrite clean in the new architecture
Problems I found in the ZIP code that I'll fix:

The images are named IMG_0478 to IMG_0570, not by subject. Each one gets identified and renamed (for example IMG_0569 is Tomato Pasta, IMG_0570 is the tote).
The recipe id kale_white_bean_soup makes Kale & Chickpea Soup. Renamed.
Some roles are questionable: in the stir-fry, soy sauce is the glaze, so it can't be "optional". Every recipe gets a review.
Swap ratios were written in a single list. They get a check that every ingredient used in them exists.
1.2 The repo's design package (FoodSafe-Project/)

design.md: a detailed spec of colours, sizes, per-screen title tilts and each screen's content. I'll follow it, with a few contrast fixes (Part 3).
One rule you set before that I'll keep: no creased or crumpled paper background. The surface is calm, flat cream.
Its SVG food drawings are simpler than the ZIP watercolors, so I won't use them.
foodsafe-wordmark.png is 188 x 101 px and derived from the mockup. It's too small, so the wordmark becomes live text in a brush font.
1.3 Earlier rules found in the repo that still apply

No photography anywhere. The mockup's cooking photo becomes a watercolor painting.
Never use mockup crops as app art.
Every button must do what it says. No dead controls.
No personal details in any file.
1.4 Fonts, measured

Bundled and free to embed (SIL Open Font License): Patrick Hand, Kalam (Light, Regular, Bold), Caveat Brush. Their internal names are verified, so the code will load them correctly.

None of these fonts has an arrow character (→). "Swap: chicken → lentils" uses a small drawn arrow icon instead.

Part 2. Product decisions (what, why, and why not)
In short: build exactly what the mockup and brief describe, make every control real, and leave out anything that needs the internet.

Topic	Decision	Why	Why not the other option
Platform	Native SwiftUI, iOS 18 and newer, iPhone portrait first, still works on iPad	Most iPhones in use run iOS 18 or newer	iOS 26-only features (like AlarmKit timers) would cut out many phones, and local notifications already work when the app is closed
Server	None	"Fully offline, no internet required" is printed on your mockup	Accounts and sync add sign-in friction and break the promise
Storage	On the phone (SwiftData)	Personal, small and instant	iCloud sync is a good v2 feature. It needs its own testing
Look	Light paper theme only	The cream and watercolor are the identity	An automatic dark mode makes the watercolors look muddy. Dark mode needs its own art pass later
Bottom bar	Exactly the mockup's: Home, Inventory, raised green +, Recipes, More	Your mockup is the source of truth, and adding food is the most common action	A standard iOS tab bar can't draw the raised + or the ink icons
"Sign In" on Welcome	Becomes "Try a sample kitchen"	There are no accounts, so a sign-in button would lead nowhere	A fake button breaks trust on the first screen
"Offline Mode" toggle	Becomes a fixed row with a check: "Always offline"	The app is always offline, so a switch would change nothing	A toggle that does nothing is a lie
Meal planning	v1: choose what to cook from your stock, and save favourites (the mockup's hearts)	The mockup doesn't draw a calendar	A weekly planner needs its own screens. Good for v1.1
Barcode or receipt scanning	Not in v1	Product lookup needs an online database	It breaks offline mode and doubles the work
AI-generated recipes	Not in v1	Amounts and food safety must be exact	Generated recipes can't be trusted for exact quantities offline
Photos	None. Watercolor everywhere	Your earlier rule	Stock photos clash with the paper style
Part 3. The look (design system)
In short: three hand-lettered fonts, a cream-and-green palette with fixed contrast, wobbly ink outlines, drawn icons and watercolor art.

3.1 Typography

Tested side by side against crops of your mockup.

Role	Font	Approx. size	Example
Brand wordmark	Caveat Brush, green, tilted -4.5°	64 pt	"FoodSafe" on Welcome
Screen titles	Kalam Regular	24 pt	"My Kitchen", "Inventory"
Recipe titles	Kalam Bold	28 pt	"Tomato Pasta"
Section headings	Kalam Regular	18 pt	"Quick Overview", "Ingredients"
Body, rows, amounts, chips, buttons	Patrick Hand	15–17 pt	"Tomatoes", "300 g", "Save"
Metadata	Patrick Hand	12–13 pt	"Exp: 2 days", "15 min · 3 servings"
Tab captions	Patrick Hand	11–12 pt	"Home", "Recipes"
Why this pairing: Kalam has the marker weight of the mockup's titles. Patrick Hand stays upright and readable at 12 pt, where the mockup's small metadata lives.

Why not Purisa everywhere (the older pack's choice): its letters look close, but the strokes are thin and widely spaced, so small text looks faint.

Why not Kalam everywhere: at body size it slants and reads like a comic.

All fonts scale with the iPhone text-size setting (Dynamic Type). No system font appears in the app's own text.

3.2 Colours

Base colours come from design.md, sampled from your mockup. I measured text contrast against the accessibility standard (WCAG 4.5:1 for normal text) and darkened the text colours that failed. Fills and icons keep the mockup colours.

Token	Hex	Used for	Contrast
paper	#F7EEDC	Screen background	—
card	#FAF2E1	Cards, inputs	—
ink	#282E28	Main text	12.1:1 ✓
ink soft	#6B604F	Metadata, hints	5.3:1 ✓
green	#47705A	Primary buttons, selected chips	cream text 5.1:1 ✓ (mockup's #527B5E was 4.4, fail)
green deep	#2E6A4F	Wordmark, active tab, "Ready Now" text	4.8:1 on its wash ✓
green wash	#DCE4C4	Ready Now pill, Vegetables tile	—
coral text	#9E4033	"Soon", "Expires in 1 day", "Missing"	4.9:1 on wash ✓ (mockup's #C96658 was 2.8, fail)
coral wash	#F8D8CB	Alert banners	—
amber text	#8A5A14	"Almost Ready" text	4.9:1 ✓
amber wash	#FBE6C7	Almost Ready pill, Low Stock tile	—
blue text	#3A6680	"Smart Swap" text	5.0:1 ✓ (mockup's #5B8DA5 was 2.9, fail)
blue wash	#DAE9EC	Smart Swap pill, Dairy tile	—
lavender	#DFDAE9	Others tile	—
orange accent	#E7A34D	Stars and doodles only	Never used for text
Tiers never rely on colour alone. Each tier pill has its own icon and word.

3.3 Shapes and the hand-drawn feel

Cards, chips, inputs and buttons get slightly wobbly ink outlines. The wobble is seeded, so a card looks the same every time and never shimmers.
Titles, pills, thumbnails and buttons get small fixed tilts from design.md (up to about 1°). Lists and paragraphs stay level so text stays sharp and columns line up.
Buttons press down to 97% with a soft haptic.
No glass, no heavy shadows, no pure white, no pure black.
3.4 Icons

About 35 custom icons drawn as ink strokes on a 24-point grid, with a faint second pen pass: home, inventory, recipes, more, plus, search, back, chevron, heart, fridge, pantry, freezer, clock, timer, calendar, alert, check, swap, arrow, leaf, chef hat, bell, gear, info, units, storage, offline, about, trash, pencil, bulb, sort, servings, play, pause.

No SF Symbols in the interface.

3.5 Illustrations

Base: the ZIP watercolors (Part 1).
To generate in the same style: the app icon, about 8 new dish paintings for the new recipes, a watercolor "pan on the stove" for the Cooking screen, the pale cutouts, and any catalog item without art.
Every cutout is checked on cream cards and on the coloured category tiles. Weak ones are regenerated.
Part 4. How the app thinks (the rules)
In short: food is stored as batches with exact amounts. Recipes are checked line by line against those batches. The answer is a tier, a "you can make this many servings" number, and an order that puts expiring food first.

4.1 Inventory rules

A batch is one entry: ingredient, zone, amount left, amount when added, expiry day, date added, notes. Two bags of tomatoes are two batches. Recipes see the total.
Units: everything is stored in grams, millilitres or pieces. "1.5 kg" is saved as 1500 g.
Pieces for weighed food: some items have an average piece weight (tomato about 120 g, onion about 150 g), so "6 tomatoes" can be entered and converted.
Suggested expiry: today plus the ingredient's shelf life in the chosen zone. Spinach is 5 days in the fridge and 240 in the freezer. Switching the zone updates the suggestion until you pick a date yourself.
Expired food (past its date) is never counted as available. It shows at the top of Expiration Priority as "Expired, check it".
Signals:
Expiring Soon: 0 to 3 days left. "Within 24h" shows for today and tomorrow.
Low Stock: 40% or less of the added amount remains.
Almost Empty: 15% or less remains.
Custom groceries that aren't in the catalog are tracked but can't be matched to recipes. The Add screen says so.
4.2 The three tiers

Every recipe line has a role:

core: the dish fails without it (pasta in Tomato Pasta)
garnish: a finishing touch (basil)
seasoning: salt, pepper and spices, used to taste
Tier	Rule	Card shows
Ready Now	Every core line and every garnish is covered	"All ingredients available"
Almost Ready	Every core line is covered, and one or more garnishes are missing	"Missing: basil (optional)"
Smart Swap	One or more core lines are missing, and each one has a substitute from the same swap group, in a big enough amount	"Swap: lemon → lime"
Not suggested	A core line is missing with no substitute	Appears only under By Ingredient, with "Missing: X"
Seasonings never change a tier. If salt runs out, the step says "to taste".

4.3 Expiring food goes first

Each batch a recipe would use earns rescue points: expires today 5, in 1 day 4, in 2 days 3, in 3 days 2.

Suggestions are sorted by tier, then rescue points, then fewer missing lines, then shorter cooking time, then name.

Recipes with rescue points show a line such as "Uses spinach (1 day left)".

4.4 Scaling to what you have (worked example)

Tomato Pasta, base recipe 3 servings: pasta 300 g, tomatoes 400 g, olive oil 30 ml, garlic 2 cloves, basil 10 g.

Your kitchen: pasta 500 g, tomatoes 500 g, olive oil 1 L, garlic 6 cloves, basil 20 g.

Ingredient	Per serving	You have	Servings it allows
Pasta	100 g	500 g	5
Tomatoes	133 g	500 g	3.75
Olive oil	10 ml	1000 ml	100
Garlic	⅔ clove	6	9
The smallest is 3.75, so you can make 3 servings. On the Portion Scaling screen, 1, 2 and 3 are available, and 4 is disabled with "Limited by tomatoes, 500 g left".

At 2 servings the amounts become pasta 200 g, tomatoes 270 g (266.7 rounded), olive oil 20 ml, garlic 1½ cloves (1.33 rounded up), basil 7 g.

Rounding rules:

Pieces round up to the nearest half (1½ cloves, ½ onion).
Grams and millilitres round to the nearest step: 1 g under 10 g, 5 g from 10 to 100 g, 10 g from 100 g up. Values exactly halfway round up. Each boundary gets a test.
Step text fills in automatically: "Add {pasta}" becomes "Add 200 g pasta".
Timers stay the same. Doubling a batch adds the note "may need a few more minutes".
4.5 Swaps (worked example)

The citrus group: 1 lemon = 1½ limes = 1 orange = 20 ml vinegar.

A recipe needs 1 lemon and you have none. The app looks in the group: you have 3 limes and need 1½, so lime is a valid swap. The Ingredient Swaps screen shows Lime (checked, in stock), Vinegar and Orange (with an info icon, not in stock), and the reasons: "Similar acidity and flavor profile."

4.6 Cook and deduct

After the last step, a sheet asks "What did you use?" with every line pre-filled from the amounts on screen.
You can edit any line or switch seasonings off.
Saving takes food from the soonest-expiring batch first. A batch at zero disappears.
An Undo bar appears for a few seconds.
A cook log records the recipe, the servings and the number of items rescued from expiring. Home shows "Rescued this month".
Outside of cooking, swipe an item to mark it Used or Tossed, so the rescued count stays honest.
Part 5. Every screen, one by one
In short: the 13 mockup screens become 15 surfaces. Two small screens are added to complete the loop: a starter picker and cook complete.

#	Screen	Mockup	What it does	Changes from the mockup and why
1	Welcome	01	Wordmark, "Good food. Less waste.", tote art, "Your kitchen. Your ingredients. Better meals.", Get Started	"Sign In" becomes "Try a sample kitchen" (no accounts)
2	Starter picker	new	A grid of common foods with default amounts. Tap to add	Stops the first launch from being empty
3	My Kitchen (Home tab)	02	Fridge/Pantry/Freezer tabs, search, category tiles, "3 items need attention" banner, Quick Overview (Expiring Soon, Low Stock, Almost Empty)	Tiles open a filtered Inventory. The heart opens Favourites. Adds a small "Rescued this month" line
4	Add Ingredient (the + button)	03	Search the catalog, then quantity and unit, zone chips, expiry (pre-filled), notes, Save	Catalog search comes first, so art, category and shelf life fill in automatically. The same screen edits an item and has Delete
5	Inventory tab	04	Search, All/Fridge/Pantry/Freezer, rows with art, amount, zone, expiry and a "Soon" pill	Swipe a row for Used, Tossed or Delete. Includes an empty state
6	Expiration Priority	12	Alert banner, the soonest-expiring items with checkboxes, a Tips card	Adds "Cook with these (n)", which opens recipes that use the checked items
7	Recipe Suggestions (Recipes tab)	05	For You / By Ingredient / By Season, sort menu, one card per tier, View All Suggestions	Sorting is real: Best match, Quickest, Uses expiring
8	Meal Suggestions	10	Ready Now (n) / Almost Ready (n) / Smart Swap (n) tabs with full lists	Counts are live
9	Recipe detail	06 + 11	Hero art, tier pill, time, servings, heart, Ingredients/Steps tabs, Start Cooking	One template for every recipe. Ingredient rows show in stock, swapped or missing
10	Portion Scaling	08	Serving buttons, live adjusted quantities, Update Recipe	Servings you can't make are disabled, with the limiting ingredient named
11	Ingredient Swaps	09	Swap candidates with converted amounts, in-stock check, "Why?" reasons, "Use Lime Instead"	Button label follows your choice
12	Cooking	07	Step "2 of 5", watercolor scene, scaled step text, timer ring with "03:42 left", "Scaled for 3 servings", Back/Next	Painting instead of a photo. Timers keep running when the app is closed. The screen stays awake
13	Cook complete	new	"What did you use?" sheet, deduction, a small celebration	This is where inventory updates automatically
14	Settings (More tab)	13	Storage Zones, Units, Notifications, Always offline, About	Offline toggle becomes a status row. Adds an optional daily expiry reminder and Reset sample data
15	Favourites	heart icons	Saved recipes	Makes the mockup's hearts do something
Every list has an empty state with ZIP spot art (the empty shelf, the copper pot) and one sentence saying what to do next.

Notifications, asked at the right time

Never on first launch. The app asks after the first item gets close to expiring, or when you turn the reminder on in Settings. You get one daily digest ("2 items expire tomorrow") plus timer alerts while cooking.

Part 6. How the code is organised
In short: a pure rules engine with no UI, a small data layer, one folder per screen, and recipe content in JSON files with an automatic checker.

ios/Sources/
  App/            app entry, custom tab bar, navigation routes
  DesignSystem/   colours, fonts, wobbly shapes, icons, buttons, chips, cards, pills, fields
  Domain/         catalog, units, recipes, swap groups, matcher, scaler, deductor, expiry rules, formatters
  Data/           SwiftData models, inventory store, cook log, sample kitchen
  Features/       Welcome, Kitchen, AddItem, Inventory, Expiry, Suggestions, RecipeDetail,
                  Scaling, Swaps, Cooking, CookComplete, Settings, Favourites
  Services/       timers + notifications, daily expiry digest
  Resources/      recipes.json, catalog.json, swaps.json, fonts, Assets.xcassets
tools/            art map, art generation script, content validator
docs/             this plan, decisions log
Rules that keep it solid:

Domain never imports UI or storage. It's plain Swift, so the matcher, scaler and deductor can be tested on their own.
"Today" is always passed in, never read inside the rules, so expiry results are repeatable and testable.
Content is data, not code. Recipes, catalog and swaps live in JSON. tools/validate_content.py checks that:
every recipe ingredient exists in the catalog
every {token} in a step matches a recipe line
every swap ingredient exists
every art name has an image
units match dimensions (no "ml of eggs")
Each tab keeps its own navigation stack, so switching tabs never loses your place.
Tests: a unit-test target for the rules if the remote build supports it (checked in Stage 2). Otherwise the same cases run as a debug self-check plus the Python validator.
Part 7. The recipe book
In short: 30 recipes, chosen so the most perishable foods always have somewhere to go.

Start from the ZIP's 22 after a full review (roles, amounts, tokens, timers).
Add about 8 recipes that use foods that spoil fast (spinach, mozzarella, ground beef, bananas, soft herbs, yogurt), each with a new painting.
Every recipe has base servings, minutes, season tags (for By Season, based on month and hemisphere), a tip, and timers on the steps that need them.
The sample kitchen is stocked so all three tiers appear honestly, like the mockup, without faking any text.
Part 8. Motion, haptics and delight
In short: things you do often don't animate. Rare moments get the delight.

Moment	How often	Motion
Tabs, filter chips, toggles	Constantly	None. Instant, with a selection haptic
Pressing buttons and cards	Constantly	Press to 97%, about 140 ms
Suggestions appearing	Sometimes	Short stagger, first appearance only
Cooking Next / Back	Per step	Slides forward or back to match the direction. Crossfade with Reduce Motion
Timer	Per timer	Ring empties at a steady rate. Bell wiggle and success haptic at zero
Saving an item	Often	Button confirms in place and the row appears in the list. No "Saved!" popup
Finishing a recipe	Rare	The one celebration: an ink sparkle and the rescued count ticking up
Welcome	Once	Tote and wordmark settle in gently
Part 9. Accessibility (built in from the start)
Text scales with the system setting. Rows switch to stacked layouts at the largest sizes.
VoiceOver reads each row as one sentence: "Tomatoes, 500 grams, Fridge, expires in 2 days."
Every icon button has a spoken label.
Tap targets are at least 44 x 44 points.
Text colours pass contrast (Part 3.2).
Tiers and alerts use icons and words, not just colour.
Reduce Motion swaps slides for fades.
Part 10. Build stages, A to Z
In short: 12 stages. Four end in a checkpoint where you review the simulator before I go on.

Stage	What happens	You get	Checkpoint
A. Asset prep	Identify and rename all 92 ZIP images. Test cutouts on cream and on tiles. Write the art map	A clean, named art library	
B. Project setup	Create the project, bundle id, app icon, fonts, asset catalog	The app opens on the simulator with its real icon	
C. Design system	Colours, fonts, wobbly shapes, icons, buttons, chips, cards, plus a hidden component gallery screen	Every building block on screen	1: approve the look
D. Rules engine	Catalog, units, matcher, scaler, swaps, deductor, expiry rules, content JSON, validator, test cases	The rules working and tested	
E. Data + sample kitchen	Storage models, inventory store, cook log, sample stock	Real data behind every screen	
F. Kitchen screens	Welcome, starter picker, My Kitchen, Add Ingredient, Inventory, Expiration Priority, tab bar	You can add, browse and edit food	2: kitchen flow
G. Recipe screens	Suggestions, Meal Suggestions, Recipe detail, Portion Scaling, Swaps, Favourites	You can find a meal and scale it	3: recipe flow
H. Cooking	Cooking steps, timers, notifications, cook complete, deduction with undo	The whole loop works end to end	
I. Settings	Zones, units, reminder, about, reset	Every row works	4: full app
J. New art	New dish paintings, the cooking scene, replacements for pale cutouts	No placeholders anywhere	
K. Polish	Motion, haptics, empty and error states, large text, VoiceOver pass	It feels finished	
L. Fidelity pass	Screenshots of each screen next to its mockup crop, with a list of remaining differences	Proof it matches your mockup	Final review
Part 11. Risks and how each is handled
Risk	Plan
No bundled font is the mockup's exact face	Checkpoint 1 is where to swap fonts, before any screen is built
Some mockup copy can't be true with real data ("Swap: chicken → lentils" on a lentil soup)	The sample kitchen produces real results. Text is never faked
Pale watercolor cutouts vanish on cream	Each is checked on cream and regenerated if needed
A custom tab bar can lose system behaviour	It sits over a hidden system TabView, so each tab keeps its own stack
Timers stopping when the app closes	A timer stores its end time, not a countdown, and a local notification is scheduled