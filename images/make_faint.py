"""Make the faint home-page versions of the biography pictures.

The home page shows each picture very pale behind the text, like print
showing through from the other side of a page. For that it wants small,
grey copies with the card mounts trimmed off. This script makes them
from the full pictures in static/images/ and puts them in
static/images/faint/. It needs Pillow (pip install pillow), which the
site build does not, so run it by hand after adding or changing a
picture:

    python3 images/make_faint.py
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
