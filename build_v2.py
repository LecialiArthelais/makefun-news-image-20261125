#!/usr/bin/env python3
"""News-25 v2 front page (1024x1024, <=1 MiB) — three-direction build.

Directions (huashu-design, 3 real drafts, one file, --direction A|B|C):
  A = asymmetric editorial: one wide hero left + two heroes stacked right.
  B = giant hero: full-width split hero (big number + type) + two hero strips.
  C = map-led: wide world map first, then a cinematic hero band.
Shared: same 39 verified stories, same numbers strip, same map/date-check.

Design system (single accent, broadsheet):
  paper white, ink near-black, ONE accent = deep blue #1E40AF (+tints).
  Region bar: single accent, no 7-colour rainbow. No decorative all-caps
  labels, no 01/02/03 numbering, no arrows, no gradients. Datelines carry
  place+date (functional newspaper convention); story numbers are map-pin
  references, not decoration.

Facts (all verified 26 Nov 2026, see BUILD-v2.md):
  US data actuals BEA/DOL/Census 13:30 UTC 25 Nov; Cairo 31/21 (CNN/Times);
  EU-Balkans (European Council); Trump-Rutte (Reuters/NATO); Gukesh Game 2
  draw 20 moves 1-1 (FIDE/Lichess); Cartagena freed 06:30 GMT (Reuters/CBS);
  Shenzhou docking 03:56 UTC (CMSA); Sandringham charges 25 Nov, break-in
  23 Nov (Norfolk Constabulary); B28 Donald 85 off 32 VERIFIED (Sky/Cricinfo);
  B31 EUR17.12bn VERIFIED (European Parliament); Netanyahu judges 25 Nov (CNN);
  Nepal M5.6 24 Nov (PTI/USGS); gold <$3,500 (FXStreet).
"""
import os
import sys
from collections import Counter

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MX = 24
CW = W - 2 * MX
PAPER = (255, 255, 255)
INK = (17, 17, 17)
MUTED = (91, 91, 91)
ACCENT = (30, 64, 175)          # the ONE accent: deep broadsheet blue
ACCENT_LT = (147, 197, 253)     # tint of the same hue, for dark bands
RULE = (203, 203, 203)
DARK = (17, 17, 17)
TAGC = {
    "CONFIRMED": (21, 128, 61),
    "OFFICIAL": ACCENT,
    "REPORTED": (146, 64, 14),
    "CLAIMED": (185, 28, 28),
}

FDIR = "/usr/share/fonts/truetype/dejavu"
LDIR = "/usr/share/fonts/truetype/liberation"


