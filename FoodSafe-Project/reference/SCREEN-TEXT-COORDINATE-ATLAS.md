# FoodSafe individual text-run atlas

This file maps each distinct visible text line to a bounding box, rotation, font size, color and role. Coordinates refer to the corresponding perspective-rectified 390×844 crop and represent text boxes, not exact pixel-level ink outlines. The source does not include editable text, so values are estimates with a conservative ±5pt placement tolerance. See `SCREEN-COORDINATE-MASTER.json` for the component bounds and homography.

## Shared rule

The same `FoodSafe Hand` family is used everywhere. Sizes vary by role, but there are no sans-serif body/control exceptions. Real iOS status bars are controlled by the OS.

## welcome — Welcome / onboarding

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `tagline-1` | Good food. | 101 | 243 | 192 | 37 | -1.00 | tagline | 22 | `#315C43` |
| `tagline-2` | Less waste. | 101 | 278 | 204 | 37 | -1.20 | tagline | 22 | `#315C43` |
| `support-1` | Your Kitchen. | 61 | 590 | 234 | 33 | -2.20 | support | 18 | `#514B3E` |
| `support-2` | Your ingredients. | 73 | 620 | 224 | 34 | -2.20 | support | 18 | `#514B3E` |
| `support-3` | Better meals. | 88 | 654 | 182 | 33 | -2.00 | support | 18 | `#514B3E` |
| `get-started` | Get Started | 95 | 730 | 188 | 28 | -0.40 | button-label | 16 | `#FBF4E5` |
| `sign-in` | Sign In | 147 | 790 | 91 | 25 | +0.60 | secondary-action | 14 | `#315C43` |

