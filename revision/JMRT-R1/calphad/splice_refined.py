"""Merge the refined mc_fe / LLM-alloy points into the main step-diagram CSV.

refine_mc_fe.py re-computes a temperature band at pdens=2000 because the pdens=500
sweep failed to converge there and returned spurious single-phase answers next to the
failures. This replaces those temperatures, leaving everything else untouched, and
reports exactly what changed so the substitution is auditable rather than silent.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'results')
MAIN = os.path.join(OUTDIR, 'step_diagrams.csv')
PART = os.path.join(OUTDIR, 'mc_fe_llm_refined.csv')
FIELDS = ['database', 'alloy', 'T_C', 'phase', 'label', 'set_index', 'fraction']

NONCONV = '__NONCONVERGED__'


def load(path):
    with open(path, newline='', encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def summarise(rows):
    """{T_C: {phase: fraction}} for one database/alloy."""
    out = {}
    for r in rows:
        t = float(r['T_C'])
        out.setdefault(t, {})
        if r['phase'] == NONCONV:
            out[t] = None
            continue
        if out[t] is None:
            continue
        try:
            out[t][r['phase']] = out[t].get(r['phase'], 0.0) + float(r['fraction'])
        except ValueError:
            pass
    return out


def fmt(d):
    if d is None:
        return 'NOT CONVERGED'
    return ', '.join('%s %.1f%%' % (k, 100 * v)
                     for k, v in sorted(d.items(), key=lambda kv: -kv[1]))


def main():
    main_rows = load(MAIN)
    refined = load(PART)
    if not refined:
        raise SystemExit('no refined rows in %s' % PART)

    temps = {float(r['T_C']) for r in refined}
    target = lambda r: r['database'] == 'mc_fe' and r['alloy'] == 'llm'

    old = summarise([r for r in main_rows if target(r) and float(r['T_C']) in temps])
    new = summarise(refined)

    print('replacing %d temperatures in mc_fe / llm\n' % len(temps))
    changed = 0
    for t in sorted(temps):
        a, b = fmt(old.get(t, {})), fmt(new.get(t, {}))
        if a != b:
            changed += 1
            print('  %6.0f C\n      was: %s\n      now: %s' % (t, a, b))
    print('\n%d of %d temperatures changed' % (changed, len(temps)))

    kept = [r for r in main_rows
            if not (target(r) and float(r['T_C']) in temps)]
    merged = kept + refined
    merged.sort(key=lambda r: (r['database'], r['alloy'], float(r['T_C']),
                               int(r['set_index'])))

    with open(MAIN, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(merged)
    print('wrote %d rows -> %s' % (len(merged), MAIN))


if __name__ == '__main__':
    main()
