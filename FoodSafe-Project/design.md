# FoodSafe — Pixel-Directed iOS Design & Implementation Contract

**Version:** 1.4 — perspective-rectified geometry, per-element and per-text-run coordinate atlas  
**Reference:** the supplied 1536 × 1024 JPEG containing 13 concept screens, hand annotations and hand-drawn food illustrations.  
**Primary target for layout calibration:** iPhone-sized portrait viewport, 390 × 844 logical points. Preserve the project’s existing deployment target; if the project has no target set, keep the implementation compatible with iOS 16.4+.  
**Status:** 13-screen HTML reference captured in a fresh local Playwright/Chromium run; 0 broken image references and 0 page errors. It is *not a verified native iOS pixel match*. The local Drawably-style control and Doodle-style icon treatments are style audition adapters, not the official upstream packages.

> **Fidelity rule:** do not invent source facts. The supplied image is a photographed/perspective-skewed collage, not the original Figma file or native screenshots. Original font files, vector paths, component constraints, exact source point values, and uncompressed food assets are not recoverable from this JPEG. This document therefore distinguishes **observed** content and palette families from **chosen implementation tokens**. The chosen tokens below are fixed and deterministic so an implementation agent can build consistently; they are not falsely labelled as recovered source CSS.

---

## Non-negotiable art direction — illustration-only product

The user explicitly rejects generic photos and all real-life pictures. **Never use photography anywhere in FoodSafe.** This includes recipe hero panels, cooking screens, inventory thumbnails, ingredient previews, cards, empty states, onboarding, and future features. Every food visual must be a cute drawing: hand-drawn outlines, soft colored-pencil/crayon texture, restrained watercolor/gouache fills, warm cream bases, friendly imperfect silhouettes, little leaf/sparkle doodles, and the existing green/terracotta/butter palette. Do not use stock photography, photorealistic AI images, realistic 3D renders, photographic food textures, or emoji as the main artwork. Prefer bundled SVG/PDF vector assets so the UI works fully offline and scales on Retina displays. The same illustration language must be applied consistently to dishes, ingredients, category tiles, storage icons, swap choices, and small status illustrations.

## 1. Required deliverables from the implementing agent

The agent receiving this document must create a real SwiftUI application, not a static replica image or a web view. The initial delivery is accepted only when it contains:

1. A reusable SwiftUI design system implementing the tokens and components in §3–§6.
2. All 13 screen states described in §7, with working navigation and the interactions in §8.
3. A deterministic local-data layer for ingredient quantities, storage zones, expiry dates, recipe ingredients, serving scaling, and ingredient swaps. All referenced functions must exist; no `TODO` handlers for visible controls.
4. Hand-drawn vector art or approved, high-resolution image assets. Do not ship emoji as a substitute for illustrated category icons or ingredient drawings.
5. A screenshot run for each screen at 390 × 844 points, plus a contact sheet and a list of differences still visible against the reference.
6. An accessibility pass: Dynamic Type without clipping, VoiceOver labels for icon-only controls, sensible contrast, and minimum 44 × 44 point interactive targets wherever the concept does not visibly require a smaller decorative control.

**Do not** flatten the screenshot into a background, place the reference image inside a `WKWebView`, copy the skewed phone frames or handwritten explanatory annotations into the app, add a generic card UI unrelated to the reference, introduce online recipe APIs, or replace the paper theme with a stock white/green dashboard.

---

## 2. Source interpretation and screen index

The image is 1536 × 1024 raster pixels. The screen frame rectangles below are coarse locator crops only. For actual reproduction, use the new coordinate atlas: [`reference/SCREEN-MEASUREMENT-ATLAS.md`](reference/SCREEN-MEASUREMENT-ATLAS.md) and machine-readable [`reference/SCREEN-COORDINATE-MASTER.json`](reference/SCREEN-COORDINATE-MASTER.json). That master file records all 13 source quadrilaterals in the original 1536×1024 collage, per-screen perspective matrices, and 289 named component/artwork bounds plus 231 distinct text-run bounds on rectified 390×844 canvases. It also records target text sizes, colors, deterministic rotations, and fit notes. These are visual measurements after rectification, not original Figma constraints; see the stated point tolerances.

| # | Screen ID | Visible screen title / purpose | Approx. source-sheet crop `(x,y,w,h)` |
|---:|---|---|---|
| 01 | `welcome` | FoodSafe welcome / onboarding | `(20, 20, 206, 528)` |
| 02 | `home` | My Kitchen | `(236, 51, 244, 513)` |
| 03 | `add` | Add Ingredient | `(488, 50, 266, 485)` |
| 04 | `inventory` | Inventory | `(757, 55, 258, 515)` |
| 05 | `suggestions` | Recipe Suggestions | `(1016, 56, 250, 499)` |
| 06 | `detail` | Tomato Pasta | `(1265, 72, 261, 476)` |
| 07 | `cooking` | Cooking… | `(34, 573, 227, 387)` |
| 08 | `scaling` | Portion Scaling | `(270, 574, 210, 385)` |
| 09 | `swaps` | Ingredient Swaps | `(485, 576, 210, 378)` |
| 10 | `meals` | Meal Suggestions | `(696, 575, 230, 381)` |
| 11 | `lentil` | Lentil Soup / Steps tab | `(925, 575, 201, 382)` |
| 12 | `expiry` | Expiration Priority | `(1129, 576, 187, 378)` |
| 13 | `settings` | Settings | `(1317, 577, 203, 379)` |

The freehand arrows, stars, captions such as “Everything you have, at a glance!”, the paper scraps, and the yellow annotation card belong to the *presentation board*, not the actual app. Recreate the app’s paper surfaces and its own small decorative accents; do not place the presentation-board labels over the UI.

### Global silhouette

- Portrait, full-screen, warm paper-like canvas; no blue/white stock iOS background.
- Most app pages have content inset roughly 14–18 pt from the display edges. Header alignment is hand-composed rather than perfectly geometric, but control alignment must remain stable and accessible.
- Screen outlines in the source are the mockup’s drawn phone bezels; **do not render those outer phone bezels inside the native application**.
- Native iOS status bar is system-owned. The “9:41” text in the reference is a mock status indicator, not app content to manually draw in SwiftUI.
- Persistent bottom navigation is visible on **My Kitchen**, **Inventory**, and **Settings**. The concept sheet omits it on full-screen flows and several recipe screens; follow that visible treatment rather than forcing a tab bar on every page.

---

## 3. Colour system

### 3.1 What was sampled versus what is prescribed

The largest warm paper pixel clusters in the supplied image include `#F4ECDC`, `#F4ECD4`, `#FCECDC`, and `#F4E4D4`. Green painted elements cluster around values such as `#44745C`, `#547C5C`, and `#4C745C`. Peach alert/card surfaces include values around `#FCDCC4`; pale green category fills include values around `#DCDCBC` and `#DCE4C4`. These samples vary due to paper grain, antialiasing, lighting, perspective, and image compression.

The following are **fixed implementation tokens** selected from those observed families. Use them consistently instead of re-sampling arbitrary pixels during implementation. Where a sampled family and prescribed hex differ by a few values, the prescribed token takes precedence.

| Token | Hex | Use | Confidence / note |
|---|---|---|---|
| `paper.base` | `#F7EEDC` | Main screen surface | Best-fit warm cream; original paper is textured and non-uniform. |
| `paper.highlight` | `#FBF4E5` | Input/card highlights, button text | Slightly lighter than base; avoid pure white. |
| `paper.card` | `#FAF2E1` | Translucent card fill | Set at ~50–70% opacity over `paper.base`; visual estimate. |
| `paper.deep` | `#E8DCC5` | Subtle separators/shadows | Derived from observed darker paper patches. |
| `ink.primary` | `#282E28` | Main text, core icon strokes | Warm charcoal, not absolute black. |
| `ink.secondary` | `#6B604F` | Metadata, helper copy, secondary icons | Muted brown-grey. |
| `line.primary` | `#827460` | Card/input outline | Use at 45–65% opacity; it must look pencil-like, not black. |
| `line.subtle` | `#BFB19A` | Internal dividers, inactive borders | Use at 25–45% opacity. |
| `green.primary` | `#527B5E` | Primary buttons, selected storage/filter chips, active navigation | Chosen representative of dominant sampled green family. |
| `green.deep` | `#2E6A4F` | FoodSafe wordmark, selected text/icons, stronger green strokes | Slightly darker than fills. |
| `green.light` | `#DCE4C4` | Vegetables tile, selected swap, pale ready tags | Closely matches measured pale-green cluster. |
| `green.wash` | `#EAF0DC` | Ready/positive info surfaces | Use only as a pale wash. |
| `peach.surface` | `#F8DCC4` | Quick alert, soft orange/peach surfaces | Representative of the peach color family visible in the reference. |
| `orange.primary` | `#E7A34D` | Small stars, warning icons, ripe-food accents | Accent only; not a full-page fill. |
| `orange.light` | `#FBE6C7` | Almost Ready pills, low-stock tile | Soft yellow-orange. |
| `red.primary` | `#C96658` | Expiry text, critical badges, missing-ingredient message | Restrained terracotta red, not bright system red. |
| `red.light` | `#F8D8CB` | Expiration alert background | Soft coral/rose. |
| `blue.primary` | `#5B8DA5` | Smart Swap labels and rare cool accents | Keep limited. |
| `blue.light` | `#DAE9EC` | Dairy tile, smart-swap wash | Pale muted blue. |
| `lavender.light` | `#DFDAE9` | Others/custom category tile | Desaturated lavender. |
| `yellow.light` | `#F4CE83` | Star/sun/fruit accents | Warm golden accent. |

### 3.2 Component-to-colour mapping

- **Background:** clean warm cream `paper.base` (`#F7EEDC`). Keep it visually quiet so the hand-drawn cards, artwork and tiny accents carry the paper/notebook feel.
- **Primary button:** `green.primary` fill, `paper.highlight` label, 0.8–1.0 pt `green.deep` edge. No glossy gradient. A very soft bottom edge/shadow is acceptable.
- **Selected storage/filter chip:** `green.primary` fill and `paper.highlight` text.
- **Unselected chip/input:** translucent `paper.card` fill, `line.primary` at ~50%, `ink.primary` label.
- **General card:** `paper.card` fill; `line.primary` at ~52%; one subtle inset highlight; shadow no more than 0–2 pt.
- **Expiring Soon:** `red.light`/peach pill with `red.primary` text; supporting date text `red.primary`.
- **Almost Ready:** `orange.light` with muted amber/brown text.
- **Smart Swap:** `blue.light` with `blue.primary` text.
- **Ready Now / All ingredients available:** `green.light` or `green.wash` with `green.deep` text.
- **Body typography:** `ink.primary`. Metadata/helper copy: `ink.secondary`.
- Never use saturated neon green, pure black outlines, bright system-red warnings, heavy blur/glass effects, or purple for primary actions.

