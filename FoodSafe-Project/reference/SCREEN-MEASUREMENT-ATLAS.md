# FoodSafe screen measurement atlas

**Source:** supplied 1536×1024 perspective collage. **Screen frame convention:** each reference panel is homography-rectified to a 390×844 coordinate canvas. All element boxes are in logical points on that canvas; coordinates are approximate, not original source code constraints.

## Accuracy and coordinate semantics

- Source quadrilateral corners were manually measured in the original collage. Corner placement uncertainty is approximately ±2–5 raster pixels; after rectification, derived boxes are conservatively treated as ±6 pt horizontally and ±7–8 pt vertically.
- `x,y` are from the top-left. `w,h` represent the whole visible component bounds, including its outline, not only text ink.
- Rotations are deterministic implementation targets. They imitate the small hand-composed tilt; the flattened JPEG cannot reveal exact source view transforms. Positive means clockwise.
- The phone frames are part of the reference board, not a native app element. Use the component positions inside the 390×844 reference coordinate system, then re-map to the real safe area in SwiftUI. The welcome panel is a separate onboarding composition.
- The JSON file is authoritative for machine-readable measurements. `visual-qa/coordinate-audit/screen-geometry.json` contains per-screen source-corner quadrilaterals plus perspective transform matrices.

## Source image screen corners (pixels)

| # | Screen | TL `(x,y)` | TR `(x,y)` | BR `(x,y)` | BL `(x,y)` | Rectified reference |
|---:|---|---:|---:|---:|---:|---|
| 01 | Welcome / onboarding | `(22, 34)` | `(218, 28)` | `(237, 535)` | `(24, 538)` | [`01-welcome.jpg`](rectified/01-welcome.jpg) |
| 02 | My Kitchen | `(246, 58)` | `(475, 61)` | `(478, 550)` | `(251, 555)` | [`02-my-kitchen.jpg`](rectified/02-my-kitchen.jpg) |
| 03 | Add Ingredient | `(505, 58)` | `(739, 60)` | `(738, 531)` | `(504, 534)` | [`03-add-ingredient.jpg`](rectified/03-add-ingredient.jpg) |
| 04 | Inventory | `(771, 59)` | `(996, 61)` | `(1001, 551)` | `(774, 555)` | [`04-inventory.jpg`](rectified/04-inventory.jpg) |
| 05 | Recipe Suggestions | `(1023, 60)` | `(1253, 63)` | `(1258, 527)` | `(1024, 533)` | [`05-recipe-suggestions.jpg`](rectified/05-recipe-suggestions.jpg) |
| 06 | Tomato Pasta detail | `(1280, 71)` | `(1514, 75)` | `(1514, 523)` | `(1278, 528)` | [`06-tomato-pasta.jpg`](rectified/06-tomato-pasta.jpg) |
| 07 | Cooking step | `(39, 580)` | `(257, 575)` | `(261, 949)` | `(48, 954)` | [`07-cooking.jpg`](rectified/07-cooking.jpg) |
| 08 | Portion Scaling | `(276, 580)` | `(475, 578)` | `(477, 945)` | `(283, 950)` | [`08-portion-scaling.jpg`](rectified/08-portion-scaling.jpg) |
| 09 | Ingredient Swaps | `(496, 583)` | `(690, 580)` | `(694, 942)` | `(505, 947)` | [`09-ingredient-swaps.jpg`](rectified/09-ingredient-swaps.jpg) |
| 10 | Meal Suggestions | `(711, 583)` | `(919, 582)` | `(919, 945)` | `(719, 949)` | [`10-meal-suggestions.jpg`](rectified/10-meal-suggestions.jpg) |
| 11 | Lentil Soup detail | `(937, 583)` | `(1121, 582)` | `(1120, 945)` | `(942, 949)` | [`11-lentil-soup.jpg`](rectified/11-lentil-soup.jpg) |
| 12 | Expiration Priority | `(1141, 583)` | `(1307, 583)` | `(1307, 941)` | `(1150, 946)` | [`12-expiration-priority.jpg`](rectified/12-expiration-priority.jpg) |
| 13 | Settings | `(1327, 585)` | `(1505, 585)` | `(1507, 925)` | `(1330, 930)` | [`13-settings.jpg`](rectified/13-settings.jpg) |

## Global typography and component tokens

All app-authored text uses **FoodSafe Hand / Purisa Regular** by default. Purisa Bold is reserved for rare source-supported emphasis. Font sizes below are visual-size estimates at the 390×844 baseline—not exact recovered point sizes. The welcome wordmark remains the source-derived artwork asset. No system-font body exception is permitted.

| Role | Size (pt) | Weight | Ink | Line-height |
|---|---:|---:|---|---:|
| `status` | 10.5 | 400 | `#282E28` | 1.00× |
| `page-title` | 22 | 400 | `#282E28` | 1.05× |
| `recipe-title` | 27 | 400 | `#282E28` | 1.04× |
| `recipe-title-small` | 21 | 400 | `#282E28` | 1.08× |
| `section-title` | 17 | 400 | `#282E28` | 1.10× |
| `body-strong` | 15 | 400 | `#282E28` | 1.15× |
| `body-copy` | 14 | 400 | `#282E28` | 1.25× |
| `field-label` | 14 | 400 | `#282E28` | 1.05× |
| `item-title` | 15 | 400 | `#282E28` | 1.05× |
| `item-title-small` | 13 | 400 | `#282E28` | 1.05× |
| `metadata` | 11.5 | 400 | `#6B604F` | 1.12× |
| `warning-metadata` | 11.2 | 400 | `#C96658` | 1.10× |
| `swap-metadata` | 11.3 | 400 | `#B87937` | 1.10× |
| `tagline` | 22 | 400 | `#315C43` | 1.03× |
| `support` | 18 | 400 | `#514B3E` | 1.20× |
| `button-label` | 16 | 400 | `#FBF4E5` | 1.00× |
| `secondary-action` | 14 | 400 | `#315C43` | 1.00× |

### Fixed surface geometry

