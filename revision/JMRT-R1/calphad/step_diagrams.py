"""Equilibrium step diagrams, 400-1400 C, for the JMRT revision.

Answers R1#2, R2 R&D#2 (thermodynamic support), R1#1 / R3#9 (the C-free control),
and R3#2 (is kappa-carbide predicted?).

Three alloys per database:
    benchmark      -- the Omori-type Fe-Mn-Al-Ni reference
    llm            -- the LLM-hypothesised composition as measured
    llm_noC        -- the same composition with C removed; every other element fixed.
                      This is the in-silico C-free variant R1#1 asks for.

Phase selection notes (these matter, and getting them wrong quietly doubles phases):

  * mpea-02b declares `DEFAULT-COM REJECT_PHASE FCC_A1 BCC_A2`, i.e. the active set is
    the ordering-aware pair A1_FCC/FCC_4SL and A2_BCC/B2_BCC. B2_BCC is *partitioned*
    (DIS_PART A2_BCC), so passing B2_BCC alone covers both ordered B2 and disordered A2.
    Passing A2_BCC as well would enter the same phase twice.

  * PrecHiMn-04 rejects its ordering models by default. We deliberately re-enable
    BCC_4SL (partitioned over A2_BCC) because D0_3 is the phase the manuscript claims
    to observe, and BCC_4SL is the only description of it we have.

  * mc_fe models BCC_B2 as an independent phase, not a partitioned one, so BCC_A2 and
    BCC_B2 are both passed.

A partitioned phase in a two-phase field appears as two *composition sets* under one
name. They are reported separately here -- summing them by name would hide exactly the
alpha + B2 coexistence this paper is about.
"""
import io
import itertools
import os

import numpy as np
from pycalphad import Database, Model, equilibrium, variables as v

HERE = os.path.dirname(os.path.abspath(__file__))
DBDIR = os.path.join(HERE, 'db')
OUTDIR = os.path.join(HERE, 'results')

T_MIN_C, T_MAX_C, T_STEP_C = 400, 1400, 10
NEAR_ZERO = 1e-6          # stand-in for "no carbon"; a true 0 is numerically awkward
FRACTION_CUTOFF = 1e-4    # below this a phase is not reported
ORDER_TOL = 0.05          # max site-fraction split below which BCC is called disordered

# Measured at.% (ICP-AES). Renormalised per database to whatever elements it carries.
ALLOYS = {
    'benchmark': {'FE': 42.7, 'MN': 34.1, 'AL': 15.2, 'NI': 7.8,
                  'SI': 0.02, 'C': 0.04, 'P': 0.10},
    'llm':       {'FE': 51.5, 'MN': 29.8, 'AL': 11.9, 'NI': 4.2,
                  'SI': 2.04, 'C': 0.45},
    'llm_noC':   {'FE': 51.5, 'MN': 29.8, 'AL': 11.9, 'NI': 4.2,
                  'SI': 2.04, 'C': NEAR_ZERO},
}

