"""Fig. 10 — cyclic tensile records of the LLM-alloy in the prolonged-anneal and
cyclically heat-treated conditions, plotted from the raw Instron exports.

Added for JMRT Round 2 (Reviewer 3, point 7). Every curve is engineering stress from the
report diameter and crosshead strain over the gauge length printed in that report's
header; the gauge differs between panels and is stated in each panel title, so strains
are NOT comparable across panels (Sec. 2.4 of the manuscript).

Sources (copied from E:\\FE-SMA\\mechanical into revision/JMRT-R2/mechanical/raw-exports/):
  (a) Fe-SMA-FC_15.csv   0.36 mm wire, 1200 C/40 min + 200 C/3 h, 127 mm gauge  (report: 0.8 %)
  (b) Fe-SMA-FC_16.csv   0.36 mm wire, 1200 C/80 min,               127 mm gauge  (report: 0.5 %)
  (c) Fe-SMA-FC_17/18    1.29 mm rod, two-cycle 1200<->900 C,        127 mm gauge  (568 / 608 MPa, 1.0 %)
  (d) Fe-SMA-FC_19.csv   1.06 mm rod, three-cycle + 200 C/3 h,       127 mm gauge  (478 MPa, 0.5 %)
  (e) Frankie-6mm_2.csv  1.06 mm rod, three-cycle + 200 C/3 h,       6.0 mm gauge  (1006 MPa, 11.9 %)
  (f) oct-11-25_2.csv    0.36 mm wire, quartz-tube 1200 C cycle,     25.4 mm gauge (1020 MPa; the report's
                         51.3 % includes crosshead travel after fracture at ~26 %; curve cut at fracture)
"""
import csv
import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, '..', 'revision', 'JMRT-R2', 'mechanical', 'raw-exports')
OUT = os.path.join(HERE, 'Figure_10.png')

LBF_TO_N = 4.4482216
LINE = '#1f6f7a'   # same line colour as Fig. 2


def load(name, dia_in, gauge_in, cut_at_fracture=False):
    area = math.pi * (dia_in * 25.4 / 2.0) ** 2  # mm^2
    e, s = [], []
    with open(os.path.join(RAW, name), newline='') as f:
        r = csv.reader(f)
        next(r); next(r)
        for row in r:
            try:
                d, F = float(row[1]), float(row[2])
            except (ValueError, IndexError):
                continue
            e.append(d / gauge_in * 100.0)
            s.append(F * LBF_TO_N / area)
    if cut_at_fracture:
        smax = max(s)
        imax = s.index(smax)
        for i in range(imax, len(s)):
            if s[i] < 0.05 * smax:
                e, s = e[:i + 1], s[:i + 1]
                break
    return e, s


PANELS = [
    ('a', '0.36 mm wire, 1200 °C/40 min + 200 °C/3 h\n127 mm gauge',
     [('Fe-SMA-FC_15.csv', 0.01410, 5.0)], 1.2, 0.2, 1000, 200),
    ('b', '0.36 mm wire, 1200 °C/80 min\n127 mm gauge',
     [('Fe-SMA-FC_16.csv', 0.01280, 5.0)], 1.2, 0.2, 1000, 200),
    ('c', '≈1.3 mm rod, two-cycle 1200 ↔ 900 °C (n = 2)\n127 mm gauge',
     [('Fe-SMA-FC_17.csv', 0.0509, 5.0), ('Fe-SMA-FC_18.csv', 0.0509, 5.0)], 1.2, 0.2, 1000, 200),
    ('d', '≈1.06 mm rod, three-cycle + 200 °C/3 h\n127 mm gauge',
     [('Fe-SMA-FC_19.csv', 0.0418, 5.0)], 1.2, 0.2, 1000, 200),
    ('e', '≈1.06 mm rod, three-cycle + 200 °C/3 h\n6.0 mm gauge',
     [('Frankie-Fe-SMA-6mm-gauge_2.csv', 0.0418, 0.236)], 14, 2, 1200, 200),
    ('f', '0.36 mm wire, quartz-tube 1200 °C cycle\n25.4 mm gauge',
     [('Fe-SMA-oct-11-25_2.csv', 0.01402, 1.0)], 30, 5, 1200, 200),
]


def main():
    # 190 mm = Elsevier double-column width, matching Fig. 2's build.
    fig, axs = plt.subplots(2, 3, figsize=(190 / 25.4, 110 / 25.4),
                            constrained_layout=True)
    for ax, (tag, title, series, xmax, xstep, ymax, ystep) in zip(axs.flat, PANELS):
        cut = (tag == 'f')
        for k, (fn, dia, gl) in enumerate(series):
            e, s = load(fn, dia, gl, cut_at_fracture=cut)
            ax.plot(e, s, color=LINE if k == 0 else '#7fb1b8', lw=0.7,
                    solid_joinstyle='round')
        ax.set_xlim(0, xmax)
        ax.set_ylim(0, ymax)
        ax.xaxis.set_major_locator(MultipleLocator(xstep))
        ax.yaxis.set_major_locator(MultipleLocator(ystep))
        ax.tick_params(labelsize=6.5, width=0.6, length=2.5, pad=1.5)
        for sp in ax.spines.values():
            sp.set_linewidth(0.6)
        ax.set_xlabel('Engineering strain (%)', fontsize=7, labelpad=1.5)
        ax.set_ylabel('Applied stress (MPa)', fontsize=7, labelpad=1.5)
        ax.set_title(title, fontsize=7, pad=3)
        ax.text(0.035, 0.955, '(%s)' % tag, transform=ax.transAxes,
                fontsize=8, fontweight='bold', va='top', ha='left')
    fig.savefig(OUT, dpi=600)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
