"""Does the D0_3 assignment in Fig. 5 hold up across ALL its unique reflections?

Fig. 5 of the submission labels three phases: FCC(gamma), BCC(alpha) and Fe3Al.
The Fe3Al (D0_3) cell is exactly the bcc cell doubled (a = 5.796 = 2 x 2.898), so:

  D0_3 {220} == bcc {110}      \
  D0_3 {400} == bcc {200}       >  shared -- carry no information about ordering
  D0_3 {422} == bcc {211}      /

  D0_3 {200}, {222}, {420}        shared with B2 ordering
  D0_3 {111}, {311}, {331}, {511} ALL-ODD -- unique to D0_3, B2 cannot produce them

So the entire 34 % alpha / 4 % D0_3 split in the refinement rests on the all-odd
reflections. If they are present in the LLM-alloy and absent in the benchmark, the
assignment is sound. This script measures every one of them.
"""
import glob
import io
import itertools
import os

import numpy as np

LAMBDA = 0.125870
A_BCC = 2.89816
A_D03 = 2 * A_BCC
A_FCC = 3.64862

CHI_DIR = r'E:\FE-SMA\synchrotron.chi'
HERE = os.path.dirname(os.path.abspath(__file__))

SAMPLES = {
    'Sam1': 'LLM-alloy, 3-cycle AGG',
    'Sam5': 'LLM-alloy, 1200C/4fpm, 0 % strain',
    'Sam6': 'LLM-alloy, 1200C/4fpm, 10 % strain',
    'Sam7': 'benchmark, 1200C/4fpm, 0 % strain',
    'Sam8': 'benchmark, 1200C/4fpm, 8 % strain',
}


def two_theta(d):
    return 2.0 * np.degrees(np.arcsin(LAMBDA / (2.0 * d)))


def load_chi(path):
    tt, y = [], []
    with io.open(path, 'r', encoding='utf-8', errors='replace') as fh:
        for line in fh:
            p = line.split()
            if len(p) == 2:
                try:
                    tt.append(float(p[0])); y.append(float(p[1]))
                except ValueError:
                    pass
    return np.array(tt), np.array(y)


def d03_reflections(nmax=6):
    """Classify every D0_3 reflection out to nmax."""
    seen, out = set(), []
    for h, k, l in itertools.product(range(nmax + 1), repeat=3):
        if h == k == l == 0:
            continue
        hkl = tuple(sorted((h, k, l), reverse=True))
        if hkl in seen:
            continue
        par = {h % 2, k % 2, l % 2}
        if len(par) != 1:          # mixed parity -> extinct in an fcc lattice
            continue
        s = h + k + l
        if par == {1}:
            kind = 'D03-UNIQUE (all odd)'
        elif s % 4 == 0:
            kind = 'shared with bcc fundamental'
        else:
            kind = 'shared with B2 superlattice'
        d = A_D03 / np.sqrt(h * h + k * k + l * l)
        if d < 1.05 or d > 4.5:
            continue
        seen.add(hkl)
        out.append((hkl, d, two_theta(d), kind))
    return sorted(out, key=lambda r: r[2])