| Component | Measurement target | Line / fill | Rotation target |
|---|---|---|---|
| Main content inset | 14–18 pt (welcome 20–24 pt) | — | — |
| Header back tap area | 44×44 pt minimum; visible glyph ~24–32 pt | ink primary | glyph wrapper −1° to +1° |
| Storage/filter chip | 34–48 pt high by source-specific row | 0.8 pt outline; selected green | body angle about −0.6° to +0.5° |
| Search field | 40–44 pt high | 0.8 pt warm outline; cream fill | outer −0.2° to +0.2° |
| Input | 42–54 pt high; note field 70–74 pt | 0.8 pt outline; 12–14 pt radius | outer −0.3° to +0.3° |
| Standard card | content-driven 60–180 pt | 0.8–1 pt outline, 0–2 pt shadow | −0.45° to +0.45° |
| Main CTA | 51–66 pt on reference; capsule | green fill, dark-green edge, cream label | typically −0.65° (per-element in JSON) |
| Tab bar | y≈752, h≈78 pt on home/settings | warm separator, center Add button ~42 pt | no whole-bar tilt |
| Icon artwork | glyph box approx 18–40 pt | hand-drawn SVG/pencil fill | art itself may vary ±0.7°; label remains aligned |

## welcome — Welcome / onboarding

Reference: [`01-welcome.jpg`](rectified/01-welcome.jpg)

This panel is a welcome/marketing composition rather than a typical app screen. Coordinates describe the visible panel; source sheet itself is photographed/rectified.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `sun-doodle` | **illustration**: sun | 14 | 39 | 76 | 94 | -5.00 | — | — | board-style decoration visible on onboarding panel |
| `wordmark` | **brand-art**: FoodSafe | 18 | 103 | 354 | 132 | -3.40 | — | — | Source-derived brush lettering; preserve asset, do not typeset. |
| `tagline-line-1` | **text**: Good food. | 99 | 239 | 195 | 41 | -1.00 | tagline | 22 | #315C43 |
| `tagline-line-2` | **text**: Less waste. | 101 | 276 | 207 | 38 | -1.20 | tagline | 22 | #315C43 |
| `grocery-bag` | **illustration**: Grocery bag with smiling face, vegetables and groceries | 36 | 327 | 321 | 246 | +0.50 | — | — | Major hero occupies ~39% of panel height; transparent source art preferred. |
| `support-copy-line-1` | **text**: Your Kitchen. | 57 | 588 | 237 | 34 | -2.20 | support | 18 | #514B3E |
| `support-copy-line-2` | **text**: Your ingredients. | 72 | 619 | 222 | 36 | -2.20 | support | 18 | #514B3E |
| `support-copy-line-3` | **text**: Better meals. | 87 | 652 | 182 | 33 | -2.00 | support | 18 | #514B3E |
| `get-started-button` | **button**: Get Started | 18 | 714 | 346 | 57 | -1.10 | primary-button | — | Capsule appears hand-drawn; green fill; preserve slightly unequal top/bottom contour. |
| `get-started-label` | **text**: Get Started | 100 | 731 | 183 | 28 | -0.40 | button-label | 16 | #FBF4E5 |
| `sign-in-label` | **text**: Sign In | 145 | 787 | 95 | 28 | +0.60 | secondary-action | 14 | #315C43 |
| `decorative-stars` | **illustration**: Small yellow star and pencil-stroke marks | 13 | 278 | 42 | 40 | -8.00 | — | — | Separate decorative assets, do not use emoji glyphs. |


## home — My Kitchen

Reference: [`02-my-kitchen.jpg`](rectified/02-my-kitchen.jpg)

Six category tiles are visible: 4 in the first row and 3 in the second; preserve the intentionally offset empty/decoration area on the second row.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `home-icon` | **icon**: Home | 27 | 48 | 42 | 40 | -1.00 | — | — | Home |
| `page-title` | **text**: My Kitchen | 91 | 48 | 161 | 37 | -0.80 | page-title | 22 | #282E28 |
| `favorite-icon` | **icon**: Heart outline | 282 | 53 | 24 | 30 | -4.00 | — | — | Heart outline |
| `header-sparkle` | **illustration**: Small yellow sparkle | 322 | 68 | 16 | 18 | +8.00 | — | — | Small yellow sparkle |
| `storage-fridge` | **chip**: Fridge | 20 | 113 | 113 | 48 | -0.60 | filter-selected | — | — |
| `storage-pantry` | **chip**: Pantry | 140 | 115 | 113 | 46 | +0.40 | filter | — | — |
| `storage-freezer` | **chip**: Freezer | 260 | 114 | 111 | 46 | -0.20 | filter | — | — |
| `search-field` | **field**: Search ingredients... | 19 | 183 | 353 | 43 | -0.10 | search | — | — |
| `category-vegetables` | **category-tile**: Vegetables | 19 | 247 | 87 | 82 | -0.50 | category | — | — |
| `category-fruits` | **category-tile**: Fruits | 117 | 248 | 83 | 82 | +0.55 | category | — | — |
| `category-dairy` | **category-tile**: Dairy | 213 | 248 | 80 | 82 | -0.35 | category | — | — |
| `category-grains` | **category-tile**: Grains | 302 | 248 | 72 | 82 | +0.80 | category | — | — |
| `category-proteins` | **category-tile**: Proteins | 19 | 344 | 88 | 79 | +0.30 | category | — | — |
| `category-others` | **category-tile**: Others | 117 | 344 | 83 | 79 | -0.60 | category | — | — |
| `category-leaves` | **category-tile**: Leaves | 213 | 344 | 81 | 79 | +0.55 | category | — | — |
| `category-decor-star` | **illustration**: Yellow sparkle | 312 | 354 | 37 | 32 | +7.00 | — | — | Yellow sparkle |
| `quick-overview-heading` | **text**: Quick Overview | 20 | 435 | 185 | 27 | -0.45 | section-title | 17 | #282E28 |
| `quick-overview-star` | **illustration**: Small black sparkle | 204 | 439 | 16 | 18 | +5.00 | — | — | Small black sparkle |
| `attention-summary` | **alert**: 3 items need attention | 18 | 470 | 354 | 40 | -0.25 | alert | — | — |
| `attention-summary-icon` | **icon**: Warning triangle | 29 | 480 | 22 | 21 | -2.00 | — | — | Warning triangle |
| `expiring-soon-card` | **card**: Expiring Soon · 2 items · within 24h | 18 | 518 | 354 | 67 | -0.35 | summary-card | — | — |
| `expiring-soon-icon` | **illustration**: Clock with sun | 28 | 528 | 51 | 47 | -1.00 | — | — | Clock with sun |
| `low-stock-card` | **card**: Low Stock · 4 items | 18 | 597 | 354 | 68 | +0.45 | summary-card | — | — |
| `low-stock-icon` | **illustration**: Carrot | 29 | 605 | 51 | 49 | +1.00 | — | — | Carrot |
| `almost-empty-card` | **card**: Almost Empty · 2 items | 18 | 675 | 354 | 65 | -0.25 | summary-card | — | — |
| `almost-empty-icon` | **illustration**: Bottle | 30 | 682 | 49 | 48 | -0.60 | — | — | Bottle |
| `bottom-navigation` | **navigation**: Home / Inventory / Add / Recipes / More | 0 | 752 | 390 | 78 | +0.00 | bottom-nav | — | Raised central Add action around 8pt above tab baseline. |


