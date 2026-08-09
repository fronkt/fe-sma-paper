"""Was the alloy that was made inside the range the agent actually proposed? For R1#2.

The recovered Gemini Deep Research report (2025-06-04, see ../llm-provenance/) proposes six
alloy families. The one that was synthesised is Hypothesis A2, "Fe-Mn-Al-Si-Ni-(B/C)", whose
proposed nominal range is, in wt.%:

    Fe (bal.), Mn 20-30, Al 8-12, Si 1-4, Ni 3-6, and either B 0.005-0.05 or C 0.1-0.3

The alloy melted was, nominally, Fe-32.3Mn-6.4Al-4.6Ni-2.2Si-0.1C (wt.%). Si, Ni and C are
inside the window. **Mn is above it and Al is well below it** -- 6.4 wt.% against a floor of
8, and against 10-15 wt.% in the sibling A1 family. Aluminium is the strongest ferrite
stabiliser in this alloy, so the deviation runs in the austenite-forming direction, which is
the direction of the observed failure. That has to be tested rather than asserted, because
the answer decides how the paper may phrase its central claim:

    if a composition inside the agent's own window ALSO has no single-phase alpha field,
        the agent's proposal was thermodynamically unsound as proposed, and the paper's
        claim survives in full;
    if a composition inside the window DOES have one,
        the failure is at least partly a synthesis deviation, and the claim must be
        narrowed to the composition that was actually made.

Two series, both against the 1200 C solution treatment that Sec. 4.1 turns on:

    Al_scan   : the measured composition with aluminium alone stepped from the as-made
                6.24 wt.% up to A2's ceiling of 12 wt.%, iron balancing. Isolates Al.
    A2_points : compositions genuinely inside the A2 window -- its midpoint, and the two
                corners that most and least favour ferrite -- plus the as-made composition
                for reference.

Both series are run with carbon at the measured level and again with carbon removed, so the
Al effect and the C effect can be separated rather than confounded.

mpea-02b is the primary database as elsewhere, and cannot carry Si; silicon is folded into
iron for that run and the substitution is reported. mc_fe carries all six elements and is run
on the named points only, as in ni_sensitivity.py.

    python agent_window.py [mpea-02b|mc_fe ...]
"""
import csv
import io
import os
import sys

import numpy as np
from pycalphad import Database, equilibrium, variables as v

from step_diagrams import (DBDIR, OUTDIR, FRACTION_CUTOFF, NEAR_ZERO, ORDER_TOL,
                           dof_layout, order_parameter)
from ni_sensitivity import phases_at, solvus

MASS = {'FE': 55.845, 'MN': 54.938, 'AL': 26.9815,
        'NI': 58.6934, 'SI': 28.0855, 'C': 12.011}

# Hypothesis A2 as written in the report, wt.%. Fe is the balance.
A2_WINDOW = {'MN': (20.0, 30.0), 'AL': (8.0, 12.0),
             'SI': (1.0, 4.0), 'NI': (3.0, 6.0), 'C': (0.1, 0.3)}

# The alloy as melted, wt.% (Table 1, nominal column).
AS_MADE_WT = {'MN': 32.3, 'AL': 6.4, 'SI': 2.2, 'NI': 4.6, 'C': 0.1}

# Table 1, measured column (ICP-AES, C by ASTM E1019). Distinct from AS_MADE_WT chiefly in
# silicon, which came in at half the intended level -- 1.11 wt.% against 2.2.
MEASURED_WT = {'MN': 31.78, 'AL': 6.24, 'SI': 1.11, 'NI': 4.81, 'C': 0.105}

AL_SCAN_WT = np.round(np.arange(6.4, 12.01, 0.7), 2)     # as-made -> A2 ceiling
T_HI = np.arange(1000, 1401, 10) + 273.15

