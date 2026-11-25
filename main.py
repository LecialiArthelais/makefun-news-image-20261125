#!/usr/bin/env python3
"""
News-25 -- "Sum up 25 November's world news in one image"
make.fun bounty: news-image-20261125 ($100, entries close 27 Nov 2026 07:00 WIB)

Entrypoint. The grader runs this file as user `nobody` with
`python3 -P -s` on a read-only filesystem and no network, so this file
uses only the Python standard library and does no drawing at all: it
copies the pre-rendered `entry.png` shipped beside it into
$MAKEFUN_OUTPUT_DIR (or /output when the variable is unset).

The page itself is drawn at build time by build_page.py (Pillow), never
here, so grading needs no third-party package and no fonts.

Run:  python3 main.py        # writes $MAKEFUN_OUTPUT_DIR/entry.png
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

MAX_BYTES = 1048576          # gate: at most 1 MiB
MAX_SIDE = 1024              # gate: at most 1024 x 1024 px


def output_dir():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.abspath(out)


def png_size(path):
    """Width and height from a PNG IHDR chunk, standard library only."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if os.path.abspath(SRC) == os.path.abspath(dst):
        print("output already is the shipped render; nothing to copy")
        return 0
    width, height = png_size(SRC)
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"entry.png is {width}x{height}, over the {MAX_SIDE}x{MAX_SIDE} gate",
              file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dst)
    size = os.path.getsize(dst)
    print(f"copied {SRC} -> {dst} ({size} bytes, {width}x{height})")
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB gate", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