RUNS = [
    dict(
        key='mpea-02b',
        file='mpea-02b.tdb',
        note='Hallstedt HEA v2b. Primary run: only database with Ni and C together. No Si.',
        elements=['FE', 'MN', 'AL', 'NI', 'C'],
        phases=['LIQUID:L', 'B2_BCC', 'A1_FCC', 'KAPPA_E21', 'CEMENTITE_D011',
                'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9', 'CBCC_A12',
                'CUB_A13', 'HCP_A3', 'SIGMA_D8B', 'AL8FE5_D82', 'AL8MN5_D810',
                'AL13FE4', 'AL5FE2', 'AL2FE', 'AL3NI2_D513', 'AL3NI_D011',
                'AL3NI5', 'AL4NI3', 'AL71FE5NI24', 'AL11MN4_HT', 'AL11MN4_LT',
                'AL12MN', 'AL6MN_D2H', 'AL4MN_MU', 'AL4MN_LAMBDA'],
        bcc='B2_BCC',
        alloys=['benchmark', 'llm', 'llm_noC'],
    ),
    dict(
        key='PrecHiMn-04',
        file='PrecHiMn-04_2.pycalphad.tdb',
        note='High-Mn steels. Carries Si and D0_3 (BCC_4SL) but has no Ni, '
             'so the benchmark cannot be run here.',
        elements=['FE', 'MN', 'AL', 'SI', 'C'],
        phases=['LIQUID:L', 'BCC_4SL', 'A1_FCC', 'KAPPA_E21', 'CEMENTITE_D011',
                'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9', 'CBCC_A12',
                'CUB_A13', 'HCP_A3', 'AL8FE5_D82', 'AL8MN5_D810', 'AL13FE4',
                'AL5FE2', 'AL2FE', 'AL12MN', 'AL6MN_D2H', 'AL11MN4_HT',
                'AL11MN4_LT', 'FE2SI', 'FESI2_H', 'FESI2_L', 'M3SI',
                'M5SI3_D88', 'FE8SI2C', 'SIGMA_D8B'],
        bcc='BCC_4SL',
        alloys=['llm', 'llm_noC'],
    ),
    dict(
        key='mc_fe',
        file='mc_fe_v2.059.pycalphad.tdb',
        note='MatCalc open Fe. Only database carrying all six elements plus P. '
             'BCC_B2 is an independent phase here, and K_CARB is kappa-(Fe,Mn)3AlC.',
        elements=['FE', 'MN', 'AL', 'NI', 'SI', 'C', 'P'],
        # SIGMA, LAVES_PHASE, MU_PHASE and CHI_A12 are dropped: every one of them
        # requires Cr, Mo, W or Nb, none of which is present in either alloy, so they
        # cannot form here. Removing them shrinks the composition-set search without
        # biasing the result. Everything that *can* form is retained, including the
        # phases that never turned out to be stable at pdens=500.
        phases=['LIQUID', 'BCC_A2', 'BCC_B2', 'FCC_A1', 'K_CARB', 'CEMENTITE',
                'M23C6', 'M7C3', 'KSI_CARBIDE', 'M5C2', 'GRAPHITE', 'BETA_MN',
                'ALPHA_MN', 'HCP_A3', 'M2P', 'M3P', 'G_PHASE'],
        bcc='BCC_B2',
        alloys=['benchmark', 'llm', 'llm_noC'],
        # 7 components and a difficult gamma/alpha miscibility region. At pdens=500 the
        # global grid was too coarse: the solver failed outright at 8 temperatures and
        # returned spurious single-phase answers next to them, around 840-990 C.
        # pdens=5000 was tried and proved intractable; 2000 is the working compromise.
        pdens=2000,
    ),
]
DEFAULT_PDENS = 500


def conditions_for(alloy, elements):
    """Renormalise a measured composition onto a database's element set."""
    raw = {el: ALLOYS[alloy].get(el, 0.0) for el in elements}
    total = sum(raw.values())
    frac = {el: val / total for el, val in raw.items()}
    # Fe is the dependent component -- pycalphad takes N-1 mole fractions
    dependent = 'FE'
    return {v.X(el): max(frac[el], NEAR_ZERO)
            for el in elements if el != dependent}, frac


def dof_layout(dbf, comps, phase_name):
    """Site-fraction ordering pycalphad uses internally, per sublattice."""
    mod = Model(dbf, comps, phase_name)
    return [sorted(str(s) for s in subl) for subl in mod.constituents]


def order_parameter(site_fractions, layout):
    """Max site-fraction split between the two substitutional sublattices of a
    partitioned BCC. ~0 means disordered A2; large means B2/D0_3 ordering."""
    if len(layout) < 2:
        return None
    sizes = [len(s) for s in layout]
    offs = list(itertools.accumulate([0] + sizes))
    subs = [dict(zip(layout[i], site_fractions[offs[i]:offs[i + 1]]))
            for i in range(len(layout) - 1)]   # drop the interstitial sublattice
    if len(subs) < 2:
        return None
    species = set().union(*[set(s) for s in subs])
    return max(max(abs(a.get(sp, 0.0) - b.get(sp, 0.0))
                   for a, b in itertools.combinations(subs, 2))
               for sp in species)


