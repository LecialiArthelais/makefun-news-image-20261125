#!/usr/bin/env python3
"""
Flat-vector illustration scenes for News-25 (build time only).

Style: illustration-flat (flat fills, no outlines on big shapes, thin
white fold strokes only where noted, palette navy/lavender/indigo/
yellow/coral/mint; no gradients, no shadows, no ground lines).
Every scene is a wide strip, viewBox 0 0 480 120, composed centre-safe
(the middle 75% holds the subject; the page crops the sides for the
3:1 medium slots). Rendered to PNG with the skill's render.mjs
(playwright + Chromium) at 2x, then placed by build_page.py.

Run:  python3 illos.py            # writes illos/*.svg
      (render with render.mjs, see build_page.py)
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "illos")

NAVY = "#011B5C"
LAV = "#9E91E1"
IND = "#6A6CEB"
YEL = "#FEC600"
CORAL = "#FF7F91"
MINT = "#93D7D5"
SKIN = "#FD9999"
WHITE = "#FFFFFF"
PLAV = "#CDC6EF"
PLAV2 = "#E4E0F7"
TAPE = "#FFE58A"
RED = "#FF6378"
ACCENT = "#DC2626"
INK = "#111827"
SKY = "#DCE9F5"
STEEL = "#8FA8BF"


def svg(body, bg, s=1.3):
    # v2: scale the scene ~1.3x about its centre so the subject fills the
    # frame (v1 subjects were small in a sea of empty sky). Background stays
    # full-bleed; edge elements may crop slightly, which is fine.
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="120" '
        f'viewBox="0 0 480 120">'
        f'<rect x="0" y="0" width="480" height="120" fill="{bg}"/>'
        f'<g transform="translate(240 60) scale({s}) translate(-240 -60)">{body}</g></svg>'
    )


def rect(x, y, w, h, fill, rx=0):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}"/>')


def circ(cx, cy, r, fill):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'


def poly(points, fill):
    p = " ".join(f"{x},{y}" for x, y in points)
    return f'<polygon points="{p}" fill="{fill}"/>'


def stars(n, seed=7, fill=WHITE):
    out = []
    x, y = 13, 11
    for i in range(n):
        x = (x * 37 + 91) % 460 + 10
        y = (y * 53 + 29) % 70 + 8
        r = 1.2 + (i % 3) * 0.5
        out.append(circ(x, y, r, fill))
    return "".join(out)


# ---------------------------------------------------------------- H1 rocket
def h1_shenzhou():
    b = []
    b.append(stars(14))
    # earth arc, bottom
    b.append(f'<circle cx="240" cy="190" r="92" fill="{IND}"/>')
    b.append(f'<circle cx="240" cy="190" r="92" fill="none" stroke="{MINT}" stroke-width="3"/>')
    # Tiangong station, top right
    b.append(rect(352, 22, 66, 10, WHITE, 2))
    b.append(rect(352, 22, 66, 10, "none"))
    b.append(rect(330, 26, 22, 3, IND))
    b.append(rect(418, 26, 22, 3, IND))
    b.append(rect(380, 14, 10, 26, LAV, 2))
    b.append(circ(385, 27, 3, YEL))
    # rocket, centre-left, diagonal
    b.append(poly([(168, 96), (196, 40), (224, 96)], WHITE))
    b.append(poly([(196, 40), (210, 66), (196, 62)], CORAL))
    b.append(rect(176, 62, 40, 30, WHITE))
    b.append(rect(176, 62, 40, 30, "none"))
    b.append(rect(184, 70, 24, 12, IND, 2))
    b.append(circ(196, 52, 5, SKY))
    b.append(poly([(176, 92), (162, 108), (176, 104)], CORAL))
    b.append(poly([(216, 92), (230, 108), (216, 104)], CORAL))
    # flame
    b.append(poly([(184, 96), (196, 118), (208, 96)], YEL))
    b.append(poly([(190, 96), (196, 112), (202, 96)], "#FF8A00"))
    # launch smoke
    b.append(circ(150, 108, 10, PLAV2))
    b.append(circ(240, 110, 12, PLAV2))
    b.append(circ(120, 112, 8, PLAV2))
    return svg("".join(b), NAVY)


# ---------------------------------------------------------------- H2 CPI bars
def h2_cpi():
    b = []
    # rising bars
    b.append(rect(120, 78, 34, 32, MINT))
    b.append(rect(168, 62, 34, 48, LAV))
    b.append(rect(216, 44, 34, 66, YEL))
    b.append(rect(264, 24, 34, 86, CORAL))
    b.append(rect(312, 8, 34, 102, ACCENT))
    # white fold lines on bars
    for x in (120, 168, 216, 264, 312):
        b.append(f'<line x1="{x+6}" y1="104" x2="{x+28}" y2="104" stroke="{WHITE}" stroke-width="1.4" stroke-linecap="round"/>')
    # arrow up
    b.append(f'<line x1="128" y1="66" x2="322" y2="10" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>')
    b.append(poly([(322, 4), (350, 10), (326, 24)], NAVY))
    # coins
    b.append(circ(392, 88, 16, YEL))
    b.append(circ(392, 88, 11, "none"))
    b.append(circ(420, 98, 12, YEL))
    b.append(circ(420, 98, 8, "none"))
    # petrol pump, left
    b.append(rect(52, 40, 34, 70, NAVY, 4))
    b.append(rect(58, 48, 22, 18, WHITE, 2))
    b.append(rect(62, 74, 14, 8, RED, 1))
    b.append(rect(86, 56, 6, 22, NAVY))
    return svg("".join(b), "#F4EFE6")


# ---------------------------------------------------------------- H3 treaty
def h3_treaty():
    b = []
    # ocean wave, bottom
    b.append(f'<path d="M0 96 Q60 84 120 96 T240 96 T360 96 T480 96 V120 H0 Z" fill="{MINT}"/>')
    b.append(f'<path d="M0 106 Q60 96 120 106 T240 106 T360 106 T480 106 V120 H0 Z" fill="{IND}"/>')
    # flag poles
    b.append(rect(58, 16, 4, 84, NAVY))
    b.append(rect(322, 16, 4, 84, NAVY))
    # Australia flag: navy field, simplified Union canton, Southern Cross
    b.append(rect(62, 16, 100, 52, NAVY))
    b.append(rect(62, 16, 48, 26, WHITE))
    b.append(f'<line x1="62" y1="16" x2="110" y2="42" stroke="{CORAL}" stroke-width="4"/>')
    b.append(f'<line x1="110" y1="16" x2="62" y2="42" stroke="{CORAL}" stroke-width="4"/>')
    b.append(f'<line x1="86" y1="16" x2="86" y2="42" stroke="{CORAL}" stroke-width="4"/>')
    b.append(f'<line x1="62" y1="29" x2="110" y2="29" stroke="{CORAL}" stroke-width="4"/>')
    b.append(poly([(138, 44), (141, 52), (149, 52), (143, 57), (145, 65), (138, 60), (131, 65), (133, 57), (127, 52), (135, 52)], WHITE))
    for sx, sy in ((148, 26), (152, 36), (144, 58), (154, 56)):
        b.append(circ(sx, sy, 2, WHITE))
    # Solomons flag: blue top, green bottom, yellow diagonal, stars
    b.append(rect(326, 16, 100, 52, "#1E5AA8"))
    b.append(poly([(326, 68), (426, 16), (426, 68)], "#2E9E5B"))
    b.append(poly([(326, 62), (426, 16), (426, 24), (326, 68)], YEL))
    for sx, sy in ((344, 28), (358, 24), (350, 38), (364, 32)):
        b.append(circ(sx, sy, 2, WHITE))
    # treaty document + seal, centre
    b.append(rect(212, 46, 56, 54, WHITE))
    b.append(f'<rect x="212" y="46" width="56" height="54" fill="none" stroke="{NAVY}" stroke-width="1.5"/>')
    b.append(f'<line x1="220" y1="58" x2="260" y2="58" stroke="{NAVY}" stroke-width="1.5"/>')
    b.append(f'<line x1="220" y1="68" x2="260" y2="68" stroke="{NAVY}" stroke-width="1.5"/>')
    b.append(f'<line x1="220" y1="78" x2="248" y2="78" stroke="{NAVY}" stroke-width="1.5"/>')
    b.append(circ(258, 90, 7, ACCENT))
    return svg("".join(b), SKY)


# ---------------------------------------------------------------- M4 tower
def m4_tower():
    b = []
    b.append(stars(10))
    # PIF tower
    b.append(poly([(196, 118), (204, 12), (236, 12), (244, 118)], IND))
    b.append(poly([(204, 12), (220, 2), (236, 12)], LAV))
    for wy in (28, 44, 60, 76, 92):
        b.append(rect(210, wy, 20, 6, YEL))
    b.append(rect(206, 20, 28, 4, WHITE))
    # smoke plume
    b.append(circ(250, 30, 12, PLAV))
    b.append(circ(264, 22, 9, PLAV2))
    b.append(circ(276, 32, 7, PLAV))
    # drone
    b.append(circ(330, 30, 3, INK))
    b.append(rect(318, 28, 24, 2, INK))
    b.append(circ(318, 26, 2, CORAL))
    b.append(circ(342, 26, 2, CORAL))
    # city lights, bottom
    for bx in (60, 110, 300, 350, 400):
        b.append(rect(bx, 96, 26, 24, NAVY))
        b.append(rect(bx + 5, 100, 4, 4, YEL))
        b.append(rect(bx + 16, 108, 4, 4, YEL))
    return svg("".join(b), "#101736")


# ---------------------------------------------------------------- M5 court+chip
def m5_court():
    b = []
    # courthouse: pediment + oculus + columns + steps
    b.append(poly([(96, 92), (220, 36), (344, 92)], WHITE))
    b.append(f'<polyline points="96,92 220,36 344,92" fill="none" stroke="{NAVY}" stroke-width="1.5"/>')
    for cx in (126, 168, 210, 252, 294):
        b.append(rect(cx - 7, 58, 14, 34, WHITE))
        b.append(f'<rect x="{cx-7}" y="58" width="14" height="34" fill="none" stroke="{NAVY}" stroke-width="1.2"/>')
    b.append(rect(96, 92, 248, 8, NAVY))
    b.append(rect(88, 100, 264, 8, NAVY))
    b.append(rect(80, 108, 280, 8, "#5A5A5A"))
    # chip, right
    b.append(rect(372, 34, 62, 62, NAVY, 4))
    b.append(rect(388, 50, 30, 30, IND, 2))
    b.append(circ(403, 65, 7, YEL))
    for px in (382, 398, 414):
        b.append(rect(px, 26, 4, 8, NAVY))
        b.append(rect(px, 96, 4, 8, NAVY))
    for py in (44, 60, 76):
        b.append(rect(364, py, 8, 4, NAVY))
        b.append(rect(434, py, 8, 4, NAVY))
    return svg("".join(b), "#EDE7DA")


# ---------------------------------------------------------------- M6 fire
def m6_fire():
    b = []
    # sky + sun
    b.append(circ(400, 26, 16, YEL))
    # coast silhouette
    b.append(poly([(0, 118), (0, 96), (90, 88), (180, 98), (260, 90), (340, 100), (480, 92), (480, 118)], "#2E5B3E"))
    # flames
    for fx, fh, col in ((120, 52, "#FF8A00"), (150, 66, RED), (185, 46, "#FF8A00"),
                        (220, 60, RED), (255, 44, "#FF8A00"), (290, 56, RED)):
        b.append(poly([(fx - 14, 108), (fx, 108 - fh), (fx + 14, 108)], col))
        b.append(poly([(fx - 6, 108), (fx, 108 - fh + 16), (fx + 6, 108)], YEL))
    # smoke
    b.append(circ(180, 30, 12, PLAV))
    b.append(circ(205, 22, 9, PLAV2))
    b.append(circ(235, 32, 10, PLAV))
    # evacuation sign
    b.append(poly([(392, 92), (408, 66), (424, 92)], WHITE))
    b.append(poly([(392, 92), (408, 66), (424, 92)], "none"))
    b.append(f'<line x1="408" y1="74" x2="408" y2="84" stroke="{ACCENT}" stroke-width="2.4" stroke-linecap="round"/>')
    b.append(circ(408, 89, 1.6, ACCENT))
    return svg("".join(b), "#F7E8D8")


# ---------------------------------------------------------------- M7 metro
def m7_metro():
    b = []
    # sunrise
    b.append(circ(90, 40, 18, YEL))
    b.append(f'<rect x="0" y="96" width="480" height="24" fill="{NAVY}"/>')
    # rails
    b.append(f'<line x1="0" y1="104" x2="480" y2="104" stroke="{WHITE}" stroke-width="2"/>')
    b.append(f'<line x1="0" y1="112" x2="480" y2="112" stroke="{WHITE}" stroke-width="2"/>')
    # train
    b.append(rect(150, 44, 220, 56, MINT, 10))
    b.append(rect(150, 44, 220, 56, "none"))
    b.append(rect(160, 54, 200, 22, WHITE, 4))
    b.append(rect(160, 54, 64, 22, IND, 4))
    b.append(rect(232, 54, 64, 22, SKY, 4))
    b.append(rect(304, 54, 56, 22, SKY, 4))
    b.append(circ(180, 90, 5, YEL))
    b.append(circ(340, 90, 5, YEL))
    # clock 02:40
    b.append(circ(410, 40, 18, WHITE))
    b.append(f'<circle cx="410" cy="40" r="18" fill="none" stroke="{NAVY}" stroke-width="1.5"/>')
    b.append(f'<line x1="410" y1="40" x2="410" y2="28" stroke="{NAVY}" stroke-width="2" stroke-linecap="round"/>')
    b.append(f'<line x1="410" y1="40" x2="398" y2="44" stroke="{NAVY}" stroke-width="2" stroke-linecap="round"/>')
    return svg("".join(b), "#EAF2F8")


# ---------------------------------------------------------------- M8 jets
def m8_jets():
    b = []
    # ADIZ dashed line
    b.append(f'<line x1="60" y1="92" x2="430" y2="92" stroke="{ACCENT}" stroke-width="1.6" stroke-dasharray="7 5"/>')
    # island with peak + shore
    b.append(poly([(150, 118), (180, 92), (240, 80), (300, 94), (330, 118)], "#3E7A4E"))
    b.append(poly([(228, 84), (242, 68), (256, 84)], "#2E5B3E"))
    b.append(f'<line x1="150" y1="112" x2="330" y2="112" stroke="{WHITE}" stroke-width="2"/>')
    # jets, bigger
    for jx, jy in ((90, 30), (170, 16)):
        b.append(poly([(jx, jy), (jx + 58, jy + 9), (jx, jy + 18)], NAVY))
        b.append(poly([(jx + 14, jy + 3), (jx + 28, jy - 10), (jx + 34, jy + 6)], NAVY))
        b.append(poly([(jx + 14, jy + 15), (jx + 28, jy + 28), (jx + 34, jy + 12)], NAVY))
        b.append(circ(jx + 52, jy + 9, 2.5, CORAL))
    # warning triangle, bigger
    b.append(poly([(396, 58), (414, 24), (432, 58)], YEL))
    b.append(f'<line x1="414" y1="34" x2="414" y2="48" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    b.append(circ(414, 53, 2, INK))
    return svg("".join(b), SKY)


# ---------------------------------------------------------------- M9 pumpjack
def m9_oil():
    b = []
    # sun + desert
    b.append(circ(420, 28, 18, YEL))
    b.append(f'<rect x="0" y="88" width="480" height="32" fill="{TAPE}"/>')
    b.append(f'<path d="M0 88 Q120 78 240 88 T480 88 V120 H0 Z" fill="#E8C86A"/>')
    # derrick
    b.append(poly([(330, 88), (346, 18), (362, 88)], NAVY))
    b.append(f'<line x1="337" y1="64" x2="355" y2="64" stroke="{TAPE}" stroke-width="2"/>')
    b.append(f'<line x1="340" y1="42" x2="352" y2="42" stroke="{TAPE}" stroke-width="2"/>')
    # pumpjack, bigger
    b.append(poly([(96, 88), (140, 28), (184, 88)], NAVY))
    b.append(poly([(140, 30), (252, 22), (252, 32), (140, 40)], CORAL))
    b.append(circ(140, 30, 8, YEL))
    b.append(f'<line x1="252" y1="27" x2="252" y2="88" stroke="{NAVY}" stroke-width="4"/>')
    b.append(rect(242, 82, 20, 10, NAVY))
    b.append(poly([(100, 88), (140, 28), (140, 40), (112, 88)], "#24356E"))
    # oil drop
    b.append(poly([(292, 62), (304, 82), (280, 82)], INK))
    b.append(circ(292, 76, 10, INK))
    return svg("".join(b), "#F4E9D2")


# ---------------------------------------------------------------- M10 tanker
def m10_tanker():
    b = []
    # strait cliffs
    b.append(poly([(0, 0), (70, 0), (50, 118), (0, 118)], "#7A6A58"))
    b.append(poly([(480, 0), (410, 0), (430, 118), (480, 118)], "#7A6A58"))
    # sea
    b.append(f'<rect x="60" y="70" width="360" height="50" fill="{IND}"/>')
    b.append(f'<path d="M60 78 Q120 72 180 78 T300 78 T420 78" fill="none" stroke="{WHITE}" stroke-width="1.6"/>')
    b.append(f'<path d="M60 96 Q120 90 180 96 T300 96 T420 96" fill="none" stroke="{WHITE}" stroke-width="1.6"/>')
    # tanker
    b.append(rect(150, 62, 180, 26, CORAL))
    b.append(rect(300, 44, 30, 18, WHITE))
    b.append(rect(306, 48, 6, 6, NAVY))
    b.append(rect(150, 62, 180, 6, RED))
    b.append(rect(160, 30, 10, 32, NAVY))
    # fire + smoke on tanker
    b.append(poly([(196, 62), (206, 34), (216, 62)], YEL))
    b.append(poly([(202, 62), (206, 46), (210, 62)], "#FF8A00"))
    b.append(circ(206, 26, 9, PLAV))
    b.append(circ(218, 20, 6, PLAV2))
    # sea mine
    b.append(circ(380, 100, 8, NAVY))
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        b.append(f'<line x1="{380 + 7 * math.cos(a):.1f}" y1="{100 + 7 * math.sin(a):.1f}" '
                 f'x2="{380 + 12 * math.cos(a):.1f}" y2="{100 + 12 * math.sin(a):.1f}" '
                 f'stroke="{NAVY}" stroke-width="2" stroke-linecap="round"/>')
    return svg("".join(b), "#DCE9F5")


# ---------------------------------------------------------------- M11 ship
def m11_ship():
    b = []
    # cold sea + ice
    b.append(f'<rect x="0" y="66" width="480" height="54" fill="{STEEL}"/>')
    b.append(f'<path d="M0 76 Q80 70 160 76 T320 76 T480 76" fill="none" stroke="{WHITE}" stroke-width="1.6"/>')
    b.append(f'<path d="M0 96 Q80 90 160 96 T320 96 T480 96" fill="none" stroke="{WHITE}" stroke-width="1.6"/>')
    b.append(poly([(60, 100), (90, 92), (120, 100)], WHITE))
    b.append(poly([(380, 104), (410, 96), (440, 104)], WHITE))
    # cargo ship
    b.append(rect(150, 58, 190, 22, NAVY))
    b.append(rect(150, 58, 190, 5, RED))
    b.append(rect(300, 34, 40, 24, WHITE))
    b.append(rect(306, 38, 8, 6, NAVY))
    b.append(rect(322, 38, 8, 6, NAVY))
    # containers
    b.append(rect(170, 40, 30, 18, CORAL))
    b.append(rect(204, 40, 30, 18, YEL))
    b.append(rect(238, 40, 30, 18, MINT))
    # fire + smoke
    b.append(poly([(246, 58), (254, 32), (262, 58)], YEL))
    b.append(poly([(250, 58), (254, 44), (258, 58)], "#FF8A00"))
    b.append(circ(254, 24, 9, PLAV))
    b.append(circ(266, 18, 6, PLAV2))
    # drone
    b.append(circ(400, 26, 3, INK))
    b.append(rect(388, 24, 24, 2, INK))
    b.append(circ(388, 22, 2, CORAL))
    b.append(circ(412, 22, 2, CORAL))
    return svg("".join(b), "#C7D6E2")


# ---------------------------------------------------------------- M12 breach
def m12_breach():
    b = []
    # laptop
    b.append(poly([(150, 92), (300, 92), (314, 108), (136, 108)], NAVY))
    b.append(rect(160, 30, 130, 62, NAVY, 3))
    b.append(rect(167, 37, 116, 48, IND, 2))
    # lock on screen
    b.append(rect(213, 56, 26, 20, YEL, 2))
    b.append(f'<path d="M217 56 V49 a9 9 0 0 1 18 0 V56" fill="none" stroke="{YEL}" stroke-width="3.5"/>')
    b.append(circ(226, 64, 3.5, NAVY))
    # crack
    b.append(poly([(226, 37), (232, 50), (224, 57), (232, 66), (226, 75), (234, 85)], RED))
    # satellite, bigger
    b.append(rect(356, 26, 48, 22, WHITE))
    b.append(f'<rect x="356" y="26" width="48" height="22" fill="none" stroke="{NAVY}" stroke-width="1.5"/>')
    b.append(rect(326, 31, 30, 12, IND))
    b.append(rect(404, 31, 30, 12, IND))
    b.append(f'<line x1="380" y1="48" x2="372" y2="62" stroke="{NAVY}" stroke-width="2.5"/>')
    b.append(circ(371, 64, 4, YEL))
    # data lines, bolder
    for dy in (22, 44, 66):
        b.append(f'<line x1="46" y1="{dy}" x2="118" y2="{dy}" stroke="{LAV}" stroke-width="3" stroke-dasharray="8 5"/>')
        b.append(circ(42, dy, 4, LAV))
    return svg("".join(b), "#EDE7DA")


# ---------------------------------------------------------------- M13 chart fall
def m13_chart():
    b = []
    # chart: spike then plunge (green rise, red fall)
    b.append(f'<polyline points="60,96 120,92 180,88 220,30" fill="none" '
             f'stroke="#2E9E5B" stroke-width="3" stroke-linecap="round"/>')
    # plunge segment, red, overlaid
    b.append(f'<polyline points="220,30 260,44 300,80 340,104 400,110" fill="none" '
             f'stroke="{ACCENT}" stroke-width="3.5" stroke-linecap="round"/>')
    b.append(circ(220, 30, 5, "#2E9E5B"))
    b.append(circ(400, 110, 5, ACCENT))
    # grid lines
    for gy in (30, 60, 90):
        b.append(f'<line x1="52" y1="{gy}" x2="420" y2="{gy}" stroke="{PLAV}" stroke-width="1"/>')
    # GPU chip
    b.append(rect(392, 18, 56, 56, NAVY, 4))
    b.append(rect(404, 30, 32, 32, IND, 2))
    b.append(circ(420, 46, 6, YEL))
    for px in (402, 418, 434):
        b.append(rect(px, 10, 4, 8, NAVY))
        b.append(rect(px, 74, 4, 8, NAVY))
    return svg("".join(b), "#F4EFE6")


# ---------------------------------------------------------------- H2-US data (v2 Hero 1)
def h2us_data():
    b = []
    # giant bars: Q2 2.2 -> advance 3.4 -> second estimate 4.3
    b.append(rect(96, 84, 52, 26, MINT))
    b.append(rect(168, 66, 52, 44, LAV))
    b.append(rect(240, 34, 52, 76, YEL))
    b.append(rect(312, 8, 52, 102, CORAL))
    for x in (96, 168, 240, 312):
        b.append(f'<line x1="{x+7}" y1="104" x2="{x+45}" y2="104" stroke="{WHITE}" stroke-width="1.6" stroke-linecap="round"/>')
    # arrow up
    b.append(f'<line x1="104" y1="72" x2="340" y2="8" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')
    b.append(poly([(340, 2), (370, 8), (344, 24)], NAVY))
    # Fed-style building, right (kept inside the frame after the 1.15x zoom)
    b.append(poly([(380, 78), (410, 54), (440, 78)], WHITE))
    b.append(rect(386, 78, 48, 8, WHITE))
    for cx in (390, 404, 418, 432):
        b.append(rect(cx, 80, 6, 22, WHITE))
    b.append(rect(382, 102, 56, 8, NAVY))
    # coins
    b.append(circ(56, 92, 14, YEL))
    b.append(circ(56, 92, 9, "none"))
    b.append(circ(80, 100, 10, YEL))
    return svg("".join(b), NAVY, s=1.15)


# ---------------------------------------------------------------- M14 Cairo tanker fire (v2)
def m14_cairo():
    b = []
    b.append(stars(8))
    # highway
    b.append(f'<rect x="0" y="86" width="480" height="34" fill="#3A3A3A"/>')
    b.append(f'<line x1="0" y1="103" x2="480" y2="103" stroke="{YEL}" stroke-width="2" stroke-dasharray="14 10"/>')
    # big tanker, centre-left
    b.append(rect(120, 52, 190, 30, CORAL))
    b.append(rect(120, 52, 190, 7, RED))
    b.append(circ(150, 67, 12, WHITE))
    b.append(circ(150, 67, 7, NAVY))
    b.append(rect(310, 40, 34, 42, WHITE))
    b.append(rect(316, 46, 10, 8, NAVY))
    b.append(circ(140, 86, 9, INK))
    b.append(circ(290, 86, 9, INK))
    b.append(circ(326, 86, 9, INK))
    # flames over tanker
    for fx, fh, col in ((150, 44, "#FF8A00"), (180, 56, RED), (215, 48, "#FF8A00"),
                        (250, 58, RED), (285, 44, "#FF8A00")):
        b.append(poly([(fx - 15, 56), (fx, 56 - fh), (fx + 15, 56)], col))
        b.append(poly([(fx - 6, 56), (fx, 56 - fh + 18), (fx + 6, 56)], YEL))
    # smoke
    b.append(circ(180, 14, 13, PLAV))
    b.append(circ(210, 8, 10, PLAV2))
    b.append(circ(240, 16, 11, PLAV))
    # cars caught in fire, right
    b.append(rect(380, 66, 56, 16, NAVY, 4))
    b.append(rect(388, 58, 30, 10, SKY, 3))
    b.append(circ(394, 84, 6, INK))
    b.append(circ(424, 84, 6, INK))
    b.append(poly([(400, 66), (406, 50), (412, 66)], YEL))
    b.append(poly([(404, 66), (406, 56), (408, 66)], "#FF8A00"))
    return svg("".join(b), "#101736")


# ---------------------------------------------------------------- M15 Sandringham break-in (v2)
def m15_sandringham():
    b = []
    # moon + night sky
    b.append(circ(420, 24, 15, YEL))
    b.append(stars(10))
    # big country house, centre
    b.append(rect(140, 44, 200, 62, "#8A4B2E"))
    b.append(poly([(130, 46), (240, 14), (350, 46)], "#5C2E1A"))
    b.append(rect(140, 44, 200, 4, "#5C2E1A"))
    for wx in (156, 196, 236, 276, 312):
        b.append(rect(wx, 56, 18, 22, YEL))
        b.append(f'<line x1="{wx+9}" y1="56" x2="{wx+9}" y2="78" stroke="#5C2E1A" stroke-width="1.5"/>')
    b.append(rect(228, 78, 24, 28, NAVY))
    b.append(circ(248, 92, 2, YEL))
    # drainpipe on the side + scuff marks
    b.append(rect(336, 20, 6, 86, STEEL))
    b.append(f'<line x1="330" y1="34" x2="342" y2="40" stroke="{WHITE}" stroke-width="1.6"/>')
    b.append(f'<line x1="330" y1="46" x2="342" y2="52" stroke="{WHITE}" stroke-width="1.6"/>')
    # police tape
    b.append(f'<rect x="0" y="106" width="480" height="10" fill="{YEL}"/>')
    b.append(f'<line x1="0" y1="106" x2="480" y2="116" stroke="{NAVY}" stroke-width="1.2"/>')
    # trees
    b.append(poly([(60, 106), (84, 60), (108, 106)], "#2E5B3E"))
    b.append(poly([(380, 106), (404, 66), (428, 106)], "#2E5B3E"))
    return svg("".join(b), "#1B2A4A")


SCENES = {
    "h1": h1_shenzhou,
    "h2": h2_cpi,
    "h2us": h2us_data,
    "h3": h3_treaty,
    "m4": m4_tower,
    "m5": m5_court,
    "m6": m6_fire,
    "m7": m7_metro,
    "m8": m8_jets,
    "m9": m9_oil,
    "m10": m10_tanker,
    "m11": m11_ship,
    "m12": m12_breach,
    "m13": m13_chart,
    "m14": m14_cairo,
    "m15": m15_sandringham,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    for key, fn in SCENES.items():
        path = os.path.join(OUT, f"{key}.svg")
        with open(path, "w") as fh:
            fh.write(fn())
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
