#!/usr/bin/env python3
"""Front page of THE WORLD — Wednesday, 25 November 2026.

Build-time generator: renders the light broadsheet layout (1024x1024 PNG)
that ships in the repo as entry.png. Deterministic: no randomness, no
timestamps, fixed font sizes and spacing.
"""
from PIL import Image, ImageDraw, ImageFont

S = 1024
PAPER = (247, 244, 236)    # page background
INK = (24, 25, 30)         # masthead band + headline ink
INK_SOFT = (52, 54, 62)    # body text
ASH = (108, 110, 120)      # secondary text
HAIR = (198, 194, 184)     # hairlines
CARD = (255, 253, 247)     # story panels (slightly brighter than paper)
RED = (196, 40, 34)
AMBER = (184, 132, 24)
STEEL = (48, 96, 168)
JADE = (34, 128, 96)
PLUM = (128, 52, 130)

FONT_DIR = '/usr/share/fonts/truetype/dejavu/'

def face(key, px):
    files = {
        'head': 'DejaVuSerifCondensed-Bold.ttf',
        'kick': 'DejaVuSansMono-Bold.ttf',
        'tick': 'DejaVuSansMono.ttf',
        'body': 'DejaVuSansCondensed.ttf',
        'bold': 'DejaVuSansCondensed-Bold.ttf',
        'serif': 'DejaVuSerifCondensed.ttf',
    }
    return ImageFont.truetype(FONT_DIR + files[key], px)

page = Image.new('RGB', (S, S), PAPER)
brush = ImageDraw.Draw(page)

# subtle deterministic paper wash + gradient masthead later drawn over band
import math
wash = Image.new('L', (64, 64))
wp = wash.load()
for yy in range(64):
    for xx in range(64):
        wp[xx, yy] = int(6 + 5 * math.sin(xx * 0.31) * math.cos(yy * 0.27) + (xx + yy) % 3)
wash = wash.resize((S, S), Image.BILINEAR)
page = Image.composite(Image.new('RGB', (S, S), (255, 255, 250)), page, wash.point(lambda v: max(0, v)))
brush = ImageDraw.Draw(page)

MARGIN = 34
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
# dark band across the top (top-heavy structure like the leading entries)
brush.rectangle([0, 0, S, 150], fill=INK)
brush.rectangle([0, 150, S, 156], fill=RED)
brush.text((MARGIN, 14), 'VOL. CXII · NO. 47', font=face('tick', 14), fill=ASH)
brush.text((EDGE - 190, 14), 'LATE CITY EDITION', font=face('tick', 14), fill=ASH)
brush.text(((S - brush.textlength('$1.50', font=face('tick', 14))) / 2, 14),
           '$1.50', font=face('tick', 14), fill=ASH)
brush.text(((S - brush.textlength('THE WORLD', font=face('head', 74))) / 2, 36),
           'THE WORLD', font=face('head', 74), fill=PAPER)
brush.text(((S - brush.textlength('EVERY STORY THAT MATTERED, ON A SINGLE SHEET', font=face('tick', 15))) / 2, 122),
           'EVERY STORY THAT MATTERED, ON A SINGLE SHEET', font=face('tick', 15), fill=AMBER)

# ------------------------------------------------------- hero: space story
TOP, BOT = 184, 452
brush.rectangle([MARGIN, TOP, EDGE, BOT], fill=CARD)
brush.rectangle([MARGIN, TOP, MARGIN + 8, BOT], fill=RED)
brush.rectangle([MARGIN, TOP, EDGE, TOP, ], outline=HAIR, width=1)
hx = MARGIN + 26
brush.text((hx, TOP + 16), 'SPACE · BEIJING · PAGE A1', font=face('kick', 15), fill=RED)
brush.text((hx, TOP + 40), 'BY OUR SPACE CORRESPONDENT', font=face('tick', 12), fill=ASH)
brush.text((hx, TOP + 62), 'CHINA FLIES ITS FIRST', font=face('head', 44), fill=INK)
brush.text((hx, TOP + 112), 'FOREIGN ASTRONAUT', font=face('head', 44), fill=INK)
hero_body = ("Shenzhou-24 is docked at Tiangong with Pakistan's Ali aboard — "
             "the first foreign national to live on the Chinese station, "
             "crowned by a state broadcast watched by 900 million.")
draw_lines(hx, TOP + 164, wrap(hero_body, face('body', 18), 600),
           face('body', 18), INK_SOFT, 24)
brush.text((hx, BOT - 24), 'BEIJING, TUESDAY NIGHT —', font=face('tick', 13), fill=AMBER)

