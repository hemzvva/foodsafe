"""Port of the test app's SplitMix64 / SketchRect / SketchCircle / GlyphPen to Python, to SEE what the code draws.
Working tool (not part of the kit). Stdlib only.
Usage: python3 -I render_sketch_kit.py <path to 'import SwiftUI 2.txt'> <out.html>
"""
import math, re, sys, html
M = (1 << 64) - 1
class Rng:
    def __init__(self, seed): self.s = (seed * 0x9E3779B97F4A7C15 + 0x2545F491) & M
    def next(self):
        self.s = (self.s + 0x9E3779B97F4A7C15) & M
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & M
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & M
        return z ^ (z >> 31)
    def jitter(self): return ((self.next() >> 11) / float(1 << 53)) * 2 - 1

def fnv(text):
    h = 0xCBF29CE484222325
    for b in text.encode("utf-8"):
        h ^= b; h = (h * 0x100000001B3) & M
    return h

class P:  # path builder producing SVG path data
    def __init__(self): self.d = []; self.cur = (0.0, 0.0); self.idx = 0
    def M(self, x, y): self.d.append(f"M{x:.3f} {y:.3f}"); self.cur = (x, y)
    def Q(self, cx, cy, x, y): self.d.append(f"Q{cx:.3f} {cy:.3f} {x:.3f} {y:.3f}"); self.cur = (x, y)
    def C(self, a, b, c, d_, x, y): self.d.append(f"C{a:.3f} {b:.3f} {c:.3f} {d_:.3f} {x:.3f} {y:.3f}"); self.cur = (x, y)
    def Z(self): self.d.append("Z")
    def add(self, other): self.d.extend(other.d)
    def svg(self): return " ".join(self.d)

def sketch_rect(x0, y0, w, h, radius=16, seed=7, wobble=1.0):
    rng = Rng(seed)
    j = lambda s=1.0: rng.jitter() * wobble * s
    r = min(radius, w / 2, h / 2)
    x1, y1 = x0 + w, y0 + h
    midx, midy = x0 + w / 2, y0 + h / 2
    bowx, bowy = min(w * 0.02, 6.0), min(h * 0.02, 5.0)
    p = P()
    p.M(x0 + r, y0 + j(0.4))
    tx, ty = x1 - r, y0 + j(0.4); cx, cy = midx + j(bowx), y0 + j(1.1); p.Q(cx, cy, tx, ty)
    tx, ty = x1 + j(0.4), y0 + r; p.Q(x1, y0, tx, ty)
    tx, ty = x1 + j(0.4), y1 - r; cx, cy = x1 + j(1.1), midy + j(bowy); p.Q(cx, cy, tx, ty)
    tx, ty = x1 - r, y1 + j(0.4); p.Q(x1, y1, tx, ty)
    tx, ty = x0 + r, y1 + j(0.4); cx, cy = midx + j(bowx), y1 + j(1.1); p.Q(cx, cy, tx, ty)
    tx, ty = x0 + j(0.4), y1 - r; p.Q(x0, y1, tx, ty)
    tx, ty = x0 + j(0.4), y0 + r; cx, cy = x0 + j(1.1), midy + j(bowy); p.Q(cx, cy, tx, ty)
    p.Q(x0, y0, x0 + r, y0)
    p.Z()
    return p

def sketch_circle(cx0, cy0, rad, seed=3):
    rng = Rng(seed)
    pts = []
    for i in range(8):
        a = i / 8 * 2 * math.pi
        rr = rad * (1 + rng.jitter() * 0.025)
        pts.append((cx0 + math.cos(a) * rr, cy0 + math.sin(a) * rr))
    p = P(); p.M(*pts[0])
    for i in range(8):
        p0, p1, p2, p3 = pts[(i - 1) % 8], pts[i], pts[(i + 1) % 8], pts[(i + 2) % 8]
        p.C(p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6, p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6, p2[0], p2[1])
    p.Z()
    return p

class Pen:
    def __init__(self): self.p = P(); self.stroke = 0
    def m(self, x, y): self.p.M(x, y)
    def l(self, x, y):
        sx, sy = self.p.cur; dx, dy = x - sx, y - sy
        length = max(math.hypot(dx, dy), 0.001)
        self.stroke += 1
        bow = (1 if self.stroke % 2 == 0 else -1) * min(length * 0.025, 0.35)
        self.p.Q((sx + x) / 2 - dy / length * bow, (sy + y) / 2 + dx / length * bow, x, y)
    def q(self, cx, cy, x, y): self.p.Q(cx, cy, x, y)
    def c(self, a, b, c, d, x, y): self.p.C(a, b, c, d, x, y)
    def close(self): self.p.Z()
    def circle(self, cx, cy, r): self.p.add(sketch_circle(cx, cy, r, int(cx * 10 + cy)))
    def dot(self, cx, cy):
        r = 0.55
        self.p.M(cx - r, cy); self.p.Q(cx - r, cy - r, cx, cy - r); self.p.Q(cx + r, cy - r, cx + r, cy)
        self.p.Q(cx + r, cy + r, cx, cy + r); self.p.Q(cx - r, cy + r, cx - r, cy)
    def rect(self, x, y, w, h, r): self.p.add(sketch_rect(x, y, w, h, r, int(x * 7 + y * 3 + w), 0.14))