### 3.3 Warm paper surface — clean version (creased background intentionally reverted)

The user reviewed the heavy crumpled-paper background and explicitly asked to revert it because it made the UI worse. **Do not use `PaperCreases (deprecated; do not use)` as the full-screen background in the current reference.** The correct present treatment is a calm, flat warm cream surface with the source's paper-like feeling supplied by the cream palette, fine outlines, subtle card shadows, small illustration accents, and irregular shape/rotation rules—not a visible crease-photo layer.

- Main surface: `#F7EEDC` (`paper.base`). Slight natural variation is acceptable only if it remains nearly invisible at normal viewing size.
- Browser contract: `.screen { background-color: var(--paper); background-image: none; }`; `.device:before` remains transparent and has no texture overlay.
- Do not use `PaperCreases (deprecated; do not use).imageset` in the current screen backgrounds. Keep its asset only as a discarded experiment/reference file; it is not part of the desired look.
- Do not add dotted grain, noise overlays, deep folds, heavy paper stains, torn edges, dark vignettes, or corner burns. Those visually compete with the actual source, which is already softly textured but not dominated by obvious folds.
- A very subtle paper grain may be reconsidered only after a side-by-side render review and only if it improves rather than overpowers the reference. The current approved baseline is the clean cream canvas.

**SwiftUI reference implementation**

```swift
ZStack {
    Color(red: 247 / 255, green: 238 / 255, blue: 220 / 255)
        .ignoresSafeArea()
    screenContent
}
```


## 4. Typography system — one hand-printed face across the entire interface

### 4.1 What the source lettering actually looks like

The supplied collage is the only typographic specimen, so the exact original font binary cannot be proven. The visible app lettering is **hand-printed, not formal cursive**: rounded but irregular forms, slight per-letter angle and baseline variation, narrow-to-medium proportions, a dark charcoal pen line, little or no tracking, and an organic rather than geometric rhythm. It appears to be a handwritten print face applied consistently to almost all interface copy. It is not merely a display heading style.

In the source, `My Kitchen`, `Add Ingredient`, `Inventory`, category captions, `Quantity`, `500`, unit labels, list item names, alert copy, metadata such as `15 min · 3 servings`, chip labels, ingredient quantities, cooking steps, helper text, button labels (`Save`, `Start Cooking`, `View All Suggestions`), bottom-tab captions (`Home`, `Inventory`, `Recipes`, `More`), and settings rows all share the same hand-printed family. They differ in point size, color, and occasionally weight—not family. A polished sans-serif body with a handwritten heading is specifically incorrect.

The welcome wordmark `FoodSafe` is an illustrated brand mark with a distinct brush-script character; preserve it as the source-derived artwork, not as live text. All other app-authored UI copy uses the single hand-printed family below. In the HTML prototype, even the simulated status-bar text uses this face so no prototype label silently reverts to system sans-serif. A real iOS status bar is OS-owned and cannot be assigned an app font; that is a platform limitation rather than an in-app typography exception.

### 4.2 Active typeface for this offline pack

**Active implementation font: Purisa Regular, locally bundled.** This is the most handwritten face already available in the offline working environment and is visibly more irregular than Comic Neue. The matching **Purisa Bold** face is used only for the source's occasional stronger emphasis. Purisa is an implementation choice, not a verified identification of the original font; do not describe it as the exact source binary.

- **All interface copy:** Purisa Regular 400 by default—titles, labels, list rows, field captions and values, quantity values, placeholder copy, metadata, pills/chips, navigation captions, button text, recipe copy, settings, alerts, validation messages, and all small helper strings.
- **Emphasis only:** Purisa Bold 700 for the few short labels that visibly need extra ink weight. Do not turn every label into bold.
- **Brand wordmark:** keep `assets/foodsafe-wordmark.png` as source-derived artwork. This is the only app-facing text-like art with its own distinctive brand-lettering treatment.
- **No alternate display/body pairing:** do not switch to Comic Neue, SF Pro, Inter, Arial, Helvetica, Segoe UI, Roboto, rounded system fonts, or a generic native default for any app-authored text. No CSS rule may set a different family for body, headers, controls, buttons, tabs, metadata, or pseudoelement text.

### 4.3 Why the active font is not claimed to be pixel-exact

The original was delivered as a flattened, skewed image collage, not a source Figma file or editable text layer. The source family cannot be identified with forensic certainty from these pixels. Purisa's hand-written print forms are the reproducible local choice for this pack; the specimen in `visual-qa/final/font-weight-audit.png` documents its regular and bold weights against the older alternative. Never silently substitute a fallback and say it is the original.

### 4.4 Size, weight and ink density at the 390 × 844 pt baseline

Sizes are logical points. Keep the source's compact hand-lettered rhythm; do not inflate it into a spacious modern dashboard. Family remains identical across all roles; only size, color and source-supported emphasis vary.

| Role | Family / weight | Size | Color | Line-height target | Additional treatment |
|---|---|---:|---|---|---|
| Welcome wordmark | Source-derived brush artwork | 60–66 pt visual height | `#2E6A4F` | 0.90–0.98 visual box | retain its original tilted brush lettering |
| Welcome tagline | Purisa 400 | 21–23 pt | `#315C43` | 1.00–1.08 | two centered lines; rotate about -1.2° |
| Standard screen title | Purisa 400 | 21–24 pt | `#282E28` | 1.0–1.08 | subtle per-screen rotation; no all-caps |
| Recipe detail title | Purisa 400 | 26–29 pt | `#282E28` | 1.0–1.08 | source-like compact title with light tilt |
| Section heading | Purisa 400; 700 only for observable emphasis | 14–19 pt | `#282E28` | 1.05–1.18 | slight tilt; preserve source casing |
| Main body / cooking step | Purisa 400 | 13–16 pt | `#282E28` | 1.20–1.32 | natural hand-printed copy; never justified |
| Field label and list row | Purisa 400 | 13–15 pt | `#282E28` | 1.03–1.15 | same face, not a native-font exception |
| Quantity / ingredient amount | Purisa 400 | 12–14 pt | `#282E28` | 1.05–1.15 | stable right alignment, still hand-printed |
| Metadata / helper copy | Purisa 400 | 10.5–12 pt | `#6B604F` | 1.05–1.18 | retain readability; no other family at small sizes |
| Chip / pill label | Purisa 400 | 11–13 pt | semantic ink color | 1.0–1.08 | compact source-like words and numbers |
| Tab caption | Purisa 400; active can use 700 | 10–11 pt | `#6B604F`; active `#2E6A4F` | 1.0–1.08 | tiny text is still hand-written |
| Primary button label | Purisa 400 | 15–17 pt | `#FBF4E5` | 1.0–1.08 | not system semibold; avoid synthetic bold |
| Onboarding/supporting copy | Purisa 400 | 18–20 pt | `#514B3E` | 1.25–1.35 | source-like loose, intentional line breaks |
| Mock status time in HTML preview | Purisa 400 | 10–12 pt | `#282E28` | 1.0 | preserve status-row geometry, but use the shared family in this prototype |

### 4.5 Mandatory web/CSS contract

The HTML must load only local font binaries. It must apply the same semantic family to every element and generated text node, including native-looking controls rendered by the browser. A global guard is intentional because one missed inherited style is the exact failure this revision is meant to prevent.

```css
@font-face {
  font-family: "FoodSafe Hand";
  src: url("../assets/fonts/Purisa-Regular.otf") format("opentype");
  font-weight: 400;
  font-style: normal;
  font-display: block;
}
@font-face {
  font-family: "FoodSafe Hand";
  src: url("../assets/fonts/Purisa-Bold.otf") format("opentype");
  font-weight: 700;
  font-style: normal;
  font-display: block;
}
:root { --hand: "FoodSafe Hand", cursive; --body: "FoodSafe Hand", cursive; }
html, body, body *, body *::before, body *::after {
  font-family: "FoodSafe Hand", cursive !important;
  font-synthesis: none !important;
}
```

The local face must load from `assets/fonts/`. Do not fetch fonts at runtime. Keep the font-family name exactly consistent so `font-weight:400` resolves to Purisa Regular and `font-weight:700` resolves to Purisa Bold. The offline prototype checks the loaded regular and bold faces through `document.fonts`; missing files set `data-foodsafe-font="missing"` and log an explicit QA error. The prototype and native implementation may not use unrelated fonts to “improve” a role.

### 4.6 Native SwiftUI typography contract

Register both bundled Purisa files in the app target and verify their actual internal/PostScript names with the font metadata before coding. Route all app-authored text through one semantic typography helper; never scatter `.font(.system(...))` through screens.

```swift
enum FoodSafeType {
    static func hand(_ size: CGFloat) -> Font {
        .custom("Purisa", size: size, relativeTo: .body)
    }

    static func handBold(_ size: CGFloat) -> Font {
        .custom("Purisa-Bold", size: size, relativeTo: .body)
    }
}
```

These PostScript/internal names are *provisional until verified in the bundled files*. Update these two constants if font metadata reports different names, but do not replace the family. Use Dynamic Type-relative custom fonts where possible while preserving the reference's compact line breaks at the 390 pt baseline.

### 4.7 Hand-printed rendering rules

- The exact same font family must be visible in **every app-authored text role**, not only the header: body copy, helper copy, labels, inputs and placeholders, data values, status badges, chips, pills, buttons, nav captions, alerts, dialogs and inline feedback.
- Base weight is 400. Use 700 only where the source clearly emphasizes a short label. Do not make every line bold just to increase handwritten character.
- Do not italicize the regular face or randomly rotate individual glyphs. The face gives the word-level hand-written print; fixed tiny wrapper rotations provide the scrapbook touch.
- Keep tracking at 0 or very close to 0. Do not use wide letter spacing to fake handwriting.
- Do not use emoji as text substitutes for illustrated icons. The FoodSafe wordmark is a source-derived illustration, not a second text font in the UI.
- Add no `font-family` exception for tiny strings, accessibility labels' visible captions, input values, button labels, metadata or pseudo-elements. SVG icon path shapes are exempt because they are not text.
- For real native iOS, the OS status bar/home indicator and system permission sheets are platform-owned. The browser prototype's simulated status line remains in Purisa so reviewers can see the requested global lettering behavior in the reference UI.

## 5. Geometry, spacing, and reusable components

### 5.1 Baseline, safe areas, and intentional hand-composed tilt