## add — Add Ingredient

Reference: [`03-add-ingredient.jpg`](rectified/03-add-ingredient.jpg)

Keep the name/image block side by side. Quantity and unit are distinct controls in one horizontal row. Storage Zone has three equal-ish selections, with Fridge selected.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 14 | 53 | 34 | 39 | -1.00 | — | — | Back |
| `page-title` | **text**: Add Ingredient | 103 | 54 | 194 | 37 | +0.40 | page-title | 22 | #282E28 |
| `ingredient-image-frame` | **illustration-frame**: Tomatoes | 20 | 127 | 139 | 124 | -0.50 | art-frame | — | Source shows tomatoes in a rounded, hand-outlined thumbnail box. |
| `ingredient-name` | **text**: Tomatoes | 178 | 144 | 132 | 35 | -0.70 | item-title | 15 | #282E28 |
| `ingredient-category-chip` | **chip**: Vegetable | 178 | 191 | 130 | 37 | +0.20 | category-chip | — | — |
| `leaf-doodle` | **illustration**: Leaf and red pen marks | 312 | 86 | 59 | 57 | +5.00 | — | — | Leaf and red pen marks |
| `quantity-label` | **text**: Quantity | 20 | 273 | 87 | 25 | -0.30 | field-label | 14 | #282E28 |
| `quantity-field` | **field**: 500 | 20 | 300 | 219 | 54 | -0.20 | text-field | — | — |
| `unit-picker` | **field**: g | 251 | 300 | 127 | 54 | +0.25 | picker | — | — |
| `storage-zone-label` | **text**: Storage Zone | 20 | 384 | 145 | 27 | +0.20 | field-label | 14 | #282E28 |
| `storage-pantry` | **segmented-option**: Pantry | 18 | 414 | 121 | 60 | -0.40 | storage-option | — | — |
| `storage-fridge` | **segmented-option**: Fridge | 145 | 413 | 121 | 62 | +0.35 | storage-selected | — | — |
| `storage-freezer` | **segmented-option**: Freezer | 273 | 414 | 99 | 60 | -0.30 | storage-option | — | — |
| `expiration-label` | **text**: Expiration Date | 20 | 501 | 154 | 28 | -0.45 | field-label | 14 | #282E28 |
| `expiration-picker` | **field**: Apr 20, 2026 | 18 | 530 | 355 | 63 | +0.10 | date-picker | — | — |
| `notes-label` | **text**: Notes (optional) | 20 | 620 | 154 | 29 | +0.10 | field-label | 14 | #282E28 |
| `notes-field` | **field**: e.g. organic, fresh, etc. | 18 | 651 | 355 | 70 | -0.15 | multiline-field | — | — |
| `save-button` | **button**: Save | 20 | 743 | 353 | 55 | -0.65 | primary-button | — | — |
| `save-label` | **text**: Save | 169 | 756 | 52 | 29 | +0.00 | button-label | 16 | #FBF4E5 |


## inventory — Inventory

Reference: [`04-inventory.jpg`](rectified/04-inventory.jpg)

Search/filter controls occupy the top; six compact item rows run at about 64pt vertical intervals. Bottom nav is visible in source.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `page-title` | **text**: Inventory | 129 | 54 | 132 | 35 | -0.65 | page-title | 22 | #282E28 |
| `back-button` | **icon-button**: Back | 14 | 52 | 35 | 38 | +0.00 | — | — | Back |
| `search-field` | **field**: Search... | 18 | 102 | 355 | 42 | -0.10 | search | — | — |
| `filter-all` | **chip**: All | 17 | 151 | 45 | 35 | -0.50 | filter-selected | — | — |
| `filter-fridge` | **chip**: Fridge | 65 | 151 | 64 | 35 | +0.30 | filter | — | — |
| `filter-pantry` | **chip**: Pantry | 133 | 151 | 64 | 35 | -0.40 | filter | — | — |
| `filter-freezer` | **chip**: Freezer | 202 | 151 | 79 | 35 | +0.20 | filter | — | — |
| `tomato-row` | **inventory-row**: Tomatoes · 50 g · Fridge · Exp: 2 days | 14 | 191 | 360 | 61 | -0.30 | inventory-row | — | — |
| `tomato-art` | **illustration**: Tomatoes | 19 | 195 | 50 | 51 | -0.60 | — | — | Tomatoes |
| `tomato-expiry-pill` | **status-pill**: Soon | 326 | 208 | 39 | 25 | +0.40 | expiry-pill | — | — |
| `eggs-row` | **inventory-row**: Eggs · 6 pcs · Fridge · Exp: 5 days | 14 | 255 | 360 | 61 | +0.35 | inventory-row | — | — |
| `eggs-art` | **illustration**: Eggs | 19 | 259 | 50 | 51 | +0.50 | — | — | Eggs |
| `spinach-row` | **inventory-row**: Spinach · 2 pcs · Fridge · Exp: 1 day | 14 | 319 | 360 | 61 | -0.25 | inventory-row | — | — |
| `spinach-art` | **illustration**: Spinach | 19 | 323 | 50 | 51 | -0.60 | — | — | Spinach |
| `spinach-expiry-pill` | **status-pill**: Soon | 326 | 335 | 39 | 25 | +0.35 | expiry-pill | — | — |
| `pasta-row` | **inventory-row**: Pasta · 50 g · Pantry · Exp: 6 months | 14 | 383 | 360 | 61 | +0.30 | inventory-row | — | — |
| `pasta-art` | **illustration**: Pasta | 19 | 387 | 50 | 51 | +0.50 | — | — | Pasta |
| `oil-row` | **inventory-row**: Olive Oil · 1 L · Pantry · Exp: 1 year | 14 | 447 | 360 | 61 | -0.20 | inventory-row | — | — |
| `oil-art` | **illustration**: Olive oil bottle | 19 | 451 | 50 | 51 | -0.50 | — | — | Olive oil bottle |
| `chicken-row` | **inventory-row**: Chicken Breast · 400 g · Fridge · Exp: 3 days | 14 | 511 | 360 | 61 | +0.40 | inventory-row | — | — |
| `chicken-art` | **illustration**: Chicken breast | 19 | 515 | 50 | 51 | +0.65 | — | — | Chicken breast |
| `chicken-expiry-pill` | **status-pill**: Soon | 326 | 529 | 39 | 25 | +0.25 | expiry-pill | — | — |
| `bottom-navigation` | **navigation**: Home / Inventory / Add / Recipes / More | 0 | 752 | 390 | 78 | +0.00 | bottom-nav | — | — |


