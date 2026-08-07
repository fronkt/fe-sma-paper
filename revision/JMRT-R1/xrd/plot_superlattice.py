"""Superlattice-region comparison: is B2 present, and is D0_3 present?

Left panel  -- the diagnostic low-angle window where ONLY superlattice reflections
               can appear. A bcc + fcc mixture puts no intensity here at all, which
               makes it a clean presence/absence test.
Right panel -- the fundamental reflections, for scale.

Answers R3#8 ("absence of a B2 peak does not prove absence of B2") with a number,
and tests the manuscript's 4 % D0_3 assignment directly.
"""
import glob
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

LAMBDA = 0.125870
A_BCC = 2.89816
A_FCC = 3.64862
CHI_DIR = r'E:\FE-SMA\synchrotron.chi'
HERE = os.path.dirname(os.path.abspath(__file__))

PICK = [
    ('Sam5-NO7286.chi', 'LLM-alloy, 1200 °C / 4 fpm, undeformed', '#c0392b'),
    ('Sam1-NO7325.chi', 'LLM-alloy, 3-cycle AGG', '#e67e22'),
    ('Sam7-NO7271.chi', 'Benchmark, 1200 °C / 4 fpm, undeformed', '#2471a3'),
    ('Sam7-NO7274.chi', 'Benchmark, repeat exposure', '#5dade2'),
]


def two_theta(d):
    return 2.0 * np.degrees(np.arcsin(LAMBDA / (2.0 * d)))


def load_chi(path):
    tt, y = [], []
    with open(path, 'r', errors='replace') as fh:
        for line in fh:
            p = line.split()
            if len(p) == 2:
                try:
                    tt.append(float(p[0])); y.append(float(p[1]))
                except ValueError:
                    pass
    return np.array(tt), np.array(y)


def baseline(y, n):
    pad = np.pad(y, n, mode='edge')
    base = np.array([pad[i:i + 2 * n + 1].min() for i in range(len(y))])
    k = np.ones(n) / n
    return np.convolve(np.pad(base, n // 2, mode='edge'), k, mode='same')[:len(y)]


MARKS = [
    (2 * A_BCC / np.sqrt(3), r'D0$_3$ (111)' '\n' 'unique to D0$_3$', '#7d3c98'),
    (A_BCC,                  r'B2 (100)' '\n' r'= D0$_3$ (200)', '#148f77'),
    (A_BCC / np.sqrt(3),     r'B2 (111)', '#148f77'),
]

fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 5.2),
                               gridspec_kw={'width_ratios': [1.15, 1]})

for fname, label, colour in PICK:
    path = os.path.join(CHI_DIR, fname)
    if not os.path.exists(path):
        continue
    tt, y = load_chi(path)
    net = y - baseline(y, 60)
    scale = net.max()
    net = 100.0 * net / scale

    m = (tt > 1.9) & (tt < 2.75)
    axL.plot(tt[m], net[m], color=colour, lw=1.3, label=label)
    m2 = (tt > 3.2) & (tt < 4.2)
    axR.plot(tt[m2], net[m2], color=colour, lw=1.3, label=label)

for d, name, col in MARKS:
    t = two_theta(d)
    for ax in (axL, axR):
        if ax.get_xlim()[0] < t < ax.get_xlim()[1] or ax is axL:
            pass
    if 1.9 < t < 2.75:
        axL.axvline(t, color=col, ls='--', lw=1.0, alpha=0.8)
        axL.annotate(name, xy=(t, 7.2), ha='center', va='top', fontsize=8,
                     color=col,
                     bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=col, lw=0.8))

for d, name, col in [(A_FCC / np.sqrt(3), r'fcc $\gamma$ (111)', '#b03a2e'),
                     (A_BCC / np.sqrt(2), r'bcc $\alpha$ (110)', '#1f618d'),
                     (A_FCC / 2, r'fcc $\gamma$ (200)', '#b03a2e')]:
    t = two_theta(d)
    axR.axvline(t, color=col, ls=':', lw=1.0, alpha=0.7)
    axR.annotate(name, xy=(t, 104), ha='center', va='bottom', fontsize=8, color=col)

axL.set_ylim(0, 8)
axL.set_xlim(1.9, 2.75)
axL.set_title('Superlattice window — only ordered phases can appear here', fontsize=10)
axL.set_xlabel(r'2$\theta$ (°),  $\lambda$ = 0.12587 Å')
axL.set_ylabel('Net intensity (% of strongest reflection)')
axL.legend(fontsize=8, loc='upper left')
axL.grid(alpha=0.25, lw=0.6)

axR.set_ylim(0, 118)
axR.set_xlim(3.2, 4.2)
axR.set_title('Fundamental reflections, for scale', fontsize=10)
axR.set_xlabel(r'2$\theta$ (°)')
axR.grid(alpha=0.25, lw=0.6)

fig.suptitle('SSRF BL12SW — B2 is present in the benchmark and absent in the LLM-alloy; '
             r'no D0$_3$ (111) in either', fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.94))
out = os.path.join(HERE, 'superlattice_window.png')
fig.savefig(out, dpi=200)
print('wrote %s' % out)