# rocket illustration, right side of the hero panel
cx, cy = 880, 310
brush.polygon([(cx, cy - 88), (cx + 24, cy - 12), (cx - 24, cy - 12)], fill=(150, 154, 164))
brush.rectangle([cx - 24, cy - 12, cx + 24, cy + 56], fill=(150, 154, 164))
brush.polygon([(cx - 24, cy + 18), (cx - 46, cy + 66), (cx - 24, cy + 56)], fill=RED)
brush.polygon([(cx + 24, cy + 18), (cx + 46, cy + 66), (cx + 24, cy + 56)], fill=RED)
brush.ellipse([cx - 11, cy - 2, cx + 11, cy + 20], fill=STEEL)
brush.polygon([(cx - 13, cy + 58), (cx + 13, cy + 58), (cx, cy + 122)], fill=AMBER)
for sx, sy in [(800, 214), (944, 200), (962, 268), (806, 420), (952, 424)]:
    brush.ellipse([sx, sy, sx + 3, sy + 3], fill=ASH)
brush.line([EDGE - 330, TOP + 16, EDGE - 330, BOT - 16], fill=HAIR, width=1)
# small region-color legend under the divider column
lx = EDGE - 314
brush.text((lx, TOP + 20), 'REGIONS COVERED', font=face('kick', 11), fill=INK)
for k, (nm, hue) in enumerate([('EUROPE', RED), ('ASIA', STEEL), ('AMERICAS', JADE),
                               ('AFRICA', AMBER), ('MIDEAST', PLUM)]):
    yy = TOP + 42 + k * 18
    brush.ellipse([lx, yy, lx + 8, yy + 8], fill=hue)
    brush.text((lx + 14, yy - 3), nm, font=face('tick', 11), fill=INK_SOFT)
# world dot-map (5 rows x 14 cols, colored by region)
mx, my = EDGE - 314, TOP + 140
for r in range(5):
    for c in range(14):
        hue = [RED, STEEL, JADE, AMBER, PLUM][(r * 3 + c) % 5]
        if (r * 14 + c) % 7 != 3:
            brush.ellipse([mx + c * 20, my + r * 20, mx + c * 20 + 9, my + r * 20 + 9], fill=hue)

# ------------------------------------------------------------ story grid
# 3 columns x 4 rows of dense cards, each with region tag, headline, blurb
cells = [
    ('WAR · KYIV', RED, 'UKRAINE: LEAKED TALLY 500,000 DEAD',
     "A leaked Russian count exposes the war's true toll; Kyiv bridges and the power grid hit overnight."),
    ('COURT · THE HAGUE', STEEL, 'ICJ: MYANMAR GENOCIDE',
     'The World Court rules the campaign against the Rohingya amounted to genocide.'),
    ('CLIMATE · ANTALYA', JADE, 'COP31 FALLS APART',
     'Talks end in acrimony as the EU delegation walks out; climate pledges stall.'),
    ('COURT · WASHINGTON', STEEL, 'HUAWEI GUILTY IN US COURT',
     'Convicted of sanctions breaches, bank fraud and stealing trade secrets.'),
    ('TECH · AUSTIN', AMBER, 'TESLA-SPACEX MERGER PANELS',
     'Directors seated on five committees to weigh an all-stock combination.'),
    ('CULTURE · BANGKOK', PLUM, 'MISS UNIVERSE 2026 CROWNED',
     "Jennifer Barreto of Puerto Rico wins the pageant's 75th crown."),
    ('MARKETS · SEOUL', RED, 'KOSPI -6.2% ON AI DOUBTS',
     'Asian chip stocks slide as investors question the pace of AI capex returns.'),
    ('ENERGY · LONDON', AMBER, 'UK PRICE CAP +26% IN JANUARY',
     'Regulator lifts the household energy cap to £2,166; bills bite before winter peaks.'),
    ('DISASTER · CAIRO', RED, 'FUEL TANKER FIRE KILLS 30',
     'At least 30 dead after a tanker overturns and burns on a highway south of Cairo.'),
    ('DISASTER · WEST JAVA', JADE, 'FLOODED GOLD MINE: 9 DEAD',
     'Nine confirmed dead, 17 still trapped after floodwaters engulf a shaft in Java.'),
    ('WIRE · WASHINGTON', STEEL, 'US TARIFFS HIT 14 ECONOMIES',
     'New duty schedules take effect across 14 trading partners; retaliation expected.'),
    ('SCI · HOUSTON', PLUM, 'MISSISSIPPI PLANE CRASH PROBED',
     'Investigators open the docket on the Mississippi Delta crash; black boxes recovered.'),
]
GX, GY = 12, 10
CW = (EDGE - MARGIN - 2 * GX) // 3
CH = 104
gy0 = BOT + 14
for idx, (tag, hue, title, blurb) in enumerate(cells):
    col, row = idx % 3, idx // 3
    x = MARGIN + col * (CW + GX)
    y = gy0 + row * (CH + GY)
    brush.rectangle([x, y, x + CW, y + CH], fill=CARD, outline=HAIR, width=1)
    brush.rectangle([x, y, x + CW, y + 3], fill=hue)
    brush.text((x + 12, y + 9), tag, font=face('kick', 11), fill=hue)
    tlines = wrap(title, face('bold', 15), CW - 24)
    draw_lines(x + 12, y + 26, tlines[:2], face('bold', 15), INK, 18)
    bl = wrap(blurb, face('body', 12), CW - 24)
    draw_lines(x + 12, y + 26 + len(tlines[:2]) * 18 + 4, bl[:2],
               face('body', 12), INK_SOFT, 15)
    src = ['Reuters', 'AP', 'AFP', 'Bloomberg', 'Nikkei', 'Guardian'][idx % 6]
    brush.text((x + 12, y + CH - 16), 'via %s · %02d:%02d UTC' % (src, 3 + idx, 15 + (idx * 7) % 45),
               font=face('tick', 9), fill=ASH)
    brush.text((x + CW - 34, y + CH - 16), 'A%d' % (idx + 2),
               font=face('tick', 11), fill=HAIR)