- Build and snapshot first at **390 × 844 logical points**, portrait.
- Use SwiftUI safe areas. The top system/status area and bottom home-indicator area must not be counted as content padding. Do not hard-code `9:41` into production.
- Default horizontal inset: 14–17 pt on content screens; 20–24 pt on welcome. The original mockup is compact and hand-composed; do not expand it to modern large-header spacing.
- Common vertical rhythm: 5, 7, 9, 11, 14, 18 pt. Keep cards and content visibly close together like the reference.
- Content that exceeds the viewport scrolls under the header. Bottom-anchored CTAs remain above the bottom safe area.
- The **outer phone frame tilt** visible in the source collage is a presentation-board effect and must not be recreated inside the app. The *internal UI* has its own tiny hand-drawn tilt and this **must be recreated**: hand-lettered text, pills, cards, illustration frames, buttons, and doodles should not all be perfectly mechanically level.
- Tilts are deterministic. Never use `random()` during rendering. Do not tilt the entire screen or all content as a single transform, and do not rotate hit-test geometry separately from its visible control.

**Per-screen title rotation** (clockwise-positive degrees; use `rotationEffect(.degrees(...))` in SwiftUI, CSS `rotate` in prototype):

| Screen ID | Rotation |
|---|---:|
| `home` | -1.0° |
| `add` | +0.85° |
| `inventory` | -0.65° |
| `suggestions` | +0.8° |
| `detail` | -0.85° |
| `cooking` | +0.75° |
| `scaling` | -0.95° |
| `swaps` | +0.8° |
| `meals` | -0.65° |
| `lentil` | +0.9° |
| `expiry` | -0.8° |
| `settings` | +0.65° |

**Component tilt tokens** (these approximate the visible wobble; they are implementation values, not mathematically recovered source coordinates):

| Component | Rotation rule | Anchor / guardrail |
|---|---|---|
| Welcome `FoodSafe` wordmark | -4.5° | center; do not rotate the entire welcome stack |
| Welcome tagline and copy | -1.2° / -1.6° | center; line breaks stay identical |
| Screen title | use per-screen table above | center; title remains within header bounds |
| Section headings | alternate fixed -0.8° / +0.65° by section order | leading; max absolute 0.9° |
| Primary capsule buttons | -0.65°; on pressed state preserve angle and translate down 1 pt | visible capsule only; keep full unrotated hit target |
| Secondary buttons | +0.55° | keep pair edges and hit targets aligned |
| Filter chips | odd item -0.7°, even item +0.55°, third item -0.35° | don't let them overlap or change row height |
| Category tiles | sequential set `[-0.45°, +0.55°, -0.35°, +0.8°, +0.3°, -0.6°, +0.55°]`, repeat after the seventh | rotate tile and artwork as one unit; preserve 8–9 pt gaps |
| List / recipe cards | alternating -0.45° / +0.55° | rotate card and contents together; keep stable row gaps |
| Ingredient thumbnails | alternate ±0.7° inside the frame | only the image/mount, not the quantity text |
| Text labels inside forms | rotate label wrapper about -0.35°; alternate selected labels +0.3° | field hitbox remains square to layout |
| Decorative stars, leaves, pencil strokes | individual asset's authored angle | free placement, never cover content |

Do not rotate every character as separate text. The **font itself** provides most of the handwritten character; transforms supply the final small, tangible paper-and-pen irregularity. Section headings and selected product/recipe labels must also rotate slightly at the text-wrapper level (roughly -0.8° to +0.65°), while regular paragraph/cooking copy stays close to level for readability. If a rotation causes a 44 pt target to stop receiving taps correctly, keep an unrotated container for hit testing while rotating only its visible child.


### 5.2 Surface shapes

| Component | Baseline dimension | Radius / stroke | Notes |
|---|---|---|---|
| Main content inset | 16 pt | — | Welcome: 24 pt. |
| Header | 44–50 pt content height below safe area | — | Back button at leading edge; title uses flexible center. |
| Storage/filter chip | 34–38 pt high | Capsule; 0.8 pt border | Three chips share width when shown as a row. |
| Search field | 40–42 pt high | 20–22 pt radius; 0.8 pt border | Search glyph left; placeholder warm grey. |
| Standard input | 42–45 pt high | 12–14 pt radius; 0.8 pt border | Cream translucent fill. |
| Large note field | 82–90 pt high | 12–14 pt radius | Placeholder muted brown; multiline. |
| Category tile | 74–80 pt high | 14–17 pt radius | Pastel fill, hand-drawn icon, caption. |
| General card | Content-driven; usually 58–72 pt | 14–16 pt radius; 0.8–1.0 pt outline | Avoid heavy shadows. |
| Inventory row | 66–72 pt high | 13–15 pt radius | 48–54 pt image/illustration. |
| Recipe suggestion card | 112–124 pt high | 13–16 pt radius | Thumb at left, metadata/title at right. |
| Recipe hero | Full content width; 124–150 pt high | 0–4 pt radius at top edge | Full-width illustrated dish; controls overlaid as circular paper buttons. |
| Pill / status badge | Content-driven, minimum 22–26 pt | Capsule | Pale category fill. |
| Primary CTA | 46–50 pt high | Full capsule; 0.8–1.0 pt edge | Full available width unless an action pair is shown. |
| Secondary CTA | 42–46 pt high | Capsule; 0.8 pt edge | Pale fill, ink text. |
| Bottom tab content | About 56–62 pt + system bottom safe area | Top separator only | Five actions, central Add raised in a green circle. |
| Small circular icon button | 32–38 pt hit target | Circle | Drawn outline or small hand symbol. |

### 5.3 Cards and linework

- Use a 0.8–1.0 pt `line.primary` stroke around 50–60% opacity.
- Add one subtle inner highlight at the top edge and a 0–2 pt downward shadow. It should feel like a sketchbook card laid on paper, not a floating material-design card.
- If custom `Shape` paths are used for the hand-drawn border, keep irregular offsets within ±0.6 pt and deterministic. Never animate the edge.
- Inset separators use `line.subtle` at 25–40% opacity.
- Avoid pure white card fills; use `paper.card` over the clean warm-cream `paper.base` surface.
- A few cards may have subtly non-identical corners (radius offsets of 1–2 pt) or a ±0.25–0.30° rotation. Do not give every card the same large pill-like radius or a thick uniform vector stroke.
- Keep line edges warm and slightly imperfect. Don't simulate hand drawing with a dark cartoon outline, chalk texture, or jagged path.

### 5.4 Primary and secondary buttons

**Primary:** forest green fill (`green.primary`), cream Purisa Regular 400 label, rounded capsule, faint dark-green edge, subtle one-pixel bottom shadow. Press state darkens slightly and moves down by at most 1 pt. Examples: “Get Started”, “Save”, “Start Cooking”, “Update Recipe”, “Use Lime Instead”.

**Secondary:** transparent/paper fill, brown outline, ink label. Back/Next on the Cooking screen use the same footprint and height; “Next” is primary.

**Icon placement:** text remains the visual center. For buttons with arrow/plus/cooking icon, keep icon at 16–20 pt and optical balance so the label is not pushed far off-center.

### 5.5 Navigation bar

Order, left to right:

1. **Home** — home outline icon.
2. **Inventory** — pantry/inventory outline icon.
3. **Add** — green 42 pt circular button, white plus, elevated around 8–10 pt above neighboring icons.
4. **Recipes** — recipe/notebook outline icon.
5. **More** — three-dot outline icon.

Inactive icon/label: `ink.secondary`; active icon/label: `green.deep`, label medium/bold. Tab height around 56 pt; bottom safe area remains clear. Do not put tab labels inside pills.

---

## 6. Illustration and asset language

**Non-negotiable art direction — illustrated food, illustrated icons, illustrated controls:** FoodSafe must not use real-life food photography, stock photography, photorealistic generated food, or camera-like imagery. Every food subject (tomatoes, eggs, pasta, soup, chicken, spinach, oil bottles, herbs, fruit, ingredient swaps and cooking scenes) must be a hand-drawn illustration that visually belongs to the supplied reference. The same hand-drawn language applies to icons, category tiles, alert symbols, storage-zone symbols, navigation icons, badges, decorative marks, and button details. Buttons are still functional UI controls, but their outlines and small details should feel drawn by hand—not like default platform controls or glossy 3D buttons.

### 6.1 Shared illustration style

- Use a cute, warm colored-pencil + soft gouache/watercolor fill, with imperfect dark olive/brown pen outlines, slightly uneven contour lines, and restrained pencil hatching.
- Use a limited palette: warm cream, leaf green, tomato/coral red, butter yellow, muted orange, olive, and soft blue accents. Keep fills matte and slightly imperfect.
- Food must read as a drawing at thumbnail size: simplified forms, clear silhouettes, a few hand-drawn internal details, and tiny expressive accents where appropriate. No photographic texture, lens blur, specular shine, realistic lighting, realistic kitchen/table backgrounds, or cut-out photography.
- Dish illustrations show a complete illustrated bowl, plate, pot, or pan. Do not put a photo inside an illustrated frame. A cooking scene with a pan is also illustrated, including the pan and food.
- Icons use the same ink color and palette, rounded hand-drawn paths, subtle asymmetry, and an approximately 1.5–2 pt stroke at a 24 pt baseline. Avoid mixing emoji, stock icon libraries, and unrelated icon families.
- Buttons use solid muted green or paper fills, hand-inked outlines, slightly irregular corner radii, and optional tiny illustrated accents (leaf, sparkle, arrow, chef-hat) drawn in the same style. Keep text contrast, hit areas, and accessible focus states intact; irregularity must not harm usability.
- The paper background remains clean warm cream. Do not add heavy crumples, prominent creases, or noisy paper overlays. The handmade feeling comes from illustrations, outlines, typography, restrained tilt, and subtle shadows.

### 6.2 Required production asset inventory

Create or source the following as named assets. Each should be exported with transparent background where appropriate, include a 2×/3× vector or raster original, and use the same line weight and palette:

