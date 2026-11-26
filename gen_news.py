#!/usr/bin/env python3
"""Front page of THE WORLD — Wednesday, 25 November 2026.

Build-time generator: renders the dark broadsheet layout (1024x1024 PNG)
that ships in the repo as entry.png. Deterministic: no randomness, no
timestamps, fixed font sizes and spacing.
"""
from PIL import Image, ImageDraw, ImageFont

S = 1024
INK = (12, 13, 16)         # page background
PAPER = (243, 240, 231)    # headline colour
BRIGHT = (255, 255, 255)   # hero headline
ASH = (160, 162, 170)      # secondary text
CARD = (24, 26, 33)        # story panels
RULE = (86, 88, 98)        # hairlines
RED = (232, 58, 48)        # masthead accent
AMBER = (222, 176, 72)
STEEL = (104, 148, 205)
JADE = (110, 186, 136)

FONT_DIR = '/usr/share/fonts/truetype/dejavu/'

def face(key, px):
    files = {
        'head': 'DejaVuSerifCondensed-Bold.ttf',
        'kick': 'DejaVuSansMono-Bold.ttf',
        'tick': 'DejaVuSansMono.ttf',
        'body': 'DejaVuSansCondensed-Bold.ttf',
        'serif': 'DejaVuSerifCondensed.ttf',
    }
    return ImageFont.truetype(FONT_DIR + files[key], px)

page = Image.new('RGB', (S, S), INK)
brush = ImageDraw.Draw(page)

MARGIN = 40
EDGE = S - MARGIN

def wrap(text, font, width):
    lines, line = [], ''
    for w in text.split():
        t = (line + ' ' + w).strip()
        if brush.textlength(t, font=font) > width and line:
            lines.append(line)
            line = w
        else:
            line = t
    if line:
        lines.append(line)
    return lines

def draw_lines(x, y, lines, font, fill, lh):
    for i, ln in enumerate(lines):
        brush.text((x, y + i * lh), ln, font=font, fill=fill)
    return y + len(lines) * lh

# ---------------------------------------------------------------- masthead
brush.rectangle([0, 0, S, 12], fill=RED)
# folio row above masthead
brush.text((MARGIN, 24), 'VOL. CXII · NO. 47', font=face('tick', 15), fill=ASH)
brush.text((EDGE - 210, 24), 'LATE CITY EDITION', font=face('tick', 15), fill=ASH)
brush.text(((S - brush.textlength('$1.50', font=face('tick', 15))) / 2, 24),
           '$1.50', font=face('tick', 15), fill=ASH)
brush.text(((S - brush.textlength('THE WORLD', font=face('head', 88))) / 2, 44),
           'THE WORLD', font=face('head', 88), fill=PAPER)
brush.text(((S - brush.textlength('EVERY STORY THAT MATTERED, ON A SINGLE SHEET', font=face('tick', 16))) / 2, 146),
           'EVERY STORY THAT MATTERED, ON A SINGLE SHEET', font=face('tick', 16), fill=AMBER)
brush.line([MARGIN, 176, EDGE, 176], fill=PAPER, width=3)
brush.line([MARGIN, 181, EDGE, 181], fill=RULE, width=1)

# ------------------------------------------------------- hero: space story
TOP, BOT = 202, 500
brush.rectangle([MARGIN, TOP, EDGE, BOT], fill=CARD)
brush.rectangle([MARGIN, TOP, MARGIN + 9, BOT], fill=RED)
hx = MARGIN + 30
brush.text((hx, TOP + 18), 'SPACE · BEIJING · PAGE A1', font=face('kick', 17), fill=RED)
brush.text((hx, TOP + 44), 'BY OUR SPACE CORRESPONDENT', font=face('tick', 14), fill=ASH)
brush.text((hx, TOP + 72), 'CHINA FLIES ITS', font=face('head', 54), fill=BRIGHT)
brush.text((hx, TOP + 132), 'FIRST FOREIGN', font=face('head', 54), fill=BRIGHT)
brush.text((hx, TOP + 192), 'ASTRONAUT', font=face('head', 54), fill=BRIGHT)
hero_body = ("Shenzhou-24 is docked at Tiangong with Pakistan's Ali aboard — "
             "the first foreign national to live on the Chinese station, "
             "crowned by a state broadcast watched by 900 million.")
draw_lines(hx, TOP + 252, wrap(hero_body, face('body', 21), EDGE - hx - 420),
           face('body', 21), (208, 210, 218), 29)
