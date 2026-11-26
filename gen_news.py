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
TOP, BOT = 172, 404
brush.rectangle([MARGIN, TOP, EDGE, BOT], fill=CARD)
brush.rectangle([MARGIN, TOP, MARGIN + 8, BOT], fill=RED)
brush.rectangle([MARGIN, TOP, EDGE, TOP, ], outline=HAIR, width=1)
hx = MARGIN + 26
brush.text((hx, TOP + 14), 'SPACE · BEIJING · PAGE A1', font=face('kick', 15), fill=RED)
brush.text((hx, TOP + 38), 'BY OUR SPACE CORRESPONDENT', font=face('tick', 12), fill=ASH)
brush.text((hx, TOP + 58), 'CHINA FLIES ITS FIRST', font=face('head', 38), fill=INK)
brush.text((hx, TOP + 102), 'FOREIGN ASTRONAUT', font=face('head', 38), fill=INK)
hero_body = ("Shenzhou-24 is docked at Tiangong with Pakistan's Ali aboard — "
             "the first foreign national to live on the Chinese station, "
             "crowned by a state broadcast watched by 900 million.")
draw_lines(hx, TOP + 146, wrap(hero_body, face('body', 16), 560),
           face('body', 16), INK_SOFT, 21)
brush.text((hx, BOT - 22), 'BEIJING, TUESDAY NIGHT —', font=face('tick', 13), fill=AMBER)

# rocket illustration, right side of the hero panel
cx, cy = 880, 280
brush.polygon([(cx, cy - 80), (cx + 22, cy - 10), (cx - 22, cy - 10)], fill=(150, 154, 164))
brush.rectangle([cx - 22, cy - 10, cx + 22, cy + 48], fill=(150, 154, 164))
brush.polygon([(cx - 22, cy + 16), (cx - 42, cy + 60), (cx - 22, cy + 50)], fill=RED)
brush.polygon([(cx + 22, cy + 16), (cx + 42, cy + 60), (cx + 22, cy + 50)], fill=RED)
brush.ellipse([cx - 10, cy - 2, cx + 10, cy + 18], fill=STEEL)
brush.polygon([(cx - 12, cy + 50), (cx + 12, cy + 50), (cx, cy + 108)], fill=AMBER)
for sx, sy in [(806, 198), (942, 188), (960, 248), (812, 384), (950, 388)]:
    brush.ellipse([sx, sy, sx + 3, sy + 3], fill=ASH)
brush.line([EDGE - 300, TOP + 14, EDGE - 300, BOT - 14], fill=HAIR, width=1)
# small region-color legend under the divider column
lx = EDGE - 286
brush.text((lx, TOP + 18), 'REGIONS COVERED', font=face('kick', 11), fill=INK)
for k, (nm, hue) in enumerate([('EUROPE', RED), ('ASIA', STEEL), ('AMERICAS', JADE),
                               ('AFRICA', AMBER), ('MIDEAST', PLUM)]):
    yy = TOP + 38 + k * 17
    brush.ellipse([lx, yy, lx + 8, yy + 8], fill=hue)
    brush.text((lx + 14, yy - 3), nm, font=face('tick', 11), fill=INK_SOFT)
# world dot-map (5 rows x 12 cols, colored by region)
mx, my = EDGE - 286, TOP + 130
for r in range(5):
    for c in range(12):
        hue = [RED, STEEL, JADE, AMBER, PLUM][(r * 3 + c) % 5]
        if (r * 12 + c) % 7 != 3:
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
CH = 84
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
    brush.text((x + CW - 116, y + 9), 'via %s' % src,
               font=face('tick', 9), fill=ASH)
    brush.text((x + CW - 34, y + 9), 'A%d' % (idx + 2),
               font=face('tick', 9), fill=HAIR)

# ------------------------------------------ wire: one-liners (dense stories)
wy0 = gy0 + 4 * (CH + GY) + 8
brush.line([MARGIN, wy0, EDGE, wy0], fill=INK, width=2)
brush.text((MARGIN, wy0 + 6), 'MORE FROM THE WIRE', font=face('kick', 13), fill=INK)
brush.text((EDGE - 260, wy0 + 7), '25 NOVEMBER 2026 · 33 STORIES · 7 REGIONS',
           font=face('tick', 12), fill=INK_SOFT)
wire = [
    ('06:12 UTC', RED,    'Bangladesh garment wages rise 36% under the new accord.'),
    ('07:40 UTC', STEEL,  'UK regulator lifts the energy cap to £2,166 from January.'),
    ('09:05 UTC', AMBER,  'Fuel tanker fire south of Cairo kills at least 30.'),
    ('10:22 UTC', JADE,   'Flooded West Java gold mine: 9 dead, 17 still trapped.'),
    ('11:48 UTC', PLUM,   'US tariff schedules take effect on 14 trading partners.'),
    ('13:10 UTC', RED,    'Mississippi Delta plane crash docket opens; recorders found.'),
    ('15:31 UTC', STEEL,  'US-Iran war funding extended by Congress through January.'),
]
for k, (t_, hue, line) in enumerate(wire):
    yy = wy0 + 26 + k * 17
    brush.text((MARGIN + 4, yy), t_, font=face('tick', 12), fill=hue)
    brush.text((MARGIN + 110, yy), line, font=face('body', 13), fill=INK_SOFT)

# --------------------------------------------------- folio footer
fy = wy0 + 26 + len(wire) * 17 + 8
brush.line([MARGIN, fy, EDGE, fy], fill=HAIR, width=1)
brush.text((MARGIN, fy + 8), 'THE WORLD — page one of one',
           font=face('tick', 12), fill=ASH)
brush.text((EDGE - 170, fy + 8), '© MMDCCVI THE WORLD',
           font=face('tick', 12), fill=ASH)

page.save('/home/hermes2/makefun/news-image/repo/entry.png', 'PNG', optimize=True)
print('rendered', page.size)
