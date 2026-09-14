"""Grid-arbitrated re-computation of the high-temperature LLM-alloy rows.

compare_gm.py (2026-09-14) showed that pycalphad's converged state depends on the
point-grid density in the 1200-1400 C range of this alloy, and that the denser grid is
NOT always the lower energy: at 1290 C in mpea-02b, pdens 500 and 1000 return
alpha + gamma at GM = -109378 J/mol while pdens 2000 and 3000 return 100 % gamma at
-109144 J/mol. The global minimiser is supposed to return the lowest-energy state; when
different grids return different states, the lowest GM among them is the equilibrium the
database describes, and that is what this script keeps.

For each temperature in a band it runs equilibrium() at every density in LADDER, keeps
the converged state with the lowest GM, and writes the rows in step_diagrams.csv format
together with a log of every candidate's GM so the choice is auditable. With --splice
the chosen rows replace those temperatures in results/step_diagrams.csv, and every
replaced constitution is printed beside its replacement.

    python refine_by_gm.py            # -> results/gm_refined.csv, results/gm_refined_log.txt
    python refine_by_gm.py --splice   # also merge into results/step_diagrams.csv
    python refine_by_gm.py --splice --only PrecHiMn-04:llm,mpea-02b:llm \
                           --ladder 300,400,450,500,550,600,700,800,1000,1200,1500,2000,3000
        # second pass on named bands with a wider ladder; outputs carry the suffix "-only"

Why a wider ladder: recheck_prechimn_dense.py showed that a 12 000-point two-phase grid
still misses the PrecHiMn-04 duplex at 1200 C that pdens 500 finds (GM -100985.8 against
-100898.6 J/mol for the gamma-only state it converges to). Grid density alone is not the
cure -- the local refinement falls into the gamma basin from most starting grids -- so
the ladder samples many grid placements and keeps the lowest energy found.
"""
import csv
import io
import os
import sys

import numpy as np
from pycalphad import Database, equilibrium, variables as v

from step_diagrams import (DBDIR, OUTDIR, RUNS, FRACTION_CUTOFF, ORDER_TOL,
                           conditions_for, dof_layout, order_parameter)

LADDER = [500, 1000, 2000, 3000]
BANDS = {                                  # (database, alloy) -> (T_lo, T_hi) in C
    ('mpea-02b', 'llm'): (1250, 1400),
    ('mpea-02b', 'benchmark'): (1300, 1400),
    ('mpea-02b', 'llm_noC'): (1350, 1400),
    ('PrecHiMn-04', 'llm'): (1150, 1400),
    ('PrecHiMn-04', 'llm_noC'): (1280, 1400),
}
FIELDS = ['database', 'alloy', 'T_C', 'phase', 'label', 'set_index', 'fraction']
NONCONV = '__NONCONVERGED__'
PART = os.path.join(OUTDIR, 'gm_refined.csv')
LOG = os.path.join(OUTDIR, 'gm_refined_log.txt')
MAIN = os.path.join(OUTDIR, 'step_diagrams.csv')


def state_at(eq, ti, cfg, layout):
    """(GM, [row dicts without database/alloy/T_C]) for one temperature index."""
    sl = eq.isel(T=ti).squeeze()
    names = np.atleast_1d(sl.Phase.values).flatten()
    fracs = np.atleast_1d(sl.NP.values).flatten()
    ys = np.atleast_2d(sl.Y.values)
    gm = float(np.atleast_1d(sl.GM.values).flatten()[0])
    rows = []
    for vi, (name, np_) in enumerate(zip(names, fracs)):
        name = str(name)
        if not name or np_ != np_ or np_ < FRACTION_CUTOFF:
            continue
        label = name
        if name == cfg['bcc'] and layout is not None:
            op = order_parameter(ys[vi], layout)
            if op is not None:
                label = '%s[%s]' % (name, 'ordered' if op > ORDER_TOL else 'A2')
        rows.append(dict(phase=name, label=label, set_index=vi, fraction=float(np_)))
    if not rows:
        gm = float('nan')
    return gm, rows


def describe(rows):
    seen = {}
    for r in rows:
        seen[r['label']] = seen.get(r['label'], 0.0) + float(r['fraction'])
    return ', '.join('%s %.1f%%' % (k, 100 * f)
                     for k, f in sorted(seen.items(), key=lambda kv: -kv[1])) or NONCONV