| Asset ID | Contents | Intended uses |
|---|---|---|
| `paper.background.clean` | `#F7EEDC` solid warm cream token | Current full-screen background on all screens; no texture image |
| `brand.foodsafe.wordmark` | “FoodSafe” brush-script wordmark, deep green | Welcome only. Prefer editable vector; do not redraw it with a system font. |
| `illustration.welcome-grocery-bag` | Grocery bag, face, green leaves, produce, handle | Welcome hero illustration. |
| `icon.home` | House with roof and door | Header and tab. |
| `icon.inventory` | Cabinet/list/box symbol | Inventory tab. |
| `icon.recipes` | Cookbook/notebook | Recipes tab and related affordances. |
| `icon.more` | Three dots | More tab. |
| `icon.fridge`, `icon.pantry`, `icon.freezer` | Storage zone symbols | Add Ingredient and Settings. |
| `icon.category.vegetables` | Leafy vegetable | Category grid. |
| `icon.category.fruits` | Apple/orange fruit | Category grid. |
| `icon.category.dairy` | Milk bottle | Category grid. |
| `icon.category.grains` | Baguette/grain | Category grid. |
| `icon.category.proteins` | Meat/beans | Category grid. |
| `icon.category.others` | Linked items/miscellaneous | Category grid. |
| `icon.category.leaves` | Handwritten plus-mark in the source’s final pale tile; caption “Leaves” | Category grid. |
| `icon.expiring`, `icon.low-stock`, `icon.almost-empty` | Clock/food/low-content jar | Quick Overview cards. |
| `food.tomatoes` | Tomatoes; framed image for Add Ingredient | Add Ingredient. |
| `food.inventory.tomatoes`, `.eggs`, `.spinach`, `.pasta`, `.olive-oil`, `.chicken` | Small isolated ingredient thumbnails | Inventory/expiry lists. |
| `food.recipe.tomato-pasta` | Cute hand-drawn bowl of tomato pasta with basil | Tomato Pasta detail; colored-pencil and soft gouache illustration. |
| `food.recipe.tomato-pasta.thumb` | Square/rounded thumbnail crop of same dish | Suggestions and scaling. |
| `food.recipe.chicken-stir-fry` | Chicken and vegetables in a bowl | Suggestions. |
| `food.recipe.lentil-soup` | Lentil soup in bowl, herbs/vegetables visible | Lentil Soup detail and suggestions. |
| `food.recipe.vegetable-curry` | Vegetable curry | Meal Suggestions. |
| `food.cooking.tomato-pasta` | Pasta in pan/pot, step image | Cooking. |
| `food.ingredient.lemon`, `.lime`, `.vinegar`, `.orange` | Small isolated ingredient illustrations | Ingredient Swaps. |
| `icon.favorite`, `icon.search`, `icon.chevron`, `icon.calendar`, `icon.clock`, `icon.check`, `icon.warning`, `icon.settings`, `icon.units`, `icon.offline`, `icon.about` | Coherent hand-drawn action icon family | Across app. |

### 6.3 Hand-drawn illustration references used by the prototype

`assets/illustrations/` contains 21 small transparent PNG crops extracted from the user's supplied UI collage: category artwork (vegetables, fruit, dairy, grains, proteins, others/plus), home Quick Overview symbols, pasta recipe ingredient marks, and lemon/lime/vinegar/orange swap art. The browser prototype now uses those crops in the category grid, overview rows, Tomato Pasta ingredient list/portion scaling, and ingredient-swap options instead of platform emoji where a source crop exists. These are reference-locked raster crops, not scalable original vectors; retain them as tracing/visual anchors or use them only for the prototype. For final iOS artwork, redraw them as clean vector paths with the same hand-drawn silhouette, stroke colour, fill and slight asymmetry, and compare against these crops at the baseline scale.

### 6.4 Illustrated food assets shipped with this pack

The `assets/` directory contains original local SVG drawings for every food-art slot. These assets are intentionally illustrated rather than photographic. The source mockup includes food photos, but the product direction has explicitly changed: **do not reproduce those photos**. Use the same cohesive cute hand-drawn language across every screen, ingredient, dish, alert, and empty state. SVGs must remain offline-capable and scale cleanly.

The following crops were taken from the supplied source image; coordinates are approximate source-pixel bounds `(x1,y1,x2,y2)`:

| Crop file | Approximate source crop | Purpose |
|---|---|---|
| `tomato-pasta-hero-clean.jpg` | `(1310,101,1475,161)` | Tomato Pasta hero preview |
| `tomato-pasta-thumb.jpg` | `(1042,222,1089,261)` | Suggested recipe thumb |
| `chicken-thumb.jpg` | `(1040,293,1088,332)` | Chicken Stir-fry thumb |
| `lentil-thumb.jpg` | `(1040,373,1088,414)` | Lentil Soup thumb |
| `tomato-large.jpg` | `(520,128,600,190)` | Add Ingredient preview |
| `tomato-inventory.jpg` | `(790,202,830,240)` | Inventory row |
| `eggs-inventory.jpg` | `(790,251,830,290)` | Inventory row |
| `spinach-inventory.jpg` | `(790,296,830,338)` | Inventory/expiry row |
| `pasta-inventory.jpg` | `(790,353,830,391)` | Inventory row |
| `olive-oil-inventory.jpg` | `(790,406,830,445)` | Inventory row |
| `chicken-inventory.jpg` | `(790,470,830,509)` | Inventory/expiry row |
| `cooking-pasta.jpg` | `(61,667,239,755)` | Cooking step image |
| `scaling-tomato.jpg` | `(289,645,318,675)` | Portion Scaling recipe thumb |
| `lemon-swap.jpg` | `(514,674,548,708)` | Ingredient Swaps placeholder |
| `lime-swap.jpg` | `(514,713,550,746)` | Ingredient Swaps placeholder |
| `meal-tomato-clean.jpg` | `(722,704,755,737)` | Meal Suggestions thumb |
| `meal-chicken-clean.jpg` | `(723,792,757,827)` | Meal Suggestions thumb |
| `meal-curry-clean.jpg` | `(723,859,757,894)` | Meal Suggestions thumb |
| `meal-lentil-clean.jpg` | `(723,923,757,951)` | Meal Suggestions thumb |
| `lentil-soup-hero-clean.jpg` | `(954,638,1068,691)` | Lentil Soup hero preview |

---

## 7. Screen-by-screen specification

**Screen-coordinate rule:** the visual proportions and relationships are now documented in the measurement atlas. Exact original source point constraints are still unavailable, but the flattened source has been manually rectified and each visible logical component/text block has an estimated `[x,y,width,height]` in logical points on a 390×844 canvas, along with target rotation, type role, color and notes. Use [`reference/SCREEN-COORDINATE-MASTER.json`](reference/SCREEN-COORDINATE-MASTER.json) as the machine-readable geometry source and [`reference/SCREEN-MEASUREMENT-ATLAS.md`](reference/SCREEN-MEASUREMENT-ATLAS.md) for readable tables. Position estimates have an explicitly stated tolerance; do not claim the values are recovered Figma constraints.

### 01 — Welcome (`welcome`)

**Purpose:** explain the product and begin the local kitchen setup. This screen is an onboarding/landing page, not a device screenshot with a visible status bar.

**Composition from top to bottom:**

1. Clean warm-cream canvas (`paper.base`); no visible creases or grain overlay (the heavier paper experiment was explicitly reverted).
2. `FoodSafe` wordmark, centered, deep green, large brush-style hand lettering. It may be tilted by roughly -3° to -5° as a brand treatment.
3. Tagline, two lines: **“Good food.” / “Less waste.”** centered in green Purisa Regular 400.
4. Hero illustration of a smiling grocery bag with leafy greens/produce. It should dominate the visual middle and be recognisable at a glance; target about 275–315 pt wide and 285–330 pt high depending on available device height.
5. Three-line support copy: **“Your kitchen. / Your ingredients. / Better meals.”** centered, warm dark brown, slight organic line positioning is acceptable but do not skew the text enough to affect legibility.
6. Wide green CTA: **“Get Started”** with a small right arrow. Below it, understated **“Sign In”** text link.
7. Optional small sun/star/leaf doodles around margins, never overlapping text or the mascot.

**Layout:** centered column; use 24 pt horizontal margins; leave an organic-but-intentional vertical rhythm. The last link should sit above the bottom safe area rather than leaving a large empty bottom half.

**Interaction:** “Get Started” opens My Kitchen (or the existing onboarding/setup flow if one exists). “Sign In” should not lead to a fake login: if the product is offline-only and has no account feature, either remove the link only with product approval or show a clearly honest local-profile/help sheet. For the static visual parity prototype, both links route into the home preview.

**Asset direction:** a hand-drawn vector grocery bag with a face and colourful produce. Do not use a Unicode shopping-bag emoji.

### 02 — My Kitchen (`home`)

**Purpose:** inventory overview by storage zone, plus quick routes to items that need attention.

**Header:**
- System status bar above.
- Leading house icon at x≈16 pt, green linework.
- Title **“My Kitchen”** in Purisa Regular 400, approximately 23–24 pt; align to left of the middle area, not centered on the full screen.
- Right-side outline heart/favorite icon and small golden accent sparkle.

**Content order:**
1. Three storage zone chips: **Fridge**, **Pantry**, **Freezer**. Equal-width row; default selected **Fridge**. Selected chip is green/cream; other chips are paper fill with brown outline.
2. Search field placeholder **“Search ingredients…”**, search icon at leading edge.
3. Category grid, four columns on row one and three on row two: **Vegetables**, **Fruits**, **Dairy**, **Grains**, then **Proteins**, **Others**, and the final pale tile with the handwritten plus mark and label **“Leaves”**. Preserve the source wording and its non-standard plus-mark icon; do not replace it with a lemon/fruit glyph. Use the pastel colors from §3.2 and hand-drawn category icons.
4. Section header: **“Quick Overview”**, with a small gold sparkle/star near the heading.
5. Peach notification strip: warning symbol + **“3 items need attention”** + trailing chevron.
6. Three full-width overview cards:
   - **Expiring Soon** / **“2 items · within 24h”** with a clock/expiry illustration.
   - **Low Stock** / **“4 items”** with a low-stock ingredient illustration.
   - **Almost Empty** / **“2 items”** in coral/red secondary text with a jar/near-empty illustration.
7. Bottom tab bar with **Home** active and raised central Add.

**Vertical rhythm:** this is a content-rich page. The overview cards should finish near the bottom navigation instead of stopping halfway down. Do not insert a decorative blank ad-sized block below “Almost Empty”.

**Interactions:**
- Storage chips filter or scope the inventory overview to the selected zone; selected visual state must update immediately.
- Search filters ingredients as the user types.
- Category tile opens Inventory with that category filter applied.
- “3 items need attention”, “Expiring Soon”, “Low Stock”, and “Almost Empty” open Expiration Priority or a matching filtered inventory list; no inert cards.
- Central plus opens Add Ingredient.
- Tabs route to Home, Inventory, Add Ingredient, Recipe Suggestions, and Settings/More.

### 03 — Add Ingredient (`add`)

**Purpose:** store a quantity of an ingredient in a specific zone and track expiry.

