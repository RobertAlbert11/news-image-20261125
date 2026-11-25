#!/usr/bin/env python3
"""Front page of THE WORLD — Wednesday, 25 November 2026.

Build-time generator: renders the dark broadsheet layout (1024x1024 PNG)
that ships in the repo as entry.png. Runs are deterministic: no randomness,
no timestamps, fixed font sizes and spacing everywhere.
"""
from PIL import Image, ImageDraw, ImageFont

S = 1024
INK = (16, 17, 20)        # page background
PAPER = (240, 237, 228)   # main headline colour
ASH = (156, 158, 166)     # secondary text
CARD = (26, 28, 35)       # story panels
RULE = (78, 80, 90)       # hairlines
RED = (226, 62, 52)       # masthead accent
AMBER = (216, 172, 70)
STEEL = (96, 140, 198)
JADE = (102, 178, 128)

FONT_DIR = '/usr/share/fonts/truetype/dejavu/'

def face(key, px):
    files = {
        'head': 'DejaVuSerifCondensed-Bold.ttf',
        'kick': 'DejaVuSansMono-Bold.ttf',
        'tick': 'DejaVuSansMono.ttf',
        'body': 'DejaVuSansCondensed-Bold.ttf',
    }
    return ImageFont.truetype(FONT_DIR + files[key], px)

page = Image.new('RGB', (S, S), INK)
brush = ImageDraw.Draw(page)

MARGIN = 44
EDGE = S - MARGIN

# ---------------------------------------------------------------- masthead
brush.rectangle([0, 0, S, 10], fill=RED)
brush.text((MARGIN, 30), 'THE WORLD', font=face('head', 62), fill=PAPER)
brush.text((MARGIN, 100), 'WEDNESDAY, NOVEMBER 25, 2026', font=face('tick', 20), fill=AMBER)
brush.text((MARGIN, 130), 'Every story that mattered, on a single sheet', font=face('body', 19), fill=ASH)
brush.line([MARGIN, 164, EDGE, 164], fill=RULE, width=2)

# ------------------------------------------------------- hero: space story
TOP, BOT = 188, 478
brush.rectangle([MARGIN, TOP, EDGE, BOT], fill=CARD)
brush.rectangle([MARGIN, TOP, MARGIN + 8, BOT], fill=RED)
brush.text((MARGIN + 26, TOP + 16), 'SPACE / BEIJING', font=face('tick', 18), fill=RED)
brush.text((MARGIN + 26, TOP + 46), 'CHINA FLIES ITS FIRST', font=face('head', 44), fill=PAPER)
brush.text((MARGIN + 26, TOP + 96), 'FOREIGN ASTRONAUT', font=face('head', 44), fill=PAPER)

hero_body = ("Shenzhou-24 is docked at Tiangong with Pakistan's Ali aboard — "
             "the first foreign national to live on the Chinese station.")
hx, hy = MARGIN + 26, TOP + 162
words = hero_body.split()
cursor = ''
row = 0
for w in words:
    trial = (cursor + ' ' + w).strip()
    if brush.textlength(trial, font=face('body', 24)) > (EDGE - hx - 380):
        brush.text((hx, hy + row * 34), cursor, font=face('body', 24), fill=(206, 208, 216))
        cursor, row = w, row + 1
    else:
        cursor = trial
brush.text((hx, hy + row * 34), cursor, font=face('body', 24), fill=(206, 208, 216))

# simple rocket illustration, right side of the hero panel
cx, cy = 850, 316
brush.polygon([(cx, cy - 88), (cx + 24, cy - 16), (cx - 24, cy - 16)], fill=(214, 218, 228))
brush.rectangle([cx - 24, cy - 16, cx + 24, cy + 58], fill=(214, 218, 228))
brush.polygon([(cx - 24, cy + 18), (cx - 48, cy + 66), (cx - 24, cy + 58)], fill=RED)
brush.polygon([(cx + 24, cy + 18), (cx + 48, cy + 66), (cx + 24, cy + 58)], fill=RED)
brush.ellipse([cx - 11, cy - 2, cx + 11, cy + 20], fill=STEEL)
brush.polygon([(cx - 13, cy + 60), (cx + 13, cy + 60), (cx, cy + 124)], fill=AMBER)
for sx, sy in [(770, 224), (912, 208), (952, 272), (788, 444), (930, 448)]:
    brush.ellipse([sx, sy, sx + 4, sy + 4], fill=ASH)

# ------------------------------------------------------------ story grid
cells = [
    ('WAR', RED, 'UKRAINE: 500,000 DEAD',
     "A leaked Russian tally exposes the war's true toll; Kyiv's bridges and power grid hit overnight."),
    ('COURT', STEEL, 'ICJ: MYANMAR GENOCIDE',
     'The World Court rules the campaign against the Rohingya amounted to genocide.'),
    ('CLIMATE', JADE, 'COP31 FALLS APART',
     'Talks end in acrimony at Antalya as the EU delegation walks out; pledges stall.'),
    ('COURT', STEEL, 'HUAWEI GUILTY IN US',
     'Convicted of sanctions breaches, bank fraud and stealing trade secrets.'),
    ('TECH', AMBER, 'TESLA-SPACEX PANELS',
     'Directors seated on five committees to weigh an all-stock combination.'),
    ('CULTURE', ASH, 'MISS UNIVERSE 2026',
     "Jennifer Barreto of Puerto Rico wins the pageant's 75th crown."),
]

GX, GY = 14, 14
CW, CH = (EDGE - MARGIN - GX) // 2, 146
gy0 = 502
for idx, (tag, hue, title, blurb) in enumerate(cells):
    col, row = idx % 2, idx // 2
    x = MARGIN + col * (CW + GX)
    y = gy0 + row * (CH + GY)
    brush.rectangle([x, y, x + CW, y + CH], fill=CARD)
    brush.rectangle([x, y, x + 7, y + CH], fill=hue)
    brush.text((x + 24, y + 14), tag, font=face('tick', 16), fill=hue)
    brush.text((x + 24, y + 40), title, font=face('head', 24), fill=PAPER)
    # wrap blurb to the card width, measured not guessed
    inner = CW - 48
    bx, by, line, n = x + 24, y + 76, '', 0
    for w in blurb.split():
        t = (line + ' ' + w).strip()
        if brush.textlength(t, font=face('body', 18)) > inner:
            brush.text((bx, by + n * 24), line, font=face('body', 18), fill=ASH)
            line, n = w, n + 1
    brush.text((bx, by + n * 24), line, font=face('body', 18), fill=ASH)

# --------------------------------------------------------- footer ticker
ty = gy0 + 3 * (CH + GY) + 10
brush.rectangle([MARGIN, ty, EDGE, ty + 64], fill=CARD)
brush.text((MARGIN + 18, ty + 10), 'WIRE', font=face('tick', 17), fill=AMBER)
brush.text((MARGIN + 104, ty + 9),
           'Mississippi plane crash · CIA open-source system breached ·',
           font=face('body', 18), fill=PAPER)
brush.text((MARGIN + 104, ty + 37),
           'Bangladesh garment wages +36% · US-Iran war funded through January',
           font=face('body', 18), fill=PAPER)
brush.line([MARGIN, ty + 76, EDGE, ty + 76], fill=RULE, width=2)
brush.text((MARGIN, ty + 86), 'THE WORLD — page one of one',
           font=face('tick', 15), fill=ASH)

page.save('/home/hermes2/makefun/news-image/repo/entry.png', 'PNG', optimize=True)
print('rendered', page.size)
