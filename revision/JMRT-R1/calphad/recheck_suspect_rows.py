"""pdens-2000 re-check of the rows the liquid-included run flagged as solver-suspect.

The first liquid-included run (revision/JMRT-R2/calphad-liquid-check-2026-09-14/, pdens 500)
returned two sequences for the LLM-alloy that look like a coarse global grid missing the
bcc minimum rather than physics:

    PrecHiMn-04   1210-1290 C : 100 % A1_FCC, re-entrant between the alpha + gamma duplex
                                at 1200 C and alpha + liquid at 1300 C
    mpea-02b      1330-1340 C : gamma + liquid, then back to alpha + liquid at 1350 C

Those bands are re-run here at pdens 2000 and the constitution printed per temperature.
No CSV is touched. If the denser grid returns the duplex -> melting sequence, the pdens-500
rows are artifacts and the manuscript quotes the dense values; if it agrees with pdens 500,
the result stands and is disclosed as a database extrapolation. Either way the answer is
written to results/suspect_rows_pdens2000.txt.

    python recheck_suspect_rows.py
"""
import io
import os

import numpy as np
from pycalphad import Database, equilibrium, variables as v

from step_diagrams import (DBDIR, OUTDIR, RUNS, FRACTION_CUTOFF, ORDER_TOL,
                           conditions_for, dof_layout, order_parameter)

PDENS = 2000
ALLOY = 'llm'
BANDS = {'PrecHiMn-04': (1190, 1310), 'mpea-02b': (1270, 1360)}


def main():
    out = io.open(os.path.join(OUTDIR, 'suspect_rows_pdens2000.txt'), 'w', encoding='utf-8')
    out.write(u'Solver-suspect rows re-run at pdens %d (LLM-alloy, liquid included)\n' % PDENS)
    for cfg in RUNS:
        if cfg['key'] not in BANDS:
            continue
        lo, hi = BANDS[cfg['key']]
        dbf = Database(os.path.join(DBDIR, cfg['file']))
        comps = cfg['elements'] + ['VA']
        phases = [p for p in cfg['phases'] if p in dbf.phases]
        if 'LIQUID' not in phases:
            raise RuntimeError('%s: LIQUID missing -- the bug this script exists to check'
                               % cfg['key'])
        layout = dof_layout(dbf, comps, cfg['bcc'])
        conds, frac = conditions_for(ALLOY, cfg['elements'])
        temps = np.arange(lo, hi + 1, 10) + 273.15
        conds = dict(conds)
        conds.update({v.T: temps, v.P: 101325, v.N: 1})
        eq = equilibrium(dbf, comps, phases, conds, calc_opts={'pdens': PDENS})

        header = u'\n=== %s / %s, %d-%d C, pdens %d ===\n' % (cfg['key'], ALLOY, lo, hi, PDENS)
        out.write(header)
        print(header, end='', flush=True)
        for ti, temp in enumerate(temps):
            sl = eq.isel(T=ti).squeeze()
            names = np.atleast_1d(sl.Phase.values).flatten()
            fracs = np.atleast_1d(sl.NP.values).flatten()
            ys = np.atleast_2d(sl.Y.values)
            seen = {}
            for vi, (name, np_) in enumerate(zip(names, fracs)):
                name = str(name)
                if not name or np_ != np_ or np_ < FRACTION_CUTOFF:
                    continue
                label = name
                if name == cfg['bcc']:
                    op = order_parameter(ys[vi], layout)
                    if op is not None:
                        label = '%s[%s]' % (name, 'ordered' if op > ORDER_TOL else 'A2')
                seen[label] = seen.get(label, 0.0) + float(np_)
            desc = ', '.join('%s %.1f%%' % (k, 100 * val)
                             for k, val in sorted(seen.items(), key=lambda kv: -kv[1]))
            line = u'  %5.0f C : %s\n' % (float(temp) - 273.15,
                                          desc or '*** NOT CONVERGED ***')
            out.write(line)
            print(line, end='', flush=True)
    out.close()
    print('-> %s' % os.path.join(OUTDIR, 'suspect_rows_pdens2000.txt'))


if __name__ == '__main__':
    main()
