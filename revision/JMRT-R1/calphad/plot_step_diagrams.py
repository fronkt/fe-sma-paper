"""Plot the step diagrams produced by step_diagrams.py.

One figure per database; one panel per alloy. Phase fraction vs temperature.

Two things this gets right that a naive plot does not:

  * **Absent phases are plotted as zero, not omitted.** A phase that is not stable has
    fraction 0, and a phase entering at a boundary grows from 0. Dropping those points
    makes lines start and stop in mid-air at whatever value the first grid point inside
    the field happens to have, which misreads as a discontinuity in the physics.
  * **Non-converged temperatures break the line** rather than being interpolated across.
    step_diagrams.py records them explicitly; they are drawn as a grey band so a gap in
    the data never looks like a phase boundary.

Composition sets carrying the same label are summed for the plot; the CSV keeps them
separate.
"""
import os
from collections import OrderedDict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'results')
NONCONV = '__NONCONVERGED__'
MIN_SHOW = 0.005          # a phase must exceed 0.5 % somewhere to earn a line

TITLES = {
    'benchmark': 'Benchmark  Fe–34.1Mn–15.2Al–7.8Ni–0.04C',
    'llm':       'LLM-alloy  Fe–29.8Mn–11.9Al–4.2Ni–2.0Si–0.45C',
    'llm_noC':   'LLM-alloy, carbon removed  (all else fixed)',
}

PALETTE = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b',
           '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#393b79', '#a55194']

PRETTY = {
    'B2_BCC[A2]':       r'bcc $\alpha$ (A2, disordered)',
    'B2_BCC[ordered]':  r'B2 (ordered bcc)',
    'BCC_4SL[A2]':      r'bcc $\alpha$ (A2, disordered)',
    'BCC_4SL[ordered]': r'ordered bcc (B2 / D0$_3$)',
    'BCC_A2':           r'bcc $\alpha$ (A2)',
    'BCC_B2':           r'B2 (ordered bcc)',
    'A1_FCC':           r'fcc $\gamma$',
    'FCC_A1':           r'fcc $\gamma$',
    'KAPPA_E21':        r'$\kappa$-carbide (Fe,Mn)$_3$AlC',
    'K_CARB':           r'$\kappa$-carbide (Fe,Mn)$_3$AlC',
    'CEMENTITE_D011':   'cementite',
    'CEMENTITE':        'cementite',
    'LIQUID:L':         'liquid',
    'LIQUID':           'liquid',
    'CUB_A13':          r'$\beta$-Mn',
    'BETA_MN':          r'$\beta$-Mn',
    'CBCC_A12':         r'$\alpha$-Mn',
    'ALPHA_MN':         r'$\alpha$-Mn',
    'GRAPHITE_A9':      'graphite',
    'GRAPHITE':         'graphite',
    'M23C6_D84':        r'M$_{23}$C$_6$',
    'M23C6':            r'M$_{23}$C$_6$',
    'M7C3_D101':        r'M$_7$C$_3$',
    'M7C3':             r'M$_7$C$_3$',
    'G_PHASE':          'G phase',
    'M3P':              r'M$_3$P',
    'M2P':              r'M$_2$P',
}


def pretty(label):
    return PRETTY.get(label, label.replace('_', ' '))


def series_for(adf, label, temps, bad):
    """Full-grid series: measured value, 0 where the phase is absent,
    NaN where equilibrium did not converge."""
    have = (adf[adf['label'] == label]
            .groupby('T_C')['fraction'].sum())
    y = np.array([have.get(t, 0.0) for t in temps], dtype=float)
    y[np.isin(temps, list(bad))] = np.nan
    return y


