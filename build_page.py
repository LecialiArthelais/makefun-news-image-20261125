#!/usr/bin/env python3
"""Build News-25 front page (1024x1024, <=1 MiB) from spec.md + verified facts.

Layout: eyebrow -> masthead -> sub-headline -> region bar -> UTC timeline
-> THE DAY IN NUMBERS (8) -> 3 hero cards -> 10 medium cards (5x2)
-> DUE TODAY panel (FORECAST) -> world map + DATE CHECK -> briefs 14-35
(4 cols x 6 rows) -> footer with HOW SURE legend.

Verified corrections vs spec (see spec.md + fact-check):
- M13 Nvidia: -5.9% CLOSE to $155.38 (spec's "~7%" is the intraday move).
- B23 turkey pardon: 24 Nov, 2:00 PM ET, White House helipad.
- B29 BJP-SAD: 24 Nov, New Delhi.
- B31 EU Parliament briefing: 25 Nov 11:00 CET, Strasbourg.
- B28 T20: Carrara Oval, Gold Coast; England won by 8 wickets.
- H3: China pact LAPSES Apr 2027 (Wale declined comment citing NDA).
- US data (B17): FORECAST only -- build ran before the 13:30 UTC release.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MX = 24                       # side margin
CW = W - 2 * MX               # 976 content width
PAPER = (255, 255, 255)
INK = (17, 24, 39)
MUTED = (107, 114, 128)
ACCENT = (220, 38, 38)
RULE = (209, 213, 219)
DARK = (17, 24, 39)
AMBER = (245, 158, 11)

FDIR = "/usr/share/fonts/truetype/dejavu"
LDIR = "/usr/share/fonts/truetype/liberation"
def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)

SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF   = lambda s: font("DejaVuSerif.ttf", s)
SERIF_I = lambda s: ImageFont.truetype(os.path.join(LDIR, "LiberationSerif-Italic.ttf"), s)
SANS_B  = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS    = lambda s: font("DejaVuSans.ttf", s)
MONO    = lambda s: font("DejaVuSansMono.ttf", s)
LIB_B   = lambda s: ImageFont.truetype(os.path.join(LDIR, "LiberationSans-Bold.ttf"), s)
LIB     = lambda s: ImageFont.truetype(os.path.join(LDIR, "LiberationSans-Regular.ttf"), s)
MONO_B  = lambda s: font("DejaVuSansMono-Bold.ttf", s)

REGIONS = [
    ("EAST ASIA", 5, (29, 78, 216)),
    ("OCEANIA", 4, (14, 116, 144)),
    ("SOUTH ASIA", 1, (124, 58, 237)),
    ("EUROPE", 7, (79, 70, 229)),
    ("AMERICAS", 11, (180, 83, 9)),
    ("MIDDLE EAST", 5, (220, 38, 38)),
    ("WORLD", 1, (71, 85, 105)),
]
REGION_COLOR = {r[0]: r[2] for r in REGIONS}

NUMBERS = [
    ("4.9%", "AU CPI, Oct YoY"),
    ("3.8%", "Trimmed mean"),
    ("00:18", "Shenzhou-24 launch"),
    ("11", "Wounded in Riyadh"),
    ("10/12", "Huawei counts guilty"),
    ("2,212", "Metro jobs saved"),
    ("4", "Tankers claimed hit"),
    ("30", "Hostages, Cartagena"),
]

TIMELINE = ("00:18 Shenzhou lifts off  ·  00:30 AU CPI 4.9%  ·  02:40 Seoul Metro deal  ·  "
            "10:43 Flinders warning  ·  13:30 US data DUE  ·  15:00 Gukesh Game 2  ·  "
            "17:00 EU–Balkans summit  ·  p.m. Trump–Rutte")

DUE = ("DUE TODAY 13:30 UTC — US DATA PILE (FORECASTS, NOT ACTUALS):  GDP Q3 +3.6%  ·  "
       "core PCE +3.2% YoY  ·  jobless claims ~200k  ·  durables +1.1%  ·  "
       "new-home sales ~648k  ·  Beige Book 14:00 ET")

# ---------------------------------------------------------------- stories
# tag: CONFIRMED / OFFICIAL / REPORTED / CLAIMED / SCHEDULED / FORECAST
HEROES = [
    dict(n=1, region="EAST ASIA", place="JIUQUAN", date="TUE 25 NOV", illo="h1",
         head="Shenzhou-24 lifts off with Pakistan's first astronaut",
         body=("Long March-2F launched 00:18:52 UTC with Tang Hongbo, Wu Yi and "
               "Muhammad Zeeshan Ali — the first Pakistani in orbit and the first "
               "foreign astronaut on Tiangong."),
         src="China Manned Space Agency", tag="CONFIRMED"),
    dict(n=2, region="OCEANIA", place="CANBERRA", date="TUE 25 NOV", illo="h2",
         head="Australia inflation jumps to 4.9% — hottest in about three years",
         body=("CPI rose 4.9% YoY (from 4.3%), above the 4.8% forecast; trimmed mean "
               "3.8%. Electricity +25.2%, transport +10.6%, housing +6.4%. RBA rate "
               "4.85%."),
         src="Australian Bureau of Statistics", tag="OFFICIAL"),
    dict(n=3, region="OCEANIA", place="CANBERRA", date="TUE 25 NOV", illo="h3",
         head="Solomons signs treaty with Australia, scraps China pact",
         body=("Albanese and PM Matthew Wale signed, making Australia the 'security "
               "partner of choice'. Honiara lets its 2022 China pact lapse in April "
               "2027."),
         src="Prime Minister of Australia", tag="CONFIRMED"),
]

MEDIUMS = [
    dict(n=4, region="MIDDLE EAST", place="RIYADH", date="MON 24 NOV", illo="m4",
         head="Houthi drone hits Riyadh's tallest tower",
         body=("A drone hit the 385m PIF Tower, the second strike in a week. 11 "
               "wounded; Riyadh vows to respond."),
         src="SPA · Saudi officials", tag="CONFIRMED"),
    dict(n=5, region="AMERICAS", place="NEW YORK", date="MON 24 NOV", illo="m5",
         head="Huawei guilty on 10 of 12 counts in US trial",
         body=("Brooklyn jury: Huawei guilty on 10 of 12 counts — fraud, sanctions "
               "breaches, trade-secret theft."),
         src="US District Court, Brooklyn", tag="CONFIRMED"),
    dict(n=6, region="OCEANIA", place="FLINDERS ISLAND", date="TUE 25 NOV", illo="m6",
         head="Flinders Island fire: 'too late to leave'",
         body=("Emergency Warning for three towns as the fire (~3,000 ha) bore down: "
               "'too late to leave'."),
         src="Tasmania Fire Service", tag="OFFICIAL"),
    dict(n=7, region="EAST ASIA", place="SEOUL", date="TUE 25 NOV", illo="m7",
         head="Seoul Metro strike called off at the last hour",
         body=("A deal at 02:40 KST after ~18 hours of talks: 2,212 job cuts "
               "suspended, 500 hires, pay +3.5%."),
         src="Seoul Metro · unions", tag="CONFIRMED"),
    dict(n=8, region="EAST ASIA", place="ULLEUNG", date="MON 24 NOV", illo="m8",
         head="Russian jets near Ulleung; shelter alert issued",
         body=("Russian jets entered the KADIZ near Ulleung; Seoul scrambled fighters "
               "and issued a rare shelter alert."),
         src="ROK Joint Chiefs of Staff", tag="REPORTED"),
    dict(n=9, region="MIDDLE EAST", place="BAGHDAD", date="TUE 25 NOV", illo="m9",
         head="Baghdad orders takeover of Kurdish oilfields",
         body=("Federal control of oilfields in four provinces ordered. Kurdistan: "
               "'in no way acceptable'."),
         src="Iraqi government", tag="CONFIRMED"),
    dict(n=10, region="MIDDLE EAST", place="STRAIT OF HORMUZ", date="MON 24 NOV", illo="m10",
         head="Iran claims four tankers hit mines in Hormuz",
         body=("IRGC claims four tankers struck mines in the Strait; Reuters could "
               "not verify it."),
         src="IRGC Navy (via Reuters)", tag="CLAIMED"),
    dict(n=11, region="EUROPE", place="GULF OF FINLAND", date="MON 24 NOV", illo="m11",
         head="Kyiv confirms it hit Russian ship Sparta II",
         body=("Zelenskiy confirmed Ukraine hit the Russian ship Sparta II with drones "
               "in the Gulf of Finland."),
         src="Zelenskiy, via Bloomberg", tag="CONFIRMED"),
    dict(n=12, region="AMERICAS", place="WASHINGTON", date="TUE 25 NOV", illo="m12",
         head="CIA and ODNI hit by breach of spy network",
         body=("The CIA and ODNI found a breach of an unclassified network. No "
               "classified systems were hit."),
         src="CIA · ODNI", tag="REPORTED"),
    dict(n=13, region="AMERICAS", place="NEW YORK", date="MON 24 NOV", illo="m13",
         head="Nvidia gives back 5.9% a day after +31.5%",
         body=("Nvidia fell 5.9% to $155.38 a day after +31.5% on Huang's return. "
               "Nasdaq −1.48%; chips −7.88%."),
         src="NYSE · Nasdaq", tag="CONFIRMED"),
]

BRIEFS = [
    (14, "TOKYO", "Six parties move to censure Seki", "Over a 2024 fundraising scandal."),
    (15, "BRUSSELS", "EU–Balkans summit — without Serbia", "Costa, von der Leyen host six partners."),
    (16, "PALM BEACH", "Trump to meet NATO chief Rutte", "Closed-door talks at Mar-a-Lago today."),
    (17, "WASHINGTON", "US data pile due 13:30 UTC", "GDP, PCE, claims — forecasts only."),
    (18, "GENEVA", "Gukesh–Sindarov Game 2 today", "Game 1 drawn in 38 moves; 0.5–0.5."),
    (19, "GLOBAL", "16 Days of Activism begins", "UN Women campaign runs to 10 Dec."),
    (20, "MADRID", "Real Madrid 5–1 PSV", "Bellingham stunner, Mbappé brace."),
    (21, "CARTAGENA", "30 hostages seized in Cartagena", "Gunmen fled a failed truck robbery."),
    (22, "OTTAWA", "Astronaut Kutryk a father from orbit", "Crew-13's Kutryk welcomes a baby girl."),
    (23, "WASHINGTON", "Trump pardons Freedom, Feathers", "Pardon Tue 24 Nov, 2pm ET."),
    (24, "WASHINGTON", "Giuliani gets Medal of Freedom", "Ex-New York mayor honoured 24 Nov."),
    (25, "PARIS", "Sarkozy corruption case goes to trial", "Pre-trial hearing set for 1 Apr 2027."),
    (26, "FORT HOOD", "Fort Hood shooter seeks stay", "Hasan killed 13 in 2009."),
    (27, "VILLAVICENCIO", "Car bomb rocks Villavicencio", "Government blames FARC dissidents."),
    (28, "CARRARA", "England win 2nd T20I by 8 wickets", "Donald 85 off 32; England chased 185."),
    (29, "NEW DELHI", "BJP, Akali Dal ally for Punjab 2027", "Reunited after six years; 117 seats."),
    (30, "TOKYO", "Nikkei falls 2.8% at the open", "Advantest −12% as chip rout resumes."),
    (31, "STRASBOURG", "EU Parliament briefs on funds", "11:00 CET, Strasbourg; €17.12bn bid."),
    (32, "HODEIDAH", "Saudi jets hit Hodeidah telecom site", "Houthi media: 4 killed, 18 hurt."),
    (33, "ADEN", "Houthis 'won't seize Aden', army says", "Houthis said to be 60 km from Aden."),
    (34, "BRUSSELS", "EU leaders head for budget summit", "Special Council 26–27 Nov; €1.78tn."),
    (35, "GLOBAL", "COP31 ended with no deal — see below", "Climate summit closed 22 Nov."),
]

DATE_CHECK_EXCLUDED = [
    "COP31 ends with no deal — 22 Nov, Antalya.",
    "ICJ: Myanmar guilty of Rohingya genocide — 19 Nov.",
    "UK formally recognises the Rohingya genocide — 23 Nov.",
    "700,000 Russian troops dead — analysis published 23 Nov.",
    "Prabowo names two VP picks — 23 Nov, Jakarta.",
    "Sparta II attack itself — 21 Nov (confirmation in M11).",
    "Russian ship sunk off Benghazi — 22 Nov.",
    "Nepal PM's India visit ends — 23 Nov.",
    "KADIZ incident — 17 Nov (superseded by M8).",
    "Market falls 20–23 Nov — only the 25 Nov open in B30.",
    "Hodeidah airstrike — 23 Nov (context in B32).",
]
DATE_CHECK_DEMOTED = [
    "Gukesh–Sindarov Game 1: draw, 38 moves — 24 Nov (in B18).",
    "First PIF Tower strike — 19 Nov, no casualties (in M4).",
]

TAG_COLOR = {
    "CONFIRMED": (21, 128, 61),
    "OFFICIAL": (29, 78, 216),
    "REPORTED": (180, 83, 9),
    "CLAIMED": (220, 38, 38),
    "SCHEDULED": (71, 85, 105),
    "FORECAST": (180, 83, 9),
}

# ---------------------------------------------------------------- helpers
def wrap(text, fnt, width):
    """Greedy word wrap; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if fnt.getlength(t) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def fit_font(text, make_font, size, width, min_size=6):
    """Largest font size <= size whose text fits width."""
    s = size
    while s > min_size and make_font(s).getlength(text) > width:
        s -= 1
    return make_font(s)

