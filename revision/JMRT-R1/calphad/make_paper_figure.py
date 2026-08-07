"""Build the manuscript figure from the step-diagram data.

Same data and same plotting rules as plot_step_diagrams.py (absent phases drawn as
zero, partitioned bcc drawn as one continuous curve with the ordered portion shaded),
but restyled for the paper:

  * alloy names match the manuscript (Omori-alloy / AI-alloy), not the script's
    internal keys
  * the 1200 degC solution-treatment temperature is marked on every panel, because
    the whole argument is read off that vertical line
  * no figure-level title; the caption carries it

Writes figures/Figure_7.png. Run plot_step_diagrams.py instead for the diagnostic
versions of all three databases.
"""
import os
from collections import OrderedDict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, 'results', 'step_diagrams.csv')
OUT = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'figures', 'Figure_7.png'))

DATABASE = 'mpea-02b'
T_SOLUTION = 1200.0
MIN_SHOW = 0.005
NONCONV = '__NONCONVERGED__'

PANELS = [
    ('benchmark', '(a)  Omori-alloy',
     'Fe–34.1Mn–15.2Al–7.8Ni–0.04C'),
    ('llm', '(b)  AI-alloy',
     'Fe–29.8Mn–11.9Al–4.2Ni–2.0Si–0.45C'),
    ('llm_noC', '(c)  AI-alloy, carbon removed',
     'all other elements held fixed'),
]

C_BCC = '#c1272d'
C_ORD = '#4b9b4b'
C_FCC = '#1f6fb4'
C_MN = '#e08214'
C_CARB = '#7b52a1'

PLAIN = OrderedDict([
    ('A1_FCC', (r'fcc $\gamma$', C_FCC)),
    ('CUB_A13', (r'$\beta$-Mn', C_MN)),
    ('M23C6_D84', (r'M$_{23}$C$_6$', C_CARB)),
])


def series(adf, label, temps):
    """Full-grid series: measured where present, 0 where the phase is absent."""
    have = adf[adf['label'] == label].groupby('T_C')['fraction'].sum()
    return np.array([have.get(t, 0.0) for t in temps], dtype=float)


def main():
    df = pd.read_csv(CSV)
    sub = df[(df['database'] == DATABASE) & (df['label'] != NONCONV)]

    fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.4), sharey=True)
    handles = OrderedDict()

    for i, (ax, (alloy, tag, comp)) in enumerate(zip(axes, PANELS)):
        adf = sub[sub['alloy'] == alloy]
        temps = np.array(sorted(adf['T_C'].unique()))

        total = series(adf, 'B2_BCC[A2]', temps) + series(adf, 'B2_BCC[ordered]', temps)
        ordered = series(adf, 'B2_BCC[ordered]', temps)

        ax.axvline(T_SOLUTION, color='0.35', lw=1.0, ls=(0, (5, 4)), zorder=1)
        if i == 0:
            ax.text(T_SOLUTION - 18, 50, '1200 °C solution treatment', rotation=90,
                    ha='right', va='center', fontsize=8, color='0.30')

        band = ax.fill_between(temps, 0, 100 * ordered, color=C_ORD, alpha=0.40, lw=0,
                               zorder=2)
        line, = ax.plot(temps, 100 * total, color=C_BCC, lw=2.1, zorder=4)
        handles.setdefault('B2 (ordered fraction of the bcc)', band)
        handles.setdefault(r'bcc $\alpha$ (total)', line)

        for label, (name, colour) in PLAIN.items():
            y = series(adf, label, temps)
            if y.max() < MIN_SHOW:
                continue
            line, = ax.plot(temps, 100 * y, color=colour, lw=2.1, zorder=3)
            handles.setdefault(name, line)

        ax.set_title('%s\n%s' % (tag, comp), fontsize=9.5, linespacing=1.35)
        ax.set_xlabel('Temperature (°C)')
        ax.set_xlim(400, 1400)
        ax.set_ylim(-2, 102)
        ax.set_xticks([400, 600, 800, 1000, 1200, 1400])
        ax.grid(alpha=0.22, lw=0.6)

    axes[0].set_ylabel('Equilibrium phase fraction (mol %)')
    fig.legend(list(handles.values()), list(handles.keys()), loc='lower center',
               ncol=len(handles), fontsize=9, frameon=False, handlelength=1.8,
               columnspacing=2.0, bbox_to_anchor=(0.5, 0.0))
    fig.tight_layout(rect=(0, 0.075, 1, 1))
    fig.savefig(OUT, dpi=400)
    plt.close(fig)
    print('wrote %s' % OUT)


if __name__ == '__main__':
    main()