## suggestions — Recipe Suggestions

Reference: [`05-recipe-suggestions.jpg`](rectified/05-recipe-suggestions.jpg)

Source has three stacked recommendation cards. “Ready Now” is a category/status label for first card and a small grouped section marker; avoid duplicating it visually. Main card extents overlap slightly with their internal title/info blocks by design.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 54 | 31 | 37 | -1.00 | — | — | Back |
| `page-title` | **text**: Recipe Suggestions | 61 | 54 | 306 | 40 | +0.75 | page-title | 22 | #282E28 |
| `tab-for-you` | **chip**: For You | 14 | 122 | 113 | 47 | -0.55 | filter-selected | — | — |
| `tab-by-ingredient` | **chip**: By Ingredient | 135 | 124 | 133 | 44 | +0.40 | filter | — | — |
| `tab-by-season` | **chip**: By Season | 271 | 124 | 99 | 44 | -0.25 | filter | — | — |
| `based-on-label` | **text**: Based on your kitchen | 20 | 197 | 194 | 27 | -0.35 | body-strong | 15 | #282E28 |
| `sort-picker` | **picker**: Sort: Best Match | 232 | 190 | 140 | 38 | +0.20 | compact-picker | — | — |
| `ready-now-heading` | **status-pill**: Ready Now | 81 | 250 | 116 | 35 | -0.15 | ready-pill | — | — |
| `tomato-pasta-card` | **recipe-card**: Tomato Pasta · 15 min · 3 servings | 14 | 232 | 360 | 151 | -0.35 | suggestion-card | — | — |
| `tomato-pasta-thumb` | **illustration**: Tomato Pasta bowl | 23 | 292 | 82 | 82 | -0.55 | — | — | Food must be illustrated in actual app; source mockup image here is photographic but pr... |
| `tomato-pasta-status` | **status-pill**: Ready Now | 80 | 251 | 112 | 28 | +0.30 | ready-pill | — | — |
| `tomato-pasta-title` | **text**: Tomato Pasta | 125 | 301 | 143 | 28 | -0.40 | item-title | 15 | #282E28 |
| `tomato-pasta-meta` | **text**: 15 min · 3 servings | 126 | 334 | 164 | 27 | +0.10 | metadata | 11.5 | #6B604F |
| `chicken-card` | **recipe-card**: Chicken Stir-fry · Missing: soy sauce (optional) | 14 | 391 | 360 | 140 | +0.35 | suggestion-card | — | — |
| `chicken-thumb` | **illustration**: Chicken Stir-fry bowl | 23 | 411 | 82 | 82 | +0.50 | — | — | Chicken Stir-fry bowl |
| `chicken-status` | **status-pill**: Almost Ready | 119 | 411 | 124 | 29 | -0.20 | almost-ready-pill | — | — |
| `chicken-title` | **text**: Chicken Stir-fry | 126 | 445 | 177 | 26 | +0.20 | item-title | 15 | #282E28 |
| `chicken-meta` | **text**: 25 min · 2 servings | 126 | 474 | 172 | 24 | -0.15 | metadata | 11.5 | #6B604F |
| `chicken-missing` | **text**: Missing: Soy Sauce (optional) | 125 | 501 | 224 | 22 | +0.40 | warning-metadata | 11.2 | #C96658 |
| `lentil-card` | **recipe-card**: Lentil Soup · Swap: chicken → lentils | 14 | 540 | 360 | 180 | -0.25 | suggestion-card | — | — |
| `lentil-thumb` | **illustration**: Lentil soup bowl | 23 | 556 | 82 | 82 | -0.40 | — | — | Lentil soup bowl |
| `lentil-status` | **status-pill**: Smart Swap | 120 | 574 | 111 | 29 | +0.25 | smart-swap-pill | — | — |
| `lentil-title` | **text**: Lentil Soup | 126 | 611 | 132 | 26 | -0.30 | item-title | 15 | #282E28 |
| `lentil-meta` | **text**: 40 min · 4 servings | 126 | 640 | 172 | 24 | +0.15 | metadata | 11.5 | #6B604F |
| `lentil-swap-line` | **text**: Swap: chicken → lentils | 126 | 670 | 210 | 22 | +0.35 | swap-metadata | 11.3 | #B87937 |
| `view-all-button` | **button**: View All Suggestions | 11 | 735 | 340 | 62 | -0.55 | primary-button | — | — |
| `view-all-label` | **text**: View All Suggestions | 83 | 752 | 222 | 30 | -0.20 | button-label | 16 | #FBF4E5 |


## detail — Tomato Pasta detail

Reference: [`06-tomato-pasta.jpg`](rectified/06-tomato-pasta.jpg)

