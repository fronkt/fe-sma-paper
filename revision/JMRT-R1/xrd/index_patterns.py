"""Index the SSRF integrated patterns against bcc + fcc, and test for D0_3.

Motivation: the manuscript states the LLM-alloy is "62 % FCC gamma, 34 % BCC alpha,
4 % D0_3 Fe3Al". The only refinement artifact on the E: drive
(`697-6-7 Fe-Mn-Al-Ni-Si/X-ray fitting.jpg`, 2025-11-26) is a MAUD fit containing
exactly two phases -- bcc a = 2.89816 A and fcc a = 3.64862 A, no D0_3 -- and
reporting 70.3 % fcc. This script tests the phases directly from the integrated data.

Key crystallography:
  * bcc A2 (a ~ 2.898 A) gives only h+k+l even reflections: 110, 200, 211, 220 ...
  * B2 order doubles nothing but switches ON 100, 111, 210 ... (h+k+l odd) as
    *superlattice* reflections of the same cell.
  * D0_3 (Fe3Al) has a DOUBLED cell, a ~ 5.796 A. Its unique fingerprint is the
    (111) superlattice reflection at d ~ 3.35 A, which B2 cannot produce.
    Its (200) coincides with the B2 (100).

So: no peak near d = 3.35 A  =>  no D0_3, regardless of anything else.
    no peak near d = 2.90 A  =>  no B2 either.

Both are *fundamental-reflection-free* regions, i.e. nothing else in a bcc+fcc
mixture puts intensity there, which makes this a clean test.
"""
import glob
import io
import os

import numpy as np
from scipy.signal import find_peaks, peak_widths

LAMBDA = 0.125870          # A, SSRF BL12SW
A_BCC = 2.89816            # A, from the MAUD fit
A_FCC = 3.64862            # A, from the MAUD fit

CHI_DIR = r'E:\FE-SMA\synchrotron.chi'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index_results.txt')

# Sam -> (alloy, condition) from E:\FE-SMA\2026-1\sample list.txt
SAMPLES = {
    'Sam1': ('LLM (697-6)',       '3-cycle AGG, 1200C/1h WQ'),
    'Sam5': ('LLM (697-6)',       '1200C / 4 fpm F72, 0 % strain'),
    'Sam6': ('LLM (697-6)',       '1200C / 4 fpm F72, 10 % strain'),
    'Sam7': ('benchmark (697-7)', '1200C / 4 fpm F72, 0 % strain'),
    'Sam8': ('benchmark (697-7)', '1200C / 4 fpm F72, 8 % strain'),
}


def two_theta(d):
    """Bragg angle in degrees for a given d-spacing."""
    s = LAMBDA / (2.0 * d)
    return 2.0 * np.degrees(np.arcsin(s)) if abs(s) <= 1 else np.nan


def d_of(tt):
    return LAMBDA / (2.0 * np.sin(np.radians(tt / 2.0)))


def hkl_list(struct, a, n=5):
    """Allowed reflections with d-spacing, tagged fundamental vs superlattice."""
    out = []
    for h in range(n + 1):
        for k in range(h + 1):
            for l in range(k + 1):
                if h == k == l == 0:
                    continue
                s2 = h * h + k * k + l * l
                d = a / np.sqrt(s2)
                if d < 0.9 or d > 7:
                    continue
                if struct == 'bcc':
                    kind = 'fundamental' if (h + k + l) % 2 == 0 else 'B2-superlattice'
                elif struct == 'fcc':
                    same = (h % 2 == k % 2 == l % 2)
                    if not same:
                        continue
                    kind = 'fundamental'
                elif struct == 'D03':
                    par = [h % 2, k % 2, l % 2]
                    if len(set(par)) != 1:
                        continue
                    if (h % 4, k % 4, l % 4) == (0, 0, 0) or (h + k + l) % 4 == 0:
                        kind = 'fundamental/shared'
                    elif all(p == 1 for p in par):
                        kind = 'D03-UNIQUE'
                    else:
                        kind = 'shared with B2'
                else:
                    continue
                out.append(((h, k, l), d, two_theta(d), kind))
    return sorted(out, key=lambda r: -r[1])


def load_chi(path):
    tt, inten = [], []
    with io.open(path, 'r', encoding='utf-8', errors='replace') as fh:
        for line in fh:
            parts = line.split()
            if len(parts) == 2:
                try:
                    x, y = float(parts[0]), float(parts[1])
                except ValueError:
                    continue
                tt.append(x)
                inten.append(y)
    return np.array(tt), np.array(inten)


