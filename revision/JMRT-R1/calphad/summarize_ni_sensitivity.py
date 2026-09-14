"""Re-derive the Ni-sensitivity summary tables from ni_sensitivity.csv.

The scan itself is expensive (about twenty minutes for mpea-02b), so when the reporting
logic changes the tables are rebuilt from the stored per-temperature data rather than by
re-running the equilibria. That is also why this is a separate script: the CSV is the
record, and every table in NI-SENSITIVITY.md should be reproducible from it alone.

Specifically, the alpha-solvus column in the .txt written by the original run used the
first version of solvus(), which invalidated the solvus on any later non-single-phase
point. One solver artifact (C_free, Ni 5.4 at.%, a lone 100% FCC point at 1210 C between
100% BCC at 1200 and 1220 C) therefore moved that entry from 1160 to 1220 C. This script
applies the corrected rule -- report the first crossing, list later excursions separately
-- so an artifact can neither shift the number nor vanish from the record.

    python summarize_ni_sensitivity.py [csv path]
"""
import collections
import csv
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'results')
BCC_PREFIXES = ('B2_BCC', 'BCC_A2', 'BCC_B2', 'BCC_4SL')
ORDER_T = [425, 500, 600, 700, 800, 900, 950]


def load(path):
    with open(path, newline='', encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    grid = collections.defaultdict(dict)          # (db, series, ni) -> {T: {label: frac}}
    for r in rows:
        key = (r['database'], r['series'], float(r['ni_at']))
        grid[key].setdefault(float(r['T_C']), {})[r['label']] = float(r['fraction'])
    return grid


def is_bcc(label):
    return label.startswith(BCC_PREFIXES)


LIQUID_TOL = 5e-3        # same threshold as ni_sensitivity.py


def solvus(per_T):
    """First temperature at which bcc is the only phase -- no gamma, no liquid -- below
    the solidus, plus later excursions, plus the solidus.

    Same rule as ni_sensitivity.solvus() after the 2026-09-14 correction. Until then the
    bcc share was taken against the SOLID total, so an alloy that melts while still duplex
    was reported as reaching a "solvus" at the temperature its last gamma dissolved into
    the liquid. That is not a solution-treatment window. The share is now taken against
    unity and the scan stops at the solidus; an alloy that never becomes single-phase bcc
    in the solid state reports no solvus at all, which is the load-bearing answer for the
    carbon-bearing composition.
    """
    temps = [T for T in sorted(per_T) if T >= 1000]
    solidus = next((T for T in temps
                    if sum(f for k, f in per_T[T].items() if k.startswith('LIQUID'))
                    > LIQUID_TOL), None)
    first, excursions = None, []
    for T in temps:
        if solidus is not None and T >= solidus:
            break
        phases = per_T[T]
        total = sum(phases.values())
        if not phases or total <= 0:
            continue
        if sum(f for k, f in phases.items() if is_bcc(k)) / total > 0.999:
            if first is None:
                first = T
        elif first is not None:
            excursions.append((T, ', '.join('%s %.3f' % kv for kv in
                                            sorted(phases.items(), key=lambda x: -x[1]))))
    return first, excursions, solidus


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(OUTDIR, 'ni_sensitivity.csv')
    grid = load(src)
    out = io.StringIO()
    out.write(u'Ni sensitivity summary, re-derived from %s\n' % os.path.basename(src))

    for db in sorted({k[0] for k in grid}):
        for series in ('C_measured', 'C_free'):
            keys = sorted([k for k in grid if k[0] == db and k[1] == series],
                          key=lambda k: k[2])
            if not keys:
                continue
            out.write(u'\n--- %s / %s ---\n' % (db, series))
            out.write(u'%6s  %10s  %9s  %s\n'
                      % ('Ni at%', 'a-solvus', 'solidus', 'phases at 1200 C'))
            for k in keys:
                per_T = grid[k]
                sol, exc, solidus = solvus(per_T)
                at1200 = per_T.get(1200.0, {})
                desc = ', '.join('%s %.1f%%' % (lbl, 100 * f) for lbl, f
                                 in sorted(at1200.items(), key=lambda x: -x[1]))
                out.write(u'%6.1f  %10s  %9s  %s\n'
                          % (k[2], ('%.0f C' % sol) if sol else 'none (solid)',
                             ('%.0f C' % solidus) if solidus else '>1400',
                             desc or '*** no converged solution ***'))
                for T, what in exc:
                    out.write(u'        !! %g C above the solvus is not single-phase '
                              u'solid: %s\n' % (T, what))

        # ordering table, carbon-bearing series only
        keys = sorted([k for k in grid if k[0] == db and k[1] == 'C_measured'],
                      key=lambda k: k[2])
        if keys:
            out.write(u'\nOrdered-bcc mole fraction, %s, C at the measured 0.45 at%%\n' % db)
            out.write(u'%6s | %s\n' % ('T (C)', '  '.join('Ni%-5.1f' % k[2] for k in keys)))
            for T in ORDER_T:
                cells = []
                for k in keys:
                    per_T = grid[k].get(float(T))
                    if not per_T:
                        cells.append('  n/c ')
                    else:
                        cells.append('%5.1f%%' % (100 * sum(
                            f for lbl, f in per_T.items() if 'ordered' in lbl)))
                out.write(u'%6d | %s\n' % (T, '  '.join(cells)))

    # non-convergence census across the whole grid
    out.write(u'\nNon-converged points (reported as gaps, never as zeros):\n')
    any_missing = False
    expected = set(range(400, 951, 25)) | set(range(1000, 1401, 10))
    for k in sorted(grid, key=lambda x: (x[0], x[1], x[2])):
        gaps = sorted(t for t in expected if float(t) not in grid[k])
        if gaps:
            any_missing = True
            out.write(u'  %-10s %-11s Ni %-4.1f : %s\n'
                      % (k[0], k[1], k[2], ', '.join(str(g) for g in gaps)))
    if not any_missing:
        out.write(u'  none\n')

    text = out.getvalue()
    dest = os.path.join(OUTDIR, 'ni_sensitivity_summary.txt')
    io.open(dest, 'w', encoding='utf-8').write(text)
    print(text)
    print('-> %s' % dest)


if __name__ == '__main__':
    main()
