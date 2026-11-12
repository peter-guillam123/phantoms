"""Make the home page's copies of the pictures.

Two sets. It needs Pillow (pip install pillow), which the site build
does not, so run it by hand after adding or changing a picture:

    python3 images/make_faint.py

1. Faint copies of the biography pictures. The home page shows each one
   very pale behind its writer's name, like print showing through from
   the other side of a page. For that it wants small, grey copies with
   the card mounts trimmed off. They are made from static/images/ and
   put in static/images/faint/.

2. The ghost pictures: the dark plates behind the title, one for each
   writer's idea of a ghost. The originals are kept in images/ghosts/,
   named after the writer. Two sizes of each go in static/images/ghosts/:
   a wide one for big screens and a small one for phones.
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "static" / "images"
OUT = SRC / "faint"
TRIM = 0.09      # share cut from each edge, to lose the mount
LONG_SIDE = 720

OUT.mkdir(exist_ok=True)
for path in sorted(SRC.glob("*.webp")):
    im = Image.open(path).convert("L")
    w, h = im.size
    im = im.crop((int(w * TRIM), int(h * TRIM), int(w * (1 - TRIM)), int(h * (1 - TRIM))))
    im = ImageOps.autocontrast(im, cutoff=1)
    im.thumbnail((LONG_SIDE, LONG_SIDE), Image.LANCZOS)
    im.save(OUT / path.name, "WEBP", quality=45, method=6)
    print(path.name, im.size, (OUT / path.name).stat().st_size // 1024, "KB")

GHOSTS = ROOT / "images" / "ghosts"
GHOSTS_OUT = SRC / "ghosts"
GHOSTS_OUT.mkdir(exist_ok=True)
for path in sorted(GHOSTS.glob("*.webp")):
    im = Image.open(path).convert("L")
    for width, suffix, quality in ((1200, "", 48), (760, "-small", 50)):
        copy = im.copy()
        copy.thumbnail((width, width), Image.LANCZOS)
        out = GHOSTS_OUT / f"{path.stem}{suffix}.webp"
        copy.save(out, "WEBP", quality=quality, method=6)
        print(out.name, copy.size, out.stat().st_size // 1024, "KB")