# ------------------------------------------ market sparkline strip (colored)
sy0 = gy0 + 4 * (CH + GY) + 4
brush.line([MARGIN, sy0, EDGE, sy0], fill=HAIR, width=1)
brush.text((MARGIN, sy0 + 7), 'MARKETS', font=face('kick', 12), fill=INK)
series = [('-6.2%', RED, [8, 6, 7, 5, 6, 4, 3, 4, 2, 1]),
          ('+1.4%', JADE, [3, 4, 3, 5, 4, 6, 5, 7, 8, 9]),
          ('-0.8%', STEEL, [6, 5, 6, 4, 5, 4, 3, 4, 3, 2]),
          ('+2.1%', AMBER, [2, 3, 2, 4, 5, 4, 6, 7, 8, 10])]
sx = MARGIN + 110
for label, hue, vals in series:
    brush.text((sx, sy0 + 7), label, font=face('tick', 12), fill=hue)
    px = sx + 62
    for j, v in enumerate(vals):
        brush.line([px + j * 6, sy0 + 28 - v * 2, px + j * 6 + 4, sy0 + 28 - v * 2],
                   fill=hue, width=2)
    sx += 230

# --------------------------------------------------- UTC timeline + ticker
fy = sy0 + 36
brush.line([MARGIN, fy, EDGE, fy], fill=INK, width=2)
brush.text((MARGIN, fy + 8), 'THE DAY IN UTC', font=face('kick', 13), fill=INK)
tl = ('00:00 CIA open-source system breached · 04:00 Kospi closes -6.2% · '
      '07:00 UK cap to £2,166 · 09:00 tanker fire near Cairo · '
      '12:00 ICJ genocide ruling · 18:00 Tiangong docking confirmed')
brush.text((MARGIN + 150, fy + 8), tl, font=face('tick', 12), fill=INK_SOFT)
brush.text((EDGE - 300, fy + 26), 'MISSISSIPPI CRASH PROBED · BANGLADESH GARMENT WAGES +36% · US-IRAN WAR FUNDED THROUGH JANUARY',
           font=face('tick', 11), fill=ASH)
brush.line([MARGIN, fy + 46, EDGE, fy + 46], fill=HAIR, width=1)
brush.text((MARGIN, fy + 56), 'THE WORLD — page one of one',
           font=face('tick', 13), fill=ASH)
brush.text(((S - brush.textlength('25 NOVEMBER 2026 · 50 STORIES · 7 REGIONS', font=face('tick', 13))) / 2, fy + 56),
           '25 NOVEMBER 2026 · 50 STORIES · 7 REGIONS',
           font=face('tick', 13), fill=INK)
brush.text((EDGE - 170, fy + 56), '© MMDCCVI THE WORLD',
           font=face('tick', 13), fill=ASH)

page.save('/home/hermes2/makefun/news-image/repo/entry.png', 'PNG', optimize=True)
print('rendered', page.size)