def rolling_baseline(y, n=60):
    """Rolling-minimum baseline, smoothed. Robust to neighbouring strong peaks,
    unlike a local linear fit whose side windows get contaminated by their tails."""
    pad = np.pad(y, n, mode='edge')
    base = np.array([pad[i:i + 2 * n + 1].min() for i in range(len(y))])
    kern = np.ones(n) / n
    return np.convolve(np.pad(base, n // 2, mode='edge'), kern, mode='same')[:len(y)]


def measure(tt, net, centre, half=0.030):
    """Net peak height at `centre` above the global baseline, and the local noise
    taken from a genuinely peak-free stretch either side of it."""
    core = (tt > centre - half) & (tt < centre + half)
    if core.sum() < 3:
        return np.nan, np.nan
    peak = net[core].max()
    # noise: nearest 0.10-0.30 deg either side, sigma-clipped so any peak tail
    # that sneaks in does not inflate the estimate
    ring = ((np.abs(tt - centre) > 0.10) & (np.abs(tt - centre) < 0.30))
    vals = net[ring]
    if vals.size < 10:
        return peak, np.nan
    for _ in range(3):
        med, sd = np.median(vals), np.std(vals)
        keep = np.abs(vals - med) < 3 * sd
        if keep.all() or keep.sum() < 10:
            break
        vals = vals[keep]
    noise = np.std(vals)
    return peak, noise


def main():
    rep = io.open(os.path.join(HERE, 'd03_test.txt'), 'w', encoding='utf-8')
    refl = d03_reflections()
    unique = [r for r in refl if r[3].startswith('D03-UNIQUE')]
    b2ish = [r for r in refl if 'B2' in r[3]]

    rep.write(u'D0_3 Fe3Al, a = %.5f A (= 2 x bcc a = %.5f)\n\n' % (A_D03, A_BCC))
    rep.write(u'Reflections unique to D0_3 (B2 cannot produce these):\n')
    for hkl, d, t, _ in unique:
        rep.write(u'   {%d%d%d}  d = %.4f A   2theta = %.4f deg\n'
                  % (hkl[0], hkl[1], hkl[2], d, t))
    rep.write(u'\nShared with B2 ordering:\n')
    for hkl, d, t, _ in b2ish:
        rep.write(u'   {%d%d%d}  d = %.4f A   2theta = %.4f deg\n'
                  % (hkl[0], hkl[1], hkl[2], d, t))

    # warn about overlaps with fcc / bcc fundamentals
    rep.write(u'\nOverlap check against fcc and bcc fundamentals '
              u'(flagged if within 0.05 deg):\n')
    fund = []
    for h, k, l in itertools.product(range(5), repeat=3):
        if h == k == l == 0:
            continue
        if len({h % 2, k % 2, l % 2}) == 1:
            d = A_FCC / np.sqrt(h * h + k * k + l * l)
            if 1.0 < d < 4:
                fund.append(('fcc', tuple(sorted((h, k, l), reverse=True)), two_theta(d)))
        if (h + k + l) % 2 == 0:
            d = A_BCC / np.sqrt(h * h + k * k + l * l)
            if 1.0 < d < 4:
                fund.append(('bcc', tuple(sorted((h, k, l), reverse=True)), two_theta(d)))
    overlap = {}
    for hkl, d, t, _ in unique + b2ish:
        near = [f for f in fund if abs(f[2] - t) < 0.12]
        overlap[hkl] = near
        rep.write(u'   {%d%d%d} @ %.4f : %s\n'
                  % (hkl[0], hkl[1], hkl[2], t,
                     'CLEAN' if not near else 'OVERLAPS ' + ', '.join(
                         '%s%s @ %.3f' % (f[0], f[1], f[2]) for f in near)))

    for path in sorted(glob.glob(os.path.join(CHI_DIR, '*.chi'))):
        base = os.path.basename(path)
        who = SAMPLES.get(base.split('-')[0], '?')
        tt, y = load_chi(path)
        net = y - rolling_baseline(y)
        # strongest reflection, for normalisation
        strong, _ = measure(tt, net, two_theta(A_BCC / np.sqrt(2)), half=0.05)
        strong2, _ = measure(tt, net, two_theta(A_FCC / np.sqrt(3)), half=0.05)
        norm = max(strong, strong2)

        rep.write(u'\n' + u'=' * 72 + u'\n%s   %s\n' % (base, who))
        rep.write(u'  %-8s %-9s %-9s %-8s %s\n'
                  % ('hkl', '2theta', '% of max', 'S/N', 'verdict'))
        for group, tag in ((unique, 'UNIQUE'), (b2ish, 'B2-shared')):
            rep.write(u'  -- %s --\n' % tag)
            for hkl, d, t, _ in group:
                if t < tt[0] + 0.2 or t > tt[-1] - 0.2:
                    continue
                peak, noise = measure(tt, net, t)
                if not np.isfinite(peak) or not np.isfinite(noise) or noise <= 0:
                    continue
                rel = 100.0 * peak / norm
                sn = peak / noise
                if overlap.get(hkl):
                    verdict = 'UNUSABLE - overlaps %s' % ', '.join(
                        '%s%s' % (f[0], f[1]) for f in overlap[hkl])
                else:
                    verdict = ('DETECTED' if sn >= 5 and rel >= 0.2 else
                               'marginal' if sn >= 3 else 'absent')
                rep.write(u'  {%d%d%d}    %-9.4f %-9.3f %-8.1f %s\n'
                          % (hkl[0], hkl[1], hkl[2], t, rel, sn, verdict))
    rep.close()
    print('wrote d03_test.txt')


if __name__ == '__main__':
    main()
