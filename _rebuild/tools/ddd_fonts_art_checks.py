"""Doubt checks for the fonts and the test-app art (working tool, not part of the kit).
Usage: python3 -I _rebuild/tools/ddd_fonts_art_checks.py <repo-root>
Reads fonts from FoodSafe-Build-Kit/assets/fonts and the test app from reference-attachments/test-for-foodsafe.
"""
import os, re, sys, ast
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

ROOT = sys.argv[1]
FONTS = os.path.join(ROOT, "FoodSafe-Build-Kit", "assets", "fonts")
APP = os.path.join(ROOT, "reference-attachments", "test-for-foodsafe")

print("== D-006 x-height and cap-height: declared (OS/2) vs measured from outlines")
for fn in ["PatrickHand-Regular", "CaveatBrush-Regular", "Kalam-Light", "Kalam-Regular", "Kalam-Bold"]:
    f = TTFont(os.path.join(FONTS, fn + ".ttf"))
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); os2 = f["OS/2"]
    def top(ch):
        bp = BoundsPen(gs); gs[cmap[ord(ch)]].draw(bp); return bp.bounds[3]
    meas_x = [top(c) for c in "xzvw"]      # flat-topped lowercase letters
    meas_h = [top(c) for c in "HEIT"]       # flat-topped capitals
    print(f"{fn:22s} x declared {os2.sxHeight:4d} measured {min(meas_x):4.0f}..{max(meas_x):4.0f} | cap declared {os2.sCapHeight:4d} measured {min(meas_h):4.0f}..{max(meas_h):4.0f} | fsSelection USE_TYPO_METRICS={(os2.fsSelection >> 7) & 1}")

print("\n== D-010 counts in the art script")
src = open(os.path.join(APP, "#!_usr_bin_env python3.txt"), encoding="utf-8").read()
tree = ast.parse(src)
sets = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ("INGREDIENTS", "CATEGORIES", "SPOTS", "DISHES", "TEXTURE"):
        sets[node.targets[0].id] = ast.literal_eval(node.value) if node.targets[0].id != "SPOTS" else {k: None for k in [e.value for e in node.value.keys]}
for k, v in sets.items():
    print(k, len(v))
tot_png = len(sets["INGREDIENTS"]) + len(sets["CATEGORIES"]) + len(sets["SPOTS"])
print("expected PNG cutouts:", tot_png, "| expected JPG:", len(sets["DISHES"]) + len(sets["TEXTURE"]))
files = os.listdir(APP)
print("actual PNG:", sum(f.endswith(".PNG") for f in files), "JPG:", sum(f.endswith(".JPG") for f in files))

print("\n== D-007 contrast (WCAG 2.x) for the test palette (light)")
def lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
def lum(h):
    r, g, b = (h >> 16) & 255, (h >> 8) & 255, h & 255
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
def cr(a, b):
    la, lb = lum(a), lum(b)
    if la < lb: la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)
pal = dict(paper=0xF3ECDC, card=0xFBF7EE, cardSunk=0xEEE6D3, ink=0x2C3830, inkSoft=0x6F6B5D, green=0x3D6B4C,
           greenDeep=0x2F5A3D, onGreen=0xFBF7EE, greenWash=0xDCE7D1, coral=0xC4523B, coralWash=0xF7DBCE,
           amber=0xA86D17, amberWash=0xF5E4C1, blue=0x4C6B83, blueWash=0xDCE5EA)
pairs = [("ink", "paper"), ("ink", "card"), ("inkSoft", "paper"), ("inkSoft", "card"), ("inkSoft", "cardSunk"),
         ("green", "card"), ("green", "greenWash"), ("onGreen", "green"), ("onGreen", "greenDeep"), ("coral", "card"),
         ("coral", "coralWash"), ("amber", "card"), ("amber", "amberWash"), ("blue", "card"), ("blue", "blueWash")]
for a, b in pairs:
    print(f"{a:9s} on {b:10s} {cr(pal[a], pal[b]):5.2f}:1")
