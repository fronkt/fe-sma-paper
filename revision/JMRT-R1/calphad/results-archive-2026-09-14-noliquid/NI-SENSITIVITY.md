# Ni sensitivity scan — the answer to R3#9

**Script:** `../ni_sensitivity.py` · **Data:** `ni_sensitivity.csv`, `ni_sensitivity.txt`
**Primary-database backup:** `ni_sensitivity_mpea-02b.{csv,txt}`
**Run:** 2026-08-09

Reviewer 3, comment #9: *the reduction in Ni from 7.5 to 4 at.% may matter as much as the
carbon addition.* Fair, and the C = 0 control in `step_diagrams.py` could not answer it —
that run holds nickel fixed at the measured 4.2 at.%, so it shows what carbon does at low
nickel and says nothing about what nickel does on its own.

## Design

Nickel stepped 4.2 → 7.8 at.% in 0.4 at.% increments (the measured value to the
benchmark's measured value), **iron taking up the difference** so Mn, Al, Si and C stay
exactly where they were measured. Two series:

| series | carbon | question |
|---|---|---|
| `C_measured` | 0.45 at.% | would restoring the benchmark's nickel have rescued this alloy? |
| `C_free` | removed | nickel's own effect, isolated — the second axis of the 2×2 against the existing control |

Per composition: a 1000–1400 °C sweep at 10 °C to locate the α solvus and the 1200 °C
constitution, plus a 400–950 °C sweep at 25 °C to test whether more nickel opens a usable
solution-and-age window. 20 compositions × 62 temperatures = 1240 equilibria on mpea-02b,
the only one of the three databases carrying Ni and C together. PrecHiMn-04 has no nickel
and cannot contribute.

## Result 1 — nickel does not move the α solvus. At all.

```
                    alpha solvus        phases at 1200 C
Ni at%   C_measured    C_free       C_measured (bcc / fcc)
  4.2      1340 C      1150 C         71.1 / 28.9
  5.0      1340 C      1160 C         69.0 / 31.0
  5.8      1340 C      1170 C         66.7 / 33.3
  6.6      1340 C      1180 C         64.1 / 35.9
  7.4      1340 C      1190 C         61.2 / 38.8
  7.8      1340 C      1190 C         59.6 / 40.4
```

With carbon at its measured value the solvus sits at **1340 °C at every nickel content
tested** — it does not move by even one 10 °C grid step across the full range up to the
benchmark's own nickel level. With carbon removed it lies at 1150–1190 °C and the alloy is
100 % α at 1200 °C at every nickel content.

**Carbon moves the solvus ≈190 °C. Nickel moves it ≈0 °C with carbon present, and ≈40 °C
without — upward, the wrong way.**

Worse for the nickel hypothesis: raising nickel at fixed carbon makes the alloy *more*
austenitic at 1200 °C, bcc falling 71.1 → 59.6 %. Restoring the benchmark's nickel would
have made the duplex problem marginally worse, not better.

## Result 2 — nickel controls how much B2, not whether α exists

Ordered-bcc mole fraction, C at the measured 0.45 at.%:

| T (°C) | Ni 4.2 | Ni 5.4 | Ni 6.6 | Ni 7.8 |
|---|---|---|---|---|
| 425 | 10.7 % | 13.7 % | 16.4 % | 19.0 % |
| 500 | 9.9 % | 12.8 % | 15.5 % | 18.1 % |
| 600 | 8.0 % | 11.0 % | 13.7 % | 16.3 % |
| 700 | 5.5 % | 8.5 % | 11.3 % | 13.9 % |
| 800 | 2.3 % | 5.5 % | 8.4 % | 11.1 % |
| 900 | 0.0 % | 2.0 % | 5.2 % | 8.1 % |
| 950 | 0.0 % | 0.1 % | 3.6 % | 6.6 % |

Monotonic in nickel, exactly as expected for a NiAl-based B2. But at 700 °C the full
constitution is **A1_FCC 86–94 % with the ordered bcc as the minority**, at every nickel
level — ordered bcc coexisting with austenite, not coherent B2 inside an α matrix.

## Result 3 — mc_fe cross-check agrees on everything load-bearing

Endpoints only (Ni 4.2 and 7.8 at.%), `pdens=2000`, all six elements:

| series | Ni at.% | α solvus | solidus | 1200 °C |
|---|---|---|---|---|
| C_measured | 4.2 | 1250 °C | **1240 °C** | 61.9 bcc / 38.1 fcc |
| C_measured | 7.8 | 1240 °C | **1230 °C** | 75.8 bcc / 24.2 fcc |
| C_free | 4.2 | 1130 °C | 1250 °C | 100 % bcc |
| C_free | 7.8 | 1070 °C | 1270 °C | 100 % bcc |

With carbon present the solvus lies *above* the solidus at both nickel contents — melting
begins while γ is still there, so **no single-phase α field exists in the solid state at
either nickel level.** That reproduces the primary run's conclusion by a different route
and matches what `ANALYSIS.md` already recorded for the measured composition. With carbon
removed the solvus drops several hundred degrees below the solidus at both nickel contents
and 1200 °C sits inside a fully single-phase field.

**One disagreement, reported rather than reconciled.** At 1200 °C with carbon present,
added nickel makes the alloy slightly *more* austenitic in mpea-02b (bcc 71.1 → 59.6 %) and
slightly *more* ferritic in mc_fe (bcc 61.9 → 75.8 %). The databases agree that nickel does
not open the window and disagree on the sign of the small residual shift. The manuscript
therefore claims only that **nickel does not open the solution-treatment window**, not that
it measurably closes it further.

mc_fe returns no ordered bcc at any temperature for either composition — `BCC_B2` never
appears in its result set here — so the ordering trend of Result 2 rests on mpea-02b alone.

## The conclusion for the manuscript

The two elements act on different parts of the problem, and are not competing explanations
of one failure:

> **Nickel sets how much B2 the alloy could form. Carbon sets whether there is ever an α
> matrix in which to form it coherently.**

So R3#9's premise is answered rather than deflected: nickel matters, it is simply not the
element that closed the processing window, and no amount of nickel up to the benchmark's
own content reopens it while the carbon is there.

Written into **§3.4** (result, with the numbers) and **§4.2** (interpretation, replacing
the one-line "held at its measured value in the control" that was there before).

## Numerical honesty

- **5 of 1240 points did not converge**, all at 400–425 °C in the `C_measured` series at
  the three lowest nickel contents (Ni 4.2 at 400 °C; Ni 4.6 and 5.0 at 400 and 425 °C).
  Reported as gaps, never as zeros. An earlier summary table silently rendered the missing
  Ni 4.2 / 400 °C point as "0.0 % ordered", which would have been wrong — the value at
  425 °C is 10.7 %.
- **A near-miss worth recording: melting was briefly misread as a solver artifact.** The
  first version of the solvus test took the bcc share against unity. Phase fractions
  include liquid, so once melting begins bcc falls below the 0.999 threshold *while still
  being the only solid present*. In mc_fe's carbon-free series that starts around 1250 °C,
  and it produced a run of sixteen consecutive "excursions" that the summary script duly
  labelled solver artifacts. They were nothing of the kind — they were the alloy melting,
  smoothly and correctly. The test now takes the bcc share **against the solid total** and
  reports the solidus in its own column, so partial melting is explicit. Had this gone
  unnoticed it would have mislabelled a real physical result as numerical noise, which is
  the more dangerous direction of the two.
- **One genuine solver artifact, disclosed and worked around.** In `C_free` at Ni = 5.4 at.%, the
  single point at 1210 °C returns 100 % FCC, sandwiched between 100 % BCC at both 1200 and
  1220 °C, with no two-phase transition on either side. That is a solver artifact, not a
  re-entrant γ field. The first version of `solvus()` invalidated the solvus on any later
  non-single-phase point and so reported 1220 °C for that composition instead of 1160 °C,
  breaking an otherwise smooth 1150 → 1190 °C trend. `solvus()` now returns the first
  crossing together with a list of later excursions, so an artifact can neither shift the
  reported number nor be silently dropped.
- **Self-check.** At the measured nickel content the scan reproduces the ordering curve of
  the primary run (≈10 % ordered bcc at the bottom of the range, falling to zero by
  ≈875 °C), which is what `step_diagrams.py` and Fig. 7b already show.
- **Cross-check.** mc_fe was run at the two nickel endpoints only; it carries all six
  elements but needs `pdens=2000` and is an order of magnitude slower. See
  `ni_sensitivity.txt` for its section.

## A repository hazard that was fixed in passing

`main()` originally opened the output CSV with `'w'` and wrote only the rows from the
databases named on the command line, so `python ni_sensitivity.py mc_fe` would have
silently discarded the twenty-minute mpea-02b scan. It now merges against the existing CSV,
matching the behaviour of `step_diagrams.py`.
