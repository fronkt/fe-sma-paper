"""Build Fig. 10 (Fig. 8 before the 2026-08-14 renumbering) — response of both alloys
to the three-cycle AGG treatment.

REDESIGNED 2026-08-18 on F. Cai's instruction: the burned-in scale bars (200/400/
250 um at three magnifications) are gone, panels (a)-(c) are cropped to one common
field of view of 0.36 x 0.36 mm at one magnification (all three sources are
0.671 um/px Clemex exports, 200-um bar = 298 px), and each carries an identical
drawn 100 um scale bar. The stock diameters (0.64 mm wire / 0.36 mm wire / ~1 mm
rod) move to the caption. Panel (d), the stereomicroscope surface view, is a
3.25 um/px macro photo (250-um bar = 77 px) and cannot support a 0.36 mm field at
print resolution; it is cropped square around the boundary cracks (1.82 mm field)
and carries no bar - the caption says it is a lower-magnification surface view.

Sources in `sources-AGG/`, copied from the E: drive and identified by md5; see
`revision/JMRT-R1/processing/AGG-MICROGRAPH-PROVENANCE.md`. Panel (c) now uses
`Fe-SMA-3 CYCLE AGG 4.jpg` (as `c_..._highmag.jpg`), the 2x-magnification sibling
of the previous panel's source - same specimen, same section, same arrested band -
because the previous 1.342 um/px overview cannot yield a sharp 0.36 mm crop.

Effective print resolution: 537 source px per panel; at single-column width
(panel ~44 mm) that is ~310 dpi, above Elsevier's 300-dpi floor. The figure is
intended for single-column placement.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "sources-AGG"
PANEL_PX = 1080         # display px per panel
GAP = 24
LABEL_SIZE = 96
LABEL_PAD = 24
UM_PER_PX = 0.671       # panels a-c source scale
FIELD_UM = 360.0        # common field of view, a-c
CROP = round(FIELD_UM / UM_PER_PX)   # 537 px

# (label, file, crop x0, crop y0, crop size, draw_bar)
PANELS = [
    ("a", "a_benchmark_0.64mm_3cycleAGG_bamboo.jpg", 300, 80, CROP, True),
    ("b", "b_LLM_0.36mm_3cycleAGG_nocoarsening.jpg", 420, 80, CROP, True),
    ("c", "c_LLM_rod_3cycleAGG_arrested_highmag.jpg", 480, 90, CROP, True),
    ("d", "d_LLM_rod_3cycleAGG_200C3h_cracks.tif", 770, 240, 560, False),
]

BAR_UM = 100.0
BAR_PX = round(BAR_UM / FIELD_UM * PANEL_PX)   # 300 display px


def load_font(size):
    for name in ("arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    canvas = Image.new("RGB", (2 * PANEL_PX + GAP, 2 * PANEL_PX + GAP), "white")
    positions = [(0, 0), (PANEL_PX + GAP, 0), (0, PANEL_PX + GAP),
                 (PANEL_PX + GAP, PANEL_PX + GAP)]
    font = load_font(LABEL_SIZE)
    bar_font = load_font(56)

    for (label, fname, x0, y0, size, draw_bar), pos in zip(PANELS, positions):
        img = Image.open(SRC / fname).convert("RGB")
        tile = img.crop((x0, y0, x0 + size, y0 + size)).resize(
            (PANEL_PX, PANEL_PX), Image.LANCZOS)
        d = ImageDraw.Draw(tile)

        # corner badge, sized to the glyphs (build_composites.py once clipped
        # the closing paren by assuming a fixed width - keep measuring)
        text = f"({label})"
        l, t, r, b = d.textbbox((0, 0), text, font=font)
        d.rectangle([LABEL_PAD, LABEL_PAD,
                     LABEL_PAD + (r - l) + 2 * LABEL_PAD,
                     LABEL_PAD + (b - t) + LABEL_PAD],
                    fill="white", outline="black", width=3)
        d.text((2 * LABEL_PAD - l, LABEL_PAD + LABEL_PAD // 2 - t), text,
               font=font, fill="black")

        if draw_bar:
            bt = "100 µm"
            l2, t2, r2, b2 = d.textbbox((0, 0), bt, font=bar_font)
            tw, th = r2 - l2, b2 - t2
            pad = 18
            bw = max(BAR_PX, tw) + 2 * pad
            bh = 14 + 10 + th + 2 * pad
            bx = PANEL_PX - 36 - bw
            by = PANEL_PX - 36 - bh
            d.rectangle([bx, by, bx + bw, by + bh], fill="white",
                        outline="black", width=3)
            cx = bx + bw // 2
            d.rectangle([cx - BAR_PX // 2, by + pad,
                         cx + BAR_PX // 2, by + pad + 14], fill="black")
            d.text((cx - tw // 2 - l2, by + pad + 14 + 10 - t2), bt,
                   font=bar_font, fill="black")

        canvas.paste(tile, pos)

    out = HERE / "Figure_10.jpg"
    canvas.save(out, dpi=(600, 600), quality=95, optimize=True)
    print(f"wrote {out.name}  ({canvas.size[0]}x{canvas.size[1]} px, "
          f"{out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
