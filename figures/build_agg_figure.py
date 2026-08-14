"""Build Fig. 10 (Fig. 8 before the 2026-08-14 renumbering) — response of both alloys
to the three-cycle AGG treatment.

Sources are in `sources-AGG/`, copied from the E: drive and identified by md5 against
the originals; see `revision/JMRT-R1/processing/AGG-MICROGRAPH-PROVENANCE.md` for the
match table and the measured specimen sizes.

Each panel keeps its own burned-in scale bar because the four specimens were imaged at
three different magnifications and at three different stock diameters. A single common
scale would have to crop three of them.

Panel (d) is a stereomicroscope surface view, not a section; it is included because the
boundary cracking it shows is what the 25-49 % strength scatter in the AGG tensile sets
is made of.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "sources-AGG"
TARGET_DPI = 600
PANEL_W = 1800          # px per panel at 600 dpi -> 3 in printed panel width
GAP = 24
LABEL_SIZE = 96
LABEL_PAD = 24

PANELS = [
    ("a", "a_benchmark_0.64mm_3cycleAGG_bamboo.jpg"),
    ("b", "b_LLM_0.36mm_3cycleAGG_nocoarsening.jpg"),
    ("c", "c_LLM_rod_3cycleAGG_arrested.jpg"),
    ("d", "d_LLM_rod_3cycleAGG_200C3h_cracks.tif"),
]


def load_font(size):
    for name in ("arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit(img, w):
    return img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)


def main():
    imgs = [fit(Image.open(SRC / f).convert("RGB"), PANEL_W) for _, f in PANELS]
    top_h = max(imgs[0].height, imgs[1].height)
    bot_h = max(imgs[2].height, imgs[3].height)
    canvas = Image.new("RGB", (2 * PANEL_W + GAP, top_h + bot_h + GAP), "white")
    positions = [(0, 0), (PANEL_W + GAP, 0),
                 (0, top_h + GAP), (PANEL_W + GAP, top_h + GAP)]
    for img, pos in zip(imgs, positions):
        canvas.paste(img, pos)

    font = load_font(LABEL_SIZE)
    draw = ImageDraw.Draw(canvas)
    for (label, _), (x, y) in zip(PANELS, positions):
        text = f"({label})"
        # Size the badge to the glyphs. build_composites.py assumed a fixed width and
        # clipped the closing paren on every panel; do not repeat that here.
        l, t, r, b = draw.textbbox((0, 0), text, font=font)
        bx, by = x + LABEL_PAD, y + LABEL_PAD
        draw.rectangle([bx, by, bx + (r - l) + 2 * LABEL_PAD, by + (b - t) + LABEL_PAD],
                       fill="white", outline="black", width=3)
        draw.text((bx + LABEL_PAD - l, by + LABEL_PAD // 2 - t), text,
                  font=font, fill="black")

    out = HERE / "Figure_10.jpg"
    canvas.save(out, dpi=(TARGET_DPI, TARGET_DPI), quality=95, optimize=True)
    print(f"wrote {out.name}  ({canvas.size[0]}x{canvas.size[1]} px, "
          f"{out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
