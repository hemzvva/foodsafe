"""Builds FoodSafe-Build-Kit/assets/fonts/fonts-manifest.json from the font files (working tool; the output ships in the kit).
Usage: python3 -I make_fonts_manifest.py <repo-root>
Every number is read from the font files themselves; nothing is typed by hand except the source facts at the top.
"""
import hashlib, json, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

ROOT = sys.argv[1]
D = os.path.join(ROOT, "FoodSafe-Build-Kit", "assets", "fonts")
SOURCE = dict(
    repository="https://github.com/google/fonts", paths=["ofl/patrickhand", "ofl/caveatbrush", "ofl/kalam"],
    commit_read_after_download="5026800714d07231937d92eb4cceabf06e05d74e", downloaded="2026-11-27",
    note="Downloaded from raw.githubusercontent.com (branch main); the commit was read right after. The sha256 of each file is the authoritative identity.")
FILES = [
 ("PatrickHand-Regular.ttf", "licenses/PatrickHand-OFL.txt"), ("CaveatBrush-Regular.ttf", "licenses/CaveatBrush-OFL.txt"),
 ("Kalam-Light.ttf", "licenses/Kalam-OFL.txt"), ("Kalam-Regular.ttf", "licenses/Kalam-OFL.txt"), ("Kalam-Bold.ttf", "licenses/Kalam-OFL.txt"),
]
def ranges(cps):
    cps = sorted(cps); out = []; s = p = None
    for c in cps:
        if s is None: s = p = c
        elif c == p + 1: p = c
        else: out.append((s, p)); s = p = c
    if s is not None: out.append((s, p))
    return [f"U+{a:04X}" if a == b else f"U+{a:04X}-{b:04X}" for a, b in out]

fonts, cmaps = [], []
for fn, lic in FILES:
    path = os.path.join(D, fn); raw = open(path, "rb").read(); f = TTFont(path)
    nm = f["name"]; g = lambda i: nm.getName(i, 3, 1, 0x409).toUnicode()
    cmap = f.getBestCmap(); cmaps.append(set(cmap)); gs = f.getGlyphSet(); hm = f["hmtx"]; os2 = f["OS/2"]; hh = f["hhea"]
    def top(ch):
        bp = BoundsPen(gs); gs[cmap[ord(ch)]].draw(bp); return bp.bounds[3]
    adv = {c: hm[cmap[ord(c)]][0] for c in "0123456789:. ·"}
    upm = f["head"].unitsPerEm
    fonts.append(dict(
        file=fn, postscript_name=g(6), family=g(1), style=g(2), full_name=g(4), weight_class=os2.usWeightClass,
        bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(), version=g(5).split(";")[0], copyright=g(0),
        license="SIL Open Font License 1.1", license_file=lic, embedding_fsType=os2.fsType, units_per_em=upm,
        line_height_em=round((hh.ascent - hh.descent + hh.lineGap) / upm, 3), ascent=hh.ascent, descent=hh.descent, line_gap=hh.lineGap,
        x_height_measured=round(sum(top(c) for c in "xzvw") / 4), cap_height_measured=round(sum(top(c) for c in "HEIT") / 4),
        x_height_declared=os2.sxHeight, cap_height_declared=os2.sCapHeight,
        digits_proportional=len({adv[c] for c in "0123456789"}) > 1, digit_advance_max=max(adv[c] for c in "0123456789"),
        digit_advance_min=min(adv[c] for c in "0123456789"), colon_advance=adv[":"], space_advance=adv[" "], middot_advance=adv["·"],
        opentype_features=sorted({fr.FeatureTag for fr in f["GSUB"].table.FeatureList.FeatureRecord}),
        glyphs=len(f.getGlyphOrder())))
common = set.intersection(*cmaps)
text_common = sorted(c for c in common if c >= 0x20 and c not in range(0x7F, 0xA0) and (c < 0x900 or 0x2000 <= c <= 0x2BFF or 0xFB00 <= c <= 0xFB06))
missing_wanted = {"U+2192 RIGHTWARDS ARROW": 0x2192, "U+2713 CHECK MARK": 0x2713, "U+2605 BLACK STAR": 0x2605, "U+26A0 WARNING SIGN": 0x26A0,
                  "U+2009 THIN SPACE": 0x2009, "U+202F NARROW NO-BREAK SPACE": 0x202F, "U+2665 BLACK HEART SUIT": 0x2665}
gaps = {k: [ft["file"] for ft, cm in zip(fonts, cmaps) if v not in cm] for k, v in missing_wanted.items()}
out = dict(schema=1, source=SOURCE, fonts=fonts,
           font_safe_characters=dict(meaning="code points present in all five fonts (Latin text and common punctuation only)", ranges=ranges(text_common), count=len(text_common)),
           characters_missing_somewhere=gaps)
json.dump(out, open(os.path.join(D, "fonts-manifest.json"), "w"), indent=1, ensure_ascii=False)
print("fonts", len(fonts), "| font-safe code points", len(text_common))
print(" ".join(ranges(text_common)))
for k, v in gaps.items(): print(k, "missing in", len(v), "of 5:", ", ".join(x.replace(".ttf", "") for x in v) if v else "-")
for ft in fonts: print(f"{ft['postscript_name']:22s} lineH {ft['line_height_em']:.3f} x {ft['x_height_measured']} cap {ft['cap_height_measured']} digits {ft['digit_advance_min']}..{ft['digit_advance_max']} colon {ft['colon_advance']} space {ft['space_advance']}")