## home — My Kitchen

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 29 | 18 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | My Kitchen | 91 | 51 | 160 | 34 | -0.80 | page-title | 22 | `#282E28` |
| `zone-fridge` | Fridge | 40 | 124 | 70 | 27 | -0.50 | chip-label | 12 | `#282E28` |
| `zone-pantry` | Pantry | 162 | 126 | 71 | 25 | +0.40 | chip-label | 12 | `#282E28` |
| `zone-freezer` | Freezer | 281 | 124 | 75 | 27 | -0.20 | chip-label | 12 | `#282E28` |
| `search-placeholder` | Search ingredients… | 76 | 191 | 235 | 24 | -0.10 | metadata | 11.5 | `#6B604F` |
| `category-vegetables` | Vegetables | 28 | 307 | 68 | 16 | -0.50 | category-label | 11.5 | `#282E28` |
| `category-fruits` | Fruits | 137 | 307 | 45 | 16 | +0.40 | category-label | 11.5 | `#282E28` |
| `category-dairy` | Dairy | 233 | 307 | 41 | 16 | -0.30 | category-label | 11.5 | `#282E28` |
| `category-grains` | Grains | 316 | 307 | 45 | 16 | +0.50 | category-label | 11.5 | `#282E28` |
| `category-proteins` | Proteins | 30 | 404 | 64 | 16 | +0.30 | category-label | 11.5 | `#282E28` |
| `category-others` | Others | 135 | 404 | 48 | 16 | -0.40 | category-label | 11.5 | `#282E28` |
| `category-leaves` | Leaves | 222 | 404 | 62 | 16 | +0.30 | category-label | 11.5 | `#282E28` |
| `quick-overview` | Quick Overview | 20 | 436 | 176 | 23 | -0.45 | section-title | 17 | `#282E28` |
| `attention-summary` | 3 items need attention | 68 | 478 | 222 | 23 | -0.20 | alert-label | 12.5 | `#C96658` |
| `expiring-title` | Expiring Soon | 86 | 530 | 126 | 20 | -0.20 | item-title | 15 | `#282E28` |
| `expiring-sub` | 2 items · within 24h | 86 | 552 | 150 | 18 | +0.20 | metadata | 11.5 | `#6B604F` |
| `low-stock-title` | Low Stock | 86 | 608 | 105 | 20 | +0.20 | item-title | 15 | `#282E28` |
| `low-stock-sub` | 4 items | 86 | 632 | 74 | 17 | -0.10 | metadata | 11.5 | `#6B604F` |
| `almost-empty-title` | Almost Empty | 86 | 686 | 136 | 20 | -0.20 | item-title | 15 | `#282E28` |
| `almost-empty-sub` | 2 items | 86 | 709 | 76 | 17 | +0.20 | warning-metadata | 11.2 | `#C96658` |
| `tab-home` | Home | 26 | 807 | 34 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-inventory` | Inventory | 86 | 807 | 62 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-recipes` | Recipes | 251 | 807 | 52 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-more` | More | 332 | 807 | 34 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |

## add — Add Ingredient

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Add Ingredient | 101 | 57 | 193 | 31 | +0.40 | page-title | 22 | `#282E28` |
| `tomato-name` | Tomatoes | 178 | 145 | 131 | 31 | -0.70 | item-title | 15 | `#282E28` |
| `vegetable-chip` | Vegetable | 206 | 199 | 80 | 20 | +0.20 | chip-label | 12 | `#282E28` |
| `quantity-label` | Quantity | 20 | 276 | 88 | 20 | -0.30 | field-label | 14 | `#282E28` |
| `quantity-value` | 500 | 39 | 312 | 43 | 28 | -0.20 | field-value | 15 | `#282E28` |
| `unit-value` | g | 276 | 313 | 19 | 26 | +0.00 | field-value | 15 | `#282E28` |
| `storage-label` | Storage Zone | 20 | 386 | 144 | 22 | +0.20 | field-label | 14 | `#282E28` |
| `storage-pantry` | Pantry | 62 | 434 | 55 | 25 | -0.40 | chip-label | 12 | `#282E28` |
| `storage-fridge` | Fridge | 186 | 433 | 62 | 25 | +0.35 | chip-label | 12 | `#282E28` |
| `storage-freezer` | Freezer | 293 | 434 | 67 | 25 | -0.30 | chip-label | 12 | `#282E28` |
| `expiration-label` | Expiration Date | 20 | 504 | 151 | 22 | -0.45 | field-label | 14 | `#282E28` |
| `expiration-value` | Apr 20, 2026 | 80 | 552 | 139 | 25 | +0.10 | field-value | 15 | `#282E28` |
| `notes-label` | Notes | 20 | 622 | 55 | 22 | +0.10 | field-label | 14 | `#282E28` |
| `notes-optional` | (optional) | 79 | 625 | 72 | 18 | +0.00 | metadata | 11.5 | `#6B604F` |
| `notes-placeholder` | e.g. organic, fresh, etc. | 28 | 666 | 245 | 23 | -0.10 | metadata | 11.5 | `#6B604F` |
| `save-label` | Save | 171 | 759 | 50 | 24 | +0.00 | button-label | 16 | `#FBF4E5` |