**Header:** back arrow on left; centered title **“Add Ingredient”**; no bottom tab bar.

**Content order:**
1. Product row: framed cute hand-drawn illustration of **Tomatoes** at left (about 105–115 × 95–105 pt); title **“Tomatoes”** at right; a pale green category chip **“Vegetable”** with a small leaf/check icon; a tiny decorative botanical mark near the upper-right of the row.
2. Label **“Quantity”**.
3. Input row: numeric field **“500”** with flexible width; unit menu **“g”** at right with down chevron. Keep unit in its own bordered field.
4. Label **“Storage Zone”**.
5. Three equal controls: **Pantry**, **Fridge**, **Freezer** with their respective zone icons. **Fridge** selected by default.
6. Label **“Expiration Date”**.
7. Date field: calendar icon, **“Apr 20, 2026”**, trailing chevron.
8. Label **“Notes (optional)”**.
9. Multiline field placeholder **“e.g. organic, fresh, etc.”**
10. Bottom-anchored green CTA **“Save”**, with a small check mark. Keep it above the home-indicator safe area.

**Component details:** labels are dark handwritten type, 14–15 pt. Inputs around 44 pt high; notes about 84–90 pt high. Keep field-to-label rhythm consistent. Use a clean product image, not a distorted collage crop in release builds.

**Interactions and validation:**
- Quantity must be numeric and greater than zero; validation copy is shown adjacent to the quantity field, not a system alert by default.
- Unit menu must support at least `g`, `kg`, `ml`, `L`, and `piece(s)` as relevant to the stored food item. Use the configured Units preference.
- Storage zone selection is mutually exclusive.
- Expiry date opens a native date picker styled consistently; retain the hand-drawn paper surface around it where possible.
- Save persists the ingredient locally, returns to Inventory, and updates the relevant count/expiry indicators. Provide visible inline validation for empty or invalid values. Never pretend it was saved when validation fails.
- Back returns to the originating screen and preserves unsaved changes only if the product’s existing editing convention does so.

### 04 — Inventory (`inventory`)

**Purpose:** view the stored ingredient collection and filter by location.

**Header:** **“Inventory”**, with a subtle plus action leading to Add Ingredient; system status bar above.

**Content order:**
1. Search field placeholder **“Search…”**.
2. Four filter chips: **All**, **Fridge**, **Pantry**, **Freezer**; **All** selected initially.
3. Scrollable list of six visible card rows. Each row contains a 48–54 pt ingredient thumbnail at left, title + metadata in the middle, expiry line beneath, and optional status pill + trailing chevron on the right.

**Reference content, in order:**
- **Tomatoes** — **“50 g · 5 · Fridge”** (keep source formatting close; in product data use correct quantity and container description), **“Exp: 2 days”**, badge **Soon**.
- **Eggs** — **“6 pcs · Fridge”**, **“Exp: 5 days”**.
- **Spinach** — **“2 × 9 g · Fridge”** (reference quantity is slightly unclear at this scale; use the project’s real stored quantity where present), **“Exp: 1 day”**, badge **Soon**.
- **Pasta** — **“50 g · Pantry”**, **“Exp: 6 months”**.
- **Olive Oil** — **“1 L · Pantry”**, **“Exp: 1 year”**.
- **Chicken Breast** — **“40 g · Fridge”**, **“Exp: 3 days”**, badge **Soon**.

Each row is about 66–72 pt tall. Use thin separators only inside rows where necessary; overall cards have their own soft outline. The first and second screen crops show the ingredient illustrations as small rounded squares, not large illustrations.

**Bottom bar:** Home / Inventory (active) / raised plus / Recipes / More.

**Interactions:** live search; mutually exclusive location filtering; tapping plus opens Add Ingredient; tapping a row opens that ingredient’s edit/detail state; state changes update sort/order and expiry labels. A filtered list with zero items must show a warm empty state and a clear “Clear filters” action, not a blank paper page.

### 05 — Recipe Suggestions (`suggestions`)

**Purpose:** suggest recipes using the actual kitchen inventory and expiry priorities.

**Header:** back arrow; centered **“Recipe Suggestions”**.

**Content order:**
1. Three pill filters: **For You** (selected), **By Ingredient**, **By Season**.
2. Line: **“Based on your kitchen”** at leading edge; trailing compact sort picker **“Sort: Best Match”**.
3. Three recipe cards, around 112–124 pt high, with a rounded illustrated-dish thumbnail at left and status/title/metadata to its right.
   - **Ready Now** — **Tomato Pasta** — **“15 min · 3 servings”** — **“All ingredients available”** (green small icon/text).
   - **Almost Ready** — **Chicken Stir-fry** — **“25 min · 2 servings”** — **“Missing: soy sauce (optional)”** (coral text).
   - **Smart Swap** — **Lentil Soup** — **“40 min · 4 servings”** — **“Swap: chicken → lentils”** (amber/brown helper text; Smart Swap pill is pale blue).
4. Bottom-anchored full-width green button with arrow treatment: **“View All Suggestions”**.

Do not force the bottom tabs onto this screen; the reference uses the call-to-action at the bottom.

**Interactions:** category tabs/sort actually change the result set/order. Each row opens the corresponding recipe. “View All Suggestions” opens Meal Suggestions. Missing ingredients must be labelled honestly; do not mark a recipe Ready Now when it requires a missing required ingredient.

### 06 — Tomato Pasta detail (`detail`)

**Purpose:** show a recipe and let the user start cooking.

**Layout:** no global bottom tabs. The top section is a full-width hero illustration, about 125–150 pt tall, showing a cute hand-drawn bowl of tomato pasta, with round paper buttons overlaid at left (back) and right (favorite/heart). Use the dedicated hand-drawn vector dish illustration in release builds.

Below the hero illustration:
1. Large title **“Tomato Pasta”**.
2. Metadata row: green **“Ready Now”** chip, **“15 min”**, and **“3 servings”**, each with small clock/portion icons and dot separators.
3. Section header **“Ingredients”**; tiny add/adjust affordance at trailing edge.
4. Seven quantity rows with a small illustrated ingredient icon, left ingredient name, and right-aligned quantity:
   - **Pasta** — **300 g**
   - **Tomatoes** — **400 g**
   - **Olive oil** — **30 ml**
   - **Garlic** — **2 cloves**
   - **Basil** — **10 g**
   - **Salt** — **1 g**
   - **Pepper** — **2 g**
5. Bottom-anchored green CTA **“Start Cooking”** with a small cooking/chef illustration.

Use row height around 36–40 pt, light paper dividers, readable right-aligned quantities. The screen should feel like a handwritten recipe card, not a standard shopping product detail page.

**Interactions:** back returns to suggestions or its actual originating page; favorite toggles state; ingredient quantities can link to scaling/editing; Start Cooking opens the Cooking flow. If recipe data changes via portion scaling, this page must show updated quantities/servings.

### 07 — Cooking (`cooking`)

**Purpose:** step-by-step guided cooking.

**Header:** back arrow and centered **“Cooking…”**.

**Content order:**
1. Small bordered recipe summary card with a mini recipe/instruction icon; **“Tomato Pasta”**; **“Step 2 of 7”**; trailing chevron.
2. Large landscape hand-drawn illustration of tomato pasta in a pan/pot, approximately 145–165 pt high at the baseline.
3. Step title **“2. Cook the pasta”**.
4. Instructions, preserving the reference wording: **“Bring a large pot of salted water to a boil. Add pasta and cook for 8–10 minutes (or according to package instructions).”**
5. Horizontal progress indicator; right-side countdown **“03:42 left”**.
6. Pale-green status card **“Scaled for 3 servings”** with check icon.
7. Two equal-width controls: **Back** outlined/paper and **Next** green. Green button contains a right arrow.

**Behaviour:** Next/Back changes step number, title, instructions, progress and active timer. A finished step must not continue displaying “Step 2 of 7”. Timer must count down only while active and should be pause/resume-able; handle foreground/background using a real date-based timer rather than decrementing a counter once per render. Do not start a countdown with invented values if the recipe has no timing data.

### 08 — Portion Scaling (`scaling`)

**Purpose:** make recipe quantities adjust to a selected serving count.

**Header:** back arrow; centered **“Portion Scaling”**.

**Content order:**
1. Mini recipe thumbnail and **“Tomato Pasta”** row with a trailing chevron.
2. Label **“Adjust servings”**.
3. Four equal selection pills/buttons: **1**, **2**, **3**, **4**; default **3** selected in green.
4. Label **“Adjusted Quantities”**.
5. Quantity list using small ingredient illustrations and right-aligned measurements:
   - Pasta — 300 g
   - Tomatoes — 400 g
   - Olive oil — 30 ml
   - Garlic — 2 cloves
   - Basil — 10 g
6. Bottom green CTA **“Update Recipe”**.

**Functional requirement:** amounts derive from the recipe’s base serving count and chosen multiplier. No hard-coded separate amounts per button unless the recipe includes discrete ingredient rules; round units sensibly and preserve units (`cloves`, `pieces`, grams, ml). After Update Recipe, reflect the selected serving count and recalculated quantities in Recipe Detail and Cooking. The visual selection state must update before Save/Update.

### 09 — Ingredient Swaps (`swaps`)

**Purpose:** provide deterministic, explainable ingredient substitutions.

**Header:** back arrow; centered **“Ingredient Swaps”**.

**Content order:**
1. Heading **“Try these swaps”**.
2. Source-ingredient card: lemon illustration, **“Lemon”**, smaller **“Can be swapped with:”**.
3. Three option cards with illustration, name, selection indicator:
   - **Lime** — selected on first load; pale-green card and green check indicator.
   - **Vinegar** — unselected.
   - **Orange** — unselected.
4. Explanation heading **“Why?”**.
5. Two short lines with check marks: **“Similar acidity and flavor profile.”** and **“Works in the same type of recipes.”**
6. Bottom full-width green CTA: **“Use Lime Instead”** (label must update when selection changes).

**Interactions:** one substitution selected at a time. Choosing a different option moves the green selection treatment and updates the CTA label. Confirm applies the swap only to the relevant recipe or shopping/ingredient view; do not silently delete the original ingredient globally. Explanation must change with the selected substitution and be based on a small built-in mapping, not a made-up AI response.

### 10 — Meal Suggestions (`meals`)

**Purpose:** browse the full set of suggested meals by readiness tier.

**Header:** back arrow; centered **“Meal Suggestions”**.

**Filters:**
- **Ready Now (2)** — selected initially.
- **Almost Ready (3)**.
- **Smart Swap (1)**.

Each filter is a compact pill. Counts must match the actual filtered content; they are not decorative constants if the inventory changes.

