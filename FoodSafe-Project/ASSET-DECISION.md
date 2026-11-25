# FoodSafe external asset decision — visual fit audit

**Decision date:** 2026-10-25  
**Source of truth:** the user-provided FoodSafe contact-sheet mockup at `reference/original-mockup.jpg`.

## Decision in one paragraph

The closest defensible online asset plan is **role-based**, not “grab a random free food icon pack”: use **AnorelArts Watercolor Cooking Set** for whole illustrated dishes (35 dishes, 500×500 transparent PNGs) and, if the cost is acceptable, **The Rogue Cookie’s hand-drawn watercolor ingredient pack** for ingredient portraits (80+ illustrations, 2000×2000 transparent PNGs). Both are painted/watercolor rather than photography. Use **Drawably** for intentionally irregular borders on HTML controls, with `boil: 0` and fixed seeds so the reference remains still, and the static SVGs from **Doodle Icons** only for interface symbols. The art sets are different creators, so this pairing is a *candidate to visually audition*, not an asserted perfect match; both use watercolor/painterly food, but their outlines and saturation differ. If you require a single purchased food-art family, use the full AnorelArts set alone for more consistency and less cost.

## What I actually compared to the source

The reference has four different visual roles:

1. **Dish illustrations in image mounts:** pasta, stir-fry, soup and curry are detailed, colorful, lightly textured, mostly viewed from above/three-quarter angle. User explicitly rejected real photographs; these slots must use drawn dishes.
2. **Ingredient thumbnails:** small object drawings (tomatoes, eggs, spinach, pasta, oil, chicken, lemon/lime, basil, salt/pepper). The desired treatment is soft color wash plus thin imperfect ink, not geometric flat icons and not emoji.
3. **UI icons:** small, mostly line-based interface symbols. These can be monochrome/green, but should share a slightly imperfect line.
4. **Controls:** buttons, pills, fields, cards and toggles have uneven, pen-drawn contours with warm fills. This is a control-rendering job rather than a food illustration pack.

## Selected sources by role

### A. Dish/meal art — AnorelArts Watercolor Cooking Set

- Main page: https://anorelarts.itch.io/watercolor-cooking-set
- Dish-only pack: https://anorelarts.itch.io/watercolor-cooking-set-food-pack-1
- Verified page facts: the complete set states 28 backgrounds, 48 ingredients, 12 utensils and 35 dishes; ingredient/dish/utensil assets are 500×500 px. The dish-only pack is £4 minimum and has 35 transparent 500×500 watercolor-style dish images; the complete set is £12.50 minimum.
- Use terms stated by creator: personal and commercial use allowed; credit is appreciated but not required. Assets are AI-assisted and edited by the creator. Do not redistribute or sell the raw asset pack standalone.
- Why selected: it is the most practical single source found for *many prepared dishes* in one painterly style, with sufficient dimensions for small recipe cards and moderate-size hero art. Its palette and outlines are more saturated/heavy than the reference; use only food cutouts, ignore the medieval/fantasy background and prop aesthetic, and audit each candidate dish before adoption.
- Best intended uses: `Tomato Pasta` hero/thumb, `Lentil Soup`, `Chicken Stir-fry`, `Vegetable Curry`, cooking-screen food visual. The actual pack's asset list must be checked before exact mapping; names are suggestions, not confirmed available filenames.
- Do not claim these files are already installed. They are a shortlisted external pack until the user downloads them.

### B. Ingredient art — The Rogue Cookie hand-drawn watercolor food pack

- Source page: https://theroguecookie.com/the-hand-drawn-low-fodmap-food-illustrations-set-for-creators/
- Verified page facts: 80+ individual transparent PNGs, 2000×2000 px, described by the creator as personally hand-drawn and digitally rendered in a soft watercolor-inspired style. Listed subjects include tomato, cherry tomato, egg, chicken, pasta, lemon, lime, basil, olive oil, and many vegetables/herbs.
- License/price caution: the article shows a commercial license at $34.99, while a linked product listing can show a wider price range by variant. Confirm the exact commercial/app license and final checkout amount before buying. This is the closest style specimen found for tiny ingredient art but is not a finished-dish pack.
- Why it fits the mockup: the preview has organic botanical shapes, thin uneven ink, low-to-mid saturation watercolor, and subtle pigment texture. It resembles the source's small produce illustrations much more closely than the current flat geometric SVG set.
- Use only with a valid app/commercial license and locally bundled files. Do not use the preview contact sheet itself as an app asset; it includes a sample-layout background and labels.

### C. Hand-drawn button/field/card contours — Drawably

