import sys, os
from PIL import Image, ImageDraw, ImageFont
D = sys.argv[1]; OUT = sys.argv[2]
F = {
 "PatrickHand": "patrickhand__PatrickHand-Regular.ttf",
 "CaveatBrush": "caveatbrush__CaveatBrush-Regular.ttf",
 "KalamLight": "kalam__Kalam-Light.ttf",
 "KalamRegular": "kalam__Kalam-Regular.ttf",
 "KalamBold": "kalam__Kalam-Bold.ttf",
}
PAPER = (243, 236, 220); INK = (44, 56, 48); SOFT = (111, 107, 93)
S = 2  # render at 2x like a retina screen
W = 780 * S
lines = [
 ("title", "Garlic Pasta"), ("big", "3 days left"), ("qty", "250 g  ·  1½ cups  ·  0.7 pcs"),
 ("body", "Boil the pasta until it just has a bite, then toss it in the garlic oil."),
 ("small", "Use soon: spinach, 2 eggs · Expires 18 Apr · 00:09:30"),
]
sizes = {"title": 30, "big": 40, "qty": 20, "body": 20, "small": 14}
# one block per font
blocks = []
H = 0
for name, fn in F.items():
    H += 30 * S + sum(int(sizes[k] * 1.55 * S) for k, _ in lines) + 24 * S
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
y = 8 * S
lab = ImageFont.truetype(os.path.join(D, F["PatrickHand"]), 13 * S)
for name, fn in F.items():
    d.text((12 * S, y), name, font=lab, fill=SOFT)
    y += 22 * S
    for k, t in lines:
        f = ImageFont.truetype(os.path.join(D, fn), sizes[k] * S)
        d.text((12 * S, y), t, font=f, fill=INK)
        y += int(sizes[k] * 1.55 * S)
    y += 10 * S
    d.line([(12 * S, y - 6 * S), (W - 12 * S, y - 6 * S)], fill=(200, 190, 170), width=S)
img.save(OUT)
print(img.size)