RUNS = [
    dict(key='mpea-02b', file='mpea-02b.tdb',
         elements=['FE', 'MN', 'AL', 'NI', 'C'],
         phases=['LIQUID:L', 'B2_BCC', 'A1_FCC', 'KAPPA_E21', 'CEMENTITE_D011',
                 'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9', 'CBCC_A12',
                 'CUB_A13', 'HCP_A3', 'SIGMA_D8B', 'AL8FE5_D82', 'AL8MN5_D810',
                 'AL13FE4', 'AL5FE2', 'AL2FE', 'AL3NI2_D513', 'AL3NI_D011',
                 'AL3NI5', 'AL4NI3', 'AL71FE5NI24', 'AL11MN4_HT', 'AL11MN4_LT',
                 'AL12MN', 'AL6MN_D2H', 'AL4MN_MU', 'AL4MN_LAMBDA'],
         bcc='B2_BCC', fcc='A1_FCC', pdens=500, points_only=False),
    dict(key='mc_fe', file='mc_fe_v2.059.pycalphad.tdb',
         elements=['FE', 'MN', 'AL', 'NI', 'SI', 'C'],
         phases=['LIQUID', 'BCC_A2', 'BCC_B2', 'FCC_A1', 'K_CARB', 'CEMENTITE',
                 'M23C6', 'M7C3', 'KSI_CARBIDE', 'M5C2', 'GRAPHITE', 'BETA_MN',
                 'ALPHA_MN', 'HCP_A3', 'G_PHASE'],
         bcc='BCC_B2', fcc='FCC_A1', pdens=2000, points_only=True),
]


def wt_to_at(wt):
    """wt.% dict (Fe implied as balance) -> at.% dict summing to 100."""
    full = dict(wt)
    full['FE'] = 100.0 - sum(wt.values())
    moles = {el: w / MASS[el] for el, w in full.items()}
    total = sum(moles.values())
    return {el: 100.0 * m / total for el, m in moles.items()}


def named_points():
    """The as-made composition plus three points genuinely inside the A2 window.

    The corners are chosen on ferrite-forming tendency, not arbitrarily: Al and Ni are the
    ferrite/B2 formers here and Mn is the austenite stabiliser, so the ferritic corner takes
    Al and Ni high with Mn and C low, and the austenitic corner the reverse. Together they
    bracket what the agent's own window permits.
    """
    lo = {el: r[0] for el, r in A2_WINDOW.items()}
    hi = {el: r[1] for el, r in A2_WINDOW.items()}
    mid = {el: 0.5 * (r[0] + r[1]) for el, r in A2_WINDOW.items()}
    return [
        # Control. This is the composition ni_sensitivity.py already scanned, reached here by a
        # different route (wt.% -> at.% -> renormalise). It must reproduce that run's answer --
        # mpea-02b solvus 1340 C, 71.1 alpha / 28.9 gamma at 1200 C; mc_fe melting from ~1240 C
        # with 61.9 / 38.1 at 1200 C. If it does not, the discrepancy is in this script, not in
        # the chemistry, and nothing else in the table can be believed.
        ('measured', MEASURED_WT),
        ('as_made', AS_MADE_WT),
        ('A2_midpoint', mid),
        ('A2_ferritic', {'MN': lo['MN'], 'AL': hi['AL'], 'SI': hi['SI'],
                         'NI': hi['NI'], 'C': lo['C']}),
        ('A2_austenitic', {'MN': hi['MN'], 'AL': lo['AL'], 'SI': lo['SI'],
                           'NI': lo['NI'], 'C': hi['C']}),
    ]


def al_scan_points():
    out = []
    for al in AL_SCAN_WT:
        wt = dict(AS_MADE_WT)
        wt['AL'] = float(al)
        out.append(('Al_%.1fwt' % al, wt))
    return out


def conditions(at_pct, elements):
    """at.% -> pycalphad mole-fraction conditions, renormalised over the DB's elements.

    Silicon is dropped for mpea-02b, which does not carry it; renormalising rather than
    zeroing means the remaining elements keep their ratios and the iron balance absorbs
    the silicon, which is the least-wrong of the available substitutions.
    """
    raw = {el: at_pct.get(el, 0.0) for el in elements}
    total = sum(raw.values())
    frac = {el: val / total for el, val in raw.items()}
    return ({v.X(el): max(frac[el], NEAR_ZERO) for el in elements if el != 'FE'},
            frac)