def parse_glyphs(src):
    body = src[src.index("func draw(_ p: inout GlyphPen)"):src.index("struct GlyphShape")]
    out = {}
    for m in re.finditer(r"case ((?:\.\w+(?:, )?)+):\n(.*?)(?=\n        case \.|\n        \}\n    \}\n\})", body, re.S):
        names = [n.strip()[1:] for n in m.group(1).split(",")]
        for n in names: out[n] = m.group(2)
    return out

def run_glyph(code):
    pen = Pen()
    if "for i in 0..<8" in code:   # gear: circles then spokes
        for part in code.split("\n"):
            part = part.strip()
            if part.startswith("p.circle"):
                for s in part.split(";"):
                    mm = re.match(r"\s*p\.circle\(([^)]*)\)", s); a = [float(v) for v in mm.group(1).split(",")]; pen.circle(*a)
        for i in range(8):
            a = i / 8 * 2 * math.pi
            pen.m(12 + math.cos(a) * 7, 12 + math.sin(a) * 7); pen.l(12 + math.cos(a) * 9.6, 12 + math.sin(a) * 9.6)
        return pen.p
    for line in code.split("\n"):
        for s in line.split(";"):
            s = s.strip()
            if not s: continue
            mm = re.match(r"p\.(\w+)\(([^)]*)\)", s)
            if not mm: raise SystemExit("cannot parse: " + s)
            name, args = mm.group(1), [float(v) for v in mm.group(2).split(",")] if mm.group(2).strip() else []
            getattr(pen, name)(*args)
    return pen.p