## inventory — Inventory

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Inventory | 129 | 57 | 132 | 29 | -0.65 | page-title | 22 | `#282E28` |
| `search-placeholder` | Search… | 48 | 111 | 108 | 21 | +0.00 | metadata | 11.5 | `#6B604F` |
| `filter-all` | All | 28 | 159 | 24 | 18 | -0.50 | chip-label | 12 | `#282E28` |
| `filter-fridge` | Fridge | 80 | 159 | 39 | 18 | +0.30 | chip-label | 12 | `#282E28` |
| `filter-pantry` | Pantry | 149 | 159 | 43 | 18 | -0.40 | chip-label | 12 | `#282E28` |
| `filter-freezer` | Freezer | 218 | 159 | 50 | 18 | +0.20 | chip-label | 12 | `#282E28` |
| `tomato-soon` | Soon | 334 | 212 | 28 | 14 | +0.40 | warning-metadata | 11.2 | `#C96658` |
| `tomato-name` | Tomatoes | 70 | 199 | 90 | 17 | -0.20 | item-title | 15 | `#282E28` |
| `tomato-meta` | 50 g · Fridge | 70 | 216 | 105 | 14 | +0.00 | metadata | 11.5 | `#6B604F` |
| `tomato-exp` | Exp: 2 days | 70 | 231 | 92 | 14 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `eggs-name` | Eggs | 70 | 263 | 52 | 17 | +0.20 | item-title | 15 | `#282E28` |
| `eggs-meta` | 6 pcs · Fridge | 70 | 279 | 109 | 14 | +0.00 | metadata | 11.5 | `#6B604F` |
| `eggs-exp` | Exp: 5 days | 70 | 294 | 92 | 14 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `spinach-soon` | Soon | 334 | 339 | 28 | 14 | +0.35 | warning-metadata | 11.2 | `#C96658` |
| `spinach-name` | Spinach | 70 | 327 | 76 | 17 | -0.20 | item-title | 15 | `#282E28` |
| `spinach-meta` | 2 pcs · Fridge | 70 | 343 | 110 | 14 | +0.00 | metadata | 11.5 | `#6B604F` |
| `spinach-exp` | Exp: 1 day | 70 | 358 | 83 | 14 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `pasta-name` | Pasta | 70 | 391 | 57 | 17 | +0.20 | item-title | 15 | `#282E28` |
| `pasta-meta` | 50 g · Pantry | 70 | 407 | 107 | 14 | +0.00 | metadata | 11.5 | `#6B604F` |
| `pasta-exp` | Exp: 6 months | 70 | 422 | 104 | 14 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `oil-name` | Olive Oil | 70 | 455 | 84 | 17 | -0.20 | item-title | 15 | `#282E28` |
| `oil-meta` | 1 L · Pantry | 70 | 471 | 99 | 14 | +0.00 | metadata | 11.5 | `#6B604F` |
| `oil-exp` | Exp: 1 year | 70 | 486 | 87 | 14 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `chicken-soon` | Soon | 334 | 533 | 28 | 14 | +0.25 | warning-metadata | 11.2 | `#C96658` |
| `chicken-name` | Chicken Breast | 70 | 519 | 129 | 17 | +0.30 | item-title | 15 | `#282E28` |
| `chicken-meta` | 400 g · Fridge | 70 | 535 | 110 | 14 | +0.00 | metadata | 11.5 | `#6B604F` |
| `chicken-exp` | Exp: 3 days | 70 | 550 | 92 | 14 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `tab-home` | Home | 26 | 807 | 34 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-inventory` | Inventory | 86 | 807 | 62 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-recipes` | Recipes | 251 | 807 | 52 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-more` | More | 332 | 807 | 34 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |

## suggestions — Recipe Suggestions

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Recipe Suggestions | 61 | 56 | 304 | 34 | +0.75 | page-title | 22 | `#282E28` |
| `tab-for-you` | For You | 34 | 132 | 73 | 24 | -0.55 | chip-label | 12 | `#282E28` |
| `tab-by-ingredient` | By Ingredient | 147 | 132 | 110 | 24 | +0.40 | chip-label | 12 | `#282E28` |
| `tab-by-season` | By Season | 283 | 132 | 76 | 24 | -0.25 | chip-label | 12 | `#282E28` |
| `based-on` | Based on your kitchen | 20 | 200 | 194 | 22 | -0.35 | body-strong | 15 | `#282E28` |
| `sort-label` | Sort: Best Match | 236 | 200 | 130 | 21 | +0.20 | metadata | 11.5 | `#6B604F` |
| `ready-now` | Ready Now | 87 | 255 | 102 | 23 | -0.15 | chip-label | 12 | `#315C43` |
| `pasta-title` | Tomato Pasta | 125 | 302 | 143 | 25 | -0.40 | item-title | 15 | `#282E28` |
| `pasta-meta` | 15 min · 3 servings | 126 | 335 | 167 | 22 | +0.10 | metadata | 11.5 | `#6B604F` |
| `chicken-status` | Almost Ready | 120 | 415 | 122 | 23 | -0.20 | chip-label | 12 | `#9E6C2A` |
| `chicken-title` | Chicken Stir-fry | 126 | 448 | 177 | 23 | +0.20 | item-title | 15 | `#282E28` |
| `chicken-meta` | 25 min · 2 servings | 126 | 477 | 173 | 22 | -0.15 | metadata | 11.5 | `#6B604F` |
| `chicken-missing` | Missing: Soy Sauce (optional) | 126 | 502 | 223 | 19 | +0.40 | warning-metadata | 11.2 | `#C96658` |
| `lentil-status` | Smart Swap | 120 | 580 | 104 | 23 | +0.25 | chip-label | 12 | `#477F95` |
| `lentil-title` | Lentil Soup | 126 | 613 | 132 | 23 | -0.30 | item-title | 15 | `#282E28` |
| `lentil-meta` | 40 min · 4 servings | 126 | 642 | 172 | 22 | +0.15 | metadata | 11.5 | `#6B604F` |
| `lentil-swap` | Swap: chicken → lentils | 126 | 671 | 210 | 19 | +0.35 | swap-metadata | 11.3 | `#B87937` |
| `view-all-label` | View All Suggestions | 83 | 752 | 220 | 29 | -0.20 | button-label | 16 | `#FBF4E5` |

