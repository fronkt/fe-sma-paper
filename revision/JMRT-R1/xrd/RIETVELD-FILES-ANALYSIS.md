# Rietveld files from S. Cai — analysis

**Received:** 2026-08-08, email thread *"sample 6, Ai alloy unloaded from 10% deformation"* (song_cai@fwmetals.com)
**Files:** two zips, unpacked to `xrd/from-scai/{zip1-sample6,zip2-resample6}/`
**Program:** MAUD 2.33 (confirmed from `_computing_structure_refinement`) — §2.5's method statement is correct.

| Zip | Contents |
|---|---|
| `sample6aialloyunloadedfrom10deformation.zip` | `sample-6-2.par`, `sample-6-2.par.lst` |
| `resample6aialloyunloadedfrom10deformation.zip` | `sample-5-2.prn`, `sample-5-2.prn.lst`, `sample-6-2.par`, `sample-6-2.par.lst`, `Fig.5.jpg` |

The two zips contain **different** `sample-6-2.par` files (421 KB vs 315 KB). They are two separate
refinements of the same specimen, not duplicates.

---

## Summary table

| | **Sample 5** (undeformed) | **Sample 6 — zip1** | **Sample 6 — zip2 "resample"** |
|---|---|---|---|
| Data file | `sample5-7286.esg` | `sample6-7280.esg` | `sample6-7280.esg` |
| Spectra | 73 | 73 | 73 |
| **Rwp** | **0.2141** | **0.2037** | **0.1252** |
| **Rp** | **0.0869** | **0.0985** | **0.0590** |
| Rwpb (no background) | 0.4830 | 0.4008 | 0.2153 |
| Rpb (no background) | 0.3326 | 0.2978 | 0.1504 |
| `goodness_of_fit_all` | 0.0891 | 0.0854 | 0.0854 |
| γ fcc (Fm-3m, COD 9008469) | **0.62** *fixed* | 0.63757 *(dependent)* | 0.60801 *fixed* |
| α bcc (Im-3m, COD 9000658) | **0.34** *fixed* | **0.34683 ± 0.00136** *refined* | 0.35146 *fixed* |
| D0₃ (Fm-3m) | **0.04** *fixed* | **0.01560 ± 0.00113** *refined* | 0.04053 *fixed* |
| a(γ) / a(α) / a(D0₃) Å | 3.6366 / 2.8865 / 5.7734 | 3.6366 / 2.8865 / 5.7801 | 3.6366 / 2.8865 / 5.7801 |
| Cells refined? | No | No | No |
| Texture | E-WIMV, ODF res **2°** | E-WIMV, ODF res **5°** | E-WIMV, ODF res **5°** |
| Refined parameters | 12 | 13 | 11 |

---

## Finding 1 — the specimen question is settled

**62 / 34 / 4 belongs to sample 5, the undeformed 1200 °C / 1 min specimen.** §3.3's attribution is
correct as written, and the `Rietveld-sample 6.jpg` filename confusion is resolved. This closes the
item that has been open since the comment-triage was written.

## Finding 2 — but 62 / 34 / 4 were not refined quantities

In `sample-5-2.prn.lst` all three phase fractions carry `Status: not refinable`, all three
`_riet_par_phase_scale_factor` are fixed at exactly 1.0, and the twelve refined parameters are:

- 8 × diffraction-instrument geometry (detector distance, beam centre, tilt, pixel ratio)
- 4 × Popa anisotropic crystallite size, for γ and α only

No phase fraction, no scale factor, no lattice parameter, no background term.

**Note on MAUD's convention:** the first phase fraction (`_pd_phase_atom_%0`) is *always* the
dependent variable enforcing closure to 1, so "%0 not refinable" is normal and expected. What is
not normal is that in sample 5 **%1 and %2 are also `not refinable`** — the independent fractions
were held fixed too.

**The values are exactly 0.62, 0.34, 0.04** — two decimal places, summing to exactly 1.00, in a
file that reports other quantities to eight significant figures. Those are typed-in values, not
refinement output.

Consequence: there are no ESDs on the published phase fractions because the fractions were never
refined. The paper currently presents them as the result of quantitative Rietveld phase analysis.

## Finding 3 — where the fractions *were* refined, D0₃ is 1.6 %, not 4 %

`zip1/sample-6-2.par.lst` is the only one of the three runs that refined phase fractions:

```
3  layer1:_pd_phase_atom_%1  value:0.34682828  error:0.0013615799   (α, refinable)
4  layer1:_pd_phase_atom_%2  value:0.015603083 error:0.0011342526   (D0₃, refinable)
```

γ 63.8 % (dependent) / α 34.68(14) % / **D0₃ 1.56(11) %**.

α lands almost exactly on the published 34 %. **D0₃ comes out 2.6× lower than the published 4 %.**
This bears directly on §4.1, which argues that D0₃ is a *bulk ordered constituent* at ~4 % rather
than a coherent nanoscale dispersion. At 1.6 % that argument weakens.