**List items, in order from the source screen:**
1. **Ready Now — Tomato Pasta** — **15 min · 3 servings** — **All ingredients available**.
2. **Ready Now — Chicken Stir-fry** — **25 min · 2 servings**.
3. **Almost Ready — Vegetable Curry** — **35 min · 3 servings** — **Missing: coconut milk (optional)**.
4. **Smart Swap — Lentil Soup** — **40 min · 4 servings** — **Swap: chicken → lentils**.

Cards use a larger landscape/square-ish dish thumbnail at left and a title, pill, time, serving count, and optional helper line at right. Around 118–130 pt high depending on helper copy. Do not squash the list into standard 60 pt settings-style rows. No bottom tabs in this source screen.

**Interactions:** selecting a filter changes items and selected pill. Card taps open Tomato Pasta or Lentil Soup detail. Optional ingredient deficits are explicitly marked and should not block “Ready Now” only when truly optional.

### 11 — Lentil Soup detail (`lentil`)

**Purpose:** display a smart-swap recipe with visible cooking steps.

**Header:** back arrow; centered **“Lentil Soup”**.

**Hero section:** landscape hand-drawn illustration of lentil soup in a bowl immediately below the titled header. Unlike the Tomato Pasta screen, the source shows a normal back arrow in the header and does not clearly show an overlaid favourite button on the hero. Keep the dish illustration wide with warm colors; one or two short colored hand-drawn rays may sit just outside its edge.

Below the hero:
1. **“Smart Swap”** badge in pale blue with small swap icon.
2. Metadata: **“40 min · 4 servings”** on the same compact status row.
4. Two-way segmented selector: **Ingredients** | **Steps**. **Steps** selected by default on this reference screen.
5. Four visible numbered steps, each with green numbered circle, title, small instruction, and trailing chevron:
   - **1 Prep vegetables** — **“Chop onion, carrot, celery.”**
   - **2 Sauté** — **“Cook in olive oil for 5 minutes.”**
   - **3 Add lentils & broth** — **“Simmer for 25 minutes.”**
   - **4 Season** — **“Add salt, pepper, herbs.”**
6. Bottom full-width CTA **“Start Cooking”**.

**Interactions:** Ingredients/Steps selector actually switches content. Step rows can expand for detail if the product architecture supports it. Start Cooking enters this recipe’s own cooking sequence (not Tomato Pasta). Favorite state is persistent and accessible.

### 12 — Expiration Priority (`expiry`)

**Purpose:** prioritise food that should be used first and encourage waste reduction.

**Header:** back arrow; centered **“Expiration Priority”**.

**Content order:**
1. Coral/red alert banner with warning triangle: **“3 items need to be used within 24–48 hours”**.
2. Three ingredient rows with image, title, expiry line and trailing checkbox:
   - **Spinach** — **“Expires in 1 day”**.
   - **Ground Beef** — **“Expires in 1 day”**.
   - **Mozzarella Cheese** — **“Expires in 2 days”**.
3. Warm pale-orange tip card: bulb icon, **“Tips”**, heart outline at trailing edge, copy **“Use these ingredients first to reduce food waste!”**

Use green/vegetable illustration for spinach, red/pink ingredient art for ground beef, pale dairy art for mozzarella. Rows are 66–72 pt; each checkbox is at least a 30 pt hit target even if the visible drawn box is smaller. No bottom tab bar in this reference screen.

**Interactions:** checked items show a clear selected state and remain locally persisted as “acknowledged/used” or a real inventory action depending on the product data model. Tapping a food row opens its detail/edit path. The alert count and time range must be derived from stored expiration dates and current local date; never hard-code “3” if the actual number changes. The heart toggles saved tips only if there is a tips/favorites feature; otherwise provide a no-op-free explanatory action.

### 13 — Settings (`settings`)

**Purpose:** minimal settings; emphasize offline use, simple units, and no subscription.

**Header:** gear icon at leading edge and centered **“Settings”**. Do not add profile/login/avatar controls absent from the reference.

**Four rows:**
1. **Storage Zones** — subtitle **“Pantry, Fridge, Freezer”** — icon like storage/calendar — trailing chevron.
2. **Units** — subtitle **“Grams, milliliters, pieces”** — unit/ruler icon — trailing chevron.
3. **Offline Mode** — subtitle **“Works without internet”** — offline/label icon — green switch, on by default in the screenshot.
4. **About** — subtitle **“Version 1.0.0”** — friendly info/person icon — trailing chevron.

Use about 66–72 pt row height, 30 pt icon container, title 14–15 pt and subtitle 11–12 pt. The paper row surface has a thin outline and modest corner radius. Bottom tab bar is present; **More** selected, with raised central Add.

**Interactions:** Storage Zones opens editable Pantry/Fridge/Freezer options; Units opens units preferences and immediately affects input/list formatting; Offline Mode toggles the real offline behaviour but must not mislead—the app is designed to work locally regardless of network availability, so this setting may be a user-facing explanation/feature flag, not a false network switch; About opens version/license information. Version must come from the built app metadata rather than hard-coded “1.0.0” after the first release.

---

## 8. Navigation and interaction contract

### 8.1 Supported screen flow

```text
Welcome ── Get Started ──> My Kitchen
My Kitchen ── Inventory tab/category ──> Inventory
My Kitchen ── central + ──> Add Ingredient ── Save ──> Inventory
My Kitchen ── expiry/attention cards ──> Expiration Priority
My Kitchen ── Recipes tab ──> Recipe Suggestions
Recipe Suggestions ── recipe card ──> Tomato Pasta detail / Lentil Soup detail
Recipe Suggestions ── View All Suggestions ──> Meal Suggestions
Tomato Pasta detail ── Start Cooking ──> Cooking
Lentil Soup detail ── Start Cooking ──> Lentil Soup cooking flow
Recipe Detail ── serving adjustment ──> Portion Scaling ── Update Recipe ──> Recipe Detail
Ingredient Swap suggestion ──> Ingredient Swaps ── Confirm ──> Updated recipe context
Settings/More ──> Settings
```

Back must return to the actual previous page where possible, not always a hard-coded screen if navigation can be reached from multiple contexts. Use a `NavigationStack` with typed routes or an equivalent deterministic navigation state. Tab navigation and full-screen recipe/cooking flows should not accidentally duplicate tabs in the stack.

### 8.2 Ingredient and expiry model

Keep stored data as typed fields rather than parsing display strings:

- Stable local ID.
- `name`, `category`, optional image/art asset key.
- `quantity` as numeric decimal plus `unit` enum.
- `storageZone` enum: `fridge`, `pantry`, `freezer`.
- Optional `expiryDate` as a date without a misleading timezone conversion.
- `notes` as optional text.
- Optional locally computed `lowStock`/`almostEmpty` thresholds based on product rules.

Expiry statuses should be computed from the current local date and date-only expiry value; do not compare arbitrary midnight timestamps in a way that changes status because of timezone offsets. If no expiry date exists, show no expiry warning rather than inventing an estimate.

### 8.3 Recipe model

Each recipe needs local structured data: stable ID, display name, illustration asset ID, base serving count, prep/cook/total time, ingredients (quantity + unit + optionality), step titles/instructions/timers, and supported substitutions. Availability tier must be computed against the inventory. Optional missing items are labelled `(optional)` and do not prevent Ready Now only when the recipe definition says they are optional.

Portion scaling should be a single reusable calculation function. For a base recipe with 3 servings, selecting 2 servings multiplies scalable quantities by `2/3`; display rounding rules must be defined per unit. Discrete ingredients such as cloves/eggs can use sensible partial/whole-unit rules, but rounding must be consistent and testable. Do not store a second, conflicting ingredient quantity list for each serving option.

### 8.4 Offline-first requirement

The screens repeatedly communicate a local/offline product. Recipe data, inventory, expiry calculation, swaps, and settings must not depend on a live API. Do not insert online images/recipe calls, cloud authentication, a subscription, ads, or paywalls as unstated dependencies. A future sync feature, if explicitly requested, must be additive and must not make core actions unavailable offline.

---

## 9. SwiftUI architecture guidance

Use small reusable views and make state/data logic testable. Suggested structure; adapt names to the existing project rather than duplicating an existing architecture:

```text
FoodSafeApp/
  App/
    FoodSafeApp.swift
    AppRouter.swift
  DesignSystem/
    FoodSafeColors.swift
    FoodSafeTypography.swift
    FoodSafeSpacing.swift
    PaperBackground.swift
    SketchCard.swift
    SketchTextField.swift
    SketchChip.swift
    PrimaryButton.swift
    BottomTabBar.swift
    HandDrawnIcon.swift
  Models/
    Ingredient.swift
    Recipe.swift
    RecipeIngredient.swift
    RecipeStep.swift
    StorageZone.swift
    MeasurementUnit.swift
    RecipeAvailability.swift
    ExpirationStatus.swift
  Data/
    LocalIngredientStore.swift
    RecipeCatalog.swift
    ExpiryCalculator.swift
    RecipeScaler.swift
    IngredientSwapCatalog.swift
  Features/
    Welcome/WelcomeView.swift
    Kitchen/KitchenView.swift
    Ingredient/AddIngredientView.swift
    Inventory/InventoryView.swift
    Recipes/RecipeSuggestionsView.swift
    Recipes/RecipeDetailView.swift
    Cooking/CookingView.swift
    Recipes/PortionScalingView.swift
    Recipes/IngredientSwapsView.swift
    Recipes/MealSuggestionsView.swift
    Expiration/ExpirationPriorityView.swift
    Settings/SettingsView.swift
  Assets.xcassets/
    Flat cream surface, wordmark, hand-drawn food illustrations, category icons
```

**Architecture rules:**
- Use `@State` for local view controls and a shared observable store for inventory/recipe preferences. Persist local data with the project’s existing store. If there is no data layer, pick one deployment-target-compatible local store and keep it isolated behind a protocol.
- `FoodSafeColors` is the single source of truth for every hex value; do not duplicate raw color literals throughout feature views.
- `FoodSafeTypography` maps semantic roles to the bundled custom fonts. Do not scatter `.font(.custom("…"))` literals.
- Hand-drawn art is custom vector/image assets in the asset catalogue. Emoji are acceptable only for a temporary prototype/debug state, never as release artwork.
- Use a reusable card/chip/input/button implementation. One-off styling drift between screens is a defect.
- The paper texture must not animate/repaint on every list update.
- Test availability, scaling, expiry, and substitution logic with deterministic unit tests separate from view code.
- Add VoiceOver labels to favorite, back, plus, date picker, zone selectors, checkbox rows and filter controls. A color change by itself is not a sufficient selection indicator; retain checkmarks/labels where appropriate.

