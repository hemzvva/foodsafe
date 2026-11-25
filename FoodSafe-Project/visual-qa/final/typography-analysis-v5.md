# FoodSafe Typography Analysis — v5

## What is visible in the supplied reference

- The app text is hand-printed rather than calligraphic: letters are mostly upright, disconnected, and irregular; it is not a brush script or a handwriting-only display header.
- Letterforms are rounded and informal, with mild baseline/angle variation and moderately tight spacing. The text is legible at small sizes, including inventory metadata and tab captions.
- The font family is consistent across page titles, item names, field labels, typed values, chips, statuses, cooking steps, helper text, quantities, and all button labels. Size/color/weight vary by role; font family does not.
- The welcome logo is a separate brush-lettered illustration and is not a valid font specimen for all UI text.
- The phone OS status icons in a real iOS app are OS-owned; the web reference's simulated 9:41 should use the UI family for consistency.

## Candidate conclusion

Purisa Regular remains the best of the local, offline fonts currently packaged for matching this particular informal hand-printed appearance. Purisa Bold is the paired emphasis face, but bold should be used sparingly, when the source visibly gives a word more ink. Comic Neue is more regularized and comic-like; it is less irregular than the source. Purisa Oblique makes the entire line slant and therefore is not the default; only use the regular upright face as the global UI family.

This is a visual similarity judgment, not proof that Purisa was the original source font. The flattened mockup does not expose its editable text layer or embedded font metadata.

## Requirement going forward

Apply `FoodSafe Hand` to every app-authored text element at every hierarchy level, including tiny metadata, numerical amounts, placeholder/help text, chips, pills, navigation tabs, button labels, form fields, errors, settings, status mock text, and prototype shell labels. Use a single family; vary only the source-supported size, ink color, and occasional weight. No SF/Arial/Roboto/system/sans font exceptions. The FoodSafe wordmark is the sole text-shaped artwork exception; illustrative doodles can contain drawn strokes rather than live text.
