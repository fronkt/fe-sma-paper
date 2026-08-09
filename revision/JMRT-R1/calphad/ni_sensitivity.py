"""Ni sensitivity scan, 4.2 -> 7.8 at.%, for R3#9.

Reviewer 3 comment #9: "the reduction in Ni from 7.5 to 4 at.% may matter as much as
the carbon addition." The C = 0 control in step_diagrams.py already holds Ni fixed at
its measured 4.2 at.%, so it shows what carbon does at low Ni but says nothing about
what Ni does on its own. This closes that gap directly.

Two series, each stepping Ni from the LLM-alloy's measured 4.2 at.% up to the
benchmark's measured 7.8 at.%, with iron taking up the difference so that Mn, Al, Si
and C stay exactly where they were measured:

    C_measured : C held at the measured 0.45 at.%  -- the question R3#9 actually asks,
                 i.e. would restoring the benchmark's nickel have rescued this alloy?
    C_free     : C removed                         -- isolates nickel's own effect,
                 and gives the second axis of the 2x2 against the existing control.

What the manuscript needs out of this is one number per composition: the temperature
at which the single-phase bcc field opens (the alpha solvus). The 1200 C solution
treatment either lies inside that field or it does not, and that is the whole argument
of Sec. 4.1. Phase fractions at 1200 C are reported alongside it.

The low-temperature sweep is coarser and answers a second question: does more nickel
open a usable solution-and-age window (single-phase alpha to quench from, ordered bcc
to age into) that the LLM-alloy lacks?

Primary database is mpea-02b, the only one of the three carrying Ni and C together.
mc_fe is run at the two endpoints only as a cross-check; it carries all six elements
but needs pdens=2000 and is an order of magnitude slower.
"""
import csv
import io
import os
import sys

import numpy as np
from pycalphad import Database, equilibrium, variables as v

from step_diagrams import (DBDIR, OUTDIR, FRACTION_CUTOFF, NEAR_ZERO, ORDER_TOL,
                           dof_layout, order_parameter)

NI_MIN, NI_MAX, NI_STEP = 4.2, 7.8, 0.4          # at.%; 4.2 = measured, 7.8 = benchmark

# The alpha solvus for the measured composition sits near 1340 C, so the fine window
# has to reach well past it. 10 C matches the spacing used for the published figure.
T_HI = np.arange(1000, 1401, 10) + 273.15
T_LO = np.arange(400, 951, 25) + 273.15          # ordering / ageing window, coarser

BASE = {'FE': 51.5, 'MN': 29.8, 'AL': 11.9, 'NI': 4.2, 'SI': 2.04, 'C': 0.45}

RUNS = [
    dict(key='mpea-02b', file='mpea-02b.tdb',
         elements=['FE', 'MN', 'AL', 'NI', 'C'],
         phases=['LIQUID:L', 'B2_BCC', 'A1_FCC', 'KAPPA_E21', 'CEMENTITE_D011',
                 'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9', 'CBCC_A12',
                 'CUB_A13', 'HCP_A3', 'SIGMA_D8B', 'AL8FE5_D82', 'AL8MN5_D810',
                 'AL13FE4', 'AL5FE2', 'AL2FE', 'AL3NI2_D513', 'AL3NI_D011',
                 'AL3NI5', 'AL4NI3', 'AL71FE5NI24', 'AL11MN4_HT', 'AL11MN4_LT',
                 'AL12MN', 'AL6MN_D2H', 'AL4MN_MU', 'AL4MN_LAMBDA'],
         bcc='B2_BCC', fcc='A1_FCC', pdens=500, endpoints_only=False),
    dict(key='mc_fe', file='mc_fe_v2.059.pycalphad.tdb',
         elements=['FE', 'MN', 'AL', 'NI', 'SI', 'C'],
         phases=['LIQUID', 'BCC_A2', 'BCC_B2', 'FCC_A1', 'K_CARB', 'CEMENTITE',
                 'M23C6', 'M7C3', 'KSI_CARBIDE', 'M5C2', 'GRAPHITE', 'BETA_MN',
                 'ALPHA_MN', 'HCP_A3', 'G_PHASE'],
         bcc='BCC_B2', fcc='FCC_A1', pdens=2000, endpoints_only=True),
]