The hero occupies about one fifth of the viewport. Ingredient amounts are right-aligned; ingredient icon columns are aligned on a shared x-axis.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `hero-dish` | **illustration-frame**: Tomato Pasta in plate | 14 | 54 | 359 | 171 | -0.20 | hero-art | — | Reference shows hero image spanning nearly full content width. For FoodSafe product, re... |
| `back-button` | **icon-button**: Back | 20 | 68 | 49 | 51 | -3.00 | — | — | Back |
| `favorite-button` | **icon-button**: Favorite heart | 323 | 68 | 48 | 50 | +2.00 | — | — | Favorite heart |
| `recipe-title` | **text**: Tomato Pasta | 15 | 234 | 254 | 43 | -0.80 | recipe-title | 27 | #282E28 |
| `ready-now-chip` | **chip**: Ready Now | 18 | 286 | 137 | 38 | -0.30 | ready-pill | — | — |
| `time-meta` | **text**: 15 min · 3 servings | 179 | 294 | 185 | 28 | +0.40 | metadata | 11.5 | #6B604F |
| `ingredients-heading` | **text**: Ingredients | 21 | 350 | 142 | 30 | -0.35 | section-title | 17 | #282E28 |
| `add-ingredient-symbol` | **icon**: Plus | 348 | 353 | 19 | 19 | +0.00 | — | — | Plus |
| `ingredient-list-container` | **card**: Ingredient list container | 22 | 383 | 344 | 341 | -0.20 | list-container | — | — |
| `ingredient-pasta` | **list-row**: Pasta · 300 g | 26 | 390 | 331 | 47 | -0.20 | ingredient-row | — | — |
| `ingredient-pasta-art` | **illustration**: Pasta | 40 | 394 | 31 | 37 | -0.50 | — | — | Pasta |
| `ingredient-tomatoes` | **list-row**: Tomatoes · 400 g | 26 | 438 | 331 | 47 | +0.30 | ingredient-row | — | — |
| `ingredient-tomatoes-art` | **illustration**: Tomato | 40 | 442 | 31 | 37 | +0.40 | — | — | Tomato |
| `ingredient-oil` | **list-row**: Olive oil · 30 ml | 26 | 486 | 331 | 47 | -0.30 | ingredient-row | — | — |
| `ingredient-oil-art` | **illustration**: Oil bottle | 40 | 490 | 31 | 37 | -0.50 | — | — | Oil bottle |
| `ingredient-garlic` | **list-row**: Garlic · 2 cloves | 26 | 534 | 331 | 47 | +0.25 | ingredient-row | — | — |
| `ingredient-garlic-art` | **illustration**: Garlic | 40 | 538 | 31 | 37 | +0.50 | — | — | Garlic |
| `ingredient-basil` | **list-row**: Basil · 10 g | 26 | 582 | 331 | 47 | -0.20 | ingredient-row | — | — |
| `ingredient-basil-art` | **illustration**: Basil leaf | 40 | 586 | 31 | 37 | -0.60 | — | — | Basil leaf |
| `ingredient-salt` | **list-row**: Salt · 1 g | 26 | 630 | 331 | 43 | +0.30 | ingredient-row | — | — |
| `ingredient-salt-art` | **illustration**: Salt | 40 | 633 | 31 | 34 | +0.30 | — | — | Salt |
| `ingredient-pepper` | **list-row**: Pepper · 2 g | 26 | 674 | 331 | 43 | -0.25 | ingredient-row | — | — |
| `ingredient-pepper-art` | **illustration**: Pepper | 40 | 677 | 31 | 34 | -0.50 | — | — | Pepper |
| `start-cooking-button` | **button**: Start Cooking | 28 | 740 | 324 | 65 | -0.40 | primary-button | — | — |
| `chef-hat-icon` | **illustration**: Chef hat | 272 | 752 | 36 | 39 | +1.00 | — | — | Chef hat |


## cooking — Cooking step

Reference: [`07-cooking.jpg`](rectified/07-cooking.jpg)

Cooking illustration should preserve the source composition of a round pan seen from above with visible pasta/sauce; text instructions occupy four compact lines and should not become modern oversized body copy.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 53 | 33 | 37 | -1.00 | — | — | Back |
| `page-title` | **text**: Cooking… | 120 | 54 | 154 | 39 | +0.65 | page-title | 22 | #282E28 |
| `recipe-step-card` | **card**: Tomato Pasta · Step 2 of 7 | 18 | 99 | 352 | 87 | -0.35 | recipe-step-card | — | — |
| `recipe-step-icon` | **illustration**: Recipe card icon | 33 | 119 | 48 | 57 | -1.00 | — | — | Recipe card icon |
| `recipe-step-title` | **text**: Tomato Pasta | 96 | 119 | 181 | 29 | -0.25 | item-title | 15 | #282E28 |
| `recipe-step-count` | **text**: Step 2 of 7 | 98 | 153 | 119 | 26 | +0.25 | metadata | 11.5 | #6B604F |
| `hero-pan` | **illustration-frame**: Tomato sauce in pan | 29 | 193 | 341 | 203 | +0.15 | cooking-art | — | Must be drawn pan and drawn food, never photograph. |
| `step-heading` | **text**: 2. Cook the pasta | 28 | 414 | 285 | 41 | -0.65 | recipe-title-small | 21 | #282E28 |
| `instruction-line-1` | **text**: Bring a large pot of salted water to | 29 | 466 | 330 | 30 | -0.15 | body-copy | 14 | #282E28 |
| `instruction-line-2` | **text**: a boil. Add pasta and cook for 8–10 | 29 | 499 | 334 | 30 | +0.15 | body-copy | 14 | #282E28 |
| `instruction-line-3` | **text**: minutes (or according to package | 29 | 531 | 335 | 30 | -0.10 | body-copy | 14 | #282E28 |
| `instruction-line-4` | **text**: instructions). | 29 | 563 | 188 | 28 | +0.15 | body-copy | 14 | #282E28 |
| `cooking-progress` | **progress**: Cooking progress bar | 29 | 620 | 242 | 17 | +0.00 | progress | — | — |
| `timer-text` | **text**: 03:42 left | 283 | 615 | 81 | 25 | +0.00 | metadata | 11.5 | #6B604F |
| `scaled-banner` | **card**: Scaled for 3 servings | 21 | 661 | 350 | 54 | -0.20 | success-banner | — | — |
| `back-button-bottom` | **button**: Back | 20 | 742 | 159 | 71 | -0.45 | secondary-button | — | — |
| `next-button` | **button**: Next | 195 | 742 | 176 | 71 | -0.55 | primary-button | — | — |


## scaling — Portion Scaling

Reference: [`08-portion-scaling.jpg`](rectified/08-portion-scaling.jpg)

One serving selector is selected (3) in green. The quantitative rows repeat exactly the same left icon and name column and right-aligned quantities.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 54 | 34 | 39 | -1.00 | — | — | Back |
| `page-title` | **text**: Portion Scaling | 90 | 58 | 221 | 39 | -0.70 | page-title | 22 | #282E28 |
| `recipe-summary-card` | **card**: Tomato Pasta | 17 | 128 | 352 | 86 | -0.25 | recipe-summary | — | — |
| `recipe-summary-art` | **illustration**: Tomato Pasta thumbnail | 26 | 145 | 50 | 53 | -0.45 | — | — | Tomato Pasta thumbnail |
| `recipe-summary-name` | **text**: Tomato Pasta | 91 | 153 | 181 | 31 | -0.20 | item-title | 15 | #282E28 |
| `servings-label` | **text**: Adjust servings | 23 | 238 | 187 | 29 | -0.45 | section-title | 17 | #282E28 |
| `serving-1` | **chip**: 1 | 21 | 280 | 81 | 67 | -0.45 | serving-option | — | — |
| `serving-2` | **chip**: 2 | 111 | 280 | 81 | 67 | +0.45 | serving-option | — | — |
| `serving-3` | **chip**: 3 | 200 | 278 | 81 | 70 | -0.20 | serving-selected | — | — |
| `serving-4` | **chip**: 4 | 289 | 280 | 81 | 67 | +0.35 | serving-option | — | — |
| `adjusted-quantities-heading` | **text**: Adjusted Quantities | 23 | 379 | 223 | 30 | -0.35 | section-title | 17 | #282E28 |
| `quantities-list` | **card**: Adjusted ingredients list | 21 | 415 | 349 | 310 | -0.25 | list-container | — | — |
| `qty-pasta` | **list-row**: Pasta · 300 g | 27 | 421 | 336 | 59 | -0.15 | ingredient-row | — | — |
| `qty-pasta-art` | **illustration**: Pasta | 35 | 430 | 39 | 41 | -0.60 | — | — | Pasta |
| `qty-tomatoes` | **list-row**: Tomatoes · 400 g | 27 | 480 | 336 | 59 | +0.25 | ingredient-row | — | — |
| `qty-tomatoes-art` | **illustration**: Tomato | 35 | 488 | 39 | 42 | +0.30 | — | — | Tomato |
| `qty-oil` | **list-row**: Olive oil · 30 ml | 27 | 539 | 336 | 59 | -0.30 | ingredient-row | — | — |
| `qty-oil-art` | **illustration**: Oil bottle | 35 | 547 | 39 | 42 | -0.50 | — | — | Oil bottle |
| `qty-garlic` | **list-row**: Garlic · 2 cloves | 27 | 598 | 336 | 59 | +0.25 | ingredient-row | — | — |
| `qty-garlic-art` | **illustration**: Garlic | 35 | 606 | 39 | 42 | +0.50 | — | — | Garlic |
| `qty-basil` | **list-row**: Basil · 10 g | 27 | 657 | 336 | 59 | -0.20 | ingredient-row | — | — |
| `qty-basil-art` | **illustration**: Basil leaf | 35 | 665 | 39 | 42 | -0.50 | — | — | Basil leaf |
| `update-recipe-button` | **button**: Update Recipe | 14 | 736 | 348 | 66 | -0.45 | primary-button | — | — |


