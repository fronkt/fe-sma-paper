"""Rebuild Fig. 3 with the benchmark's stepwise cyclic curves added as (c) and (d).

R3#7: "no corresponding stepwise cyclic curves for the benchmark". The panels exist; they
were cut during the Materials & Design revision and live in
`archive-2026-06-pre-MD-revision/`.

They are appended to Fig. 3 rather than made a new figure because they are the same
experiment on the same two alloys as (a) and (b), and because inserting a new figure into
Sec. 3.2 would renumber Figs. 4-7 and put 26 cosmetic tracked changes in front of the
editor for no reviewer benefit.

Panels (a) and (b) are carried over as the single existing `Figure_3.jpg`, which already
contains both and already carries its own "a)" / "b)" labels; only (c) and (d) get new
badges. Restyling all four from raw data is the right long-term fix and is not this pass -
the Instron spool behind each archived panel has to be identified first, for the same
reason `Fig2b` had to be (see AGG-MICROGRAPH-PROVENANCE.md).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
ARCHIVE = HERE / "archive-2026-06-pre-MD-revision"
TARGET_DPI = 600
PANEL_W = 1800
GAP = 24
LABEL_SIZE = 96
LABEL_PAD = 24


def load_font(size):
    for name in ("arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit(img, w):
    return img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)


def badge(draw, font, text, x, y):
    l, t, r, b = draw.textbbox((0, 0), text, font=font)
    draw.rectangle([x, y, x + (r - l) + 2 * LABEL_PAD, y + (b - t) + LABEL_PAD],
                   fill="white", outline="black", width=3)
    draw.text((x + LABEL_PAD - l, y + LABEL_PAD // 2 - t), text, font=font, fill="black")


def main():
    # (c) and (d) are Excel exports whose y-axis numbers run to the very left edge, so the
    # badge needs a gutter of its own or it lands on top of "1000".
    GUTTER = 200
    top = fit(Image.open(HERE / "archive-2026-08-12-Figure_3-two-panel.jpg").convert("RGB"),
              2 * PANEL_W + GAP)
    c = fit(Image.open(ARCHIVE / "Fig3c_Omori_1200C_5min_cyclic.png").convert("RGB"),
            PANEL_W - GUTTER)
    d = fit(Image.open(ARCHIVE / "Fig3d_Omori_1200C_12sec_cyclic.png").convert("RGB"),
            PANEL_W - GUTTER)

    bot_h = max(c.height, d.height)
    canvas = Image.new("RGB", (2 * PANEL_W + GAP, top.height + bot_h + GAP), "white")
    canvas.paste(top, (0, 0))
    canvas.paste(c, (GUTTER, top.height + GAP))
    canvas.paste(d, (PANEL_W + GAP + GUTTER, top.height + GAP))

    font = load_font(LABEL_SIZE)
    draw = ImageDraw.Draw(canvas)
    badge(draw, font, "(c)", LABEL_PAD, top.height + GAP + LABEL_PAD)
    badge(draw, font, "(d)", PANEL_W + GAP + LABEL_PAD, top.height + GAP + LABEL_PAD)

    out = HERE / "Figure_3.jpg"
    canvas.save(out, dpi=(TARGET_DPI, TARGET_DPI), quality=95, optimize=True)
    print(f"wrote {out.name}  ({canvas.size[0]}x{canvas.size[1]} px, "
          f"{out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
