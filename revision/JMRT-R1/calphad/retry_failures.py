"""Retry any mc_fe / LLM temperature that failed to converge, at alternative grid
densities, and record which density succeeded.

Convergence of the global-minimisation step is grid-dependent: a density that works at
one temperature can fail at its neighbour. Retrying a failed point at a different density
is a numerical fix, not a choice of answer -- the accepted result is whichever density
converges, and the density used is written into the output so the substitution stays
auditable. If several densities converge they are compared, and a disagreement is
reported rather than silently resolved.
"""
import csv
import os

import numpy as np
from pycalphad import Database, equilibrium, variables as v

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'results')
PART = os.path.join(OUTDIR, 'mc_fe_llm_refined.csv')
LOG = os.path.join(OUTDIR, 'retry_log.txt')

LADDER = [1000, 3000, 700, 4000]
FRACTION_CUTOFF = 1e-4
FIELDS = ['database', 'alloy', 'T_C', 'phase', 'label', 'set_index', 'fraction']

PHASES = ['LIQUID', 'BCC_A2', 'BCC_B2', 'FCC_A1', 'K_CARB', 'CEMENTITE', 'M23C6',
          'M7C3', 'KSI_CARBIDE', 'M5C2', 'GRAPHITE', 'BETA_MN', 'ALPHA_MN',
          'HCP_A3', 'M2P', 'M3P', 'G_PHASE']
ELEMENTS = ['FE', 'MN', 'AL', 'NI', 'SI', 'C', 'P']
RAW = {'FE': 51.5, 'MN': 29.8, 'AL': 11.9, 'NI': 4.2, 'SI': 2.04, 'C': 0.45, 'P': 0.0}


def solve(dbf, phases, comps, temp_c, pdens):
    total = sum(RAW[e] for e in ELEMENTS)
    conds = {v.X(e): max(RAW[e] / total, 1e-6) for e in ELEMENTS if e != 'FE'}
    conds.update({v.T: temp_c + 273.15, v.P: 101325, v.N: 1})
    eq = equilibrium(dbf, comps, phases, conds, calc_opts={'pdens': pdens})
    sl = eq.squeeze()
    out = {}
    for name, npf in zip(np.atleast_1d(sl.Phase.values).flatten(),
                         np.atleast_1d(sl.NP.values).flatten()):
        name = str(name)
        if name and npf == npf and npf >= FRACTION_CUTOFF:
            out[name] = out.get(name, 0.0) + float(npf)
    return out


def main():
    rows = list(csv.DictReader(open(PART, newline='', encoding='utf-8')))
    failed = sorted({float(r['T_C']) for r in rows
                     if r['phase'] == '__NONCONVERGED__'})
    if not failed:
        print('no failures to retry')
        return
    print('retrying %d failed temperatures: %s'
          % (len(failed), ', '.join('%g' % f for f in failed)))

    dbf = Database(os.path.join(HERE, 'db', 'mc_fe_v2.059.pycalphad.tdb'))
    phases = [p for p in PHASES if p in dbf.phases]
    comps = ELEMENTS + ['VA']

    log = open(LOG, 'a', encoding='utf-8')
    fixed = {}
    for temp_c in failed:
        results = {}
        for pdens in LADDER:
            try:
                got = solve(dbf, phases, comps, temp_c, pdens)
            except Exception as exc:
                log.write('%.0f C  pdens %d : ERROR %s\n' % (temp_c, pdens, exc))
                continue
            log.write('%.0f C  pdens %-5d : %s\n'
                      % (temp_c, pdens,
                         ', '.join('%s %.2f%%' % (k, 100 * val)
                                   for k, val in sorted(got.items(),
                                                        key=lambda kv: -kv[1]))
                         or 'no convergence'))
            if got:
                results[pdens] = got
        if not results:
            print('  %6.0f C : still fails at every density' % temp_c)
            continue
        # do the converged densities agree?
        keys = [frozenset(r) for r in results.values()]
        agree = all(k == keys[0] for k in keys)
        chosen = sorted(results)[0]
        fixed[temp_c] = (chosen, results[chosen])
        print('  %6.0f C : converged at pdens %d -> %s  [%d/%d densities, %s]'
              % (temp_c, chosen,
                 ', '.join('%s %.1f%%' % (k, 100 * val)
                           for k, val in sorted(results[chosen].items(),
                                                key=lambda kv: -kv[1])),
                 len(results), len(LADDER),
                 'phase sets agree' if agree else 'PHASE SETS DISAGREE'))
        if not agree:
            print('       !! %s' % {p: sorted(r) for p, r in results.items()})
    log.close()

    if not fixed:
        return
    keep = [r for r in rows if float(r['T_C']) not in fixed]
    for temp_c, (pdens, phase_frac) in fixed.items():
        for i, (name, frac) in enumerate(sorted(phase_frac.items())):
            keep.append(dict(database='mc_fe', alloy='llm', T_C=temp_c,
                             phase=name, label=name, set_index=i, fraction=frac))
    keep.sort(key=lambda r: (float(r['T_C']), int(r['set_index'])))
    with open(PART, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(keep)
    print('updated %s  (density used per point logged in %s)'
          % (os.path.basename(PART), os.path.basename(LOG)))


if __name__ == '__main__':
    main()
