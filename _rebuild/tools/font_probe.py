import sys, os, hashlib, json
from fontTools.ttLib import TTFont

D = sys.argv[1]
FILES = ["patrickhand__PatrickHand-Regular.ttf", "caveatbrush__CaveatBrush-Regular.ttf",
         "kalam__Kalam-Regular.ttf", "kalam__Kalam-Light.ttf", "kalam__Kalam-Bold.ttf"]
# characters the app may print (English only)
CHARS = {
 "ascii letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
 "digits": "0123456789",
 "punct": ".,:;!?'\"()[]{}/\\-_+=*&@#%$",
 "middot U+00B7": "·", "bullet U+2022": "•", "en dash U+2013": "–", "em dash U+2014": "—",
 "minus U+2212": "−", "times U+00D7": "×", "arrow right U+2192": "→", "ellipsis U+2026": "…",
 "curly quotes": "‘’“”", "degree U+00B0": "°", "check U+2713": "✓",
 "half U+00BD": "½", "quarter U+00BC": "¼", "3quarter U+00BE": "¾",
 "tilde U+007E": "~", "approx U+2248": "≈", "nbsp U+00A0": " ", "thin sp U+2009": " ",
 "euro U+20AC": "€", "pound U+00A3": "£", "e-acute U+00E9": "é", "n-tilde U+00F1": "ñ",
 "slash U+2044": "⁄", "super 2 U+00B2": "²", "plusminus U+00B1": "±", "less/greater": "<>",
 "heart U+2665": "♥", "star U+2605": "★", "warning U+26A0": "⚠",
}
out = {}
for fn in FILES:
    p = os.path.join(D, fn)
    raw = open(p, "rb").read()
    f = TTFont(p)
    nm = f["name"]
    def n(i):
        r = nm.getName(i, 3, 1, 0x409) or nm.getName(i, 1, 0, 0)
        return r.toUnicode() if r else None
    cmap = f.getBestCmap()
    os2 = f["OS/2"]; hhea = f["hhea"]; head = f["head"]
    gsub = f["GSUB"].table if "GSUB" in f else None
    feats = sorted({fr.FeatureTag for fr in gsub.FeatureList.FeatureRecord}) if gsub else []
    hm = f["hmtx"]
    digit_adv = {c: hm[cmap[ord(c)]][0] for c in "0123456789" if ord(c) in cmap}
    cov = {}
    for k, s in CHARS.items():
        miss = [c for c in s if ord(c) not in cmap]
        cov[k] = "OK" if not miss else "MISSING " + "".join(miss)
    info = dict(
        file=fn.split("__")[1], bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
        family=n(1), subfamily=n(2), full=n(4), version=n(5), postscript=n(6),
        typo_family=n(16), typo_sub=n(17), copyright=n(0), license_desc=(n(13) or "")[:90], license_url=n(14),
        weight_class=os2.usWeightClass, fsType=os2.fsType, fsSelection=bin(os2.fsSelection),
        upm=head.unitsPerEm, hhea_asc=hhea.ascent, hhea_desc=hhea.descent, hhea_gap=hhea.lineGap,
        typo_asc=os2.sTypoAscender, typo_desc=os2.sTypoDescender, typo_gap=os2.sTypoLineGap,
        win_asc=os2.usWinAscent, win_desc=os2.usWinDescent,
        xheight=getattr(os2, "sxHeight", None), capheight=getattr(os2, "sCapHeight", None),
        glyphs=len(f.getGlyphOrder()), cmap_entries=len(cmap), features=feats,
        digit_advances=digit_adv, tabular_digits=(len(set(digit_adv.values())) == 1),
        has_fvar=("fvar" in f), has_gdef="GDEF" in f, outlines=("glyf" if "glyf" in f else "CFF"),
        coverage=cov,
    )
    out[fn] = info
json.dump(out, open(os.path.join(D, "probe.json"), "w"), indent=1)
for fn, i in out.items():
    print("=====", fn)
    for k in ["family","subfamily","full","version","postscript","copyright","license_desc","license_url","weight_class","fsType","upm","hhea_asc","hhea_desc","hhea_gap","typo_asc","typo_desc","typo_gap","win_asc","win_desc","xheight","capheight","glyphs","cmap_entries","tabular_digits","has_fvar","outlines"]:
        print(f"  {k}: {i[k]}")
    print("  features:", " ".join(i["features"]))
    print("  digit advances:", i["digit_advances"])
    bad = {k: v for k, v in i["coverage"].items() if v != "OK"}
    print("  coverage gaps:", bad if bad else "none")
