# FoodSafe — full design and prototype project

**Start with `START-HERE.html`.** It links to the offline UI demo, local prototype, 13-screen board, original comparison, design specification, coordinate atlas and QA dashboard.

## Main files

- `design.md` — 1000+ line visual/implementation contract.
- `FoodSafe-Preview.html` — single-file offline demo; fonts and SVG illustration assets are embedded.
- `prototype/index.html` + `assets/` — editable HTML/CSS/JS prototype and local assets.
- `FoodSafe-UI-Mockup-13-Screen-Board.jpg` — current 13-screen board.
- `FoodSafe-UI-Mockup-Source-Comparison.jpg` — current preview against the original mockup.
- `reference/SCREEN-COORDINATE-MASTER.json` — coordinate, perspective and text-run data.
- `reference/SCREEN-MEASUREMENT-ATLAS.md` and `reference/SCREEN-TEXT-COORDINATE-ATLAS.md` — human-readable measurements.
- `visual-qa/` — screenshot outputs, coordinate overlays, comparisons and reports.
- `ASSET-RESEARCH.md`, `ASSET-DECISION.md`, `ASSET-LICENSES.md` — external asset options and license caveats.

## Open locally

Extract the archive and open `START-HERE.html`. For a zero-dependency, single-file preview, open `FoodSafe-Preview.html`. If your browser restricts local files, see `INSTALL-LOCAL.md` for the built-in Python HTTP server command.

## What this is / isn't

This archive is a design specification and browser prototype. It is **not** a signed iOS app, `.ipa`, or complete Xcode project. No npm packages or internet connection are required for the self-contained preview. The external asset candidates in research documents are not represented as installed binaries unless present under `assets/`.

## Portable package note

This ZIP retains all editable source, required local assets, all 13 rectified references, coordinate/text master data, the complete coordinate dashboard and all per-screen captures the dashboard links to. Redundant historical showcase HTML and repeat captures are omitted to reduce download size; the full archive contains the complete QA history.