def load_illo(key):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "illos", key + ".png")
    im = Image.open(p).convert("RGB")
    assert im.size == (960, 240), (key, im.size)
    return im

def illo_crop(im, ratio):
    """Centre-crop a 960x240 (4:1) illo to the target width/height ratio."""
    w, h = im.size
    tw = int(h * ratio)
    x0 = (w - tw) // 2
    return im.crop((x0, 0, x0 + tw, h))

# ---------------------------------------------------------------- build
def build(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    defects = []
    y = 12

    # ---- eyebrow ----
    d.text((MX, y), "35 STORIES  ·  7 REGIONS  ·  ALL TIMES UTC  ·  EVERY STORY DATED BY ITS EVENT",
           fill=ACCENT, font=MONO_B(10))
    d.text((W - MX - MONO_B(10).getlength("THE WORLD IN ONE PAGE"), y), "THE WORLD IN ONE PAGE",
           fill=MUTED, font=MONO_B(10))
    y += 15

    # ---- masthead ----
    d.line([(MX, y), (W - MX, y)], fill=INK, width=2)
    y += 3
    f_mast = fit_font("WEDNESDAY, 25 NOVEMBER 2026", SERIF_B, 44, CW)
    d.text((MX, y), "WEDNESDAY, 25 NOVEMBER 2026", fill=INK, font=f_mast)
    # date line: how-sure note, right aligned
    y += 44
    d.line([(MX, y), (W - MX, y)], fill=INK, width=2)
    y += 5
    # ---- sub-headline ----
    sub = ("Shenzhou-24 carries the first Pakistani into orbit  /  Australia inflation jumps to 4.9%  /  "
           "Solomons scraps its China pact, signs with Canberra")
    f_sub = fit_font(sub, SERIF_I, 14, CW)
    d.text((MX, y), sub, fill=INK, font=f_sub)
    y += 19

    # ---- region bar ----
    seg_w = CW // len(REGIONS)
    for i, (name, cnt, col) in enumerate(REGIONS):
        x0 = MX + i * seg_w
        x1 = MX + (i + 1) * seg_w if i < len(REGIONS) - 1 else W - MX
        d.rectangle([x0, y, x1 - 2, y + 18], fill=col)
        lab = f"{name} {cnt}"
        f_lab = MONO_B(9)
        tw = f_lab.getlength(lab)
        d.text((x0 + (x1 - x0 - tw) / 2, y + 4), lab, fill=(255, 255, 255), font=f_lab)
    y += 23

    # ---- UTC timeline ----
    f_tl = fit_font(TIMELINE, SANS, 10, CW)
    d.text((MX, y), TIMELINE, fill=MUTED, font=f_tl)
    y += 15

    # ---- THE DAY IN NUMBERS ----
    d.rectangle([MX, y, W - MX, y + 44], fill=DARK)
    d.text((MX + 10, y + 4), "THE DAY IN NUMBERS", fill=(255, 255, 255), font=MONO_B(9))
    cell_w = (CW - 170) // 8
    x = MX + 170
    for num, lab in NUMBERS:
        f_num = fit_font(num, SANS_B, 18, cell_w - 8)
        d.text((x, y + 5), num, fill=(255, 255, 255), font=f_num)
        for j, ln in enumerate(wrap(lab, SANS(8), cell_w - 8)):
            d.text((x, y + 26 + j * 9), ln, fill=(209, 213, 219), font=SANS(8))
        x += cell_w
    y += 46

    # ---- hero cards (3 cols) ----
    HERO_H = 152
    HERO_W = (CW - 16) // 3
    ILLO_H = 54
    for i, s in enumerate(HEROES):
        x0 = MX + i * (HERO_W + 8)
        d.rectangle([x0, y, x0 + HERO_W, y + HERO_H], outline=RULE, width=1)
        # illustration band (4:1 -> crop to slot ratio)
        im = load_illo(s["illo"])
        slot = illo_crop(im, HERO_W / ILLO_H).resize((HERO_W, ILLO_H), Image.LANCZOS)
        img.paste(slot, (x0, y))
        ty = y + ILLO_H + 4
        # kicker: number + region + place + date, left; tag chip right
        col = REGION_COLOR[s["region"]]
        kick = f"{s['n']} · {s['region']} · {s['place']} · {s['date']}"
        f_k = MONO_B(8)
        d.text((x0 + 8, ty), kick, fill=col, font=f_k)
        tag = s["tag"]
        tw = MONO_B(8).getlength(tag) + 8
        d.rectangle([x0 + HERO_W - tw - 6, ty - 1, x0 + HERO_W - 6, ty + 11], fill=TAG_COLOR[tag])
        d.text((x0 + HERO_W - tw - 2, ty), tag, fill=(255, 255, 255), font=MONO_B(8))
        ty += 13
        # headline, 2 lines max
        hl = wrap(s["head"], SERIF_B(15), HERO_W - 16)
        if len(hl) > 2:
            defects.append(f"hero {s['n']} headline {len(hl)} lines: {s['head']}")
        for ln in hl[:2]:
            d.text((x0 + 8, ty), ln, fill=INK, font=SERIF_B(15))
            ty += 17
        # body, 3 lines max
        bl = wrap(s["body"], SANS(10), HERO_W - 16)
        if len(bl) > 3:
            defects.append(f"hero {s['n']} body {len(bl)} lines: {s['body']}")
        for ln in bl[:3]:
            d.text((x0 + 8, ty), ln, fill=(55, 65, 81), font=SANS(10))
            ty += 12
        # source, bottom
        d.text((x0 + 8, y + HERO_H - 12), s["src"].upper(), fill=MUTED, font=MONO(7))
    y += HERO_H + 5

    # ---- medium cards (5 cols x 2 rows) ----
    MED_H = 134
    MED_W = (CW - 4 * 8) // 5
    M_ILLO_H = 50
    for row in range(2):
        for c in range(5):
            s = MEDIUMS[row * 5 + c]
            x0 = MX + c * (MED_W + 8)
            yy = y + row * (MED_H + 6)
            d.rectangle([x0, yy, x0 + MED_W, yy + MED_H], outline=RULE, width=1)
            im = load_illo(s["illo"])
            slot = illo_crop(im, MED_W / M_ILLO_H).resize((MED_W, M_ILLO_H), Image.LANCZOS)
            img.paste(slot, (x0, yy))
            ty = yy + M_ILLO_H + 3
            col = REGION_COLOR[s["region"]]
            kick = f"{s['n']} · {s['place']}"
            f_k = MONO_B(7)
            d.text((x0 + 6, ty), kick, fill=col, font=f_k)
            tag = s["tag"]
            tw = MONO_B(7).getlength(tag) + 6
            d.rectangle([x0 + MED_W - tw - 4, ty - 1, x0 + MED_W - 4, ty + 9], fill=TAG_COLOR[tag])
            d.text((x0 + MED_W - tw - 1, ty), tag, fill=(255, 255, 255), font=MONO_B(7))
            ty += 11
            hl = wrap(s["head"], SANS_B(11), MED_W - 12)
            if len(hl) > 2:
                defects.append(f"medium {s['n']} headline {len(hl)} lines: {s['head']}")
            for ln in hl[:2]:
                d.text((x0 + 6, ty), ln, fill=INK, font=SANS_B(11))
                ty += 13
            bl = wrap(s["body"], SANS(9), MED_W - 12)
            if len(bl) > 3:
                defects.append(f"medium {s['n']} body {len(bl)} lines: {s['body']}")
            for ln in bl[:3]:
                d.text((x0 + 6, ty), ln, fill=(55, 65, 81), font=SANS(9))
                ty += 11
            d.text((x0 + 6, yy + MED_H - 11), s["src"].upper(), fill=MUTED, font=MONO(6))
    y += 2 * MED_H + 6 + 5

    # ---- DUE TODAY panel ----
    d.rectangle([MX, y, W - MX, y + 30], outline=AMBER, width=1)
    d.rectangle([MX, y, W - MX, y + 30], fill=(255, 251, 235))
    f_due = fit_font(DUE, SANS_B, 10, CW - 20)
    d.text((MX + 10, y + 9), DUE, fill=(146, 64, 14), font=f_due)
    y += 33

    # ---- map + DATE CHECK ----
    MAP_H = 185
    map_im = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "map_panel.png")).convert("RGB")
    assert map_im.size[0] == 470, map_im.size
    img.paste(map_im.resize((470, MAP_H), Image.LANCZOS), (MX, y))
    d.text((MX, y + MAP_H - 14), "WORLD MAP — PIN = STORY NUMBER", fill=MUTED, font=MONO(7))
    dx = MX + 470 + 8
    dw = W - MX - dx
    d.rectangle([dx, y, W - MX, y + MAP_H], outline=RULE, width=1)
    d.text((dx + 8, y + 5), "DATE CHECK — WHY THESE ARE NOT IN TODAY'S NEWS",
           fill=ACCENT, font=MONO_B(8))
    d.line([(dx + 8, y + 17), (W - MX - 8, y + 17)], fill=RULE, width=1)
    ty = y + 21
    d.text((dx + 8, ty), "EXCLUDED — TOO OLD (≥36 HOURS BEFORE 25 NOV 02:00 UTC)",
           fill=MUTED, font=MONO_B(7))
    ty += 11
    for it in DATE_CHECK_EXCLUDED:
        d.text((dx + 8, ty), "·  " + it, fill=(55, 65, 81), font=SANS(8.5))
        ty += 10
    ty += 1
    d.text((dx + 8, ty), "DEMOTED — FOLDED INTO A LIVE STORY",
           fill=MUTED, font=MONO_B(7))
    ty += 11
    for it in DATE_CHECK_DEMOTED:
        d.text((dx + 8, ty), "·  " + it, fill=(55, 65, 81), font=SANS(8.5))
        ty += 10
    if ty > y + MAP_H - 4:
        defects.append(f"DATE CHECK overflows by {ty - (y + MAP_H - 4):.0f}px")
    y += MAP_H + 5

    # ---- briefs 14-35 (4 cols x 6 rows) ----
    d.text((MX, y), "THE REST OF THE DAY — BRIEFS 14–35", fill=INK, font=MONO_B(9))
    y += 14
    BRIEF_H = 20
    COL_W = (CW - 3 * 12) // 4
    for i, (n, place, head, summ) in enumerate(BRIEFS):
        r, c = divmod(i, 4)
        x0 = MX + c * (COL_W + 12)
        yy = y + r * BRIEF_H
        line1 = f"{n} · {place} — {head}"
        l1 = wrap(line1, LIB_B(8.5), COL_W)
        if len(l1) > 1:
            defects.append(f"brief {n} line1 {len(l1)} lines: {line1}")
        d.text((x0, yy), l1[0], fill=INK, font=LIB_B(8.5))
        l2 = wrap(summ, LIB(8.5), COL_W)
        if len(l2) > 1:
            defects.append(f"brief {n} line2 {len(l2)} lines: {summ}")
        d.text((x0, yy + 10), l2[0], fill=MUTED, font=LIB(8.5))
    y += 6 * BRIEF_H + 5

    # ---- footer ----
    d.line([(MX, y), (W - MX, y)], fill=RULE, width=1)
    y += 5
    foot1 = ("HOW SURE:  CONFIRMED = verified by ≥2 sources or official  ·  OFFICIAL = agency statement  ·  "
             "REPORTED = 1+ major outlet  ·  CLAIMED = one party, unverified  ·  FORECAST = estimate, not actual")
    f_f1 = fit_font(foot1, SANS, 8, CW)
    d.text((MX, y), foot1, fill=MUTED, font=f_f1)
    y += 11
    foot2 = ("All times UTC  ·  Every story dated by its event, not the article date  ·  Illustrations are original "
             "flat-vector drawings  ·  Sources named on each story  ·  News-25 · 25 November 2026")
    f_f2 = fit_font(foot2, SANS, 8, CW)
    d.text((MX, y), foot2, fill=MUTED, font=f_f2)
    y += 12

    img.save(out_path, optimize=True)
    size = os.path.getsize(out_path)
    print(f"saved {out_path}: {img.size}, {size} bytes ({size/1024:.0f} KiB), final y={y}")
    print(f"1 MiB gate: {'PASS' if size <= 1048576 else 'FAIL'}; 1024x1024 gate: {'PASS' if img.size == (1024, 1024) else 'FAIL'}")
    if defects:
        print(f"DEFECTS ({len(defects)}):")
        for df in defects:
            print("  -", df)
    else:
        print("DEFECTS: 0")
    return defects, y

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    build(out)