def composition(ni_at, carbon_free):
    """Measured composition with Ni set to ni_at, iron balancing, C optionally removed."""
    comp = dict(BASE)
    comp['FE'] = BASE['FE'] - (ni_at - BASE['NI'])
    comp['NI'] = ni_at
    if carbon_free:
        comp['C'] = NEAR_ZERO
    return comp


def conditions(comp, elements):
    raw = {el: comp.get(el, 0.0) for el in elements}
    total = sum(raw.values())
    frac = {el: val / total for el, val in raw.items()}
    return ({v.X(el): max(frac[el], NEAR_ZERO) for el in elements if el != 'FE'},
            frac)


def phases_at(eq, ti, cfg, layout):
    """Phase fractions at one temperature index, ordered-bcc split out by name."""
    sl = eq.isel(T=ti).squeeze()
    names = np.atleast_1d(sl.Phase.values).flatten()
    fracs = np.atleast_1d(sl.NP.values).flatten()
    ys = np.atleast_2d(sl.Y.values)
    out = {}
    for vi, (name, np_) in enumerate(zip(names, fracs)):
        name = str(name)
        if not name or np_ != np_ or np_ < FRACTION_CUTOFF:
            continue
        label = name
        if name == cfg['bcc'] and layout is not None:
            op = order_parameter(ys[vi], layout)
            if op is not None:
                label = '%s[%s]' % (name, 'ordered' if op > ORDER_TOL else 'A2')
        out[label] = out.get(label, 0.0) + float(np_)
    return out


def solvus(temps_c, per_T, cfg):
    """Lowest temperature above which bcc is the only solid phase.

    Returns (T_solvus, excursions). T_solvus is None if no single-phase bcc field
    exists anywhere in the scanned window, which would be the interesting answer.

    An earlier version invalidated the solvus on *any* later non-single-phase point,
    which let one bad temperature move the reported value by 60 C: at Ni = 5.4 at.%
    in the C-free series, 1210 C returns 100% FCC sandwiched between 100% BCC at both
    1200 and 1220 C. An isolated single-point flip with no two-phase transition on
    either side is a solver artifact, not a re-entrant gamma field. So the first
    crossing is reported and any later excursions are returned alongside it rather
    than being allowed to silently shift the number or be silently dropped.
    """
    single, excursions = None, []
    for tc, seen in zip(temps_c, per_T):
        solid = {k: f for k, f in seen.items() if not k.startswith('LIQUID')}
        if not solid or sum(solid.values()) <= 0:
            excursions.append((tc, 'not converged'))
            continue
        # Share of the SOLID, not of unity: fractions include liquid, so past the solidus
        # bcc drops below the threshold while still being the only solid phase. Normalising
        # against unity reads sixteen consecutive melting steps in mc_fe as gamma re-entry.
        # Also match every bcc description -- mc_fe models BCC_A2 and BCC_B2 as separate
        # phases, so testing cfg['bcc'] alone misses the disordered one entirely.
        bcc = (sum(f for k, f in solid.items()
                   if k.startswith(('B2_BCC', 'BCC_A2', 'BCC_B2', 'BCC_4SL')))
               / sum(solid.values()))
        if bcc > 0.999:
            if single is None:
                single = tc
        elif single is not None:
            excursions.append((tc, ', '.join('%s %.3f' % kv for kv in
                                             sorted(solid.items(), key=lambda x: -x[1]))))
    return single, excursions


