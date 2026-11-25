# FoodSafe asset-integration demo — QA report

**Run date:** 2026-10-25  
**Build:** local prototype with the illustration and sketch-style integration pass  
**Capture method:** Playwright + Chromium `page.set_content()` with project assets inlined into a self-contained HTML document. No external network or runtime CDN request is required.

## Automated checks

| Check | Result |
|---|---:|
| Screens captured | 13 / 13 |
| Broken image loads | 0 |
| Browser page errors | 0 |
| Visible text font-family stacks outside `FoodSafe Hand` | 0 |
| Purisa Regular loaded | PASS |
| Purisa Bold loaded | PASS |
| Drawably-style control overlay | 16 present → 0 when disabled → 16 after re-enable |
| Doodle-style SVG ink filter | Filter active → `none` when disabled → active after re-enable |
| Navigation smoke test | Clicking Inventory landed on `inventory` |
| Runtime photo/JPEG assets | 0 JPG/JPEG/WebP files in the bundled assets directory |
| Active PNG assets | 2: the source-derived FoodSafe wordmark and illustrated grocery-bag crop |
| Local SVG illustration assets | 43 |

Full machine-readable results: `test-report.json`.

## Files to inspect

- `self-contained-demo.html` — self-contained, offline HTML copy with the test switches in the right-side inspector.
- `contact-sheet.jpg` — all 13 screen renders.
- `home-style-ab-comparison.jpg` — Home screen with sketch outlines and icon-ink filter toggled in all four combinations.
- `svg-asset-audit.jpg` — inventory of the 43 local SVG food/category/recipe/swap drawings.
- `<screen>.png` and `<screen>-device.png` — per-screen desktop workspace and device captures.

## What is actually integrated

1. **Illustration-only FoodSafe art:** the app screens use local, hand-authored SVG illustrations for food, ingredients, categories, recipe cards, swaps, and expiry-priority rows. The only active raster artwork is cropped from the user's original illustrated mockup (the FoodSafe wordmark and welcome grocery-bag illustration). There are no photos in the active screens.
2. **Drawably-style controls:** an offline deterministic SVG path overlay has been written into the demo for semantic controls—buttons, fields, cards, chips, category tiles, segmented controls, toggles, and related elements. The user can toggle it in the inspector and compare the result. This is a **local visual adapter inspired by the documented static/seeded behavior**, not the upstream Drawably package.
3. **Doodle-style icons:** locally authored SVG interface symbols are given a light static SVG displacement/ink treatment. The user can toggle it independently. This is a **local style audition**, not the upstream Doodle Icons icon set.
4. **Global handwritten typography:** the CSS routes all visible app text to `FoodSafe Hand` backed by locally bundled Purisa Regular/Bold. The automated computed-style audit found a single font-family stack across text-bearing elements on all 13 screens. This is a candidate match, not proof of the original typeface.

## Residual differences / not yet claimed

- The upstream Drawably, Doodle Icons, Culinary Assets and external font packages were not downloaded into the package because direct downloads were unavailable from this runtime. Their public repos and license statements remain listed in `ASSET-RESEARCH.md`; they are not represented as installed.
- Food illustrations are bespoke, consistent local vectors, but still simpler than the original colored-pencil mockup in some areas. Some different recipes use related shared visual motifs; these can be individually refined.
- The page is an HTML verification prototype. No native SwiftUI app/Simulator capture has been produced by this pass.
- A contact sheet is useful for density and missing-asset checks but does not prove pixel equality. The source is a perspective-skewed single collage, not editable source frames. Remaining work should compare rectified source crops with individual screen captures and adjust geometry, type size/shape, photo-free illustration framing, line weight, tilt and spacing.

## Reproduction

Run `/tmp/render_foodsafe.py` in the current runtime to regenerate the self-contained HTML, individual captures, contact sheet, A/B comparison, and `test-report.json`. The script uses local assets and does not need the external asset packages or a network connection.
