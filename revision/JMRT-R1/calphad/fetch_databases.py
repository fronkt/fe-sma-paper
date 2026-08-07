"""Fetch the open thermodynamic databases used for the JMRT revision.

The TDB files are third-party assessments and are not committed to this repo
(see README.md, "Licensing"). Run this once to populate db/.

    python fetch_databases.py
"""
import os
import urllib.request

BASE = ('https://raw.githubusercontent.com/pycalphad/binder/'
        'develop/multicomponent-databases/')

# The three we actually use, plus the ones surveyed and rejected -- kept so the
# selection in README.md can be re-derived rather than taken on trust.
USED = {
    'mpea-02b.tdb':                 'Hallstedt HEA v2b (2017). Al C Co Cr Fe Mn Ni. B2 + kappa.',
    'PrecHiMn-04_2.pycalphad.tdb':  'High-Mn steels. Al C Fe Mn N Nb Si Ti V. BCC_4SL (D03) + kappa.',
    'mc_fe_v2.059.pycalphad.tdb':   'MatCalc open Fe. 24 elements incl. all six + P. A2/B2.',
}
SURVEYED = {
    'COST507.pycalphad.tdb':        'all six elements but assessed for the Al-rich corner.',
    'iron-04.tdb':                  'no Al.',
    'mc_al_v2.032.pycalphad.tdb':   'no C.',
    'mc_ni_v2.034.pycalphad.tdb':   'Ni-base.',
    'steel1.TDB':                   'no Mn, Al or Ni.',
}


def fetch(names, dest):
    for name in names:
        target = os.path.join(dest, name)
        if os.path.exists(target):
            print('  have  %s' % name)
            continue
        print('  get   %s ...' % name, end=' ')
        urllib.request.urlretrieve(BASE + name, target)
        print('%d bytes' % os.path.getsize(target))


if __name__ == '__main__':
    import sys
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db')
    os.makedirs(dest, exist_ok=True)

    print('databases in use:')
    fetch(USED, dest)

    if '--all' in sys.argv:
        print('surveyed and rejected (for re-deriving the selection):')
        fetch(SURVEYED, dest)

    print('\ndone -> %s' % dest)
