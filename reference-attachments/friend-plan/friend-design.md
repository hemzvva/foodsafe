FoodSafe design.md — the definitive guideline
Version 1.0. This file is the single source of truth for turning the 13-screen mockup into a top-tier native iOS app. Every value below is either measured from the mockup, tested against it, or fixed here as an implementation token. Nothing is guessed twice: if a value appears here, it is the value.

Companion documents: PLAN.md (product decisions and build order). If the two disagree, PLAN.md wins on product scope and this file wins on visual and interaction detail.

0. Source of truth and fidelity rules
The mockup is the visual source of truth. The reference is the 1536 × 1024 board (FoodSafe-Project/reference/original-mockup.jpg) with 13 phone screens. Rectified, perspective-corrected crops at the 390 × 844 baseline live in FoodSafe-Project/reference/rectified/01…13.jpg.

What is app, what is board:

The phone screens, their surfaces, controls, lettering and food art are the app. Recreate them.
The freehand arrows, stars, captions ("Everything you have, at a glance!"), the yellow sticky note and the paper scraps belong to the presentation board. Never place them in the UI.
The drawn phone bezels and their tilt are board effects. Never render a bezel. The native status bar and home indicator are iOS-owned; never draw "9:41".
The internal UI has its own small hand-composed irregularity (tilts, wobbly outlines). That part is app, and it is mandatory.
Hard art rules:

Illustration only. No photography anywhere, ever. The mockup's one cooking photo becomes a watercolor painting.
Never crop the mockup and use the crop as art. All food art is original watercolor (the generated set in assets/).
No emoji as icons. No SF Symbols in the interface. Every icon is a drawn glyph from §7.
English only, portrait-first, light appearance only in v1.
1. Art direction
Warm sketchbook. FoodSafe looks like a well-loved cookbook page: warm cream paper, deep forest-green controls, ink-drawn linework, soft watercolor food, and hand-printed lettering. Nothing glossy, nothing glass, nothing neon.

Feel targets:

Calm, not cluttered. One decorative accent per region (a star, a leaf, a doodle), never covering content.
Handmade, not sloppy: outlines wobble within ±0.6 pt, tilts stay under ~1°, and everything is deterministic (seeded), so nothing shimmers or changes between launches.
Food is the hero. Watercolor art carries warmth; the chrome (paper, ink lines) stays quiet so the art and green actions stand out.
The surface is calm flat cream. The crumpled-paper look was explicitly rejected by the owner and must not return. A barely-visible paper grain is permitted only if it passes a side-by-side check; default is none.
2. Colour system
Sampled from the mockup and fixed as tokens. Text colours were measured against WCAG AA (4.5:1 for normal text) and darkened where the mockup's originals failed. Fills and icon colours keep the mockup's values.

2.1 Tokens

Token	Hex	Use	Contrast (vs its text surface)
paper	#F7EEDC	Screen background	—
card	#FAF2E1	Cards, inputs, unselected chips	—
cardSunk	#EEE4CE	Segmented track, recessed wells	—
paperDeep	#E8DCC5	Separators, soft shadows	—
ink	#282E28	Primary text, icon strokes	12.1:1 on paper ✓
inkSoft	#6B604F	Metadata, helper copy, placeholders	5.3:1 on paper ✓
line	#827460	Card and input outlines, at 45–60% opacity	pencil-like, never black
lineSubtle	#BFB19A	Inner dividers, at 25–40% opacity	—
green	#47705A	Primary buttons, selected chips, active tab	cream label 5.1:1 ✓ (mockup's #527B5E measured 4.4:1 — do not use it for text-bearing fills)
greenDeep	#2E6A4F	Wordmark, Ready Now text, pressed green, focus	4.8:1 on greenWash ✓
onGreen	#FBF4E5	Labels on green fills	—
greenWash	#DCE4C4	Ready Now pill, Vegetables tile	—
greenSoft	#EAF0DC	Positive info surfaces	—
coralText	#9E4033	"Soon", "Expires in…", "Missing:" text	4.9:1 on coralWash ✓ (mockup's #C96658 measured 2.8:1 — fills and icons only)
coral	#C96658	Expiry icons, critical badges (non-text)	—
coralWash	#F8D8CB	Alert banner, Soon pill, Proteins tile	—
amberText	#8A5A14	Almost Ready, Low Stock text	4.9:1 on amberWash ✓
amberWash	#FBE6C7	Almost Ready pill, Low Stock tile	—
blueText	#3A6680	Smart Swap text	5.0:1 on blueWash ✓ (mockup's #5B8DA5 measured 2.9:1 — fills/icons only)
blue	#5B8DA5	Smart Swap icons, rare cool accents	—
blueWash	#DAE9EC	Smart Swap pill, Dairy tile	—
lavenderWash	#DFDAE9	Others tile	—
orangeAccent	#E7A34D	Stars, doodles, ripe-food accents only	never for text (1.9:1)
redSoft	#DFB9AF	Overdue accents on washes	—
2.2 Rules

