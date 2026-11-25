# FoodSafe asset research — verified candidates

Research date: 25 October 2026

This file records real external resources located and checked through their public project pages. Finding a resource is not the same as downloading, auditing every file, or integrating it. The runtime container failed DNS resolution for direct downloads during this pass, so none of the following is claimed to be vendored. See `ASSET-LICENSES.md` and `asset-sources.json` for the same status in machine-readable form.

## Best-fit shortlist

### 1. Drawably — hand-sketched controls (highest priority for controls)

- Source: https://github.com/danielwh2/drawably
- License: MIT, per the upstream README.
- Provides: SVG-sketch rendering for buttons, checkboxes, radios, toggles, inputs, textareas, selects, dividers, cards, badges and lists; deterministic seeds; a static mode (`boil: 0`); and an optional roughly 31 KB “Drawably Pen” typeface.
- Why it can help: it draws the UI chrome itself, rather than merely adding food illustrations. This directly maps to FoodSafe’s buttons, cards, form fields, toggles, chips and badge outlines.
- Integration decision: test static seeded rendering first; keep actual HTML controls in the DOM for hit targets, keyboard interaction and accessibility. Preserve FoodSafe’s colors and radii rather than taking defaults unchanged.
- Fit warning: animated “boiling” edges may feel more wiggly than the supplied still mockup, so motion should remain disabled in the fidelity reference. The optional font is a candidate only, not a proven match.

### 2. Doodle Icons — hand-drawn interface SVGs (highest priority for icon coverage)

- Source: https://github.com/oreo-design/doodle-icons
- License: MIT, per the upstream README.
- Provides: 152 hand-drawn SVG icons, in static `icons/` and animated `icons-animated/` directories. Icons cover interface symbols, arrows, objects and other common UI concepts. SVG strokes use `currentColor`; for recoloring, the README advises inlining the SVG rather than loading it as an image.
- Why it can help: a coherent hand-drawn family is better than mixing generic icons, emoji and unrelated line-art. The repository also documents an agent skill for use in coding-agent workflows.
- Integration decision: map only suitable symbols—home, heart, back, search, plus, calendar, clock, warning, settings, storage and navigation. Use static SVGs for screenshot fidelity; recolor and adjust stroke only after comparison with the reference; include the MIT notice.
- Font note: the upstream README explicitly recommends pairing these icons with Schoolbell. This makes Schoolbell worth comparing for all UI text, but not an automatic replacement for the current font.

### 3. Culinary Assets — supplementary food/ingredient coverage (conditional)

- Source: https://github.com/cosmintrica/culinary-assets
- Catalog: https://cosmintrica.github.io/culinary-assets/
- License: upstream states artwork and metadata are CC0 1.0; software/examples are MIT.
- Provides: 200 transparent culinary illustrations, as PNG and WebP, across ingredients, produce, pantry staples, cookware, utensils and appliances. The upstream description identifies the style as coral-and-mint, says artwork is AI-generated and visually reviewed, and notes the assets are raster illustrations rather than vector SVGs.
- Why it can help: it fills ingredient gaps consistently and supports transparent image wells.
- Integration decision: do not replace the bespoke FoodSafe dish art wholesale. Inspect individual items against the supplied mockup and use only those that pass a style audit. Do not mix a conflicting art direction into the same screen. Reject assets that look too clean, plasticky, 3D, or unlike colored-pencil/soft-wash drawing even if the license is permissive.

### 4. Food Icon Pack Classic — backup coverage (secondary)

- Source: https://www.foodiconpack.com/free-food-icons
- License: the source’s license page identifies the free Common ingredient, utensil, dish and beverage packs as CC BY 4.0; attribution and change notices are required.
- Provides: 743 icons in the free Classic group across ingredients, utensils, dishes and beverages.
- Why it can help: it covers many food concepts the current bespoke SVG library may not include.
- Fit warning: the free Classic set is described as outline icons. It could look too clean or monochrome for the colored-pencil reference. Use only after visual review and include attribution/change notices in third-party notices if selected.

## Font candidates to compare against the mockup

The original is a flattened collage, not editable text; no exact original font binary can be proven from the JPEG alone.

### Current local baseline: Purisa Regular/Bold

- Files: `assets/fonts/Purisa-Regular.otf`, `assets/fonts/Purisa-Bold.otf`.
- Status: local/offline and already packaged. The prototype currently routes app-authored text through `FoodSafe Hand`.
- Decision: keep as the fallback baseline until real, side-by-side local specimens are rendered. Do not claim Purisa is the source font.

### Schoolbell — highest-priority external comparison

- Official family: https://fonts.google.com/specimen/Schoolbell
- Rationale: Doodle Icons’ own README pairs its hand-drawn icon system with Schoolbell. Compare it across all roles, especially tiny metadata, tab captions, input values, quantities and button labels—not just headings.
- License: Doodle Icons’ README says Schoolbell is free under the SIL Open Font License. Bundle the font and its actual upstream license file if selected.
- Status: researched only; not bundled or visually verified here.