def run(cfg, report, rows):
    dbf = Database(os.path.join(DBDIR, cfg['file']))
    comps = cfg['elements'] + ['VA']
    phases = [p for p in cfg['phases'] if p in dbf.phases]
    layout = dof_layout(dbf, comps, cfg['bcc']) if cfg['bcc'] in dbf.phases else None

    ni_values = ([NI_MIN, NI_MAX] if cfg['endpoints_only']
                 else list(np.round(np.arange(NI_MIN, NI_MAX + 1e-9, NI_STEP), 2)))

    report.write(u'\n' + u'=' * 78 + u'\n%s   elements: %s\n'
                 % (cfg['key'], ' '.join(cfg['elements'])))
    report.write(u'Ni values (at.%%): %s\n'
                 % ', '.join('%.1f' % n for n in ni_values))

    for carbon_free in (False, True):
        series = 'C_free' if carbon_free else 'C_measured'
        report.write(u'\n--- %s / %s ---\n' % (cfg['key'], series))
        report.write(u'%6s  %10s  %s\n' % ('Ni at%', 'a-solvus', 'phases at 1200 C'))

        for ni in ni_values:
            comp = composition(ni, carbon_free)
            conds, frac = conditions(comp, cfg['elements'])

            hi = dict(conds); hi.update({v.T: T_HI, v.P: 101325, v.N: 1})
            eq = equilibrium(dbf, comps, phases, hi,
                             calc_opts={'pdens': cfg['pdens']})
            temps_c = [round(float(t) - 273.15, 1) for t in T_HI]
            per_T = [phases_at(eq, i, cfg, layout) for i in range(len(T_HI))]

            sol, excursions = solvus(temps_c, per_T, cfg)
            at1200 = per_T[temps_c.index(1200.0)]
            desc = ', '.join('%s %.1f%%' % (k, 100 * f)
                             for k, f in sorted(at1200.items(), key=lambda kv: -kv[1]))
            report.write(u'%6.1f  %10s  %s\n'
                         % (ni, ('%.0f C' % sol) if sol else 'none <=1400',
                            desc or '*** NOT CONVERGED ***'))
            for tc, what in excursions:
                report.write(u'        !! %g C above the solvus is not single-phase bcc: %s\n'
                             % (tc, what))

            for tc, seen in zip(temps_c, per_T):
                for label, f in seen.items():
                    rows.append(dict(database=cfg['key'], series=series, ni_at=ni,
                                     T_C=tc, label=label, fraction=f,
                                     alpha_solvus_C=sol if sol else ''))

            # Ageing window: is there ever ordered bcc without gamma swamping it?
            lo = dict(conds); lo.update({v.T: T_LO, v.P: 101325, v.N: 1})
            eq_lo = equilibrium(dbf, comps, phases, lo,
                                calc_opts={'pdens': cfg['pdens']})
            for i, t in enumerate(T_LO):
                tc = round(float(t) - 273.15, 1)
                for label, f in phases_at(eq_lo, i, cfg, layout).items():
                    rows.append(dict(database=cfg['key'], series=series, ni_at=ni,
                                     T_C=tc, label=label, fraction=f,
                                     alpha_solvus_C=sol if sol else ''))
            print('  %s %s Ni=%.1f  solvus=%s' % (cfg['key'], series, ni, sol))


def main():
    """Run every database, or just the ones named on the command line.

    Naming a subset merges into the existing CSV instead of replacing it, matching
    step_diagrams.py. Without this a `python ni_sensitivity.py mc_fe` silently discards
    the mpea-02b scan, which takes about twenty minutes to produce.
    """
    os.makedirs(OUTDIR, exist_ok=True)
    wanted = [a for a in sys.argv[1:] if not a.startswith('-')]
    runs = [c for c in RUNS if c['key'] in wanted] if wanted else RUNS
    if wanted and not runs:
        raise SystemExit('no database matches %s (have: %s)'
                         % (wanted, ', '.join(c['key'] for c in RUNS)))

    path = os.path.join(OUTDIR, 'ni_sensitivity.csv')
    txt = os.path.join(OUTDIR, 'ni_sensitivity.txt')
    fields = ['database', 'series', 'ni_at', 'T_C', 'label', 'fraction', 'alpha_solvus_C']

    kept = []
    if wanted and os.path.exists(path):
        with open(path, newline='', encoding='utf-8') as fh:
            kept = [r for r in csv.DictReader(fh) if r['database'] not in wanted]

    mode = 'a' if wanted and os.path.exists(txt) else 'w'
    report = io.open(txt, mode, encoding='utf-8')
    report.write(u'\nNi sensitivity, %.1f-%.1f at.%% in %.1f steps, iron balancing.%s\n'
                 % (NI_MIN, NI_MAX, NI_STEP,
                    '  [re-run of %s]' % ', '.join(wanted) if wanted else ''))
    report.write(u'Mn, Al, Si and C held at measured values; C removed in the C_free series.\n')

    rows = []
    for cfg in runs:
        try:
            run(cfg, report, rows)
        except Exception as exc:
            report.write(u'\n!!! %s FAILED: %s: %s\n' % (cfg['key'], type(exc).__name__, exc))
            print('FAILED %s: %s' % (cfg['key'], exc))

    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(kept)
        w.writerows(rows)
    report.close()
    print('wrote %d new rows (+%d kept) -> %s' % (len(rows), len(kept), path))


if __name__ == '__main__':
    main()