## detail — Tomato Pasta detail

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `recipe-title` | Tomato Pasta | 15 | 235 | 254 | 39 | -0.80 | recipe-title | 27 | `#282E28` |
| `ready-chip` | Ready Now | 50 | 296 | 91 | 22 | -0.30 | chip-label | 12 | `#315C43` |
| `time-servings` | 15 min · 3 servings | 179 | 297 | 185 | 24 | +0.40 | metadata | 11.5 | `#6B604F` |
| `ingredients-heading` | Ingredients | 21 | 353 | 142 | 25 | -0.35 | section-title | 17 | `#282E28` |
| `pasta-name` | Pasta | 83 | 400 | 72 | 22 | -0.20 | item-title | 15 | `#282E28` |
| `pasta-amount` | 300 g | 280 | 399 | 53 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `tomatoes-name` | Tomatoes | 83 | 448 | 85 | 22 | +0.30 | item-title | 15 | `#282E28` |
| `tomatoes-amount` | 400 g | 280 | 447 | 53 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `oil-name` | Olive oil | 83 | 496 | 82 | 22 | -0.30 | item-title | 15 | `#282E28` |
| `oil-amount` | 30 ml | 280 | 495 | 53 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `garlic-name` | Garlic | 83 | 544 | 65 | 22 | +0.25 | item-title | 15 | `#282E28` |
| `garlic-amount` | 2 cloves | 272 | 543 | 68 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `basil-name` | Basil | 83 | 592 | 60 | 22 | -0.20 | item-title | 15 | `#282E28` |
| `basil-amount` | 10 g | 286 | 591 | 46 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `salt-name` | Salt | 83 | 639 | 51 | 22 | +0.30 | item-title | 15 | `#282E28` |
| `salt-amount` | 1 g | 300 | 638 | 32 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `pepper-name` | Pepper | 83 | 683 | 69 | 22 | -0.25 | item-title | 15 | `#282E28` |
| `pepper-amount` | 2 g | 297 | 682 | 35 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `start-cooking-label` | Start Cooking | 89 | 761 | 175 | 28 | -0.40 | button-label | 16 | `#FBF4E5` |

## cooking — Cooking step

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Cooking… | 120 | 55 | 154 | 35 | +0.65 | page-title | 22 | `#282E28` |
| `summary-recipe` | Tomato Pasta | 96 | 121 | 181 | 24 | -0.25 | item-title | 15 | `#282E28` |
| `summary-step` | Step 2 of 7 | 98 | 155 | 119 | 21 | +0.25 | metadata | 11.5 | `#6B604F` |
| `step-heading` | 2. Cook the pasta | 28 | 417 | 285 | 35 | -0.65 | recipe-title-small | 21 | `#282E28` |
| `instruction-1` | Bring a large pot of salted water to | 29 | 468 | 330 | 27 | -0.15 | body-copy | 14 | `#282E28` |
| `instruction-2` | a boil. Add pasta and cook for 8–10 | 29 | 500 | 334 | 27 | +0.15 | body-copy | 14 | `#282E28` |
| `instruction-3` | minutes (or according to package | 29 | 532 | 335 | 27 | -0.10 | body-copy | 14 | `#282E28` |
| `instruction-4` | instructions). | 29 | 564 | 188 | 25 | +0.15 | body-copy | 14 | `#282E28` |
| `timer` | 03:42 left | 283 | 617 | 81 | 21 | +0.00 | metadata | 11.5 | `#6B604F` |
| `scaled-label` | Scaled for 3 servings | 65 | 678 | 200 | 25 | -0.20 | metadata | 11.5 | `#6B604F` |
| `back-label` | Back | 72 | 761 | 65 | 27 | -0.45 | secondary-action | 14 | `#315C43` |
| `next-label` | Next | 251 | 761 | 65 | 27 | -0.55 | button-label | 16 | `#FBF4E5` |