Never pure white and never pure black. Lightest surface is card, darkest text is ink.
Colour never carries meaning alone. Every tier, alert and status pairs colour with a drawn icon and a word (§9 pills).
Category tiles use the wash colours as fills with the watercolor subject on top; text on tiles is always ink at tiny size.
Dark mode: not in v1. Watercolor on dark paper was judged muddy. A dark pass is a separate design project.
3. Typography
Tested against mockup crops. The mockup's lettering is hand-printed: upright, rounded, irregular, legible at 12 pt. No bundled font is identical to it, so the pairing below was chosen by rendering candidates against rectified crops.

3.1 The stack

Role	Font	Size (pt at default Dynamic Type)	Notes
Brand wordmark "FoodSafe"	Caveat Brush	64	#2E6A4F, rotated −4.5°, live text (no bitmap)
Screen titles ("My Kitchen", "Inventory")	Kalam Regular	24	ink, per-screen tilt from §6.2
Recipe titles ("Tomato Pasta")	Kalam Bold	28	ink, tilt −0.85° on detail
Section headings ("Quick Overview", "Ingredients")	Kalam Regular	18	ink, alternating tilt −0.8° / +0.65° by order
Body, rows, amounts, chips, button labels	Patrick Hand	16–17	ink; buttons on green use onGreen
Metadata ("Exp: 2 days · 15 min")	Patrick Hand	12.5	inkSoft, or coralText for expiry
Tab captions	Patrick Hand	11	inactive inkSoft, active greenDeep
PostScript names (verified in the bundled files): Kalam-Regular, Kalam-Bold, PatrickHand-Regular, CaveatBrush-Regular. Kalam Light is bundled but reserved; do not use it in v1.

3.2 Why this pairing

