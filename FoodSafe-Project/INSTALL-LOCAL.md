# Open FoodSafe locally

This download is a **design/prototype project**, not an installable iOS `.ipa`, signed app, or complete Xcode project.

## Easiest: open one HTML file

1. Download and extract `FoodSafe-Project.zip`.
2. Open `FoodSafe-Preview.html` in a modern browser. It is a self-contained demo with its fonts and illustration assets embedded, so it does not need internet access or a package install.
3. For the source files and editable local assets, open `prototype/index.html` or read `design.md`.

## Start page

Open `START-HERE.html` to access the preview, full prototype, 13-screen mockup board, source comparison, coordinate dashboard, and design specification.

## If your browser blocks local HTML files

Open Terminal in the extracted `FoodSafe-Project` folder and run:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080/START-HERE.html` in your browser. Stop the server with `Control-C` when finished.

## Contents

- `design.md` — main design/implementation contract.
- `prototype/index.html` and `assets/` — working, asset-based browser prototype.
- `FoodSafe-Preview.html` — self-contained offline demo.
- `FoodSafe-UI-Mockup-13-Screen-Board.jpg` — current 13-screen mockup board.
- `FoodSafe-UI-Mockup-Source-Comparison.jpg` — comparison against the original source.
- `reference/` — original mockup, rectified screen crops, geometry, and text-run measurements.
- `visual-qa/` — captures, overlays, comparison boards, and test reports.
- `ASSET-RESEARCH.md`, `ASSET-DECISION.md`, `ASSET-LICENSES.md` — external asset research and licensing notes.

No npm packages, remote font downloads, cloud API keys, or third-party assets fetched at runtime are required by the offline preview.
