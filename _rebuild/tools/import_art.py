"""One-time import of the owner's test-zip art into the kit with stable ids (working tool, not part of the kit).
Usage: python3 -I import_art.py <repo-root>
Maps the zip's camera-style names (IMG_0478...) to ids by subject. The mapping was made by eye from contact
sheets and is checked again by `--sheet`, which writes labelled contact sheets for a second visual check.
"""
import hashlib, json, os, shutil, sys
from PIL import Image

ROOT = sys.argv[1]
SRC = os.path.join(ROOT, "reference-attachments", "test-for-foodsafe")
DST = os.path.join(ROOT, "FoodSafe-Build-Kit", "assets", "art")

DISH = {  # recipe id (kebab-case) -> source number
 478: "kale-chickpea-soup", 480: "broccoli-cheddar-soup", 481: "tofu-stir-fry", 482: "yogurt-parfait", 483: "caprese-toast",
 484: "garlic-shrimp-pasta", 485: "bean-quesadillas", 486: "potato-frittata", 487: "shakshuka", 488: "lemon-salmon",
 489: "minestrone", 490: "banana-oat-pancakes", 491: "omelette", 492: "beef-tacos", 493: "fried-rice", 494: "mushroom-risotto",
 495: "vegetable-curry", 496: "lentil-soup", 497: "spinach-egg-skillet", 498: "chickpea-salad", 499: "chicken-stir-fry", 569: "tomato-pasta",
}
SPOT = {500: "no-recipes", 501: "empty-kitchen", 502: "tips", 503: "bell", 504: "done", 570: "welcome"}
CAT = {505: "others", 506: "proteins", 507: "dairy", 508: "grains", 509: "fruits", 511: "vegetables"}
ING = {
 510: "feta", 512: "chili-flakes", 513: "jar", 514: "kale", 515: "tofu", 516: "avocado", 517: "shrimp", 518: "broccoli", 519: "cream",
 520: "cumin", 521: "sugar", 522: "black-beans", 523: "tortilla", 524: "salmon", 525: "mushroom", 526: "zucchini", 527: "honey",
 528: "oats", 529: "apple", 530: "banana", 531: "bread", 532: "cilantro", 533: "curry-paste", 534: "parsley", 535: "peas", 536: "ginger",
 537: "coconut-milk", 538: "yogurt", 539: "chickpeas", 540: "flour", 541: "potato", 542: "vinegar", 543: "orange", 544: "lime", 545: "lemon",
 546: "butter", 547: "cheddar", 548: "milk", 549: "soy-sauce", 550: "ground-beef", 551: "celery", 552: "bell-pepper", 553: "mozzarella",
 554: "broth", 555: "rice", 556: "lentils", 557: "carrot", 558: "onion", 559: "black-pepper", 560: "olive-oil", 561: "egg", 562: "basil",
 563: "spinach", 564: "chicken-breast", 565: "salt", 566: "pasta", 567: "garlic", 568: "tomato",
}
# subject lines copied from the generator script (the prompts the owner's platform used)
UNSURE = {"cilantro": "leaves resemble parsley; chosen by leaf shape (rounded lobes)", "parsley": "leaves resemble cilantro; chosen by leaf shape and twine tie",
          "apple": "identical subject to cat-fruits; the two apple files are interchangeable", "fruits": "identical subject to ing-apple; interchangeable"}

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

NORMALISE = {"honey", "spinach", "rice"}   # subject fills under 72% of the frame; the other 67 cutouts fill 75-89%
FILL = 0.893                                # the generator's own standard: 5.3% margin on the long side

def main_bbox(im):
    """Bounding box (full-res) of every connected mass holding at least 1% of the visible pixels; specks ignored."""
    a = im.getchannel("A"); w, h = a.size; s = 2
    a2 = a.resize((w // s, h // s)); px = a2.load(); W, H = a2.size
    seen = [[False] * W for _ in range(H)]; comps = []
    for y in range(H):
        for x in range(W):
            if px[x, y] > 40 and not seen[y][x]:
                st = [(x, y)]; seen[y][x] = True; n = 0; b = [x, y, x, y]
                while st:
                    cx, cy = st.pop(); n += 1
                    b = [min(b[0], cx), min(b[1], cy), max(b[2], cx), max(b[3], cy)]
                    for dx in (-2, -1, 0, 1, 2):
                        for dy in (-2, -1, 0, 1, 2):
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < W and 0 <= ny < H and not seen[ny][nx] and px[nx, ny] > 40:
                                seen[ny][nx] = True; st.append((nx, ny))
                comps.append((n, b))
    tot = sum(n for n, _ in comps); keep = [b for n, b in comps if n >= 0.01 * tot]
    return (min(b[0] for b in keep) * s, min(b[1] for b in keep) * s, (max(b[2] for b in keep) + 1) * s, (max(b[3] for b in keep) + 1) * s)

def refit(path):
    im = Image.open(path).convert("RGBA"); W = im.width
    x0, y0, x1, y1 = main_bbox(im); pad = int(0.02 * W)
    box = (max(0, x0 - pad), max(0, y0 - pad), min(W, x1 + pad), min(im.height, y1 + pad))
    crop = im.crop(box); scale = (FILL * W) / max(crop.width, crop.height)
    crop = crop.resize((round(crop.width * scale), round(crop.height * scale)), Image.LANCZOS)
    out = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    out.paste(crop, ((W - crop.width) // 2, (W - crop.height) // 2), crop)
    out.save(path, optimize=True)
    return round(scale, 2)
rows = []
def put(num, kind, ident, subdir, prefix, ext):
    src = os.path.join(SRC, f"IMG_0{num}.{ext.upper()}")
    name = f"{prefix}-{ident}.{ext}" if prefix else f"{ident}.{ext}"
    out_dir = os.path.join(DST, subdir); os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, name)
    shutil.copyfile(src, out)
    note = None
    if kind == "ingredient" and ident in NORMALISE:
        k = refit(out)
        note = f"subject re-fitted to the standard 89% frame (x{k} Lanczos); regenerating this art at higher resolution is preferred"
    im = Image.open(out)
    row = dict(kind=kind, id=ident, file=f"{subdir}/{name}", source=f"IMG_0{num}.{ext.upper()}", width=im.width, height=im.height,
               mode=im.mode, bytes=os.path.getsize(out), sha256=sha(out))
    if ident in UNSURE: row["mapping_note"] = UNSURE[ident]
    if note: row["processing_note"] = note
    rows.append(row)

for n, i in sorted(DISH.items()): put(n, "dish", i, "dishes", "dish", "jpg")
for n, i in sorted(ING.items()): put(n, "ingredient", i, "ingredients", "ing", "png")
for n, i in sorted(CAT.items()): put(n, "category", i, "categories", "cat", "png")
for n, i in sorted(SPOT.items()): put(n, "spot", i, "spots", "spot", "png")
put(479, "texture", "paper", "texture", "", "jpg")
assert len(rows) == 93 and len({r["file"] for r in rows}) == 93
json.dump(dict(schema=1, count=len(rows), items=rows), open(os.path.join(DST, "art-manifest.json"), "w"), indent=1)
print("wrote", len(rows), "items;", sum(r["bytes"] for r in rows) // 1024, "KB")