def main():
    src = open(sys.argv[1], encoding="utf-8").read()
    glyphs = parse_glyphs(src)
    order = re.findall(r"case ([a-z, A-Z]+)\n", src[src.index("enum Glyph"):src.index("var isFilled")])
    names = []
    for line in order:
        names += [n.strip() for n in line.split(",")]
    print(len(names), "glyph names;", len(glyphs), "parsed bodies")
    missing = [n for n in names if n not in glyphs]
    print("missing bodies:", missing)
    INK, GREEN = "#2C3830", "#3D6B4C"
    parts = ["<!doctype html><meta charset=utf-8><body style='margin:0;background:#F3ECDC;font:12px sans-serif;color:#2C3830'>"]
    parts.append("<h3 style='margin:10px'>Glyph set (46) at 22pt actual size (top strip), then at 64pt</h3>")
    def glyph_svg(n, size, color):
        p = run_glyph(glyphs[n]); d = p.svg()
        w1 = 1.8 / (size / 24.0) * (size / 22.0)  # 1.8pt at 22pt, in 24-grid units
        filled = n in ("heartFill", "play")
        inner = (f"<path d='{d}' fill='{color}'/>" if filled else
                 f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{w1*24/size:.3f}' stroke-linecap='round' stroke-linejoin='round'/>"
                 f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{w1*24/size*0.45:.3f}' stroke-linecap='round' stroke-linejoin='round' opacity='.35' transform='translate(0.6 0.48)'/>")
        return f"<svg width='{size}' height='{size}' viewBox='0 0 24 24'>{inner}</svg>"
    parts.append("<div style='display:flex;flex-wrap:wrap;gap:10px;padding:10px;background:#FBF7EE'>" + "".join(glyph_svg(n, 22, INK) for n in names) + "</div>")
    parts.append("<div style='display:flex;flex-wrap:wrap;gap:6px;padding:10px'>")
    for n in names:
        parts.append(f"<div style='width:84px;text-align:center;background:#FBF7EE;border-radius:8px;padding:6px 0'>{glyph_svg(n, 64, INK)}<div>{n}</div></div>")
    parts.append("</div>")
    # sketch shapes
    parts.append("<h3 style='margin:10px'>Sketch shapes: card, button (primary/secondary/quiet/danger), chips, toggle, segmented</h3>")
    def card(w, h, seed, fill="#FBF7EE", stroke="#3A4337", radius=16, lw=1.2):
        a = sketch_rect(2, 2, w - 4, h - 4, radius, seed).svg()
        b = sketch_rect(2, 2, w - 4, h - 4, radius, seed, 1.0).svg()
        c = sketch_rect(2, 2, w - 4, h - 4, radius, seed + 97, 1.6).svg()
        return (f"<path d='{a}' fill='{fill}'/><path d='{b}' fill='none' stroke='{stroke}' stroke-opacity='.55' stroke-width='{lw}'/>"
                f"<path d='{c}' fill='none' stroke='{stroke}' stroke-opacity='.16' stroke-width='{lw*0.7:.2f}'/>")
    svg = ["<svg width='760' height='520' style='background:#F3ECDC'>"]
    svg.append("<g transform='translate(10 10)'>" + card(340, 96, 1) + "<text x='16' y='40' font-family='Kalam, sans-serif' font-size='20' font-weight='700' fill='#2C3830'>Card seed 1</text></g>")
    svg.append("<g transform='translate(380 10)'>" + card(340, 96, 5) + "<text x='16' y='40' font-family='Kalam, sans-serif' font-size='20' font-weight='700' fill='#2C3830'>Card seed 5</text></g>")
    kinds = [("primary", "#3D6B4C", "#2F5A3D", "#FBF7EE"), ("secondary", "#DCE7D1", "#3D6B4C", "#3D6B4C"), ("quiet", "#FBF7EE", "#3A4337", "#2C3830"), ("danger", "#F7DBCE", "#C4523B", "#C4523B")]
    for i, (k, bg, bd, fg) in enumerate(kinds):
        x = 10 + (i % 2) * 370; y = 130 + (i // 2) * 66
        a = sketch_rect(x, y, 340, 50, 14, 11).svg(); b = sketch_rect(x, y, 340, 50, 14, 12, 1.3).svg()
        svg.append(f"<path d='{a}' fill='{bg}'/><path d='{b}' fill='none' stroke='{bd}' stroke-width='1.3' stroke-opacity='{1 if k=='primary' else .6}'/>"
                   f"<text x='{x+170}' y='{y+31}' text-anchor='middle' font-size='18' fill='{fg}' font-weight='700'>{k} button</text>")
    for i, (t, sel) in enumerate([("Fridge", True), ("Pantry", False), ("Freezer", False), ("Garlic", False)]):
        x = 10 + i * 120; y = 280; s = fnv(t)
        a = sketch_rect(x, y, 108, 42, 21, s & M).svg(); b = sketch_rect(x, y, 108, 42, 21, (s + 1) & M).svg()
        svg.append(f"<path d='{a}' fill='{'#3D6B4C' if sel else '#FBF7EE'}'/><path d='{b}' fill='none' stroke='{'#2F5A3D' if sel else '#3A4337'}' stroke-opacity='{1 if sel else .45}' stroke-width='1.2'/>"
                   f"<text x='{x+54}' y='{y+27}' text-anchor='middle' font-size='16' fill='{'#FBF7EE' if sel else '#2C3830'}' font-weight='700'>{t}</text>")
    # toggle on / off
    for i, on in enumerate([False, True]):
        x = 520 + i * 90; y = 284
        a = sketch_rect(x, y, 52, 30, 15, 21).svg(); b = sketch_rect(x, y, 52, 30, 15, 22).svg()
        kx = x + (26 if on else 4) + 11; ky = y + 15
        k = sketch_circle(kx, ky, 11, 9).svg()
        svg.append(f"<path d='{a}' fill='{'#3D6B4C' if on else '#EEE6D3'}'/><path d='{b}' fill='none' stroke='#3A4337' stroke-opacity='.5' stroke-width='1.2'/>"
                   f"<path d='{k}' fill='#FBF7EE' stroke='#3A4337' stroke-opacity='.5'/>")
    # segmented
    a = sketch_rect(10, 350, 340, 48, 14, 3).svg(); sel = sketch_rect(14 + 2, 354, 106, 40, 11, 4).svg(); selb = sketch_rect(16, 354, 106, 40, 11, 5).svg()
    svg.append(f"<path d='{a}' fill='#EEE6D3'/><path d='{sel}' fill='#FBF7EE'/><path d='{selb}' fill='none' stroke='#3A4337' stroke-opacity='.45'/>")
    for i, t in enumerate(["Today", "Week", "Month"]):
        svg.append(f"<text x='{10+4+57+i*113}' y='378' text-anchor='middle' font-size='17' font-weight='700' fill='{'#2C3830' if i==0 else '#6F6B5D'}'>{t}</text>")
    # big comparison of wobble: perfect rounded rect vs sketch
    svg.append("<rect x='380' y='350' width='160' height='60' rx='16' fill='#FBF7EE' stroke='#3A4337' stroke-opacity='.55' stroke-width='1.2'/><text x='392' y='430' font-size='12' fill='#6F6B5D'>plain rounded rect (reference)</text>")
    svg.append("<g transform='translate(560 348)'>" + card(160, 64, 1) + "</g><text x='572' y='430' font-size='12' fill='#6F6B5D'>sketch card (same size)</text>")
    svg.append("</svg>")
    parts.append("".join(svg))
    open(sys.argv[2], "w", encoding="utf-8").write("\n".join(parts))
main()