def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SERIF_I = lambda s: ImageFont.truetype(os.path.join(LDIR, "LiberationSerif-Italic.ttf"), s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
MONO = lambda s: font("DejaVuSansMono.ttf", s)
MONO_B = lambda s: font("DejaVuSansMono-Bold.ttf", s)
LIB_B = lambda s: ImageFont.truetype(os.path.join(LDIR, "LiberationSans-Bold.ttf"), s)
LIB = lambda s: ImageFont.truetype(os.path.join(LDIR, "LiberationSans-Regular.ttf"), s)

HERE = os.path.dirname(os.path.abspath(__file__))

NUMBERS = [
    ("4.3%", "US GDP, Q3 ann."),
    ("3.3%", "Core PCE, Oct YoY"),
    ("189K", "Jobless claims"),
    ("701K", "New-home sales"),
    ("4.9%", "Australia CPI, Oct"),
    ("31", "Killed, Cairo fire"),
    ("03:56", "Shenzhou-24 docking"),
    ("25/33", "Montenegro chapters"),
]

TIMELINE = ("00:18 Shenzhou lifts off  ·  03:56 Docking at Tiangong  ·  00:30 AU CPI 4.9%  ·  "
            "02:40 Seoul Metro deal  ·  06:30 Cartagena hostages freed  ·  10:43 Flinders warning  ·  "
            "13:30 US data: GDP 4.3%, PCE 3.3%  ·  15:00 Gukesh Game 2 drawn  ·  17:00 EU–Balkans deal  ·  "
            "evening Cairo fire, Trump–Rutte")

SUB = ("America runs hot: GDP 4.3%, inflation 3.3%  /  Shenzhou-24 docks with Pakistan's first "
       "astronaut  /  Solomons signs with Canberra, scraps China pact")

# tag: CONFIRMED / OFFICIAL / REPORTED / CLAIMED
HEROES = [
    dict(n=1, region="AMERICAS", place="WASHINGTON", date="TUE 25 NOV", illo="h2us",
         head="America runs hot: GDP jumps 4.3% as inflation sticks at 3.3%",
         body=("Q3 growth revised up from 3.4%, beating the 3.5% forecast; core PCE 3.3%, "
               "highest since Nov 2023. Claims 189K; new homes 701K."),
         src="BEA · DOL · Census", tag="CONFIRMED"),
    dict(n=2, region="EAST ASIA", place="JIUQUAN", date="TUE 25 NOV", illo="h1",
         head="Shenzhou-24 docks with Pakistan's first astronaut aboard",
         body=("Launched 00:18:52 UTC, docked 03:56 UTC. Ali, 40, first Pakistani in orbit "
               "and first foreign astronaut on Tiangong."),
         src="China Manned Space Agency", tag="CONFIRMED"),
    dict(n=3, region="OCEANIA", place="CANBERRA", date="TUE 25 NOV", illo="h3",
         head="Solomons signs treaty with Australia, scraps China pact",
         body=("Albanese and PM Wale signed in Canberra; China pact lapses Apr 2027."),
         src="Prime Minister of Australia", tag="CONFIRMED"),
]

MEDIUMS = [
    dict(n=4, region="MIDDLE EAST", place="RIYADH", date="MON 24 NOV", illo="m4",
         head="Houthi drone hits Riyadh tower",
         body="Drone hit the 385m PIF Tower. 11 wounded.",
         src="Reuters", tag="CONFIRMED"),
    dict(n=5, region="AMERICAS", place="NEW YORK", date="MON 24 NOV", illo="m5",
         head="Huawei guilty on 10 of 12 counts",
         body="Fraud, sanctions, trade secrets. Sentencing 2027.",
         src="US DOJ", tag="CONFIRMED"),
    dict(n=6, region="OCEANIA", place="FLINDERS ISLAND", date="TUE 25 NOV", illo="m6",
         head="Flinders fire: 'too late to leave'",
         body="Emergency Warning for three towns; ~3,000 ha.",
         src="Tasmania Fire Service", tag="OFFICIAL"),
    dict(n=7, region="EAST ASIA", place="SEOUL", date="TUE 25 NOV", illo="m7",
         head="Seoul Metro strike called off",
         body="Deal 02:40 KST: 2,212 cuts off, pay +3.5%.",
         src="Yonhap", tag="CONFIRMED"),
    dict(n=8, region="EAST ASIA", place="ULLEUNG", date="MON 24 NOV", illo="m8",
         head="Russian jets near Ulleung; shelter alert",
         body="Jets in KADIZ; fighters scrambled. Rare alert.",
         src="ROK Joint Chiefs", tag="REPORTED"),
    dict(n=9, region="MIDDLE EAST", place="BAGHDAD", date="TUE 25 NOV", illo="m9",
         head="Baghdad takes over Kurdish oilfields",
         body="Federal control of 4 provinces. Kurds object.",
         src="Reuters", tag="CONFIRMED"),
    dict(n=10, region="MIDDLE EAST", place="STRAIT OF HORMUZ", date="MON 24 NOV", illo="m10",
         head="Iran claims four tankers hit in Hormuz",
         body="IRGC claims 4 tankers hit mines. Unverified.",
         src="IRGC via Reuters", tag="CLAIMED"),
    dict(n=11, region="EUROPE", place="FINLAND", date="MON 24 NOV", illo="m11",
         head="Kyiv confirms it hit ship Sparta II",
         body="Zelenskiy confirmed the 21 Nov drone strike.",
         src="Bloomberg", tag="CONFIRMED"),
    dict(n=12, region="AMERICAS", place="WASHINGTON", date="TUE 25 NOV", illo="m12",
         head="CIA and ODNI hit by spy-network breach",
         body="Unclassified network breached; secrets safe.",
         src="NYT", tag="REPORTED"),
    dict(n=13, region="AMERICAS", place="NEW YORK", date="TUE 25 NOV", illo="m13",
         head="Wall Street whipsaws: Dow up, Nasdaq off",
         body="S&P −3.2% intraday, then pared. Yield 4.85%.",
         src="NYSE · Cboe", tag="CONFIRMED"),
    dict(n=14, region="AFRICA", place="CAIRO", date="TUE 25 NOV", illo="m14",
         head="Fuel tanker fire kills 31 in Cairo",
         body="Tanker overturned at Al-Warraq; 27 cars burned.",
         src="Egypt Health Ministry", tag="CONFIRMED"),
    dict(n=15, region="EUROPE", place="SANDRINGHAM", date="TUE 25 NOV", illo="m15",
         head="Two charged over Sandringham break-in",
         body="Doku, 34, and Ndoci, 32, in court 25 Nov.",
         src="Norfolk Constabulary", tag="CONFIRMED"),
]

# (n, place, region, head, summary)
BRIEFS = [
    (16, "TOKYO", "EAST ASIA", "Six parties move to censure Seki", "Fundraising scandal; won't quit."),
    (17, "BRUSSELS", "EUROPE", "EU–Balkans deal; Serbia stays away", "Declaration agreed; 25/33 chapters."),
    (18, "PALM BEACH", "AMERICAS", "Trump, Rutte: don't widen the war", "Joint statement after Mar-a-Lago."),
    (19, "GENEVA", "EUROPE", "Gukesh–Sindarov Game 2 drawn in 20", "London System; match level 1–1."),
    (20, "GLOBAL", "WORLD", "16 Days of Activism begins", "UN Women campaign to 10 Dec."),
    (21, "MADRID", "EUROPE", "Real Madrid 5–1 PSV", "Bellingham stunner, Mbappé brace."),
    (22, "CARTAGENA", "AMERICAS", "All hostages freed in Cartagena", "20 freed in raid; 1 killed, 4 held."),
    (23, "OTTAWA", "AMERICAS", "Astronaut Kutryk a father from orbit", "Crew-13's Kutryk welcomes a girl."),
    (24, "WASHINGTON", "AMERICAS", "Trump pardons Freedom and Feathers", "Turkey pardon, 2pm ET."),
    (25, "WASHINGTON", "AMERICAS", "Giuliani gets Medal of Freedom", "Ex-mayor honoured 24 Nov."),
    (26, "PARIS", "EUROPE", "Sarkozy corruption case goes to trial", "Pre-trial hearing 1 Apr 2027."),
    (27, "FORT HOOD", "AMERICAS", "Fort Hood shooter seeks stay", "Hasan killed 13 in 2009."),
    (28, "VILLAVICENCIO", "AMERICAS", "Car bomb rocks Villavicencio", "FARC dissidents blamed."),
    (29, "CARRARA", "OCEANIA", "Donald 85 off 32 seals England win", "England chase 185; series 1–1."),
    (30, "NEW DELHI", "SOUTH ASIA", "BJP, Akali Dal ally for Punjab 2027", "Reunited after six years."),
    (31, "TOKYO", "EAST ASIA", "Nikkei falls 2.8% at the open", "Advantest −12%; chip rout resumes."),
    (32, "STRASBOURG", "EUROPE", "MEPs seek €17.12bn for borders", "Ressler's bid: €17.12bn."),
    (33, "HODEIDAH", "MIDDLE EAST", "Saudi jets hit Hodeidah telecom site", "Houthi media: 4 killed, 18 hurt."),
    (34, "ADEN", "MIDDLE EAST", "Houthis 'won't seize Aden', army says", "Houthis said to be 60 km away."),
    (35, "BRUSSELS", "EUROPE", "EU leaders head for budget summit", "Special Council 26–27 Nov; €1.78tn."),
    (36, "JERUSALEM", "MIDDLE EAST", "Judges doubt Netanyahu cases", "Court urges dropping Case 4000."),
    (37, "TAPLEJUNG", "SOUTH ASIA", "M5.6 quake shakes east Nepal", "No casualties; felt in 5 countries."),
    (38, "GLOBAL", "WORLD", "COP31 ended with no deal — see below", "Climate summit closed 22 Nov."),
    (39, "GLOBAL", "WORLD", "Gold slips below $3,500", "Hot PCE lifts hike odds; gold −0.7%."),
]

DATE_CHECK_EXCLUDED = [
    "COP31 ends with no deal — 22 Nov, Antalya.",
    "ICJ: Myanmar guilty of Rohingya genocide — 19 Nov; UK recognised it 23 Nov.",
    "700,000 Russian troops dead — analysis published 23 Nov.",
    "Prabowo names two VP picks — 23 Nov, Jakarta.",
    "Sparta II attack itself — 21 Nov (confirmation in M11).",
    "Russian ship sunk off Benghazi — 22 Nov.",
    "Nepal PM's India visit ends — 23 Nov.",
    "KADIZ incident — 17 Nov (superseded by M8).",
    "Market falls 20–23 Nov — only the 25 Nov open in B31.",
    "Hodeidah airstrike — 23 Nov (context in B33).",
]
DATE_CHECK_DEMOTED = [
    "Gukesh–Sindarov Game 1: draw, 38 moves — 24 Nov (in B19).",
    "First PIF Tower strike — 19 Nov, no casualties (in M4).",
]

REGION_ORDER = ["EAST ASIA", "OCEANIA", "SOUTH ASIA", "EUROPE",
                "AMERICAS", "MIDDLE EAST", "AFRICA", "WORLD"]


def compute_regions():
    tally = Counter()
    for s in HEROES + MEDIUMS:
        tally[s["region"]] += 1
    for (_n, _p, r, _h, _s) in BRIEFS:
        tally[r] += 1
    total = sum(tally.values())
    assert total == len(HEROES) + len(MEDIUMS) + len(BRIEFS), (total, "tally != story count")
    assert set(tally) == set(REGION_ORDER), set(tally) ^ set(REGION_ORDER)
    return [(r, tally[r]) for r in REGION_ORDER], total


# ---------------------------------------------------------------- helpers
def wrap(text, fnt, width):
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
    s = size
    while s > min_size and make_font(s).getlength(text) > width:
        s -= 1
    return make_font(s)


def load_illo(key):
    p = os.path.join(HERE, "illos", key + ".png")
    im = Image.open(p).convert("RGB")
    assert im.size == (960, 240), (key, im.size)
    return im


def illo_crop(im, ratio):
    """Cover-crop to target ratio, never out of bounds (v1 bug: PIL filled
    out-of-bounds crop with BLACK). Horizontal crop when the slot is narrower
    than 4:1, centred vertical crop when wider."""
    w, h = im.size
    tw = int(h * ratio)
    if tw <= w:
        x0 = (w - tw) // 2
        return im.crop((x0, 0, x0 + tw, h))
    th = int(w / ratio)
    y0 = (h - th) // 2
    return im.crop((0, y0, w, y0 + th))


def draw_card(d, img, x0, y, w, h, illo_h, s, head_size, body_size,
              body_lines, head_serif=False, defects=None):
    """One illustrated story card. The illo band height is derived from the
    card height minus the text block, so body text can never run into the
    source line (v1/v2-draft bug). Narrow cards get a short dateline
    (number + place); the date moves to the source line."""
    text_h = 4 + 13 + 2 * (head_size + 2) + body_lines * (body_size + 2) + 12
    illo_h = h - text_h
    if illo_h < 28 and defects is not None:
        defects.append(f"card {s['n']} illo band only {illo_h}px")
    d.rectangle([x0, y, x0 + w, y + h], outline=RULE, width=1)
    im = load_illo(s["illo"])
    slot = illo_crop(im, w / illo_h).resize((w, illo_h), Image.LANCZOS)
    img.paste(slot, (x0, y))
    ty = y + illo_h + 4
    narrow = w < 200
    kick = f"{s['n']} · {s['place']}" if narrow else f"{s['n']} · {s['place']} · {s['date']}"
    fk = MONO_B(8)
    d.text((x0 + 8, ty), kick, fill=ACCENT, font=fk)
    tag = s["tag"]
    tw = fk.getlength(tag)
    if fk.getlength(kick) + tw + 20 > w and defects is not None:
        defects.append(f"card {s['n']} dateline+tag too wide")
    d.text((x0 + w - tw - 8, ty), tag, fill=TAGC[tag], font=fk)
    ty += 13
    hf = SERIF_B(head_size) if head_serif else SANS_B(head_size)
    hl = wrap(s["head"], hf, w - 16)
    if len(hl) > 2 and defects is not None:
        defects.append(f"card {s['n']} headline {len(hl)} lines")
    for ln in hl[:2]:
        d.text((x0 + 8, ty), ln, fill=INK, font=hf)
        ty += head_size + 2
    bl = wrap(s["body"], SANS(body_size), w - 16)
    if len(bl) > body_lines and defects is not None:
        defects.append(f"card {s['n']} body {len(bl)} lines > {body_lines}")
    for ln in bl[:body_lines]:
        d.text((x0 + 8, ty), ln, fill=(55, 65, 81), font=SANS(body_size))
        ty += body_size + 2
    # source, bottom, 6px clear of the card edge (v1 clipped it); narrow
    # cards carry the date here.
    src = s["src"].upper() if not narrow else f"{s['src']} · {s['date']}".upper()
    d.text((x0 + 8, y + h - 12), src, fill=MUTED, font=MONO(7))
    return ty


# ---------------------------------------------------------------- sections
def draw_header(d, y):
    regions, total = compute_regions()
    eyebrow = (f"{total} STORIES  ·  {len(regions)} REGIONS  ·  ALL TIMES UTC  ·  "
               "EVERY STORY DATED BY ITS EVENT")
    d.text((MX, y), eyebrow, fill=ACCENT, font=MONO_B(10))
    d.text((W - MX - MONO_B(10).getlength("THE WORLD IN ONE PAGE"), y),
           "THE WORLD IN ONE PAGE", fill=MUTED, font=MONO_B(10))
    y += 14
    d.line([(MX, y), (W - MX, y)], fill=INK, width=2)
    y += 3
    f_mast = fit_font("WEDNESDAY, 25 NOVEMBER 2026", SERIF_B, 38, CW)
    d.text((MX, y), "WEDNESDAY, 25 NOVEMBER 2026", fill=INK, font=f_mast)
    y += 38
    d.line([(MX, y), (W - MX, y)], fill=INK, width=2)
    y += 5
    f_sub = fit_font(SUB, SERIF_I, 13, CW)
    d.text((MX, y), SUB, fill=INK, font=f_sub)
    y += 16
    # region bar: ONE accent, segments split by white gaps
    seg_w = CW // len(regions)
    for i, (name, cnt) in enumerate(regions):
        x0 = MX + i * seg_w
        x1 = MX + (i + 1) * seg_w if i < len(regions) - 1 else W - MX
        d.rectangle([x0, y, x1 - 2, y + 18], fill=ACCENT)
        lab = f"{name} {cnt}"
        f_lab = MONO_B(9)
        tw = f_lab.getlength(lab)
        d.text((x0 + (x1 - x0 - tw) / 2, y + 4), lab, fill=(255, 255, 255), font=f_lab)
    y += 20
    f_tl = fit_font(TIMELINE, SANS, 10, CW)
    d.text((MX, y), TIMELINE, fill=MUTED, font=f_tl)
    y += 12
    # THE DAY IN NUMBERS — dark band, numbers in a tint of the accent
    d.rectangle([MX, y, W - MX, y + 42], fill=DARK)
    d.text((MX + 10, y + 14), "THE DAY\nIN NUMBERS", fill=(255, 255, 255), font=MONO_B(9))
    cell_w = (CW - 170) // 8
    x = MX + 170
    for num, lab in NUMBERS:
        f_num = fit_font(num, SANS_B, 17, cell_w - 8)
        d.text((x, y + 4), num, fill=ACCENT_LT, font=f_num)
        for j, ln in enumerate(wrap(lab, SANS(8), cell_w - 8)):
            d.text((x, y + 25 + j * 9), ln, fill=(209, 213, 219), font=SANS(8))
        x += cell_w
    y += 46
    return y


def draw_mediums(d, img, y, med_h, defects):
    MED_W = (CW - 5 * 8) // 6
    for row in range(2):
        for c in range(6):
            s = MEDIUMS[row * 6 + c]
            x0 = MX + c * (MED_W + 8)
            yy = y + row * (med_h + 6)
            draw_card(d, img, x0, yy, MED_W, med_h, 48, s, 11, 10, 2, defects=defects)
    return y + 2 * med_h + 6


def draw_briefs(d, y, row_h=20):
    d.text((MX, y), "THE REST OF THE DAY", fill=INK, font=MONO_B(10))
    y += 13
    COL_W = (CW - 3 * 12) // 4
    defects = []
    for i, (n, place, region, head, summ) in enumerate(BRIEFS):
        r, c = divmod(i, 4)
        x0 = MX + c * (COL_W + 12)
        yy = y + r * row_h
        l1 = wrap(head, LIB_B(10), COL_W)
        if len(l1) > 1:
            defects.append(f"brief {n} headline wraps: {head}")
        d.text((x0, yy), l1[0], fill=INK, font=LIB_B(10))
        line2 = f"{n} · {place} — {summ}"
        l2 = wrap(line2, LIB(9), COL_W)
        if len(l2) > 1:
            defects.append(f"brief {n} line2 wraps: {line2}")
        d.text((x0, yy + 11), l2[0], fill=MUTED, font=LIB(9))
    return y + 6 * row_h, defects


def draw_map_dc(d, img, y, map_h, map_file="map_panel.png", defects=None):
    mp = Image.open(os.path.join(HERE, map_file)).convert("RGB")
    img.paste(mp.resize((470, map_h), Image.LANCZOS), (MX, y))
    d.text((MX, y + map_h - 13), "WORLD MAP — PIN = STORY NUMBER", fill=MUTED, font=MONO(7))
    dx = MX + 470 + 8
    d.rectangle([dx, y, W - MX, y + map_h], outline=RULE, width=1)
    d.text((dx + 8, y + 5), "DATE CHECK — WHY THESE ARE NOT IN TODAY'S NEWS",
           fill=ACCENT, font=MONO_B(8))
    d.line([(dx + 8, y + 17), (W - MX - 8, y + 17)], fill=RULE, width=1)
    ty = y + 21
    d.text((dx + 8, ty), "EXCLUDED — TOO OLD (≥36 HOURS BEFORE 25 NOV 02:00 UTC)",
           fill=MUTED, font=MONO_B(7))
    ty += 11
    for it in DATE_CHECK_EXCLUDED:
        d.text((dx + 8, ty), "·  " + it, fill=(55, 65, 81), font=SANS(8))
        ty += 9
    ty += 1
    d.text((dx + 8, ty), "DEMOTED — FOLDED INTO A LIVE STORY",
           fill=MUTED, font=MONO_B(7))
    ty += 11
    for it in DATE_CHECK_DEMOTED:
        d.text((dx + 8, ty), "·  " + it, fill=(55, 65, 81), font=SANS(8))
        ty += 9
    if ty > y + map_h - 4 and defects is not None:
        defects.append(f"DATE CHECK overflows by {ty - (y + map_h - 4):.0f}px")
    return y + map_h


def draw_datecheck_full(d, y, h, defects=None):
    """Full-width DATE CHECK (direction C): three columns."""
    d.rectangle([MX, y, W - MX, y + h], outline=RULE, width=1)
    d.text((MX + 8, y + 5), "DATE CHECK — WHY THESE ARE NOT IN TODAY'S NEWS",
           fill=ACCENT, font=MONO_B(8))
    ty = y + 20
    col_w = (CW - 16) // 3
    d.text((MX + 8, ty), "EXCLUDED — TOO OLD (≥36 HOURS)",
           fill=MUTED, font=MONO_B(7))
    ty += 11
    for it in DATE_CHECK_EXCLUDED[:5]:
        d.text((MX + 8, ty), "·  " + it, fill=(55, 65, 81), font=SANS(8))
        ty += 10
    ty2 = y + 20
    d.text((MX + 8 + col_w, ty2), "EXCLUDED (CONT.)",
           fill=MUTED, font=MONO_B(7))
    ty2 += 11
    for it in DATE_CHECK_EXCLUDED[5:]:
        d.text((MX + 8 + col_w, ty2), "·  " + it, fill=(55, 65, 81), font=SANS(8))
        ty2 += 10
    ty3 = y + 20
    d.text((MX + 8 + 2 * col_w, ty3), "DEMOTED — FOLDED INTO A LIVE STORY",
           fill=MUTED, font=MONO_B(7))
    ty3 += 11
    for it in DATE_CHECK_DEMOTED:
        d.text((MX + 8 + 2 * col_w, ty3), "·  " + it, fill=(55, 65, 81), font=SANS(8))
        ty3 += 10
    if max(ty, ty2, ty3) > y + h - 4 and defects is not None:
        defects.append("DATE CHECK full-width overflows")
    return y + h


def draw_footer(d, y):
    d.line([(MX, y), (W - MX, y)], fill=RULE, width=1)
    y += 5
    foot1 = ("HOW SURE:  CONFIRMED = verified by 2+ sources or official  ·  OFFICIAL = agency "
             "statement  ·  REPORTED = 1+ major outlet  ·  CLAIMED = one party, unverified")
    d.text((MX, y), foot1, fill=MUTED, font=fit_font(foot1, SANS, 8, CW))
    y += 11
    foot2 = ("All times UTC  ·  Every story dated by its event, not the article date  ·  "
             "Illustrations are original flat-vector drawings  ·  Sources named on each story  ·  "
             "News-25 · 25 November 2026")
    d.text((MX, y), foot2, fill=MUTED, font=fit_font(foot2, SANS, 8, CW))
    return y + 12


# ---------------------------------------------------------------- directions
def heroes_a(d, img, y, defects):
    """A: wide hero left (640), two heroes stacked right (328)."""
    H1_W, R_W = 640, 328
    HH = 240
    draw_card(d, img, MX, y, H1_W, HH, 140, HEROES[0], 18, 11, 2,
              head_serif=True, defects=defects)
    rh = (HH - 6) // 2
    draw_card(d, img, MX + H1_W + 8, y, R_W, rh, 40, HEROES[1], 13, 10, 2, defects=defects)
    draw_card(d, img, MX + H1_W + 8, y + rh + 6, R_W, rh, 40, HEROES[2], 13, 10, 2, defects=defects)
    return y + HH


def heroes_b(d, img, y, defects):
    """B: giant split hero (illo left + giant number/type right), then two strips."""
    s = HEROES[0]
    HH = 148
    d.rectangle([MX, y, W - MX, y + HH], outline=RULE, width=1)
    im = load_illo(s["illo"])
    slot = illo_crop(im, 592 / HH).resize((592, HH), Image.LANCZOS)
    img.paste(slot, (MX, y))
    tx = MX + 592 + 12
    tw = W - MX - tx
    ty = y + 8
    d.text((tx, ty), f"1 · {s['place']} · {s['date']}", fill=ACCENT, font=MONO_B(9))
    d.text((tx + tw - MONO_B(9).getlength(s["tag"]), ty), s["tag"],
           fill=TAGC[s["tag"]], font=MONO_B(9))
    ty += 14
    d.text((tx, ty), "4.3%", fill=ACCENT, font=SERIF_B(42))
    ty += 46
    hl = wrap(s["head"], SERIF_B(16), tw - 8)
    for ln in hl[:2]:
        d.text((tx, ty), ln, fill=INK, font=SERIF_B(16))
        ty += 18
    bl = wrap(s["body"], SANS(10), tw - 8)
    for ln in bl[:3]:
        d.text((tx, ty), ln, fill=(55, 65, 81), font=SANS(10))
        ty += 12
    d.text((tx, y + HH - 12), s["src"].upper(), fill=MUTED, font=MONO(7))
    y += HH + 6
    HH2 = 120
    for i, s in enumerate(HEROES[1:]):
        x0 = MX + i * (484 + 8)
        draw_card(d, img, x0, y, 484, HH2, 50, s, 13, 10, 2, defects=defects)
    return y + HH2


def heroes_c(d, img, y, defects):
    """C: cinematic band — three heroes in a row, tall native-ratio illos."""
    HW = (CW - 16) // 3
    HH = 176
    for i, s in enumerate(HEROES):
        x0 = MX + i * (HW + 8)
        draw_card(d, img, x0, y, HW, HH, 80, s, 14, 10, 3,
                  head_serif=True, defects=defects)
    return y + HH


def build(direction, out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    defects = []
    y = 10
    y = draw_header(d, y) + 5
    if direction == "A":
        y = heroes_a(d, img, y, defects) + 5
        y = draw_mediums(d, img, y, 124, defects) + 5
        y = draw_map_dc(d, img, y, 168, defects=defects) + 5
        y, _bd = draw_briefs(d, y, row_h=20); defects += _bd; y += 5
    elif direction == "B":
        y = heroes_b(d, img, y, defects) + 5
        y = draw_mediums(d, img, y, 116, defects) + 5
        y = draw_map_dc(d, img, y, 160, defects=defects) + 5
        y, _bd = draw_briefs(d, y, row_h=20); defects += _bd; y += 5
    elif direction == "C":
        mp = Image.open(os.path.join(HERE, "map_panel_wide.png")).convert("RGB")
        img.paste(mp.resize((CW, 150), Image.LANCZOS), (MX, y))
        d.text((MX, y + 150 - 13), "WORLD MAP — PIN = STORY NUMBER", fill=MUTED, font=MONO(7))
        y += 150 + 5
        y = heroes_c(d, img, y, defects) + 5
        y = draw_mediums(d, img, y, 124, defects) + 5
        y = draw_datecheck_full(d, y, 86, defects=defects) + 5
        y, _bd = draw_briefs(d, y, row_h=20); defects += _bd; y += 5
    else:
        raise ValueError(direction)
    y = draw_footer(d, y)
    img.save(out_path, optimize=True)
    size = os.path.getsize(out_path)
    print(f"[{direction}] saved {out_path}: {img.size}, {size} bytes ({size/1024:.0f} KiB), final y={y}")
    print(f"[{direction}] 1 MiB gate: {'PASS' if size <= 1048576 else 'FAIL'}; "
          f"1024x1024 gate: {'PASS' if img.size == (1024, 1024) else 'FAIL'}; "
          f"overflow: {'FAIL y>1024' if y > 1024 else 'PASS'}")
    if defects:
        print(f"[{direction}] DEFECTS ({len(defects)}):")
        for df in defects:
            print("  -", df)
    else:
        print(f"[{direction}] DEFECTS: 0")
    return defects, y


if __name__ == "__main__":
    direction = sys.argv[1] if len(sys.argv) > 1 else "A"
    out = sys.argv[2] if len(sys.argv) > 2 else f"entry-dir-{direction.lower()}.png"
    build(direction, out)
