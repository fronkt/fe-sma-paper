"""Phase compositions at 1200 C for the LLM-alloy (JMEP-26-07-50730.R1, Reviewer 1 #4).

R1#4 asks where the added Si and C reside. EDS cannot see carbon and was qualitative, so
the only quantitative statement available from existing work is the calculated partitioning
between the alpha and gamma that coexist at the 1200 C solution-treatment temperature.

Uses exactly the database files, phase lists, compositions and grid densities of
step_diagrams.py (imported, not copied), at one temperature. The phase fractions printed
here must reproduce Table 3 of the manuscript; if they do not, the composition-grid issue
documented in refine_by_gm.py has struck and the partitioning must not be quoted.

    python phase_compositions_1200.py          -> results/phase_compositions_1200.txt
"""
import io
import os

import numpy as np
from pycalphad import Database, equilibrium, variables as v

import step_diagrams as sd

T_C = 1200.0
TABLE3 = {  # mol% alpha / gamma at 1200 C, manuscript Table 3
    'mpea-02b': (71.1, 28.9),
    'PrecHiMn-04': (64.5, 35.5),
    'mc_fe': (61.9, 38.1),
}


def main():
    out = io.StringIO()
    out.write('LLM-alloy (measured chemistry) at %.0f C: equilibrium phase compositions\n' % T_C)
    out.write('Same databases, phase lists, compositions and pdens as step_diagrams.py.\n')
    for cfg in sd.RUNS:
        dbf = Database(os.path.join(sd.DBDIR, cfg['file']))
        comps = cfg['elements'] + ['VA']
        phases = [p for p in cfg['phases'] if p in dbf.phases]
        conds, frac = sd.conditions_for('llm', cfg['elements'])
        conds = dict(conds)
        conds.update({v.T: T_C + 273.15, v.P: 101325, v.N: 1})
        eq = equilibrium(dbf, comps, phases, conds,
                         calc_opts={'pdens': cfg.get('pdens', sd.DEFAULT_PDENS)})
        sl = eq.squeeze()
        names = np.atleast_1d(sl.Phase.values).flatten()
        nps = np.atleast_1d(sl.NP.values).flatten()
        xs = np.atleast_2d(sl.X.values)
        comp_names = [str(c) for c in sl.component.values]

        out.write('\n=== %s (%s), pdens %d\n' % (cfg['key'], ', '.join(cfg['elements']),
                                                cfg.get('pdens', sd.DEFAULT_PDENS)))
        out.write('alloy at%%: %s\n' % ', '.join('%s %.3f' % (el, 100 * f)
                                                for el, f in frac.items()))
        out.write('%-14s %7s  %s\n' % ('phase', 'mol%', '  '.join('%7s' % c for c in comp_names)))
        for name, np_, x in zip(names, nps, xs):
            name = str(name)
            if not name or np_ != np_ or np_ < sd.FRACTION_CUTOFF:
                continue
            out.write('%-14s %7.2f  %s\n' % (name, 100 * np_,
                                              '  '.join('%7.3f' % (100 * xi) for xi in x)))
        ref = TABLE3.get(cfg['key'])
        if ref:
            out.write('Table 3 check: alpha %.1f / gamma %.1f mol%%\n' % ref)

    os.makedirs(sd.OUTDIR, exist_ok=True)
    path = os.path.join(sd.OUTDIR, 'phase_compositions_1200.txt')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(out.getvalue())
    print(out.getvalue())


if __name__ == '__main__':
    main()
