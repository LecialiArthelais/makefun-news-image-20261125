#!/usr/bin/env python3
"""
Map panel for News-25 — renders the numbered world map with
geopandas + matplotlib (skill: geopandas, K-Dense, 58.370 stars).

Source data: Natural Earth 110m land, GeoJSON, vetted upstream
  https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_land.geojson
  sha256 9e0729ee253ca7d7a5c4ae9395fb1902264c5377c52e224d13dd85010e2835d9
  (127 Polygon features, downloaded 25 Nov 2026 01:45 WIB; stored in
  data/ne_110m_land.geojson, NOT committed to the entry repo.)
Projection: ESRI:54030 (Robinson), cropped to lat -42..78 so the panel
fits the 470x185 slot beside DATE CHECK. Pins are numbered red discs;
shared locations carry a combined label (2.3, 5.13, 12+, 14.30, 15.34).
Crowded pins (Europe, US East, Korea) get leader-line offsets.

Run:  ./venv-map/bin/python map_panel.py [out.png]   (build time only)
"""
import sys

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

LAND = "data/ne_110m_land.geojson"
ROBINSON = "ESRI:54030"

# (label, lat, lon, dx_pt, dy_pt) — dx/dy move the number chip off the dot
# when pins crowd each other; (0, 0) means the number sits on the dot.
PINS = [
    ("1", 40.96, 100.30, 0, 0),        # Jiuquan
    ("2·3", -35.28, 149.13, -16, 0),     # Canberra (CPI + treaty)
    ("4", 24.71, 46.68, 0, 0),         # Riyadh
    ("5·13", 40.71, -74.01, -18, 10),    # New York (Huawei + Nvidia)
    ("6", -39.85, 147.98, 0, 0),       # Flinders Island
    ("7", 37.57, 126.98, -20, 6),      # Seoul
    ("8", 37.48, 130.87, 20, -6),      # Ulleung
    ("9", 33.31, 44.36, 0, 0),         # Baghdad
    ("10", 26.57, 56.25, 0, 0),        # Strait of Hormuz
    ("11", 59.80, 24.50, 0, 0),        # Gulf of Finland
    ("12+", 38.91, -77.04, 20, -16),   # Washington (12, 17, 23, 24)
    ("14·30", 35.68, 139.69, 14, -12),    # Tokyo (Seki + Nikkei)
    ("15·34", 50.85, 4.35, -8, 16),   # Brussels (summit + budget)
    ("16", 26.71, -80.04, 18, -16),    # Palm Beach
    ("18", 46.20, 6.14, 16, -14),       # Geneva
    ("20", 40.42, -3.70, -14, -16),    # Madrid
    ("21", 10.39, -75.51, -16, 0),       # Cartagena
    ("22", 45.42, -75.70, 18, 12),     # Ottawa (Kutryk / ISS)
    ("25", 48.86, 2.35, -24, -4),        # Paris
    ("26", 31.13, -97.78, 0, 0),       # Fort Hood, Texas
    ("27", 4.15, -73.64, 16, -6),        # Villavicencio
    ("28", -28.01, 153.40, 0, 0),      # Carrara, Gold Coast
    ("29", 28.61, 77.21, 0, 0),        # New Delhi
    ("31", 48.58, 7.75, 22, 4),        # Strasbourg
    ("32", 14.80, 42.95, -16, 2),        # Hodeidah
    ("33", 12.79, 45.04, 16, -10),        # Aden
]


def render(pins, out_path, width_px=470, height_px=185):
    world = gpd.read_file(LAND)
    world = world.to_crs(ROBINSON)
    fig = plt.figure(figsize=(width_px / 100, height_px / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    world.plot(ax=ax, color="#DDE1E4", edgecolor="#FFFFFF", linewidth=0.4)
    ax.set_xlim(-1.72e7, 1.72e7)
    ax.set_ylim(-5.0e6, 8.8e6)
    ax.set_aspect("equal")
    pts = gpd.GeoDataFrame(
        geometry=gpd.points_from_xy([p[2] for p in pins], [p[1] for p in pins]),
        crs="EPSG:4326",
    ).to_crs(ROBINSON)
    for (label, _lat, _lon, dx, dy), geom in zip(pins, pts.geometry):
        x, y = geom.x, geom.y
        # On-dot labels must fit INSIDE the disc: 1 char -> r 400 km,
        # 2 chars -> r 500 km (white text on light land is invisible
        # outside the disc). Longer labels always use offset chips.
        radius = 500000 if len(label) == 2 else 400000
        ax.add_patch(Circle((x, y), radius, facecolor="#DC2626",
                            edgecolor="#FFFFFF", linewidth=1.0, zorder=5))
        if dx == 0 and dy == 0:
            ax.text(x, y, label, ha="center", va="center", fontsize=6,
                    color="#FFFFFF", fontweight="bold", zorder=6)
        else:
            ax.annotate(label, xy=(x, y), xytext=(dx, dy),
                        textcoords="offset points", ha="center", va="center",
                        fontsize=6.5, color="#FFFFFF", fontweight="bold",
                        bbox=dict(boxstyle="round,pad=0.22,rounding_size=1.2", facecolor="#DC2626",
                                  edgecolor="#FFFFFF", linewidth=0.8),
                        arrowprops=dict(arrowstyle="-", color="#DC2626",
                                        linewidth=0.8, shrinkA=2, shrinkB=1),
                        zorder=6)
    fig.savefig(out_path, dpi=100)
    plt.close(fig)
    print(f"wrote {out_path} ({width_px}x{height_px}) from {len(pins)} pins")


if __name__ == "__main__":
    render(PINS, sys.argv[1] if len(sys.argv) > 1 else "map_panel.png")