### Patrick Hand — readability benchmark

- Official family: https://fonts.google.com/specimen/Patrick+Hand
- Source metadata: https://github.com/google/fonts/blob/main/ofl/patrickhand/METADATA.pb
- License: SIL Open Font License 1.1, according to the upstream OFL file.
- Rationale: based on the designer’s handwriting; useful for comparing tiny list labels and quantities.
- Fit warning: may look more regular/clean than FoodSafe’s informal, individually uneven hand-printing.

### Kalam — slanted-pen benchmark

- Official family: https://fonts.google.com/specimen/Kalam
- Source description: https://github.com/google/fonts/blob/main/ofl/kalam/DESCRIPTION.en_us.html
- Rationale: handwriting optimized for on-screen text, with Light, Regular and Bold weights.
- Fit warning: the upstream description calls out its steep slant; that may be too slanted for the relatively upright text in FoodSafe. Treat as a comparison sample, not an assumed winner.

## Recommended decisions

1. Keep bespoke/source-derived FoodSafe SVGs as the visual source of truth for hero dishes, tomatoes, eggs, spinach, oil, pantry items and welcome artwork.
2. Evaluate Drawably for buttons, fields, toggles, checkboxes, chips, badges and cards; its value is a system-wide irregular outline, not another icon set.
3. Evaluate Doodle Icons for interface symbols and replace existing shapes only when a close semantic and stylistic match exists.
4. Use Culinary Assets only as an illustrated-content gap filler after visual inspection; do not import all 200 assets blindly.
5. Compare Schoolbell, Patrick Hand, Kalam and Purisa in a single specimen at 10–24 px with the exact same reference words. Choose one family globally, across headings, body, values, metadata, chips, tabs, placeholders and buttons.
6. No photography, photorealistic food, realistic 3D, remote runtime assets, emoji substitutions, or mixed illustration styles.

## Integration checklist for an AI coding agent

- [ ] Download/clone only from the upstream links; record exact release/commit and license file.
- [ ] Add the exact version, copyright holder, license, assets used and changes to `ASSET-LICENSES.md`.
- [ ] Build a 1:1 comparison sheet for each candidate before adopting it.
- [ ] Reject any asset that looks photographic, photorealistic, too polished or from a conflicting visual family.
- [ ] Keep assets local/offline at runtime; no CDN dependencies.
- [ ] Keep control tap targets and accessibility semantics independent of sketched decorative outlines.
- [ ] Render all 13 screens after each adoption; validate asset paths and visually inspect every screen.
- [ ] Audit every visible text node for one font family and test it at actual phone size. A header-only handwriting match is a failure.

## Research honesty

The sources above were found and their public descriptions and license statements were inspected through web search. Direct network downloads failed DNS resolution in the runtime container during this pass. These are **verified leads, not downloaded or integrated assets**. Existing local FoodSafe artwork remains the actual bundled art until a new source is present locally and passes license and visual QA.


## Current demo application status (2026-10-25)

The demo now contains **local offline visual auditions** for the leading concepts: a deterministic sketch-outline SVG overlay for buttons/fields/cards/chips (Drawably-style), and a static displacement filter for hand-authored local interface SVGs (Doodle-style). The local UI has independent switches so the visual difference can be checked. These are not the official upstream packages and no package code or icons have been copied into the project. The Culinary Assets set has not been imported; the current illustrated FoodSafe SVG set remains active because visual consistency matters more than raw catalog size. The current run has a 13-screen browser contact sheet and automated QA report in `visual-qa/asset-integration-v1/`.


## Visual inspection update — 2026-10-25

The original target was reopened and compared against actual online preview images, not just asset descriptions. The strongest food candidates are split by role: **The Rogue Cookie** has the closest thin-ink/soft-watercolor ingredient style but sells ingredient art only; **AnorelArts Watercolor Cooking Set** is the more complete dish family, with 35 dishes plus 48 ingredients and 12 utensils in the complete set. AnorelArts is more saturated/heavy-lined than the mockup, so it is a candidate to audition, not a guaranteed match. The combination is more faithful than substituting the current flat geometrical SVGs for everything. See `ASSET-DECISION.md` and `visual-qa/external-asset-audition.html` for source previews next to the original mockup.

Drawably is confirmed in its upstream README to support deterministic seed, a roughness control and `boil: 0` for static outlines; use that mode for faithful screenshots. Doodle Icons has separate static `icons/` and animated `icons-animated/` folders; use static assets only. PictArts was inspected as a real illustration sample and rejected for core dish art because its white sticker rim/heavy black outlines differ from the source; its terms also require caution for an app whose main content is food art.

No external binaries were downloaded or claimed to be bundled: the runtime container cannot resolve external hosts for binary downloads. The audition HTML uses live source previews only for review, separate from app runtime. The app remains offline; external assets must be downloaded and licensed before production integration.