### 9.1 Reusable semantic token sketch

Use a single mapping conceptually equivalent to:

```swift
enum FoodSafePalette {
    static let paperBase       = Color(hex: 0xF7EEDC)
    static let paperHighlight  = Color(hex: 0xFBF4E5)
    static let paperCard       = Color(hex: 0xFAF2E1)
    static let paperDeep       = Color(hex: 0xE8DCC5)
    static let inkPrimary      = Color(hex: 0x282E28)
    static let inkSecondary    = Color(hex: 0x6B604F)
    static let linePrimary     = Color(hex: 0x827460)
    static let lineSubtle      = Color(hex: 0xBFB19A)
    static let greenPrimary    = Color(hex: 0x527B5E)
    static let greenDeep       = Color(hex: 0x2E6A4F)
    static let greenLight      = Color(hex: 0xDCE4C4)
    static let peachSurface    = Color(hex: 0xF8DCC4)
    static let orangePrimary   = Color(hex: 0xE7A34D)
    static let orangeLight     = Color(hex: 0xFBE6C7)
    static let redPrimary      = Color(hex: 0xC96658)
    static let redLight        = Color(hex: 0xF8D8CB)
    static let bluePrimary     = Color(hex: 0x5B8DA5)
    static let blueLight       = Color(hex: 0xDAE9EC)
    static let lavenderLight   = Color(hex: 0xDFDAE9)
    static let yellowLight     = Color(hex: 0xF4CE83)
}
```

Treat the token hexes above as production tokens to use consistently. They are informed by image sampling but are not asserted to be the original app’s recovered vector values.

---

## 10. Visual QA and acceptance checklist

### 10.1 Required screenshot pass

For every native screen, capture at 390 × 844 points, same device scale, light appearance, and deterministic seeded test data. Compare with the relevant reference crop for relative alignment, content density, illustration shape, font size/weight, color family, and bottom spacing. Keep the source image’s frame perspective out of the native screenshot comparison.

Compare in this priority order:

1. **Screen structure:** same controls, same order, same visible content, same pinned/scrolling regions.
2. **Geometry:** header baseline, margins, card heights, row spacing, bottom CTA or tab location, image aspect ratio.
3. **Typography:** inspect the rendered bundled Purisa family at 100% zoom and verify its stroke thickness, line breaks, and title tilt. Every authored string must use Purisa Regular or Purisa Bold. Verify the runtime font-load audit and 400/700 weight contrast; any silent alternate-family fallback fails QA.
4. **Palette / surface:** use the tokens in §3. The approved current background is clean `paper.base` only. Heavy crease-photo texture and visible dotted/noise overlays fail QA for this revision.
5. **Art:** image subject/crop, line-art stroke weight, illustration palette and placement.
6. **Texture/detail:** paper grain, tiny stars, thin borders, subtle irregularities.

Pixel-by-pixel diff is meaningful only after there are clean, front-facing screen references at the same logical size. The provided collage has paper lighting, bevel/frame lines, perspective distortion and different source dimensions; a raw image diff against its outer screen crop would measure those mockup effects rather than native UI correctness. Do not report “100% pixel match” until equivalent native/reference images exist and a diff has been run.

### 10.2 Must-pass checks

- [ ] Each of the 13 screens renders without clipped or missing content.
- [ ] Typography is the bundled chosen typeface, not silently substituted.
- [ ] All colors are sourced through the semantic token file.
- [ ] Search, storage filters, recipe-tier filters, selection chips, favorite, checkbox, serving count, tabs, and Back/Next are functional.
- [ ] Save creates/updates a local ingredient; invalid quantity shows inline error.
- [ ] Expiration banner count changes when stored data changes; date-only comparisons are correct.
- [ ] Portion scaling recalculates quantities from a single recipe model and updates detail/cooking views.
- [ ] Recipe availability reflects all required/optional ingredients correctly.
- [ ] Ingredient swaps apply to the selected recipe context only.
- [ ] Cooking step navigation updates the step indicator, instruction and progress; timers use real elapsed time.
- [ ] App core features work with networking disabled.
- [ ] Bottom-anchored actions clear the iPhone home indicator and are never overlapped by the keyboard.
- [ ] VoiceOver labels and selected states are present; no essential status depends only on color.
- [ ] A 13-screen native screenshot contact sheet and a short residual-differences report are included with the next handoff.

### 10.3 Known limitations of this reference package

- The original image does not contain editable vector layers or uncompressed original assets.
- The original UI typeface cannot be proven from the raster. Purisa Regular/Bold is the current consistent offline implementation family; the wordmark remains source-derived artwork.
- The browser prototype now uses bundled SVG illustrations for food and dish imagery. The style must remain illustration-only across the native app; photographic substitutions are a design regression.
- The prototype was rendered at a 390 × 844 CSS viewport for all 13 screens; the latest automated report recorded zero JavaScript errors and zero failed images. This is **not** a native SwiftUI build and is not evidence of device-rendered pixel equality.
- The UI still differs from the source in the provable original font identity, illustration fidelity, exact crop quality, and some per-screen geometry/rotation. A successful render means only that the prototype loaded correctly, not that it is pixel-identical.
- The source’s hand-drawn strokes/lettering vary naturally. Do not attempt to match the JPEG’s paper lighting/phone bezels as application UI.

---

## 11. Browser prototype included with this specification

`prototype/index.html` is an interactive design-reference prototype with all 13 screen states. It is intentionally a visual review tool, not the shipping iOS runtime. Open it in a browser; use the left-hand screen selector on desktop or browse the screen on a narrow viewport. Cards/buttons route to related screens, filter pills change selection, serving-count controls recalculate displayed quantities, the swap selection changes the CTA, expiry checkboxes toggle, and the offline preference switches state.

The current 13-screen browser capture is `visual-qa/asset-integration-v1/contact-sheet.jpg`; per-screen full workspace and device captures are in the same folder. `test-report.json` records browser runtime status, font-loading results, image integrity, navigation, and style-switch checks. `home-style-ab-comparison.jpg` compares the sketch overlay and icon ink switches. These captures verify the current HTML demo, not a native SwiftUI screenshot or pixel-perfect equality. Continue with measured reference-crop comparisons and native simulator validation before claiming pixel accuracy.

---

## 12. Build order for the implementation agent

1. **Audit project state.** Preserve existing app structure and deployment target; locate data models, assets, and navigation before creating duplicates.
2. **Create the token/typography layer.** Validate one home screen against the prototype and source before implementing the remaining pages.
3. **Build reusable controls.** Card, primary button, chips, search, field/date/unit controls, status pills, ingredient rows, recipe rows, and tab bar must share the exact styles.
4. **Implement local models and derived logic.** Storage filters, expiry status, recipe availability, swaps, scaling, and cooking state.
5. **Build all 13 screens in screen-index order.** Use the exact text and default states in §7; no placeholder screens for visible features.
6. **Replace prototype placeholders with proper art assets.** Use vector illustrations for every food, ingredient, dish, icon, and decorative accent. Photography is prohibited.
7. **Visual QA in batches.** Capture first Welcome/Home/Add/Inventory; then Suggestions/Recipe Detail/Cooking/Scaling; then Swaps/Meal Suggestions/Lentil/Expiration/Settings. Review rendered outputs after each batch and fix the largest geometry mismatch before polishing texture.
8. **Accessibility and functional tests.** Validate type scaling, dynamic lists, keyboard, safe areas, offline operation, and derived-data correctness.
9. **Deliver source and evidence.** Include all source files, assets/license notices, screenshots for every screen, the contact sheet and explicit remaining known differences.

**Definition of done:** the app is interactive, local-first, visually coherent with the concept, and its rendering has been inspected. “Done” does not mean a screenshot was drawn once; it means each control has behaviour, the derived values are real, the assets are clean, and screenshots were captured and corrected in an iterative loop.


## 12. Latest iteration note (2026-10-25)

- Reverted the heavy creased-paper image and visible noise layer. Screen backgrounds are flat warm cream (`background-image: none`).
- Made Purisa Regular/Bold the only active type family across every authored string: headings, body, controls, input values, metadata, tabs, buttons, status simulation and generated checkmarks. Removed Comic Neue from the active prototype and eliminated explicit system-sans font declarations. Updated the CSS contract and typography audit to distinguish the chosen offline family from the unprovable original font binary.
- Replaced the typed welcome wordmark with the source-derived transparent FoodSafe wordmark asset.
- Replaced photo-based slots with original bundled SVG drawings. Food imagery is now explicitly illustration-only: cute, hand-drawn, colored-pencil/gouache style, no real-life pictures.
- Direct `file://` / localhost navigation was blocked earlier in the session, so current QA uses Playwright `page.set_content` with a self-contained HTML document and inlined local assets. This has now successfully rendered the latest 13-screen browser reference; native iOS Simulator QA remains outstanding.


## External asset research and implementation candidates

See [`ASSET-RESEARCH.md`](ASSET-RESEARCH.md) for the researched, license-aware shortlist of Drawably controls, Doodle Icons, Culinary Assets, Food Icon Pack and font candidates. Official external resources are candidates only until downloaded, licensed into the package, and visually checked against the original reference. The current Drawably-style controls and Doodle-style icons are local offline audition adapters and are not vendor packages. **Do not treat license availability as visual approval.**

Priority plan: (1) evaluate Drawably’s static seeded drawing mode for fields, controls and buttons; (2) map Doodle Icons SVGs for suitable interface symbols; (3) test Schoolbell, Patrick Hand, Kalam and the current local Purisa using one shared typography specimen; (4) fill missing ingredient-art gaps only with visually approved drawings. Keep all assets local at runtime.


### Latest asset-integration demo result

On 2026-10-25, the local self-contained HTML was rendered with Playwright/Chromium. Results: 13/13 screens captured, zero broken image loads, zero page-level JavaScript errors, Purisa Regular and Bold both loaded, Drawably-style sketch-control switch counts were 16 ON / 0 OFF / 16 ON after re-enable, SVG ink filter correctly switched on/off, and navigation click landed on Inventory. Evidence: `visual-qa/asset-integration-v1/test-report.json`, `contact-sheet.jpg`, `home-style-ab-comparison.jpg`, and per-screen PNGs.

The A/B panel uses local hand-authored adapters that emulate the intended *visual effect* of hand-sketched controls and inked SVG icons. It does **not** contain the upstream Drawably or Doodle Icons source packages; runtime network downloads were unavailable. Local FoodSafe food illustrations remain the project's visual source of truth. The current font is Purisa globally and is only a candidate match, not proof of the original source font.


## 13. External asset decisions based on visual inspection (2026-10-25)

