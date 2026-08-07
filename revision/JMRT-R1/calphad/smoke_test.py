"""Feasibility check for the JMRT revision's CALPHAD work.

Two questions:

  1. Does an open database reproduce the *benchmark* alloy's known behaviour?
     Omori et al. solution-treat at 1200 C expecting single-phase alpha (A2 bcc).
     If the database gets the control right, its verdict on the test alloy is quotable.

  2. Does removing carbon from the LLM composition change the phase constitution?
     This is the in-silico C-free control R1#1 asks for and R3#9 challenges.

Run fetch_databases.py first.  ~5 s per equilibrium point.
"""
import io
import os
import time

from pycalphad import Database, equilibrium, variables as v

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'db', 'mpea-02b.tdb')

# at.% from ICP-AES, renormalised without Si (absent from mpea-02b) and P.
ALLOYS = [
    ('BENCHMARK (Fe-34.2Mn-15.2Al-7.8Ni-0.04C)',
     {v.X('MN'): 0.3415, v.X('AL'): 0.1522, v.X('NI'): 0.0781, v.X('C'): 0.0004}),
    ('LLM-ALLOY (Fe-30.4Mn-12.2Al-4.3Ni-0.46C)',
     {v.X('MN'): 0.3042, v.X('AL'): 0.1215, v.X('NI'): 0.0429, v.X('C'): 0.0046}),
    ('LLM-ALLOY, C set to zero',
     {v.X('MN'): 0.3056, v.X('AL'): 0.1221, v.X('NI'): 0.0431, v.X('C'): 1e-6}),
]

TEMPERATURES_C = [1200, 900, 600]

CANDIDATE_PHASES = [
    'LIQUID:L', 'B2_BCC', 'A2_BCC', 'FCC_A1', 'A1_FCC', 'KAPPA_E21',
    'CEMENTITE_D011', 'M23C6_D84', 'M7C3_D101', 'M5C2', 'GRAPHITE_A9',
    'AL8FE5_D82', 'AL8MN5_D810', 'AL13FE4', 'AL5FE2', 'AL2FE',
    'AL3NI2_D513', 'AL3NI_D011', 'AL3NI5', 'AL4NI3', 'AL71FE5NI24',
    'BCC_A2', 'HCP_A3', 'CBCC_A12', 'CUB_A13', 'SIGMA_D8B',
]


def stable_phases(eq, cutoff=1e-6):
    """Collapse an equilibrium result to {phase name: molar fraction}."""
    out = {}
    for name, frac in zip(eq.Phase.squeeze().values.flatten(),
                          eq.NP.squeeze().values.flatten()):
        name = str(name)
        if name and frac == frac and frac > cutoff:   # frac == frac filters NaN
            out[name] = out.get(name, 0.0) + float(frac)
    return out


def main():
    if not os.path.exists(DB):
        raise SystemExit('missing %s -- run fetch_databases.py first' % DB)

    report = io.open(os.path.join(HERE, 'smoke_test_results.txt'), 'w', encoding='utf-8')

    t0 = time.time()
    dbf = Database(DB)
    comps = ['FE', 'MN', 'AL', 'NI', 'C', 'VA']
    phases = [p for p in CANDIDATE_PHASES if p in dbf.phases]
    report.write(u'mpea-02b, %d phases: %s\n\n' % (len(phases), ', '.join(phases)))

    for label, composition in ALLOYS:
        report.write(u'--- %s ---\n' % label)
        for temp_c in TEMPERATURES_C:
            conds = dict(composition)
            conds.update({v.T: temp_c + 273.15, v.P: 101325, v.N: 1})
            eq = equilibrium(dbf, comps, phases, conds)
            frac = stable_phases(eq)
            report.write(u'  %5d C : %s\n' % (temp_c, ', '.join(
                '%s %.1f%%' % (k, 100 * f)
                for k, f in sorted(frac.items(), key=lambda kv: -kv[1]))))
        report.write(u'\n')

    report.write(u'total %.0f s\n' % (time.time() - t0))
    report.close()
    print('wrote smoke_test_results.txt')


if __name__ == '__main__':
    main()