def compute(log, ladder, only):
    out = []
    for cfg in RUNS:
        dbf = None
        for alloy in cfg['alloys']:
            band = BANDS.get((cfg['key'], alloy))
            if band is None or (only and (cfg['key'], alloy) not in only):
                continue
            if dbf is None:
                dbf = Database(os.path.join(DBDIR, cfg['file']))
                comps = cfg['elements'] + ['VA']
                phases = [p for p in cfg['phases'] if p in dbf.phases]
                if 'LIQUID' not in phases:
                    raise RuntimeError('%s: LIQUID missing' % cfg['key'])
                layout = dof_layout(dbf, comps, cfg['bcc'])
            lo, hi = band
            temps = np.arange(lo, hi + 1, 10) + 273.15
            conds, frac = conditions_for(alloy, cfg['elements'])
            conds = dict(conds)
            conds.update({v.T: temps, v.P: 101325, v.N: 1})

            candidates = {}                       # pdens -> eq
            for pd in ladder:
                candidates[pd] = equilibrium(dbf, comps, phases, conds,
                                             calc_opts={'pdens': pd})
                print('  %s %s pdens %d done' % (cfg['key'], alloy, pd), flush=True)
            log.write(u'\n=== %s / %s, %d-%d C, ladder %s ===\n'
                      % (cfg['key'], alloy, lo, hi, ladder))
            for ti, temp in enumerate(temps):
                tc = round(float(temp) - 273.15, 1)
                states = []
                for pd in ladder:
                    gm, rows = state_at(candidates[pd], ti, cfg, layout)
                    states.append((gm, pd, rows))
                finite = [s for s in states if s[0] == s[0]]
                if finite:
                    gm, pd, rows = min(finite, key=lambda s: s[0])
                    for r in rows:
                        out.append(dict(database=cfg['key'], alloy=alloy, T_C=tc, **r))
                    chosen = 'pdens %d' % pd
                else:
                    out.append(dict(database=cfg['key'], alloy=alloy, T_C=tc, phase=NONCONV,
                                    label=NONCONV, set_index=-1, fraction=float('nan')))
                    chosen = 'none converged'
                distinct = len({describe(s[2]) for s in finite})
                log.write(u'  %5.0f C  keep %-11s %s\n' % (tc, chosen, describe(rows) if finite else NONCONV))
                if distinct > 1:
                    for gm, pd, rows in states:
                        log.write(u'           pdens %-5d GM %12.2f  %s\n' % (pd, gm, describe(rows)))
                print('  %s %s %5.0f C  %s' % (cfg['key'], alloy, tc, chosen), flush=True)
    return out


def splice(refined, log, main_path=None):
    main_path = main_path or MAIN
    with open(main_path, newline='', encoding='utf-8') as fh:
        main = list(csv.DictReader(fh))
    keys = {(r['database'], r['alloy'], float(r['T_C'])) for r in refined}

    def summary(rows):
        seen = {}
        for r in rows:
            seen[r['label']] = seen.get(r['label'], 0.0) + float(r['fraction'])
        return ', '.join('%s %.1f%%' % (k, 100 * f)
                         for k, f in sorted(seen.items(), key=lambda kv: -kv[1]))

    log.write(u'\n=== splice into step_diagrams.csv: rows whose constitution changed ===\n')
    changed = 0
    for key in sorted(keys):
        old = [r for r in main if (r['database'], r['alloy'], float(r['T_C'])) == key]
        new = [r for r in refined if (r['database'], r['alloy'], float(r['T_C'])) == key]
        so, sn = summary(old), summary(new)
        if so != sn:
            changed += 1
            log.write(u'  %s / %s %5.0f C : %s  ->  %s\n' % (key[0], key[1], key[2], so, sn))
    kept = [r for r in main if (r['database'], r['alloy'], float(r['T_C'])) not in keys]
    with open(main_path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(kept)
        w.writerows(refined)
    log.write(u'  %d of %d temperatures changed; %d rows kept, %d rows written\n'
              % (changed, len(keys), len(kept), len(refined)))
    print('spliced: %d of %d temperatures changed' % (changed, len(keys)))


def main():
    args = sys.argv[1:]
    do_splice = '--splice' in args
    ladder = list(LADDER)
    only = None
    if '--ladder' in args:
        ladder = [int(x) for x in args[args.index('--ladder') + 1].split(',')]
    if '--only' in args:
        only = {tuple(x.split(':')) for x in args[args.index('--only') + 1].split(',')}
    suffix = '-only' if only else ''
    part = PART.replace('.csv', suffix + '.csv')
    logp = LOG.replace('.txt', suffix + '.txt')

    log = io.open(logp, 'w', encoding='utf-8')
    log.write(u'Grid-arbitrated rows: lowest GM across pdens %s%s\n'
              % (ladder, ('  [bands: %s]' % sorted(only)) if only else ''))
    refined = compute(log, ladder, only)
    with open(part, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(refined)
    print('wrote %d rows -> %s' % (len(refined), part))
    if do_splice:
        splice(refined, log)
    log.close()
    print('log -> %s' % logp)


if __name__ == '__main__':
    main()