def run(cfg, report, rows):
    dbf = Database(os.path.join(DBDIR, cfg['file']))
    comps = cfg['elements'] + ['VA']
    phases = [p for p in cfg['phases'] if p in dbf.phases]
    layout = dof_layout(dbf, comps, cfg['bcc']) if cfg['bcc'] in dbf.phases else None

    points = named_points() if cfg['points_only'] else named_points() + al_scan_points()
    dropped = [el for el in MASS if el not in cfg['elements']]

    report.write(u'\n' + u'=' * 78 + u'\n%s   elements: %s%s\n'
                 % (cfg['key'], ' '.join(cfg['elements']),
                    ('   [dropped, folded into Fe: %s]' % ', '.join(dropped)) if dropped else ''))

    for carbon_free in (False, True):
        series = 'C_free' if carbon_free else 'C_measured'
        report.write(u'\n--- %s / %s ---\n' % (cfg['key'], series))
        report.write(u'%-14s  %-42s  %10s  %s\n'
                     % ('point', 'composition (at.%)', 'a-solvus', 'phases at 1200 C'))

        for name, wt in points:
            at_pct = wt_to_at(wt)
            if carbon_free:
                at_pct['C'] = NEAR_ZERO
            conds, frac = conditions(at_pct, cfg['elements'])

            hi = dict(conds); hi.update({v.T: T_HI, v.P: 101325, v.N: 1})
            eq = equilibrium(dbf, comps, phases, hi, calc_opts={'pdens': cfg['pdens']})
            temps_c = [round(float(t) - 273.15, 1) for t in T_HI]
            per_T = [phases_at(eq, i, cfg, layout) for i in range(len(T_HI))]

            sol, excursions = solvus(temps_c, per_T, cfg)
            at1200 = per_T[temps_c.index(1200.0)]
            desc = ', '.join('%s %.1f%%' % (k, 100 * f)
                             for k, f in sorted(at1200.items(), key=lambda kv: -kv[1]))
            shown = ' '.join('%s%.1f' % (el.title(), at_pct[el])
                             for el in ('FE', 'MN', 'AL', 'NI', 'SI', 'C') if el in at_pct)
            report.write(u'%-14s  %-42s  %10s  %s\n'
                         % (name, shown, ('%.0f C' % sol) if sol else 'none <=1400',
                            desc or '*** NOT CONVERGED ***'))
            for tc, what in excursions:
                report.write(u'        !! %g C above the solvus is not single-phase bcc: %s\n'
                             % (tc, what))

            for tc, seen in zip(temps_c, per_T):
                for label, f in seen.items():
                    rows.append(dict(database=cfg['key'], series=series, point=name,
                                     al_wt=wt['AL'], mn_wt=wt['MN'], ni_wt=wt['NI'],
                                     si_wt=wt['SI'], c_wt=wt['C'], T_C=tc,
                                     label=label, fraction=f,
                                     alpha_solvus_C=sol if sol else ''))
            print('  %s %s %-14s solvus=%s' % (cfg['key'], series, name, sol))


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    wanted = [a for a in sys.argv[1:] if not a.startswith('-')]
    runs = [c for c in RUNS if c['key'] in wanted] if wanted else RUNS
    if wanted and not runs:
        raise SystemExit('no database matches %s (have: %s)'
                         % (wanted, ', '.join(c['key'] for c in RUNS)))

    path = os.path.join(OUTDIR, 'agent_window.csv')
    txt = os.path.join(OUTDIR, 'agent_window.txt')
    fields = ['database', 'series', 'point', 'al_wt', 'mn_wt', 'ni_wt', 'si_wt', 'c_wt',
              'T_C', 'label', 'fraction', 'alpha_solvus_C']

    # Merge, never replace -- a subset re-run must not discard the other database's scan.
    kept = []
    if wanted and os.path.exists(path):
        with open(path, newline='', encoding='utf-8') as fh:
            kept = [r for r in csv.DictReader(fh) if r['database'] not in wanted]

    mode = 'a' if wanted and os.path.exists(txt) else 'w'
    report = io.open(txt, mode, encoding='utf-8')
    report.write(u'\nHypothesis A2 window vs the alloy as made.%s\n'
                 % ('  [re-run of %s]' % ', '.join(wanted) if wanted else ''))
    report.write(u'A2 (wt.%%): Fe bal, %s\n'
                 % ', '.join('%s %g-%g' % (el.title(), r[0], r[1])
                             for el, r in A2_WINDOW.items()))
    report.write(u'as made (wt.%%): Fe bal, %s\n'
                 % ', '.join('%s %g' % (el.title(), w) for el, w in AS_MADE_WT.items()))

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
