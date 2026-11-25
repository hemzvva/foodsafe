# Asset licenses and provenance

## Local FoodSafe artwork included in this prototype

- `assets/*.svg` FoodSafe ingredient, category, dish, storage, and swap drawings: custom local vector illustrations authored for this demo. No third-party illustration pack source was copied into these files. They are part of this project package.
- `assets/foodsafe-wordmark.png` and `assets/welcome-grocery-art.png`: cropped from the user's supplied FoodSafe concept mockup for fidelity. Keep them only as source-derived reference artwork; do not claim the crop operation created the original art.
- `assets/fonts/Purisa-Regular.otf` and `assets/fonts/Purisa-Bold.otf`: local font files already present in the project; preserve their upstream license/notice if distributing the project. The demo's CSS family is `FoodSafe Hand`, pointing to these fonts. Purisa is a practical local baseline, not a verified identification of the font in the screenshot.

## Locally implemented visual audition adapters

- `Drawably-style static control sketch`: a locally written, deterministic SVG overlay that draws imperfect double outlines around semantic HTML controls. It was created from observed documented behavior as a style audition. **It is not Drawably's package source and does not include Drawably code.**
- `Doodle-style ink on SVG icons`: a tiny local SVG turbulence/displacement filter applied to hand-authored local SVG icons. **It is not the Doodle Icons package or any of its shipped icons.**

These adapters need no third-party package attribution because no upstream source code or art was imported into them. They are clearly marked as local prototypes in the UI and docs.

## Researched but not bundled upstream resources

- Drawably — MIT — https://github.com/danielwh2/drawably
- Doodle Icons — MIT — https://github.com/oreo-design/doodle-icons
- Culinary Assets artwork/metadata — CC0 1.0; software/examples are described as MIT — https://github.com/cosmintrica/culinary-assets
- Food Icon Pack free Classic assets — CC BY 4.0; attribution and change notice required — https://www.foodiconpack.com/free-food-icons
- Schoolbell — https://fonts.google.com/specimen/Schoolbell (bundle exact upstream license if imported)
- Patrick Hand — SIL OFL 1.1 — https://fonts.google.com/specimen/Patrick+Hand
- Kalam — https://fonts.google.com/specimen/Kalam (bundle exact upstream license if imported)

Network downloads from the external package/font hosts failed in this runtime, so these are researched leads and **are not shipped**. Do not infer that a candidate license applies to current local FoodSafe art. Before importing any external asset, record the exact release/commit, license file, copyright holder, attribution requirements, selected assets, and modifications.


## Newly audited external candidates (not yet installed)

- **AnorelArts Watercolor Cooking Set** — source: https://anorelarts.itch.io/watercolor-cooking-set . Listing says £12.50 minimum for the complete pack (28 backgrounds, 48 ingredients, 12 utensils, 35 dishes); dish-only pack: https://anorelarts.itch.io/watercolor-cooking-set-food-pack-1 at £4 minimum. Creator says personal/commercial use allowed, credit not required, raw asset pack may not be claimed as your own. Art is AI-assisted and edited. Review current terms at download time. Status: not downloaded.
- **The Rogue Cookie Low FODMAP Clipart** — source: https://theroguecookie.com/the-hand-drawn-low-fodmap-food-illustrations-set-for-creators/ . 80+ transparent PNGs, 2000×2000, described as personally hand-drawn, watercolor-inspired. The article lists a $34.99 commercial option; product variants may display a range. Confirm exact license scope for an iOS application and current checkout price. Status: not downloaded.
- **Drawably** — https://github.com/danielwh2/drawably, MIT. Use static generated outlines with reproducible seeds and `boil: 0`; preserve the MIT notice when upstream code is actually vendored. Current local adapter is not Drawably source code. Status: upstream researched, not vendored.
- **Doodle Icons** — https://github.com/oreo-design/doodle-icons, MIT. Use static SVGs from `icons/` only; `icons-animated/` is a distinct animated set. Preserve MIT notice if vendored. Status: upstream researched, not vendored.
- **PictArts spaghetti sample** — https://food-illustration.com/material/002-bitten-gourmet-food/fork-twirling-bolognese-spaghetti-l.png . Site terms https://food-illustration.com/info/j-termsofuse.html say free personal/commercial use but prohibit raw redistribution/sale and describe application use as design components; due to ambiguity for a food-centered app and visible white outline mismatch, not selected.
- **World Food Tour Cozy Cooking Collection** — https://juichieh.itch.io/world-food-tour-cozy-cooking-collection . Listing says 160 256×256 transparent PNGs, $1.99 minimum, commercial/personal use as stated by creator. Only a low-cost fallback due to size and art-direction mismatch. Status: not downloaded.