## scaling — Portion Scaling

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Portion Scaling | 90 | 61 | 221 | 34 | -0.70 | page-title | 22 | `#282E28` |
| `recipe-name` | Tomato Pasta | 91 | 157 | 181 | 25 | -0.20 | item-title | 15 | `#282E28` |
| `adjust-servings` | Adjust servings | 23 | 241 | 187 | 24 | -0.45 | section-title | 17 | `#282E28` |
| `serving-1` | 1 | 52 | 301 | 20 | 29 | -0.45 | field-value | 15 | `#282E28` |
| `serving-2` | 2 | 142 | 301 | 20 | 29 | +0.45 | field-value | 15 | `#282E28` |
| `serving-3` | 3 | 230 | 300 | 20 | 29 | -0.20 | field-value | 15 | `#282E28` |
| `serving-4` | 4 | 320 | 301 | 20 | 29 | +0.35 | field-value | 15 | `#282E28` |
| `adjusted-quantities` | Adjusted Quantities | 23 | 382 | 223 | 25 | -0.35 | section-title | 17 | `#282E28` |
| `pasta-name` | Pasta | 88 | 444 | 72 | 22 | -0.15 | item-title | 15 | `#282E28` |
| `pasta-amount` | 300 g | 299 | 443 | 53 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `tomatoes-name` | Tomatoes | 88 | 503 | 85 | 22 | +0.25 | item-title | 15 | `#282E28` |
| `tomatoes-amount` | 400 g | 299 | 502 | 53 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `oil-name` | Olive oil | 88 | 562 | 82 | 22 | -0.30 | item-title | 15 | `#282E28` |
| `oil-amount` | 30 ml | 299 | 561 | 53 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `garlic-name` | Garlic | 88 | 621 | 65 | 22 | +0.25 | item-title | 15 | `#282E28` |
| `garlic-amount` | 2 cloves | 291 | 620 | 68 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `basil-name` | Basil | 88 | 680 | 60 | 22 | -0.20 | item-title | 15 | `#282E28` |
| `basil-amount` | 10 g | 305 | 679 | 46 | 22 | +0.00 | quantity | 14 | `#282E28` |
| `update-label` | Update Recipe | 87 | 755 | 218 | 31 | -0.45 | button-label | 16 | `#FBF4E5` |

## swaps — Ingredient Swaps

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Ingredient Swaps | 82 | 57 | 232 | 31 | +0.60 | page-title | 22 | `#282E28` |
| `intro` | Try these swaps | 20 | 125 | 165 | 22 | -0.30 | body-strong | 15 | `#282E28` |
| `lemon-name` | Lemon | 86 | 164 | 77 | 22 | -0.20 | item-title | 15 | `#282E28` |
| `lemon-sub` | can be swapped with: | 86 | 184 | 154 | 17 | +0.00 | metadata | 11.5 | `#6B604F` |
| `lime-name` | Lime | 86 | 237 | 64 | 22 | +0.30 | item-title | 15 | `#282E28` |
| `vinegar-name` | Vinegar | 86 | 308 | 88 | 22 | -0.20 | item-title | 15 | `#282E28` |
| `orange-name` | Orange | 86 | 379 | 84 | 22 | +0.25 | item-title | 15 | `#282E28` |
| `why` | Why? | 20 | 459 | 84 | 23 | -0.40 | section-title | 17 | `#282E28` |
| `why-1` | ✓ Similar acidity and flavor profile. | 20 | 491 | 321 | 19 | -0.10 | body-copy | 14 | `#282E28` |
| `why-2` | ✓ Works in the same type of recipes. | 20 | 517 | 332 | 20 | +0.15 | body-copy | 14 | `#282E28` |
| `use-lime-label` | Use Lime Instead | 89 | 759 | 214 | 28 | -0.45 | button-label | 16 | `#FBF4E5` |

