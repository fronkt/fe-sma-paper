"""Rebuild Fig. 2 from the raw Instron exports — answers R2 Results&Discussion #3 and #4.

#3: the published panel axes clip their last tick label ("2.5" renders as "2.", "10" as "1(")
    because the panels were laid out by hand and overlap. Rebuilding with constrained_layout
    and explicit tick locators removes the failure mode rather than nudging it.
#4: Table 2 lists eight anneal conditions and the published figure shows six. All eight of the
    annealed conditions are drawn here, so the 700 / 900 / 1100 degC curves no longer have to be
    described as "omitted for space" -- the reader can see that they interpolate.

Provenance. Every curve is a raw export from `Fe-SMA-FC.is_tcyclic` (Fort Wayne Metals,
8 Sep 2025), spool numbers as printed in that report. Stress is load / initial area using the
per-spool diameter from the report, not a nominal 0.36 mm. Strain is crosshead extension over a
127 mm (5 in) gauge, which is the value the instrument recorded and the only one consistent with
Table 2: it reproduces the published elongation column to three significant figures
(600 -> 2.26 vs 2.3; 800 -> 24.02 vs 24.0; 1000 -> 33.41 vs 33.4; 1200 -> 23.89 vs 23.9) and with
the 0.25 in/min crosshead speed gives 8.3e-4 /s, the strain rate Sec. 2.4 quotes as 1e-3 /s.
See ../processing/PROCESSING-AND-REPLICATES.md; Sec. 2.4's "13 mm" is inconsistent with both.

The as-drawn panel is NOT reproduced: no trace matching Table 2's as-drawn row (UTS 1925 MPa at
2.0 % elongation) exists in any export folder on the drive. Add it to SPOOLS when S. Cai supplies
it and the layout picks it up automatically.

    python rebuild_figure2.py
"""
import csv
import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'E:/FE-SMA/mechanical/Fe-SMA-FC.is_tcyclic_Exports'
# Adopted as the manuscript figure 2026-08-14 (was Figure_2_rebuilt.png here); the PDF
# proof stays in this folder.
OUT = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'figures', 'Figure_2.png'))
PDF = os.path.join(HERE, 'Figure_2_rebuilt.pdf')

LBF_N = 4.4482216
IN_MM = 25.4
GAUGE_MM = 5.0 * IN_MM              # 127.0 mm, the instrument's gauge for this run

# (spool, label, diameter/in, x max /%, y max /MPa) -- diameters from the Instron report
SPOOLS = [
    (3,  u'600 \u00b0C',                  0.01410,  2.5, 2500),
    (4,  u'700 \u00b0C',                  0.01415,  2.5, 2500),
    (5,  u'800 \u00b0C',                  0.01410, 10.0, 1500),
    (6,  u'900 \u00b0C',                  0.01415, 10.0, 1500),
    (7,  u'1000 \u00b0C',                 0.01404, 10.0, 1500),
    (8,  u'1100 \u00b0C',                 0.01399, 10.0, 1500),
    (9,  u'1200 \u00b0C',                 0.01384, 10.0, 1500),
    (11, u'1200 \u00b0C + 200 \u00b0C/3 h', 0.01370, 10.0, 1500),
]

LINE = '#1f6f7a'


def read_trace(spool):
    """(strain %, stress MPa) from one export. Header is two rows: names, then units."""
    path = os.path.join(SRC, 'Fe-SMA-FC_%d.csv' % spool)
    ext, load = [], []
    with open(path, newline='', encoding='utf-8', errors='ignore') as fh:
        r = csv.reader(fh)
        next(r, None)
        next(r, None)
        for row in r:
            if len(row) < 3:
                continue
            try:
                ext.append(float(row[1]))
                load.append(float(row[2]))
            except ValueError:
                continue
    return ext, load


def main():
    if not os.path.isdir(SRC):
        raise SystemExit('source not reachable: %s\n(the E: drive must be mounted)' % SRC)

    # 190 mm is Elsevier's double-column width; 4 x 2 keeps each panel above 45 mm wide.
    fig, axes = plt.subplots(2, 4, figsize=(190 / 25.4, 95 / 25.4),
                             constrained_layout=True)

    for ax, (spool, label, dia_in, xmax, ymax) in zip(axes.ravel(), SPOOLS):
        ext, load = read_trace(spool)
        area = math.pi / 4 * (dia_in * IN_MM) ** 2
        strain = [e * IN_MM / GAUGE_MM * 100 for e in ext]
        stress = [f * LBF_N / area for f in load]

        ax.plot(strain, stress, color=LINE, lw=0.7, solid_joinstyle='round')
        ax.set_xlim(0, xmax)
        ax.set_ylim(0, ymax)
        # Explicit locators: the last label is placed *at* the limit, and constrained_layout
        # then reserves room for it. This is the actual fix for the clipping in R2 R&D#3.
        ax.xaxis.set_major_locator(MultipleLocator(0.5 if xmax <= 2.5 else 2))
        ax.yaxis.set_major_locator(MultipleLocator(500))
        ax.tick_params(labelsize=6.5, width=0.6, length=2.5, pad=1.5)
        for s in ax.spines.values():
            s.set_linewidth(0.6)
        ax.set_title(label, fontsize=7, pad=3)

    for i, ax in enumerate(axes.ravel()):
        ax.text(0.035, 0.955, '(%s)' % 'abcdefgh'[i], transform=ax.transAxes,
                fontsize=8, fontweight='bold', va='top', ha='left')
    for ax in axes[-1]:
        ax.set_xlabel(u'Engineering strain (%)', fontsize=7, labelpad=1.5)
    for ax in axes[:, 0]:
        ax.set_ylabel(u'Applied stress (MPa)', fontsize=7, labelpad=1.5)
    # Panels (c)-(h) share a scale with (c)/(g) but sit in different columns, so the strain
    # axis is labelled on every bottom panel and the stress axis on both left-hand panels only.
    axes[0][2].set_xlabel(u'Engineering strain (%)', fontsize=7, labelpad=1.5)
    axes[0][3].set_xlabel(u'Engineering strain (%)', fontsize=7, labelpad=1.5)

    fig.savefig(OUT, dpi=600)
    fig.savefig(PDF)
    print('wrote %s (+ %s)' % (OUT, PDF))

    print('\nreconstruction check against Table 2:')
    check = {3: (2293, 2.3), 4: (2009, 2.2), 5: (1216, 24.0), 6: (1078, 29.7),
             7: (967, 33.4), 8: (947, 29.7), 9: (938, 23.9)}
    for spool, label, dia_in, _, _ in SPOOLS:
        if spool not in check:
            continue
        ext, load = read_trace(spool)
        area = math.pi / 4 * (dia_in * IN_MM) ** 2
        uts = max(load) * LBF_N / area
        el = max(ext) * IN_MM / GAUGE_MM * 100
        pu, pe = check[spool]
        print('  spool %-2d %-12s UTS %7.1f vs %5d (%+.1f%%)   elong %6.2f vs %5.1f'
              % (spool, label, uts, pu, 100 * (uts - pu) / pu, el, pe))


if __name__ == '__main__':
    main()
