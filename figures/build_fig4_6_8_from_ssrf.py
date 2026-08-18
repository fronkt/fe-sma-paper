"""Rebuild Figures 4, 6 and 8 from the raw SSRF synchrotron data at print resolution.

Replaces the low-resolution viewer screenshots (Fig. 4: 796 px, Fig. 6: 767 px,
Fig. 8: 475 px) that were below Elsevier's 300-dpi floor. Requires the E: drive.

Sources (E:\\FE-SMA):
  2026-1\\CS\\Sam*.tif      4288 x 4288 uint16 detector frames, 100 um pixels,
                            0.125872 A / 98.5 keV (SSRF; see 2026-1\\CS\\测试信息.txt)
  synchrotron.chi\\*.chi     azimuthal integrations of the same frames

Sample mapping (2026-1\\sample list.txt):
  Sam5-NO7286  LLM-alloy   1200 C/4 fpm, 0 % strain    -> Fig. 4a, Fig. 6a orange
  Sam6-NO7280  LLM-alloy   after 10 % strain           -> Fig. 4b, Fig. 6a teal
  Sam7-NO7271  benchmark   1200 C/4 fpm, 0 % strain    -> Fig. 4c, Fig. 6b orange
  Sam8-NO7265  benchmark   after 8 % strain            -> Fig. 4d, Fig. 6b teal
  Sam1-NO7325  LLM-alloy   AGG cyclic treatment        -> Fig. 8

Geometry, fitted from the frames themselves (Friedel-pair autocorrelation; the
CeO2 calibrant frame NO7412 gives the identical center):
  beam center (2120, 2230);  ring radius r = 18275 * tan(2theta) px
  (consistent to <0.1 % across all six indexed rings)

All five panels use one field of view - x in [center+600, center+2100],
y centered on the equator, 1500 x 1500 px - chosen so every labeled reflection,
including the D03/B2 superlattice rings at r = 688-795 px, is inside the frame.
Annotation arrows point at spot centroids located numerically in the band
r +/- 15 px of each ring; the faint Fe3Al/B2 targets are 4-6 sigma features on
the equator (they vanish in the azimuthal average, which is why Fig. 6 shows
only a small bump at 2.49 deg).

Fig. 6 reproduces the published curves exactly: raw intensities for Sam5/6/7,
Sam8 divided by 1.625 - the exposure normalization used in the source
spreadsheet (2026-1\\CS\\spectra.xlsx, cell AG4 = 2.6/1.6).
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

TIF_DIR = r"E:\FE-SMA\2026-1\CS"
CHI_DIR = r"E:\FE-SMA\synchrotron.chi"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

CX, CY = 2120, 2230          # beam center, px
OFF, W = 600, 1500           # panel: x in [CX+OFF, CX+OFF+W], y in [CY-W/2, CY+W/2]

ORANGE, TEAL = "#ED7D31", "#44546A"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "STIXGeneral"],
    "mathtext.fontset": "stix",
})

G111 = r"$\{111\}_{\gamma}$"
A110 = r"$\{110\}_{\alpha}$"
G200 = r"$\{200\}_{\gamma}$"
A200 = r"$\{200\}_{\alpha}$"
G220 = r"$\{220\}_{\gamma}$"
A211 = r"$\{211\}_{\alpha}$"
F111 = r"$\{111\}_{\mathrm{Fe_3Al}}$"
F200 = r"$\{200\}_{\mathrm{Fe_3Al}}$"
F311 = r"$\{311\}_{\mathrm{Fe_3Al}}$"
B100 = r"$\{100\}_{\mathrm{B2}}$"
B200 = r"$\{200\}_{\mathrm{B2}}$"


def panel(tif):
    """Inverted-grayscale display crop: median -> white, 99.7th pct -> black."""
    a = np.array(Image.open(os.path.join(TIF_DIR, tif + ".tif"))).astype(np.float64)
    crop = a[CY - W // 2:CY + W // 2, CX + OFF:CX + OFF + W]
    lo, hi = np.percentile(a, 50), np.percentile(a, 99.7)
    return 1.0 - np.clip((crop - lo) / (hi - lo), 0, 1)


def dress(ax, img, letter=None):
    ax.imshow(img, cmap="gray", vmin=0, vmax=1, interpolation="antialiased")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_linewidth(0.8)
    if letter:
        ax.text(60, 150, letter, fontsize=22, style="italic" if False else "normal")


def note(ax, text, label_xy, tip_xy=None, fs=13):
    if tip_xy is None:
        ax.text(*label_xy, text, fontsize=fs, ha="left", va="center")
    else:
        ax.annotate(text, xy=tip_xy, xytext=label_xy, fontsize=fs,
                    ha="center", va="center",
                    arrowprops=dict(arrowstyle="-|>", color="black",
                                    lw=1.1, mutation_scale=13))


def build_fig4():
    fig, axes = plt.subplots(2, 2, figsize=(7.6, 7.6))
    fig.subplots_adjust(left=0.004, right=0.996, top=0.996, bottom=0.004,
                        wspace=0.015, hspace=0.015)
    a, b, c, d = axes.ravel()

    dress(a, panel("Sam5-NO7286"), "a)")
    note(a, F111, (215, 1040), (97, 780))
    note(a, G111, (330, 950), (494, 772))
    note(a, A110, (360, 520), (521, 726))
    note(a, G200, (760, 430), (668, 590))
    note(a, F311, (800, 1140), (600, 1308))
    note(a, A200, (1020, 1080), None)
    note(a, G220, (760, 240), (1164, 420))

    dress(b, panel("Sam6-NO7280"), "b)")
    note(b, G220, (830, 150), None)
    note(b, A211, (1170, 330), None)
    note(b, G200, (470, 380), None)
    note(b, A200, (860, 640), None)
    note(b, F200, (330, 1000), (204, 772))

    dress(c, panel("Sam7-NO7271"), "c)")
    note(c, G220, (860, 180), None)
    note(c, A110, (300, 490), (518, 712))
    note(c, G111, (330, 1030), (485, 878))
    note(c, A200, (900, 920), None)
    note(c, B100, (300, 1200), (200, 768))
    note(c, B200, (1150, 1445), (904, 1290))

    dress(d, panel("Sam8-NO7265"), "d)")
    note(d, G200, (770, 530), (678, 730))

    fig.savefig(os.path.join(OUT_DIR, "Figure_4.jpg"), dpi=400,
                pil_kwargs={"quality": 95})
    plt.close(fig)


def build_fig8():
    fig, ax = plt.subplots(figsize=(3.9, 3.9))
    fig.subplots_adjust(left=0.008, right=0.992, top=0.992, bottom=0.008)
    dress(ax, panel("Sam1-NO7325"))
    note(ax, G200, (840, 900), (678, 776), fs=11)
    note(ax, A110, (320, 480), (515, 707), fs=11)
    note(ax, G111, (280, 1240), (438, 1098), fs=11)
    fig.savefig(os.path.join(OUT_DIR, "Figure_8.jpg"), dpi=400,
                pil_kwargs={"quality": 95})
    plt.close(fig)


def chi(name):
    c = np.loadtxt(os.path.join(CHI_DIR, name + ".chi"), skiprows=4)
    m = (c[:, 0] >= 2.0) & (c[:, 0] <= 6.0)
    return c[m, 0], c[m, 1]


def build_fig6():
    fig, (top, bot) = plt.subplots(2, 1, figsize=(5.6, 6.5), sharex=True)
    fig.subplots_adjust(left=0.115, right=0.97, top=0.985, bottom=0.075,
                        hspace=0.08)

    x0, y0 = chi("Sam5-NO7286")
    x1, y1 = chi("Sam6-NO7280")
    top.plot(x0, y0, color=ORANGE, lw=1.3, label="0% strain")
    top.plot(x1, y1, color=TEAL, lw=1.3, label="10% strain")
    for t, xy in [(F200, (2.44, 235)), (G111, (3.10, 1250)), (A110, (3.63, 1600)),
                  (G200, (3.97, 850)), (A200, (4.99, 330)), (G220, (5.58, 400))]:
        top.text(*xy, t, fontsize=11, ha="center")
    top.text(0.025, 0.93, "a)", transform=top.transAxes, fontsize=15, va="top")

    x2, y2 = chi("Sam7-NO7271")
    x3, y3 = chi("Sam8-NO7265")
    bot.plot(x2, y2, color=ORANGE, lw=1.3, label="0% strain")
    bot.plot(x3, y3 / 1.625, color=TEAL, lw=1.3, label="8% strain")
    for t, xy in [(B100, (2.47, 260)), (G111, (3.18, 700)), (A110, (3.62, 1650)),
                  (G200, (3.97, 320)), (A200, (4.98, 700)), (G220, (5.58, 250))]:
        bot.text(*xy, t, fontsize=11, ha="center")
    bot.text(0.025, 0.93, "b)", transform=bot.transAxes, fontsize=15, va="top")

    for ax in (top, bot):
        ax.set_xlim(2, 6)
        ax.set_ylim(0, 1800)
        ax.set_yticks([0, 400, 800, 1200, 1600])
        ax.set_ylabel("Intensity", fontsize=13)
        ax.legend(frameon=False, fontsize=12, loc="upper right")
        ax.tick_params(labelsize=11)
    bot.set_xlabel(r"2$\theta$ (°)", fontsize=13)

    fig.savefig(os.path.join(OUT_DIR, "Figure_6.jpg"), dpi=400,
                pil_kwargs={"quality": 95})
    plt.close(fig)


if __name__ == "__main__":
    build_fig4()
    build_fig8()
    build_fig6()
    for f in ("Figure_4.jpg", "Figure_6.jpg", "Figure_8.jpg"):
        im = Image.open(os.path.join(OUT_DIR, f))
        print(f, im.size, f"{os.path.getsize(os.path.join(OUT_DIR, f)) / 1e6:.1f} MB")