## swaps — Ingredient Swaps

Reference: [`09-ingredient-swaps.jpg`](rectified/09-ingredient-swaps.jpg)

Four tall choice rows: artwork left, name and helper copy center-left, radio/check at right. Lime is selected in the reference.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 53 | 34 | 38 | -1.00 | — | — | Back |
| `page-title` | **text**: Ingredient Swaps | 82 | 55 | 232 | 36 | +0.60 | page-title | 22 | #282E28 |
| `intro` | **text**: Try these swaps | 20 | 124 | 165 | 26 | -0.30 | body-strong | 15 | #282E28 |
| `swap-lemon` | **swap-row**: Lemon | 18 | 153 | 354 | 65 | -0.25 | swap-option | — | — |
| `swap-lemon-art` | **illustration**: Lemon | 31 | 162 | 45 | 45 | -0.50 | — | — | Lemon |
| `swap-lemon-note` | **text**: can be swapped with: | 86 | 182 | 154 | 19 | +0.00 | metadata | 11.5 | #6B604F |
| `swap-lime` | **swap-row**: Lime | 18 | 224 | 354 | 65 | +0.30 | swap-selected | — | — |
| `swap-lime-art` | **illustration**: Lime | 31 | 233 | 45 | 45 | +0.50 | — | — | Lime |
| `swap-lime-check` | **icon**: Selected check | 338 | 243 | 20 | 20 | +0.00 | — | — | Selected check |
| `swap-vinegar` | **swap-row**: Vinegar | 18 | 295 | 354 | 65 | -0.20 | swap-option | — | — |
| `swap-vinegar-art` | **illustration**: Vinegar bottle | 31 | 304 | 45 | 45 | -0.50 | — | — | Vinegar bottle |
| `swap-vinegar-radio` | **icon**: Radio outline | 339 | 318 | 18 | 18 | +0.00 | — | — | Radio outline |
| `swap-orange` | **swap-row**: Orange | 18 | 366 | 354 | 65 | +0.25 | swap-option | — | — |
| `swap-orange-art` | **illustration**: Orange | 31 | 375 | 45 | 45 | +0.50 | — | — | Orange |
| `swap-orange-radio` | **icon**: Radio outline | 339 | 389 | 18 | 18 | +0.00 | — | — | Radio outline |
| `why-heading` | **text**: Why? | 20 | 456 | 84 | 27 | -0.40 | section-title | 17 | #282E28 |
| `why-line-1` | **text**: ✓ Similar acidity and flavor profile. | 20 | 490 | 321 | 22 | -0.10 | body-copy | 14 | #282E28 |
| `why-line-2` | **text**: ✓ Works in the same type of recipes. | 20 | 516 | 332 | 23 | +0.15 | body-copy | 14 | #282E28 |
| `use-lime-button` | **button**: Use Lime Instead | 21 | 744 | 350 | 56 | -0.45 | primary-button | — | — |


## meals — Meal Suggestions

Reference: [`10-meal-suggestions.jpg`](rectified/10-meal-suggestions.jpg)