def main():
    df = pd.read_csv(os.path.join(OUTDIR, 'step_diagrams.csv'))

    for db in df['database'].unique():
        sub = df[df['database'] == db]
        alloys = [a for a in ['benchmark', 'llm', 'llm_noC'] if a in set(sub['alloy'])]
        if not alloys:
            continue

        real = sub[sub['label'] != NONCONV]
        labels = (real.groupby('label')['fraction'].max()
                  .sort_values(ascending=False).index.tolist())
        colours = {L: PALETTE[i % len(PALETTE)] for i, L in enumerate(labels)}

        fig, axes = plt.subplots(1, len(alloys), figsize=(5.4 * len(alloys), 4.6),
                                 sharey=True, squeeze=False)
        axes = axes[0]

        for ax, alloy in zip(axes, alloys):
            adf = sub[sub['alloy'] == alloy]
            temps = np.array(sorted(adf['T_C'].unique()))
            bad = set(adf[adf['label'] == NONCONV]['T_C'])

            # shade any non-converged region so a gap never reads as a boundary
            for t in sorted(bad):
                ax.axvspan(t - 5, t + 5, color='0.85', zorder=0, lw=0)

            # A partitioned phase (B2_BCC / BCC_4SL) is ONE phase whose degree of
            # order varies. Drawing "[A2]" and "[ordered]" as separate lines makes the
            # order-disorder transition look like one phase vanishing and another
            # appearing, when the total bcc fraction is perfectly continuous through it.
            # So: plot the total as a single line, and shade the ordered portion under it.
            partitioned = sorted({L.split('[')[0] for L in adf['label'].unique()
                                  if '[' in str(L)})
            plain = [L for L in adf['label'].unique()
                     if L != NONCONV and '[' not in str(L)]

            present = (adf[adf['label'] != NONCONV]
                       .groupby('label')['fraction'].max()
                       .sort_values(ascending=False))

            for stem in partitioned:
                tot = sum(series_for(adf, '%s[%s]' % (stem, s), temps, bad)
                          for s in ('A2', 'ordered'))
                ordered = series_for(adf, '%s[ordered]' % stem, temps, bad)
                if np.nanmax(tot) < MIN_SHOW:
                    continue
                col = colours.get('%s[A2]' % stem, PALETTE[0])
                ax.plot(temps, 100 * tot, color=col, lw=2.0,
                        label=r'bcc $\alpha$ (total)', solid_capstyle='round')
                if np.nanmax(ordered) >= MIN_SHOW:
                    ocol = colours.get('%s[ordered]' % stem, PALETTE[2])
                    ax.fill_between(temps, 0, 100 * ordered, color=ocol, alpha=0.45,
                                    lw=0, label=pretty('%s[ordered]' % stem))

            for label in plain:
                if present.get(label, 0) < MIN_SHOW:
                    continue
                y = series_for(adf, label, temps, bad)
                ax.plot(temps, 100 * y, color=colours[label], lw=2.0,
                        label=pretty(label), solid_capstyle='round')

            if bad:
                ax.plot([], [], color='0.85', lw=8, label='not converged')
            ax.set_title(TITLES.get(alloy, alloy), fontsize=9)
            ax.set_xlabel('Temperature (°C)')
            ax.set_xlim(temps.min(), temps.max())
            ax.set_ylim(-2, 102)
            ax.grid(alpha=0.25, lw=0.6)

        # One shared legend below the axes. Per-panel legends sat on top of the
        # curves they were labelling.
        handles = OrderedDict()
        for ax in axes:
            for handle, label in zip(*ax.get_legend_handles_labels()):
                handles.setdefault(label, handle)

        axes[0].set_ylabel('Equilibrium phase fraction (mol %)')
        fig.legend(list(handles.values()), list(handles.keys()), loc='lower center',
                   ncol=min(len(handles), 6), fontsize=8, frameon=False,
                   handlelength=1.8, columnspacing=1.8)
        fig.suptitle('Equilibrium step diagram — %s' % db, fontsize=11)
        fig.tight_layout(rect=(0, 0.07, 1, 0.94))
        out = os.path.join(OUTDIR, 'step_%s.png' % db.replace('.', '-'))
        fig.savefig(out, dpi=200)
        plt.close(fig)
        print('wrote %s' % out)


if __name__ == '__main__':
    main()