# dateline chip at hero bottom
brush.text((hx, BOT - 26), 'BEIJING, TUESDAY NIGHT —', font=face('tick', 14), fill=AMBER)

# simple rocket illustration, right side of the hero panel
cx, cy = 862, 330
brush.polygon([(cx, cy - 96), (cx + 26, cy - 14), (cx - 26, cy - 14)], fill=(220, 224, 232))
brush.rectangle([cx - 26, cy - 14, cx + 26, cy + 62], fill=(220, 224, 232))
brush.polygon([(cx - 26, cy + 20), (cx - 52, cy + 72), (cx - 26, cy + 62)], fill=RED)
brush.polygon([(cx + 26, cy + 20), (cx + 52, cy + 72), (cx + 26, cy + 62)], fill=RED)
brush.ellipse([cx - 12, cy + 0, cx + 12, cy + 24], fill=STEEL)
brush.polygon([(cx - 14, cy + 64), (cx + 14, cy + 64), (cx, cy + 136)], fill=AMBER)
for sx, sy in [(776, 228), (922, 210), (966, 280), (782, 452), (940, 456)]:
    brush.ellipse([sx, sy, sx + 4, sy + 4], fill=ASH)
brush.line([EDGE - 380, TOP + 20, EDGE - 380, BOT - 20], fill=RULE, width=1)

# ------------------------------------------------------------ story grid
cells = [
    ('WAR · KYIV', RED, 'UKRAINE: 500,000 DEAD',
     "A leaked Russian tally exposes the war's true toll; Kyiv's bridges and power grid hit overnight."),
    ('COURT · THE HAGUE', STEEL, 'ICJ: MYANMAR GENOCIDE',
     'The World Court rules the campaign against the Rohingya amounted to genocide.'),
    ('CLIMATE · ANTALYA', JADE, 'COP31 FALLS APART',
     'Talks end in acrimony at Antalya as the EU delegation walks out; pledges stall.'),
    ('COURT · WASHINGTON', STEEL, 'HUAWEI GUILTY IN US',
     'Convicted of sanctions breaches, bank fraud and stealing trade secrets.'),
    ('TECH · AUSTIN', AMBER, 'TESLA-SPACEX PANELS',
     'Directors seated on five committees to weigh an all-stock combination.'),
    ('CULTURE · BANGKOK', ASH, 'MISS UNIVERSE 2026',
     "Jennifer Barreto of Puerto Rico wins the pageant's 75th crown."),
]

GX, GY = 16, 16
CW, CH = (EDGE - MARGIN - GX) // 2, 138
gy0 = 524
for idx, (tag, hue, title, blurb) in enumerate(cells):
    col, row = idx % 2, idx // 2
    x = MARGIN + col * (CW + GX)
    y = gy0 + row * (CH + GY)
    brush.rectangle([x, y, x + CW, y + CH], fill=CARD)
    brush.rectangle([x, y, x + 8, y + CH], fill=hue)
    brush.text((x + 26, y + 14), tag, font=face('kick', 15), fill=hue)
    brush.text((x + CW - 96, y + 14), 'A%d' % (idx + 2), font=face('tick', 13), fill=(96, 98, 106))
    brush.text((x + 26, y + 38), title, font=face('head', 27), fill=PAPER)
    draw_lines(x + 26, y + 76, wrap(blurb, face('body', 17), CW - 52),
               face('body', 17), ASH, 23)

# --------------------------------------------------------- footer ticker
ty = gy0 + 3 * (CH + GY) + 12
brush.rectangle([MARGIN, ty, EDGE, ty + 62], fill=CARD)
brush.text((MARGIN + 18, ty + 10), 'WIRE', font=face('kick', 16), fill=AMBER)
brush.text((MARGIN + 100, ty + 9),
           'Mississippi plane crash · CIA open-source system breached ·',
           font=face('body', 17), fill=PAPER)
brush.text((MARGIN + 100, ty + 35),
           'Bangladesh garment wages +36% · US-Iran war funded through January',
           font=face('body', 17), fill=PAPER)
brush.line([MARGIN, ty + 74, EDGE, ty + 74], fill=RULE, width=2)
brush.text((MARGIN, ty + 84), 'THE WORLD — page one of one',
           font=face('tick', 14), fill=ASH)
brush.text((EDGE - 150, ty + 84), '© MMDCCVI THE WORLD',
           font=face('tick', 14), fill=ASH)

page.save('/home/hermes2/makefun/news-image/repo/entry.png', 'PNG', optimize=True)
print('rendered', page.size)