This section supersedes any earlier suggestion to blindly fill FoodSafe with generic free assets. The mockup is the visual source of truth; every external item must pass a screenshot comparison at its intended size.

### Selected candidates by role

- **Whole dishes:** AnorelArts Watercolor Cooking Set — https://anorelarts.itch.io/watercolor-cooking-set . The listed full pack includes 35 dishes, 48 ingredients and 12 utensils; dish/ingredient objects are 500×500 px. The dish-only pack is https://anorelarts.itch.io/watercolor-cooking-set-food-pack-1 . Use only transparent dish objects, not the medieval background graphics. The creator permits personal/commercial use as stated on the listing; files are AI-assisted and edited. Candidate only until files and license are obtained.
- **Ingredient thumbnails:** The Rogue Cookie — https://theroguecookie.com/the-hand-drawn-low-fodmap-food-illustrations-set-for-creators/ . The published preview has the closest soft watercolor + thin irregular ink appearance found for vegetables and objects. 80+ transparent 2000×2000 PNGs, with many FoodSafe-specific ingredients. The commercial license price shown on the article is $34.99; confirm current license and final price. It is not a finished-dish pack, so it cannot fill all recipe hero images alone.
- **Buttons/fields/cards/toggles:** Drawably — https://github.com/danielwh2/drawably . MIT. Use fixed seed and `boil: 0`, tune roughness down, custom FoodSafe colors, semantic controls preserved.
- **UI symbols:** Doodle Icons — https://github.com/oreo-design/doodle-icons . MIT. Use static SVGs in `icons/` only. Recolor/scale after testing at 18–24 px; keep custom storage and food-category drawings wherever silhouette fidelity is higher.

### Explicit rejects

Do not use PictArts as primary dish art; its spaghetti preview has thick black contours and a large white halo, and its terms need caution for food assets central to an app. Do not use Culinary Assets wholesale; its coral/mint polish is too geometric. Do not use the 256×256 World Food Tour set for hero images unless visual and resolution tests pass; it is a cheap fallback only. Do not use Food Icon Pack Classic as hero art; it is mostly outline icons. None of the research preview images is itself an application asset.

### Visual audition

Open `visual-qa/external-asset-audition.html` while connected to the internet. It places the original mockup beside published previews from the candidate sources and records a subjective fit verdict. The audition board may load externally hosted preview images; the real app must not. Keep the offline rule: once a license is secured, download/commit individual assets locally, add attribution/license/source/hash metadata, and remove every remote asset URL from app code.

### Integration status honesty

External asset sources were opened and their public previews visually inspected. The container cannot resolve the external hosts for binary downloads, so no upstream food pack or upstream package code is claimed as installed. Existing local FoodSafe SVGs remain the shipped demo assets until an external pack is actually present locally. Do not call the external audition page a completed in-app integration.


## 14. Measurement-based reconstruction contract (normative)

**This section and its linked files supersede generic layout guesses in earlier sections wherever a coordinate, screen box, or rotation is specified.** The goal is to make the flattened reference reproducible by a second designer/agent without asking that person to guess every visual placement.

### 14.1 Authoritative artifacts

- [`reference/SCREEN-COORDINATE-MASTER.json`](reference/SCREEN-COORDINATE-MASTER.json) — single machine-readable source of truth: source-pixel quadrilateral corners for each screen, source-to-rectified homography matrices, all 13 pages, 289 named component/artwork elements plus 231 text-run records, `[x,y,w,h]` boxes, deterministic rotation degrees, font roles/sizes/colors, and notes.
- [`reference/SCREEN-MEASUREMENT-ATLAS.md`](reference/SCREEN-MEASUREMENT-ATLAS.md) — complete Markdown tables for every measured element, shared typography role sizes, surface dimensions, and native iOS mapping rules.
- [`reference/SCREEN-TEXT-COORDINATE-ATLAS.md`](reference/SCREEN-TEXT-COORDINATE-ATLAS.md) — every distinct visible text line with its own bounding box, role-based font size, color and rotation.
- [`reference/SCREEN-TEXT-RUNS.json`](reference/SCREEN-TEXT-RUNS.json) — machine-readable per-text-run coordinates, separate from parent button/card geometry.
- [`visual-qa/coordinate-audit/screen-geometry.json`](visual-qa/coordinate-audit/screen-geometry.json) — source-screen corners and homography transforms only.
- [`visual-qa/coordinate-audit/source-screen-quadrilaterals.jpg`](visual-qa/coordinate-audit/source-screen-quadrilaterals.jpg) — each crop polygon drawn over the original 1536×1024 collage.
- [`visual-qa/coordinate-audit/coordinate-grid-contact-sheet.jpg`](visual-qa/coordinate-audit/coordinate-grid-contact-sheet.jpg) — 50pt coordinate grid laid over all rectified screen references.
- [`visual-qa/coordinate-audit/element-box-overlays-contact-sheet.jpg`](visual-qa/coordinate-audit/element-box-overlays-contact-sheet.jpg) — named bounding-box overlay for every measured component; each numeric box label maps to `ELEMENT-OVERLAY-INDEX.md` and `overlay_index` in JSON.
- [`visual-qa/coordinate-audit/ELEMENT-OVERLAY-INDEX.md`](visual-qa/coordinate-audit/ELEMENT-OVERLAY-INDEX.md) — per-screen visual element ID legend and coordinate table.
- [`visual-qa/coordinate-audit/reference-vs-current-batch-1.jpg`](visual-qa/coordinate-audit/reference-vs-current-batch-1.jpg), [`reference-vs-current-batch-2.jpg`](visual-qa/coordinate-audit/reference-vs-current-batch-2.jpg) and [`reference-vs-current-batch-3.jpg`](visual-qa/coordinate-audit/reference-vs-current-batch-3.jpg) — rectified source shown next to the currently available HTML prototype captures.
- [`visual-qa/coordinate-audit/VISUAL-DISCREPANCY-AUDIT.md`](visual-qa/coordinate-audit/VISUAL-DISCREPANCY-AUDIT.md) — reviewed per-screen differences and an ordered corrective plan.

### 14.2 What the coordinates mean

1. The original board is 1536×1024 pixels. Each panel is a different quadrilateral due to perspective and the phone mockups' skew. Four manually measured corners (`TL, TR, BR, BL`) are transformed to a 390×844 reference canvas with a homography. This removes the board's perspective *for measurement only*.
2. Every element `bbox_pt = [x,y,w,h]` uses an origin at the top-left of that rectified 390×844 canvas. It is the full visible component box (including outline) or the visible text container—not the ink-only glyph silhouette. Angles are clockwise-positive; the text-wrapper angle is not the slope of each handwritten glyph.
3. Measured frame-edge corner uncertainty is about ±2–5 pixels in the original collage. After perspective correction, component bounds are conservatively treated as around ±6pt horizontal and ±7–8pt vertical. Small thumbnail and text-box placements can have greater relative uncertainty because the source panel itself is only ~200–240 pixels wide before enlargement.
4. These coordinates are an engineering approximation intended to make the next visual pass objective and repeatable. The source does not include editable text, original font names, vector shape paths, autolayout constraints, or native iOS view bounds, so exact source values cannot be asserted. On Settings, a yellow presentation sticky note physically obscures the lower-right part of the panel; do not interpret that note as UI. Use the Home screen bottom-tab arrangement as the corroborating reference for the hidden portion of Settings navigation.
5. Use SwiftUI stacks/grids and safe-area-aware layout for production; use the boxes as visual targets at 390×844, not a fragile pile of hardcoded frames for all devices. Use fixed frame/alignment where the source visibly requires it, such as thumbnail columns, amounts right-aligned, buttons full-width, and selected segments.
6. Do not transfer source phone-panel perspective to the actual app controls. Correct the phone/panel perspective first, then mimic only the subtle independent UI object rotations listed per element. The physical mockup border and surrounding presentation notes are not app content.

### 14.3 Text and rotation fidelity contract

- Use the exact source line breaks specified in the per-element data. Text content should not be rephrased to fit a layout; adjust the matching font size and width before changing the line breaks.
- All app-authored text shares `FoodSafe Hand`/Purisa Regular by default, including fields, values, metadata, tab labels, chips, alerts, status simulation, and every button. The source-derived wordmark is an image asset and is the exception.
- Font sizes are role-level visual estimates, not font metadata extracted from the JPEG. Use the JSON `font_size_pt` / shared style role and test against the rectified crop at native scale. For dense small metadata, stay inside the specified visual bbox and preserve legibility.
- Rotation values are deterministic target mimics. Apply them to visible text/artwork shells, not the tap area. Do not use random layout jitter; do not apply the phone's skew to the entire view tree.

### 14.4 Current visual mismatch is recorded, not hidden

The current captured browser prototype is functional and illustration-only, but the comparison audit shows it is **not yet a close geometric match**. Highest-impact differences include under-scaled welcome brand art, small category artwork and summary rows on My Kitchen, compressed suggestion/meal cards, hero art shown as an icon instead of filling the source hero rectangle, a cooking-pan visual that is too small, compressed portion rows, and under-sized settings/expiry controls. The exact target rectangles and priority corrections are written per screen in `visual-qa/coordinate-audit/VISUAL-DISCREPANCY-AUDIT.md`.

### 14.5 Corrective render loop required

For each iteration, implement the largest 3–5 geometry corrections from the discrepancy report, render all 13 at 390×844, regenerate side-by-side comparisons, and mark a mismatch closed only after visual inspection. The next pass should prioritize: (1) image/illustration footprint and correct composition, (2) vertical rhythm/card height, (3) title/body size and line wrapping, (4) button baseline/margins, (5) stroke and tilt detail. Do not optimize only the Home screen and assume the other screens inherit a match.


### Measured geometry pass (2026-10-25)

- Rectified all 13 screen panels from the original 1536×1024 board to independent 390×844 canvases using manually estimated quadrilaterals and homography transforms.
- Added 289 named component/artwork boxes and 231 separate text-line boxes with x/y/w/h, font role and size, color, and deterministic wrapper rotations. Added visual bounding-box overlays, 50pt coordinate grids, three batches of source-vs-current renders, and a per-screen discrepancy plan.
- Main target records: `reference/SCREEN-COORDINATE-MASTER.json`, `reference/SCREEN-MEASUREMENT-ATLAS.md`, and `reference/SCREEN-TEXT-COORDINATE-ATLAS.md`.
- Important status: coordinates are manually measured estimates with stated tolerances, not recovered Figma constraints. The captured current prototype remains visibly different from the source; the discrepancy report identifies the highest-impact corrections and should drive the next coding/render loop.
