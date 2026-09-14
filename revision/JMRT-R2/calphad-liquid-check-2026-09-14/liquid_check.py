"""Verification run: repeat the mpea-02b and PrecHiMn-04 step diagrams of
revision/JMRT-R1/calphad/step_diagrams.py over 1000-1400 C with the liquid phase
INCLUDED. The deposited run asked for 'LIQUID:L'; pycalphad names the phase
'LIQUID', so run() silently dropped it (results/step_diagrams.txt lines 8 and 57:
'absent : LIQUID:L'). Same alloys, same renormalisation, same pdens (500).
Nothing in the repo is modified; output goes to liquid_check.txt beside this file.
"""
import os
import sys
import numpy as np
from pycalphad import Database, equilibrium, variables as v

HERE = os.path.dirname(os.path.abspath(__file__))
DBDIR = r'C:\Users\frank\fe-sma-paper\revision\JMRT-R1\calphad\db'
OUT = os.path.join(HERE, 'liquid_check.txt')

T_MIN_C, T_MAX_C, T_STEP_C = 1000, 1400, 10
NEAR_ZERO = 1e-6
PDENS = 500

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
        key='mpea-02b', file='mpea-02b.tdb',
        elements=['FE', 'MN', 'AL', 'NI', 'C'],
        phases=['LIQUID', 'B2_BCC', 'A1_FCC', 'KAPPA_E21', 'CEMENTITE_D011',
                'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9', 'CBCC_A12',
                'CUB_A13', 'HCP_A3', 'SIGMA_D8B', 'AL8FE5_D82', 'AL8MN5_D810',
                'AL13FE4', 'AL5FE2', 'AL2FE', 'AL3NI2_D513', 'AL3NI_D011',
                'AL3NI5', 'AL4NI3', 'AL71FE5NI24', 'AL11MN4_HT', 'AL11MN4_LT',
                'AL12MN', 'AL6MN_D2H', 'AL4MN_MU', 'AL4MN_LAMBDA'],
        alloys=['llm', 'llm_noC', 'benchmark'],
    ),
    dict(
        key='PrecHiMn-04', file='PrecHiMn-04_2.pycalphad.tdb',
        elements=['FE', 'MN', 'AL', 'SI', 'C'],
        phases=['LIQUID', 'BCC_4SL', 'A1_FCC', 'KAPPA_E21', 'CEMENTITE_D011',
                'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9', 'CBCC_A12',
                'CUB_A13', 'HCP_A3', 'AL8FE5_D82', 'AL8MN5_D810', 'AL13FE4',
                'AL5FE2', 'AL2FE', 'AL12MN', 'AL6MN_D2H', 'AL11MN4_HT',
                'AL11MN4_LT', 'FE2SI', 'FESI2_H', 'FESI2_L', 'M3SI',
                'M5SI3_D88', 'FE8SI2C', 'SIGMA_D8B'],
        alloys=['llm', 'llm_noC'],
    ),
]


def conditions_for(alloy, elements):
    raw = {el: ALLOYS[alloy].get(el, 0.0) for el in elements}
    total = sum(raw.values())
    frac = {el: val / total for el, val in raw.items()}
    return {v.X(el): max(frac[el], NEAR_ZERO)
            for el in elements if el != 'FE'}, frac


def main():
    out = open(OUT, 'w', encoding='utf-8')

    def w(s):
        out.write(s + '\n')
        out.flush()
        print(s, flush=True)

    w('Liquid-included check, %d-%d C, %d C steps, pdens %d' % (T_MIN_C, T_MAX_C, T_STEP_C, PDENS))
    temps = np.arange(T_MIN_C, T_MAX_C + 1, T_STEP_C) + 273.15
    for cfg in RUNS:
        dbf = Database(os.path.join(DBDIR, cfg['file']))
        comps = cfg['elements'] + ['VA']
        phases = [p for p in cfg['phases'] if p in dbf.phases]
        missing = [p for p in cfg['phases'] if p not in dbf.phases]
        w('=' * 78)
        w('%s  (%s)' % (cfg['key'], cfg['file']))
        w('phases  : %s' % ' '.join(phases))
        w('absent  : %s' % (' '.join(missing) if missing else '(none)'))
        if 'LIQUID' not in phases:
            w('!!! LIQUID still not in this database under that name: %s' % sorted(dbf.phases))
            continue
        for alloy in cfg['alloys']:
            conds, frac = conditions_for(alloy, cfg['elements'])
            w('--- %s / %s ---' % (cfg['key'], alloy))
            w('    at.%%: %s' % ', '.join('%s %.3f' % (el, 100 * f) for el, f in sorted(frac.items())))
            conds = dict(conds)
            conds.update({v.T: temps, v.P: 101325, v.N: 1})
            eq = equilibrium(dbf, comps, phases, conds, calc_opts={'pdens': PDENS})
            for t in eq.T.values:
                names = eq.Phase.sel(T=t).values.ravel()
                fracs = eq.NP.sel(T=t).values.ravel()
                acc = {}
                for n, f in zip(names, fracs):
                    if n and not np.isnan(f):
                        acc[n] = acc.get(n, 0.0) + float(f)
                if not acc:
                    w('   %5.0f C : *** NOT CONVERGED ***' % (t - 273.15))
                    continue
                items = sorted(acc.items(), key=lambda kv: -kv[1])
                w('   %5.0f C : %s' % (t - 273.15, ', '.join('%s %.1f%%' % (n, 100 * f) for n, f in items if f > 1e-4)))
    w('DONE')
    out.close()


if __name__ == '__main__':
    main()
