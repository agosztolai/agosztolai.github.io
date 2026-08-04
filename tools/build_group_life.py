#!/usr/bin/env python3
"""Prepare the Group life gallery.

Reads the full-size photos in images/group_life/, writes web-sized copies into
images/group_life/web/, and records each photo's size and mosaic tile span in
_data/group_life.yml, which group-life.html renders.

Run this after adding or removing photos:

    python3 tools/build_group_life.py

Photos whose `alt` text has already been written in the data file keep it.
Originals are never modified. Requires macOS `sips`.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, "images", "group_life")
WEB_DIR = os.path.join(SRC_DIR, "web")
DATA = os.path.join(ROOT, "_data", "group_life.yml")

# Long-edge widths written for each photo, with JPEG quality.
SIZES = [(1200, 78), (600, 72)]
EXTS = (".jpg", ".jpeg", ".png")

# Grid geometry: 6 columns, each row one third of a column wide, so a 2x2 tile
# is 3:2 and a 2x4 tile is 3:4. Keeps cropping mild for typical camera aspects.
PORTRAIT = (2, 4)
LANDSCAPE = (2, 2)
FEATURE = (4, 4)   # same shape as LANDSCAPE, twice the size
FEATURE_EVERY = 5  # every Nth landscape photo becomes a feature tile


def sips_dims(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                         capture_output=True, text=True, check=True).stdout
    w = int(re.search(r"pixelWidth:\s*(\d+)", out).group(1))
    h = int(re.search(r"pixelHeight:\s*(\d+)", out).group(1))
    return w, h


def resize(src, dest, long_edge, quality):
    subprocess.run(["sips", "-Z", str(long_edge),
                    "--setProperty", "format", "jpeg",
                    "--setProperty", "formatOptions", str(quality),
                    src, "--out", dest],
                   capture_output=True, check=True)


def existing_alts():
    """Alt text already written in the data file, keyed by base name."""
    alts = {}
    if not os.path.exists(DATA):
        return alts
    base = None
    for line in open(DATA, encoding="utf-8"):
        m = re.match(r"\s*-\s*base:\s*(\S+)", line)
        if m:
            base = m.group(1)
        m = re.match(r"\s*alt:\s*(.+?)\s*$", line)
        if m and base:
            alts[base] = m.group(1).strip('"')
    return alts


def pack(photos):
    """Order photos so the six-column mosaic packs without holes.

    A feature (4 wide, 4 tall) leaves a 2x4 gap beside it, which one portrait or
    two stacked landscapes fill exactly; a portrait leaves room for four
    landscapes; three landscapes make a flush two-row band. The grid's dense flow
    does the placing, so this only has to hand it a workable sequence.
    """
    features = [p for p in photos if p["kind"] == "feature"]
    portraits = [p for p in photos if p["kind"] == "portrait"]
    landscapes = [p for p in photos if p["kind"] == "landscape"]
    out = []

    while features:
        out.append(features.pop(0))
        if portraits:
            out.append(portraits.pop(0))
        else:
            out += [landscapes.pop(0) for _ in range(min(2, len(landscapes)))]

    while len(portraits) >= 3:
        out += [portraits.pop(0) for _ in range(3)]

    while portraits:
        out.append(portraits.pop(0))
        out += [landscapes.pop(0) for _ in range(min(4, len(landscapes)))]

    out += landscapes
    return out


def main():
    if not os.path.isdir(SRC_DIR):
        sys.exit(f"no such directory: {SRC_DIR}")
    os.makedirs(WEB_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    alts = existing_alts()

    photos = sorted(f for f in os.listdir(SRC_DIR)
                    if f.lower().endswith(EXTS) and not f.startswith("."))
    if not photos:
        sys.exit(f"no photos found in {SRC_DIR}")

    entries = []
    landscapes = 0
    for name in photos:
        base, _ = os.path.splitext(name)
        src = os.path.join(SRC_DIR, name)
        w, h = sips_dims(src)
        aspect = w / h

        for long_edge, quality in SIZES:
            dest = os.path.join(WEB_DIR, f"{base}-{long_edge}.jpg")
            resize(src, dest, long_edge, quality)

        if aspect < 0.9:
            kind, (cols, rows) = "portrait", PORTRAIT
        else:
            landscapes += 1
            if landscapes % FEATURE_EVERY == 1:
                kind, (cols, rows) = "feature", FEATURE
            else:
                kind, (cols, rows) = "landscape", LANDSCAPE

        widest = min(SIZES[0][0], max(w, h))
        entries.append({
            "base": base,
            "width": widest if aspect >= 1 else round(widest * aspect),
            "height": round(widest / aspect) if aspect >= 1 else widest,
            "cols": cols,
            "rows": rows,
            "kind": kind,
            "alt": alts.get(base, ""),
        })
        kb = os.path.getsize(os.path.join(WEB_DIR, f"{base}-1200.jpg")) // 1024
        print(f"{name}: {w}x{h} (aspect {aspect:.2f}) -> {kind} {cols}x{rows} tile, {kb} KB")

    entries = pack(entries)

    with open(DATA, "w", encoding="utf-8") as fh:
        fh.write("# Generated by tools/build_group_life.py -- rerun after adding photos.\n")
        fh.write("# `alt` is safe to edit by hand; the script preserves it.\n")
        for e in entries:
            fh.write(f"- base: {e['base']}\n")
            fh.write(f"  width: {e['width']}\n")
            fh.write(f"  height: {e['height']}\n")
            fh.write(f"  cols: {e['cols']}\n")
            fh.write(f"  rows: {e['rows']}\n")
            fh.write(f"  alt: \"{e['alt']}\"\n")
    print(f"\nwrote {DATA} with {len(entries)} photos")


if __name__ == "__main__":
    main()
