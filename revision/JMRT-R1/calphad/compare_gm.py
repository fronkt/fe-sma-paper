"""Which grid is right? Gibbs-energy arbitration of the LLM-alloy states on which pdens 500
and pdens 2000 disagree.

recheck_suspect_rows.py (pdens 2000, 2026-09-14) returned 100 % gamma where the pdens-500
run returned alpha + gamma (PrecHiMn-04, 1190-1290 C -- including the 1200 C row of
manuscript Table 3) and alpha + liquid (mpea-02b, 1290-1310 C). pycalphad's global
minimisation picks the lowest hyperplane it can see on its point grid and then refines
locally, so two grids can settle in different basins. The arbiter is the molar Gibbs
energy of the converged state: at fixed T, P and composition the lower GM is the
equilibrium the database actually describes, whatever grid found it.

For each listed temperature this computes
  * the unconstrained equilibrium at pdens 500, 1000, 2000, 3000
  * the equilibrium with the phase list restricted to fcc only, and to bcc + fcc only
    (pdens 2000), which forces the solver into the competing basin
and prints GM (J/mol) beside the constitution, marking the lowest.

    python compare_gm.py
"""
import io
import os

import numpy as np
from pycalphad import Database, equilibrium, variables as v

from step_diagrams import DBDIR, OUTDIR, RUNS, FRACTION_CUTOFF, conditions_for

ALLOY = 'llm'
TEMPS_C = [1150, 1200, 1250, 1280, 1290, 1300]
PDENS_LADDER = [500, 1000, 2000, 3000]


def constitution(eq, ti):
    sl = eq.isel(T=ti).squeeze()
    names = np.atleast_1d(sl.Phase.values).flatten()
    fracs = np.atleast_1d(sl.NP.values).flatten()
    seen = {}
    for name, np_ in zip(names, fracs):
        name = str(name)
        if not name or np_ != np_ or np_ < FRACTION_CUTOFF:
            continue
        seen[name] = seen.get(name, 0.0) + float(np_)
    gm = float(np.atleast_1d(sl.GM.values).flatten()[0])
    desc = ', '.join('%s %.1f%%' % (k, 100 * f)
                     for k, f in sorted(seen.items(), key=lambda kv: -kv[1]))
    return gm, desc or '*** NOT CONVERGED ***'


def main():
    out = io.open(os.path.join(OUTDIR, 'gm_comparison.txt'), 'w', encoding='utf-8')

    def emit(s):
        out.write(s)
        print(s, end='', flush=True)

    emit(u'Gibbs-energy arbitration, LLM-alloy, liquid included (2026-09-14)\n')
    temps_k = np.array(TEMPS_C, dtype=float) + 273.15
    for cfg in RUNS:
        if cfg['key'] == 'mc_fe':
            continue
        dbf = Database(os.path.join(DBDIR, cfg['file']))
        comps = cfg['elements'] + ['VA']
        phases = [p for p in cfg['phases'] if p in dbf.phases]
        if 'LIQUID' not in phases:
            raise RuntimeError('%s: LIQUID missing' % cfg['key'])
        fcc = [p for p in phases if p in ('A1_FCC', 'FCC_A1')]
        conds, frac = conditions_for(ALLOY, cfg['elements'])
        conds = dict(conds)
        conds.update({v.T: temps_k, v.P: 101325, v.N: 1})

        variants = []
        for pd in PDENS_LADDER:
            eq = equilibrium(dbf, comps, phases, conds, calc_opts={'pdens': pd})
            variants.append(('all phases, pdens %d' % pd, eq))
        eq = equilibrium(dbf, comps, fcc, conds, calc_opts={'pdens': 2000})
        variants.append(('fcc only, pdens 2000', eq))
        eq = equilibrium(dbf, comps, fcc + [cfg['bcc']], conds, calc_opts={'pdens': 2000})
        variants.append(('bcc + fcc only, pdens 2000', eq))
        eq = equilibrium(dbf, comps, fcc + [cfg['bcc'], 'LIQUID'], conds,
                         calc_opts={'pdens': 3000})
        variants.append(('bcc + fcc + liquid, pdens 3000', eq))

        emit(u'\n=== %s / %s ===\n' % (cfg['key'], ALLOY))
        for ti, tc in enumerate(TEMPS_C):
            rows = []
            for name, eq in variants:
                gm, desc = constitution(eq, ti)
                rows.append((name, gm, desc))
            finite = [r for r in rows if r[1] == r[1]]
            best = min(r[1] for r in finite) if finite else float('nan')
            emit(u'\n  %d C\n' % tc)
            for name, gm, desc in rows:
                mark = '  <-- lowest' if (gm == gm and abs(gm - best) < 1e-6) else ''
                emit(u'    %-32s GM %12.2f J/mol   %s%s\n' % (name, gm, desc, mark))
    out.close()
    print('-> %s' % os.path.join(OUTDIR, 'gm_comparison.txt'))


if __name__ == '__main__':
    main()
