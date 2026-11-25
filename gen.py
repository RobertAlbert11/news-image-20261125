#!/usr/bin/env python3
"""Generate the 2026-11-25 world news front page (1024x1024, deterministic)."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (14, 16, 22)
FG = (238, 238, 232)
MUT = (150, 155, 165)
ACC = (232, 76, 61)      # editorial red
GOLD = (214, 168, 62)
BLUE = (86, 130, 190)
GREEN = (94, 168, 120)

def F(name, size):
    p = {
        'serif': '/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf',
        'sans': '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf',
        'mono': '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
    }[name]
    return ImageFont.truetype(p, size)

img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)

# ---- masthead
d.rectangle([0, 0, W, 8], fill=ACC)
d.text((40, 26), "THE WORLD", font=F('serif', 58), fill=FG)
d.text((40, 92), "WEDNESDAY · NOVEMBER 25 · 2026", font=F('mono', 21), fill=GOLD)
d.text((40, 122), "One day, one page — the planet in nine stories", font=F('sans', 20), fill=MUT)
d.line([40, 156, W - 40, 156], fill=(70, 74, 84), width=2)

# ---- hero: China's first foreign astronaut
d.rectangle([40, 180, W - 40, 470], fill=(22, 27, 38))
d.rectangle([40, 180, 48, 470], fill=ACC)
d.text((66, 198), "SPACE", font=F('mono', 19), fill=ACC)
d.text((66, 226), "CHINA LAUNCHES FIRST", font=F('serif', 46), fill=FG)
d.text((66, 278), "FOREIGN ASTRONAUT", font=F('serif', 46), fill=FG)
# rocket
rx, ry = 830, 250
d.polygon([(rx, ry - 90), (rx + 26, ry - 20), (rx - 26, ry - 20)], fill=(210, 214, 224))
d.rectangle([rx - 26, ry - 20, rx + 26, ry + 60], fill=(210, 214, 224))
d.polygon([(rx - 26, ry + 20), (rx - 52, ry + 70), (rx - 26, ry + 60)], fill=ACC)
d.polygon([(rx + 26, ry + 20), (rx + 52, ry + 70), (rx + 26, ry + 60)], fill=ACC)
d.ellipse([rx - 12, ry - 4, rx + 12, ry + 20], fill=BLUE)
flame = [(rx - 14, ry + 62), (rx + 14, ry + 62), (rx, ry + 130)]
d.polygon(flame, fill=GOLD)
# stars
for sx, sy in [(760, 210), (920, 200), (950, 260), (770, 430), (930, 430), (860, 195)]:
    d.ellipse([sx, sy, sx + 4, sy + 4], fill=MUT)
d.text((66, 350), "Shenzhou-24 docks for Tiangong: Pakistan's", font=F('sans', 25), fill=(200, 205, 214))
d.text((66, 382), "Ali becomes the first foreign national on a", font=F('sans', 25), fill=(200, 205, 214))
d.text((66, 414), "Chinese space station.", font=F('sans', 25), fill=(200, 205, 214))

# ---- story grid
stories = [
    ("WAR", ACC, "UKRAINE: 500,000 DEAD",
     "Leaked Russian figures reveal the war's true cost; Kyiv bridges and grid struck overnight."),
    ("COURT", BLUE, "MYANMAR: GENOCIDE RULED",
     "The ICJ rules Myanmar committed genocide against the Rohingya — a landmark verdict."),
    ("CLIMATE", GREEN, "COP31 TALKS COLLAPSE",
     "EU walks out at Antalya; no deal, emissions pledges in tatters."),
    ("COURT", BLUE, "HUAWEI CONVICTED IN US",
     "Jury finds sanctions violations, bank fraud and theft of trade secrets."),
    ("TECH", GOLD, "TESLA × SPACEX MERGER?",
     "Five directors named to negotiate a possible all-stock combination."),
    ("LIFE", MUT, "MISS UNIVERSE 2026",
     "Puerto Rico's Jennifer Barreto takes the crown in the pageant's 75th edition."),
]

x0, y0 = 40, 494
cw, ch = 455, 148
gx, gy = 14, 14
for i, (tag, col, head, body) in enumerate(stories):
    r, c = divmod(i, 2)
    x = x0 + c * (cw + gx)
    y = y0 + r * (ch + gy)
    d.rectangle([x, y, x + cw, y + ch], fill=(22, 27, 38))
    d.rectangle([x, y, x + 6, y + ch], fill=col)
    d.text((x + 22, y + 12), tag, font=F('mono', 16), fill=col)
    d.text((x + 22, y + 36), head, font=F('serif', 25), fill=FG)
    words, line, lines = body.split(), '', []
    for w_ in words:
        t = (line + ' ' + w_).strip()
        if d.textlength(t, font=F('sans', 17)) > cw - 40:
            lines.append(line); line = w_
        else:
            line = t
    lines.append(line)
    for j, ln in enumerate(lines[:3]):
        d.text((x + 22, y + 72 + j * 23), ln, font=F('sans', 17), fill=MUT)

# ---- footer ticker
fy = y0 + 3 * (ch + gy) + 6
d.rectangle([40, fy, W - 40, fy + 66], fill=(22, 27, 38))
d.text((60, fy + 10), "ALSO:", font=F('mono', 17), fill=GOLD)
d.text((130, fy + 10), "Mississippi plane crash · CIA open-source system breached ·", font=F('sans', 18), fill=FG)
d.text((130, fy + 38), "Bangladesh garment wages +36% · US-Iran war funded to January", font=F('sans', 18), fill=FG)
d.line([40, fy + 78, W - 40, fy + 78], fill=(70, 74, 84), width=2)

img.save('/home/hermes2/makefun/news-image/repo/entry.png', 'PNG', optimize=True)
print('written', img.size)