def background(y, frac=0.02):
    """Crude rolling-minimum baseline, smoothed."""
    n = max(5, int(len(y) * frac))
    pad = np.pad(y, n, mode='edge')
    base = np.array([pad[i:i + 2 * n + 1].min() for i in range(len(y))])
    kern = np.ones(n) / n
    return np.convolve(np.pad(base, n // 2, mode='edge'), kern, mode='same')[:len(y)]


def main():
    rep = io.open(OUT, 'w', encoding='utf-8')
    rep.write(u'SSRF integrated patterns, lambda = %.6f A\n' % LAMBDA)
    rep.write(u'Reference cells from the MAUD fit: bcc a = %.5f A, fcc a = %.5f A\n'
              % (A_BCC, A_FCC))

    a_d03 = 2 * A_BCC
    rep.write(u'\nDiagnostic windows\n')
    for name, d in [('D0_3 (111)  UNIQUE to D0_3', a_d03 / np.sqrt(3)),
                    ('B2 (100) = D0_3 (200)', A_BCC),
                    ('B2 (111) = D0_3 (222)', A_BCC / np.sqrt(3)),
                    ('bcc (110) fundamental', A_BCC / np.sqrt(2)),
                    ('fcc (111) fundamental', A_FCC / np.sqrt(3)),
                    ('fcc (200) fundamental', A_FCC / 2)]:
        rep.write(u'  %-28s d = %.4f A -> 2theta = %.4f deg\n' % (name, d, two_theta(d)))

    for path in sorted(glob.glob(os.path.join(CHI_DIR, '*.chi'))):
        base = os.path.basename(path)
        tag = base.split('-')[0]
        alloy, cond = SAMPLES.get(tag, ('?', '?'))
        tt, y = load_chi(path)
        bg = background(y)
        net = y - bg
        scale = net.max() if net.max() > 0 else 1.0

        rep.write(u'\n' + u'=' * 74 + u'\n')
        rep.write(u'%s   %s   %s\n' % (base, alloy, cond))
        rep.write(u'2theta range %.4f - %.4f deg, %d points\n' % (tt[0], tt[-1], len(tt)))

        idx, props = find_peaks(net, prominence=0.02 * scale, distance=5)
        widths = peak_widths(net, idx, rel_height=0.5)[0]
        step = np.median(np.diff(tt))

        rep.write(u'\n  %-9s %-9s %-8s %-7s  %s\n'
                  % ('2theta', 'd (A)', 'I/Imax', 'FWHM', 'assignment'))
        for i, w in zip(idx, widths):
            d = d_of(tt[i])
            rel = net[i] / scale
            if rel < 0.01:
                continue
            best, err = '', 1e9
            for struct, a in (('bcc', A_BCC), ('fcc', A_FCC)):
                for hkl, dd, _, kind in hkl_list(struct, a):
                    e = abs(dd - d) / d
                    if e < err:
                        err, best = e, '%s %s %s' % (struct, hkl, kind)
            label = best if err < 0.01 else 'UNINDEXED (nearest %s, %.1f%% off)' % (
                best, 100 * err)
            rep.write(u'  %-9.4f %-9.4f %-8.3f %-7.4f  %s\n'
                      % (tt[i], d, rel, w * step, label))

        # explicit diagnostic windows
        rep.write(u'\n  Diagnostic windows -- net intensity relative to the strongest peak:\n')
        for name, d in [('D0_3 (111) UNIQUE', a_d03 / np.sqrt(3)),
                        ('B2 (100) / D0_3 (200)', A_BCC),
                        ('B2 (111) / D0_3 (222)', A_BCC / np.sqrt(3))]:
            centre = two_theta(d)
            if np.isnan(centre) or centre < tt[0] or centre > tt[-1]:
                rep.write(u'    %-24s 2theta %.4f OUTSIDE measured range\n'
                          % (name, centre))
                continue
            win = (tt > centre - 0.03) & (tt < centre + 0.03)
            local = net[win]
            noise = np.std(net[(tt > centre - 0.25) & (tt < centre + 0.25)])
            peak_rel = local.max() / scale if local.size else float('nan')
            rep.write(u'    %-24s 2theta %.4f : max %.4f of Imax, '
                      u'local sigma %.4f -> %s\n'
                      % (name, centre, peak_rel, noise / scale,
                         'PEAK PRESENT' if local.max() > 5 * noise else 'no peak above 5 sigma'))
    rep.close()
    print('wrote %s' % OUT)


if __name__ == '__main__':
    main()