The fourth card is partially clipped by the bottom of the screenshot, with no visible bottom navigation. Do not compress the four cards equally to force all content above the fold.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 53 | 34 | 39 | -1.00 | — | — | Back |
| `page-title` | **text**: Meal Suggestions | 59 | 54 | 275 | 38 | -0.45 | page-title | 22 | #282E28 |
| `ready-tab` | **chip**: Ready Now (2) | 4 | 128 | 129 | 51 | -0.40 | filter-selected | — | — |
| `almost-tab` | **chip**: Almost Ready (1) | 137 | 129 | 120 | 50 | +0.35 | filter | — | — |
| `swap-tab` | **chip**: Smart Swap (1) | 263 | 129 | 111 | 50 | -0.25 | filter | — | — |
| `meal-card-pasta` | **meal-card**: Tomato Pasta · 15 min · 3 servings | 8 | 208 | 365 | 159 | -0.20 | meal-card | — | — |
| `meal-pasta-status` | **status-pill**: Ready Now | 15 | 220 | 116 | 37 | -0.20 | ready-pill | — | — |
| `meal-pasta-thumb` | **illustration**: Tomato Pasta bowl | 14 | 264 | 111 | 89 | -0.55 | — | — | Tomato Pasta bowl |
| `meal-pasta-title` | **text**: Tomato Pasta | 143 | 225 | 183 | 29 | -0.30 | item-title | 15 | #282E28 |
| `meal-pasta-meta` | **text**: 15 min · 3 servings | 142 | 264 | 207 | 25 | +0.10 | metadata | 11.5 | #6B604F |
| `meal-pasta-availability` | **text**: All ingredients available | 142 | 309 | 215 | 25 | -0.15 | metadata | 11.5 | #6B604F |
| `meal-card-chicken` | **meal-card**: Chicken Stir-fry · 25 min · 2 servings | 8 | 378 | 365 | 153 | +0.35 | meal-card | — | — |
| `meal-chicken-status` | **status-pill**: Ready Now | 15 | 389 | 116 | 37 | +0.20 | ready-pill | — | — |
| `meal-chicken-thumb` | **illustration**: Chicken Stir-fry bowl | 14 | 434 | 111 | 88 | +0.55 | — | — | Chicken Stir-fry bowl |
| `meal-chicken-title` | **text**: Chicken Stir-fry | 143 | 394 | 203 | 30 | +0.20 | item-title | 15 | #282E28 |
| `meal-chicken-meta` | **text**: 25 min · 2 servings | 142 | 433 | 207 | 25 | -0.15 | metadata | 11.5 | #6B604F |
| `meal-card-curry` | **meal-card**: Vegetable Curry · Missing coconut milk (optional) | 8 | 539 | 365 | 160 | -0.20 | meal-card | — | — |
| `meal-curry-status` | **status-pill**: Almost Ready | 15 | 550 | 126 | 36 | -0.25 | almost-ready-pill | — | — |
| `meal-curry-thumb` | **illustration**: Vegetable curry bowl | 14 | 595 | 111 | 91 | -0.40 | — | — | Vegetable curry bowl |
| `meal-curry-title` | **text**: Vegetable Curry | 143 | 554 | 207 | 30 | -0.20 | item-title | 15 | #282E28 |
| `meal-curry-meta` | **text**: 35 min · 3 servings | 142 | 592 | 205 | 25 | +0.20 | metadata | 11.5 | #6B604F |
| `meal-curry-missing` | **text**: Missing: coconut milk (optional) | 142 | 630 | 217 | 30 | +0.40 | warning-metadata | 11.2 | #C96658 |
| `meal-card-lentil` | **meal-card**: Lentil Soup · Swap: chicken → lentils | 8 | 707 | 365 | 137 | +0.25 | meal-card | — | Reference card continues below the visible bottom edge; preserve source clipping/scroll... |
| `meal-lentil-status` | **status-pill**: Smart Swap | 15 | 720 | 124 | 36 | +0.10 | smart-swap-pill | — | — |
| `meal-lentil-thumb` | **illustration**: Lentil soup bowl | 14 | 764 | 111 | 75 | +0.50 | — | — | Lentil soup bowl |
| `meal-lentil-title` | **text**: Lentil Soup | 143 | 725 | 190 | 30 | -0.20 | item-title | 15 | #282E28 |
| `meal-lentil-meta` | **text**: 40 min · 4 servings | 142 | 762 | 205 | 25 | +0.15 | metadata | 11.5 | #6B604F |


## lentil — Lentil Soup / Steps

Reference: [`11-lentil-soup.jpg`](rectified/11-lentil-soup.jpg)

Selected tab is Steps. Step numbers are small green filled circles; the text is compact and left-aligned with one-line title and one-line supporting instruction.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 53 | 33 | 39 | -1.00 | — | — | Back |
| `page-title` | **text**: Lentil Soup | 64 | 55 | 203 | 38 | +0.65 | page-title | 22 | #282E28 |
| `hero-dish` | **illustration-frame**: Lentil soup bowl | 15 | 101 | 356 | 85 | -0.30 | hero-art | — | — |
| `smart-swap-label` | **status-pill**: Smart Swap | 17 | 192 | 101 | 28 | -0.20 | smart-swap-pill | — | — |
| `time-meta` | **text**: 40 min · 4 servings | 126 | 193 | 171 | 26 | +0.20 | metadata | 11.5 | #6B604F |
| `tab-ingredients` | **segmented-option**: Ingredients | 18 | 245 | 177 | 40 | -0.20 | segmented | — | — |
| `tab-steps` | **segmented-option**: Steps | 196 | 245 | 175 | 40 | +0.25 | segmented-selected | — | — |
| `step-1-number` | **step-number**: 1 | 14 | 296 | 26 | 28 | +0.00 | — | — | 1 |
| `step-1-title` | **text**: Prep vegetables | 48 | 295 | 150 | 22 | -0.20 | item-title-small | 13 | #282E28 |
| `step-1-copy` | **text**: Chop onion, carrot, celery. | 48 | 316 | 246 | 19 | +0.10 | metadata | 11.5 | #6B604F |
| `step-2-number` | **step-number**: 2 | 14 | 354 | 26 | 28 | +0.00 | — | — | 2 |
| `step-2-title` | **text**: Sauté | 48 | 354 | 91 | 22 | +0.20 | item-title-small | 13 | #282E28 |
| `step-2-copy` | **text**: Cook in olive oil for 5 minutes. | 48 | 375 | 278 | 19 | -0.10 | metadata | 11.5 | #6B604F |
| `step-3-number` | **step-number**: 3 | 14 | 413 | 26 | 28 | +0.00 | — | — | 3 |
| `step-3-title` | **text**: Add lentils & broth | 48 | 413 | 187 | 22 | -0.20 | item-title-small | 13 | #282E28 |
| `step-3-copy` | **text**: Simmer for 25 minutes. | 48 | 434 | 224 | 19 | +0.15 | metadata | 11.5 | #6B604F |
| `step-4-number` | **step-number**: 4 | 14 | 472 | 26 | 28 | +0.00 | — | — | 4 |
| `step-4-title` | **text**: Season | 48 | 472 | 90 | 22 | +0.20 | item-title-small | 13 | #282E28 |
| `step-4-copy` | **text**: Add salt, pepper, herbs. | 48 | 493 | 224 | 19 | -0.10 | metadata | 11.5 | #6B604F |
| `start-cooking-button` | **button**: Start Cooking | 15 | 793 | 356 | 50 | -0.40 | primary-button | — | — |


## expiry — Expiration Priority

Reference: [`12-expiration-priority.jpg`](rectified/12-expiration-priority.jpg)

