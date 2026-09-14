"""Is the PrecHiMn-04 gamma-only band at 1210-1290 C real, or a missed minimum?

compare_gm.py (2026-09-14) settled that the 1200 C duplex row of Table 3 is the lower-energy
state in PrecHiMn-04 (GM -100985.8 J/mol against -100898.6 for 100 % gamma). But every grid
tried (pdens 500-3000, with and without the other phases) returns 100 % gamma from 1210 C
upward. A phase fraction cannot jump from 64.5 % alpha to zero across 10 C inside a
two-phase field of a five-component alloy at fixed composition -- fractions vary
continuously there -- so one of the two rows is a solver miss. This restricts the phase
list to bcc + fcc + liquid, which makes a much denser grid affordable, and reports GM beside
the all-phase pdens-500 value at each temperature. If the dense two-phase run finds a
duplex with lower GM than the gamma-only state, the band is an artifact; if it agrees with
100 % gamma, the database really does close the alpha field from above at ~1210 C.

    python recheck_prechimn_dense.py
"""
import io
import os

import numpy as np
from pycalphad import Database, equilibrium, variables as v

from step_diagrams import DBDIR, OUTDIR, RUNS, conditions_for
from compare_gm import constitution

DENSE = [6000, 12000]
TEMPS_C = list(range(1200, 1301, 10))


def main():
    cfg = next(c for c in RUNS if c['key'] == 'PrecHiMn-04')
    dbf = Database(os.path.join(DBDIR, cfg['file']))
    comps = cfg['elements'] + ['VA']
    phases = [p for p in cfg['phases'] if p in dbf.phases]
    two = ['A1_FCC', cfg['bcc'], 'LIQUID']
    conds, frac = conditions_for('llm', cfg['elements'])
    conds = dict(conds)
    conds.update({v.T: np.array(TEMPS_C, dtype=float) + 273.15, v.P: 101325, v.N: 1})

    variants = [('all phases, pdens 500', equilibrium(dbf, comps, phases, conds,
                                                       calc_opts={'pdens': 500}))]
    for pd in DENSE:
        variants.append(('bcc + fcc + liquid, pdens %d' % pd,
                         equilibrium(dbf, comps, two, conds, calc_opts={'pdens': pd})))

    out = io.open(os.path.join(OUTDIR, 'prechimn_dense_check.txt'), 'w', encoding='utf-8')
    out.write(u'PrecHiMn-04 / LLM-alloy, dense two-phase check (2026-09-14)\n')
    for ti, tc in enumerate(TEMPS_C):
        rows = [(name, ) + constitution(eq, ti) for name, eq in variants]
        best = min(r[1] for r in rows if r[1] == r[1])
        out.write(u'\n  %d C\n' % tc)
        for name, gm, desc in rows:
            mark = '  <-- lowest' if abs(gm - best) < 1e-6 else ''
            line = u'    %-32s GM %12.2f J/mol   %s%s\n' % (name, gm, desc, mark)
            out.write(line)
            print(line, end='', flush=True)
    out.close()
    print('-> %s' % os.path.join(OUTDIR, 'prechimn_dense_check.txt'))


if __name__ == '__main__':
    main()