Caveat: the quoted ESDs (±0.14 % on a 34.7 % fraction) are implausibly tight and are the usual
MAUD least-squares underestimate. They should not be reported at face value.

## Finding 4 — the "resample" bought its better Rwp with unphysical parameters

`zip2/sample-6-2.par.lst` reports the best fit of the three (Rwp 0.125 vs 0.204) but two of its four
refined Popa crystallite-size terms are **negative**:

```
8  9000658:Popa rules:_riet_par_anisocryst_size1  value:-160.39459
9  DO3:Popa rules:_riet_par_anisocryst_size0      value:-208.09433
```

A negative crystallite size is not physical. Its phase fractions (0.6080085 / 0.35145757 / 0.0405339)
are non-round, so they look like refined output from some earlier run that was then frozen — but they
were not refined in this one.

## Finding 5 — lattice parameters were never refined in any run

All three files: `_cell_length_a Status: not refinable`, in all three phases. The parameter bounds
are also wrong (`minimum: 5.0, maximum: 30.0`) while the values are 3.6366 and 2.8865 — i.e. below
the stated minimum, which only passes because the parameter is not being varied.

S. Cai's proposed Fig. 5 caption quotes these cells as results. They are fixed inputs.

## Finding 6 — `goodness_of_fit_all` is not a usable χ²

All three report ≈0.085–0.089. A χ² of 0.085 would mean the model fits ~11× better than counting
statistics allow, which is impossible; the value reflects MAUD's `WgtSS` / `sqrt` weighting scheme,
not a conventional GoF. **Do not put this number in the caption.** Report Rwp and Rp only.

## Finding 7 — texture *was* modelled, but not identically between the two panels

Good news relative to the earlier concern: **E-WIMV ODF refinement is present in all three runs**
across all 73 azimuthal spectra, so the fibre texture of the drawn wire is being handled, and §2.5's
"72 spectra at 5° intervals" is accurate. E-WIMV is computed iteratively rather than by least
squares, which is why no texture terms appear in the refined-parameter lists.

However **the ODF resolution differs between the two panels of the proposed figure**: 2° for
sample 5, 5° for sample 6. The before/after comparison is therefore not like-for-like.

---

## What this means for the revision

The before/after pair is a real upgrade to the paper and worth having. But as delivered, the two
panels cannot be compared quantitatively:

1. Only one of the three runs refined phase fractions at all.
2. The undeformed fractions are fixed round numbers with no uncertainties.
3. The two sample-6 files disagree with each other on D0₃ by a factor of 2.6.
4. The ODF resolution differs between panels.
5. Lattice parameters are fixed everywhere, so the caption cannot quote them as measurements.

## Decision (Frank, 2026-08-08): **zip2 is canonical**

The `resample6…` bundle is the intended deliverable — it is the later refinement and the one
S. Cai assembled complete with sample 5 and `Fig.5.jpg`. Consequences accepted:

- Panel (b) reports **R_wp = 12.5 %, R_p = 5.9 %**; panel (a) reports **R_wp = 21.4 %, R_p = 8.7 %**.
- Neither panel refined its phase fractions. Sample 6's values are non-round
  (0.6080085 / 0.35145757 / 0.0405339) and look like refined output frozen for a final cycle;
  sample 5's are typed. **The remaining problem is sample 5, not sample 6.**
- The before/after (62 → 60.8, 34 → 35.1, 4 → 4.05) is consistent with the paper's thesis of no
  stress-induced transformation, but supports only the *qualitative* claim.
- The negative Popa crystallite sizes are tolerable because the manuscript never reports
  crystallite size — verified by grep against `manuscript.md`. They remain a liability only if the
  refinement files are shared with an editor.
- zip1's refined D0₃ of 1.56(11) % is now off the record as a reported number, but it still shows
  the published 4 % is **not robust** — a refinement of the same specimen put it 2.6× lower.
  §4.1's "D0₃ is a bulk ordered constituent at ~4 %" should be softened accordingly.

## Questions for S. Cai

1. **Which `sample-6-2.par` is the intended one** — zip1 (fractions refined, Rwp 0.204) or zip2
   (better Rwp 0.125, fractions fixed, negative crystallite sizes)?
2. **Where did 0.62 / 0.34 / 0.04 come from?** If an earlier refinement produced them, does that
   file still exist? If they were estimated and fixed, §3.3 has to say so.
3. **Can both specimens be re-run on one identical recipe** — same ODF resolution, phase fractions
   free, cells free, crystallite sizes constrained positive? That is the only route to a
   defensible before/after comparison, and it is what R1#3 and R2 R&D#1 are asking for.

## Still missing

- `sample-5-2.par` — the undeformed analysis file (we have only the profile and the listing)
- `sample-6-2.prn` — the deformed profile export, needed to draw panel (b)'s difference curve