Alert panel first, then three priority rows and a highlighted tips card. There is no persistent bottom navigation visible in this reference screen.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `back-button` | **icon-button**: Back | 18 | 54 | 33 | 37 | -1.00 | — | — | Back |
| `page-title` | **text**: Expiration Priority | 56 | 55 | 280 | 38 | -0.40 | page-title | 22 | #282E28 |
| `alert-card` | **alert**: 3 items need to be used within 24–48 hours | 12 | 101 | 366 | 75 | -0.30 | critical-alert | — | — |
| `alert-icon` | **icon**: Warning triangle | 21 | 115 | 27 | 29 | -1.00 | — | — | Warning triangle |
| `spinach-priority` | **priority-row**: Spinach · Expires in 1 day | 14 | 184 | 362 | 71 | +0.25 | priority-row | — | — |
| `spinach-priority-art` | **illustration**: Spinach leaves | 20 | 188 | 52 | 60 | -0.60 | — | — | Spinach leaves |
| `spinach-checkbox` | **checkbox**:  | 342 | 206 | 18 | 18 | -1.00 | — | — | — |
| `beef-priority` | **priority-row**: Ground Beef · Expires in 1 day | 14 | 260 | 362 | 71 | -0.25 | priority-row | — | — |
| `beef-priority-art` | **illustration**: Ground beef | 20 | 264 | 52 | 60 | +0.45 | — | — | Ground beef |
| `beef-checkbox` | **checkbox**:  | 342 | 282 | 18 | 18 | +1.00 | — | — | — |
| `mozzarella-priority` | **priority-row**: Mozzarella Cheese · Expires in 2 days | 14 | 336 | 362 | 71 | +0.30 | priority-row | — | — |
| `mozzarella-priority-art` | **illustration**: Mozzarella cheese | 20 | 340 | 52 | 60 | -0.50 | — | — | Mozzarella cheese |
| `mozzarella-checkbox` | **checkbox**:  | 342 | 358 | 18 | 18 | -1.00 | — | — | — |
| `tips-card` | **card**: Tips · Use these ingredients first to reduce food waste! | 16 | 423 | 358 | 113 | -0.25 | tip-card | — | — |
| `tips-icon` | **illustration**: Lightbulb | 26 | 436 | 33 | 35 | -1.00 | — | — | Lightbulb |
| `tips-title` | **text**: Tips | 64 | 435 | 70 | 25 | -0.20 | section-title | 17 | #282E28 |
| `tips-copy-line-1` | **text**: Use these ingredients first | 30 | 471 | 270 | 22 | -0.20 | body-copy | 14 | #282E28 |
| `tips-copy-line-2` | **text**: to reduce food waste! | 30 | 495 | 242 | 22 | +0.10 | body-copy | 14 | #282E28 |


## settings — Settings

Reference: [`13-settings.jpg`](rectified/13-settings.jpg)

**Occlusion note:** the lower-right is partially hidden by a yellow presentation sticky note in the original board; that note is not app UI. Use the Home tab-bar geometry to infer obscured navigation details.

Handwritten explanatory text under the phone and the sticky-note card overlapping the source collage are annotations, not in-app content. Omit them in the actual screen.

| Element ID | Component / text | x | y | w | h | θ° | Font | Size pt | Color / asset / note |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-row` | **status**: 9:41 | 27 | 16 | 331 | 23 | +0.00 | status | 10.5 | #282E28 |
| `settings-gear` | **icon**: Settings gear | 19 | 52 | 31 | 33 | -1.00 | — | — | Settings gear |
| `page-title` | **text**: Settings | 55 | 54 | 120 | 37 | +0.45 | page-title | 22 | #282E28 |
| `storage-zones-row` | **settings-row**: Storage Zones · Pantry, Fridge, Freezer | 16 | 108 | 357 | 75 | -0.25 | settings-row | — | — |
| `storage-zones-icon` | **icon**: Storage cabinet | 26 | 125 | 28 | 32 | -0.50 | — | — | Storage cabinet |
| `storage-zones-title` | **text**: Storage Zones | 62 | 119 | 171 | 24 | -0.25 | item-title | 15 | #282E28 |
| `storage-zones-subtitle` | **text**: Pantry, Fridge, Freezer | 62 | 146 | 205 | 20 | +0.10 | metadata | 11.5 | #6B604F |
| `units-row` | **settings-row**: Units · Grams, milliliters, pieces | 16 | 190 | 357 | 75 | +0.30 | settings-row | — | — |
| `units-icon` | **icon**: Measurement units | 26 | 207 | 28 | 32 | +0.50 | — | — | Measurement units |
| `units-title` | **text**: Units | 62 | 202 | 95 | 24 | +0.20 | item-title | 15 | #282E28 |
| `units-subtitle` | **text**: Grams, milliliters, pieces | 62 | 229 | 212 | 20 | -0.10 | metadata | 11.5 | #6B604F |
| `offline-row` | **settings-row**: Offline Mode · Works without internet | 16 | 272 | 357 | 75 | -0.20 | settings-row | — | — |
| `offline-icon` | **icon**: Offline symbol | 26 | 289 | 28 | 32 | -0.50 | — | — | Offline symbol |
| `offline-title` | **text**: Offline Mode | 62 | 284 | 142 | 24 | -0.15 | item-title | 15 | #282E28 |
| `offline-subtitle` | **text**: Works without internet | 62 | 310 | 192 | 20 | +0.15 | metadata | 11.5 | #6B604F |
| `offline-toggle` | **toggle**: On | 320 | 295 | 44 | 26 | +0.00 | — | — | — |
| `about-row` | **settings-row**: About · Version 1.0.0 | 16 | 354 | 357 | 75 | +0.25 | settings-row | — | — |
| `about-icon` | **icon**: About / information | 26 | 371 | 28 | 32 | +0.45 | — | — | About / information |
| `about-title` | **text**: About | 62 | 367 | 95 | 24 | +0.10 | item-title | 15 | #282E28 |
| `about-subtitle` | **text**: Version 1.0.0 | 62 | 394 | 140 | 20 | -0.15 | metadata | 11.5 | #6B604F |
| `bottom-navigation` | **navigation**: Home / Inventory / Add / Recipes / More | 0 | 752 | 390 | 78 | +0.00 | bottom-nav | — | — |


## Native iOS mapping rules

1. Use these 390×844 rectangles as the visual calibration canvas, not as literal absolute `frame` calls for every device. Implement the layouts with stable container relationships (header, stack, rows, bottom anchored content) and use these coordinates as the source reference for preview snapshots at exactly 390×844.
2. The screenshot is a collage with phone perspective; the perspective matrices rectify each panel. Do not reproduce the outer phone frame, board annotations, sticky notes, arrows, or captions as app UI.
3. To rebuild per-screen layout, compare the corresponding rectified JPEG and source-corner coordinates. Maintain ±6 pt horizontal and ±8 pt vertical tolerance initially, then refine visually.
4. For text, fit font size to visible ink-height and line wrap. The bounding box is a text container placement; it is not the exact ink glyph bounds. Maintain the source line breaks, especially on Welcome, cooking instructions, and small helper text.
5. For buttons, report both visible bounds and hit area: rotate only the visual shell/label a few tenths of a degree; keep the hit-target container aligned and >=44×44 pt.
6. Illustration-only art direction takes precedence over photos shown in the original mockup. Keep each illustration in the same rectangle/shape/composition as the source image, but replace realistic images with hand-drawn watercolor/colored-pencil artwork.
