"""Assemble 2x2 composite figures for the Fe-SMA SMS manuscript.

Outputs Fig2_microstructure.png, Fig3_stressstrain.png, Fig5_XRD_2D.png
at 600 dpi with white panel-label badges (a)-(d) in the top-left corner of
each panel.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
TARGET_DPI = 600
PANEL_W = 1800  # px per panel at 600 dpi → 3 in panel width
GAP = 24        # px between panels
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
    h = round(img.height * w / img.width)
    return img.resize((w, h), Image.LANCZOS)

def compose_2x2(panels, labels, out_path):
    imgs = [fit(Image.open(p).convert("RGB"), PANEL_W) for p in panels]
    row_h = max(imgs[0].height, imgs[1].height), max(imgs[2].height, imgs[3].height)
    total_w = 2 * PANEL_W + GAP
    total_h = row_h[0] + row_h[1] + GAP
    canvas = Image.new("RGB", (total_w, total_h), "white")
    positions = [
        (0, 0), (PANEL_W + GAP, 0),
        (0, row_h[0] + GAP), (PANEL_W + GAP, row_h[0] + GAP),
    ]
    for img, pos in zip(imgs, positions):
        canvas.paste(img, pos)
    font = load_font(LABEL_SIZE)
    draw = ImageDraw.Draw(canvas)
    for label, (x, y) in zip(labels, positions):
        bx = x + LABEL_PAD
        by = y + LABEL_PAD
        bw = LABEL_SIZE + LABEL_PAD
        bh = LABEL_SIZE + LABEL_PAD // 2
        draw.rectangle([bx - 8, by - 8, bx + bw, by + bh], fill="white", outline="black", width=3)
        draw.text((bx + 12, by - 8), f"({label})", font=font, fill="black")
    canvas.save(out_path, dpi=(TARGET_DPI, TARGET_DPI), optimize=True)
    print(f"  wrote {out_path.name}  ({canvas.size[0]}x{canvas.size[1]} px)")

def main():
    print("Building Fig.2 microstructure 2x2 ...")
    compose_2x2(
        [HERE / "Fig2a_AI_1200C_1min_microstructure.jpg",
         HERE / "Fig2b_AI_3cycle_AGG_microstructure.jpg",
         HERE / "Fig2c_Omori_3cycle_AGG_bamboo.jpg",
         HERE / "Fig2d_Omori_1200C_1min_acicular.jpg"],
        ["a", "b", "c", "d"],
        HERE / "Fig2_microstructure_composite.png",
    )
    print("Building Fig.3 stress-strain 2x2 ...")
    compose_2x2(
        [HERE / "Fig3a_AI_standard_1200C_cyclic.png",
         HERE / "Fig3b_AI_3cycle_AGG_cyclic.png",
         HERE / "Fig3c_Omori_1200C_5min_cyclic.png",
         HERE / "Fig3d_Omori_1200C_12sec_cyclic.png"],
        ["a", "b", "c", "d"],
        HERE / "Fig3_stressstrain_composite.png",
    )
    print("Building Fig.5 XRD 2D 2x2 (indexed AI panels + Omori panels) ...")
    # Fig5_XRD_2D_4panel.png is already a 2x2; just add labels and re-render at 600 dpi.
    src = Image.open(HERE / "Fig5_XRD_2D_4panel.png").convert("RGB")
    src = src.resize((2 * PANEL_W + GAP, round(src.height * (2 * PANEL_W + GAP) / src.width)), Image.LANCZOS)
    font = load_font(LABEL_SIZE)
    draw = ImageDraw.Draw(src)
    half_w = src.width // 2
    half_h = src.height // 2
    for label, (x, y) in zip(["a", "b", "c", "d"],
                              [(0, 0), (half_w, 0), (0, half_h), (half_w, half_h)]):
        bx = x + LABEL_PAD
        by = y + LABEL_PAD
        bw = LABEL_SIZE + LABEL_PAD
        bh = LABEL_SIZE + LABEL_PAD // 2
        draw.rectangle([bx - 8, by - 8, bx + bw, by + bh], fill="white", outline="black", width=3)
        draw.text((bx + 12, by - 8), f"({label})", font=font, fill="black")
    src.save(HERE / "Fig5_XRD_2D_composite.png", dpi=(TARGET_DPI, TARGET_DPI), optimize=True)
    print(f"  wrote Fig5_XRD_2D_composite.png  ({src.size[0]}x{src.size[1]} px)")

if __name__ == "__main__":
    main()