- Source: https://github.com/danielwh2/drawably
- License: MIT.
- Verified behavior/options: it provides hand-drawn buttons, input, textarea, select, checkbox, radio, toggle, card, badge, divider and list treatments. The README specifies a fixed `seed` for reproducible sketching, `roughness` for wobble, and `boil: 0` for a single static path. It exposes CSS custom properties for stroke/fill/paper.
- Integration decision: use its static seeded form as a **contour layer**, but keep actual inputs, buttons and accessibility behavior. Override colors to FoodSafe's forest green, dark warm ink, sage and cream. Do not use the default Inter/system font; every visible label remains in the single global handwritten FoodSafe font.
- Fit note: do not animate/boil the edges in the fidelity demo. The supplied mockup shows a still hand-drawn UI. Default Drawably roughness may be too strongly wobbly; tune down until the screenshot's subtle doubled pencil outline is matched.

### D. Interface icon family — Doodle Icons

- Source: https://github.com/oreo-design/doodle-icons
- License: MIT.
- Verified facts: 152 hand-drawn SVG interface/object icons; the repo separates still `icons/` SVGs from `icons-animated/`. Stroke color follows `currentColor` when inlined.
- Integration decision: use the **still** SVGs, not animated/boiling icons. Suitable candidates include heart, back/arrows, search, plus, home and generic settings/alert symbols. Use custom/source-matched drawings for fridge/freezer/pantry and food-category objects if Doodle Icons lacks the specific silhouette.
- Fit note: icons are monochrome outline art, not the colored food art. They are for UI symbols only. At 18–24 CSS px, adjust effective line weight to match the thin source icons.

## Rejected or secondary resources

### PictArts free hand-drawn food PNGs — reject for core dish images

- Example: https://food-illustration.com/material/002-bitten-gourmet-food/fork-twirling-bolognese-spaghetti-l.png
- Official terms: https://food-illustration.com/info/j-termsofuse.html
- Page advertises free, no-registration, commercial use and transparent PNG. Its visible pasta sample is hand-drawn, but has a much heavier black contour and prominent white sticker halo than the reference. The terms permit use as a design component but prohibit raw redistribution/sale and “asset collection” inclusion in apps; because FoodSafe’s food imagery is central to its product, avoid relying on these terms for production food objects without explicit clarification from the rights holder.

### World Food Tour — Cozy Cooking Collection — low-cost backup, not first choice

- Source: https://juichieh.itch.io/world-food-tour-cozy-cooking-collection
- The listing states $1.99 minimum for 160 transparent PNGs, 256×256 px, hand-painted warm colors, a consistent three-quarter view, covering finished dishes, ingredients, drinks and kitchen props. It is AI-assisted.
- Why not primary: 256 px is marginal for a hero image on a 3× phone screen, and the preview reads as higher-contrast game art than the reference's soft hand-drawn food. It is a good cheap prototype fallback, not the closest visual match.

### Culinary Assets (CC0) — reject as primary style

- Source: https://github.com/cosmintrica/culinary-assets
- The README lists 200 transparent raster illustrations under CC0 artwork terms in a coral-and-mint direction. This is useful breadth, but its polished/geometric look is less close to FoodSafe's colored-pencil, thin-ink, warm watercolor treatment. Do not replace bespoke art wholesale.

### Food Icon Pack Classic — reject for primary illustrations

- Source: https://www.foodiconpack.com/free-food-icons
- Free Classic food packs are CC BY 4.0 with attribution/change notices. The free set is mostly outline icons; it does not provide the shaded, painterly dish artwork required for FoodSafe's meal images. Keep only as a gap filler if a specific outline asset is a close fit.

## Visual-fit verdict (subjective, explicitly not pixel metrics)

| Source | Food-style fit | Coverage | Resolution | Verdict |
|---|---:|---:|---:|---|
| The Rogue Cookie | 5/5 for ingredients | 3/5 | 2000×2000 | Closest ingredient-stroke style; purchase/app terms need checking |
| AnorelArts Watercolor Cooking Set | 4/5 for dishes | 5/5 | 500×500 | Primary dish source; trim/mask/scale by visual inspection |
| Drawably | 5/5 for control outlines | N/A | Vector/SVG overlay | Use static seeded component contours |
| Doodle Icons | 4/5 for interface symbols | 4/5 | SVG | Use still SVGs only |
| PictArts | 2/5 | 2/5 for current subjects | Transparent PNG | Reject for primary food art: too heavy outline/white halo |
| World Food Tour | 3/5 | 4/5 | 256×256 | Inexpensive backup, too game-like/low-res for heroes |
| Culinary Assets | 2/5 | 5/5 | 512×512 PNG/WebP | Broad coverage, style too geometric/polished |

These are design-review judgments based on the published previews, not computed visual-similarity metrics. The real asset files must be downloaded and auditioned at FoodSafe's actual sizes before final approval.

## Runtime rule and next action

- The shipping app remains offline: download licensed assets, store them in the project, record a license and SHA-256/hash/source manifest, then remove remote URLs from any production view.
- The separate `visual-qa/external-asset-audition.html` board intentionally links to upstream previews for inspection; it is a research page, not the app runtime, and requires internet to load the source previews.
- The current container can browse these websites through web research but cannot resolve external hosts for binary download. Accordingly, external files are **not** represented as already vendored. Current local SVG illustrations stay in the app until downloaded external files pass the audition.