def run(cfg, report):
    path = os.path.join(DBDIR, cfg['file'])
    dbf = Database(path)
    comps = cfg['elements'] + ['VA']
    phases = [p for p in cfg['phases'] if p in dbf.phases]
    missing = [p for p in cfg['phases'] if p not in dbf.phases]

    report.write(u'\n' + u'=' * 78 + u'\n')
    report.write(u'%s  (%s)\n%s\n' % (cfg['key'], cfg['file'], cfg['note']))
    report.write(u'elements: %s\n' % ' '.join(cfg['elements']))
    report.write(u'phases  : %s\n' % ' '.join(phases))
    if missing:
        report.write(u'absent  : %s\n' % ' '.join(missing))

    layout = dof_layout(dbf, comps, cfg['bcc']) if cfg['bcc'] in dbf.phases else None
    temps = np.arange(T_MIN_C, T_MAX_C + 1, T_STEP_C) + 273.15
    rows = []

    for alloy in cfg['alloys']:
        conds, frac = conditions_for(alloy, cfg['elements'])
        report.write(u'\n--- %s / %s ---\n' % (cfg['key'], alloy))
        report.write(u'    at.%%: %s\n' % ', '.join(
            '%s %.3f' % (el, 100 * f) for el, f in sorted(frac.items())))

        conds = dict(conds)
        conds.update({v.T: temps, v.P: 101325, v.N: 1})
        eq = equilibrium(dbf, comps, phases, conds,
                         calc_opts={'pdens': cfg.get('pdens', DEFAULT_PDENS)})

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
                if name == cfg['bcc'] and layout is not None:
                    op = order_parameter(ys[vi], layout)
                    if op is not None:
                        label = '%s[%s]' % (
                            name, 'ordered' if op > ORDER_TOL else 'A2')
                seen[label] = seen.get(label, 0.0) + float(np_)
                rows.append(dict(database=cfg['key'], alloy=alloy,
                                 T_C=round(float(temp) - 273.15, 1),
                                 phase=name, label=label, set_index=vi,
                                 fraction=float(np_)))
            if not seen:
                # equilibrium did not converge here -- record it so the plot can
                # break the line instead of silently interpolating across the gap
                rows.append(dict(database=cfg['key'], alloy=alloy,
                                 T_C=round(float(temp) - 273.15, 1),
                                 phase='__NONCONVERGED__', label='__NONCONVERGED__',
                                 set_index=-1, fraction=float('nan')))
            desc = ', '.join('%s %.1f%%' % (k, 100 * val)
                             for k, val in sorted(seen.items(), key=lambda kv: -kv[1]))
            if int(round(float(temp) - 273.15)) % 100 == 0:
                report.write(u'  %5.0f C : %s\n'
                             % (float(temp) - 273.15, desc or '*** NOT CONVERGED ***'))

        bad = [r['T_C'] for r in rows
               if r['alloy'] == alloy and r['phase'] == '__NONCONVERGED__']
        if bad:
            report.write(u'  !! did not converge at %d of %d temperatures: %s\n'
                         % (len(bad), len(temps),
                            ', '.join('%g' % b for b in bad)))
    return rows


def main():
    """Run every database, or just the ones named on the command line.

    Naming a subset re-runs only those and merges the result into the existing CSV,
    so a single misbehaving database can be re-done without repeating the rest:

        python step_diagrams.py mc_fe
    """
    import csv
    import sys

    os.makedirs(OUTDIR, exist_ok=True)
    wanted = [a for a in sys.argv[1:] if not a.startswith('-')]
    runs = [c for c in RUNS if c['key'] in wanted] if wanted else RUNS
    if wanted and not runs:
        raise SystemExit('no database matches %s (have: %s)'
                         % (wanted, ', '.join(c['key'] for c in RUNS)))

    csv_path = os.path.join(OUTDIR, 'step_diagrams.csv')
    fields = ['database', 'alloy', 'T_C', 'phase', 'label', 'set_index', 'fraction']

    kept = []
    if wanted and os.path.exists(csv_path):
        with open(csv_path, newline='', encoding='utf-8') as fh:
            kept = [r for r in csv.DictReader(fh) if r['database'] not in wanted]

    mode = 'a' if wanted and os.path.exists(os.path.join(OUTDIR, 'step_diagrams.txt')) else 'w'
    report = io.open(os.path.join(OUTDIR, 'step_diagrams.txt'), mode, encoding='utf-8')
    report.write(u'\nEquilibrium step diagrams, %d-%d C in %d C steps%s\n'
                 % (T_MIN_C, T_MAX_C, T_STEP_C,
                    '  [re-run of %s]' % ', '.join(wanted) if wanted else ''))

    all_rows = []
    for cfg in runs:
        try:
            all_rows.extend(run(cfg, report))
        except Exception as exc:
            report.write(u'\n!!! %s FAILED: %s: %s\n'
                         % (cfg['key'], type(exc).__name__, exc))
            print('FAILED %s: %s' % (cfg['key'], exc))

    with open(csv_path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(kept)
        w.writerows(all_rows)

    report.close()
    print('wrote %d new rows (+%d kept) -> %s' % (len(all_rows), len(kept), csv_path))


if __name__ == '__main__':
    main()
