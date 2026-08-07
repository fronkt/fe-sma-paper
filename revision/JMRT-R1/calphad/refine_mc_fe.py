"""Surgically re-run the mc_fe / LLM-alloy region that failed to converge.

Two whole-database re-runs at pdens 5000 and 2000 were killed before finishing, so this
does the minimum that actually matters: one alloy, one temperature band, a denser global
grid, and **results flushed to disk after every chunk** so a kill costs at most one chunk
instead of the whole run. Re-running it resumes from whatever is already on disk.

    python refine_mc_fe.py            # default band
    python refine_mc_fe.py 700 1300   # explicit band

Then `python splice_refined.py` merges the result into step_diagrams.csv.
"""
import csv
import io
import os
import sys
import time

import numpy as np
from pycalphad import Database, equilibrium, variables as v

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'results')
PART = os.path.join(OUTDIR, 'mc_fe_llm_refined.csv')

PDENS = 2000
CHUNK = 4                       # temperatures per equilibrium() call
FRACTION_CUTOFF = 1e-4
FIELDS = ['database', 'alloy', 'T_C', 'phase', 'label', 'set_index', 'fraction']

# same trimmed list as step_diagrams.py -- sigma/Laves/mu/chi all need Cr, Mo, W or Nb
PHASES = ['LIQUID', 'BCC_A2', 'BCC_B2', 'FCC_A1', 'K_CARB', 'CEMENTITE', 'M23C6',
          'M7C3', 'KSI_CARBIDE', 'M5C2', 'GRAPHITE', 'BETA_MN', 'ALPHA_MN',
          'HCP_A3', 'M2P', 'M3P', 'G_PHASE']
ELEMENTS = ['FE', 'MN', 'AL', 'NI', 'SI', 'C', 'P']
RAW = {'FE': 51.5, 'MN': 29.8, 'AL': 11.9, 'NI': 4.2, 'SI': 2.04, 'C': 0.45, 'P': 0.0}


def conditions():
    total = sum(RAW[e] for e in ELEMENTS)
    return {v.X(e): max(RAW[e] / total, 1e-6) for e in ELEMENTS if e != 'FE'}


def done_temperatures():
    if not os.path.exists(PART):
        return set()
    with open(PART, newline='', encoding='utf-8') as fh:
        return {float(r['T_C']) for r in csv.DictReader(fh)}


def main():
    lo = float(sys.argv[1]) if len(sys.argv) > 2 else 780.0
    hi = float(sys.argv[2]) if len(sys.argv) > 2 else 1280.0
    os.makedirs(OUTDIR, exist_ok=True)

    want = np.arange(lo, hi + 1, 10.0)
    have = done_temperatures()
    todo = [t for t in want if t not in have]
    print('%d temperatures, %d already done, %d to do' % (len(want), len(have), len(todo)))
    if not todo:
        print('nothing to do')
        return

    dbf = Database(os.path.join(HERE, 'db', 'mc_fe_v2.059.pycalphad.tdb'))
    phases = [p for p in PHASES if p in dbf.phases]
    comps = ELEMENTS + ['VA']
    base = conditions()

    new = not os.path.exists(PART)
    fh = open(PART, 'a', newline='', encoding='utf-8')
    writer = csv.DictWriter(fh, fieldnames=FIELDS)
    if new:
        writer.writeheader()

    for start in range(0, len(todo), CHUNK):
        block = todo[start:start + CHUNK]
        t0 = time.time()
        conds = dict(base)
        conds.update({v.T: [b + 273.15 for b in block], v.P: 101325, v.N: 1})
        try:
            eq = equilibrium(dbf, comps, phases, conds, calc_opts={'pdens': PDENS})
        except Exception as exc:
            print('  %s : FAILED %s' % (block, exc))
            continue

        for i, temp_c in enumerate(block):
            sl = eq.isel(T=i).squeeze()
            names = np.atleast_1d(sl.Phase.values).flatten()
            fracs = np.atleast_1d(sl.NP.values).flatten()
            rows, seen = [], {}
            for vi, (name, npf) in enumerate(zip(names, fracs)):
                name = str(name)
                if not name or npf != npf or npf < FRACTION_CUTOFF:
                    continue
                seen[name] = seen.get(name, 0.0) + float(npf)
                rows.append(dict(database='mc_fe', alloy='llm', T_C=temp_c,
                                 phase=name, label=name, set_index=vi,
                                 fraction=float(npf)))
            if not rows:
                rows = [dict(database='mc_fe', alloy='llm', T_C=temp_c,
                             phase='__NONCONVERGED__', label='__NONCONVERGED__',
                             set_index=-1, fraction=float('nan'))]
            writer.writerows(rows)
            print('  %6.0f C : %s' % (temp_c, ', '.join(
                '%s %.1f%%' % (k, 100 * val)
                for k, val in sorted(seen.items(), key=lambda kv: -kv[1]))
                or '*** NOT CONVERGED ***'))
        fh.flush()
        os.fsync(fh.fileno())
        print('  [chunk of %d in %.0f s, flushed]' % (len(block), time.time() - t0))

    fh.close()
    print('done -> %s' % PART)


if __name__ == '__main__':
    main()