## meals — Meal Suggestions

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Meal Suggestions | 59 | 57 | 275 | 34 | -0.45 | page-title | 22 | `#282E28` |
| `tab-ready` | Ready Now (2) | 12 | 142 | 113 | 22 | -0.40 | chip-label | 12 | `#282E28` |
| `tab-almost` | Almost Ready (1) | 145 | 142 | 108 | 22 | +0.35 | chip-label | 12 | `#282E28` |
| `tab-smart` | Smart Swap (1) | 276 | 142 | 90 | 22 | -0.25 | chip-label | 12 | `#282E28` |
| `pasta-status` | Ready Now | 18 | 227 | 110 | 25 | -0.20 | chip-label | 12 | `#315C43` |
| `pasta-title` | Tomato Pasta | 143 | 228 | 183 | 26 | -0.30 | item-title | 15 | `#282E28` |
| `pasta-meta` | 15 min · 3 servings | 142 | 266 | 207 | 22 | +0.10 | metadata | 11.5 | `#6B604F` |
| `pasta-availability` | All ingredients available | 142 | 310 | 215 | 22 | -0.15 | metadata | 11.5 | `#6B604F` |
| `chicken-status` | Ready Now | 18 | 396 | 110 | 25 | +0.20 | chip-label | 12 | `#315C43` |
| `chicken-title` | Chicken Stir-fry | 143 | 398 | 203 | 26 | +0.20 | item-title | 15 | `#282E28` |
| `chicken-meta` | 25 min · 2 servings | 142 | 435 | 207 | 22 | -0.15 | metadata | 11.5 | `#6B604F` |
| `curry-status` | Almost Ready | 17 | 557 | 121 | 25 | -0.25 | chip-label | 12 | `#9E6C2A` |
| `curry-title` | Vegetable Curry | 143 | 557 | 207 | 26 | -0.20 | item-title | 15 | `#282E28` |
| `curry-meta` | 35 min · 3 servings | 142 | 594 | 205 | 22 | +0.20 | metadata | 11.5 | `#6B604F` |
| `curry-missing` | Missing: coconut milk (optional) | 142 | 631 | 217 | 25 | +0.40 | warning-metadata | 11.2 | `#C96658` |
| `lentil-status` | Smart Swap | 18 | 727 | 120 | 25 | +0.10 | chip-label | 12 | `#477F95` |
| `lentil-title` | Lentil Soup | 143 | 728 | 190 | 26 | -0.20 | item-title | 15 | `#282E28` |
| `lentil-meta` | 40 min · 4 servings | 142 | 765 | 205 | 22 | +0.15 | metadata | 11.5 | `#6B604F` |
| `lentil-swap` | Swap: chicken → lentils | 142 | 790 | 210 | 22 | +0.30 | swap-metadata | 11.3 | `#B87937` |

## lentil — Lentil Soup / Steps

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Lentil Soup | 64 | 58 | 203 | 33 | +0.65 | page-title | 22 | `#282E28` |
| `smart-swap` | Smart Swap | 40 | 196 | 80 | 20 | -0.20 | chip-label | 12 | `#477F95` |
| `time-meta` | 40 min · 4 servings | 126 | 195 | 171 | 22 | +0.20 | metadata | 11.5 | `#6B604F` |
| `ingredients-tab` | Ingredients | 62 | 255 | 94 | 20 | -0.20 | chip-label | 12 | `#282E28` |
| `steps-tab` | Steps | 257 | 255 | 55 | 20 | +0.25 | chip-label | 12 | `#282E28` |
| `step1-number` | 1 | 21 | 299 | 12 | 20 | +0.00 | step-number | 12 | `#FBF4E5` |
| `step1-title` | Prep vegetables | 48 | 297 | 150 | 18 | -0.20 | item-title-small | 13 | `#282E28` |
| `step1-copy` | Chop onion, carrot, celery. | 48 | 318 | 246 | 16 | +0.10 | metadata | 11.5 | `#6B604F` |
| `step2-number` | 2 | 21 | 357 | 12 | 20 | +0.00 | step-number | 12 | `#FBF4E5` |
| `step2-title` | Sauté | 48 | 356 | 91 | 18 | +0.20 | item-title-small | 13 | `#282E28` |
| `step2-copy` | Cook in olive oil for 5 minutes. | 48 | 377 | 278 | 16 | -0.10 | metadata | 11.5 | `#6B604F` |
| `step3-number` | 3 | 21 | 416 | 12 | 20 | +0.00 | step-number | 12 | `#FBF4E5` |
| `step3-title` | Add lentils & broth | 48 | 415 | 187 | 18 | -0.20 | item-title-small | 13 | `#282E28` |
| `step3-copy` | Simmer for 25 minutes. | 48 | 436 | 224 | 16 | +0.15 | metadata | 11.5 | `#6B604F` |
| `step4-number` | 4 | 21 | 475 | 12 | 20 | +0.00 | step-number | 12 | `#FBF4E5` |
| `step4-title` | Season | 48 | 474 | 90 | 18 | +0.20 | item-title-small | 13 | `#282E28` |
| `step4-copy` | Add salt, pepper, herbs. | 48 | 495 | 224 | 16 | -0.10 | metadata | 11.5 | `#6B604F` |
| `start-cooking` | Start Cooking | 102 | 809 | 157 | 25 | -0.40 | button-label | 16 | `#FBF4E5` |