Kalam carries titles because its marker weight matches the mockup's headline ink; Patrick Hand stays upright and dense, matching the mockup's small metadata, where Purisa (the older pack's single-face choice) went thin and faint at 12 pt.
Purisa remains available and is the fallback identity if a review at Checkpoint 1 prefers it.
Caveat Brush is for the wordmark only. Never use it for body copy.
3.3 Rules

Every font loads with relativeTo: so Dynamic Type works. No .system(…) on any app-authored text, no exceptions for tiny labels, placeholders or button captions.
Tracking stays 0. No letter-spacing to fake handwriting; no italics; no per-glyph rotation.
Bold (Kalam Bold) appears only where the mockup shows extra ink: recipe titles and, sparingly, short emphasis. Never make all labels bold.
Amounts in tables align right but keep the hand-printed face.
One semantic enum (Font.fsTitle, .fsBody, .fsMeta…) routes all text. Screens never call .custom directly.
4. Geometry
Baseline device: 390 × 844 pt. iPhone portrait-first; iPad keeps the same single-column layout at a readable max width (≤ 480 pt content).

4.1 Spacing

Content inset: 16 pt from screen edges (welcome: 24 pt).
Vertical rhythm: 5, 7, 9, 11, 14, 18 pt. Cards and content sit close, like the mockup, never on a spacious 24 pt grid.
Section gap: 18 pt. Card internal padding: 10–12 pt.
4.2 Tilt tokens (deterministic, rotationEffect)

Element	Rotation
Wordmark	−4.5°
Welcome tagline	−1.2° / −1.6°
Screen title	per screen: home −1.0, add +0.85, inventory −0.65, suggestions +0.8, detail −0.85, cooking +0.75, scaling −0.95, swaps +0.8, meals −0.65, lentil/detail2 +0.9, expiry −0.8, settings +0.65
Section headings	alternate −0.8° / +0.65°
Primary buttons	−0.65°; secondary +0.55°
Filter chips	odd −0.7°, even +0.55°, third −0.35°
Category tiles	[−0.45, +0.55, −0.35, +0.8, +0.3, −0.6], repeating
List/recipe cards	alternating −0.45° / +0.55°
Ingredient thumbnails	±0.7° (image only, never its amount text)
Form labels	−0.35°, selected labels +0.3°
Rules: hit targets and scroll geometry never rotate. Lists and paragraphs stay level for sharp text and aligned columns. Never use random(); seeds are stable per element (FNV-1a of its title or id).

4.3 Component dimensions (at the 390 baseline)

Component	Height	Radius	Stroke
Header (back button + title)	44–50 below safe area	—	—
Zone/filter chip	34–38 (min touch 44)	capsule	0.8
Search field	40–42	21	0.8
Standard input	42–45	13	0.8
Notes field	82–90	13	0.8
Category tile	74–80	15	1.0
General card	58–72	14–16	0.8–1.0
Inventory row	66–72	14	1.0; art 48–54
Recipe suggestion card	112–124	15	1.0; thumb left, text right
Recipe hero	full width, 124–150	0–4 top	controls as circular paper buttons
Status pill	min 22–26	capsule	pale wash fill
Primary CTA	46–50	14	full width unless paired
Secondary CTA	42–46	14	—
Tab bar	56–62 + safe area	top separator only	five slots, raised green +
Circular icon button	32–38 visible, ≥44 touch	circle	drawn outline
Cards feel like sketchbook paper laid on the desk: one subtle top-edge highlight, 0–2 pt downward shadow, no heavy elevation.

5. Surfaces and linework
Every card, chip, input, button and pill sits on a seeded wobbly outline (SketchRect/SketchCircle): edges bow slightly, corners are never quite equal, and a faint second pass (opacity ~0.16, offset ~1 pt) reads as pencil under ink. Offsets stay within ±0.6 pt.
Outlines never animate. The wobble is fixed per element for life.
Fills: card on paper; washes on tiles and pills. No gradients, no blur, no glass materials, no shadows over 2 pt.
Dividers: lineSubtle at 25–40% opacity, inset 12 pt.
Scrolling content passes under floating chrome (headers, tab bar) with a soft edge fade, not a hard divider.
6. Screen anatomy
6.1 Global silhouette

Warm paper canvas fills the screen; no white/blue stock background anywhere.
Content insets 16 pt; headers are compact (44–50 pt), not iOS large-title.
Persistent bottom tab bar on Home, Inventory, Recipes and More. Full-screen flows (cooking, add sheet) hide it.
Back is always top-left, a drawn back glyph with ≥44 pt touch, label spoken by VoiceOver.
Every screen answers: where am I (title), what's here (content), how do I get out (back/tab/Close).
6.2 Screen-by-screen spec

01 Welcome — wordmark (Caveat Brush, −4.5°), tagline "Good food. Less waste." (Kalam, greenDeep), the smiling tote watercolor centered, "Your kitchen. Your ingredients. Better meals." (Patrick Hand 18, rotated −1.6°), primary "Get Started", quiet "Try a sample kitchen" instead of Sign In. Doodles: one star, one leaf. Nothing else.

02 My Kitchen (Home tab) — title "My Kitchen" (−1.0°) with drawn home glyph leading; zone chips Fridge/Pantry/Freezer; search field; 4×2 category tiles (art subjects, wash fills, tilts per §4.2); Quick Overview heading with drawn star; alert row "N items need attention" (coral) opening Expiration Priority; rows Expiring Soon / Low Stock / Almost Empty (coral, amber washes) with counts; tab bar. Heart glyph top-right opens Favourites.

03 Add Ingredient (sheet over tab bar) — back + title "Add Ingredient" (+0.85°). Catalog search first: pick an item and its watercolor, category and shelf life fill in automatically. Then: art + name header; Quantity (numeric field bound to the number, unit picker g/kg/ml/L/pcs); Storage Zone chips (Pantry/Fridge/Freezer with glyphs, selected = green fill); Expiration Date field pre-filled with suggested date (add date + shelf life in chosen zone; zone change updates suggestion until the user edits it); optional Notes; primary Save. Editing an existing item adds a danger Delete. Custom (non-catalog) names are allowed with a note that they won't match recipes.

04 Inventory (tab) — title "Inventory" (−0.65°), search, All/Fridge/Pantry/Freezer chips (All selected default), rows: art, name, "500 g · Fridge", expiry line in coralText when ≤3 days with a "Soon" pill, chevron. Tap = edit sheet. Swipe actions: Used (green check), Tossed (coral), Delete. Empty state: the empty-shelf spot art + "Your shelves are empty. Add your first item with the green +."

05 Recipe Suggestions (Recipes tab) — title "Recipe Suggestions" (+0.8°); segmented For You / By Ingredient / By Season; meta line "Based on your kitchen" with a sort menu (Best match, Quickest, Uses expiring); tier-grouped cards: pill (Ready Now green / Almost Ready amber / Smart Swap blue), dish thumb, name, "15 min · 3 servings", missing/swap line when applicable, chevron; trailing full-width secondary "View All Suggestions" opening the tiered Meal Suggestions screen. Empty state: copper-pot spot art + "Cook something first, or add more food to your kitchen."

06 Recipe detail (one template for all) — back; hero watercolor full-width (124–150) with circular paper heart button top-right (fills on tap, haptic); title (Kalam Bold 28, −0.85°); tier pill + "15 min · 3 servings" row; segmented Ingredients / Steps. Ingredients: drawn art per line, name, scaled amount right-aligned, status (in stock green check / swap arrow with substitute / missing coral). Steps: numbered hand-drawn circles, step title (Kalam 18), body text with live scaled amounts, timer chip when the step has one. Tip card at the bottom (bulb spot art, "Tips" heading, tip text). Primary "Start Cooking".

07 Portion Scaling — back; recipe header row; "Adjust servings" heading; serving buttons 1–4 (selected = green fill; values above the achievable max are disabled with "Limited by tomatoes, 500 g left"); "Adjusted Quantities" list updating live (art, name, scaled amount, fractions like 1½); primary "Update Recipe".

08 Ingredient Swaps — back; "Try these swaps" heading; card per candidate: art, name, "Can be swapped with:" context; in-stock candidates show a green check and converted amount ("1 lemon → 1½ limes"); out-of-stock show an info glyph; "Why?" card with the swap group's reasons (green checks); primary "Use Lime Instead" (label follows the chosen candidate).

09 Cooking (full-screen, hides tab bar) — back + "Cooking…" (+0.75°); header card: recipe name + "Step 2 of 5"; watercolor scene (the pan-on-stove painting, not a photo); step number in a drawn circle, step title (Kalam 18), step text with scaled amounts; timer row when the step has one: ring countdown, "03:42 left" (tabular numbers), start/pause, and it keeps running with a local notification when the app closes; "Scaled for 3 servings" row with green check; Back (quiet) / Next (primary) pair; final step is "Finish & log used food". Screen stays awake (idleTimerDisabled) while cooking.

10 Cook complete (sheet) — "What did you use?" list of every ingredient line pre-filled with on-screen amounts, editable steppers, seasonings optional; "Rescued: spinach, tomatoes" line when applicable; primary "Save"; brief Undo bar after; small sparkle + rescued-count tick (the app's one celebration; crossfade under Reduce Motion).

11 Meal Suggestions — back; title "Meal Suggestions" (−0.65°); tier tabs with live counts "Ready Now (2) / Almost Ready (1) / Smart Swap (0)"; full-height list of suggestion cards per tier with missing/swap lines.

12 Expiration Priority — back; title "Expiration Priority" (−0.8°); alert banner (coral wash): "3 items need to be used within 24–48 hours"; checkable rows for the soonest items (art, name, "Expires in 1 day", checkbox drawn); primary "Cook with these (n)" → Suggestions filtered to recipes using checked items; Tips card (bulb art, heart doodle): "Use these ingredients first to reduce food waste!" Expired items appear first with "Expired, check it" and no recipe matching.

13 Settings (More tab) — title "Settings" (+0.65°) with gear glyph; rows with glyph badges: Storage Zones ("Pantry, Fridge, Freezer" — reorder/hide), Units ("Grams, millilitres, pieces" — or US display), Notifications (optional daily expiry digest; permission asked here or after the first near-expiry item, never on first launch), "Always offline" fixed row with a check (no toggle: the app is always offline), About ("Version 1.0.0"), Reset sample data (danger, confirm dialog).

Added: Favourites — reached from the heart on Home and detail; list of hearted recipes as suggestion cards; empty state with the bowl spot art.

6.3 Navigation

One NavigationStack per tab; each tab keeps its scroll position and history independently.
The custom tab bar draws the mockup's five slots (Home, Inventory, raised green +, Recipes, More) over a hidden system container. The raised + opens the Add sheet from every tab.
Full-screen flows (Cooking) cover the tab bar; sheets (Add, Scaling, Swaps, Cook complete) keep it dimmed beneath.
7. Iconography
A FoodSafe icon is ink, not a symbol: strokes on a 24 pt grid with rounded caps, a very slight bow on straight lines, and a faint offset second pass (pencil under ink). Stroke weight 1.8 at 22 pt, scaled with Dynamic Type.

Set (50): home, inventory, recipes, more, plus, minus, search, back, forward, chevron, chevronDown, heart, heartFill, fridge, pantry, freezer, clock, calendar, alert, check, checkCircle, bell, gear, leaf, chefHat, timer, swap, arrow, trash, pencil, info, sparkle, bowl, offline, sort, person, close, bulb, play, pause, reset, units, storage, about.

Rules:

No SF Symbols and no emoji anywhere in the interface.
Every glyph button carries a spoken label (Glyph.label); the glyph itself is hidden from VoiceOver.
The swap sentence "chicken → lentils" uses the drawn arrow glyph inline; no bundled font has a → character, so never type it.
8. Illustration and assets
Watercolor language (shared by all art, generated and existing): hand-painted watercolor and ink, loose confident brown outlines, soft washes, warm cream backgrounds keyed to alpha for cutouts, charming cookbook sketchbook style, no text in art.

Inventory already in the repo (assets/, mapped in assets/art-map.json):

22 dish paintings (960×717) covering the recipe book's 22 dishes — heroes and card thumbs.
56 ingredient cutouts + empty jar (360 px, transparent) — inventory rows, add-item header, ingredient lists.
6 category subjects — Home category tiles.
6 spot illustrations: copper pot (no recipes), empty shelf (empty inventory), light bulb (tips), bell (alerts), soup with heart (done), smiling tote (welcome).
1 paper texture (768 px) — in reserve only; not applied by default.
To generate in the same style (Stage J): the 8 new dish paintings for recipes 23–30, the cooking scene (a pan on the stove with steam), replacements for pale cutouts (milk, mozzarella, tofu, empty jar), and any catalog item without art. Every cutout is audited on cream and on each wash fill; weak ones are regenerated.

Placement rules:

Cutouts get a ±0.7° tilt inside rows; never rotate the amount text.
One accent doodle per screen region; never over text; decorative art is hidden from VoiceOver.
Art never carries information the text doesn't also carry.
9. Status and tier language
State	Pill	Icon	Text colour	Wash
Ready Now	"Ready Now"	checkCircle	greenDeep	greenWash
Almost Ready	"Almost Ready"	clock	amberText	amberWash
Smart Swap	"Smart Swap"	swap	blueText	blueWash
Expiring soon	"Soon" / "Expires in N days"	alert/clock	coralText	coralWash
In stock	green check	check	greenDeep	—
Swapped	"lemon → lime"	arrow	blueText	—
Missing (optional)	"Missing: basil (optional)"	alert	coralText	—
Card copy for tiers is live from the rules engine: "All ingredients available", "Missing: soy sauce (optional)", "Swap: chicken → lentils". The mockup's exact sentences are the template, the data must be true.

10. Motion and haptics
Frequency decides motion. Frequent actions are instant; rare moments get the delight.

Moment	Frequency	Treatment
Tab switch, chip select, toggle	constant	none; selection haptic only
Button/card press	constant	scale 0.97, ~140 ms, light impact
Suggestions first appearance	occasional	30–80 ms stagger, once
Cooking Next/Back	per step	direction-aware slide (forward on Next, reverse on Back); crossfade under Reduce Motion
Timer ring	per timer	linear countdown; bell wiggle + success haptic at zero
Save item	often	button confirms in place, row appears in list; no "Saved!" modal
Cook complete	rare	ink sparkle + rescued count ticks up (the one celebration)
Welcome	once	wordmark and tote settle in with a gentle ease-out
Never animate: keyboard-initiated actions, wobbly outlines, tilt, data the user is reading. Interruptible everywhere: gestures blend velocity, nothing locks input during a transition. Reduce Motion replaces slides and springs with short crossfades.

11. Sound
None in v1 except haptics. The timer completion may add a soft bell through the system notification sound only. No background audio.

12. Accessibility
Dynamic Type: every custom font scales; at accessibility sizes rows reflow to stacked layouts and nothing clips.
VoiceOver: rows read as one sentence ("Tomatoes, 500 grams, Fridge, expires in 2 days"); icon buttons have spoken labels; decorative art hidden.
Touch: every interactive element ≥44 × 44 pt, including chips and circular buttons.
Contrast: text tokens in §2 all pass AA on their surfaces; information never relies on colour alone (every state has icon + word).
Reduce Motion and Reduce Transparency respected; Increase Contrast keeps all washes near-solid with defined borders.
13. Do / Don't
Do:

Keep every surface warm cream; let green and watercolor carry the colour.
Use live data for all status text; never hard-code a tier or a date.
Keep the hand feel through seeded wobble and small tilts.
Let food art be big where it's the point (hero, welcome) and small where it's data (rows).
Don't:

Don't ship photography, emoji icons, SF Symbols or system-font text.
Don't render the board's annotations, bezels, "9:41", or creased paper.
Don't invent spacing on a 24 pt grid; the mockup is compact (§4.1).
Don't animate outlines, tilts, or reading data; don't celebrate routine actions.
Don't place a control the data can't support (no Sign In, no Offline toggle).
14. Acceptance checklist (per screen, at Checkpoint reviews)
Matches its rectified mockup crop in layout, hierarchy, palette and type roles; differences are listed, not hidden.
Every visible control does what its label says on real data; no dead controls, no placeholder text.
All text uses the stack from §3; Dynamic Type at the largest size shows no clipping.
Every interactive element ≥44 pt; VoiceOver reads each row as one sensible sentence.
Statuses use icon + word + colour (§9); no meaning by colour alone.
Motion matches §10; Reduce Motion degrades gracefully.
Empty, loading and error states exist and use the spot art with one clear sentence