## expiry — Expiration Priority

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Expiration Priority | 56 | 57 | 280 | 34 | -0.40 | page-title | 22 | `#282E28` |
| `alert-line1` | 3 items need to be used within | 48 | 117 | 279 | 20 | -0.30 | alert-label | 12.5 | `#C96658` |
| `alert-line2` | 24–48 hours | 116 | 140 | 146 | 20 | +0.30 | alert-label | 12.5 | `#C96658` |
| `spinach-title` | Spinach | 76 | 195 | 94 | 21 | +0.25 | item-title | 15 | `#282E28` |
| `spinach-exp` | Expires in 1 day | 76 | 220 | 144 | 19 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `beef-title` | Ground Beef | 76 | 271 | 139 | 21 | -0.25 | item-title | 15 | `#282E28` |
| `beef-exp` | Expires in 1 day | 76 | 296 | 144 | 19 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `mozz-title` | Mozzarella Cheese | 76 | 347 | 170 | 21 | +0.30 | item-title | 15 | `#282E28` |
| `mozz-exp` | Expires in 2 days | 76 | 372 | 145 | 19 | +0.00 | warning-metadata | 11.2 | `#C96658` |
| `tips-title` | Tips | 64 | 438 | 70 | 22 | -0.20 | section-title | 17 | `#282E28` |
| `tips-line1` | Use these ingredients first | 30 | 472 | 270 | 19 | -0.20 | body-copy | 14 | `#282E28` |
| `tips-line2` | to reduce food waste! | 30 | 496 | 242 | 19 | +0.10 | body-copy | 14 | `#282E28` |

## settings — Settings

| ID | Exact visible text | x | y | w | h | θ° | Role | Size pt | Color |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| `status-time` | 9:41 | 27 | 17 | 38 | 16 | +0.00 | status | 10.5 | `#282E28` |
| `page-title` | Settings | 55 | 58 | 120 | 32 | +0.45 | page-title | 22 | `#282E28` |
| `storage-title` | Storage Zones | 62 | 121 | 171 | 21 | -0.25 | item-title | 15 | `#282E28` |
| `storage-sub` | Pantry, Fridge, Freezer | 62 | 148 | 205 | 18 | +0.10 | metadata | 11.5 | `#6B604F` |
| `units-title` | Units | 62 | 204 | 95 | 21 | +0.20 | item-title | 15 | `#282E28` |
| `units-sub` | Grams, milliliters, pieces | 62 | 231 | 212 | 18 | -0.10 | metadata | 11.5 | `#6B604F` |
| `offline-title` | Offline Mode | 62 | 286 | 142 | 21 | -0.15 | item-title | 15 | `#282E28` |
| `offline-sub` | Works without internet | 62 | 312 | 192 | 18 | +0.15 | metadata | 11.5 | `#6B604F` |
| `about-title` | About | 62 | 369 | 95 | 21 | +0.10 | item-title | 15 | `#282E28` |
| `about-sub` | Version 1.0.0 | 62 | 396 | 140 | 18 | -0.15 | metadata | 11.5 | `#6B604F` |
| `tab-home` | Home | 26 | 807 | 34 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-inventory` | Inventory | 86 | 807 | 62 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-recipes` | Recipes | 251 | 807 | 52 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
| `tab-more` | More | 332 | 807 | 34 | 17 | +0.00 | nav-label | 10.5 | `#6B604F` |
