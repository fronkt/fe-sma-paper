# Ni sensitivity scan — the answer to R3#9 (Round 1)

**Script:** `../ni_sensitivity.py` · **Data:** `ni_sensitivity.csv`, `ni_sensitivity.txt`,
`ni_sensitivity_summary.txt` (rebuilt by `../summarize_ni_sensitivity.py`)
**Run:** 2026-09-14, liquid phase included. **Supersedes** the 2026-08-09 run, archived in
`../results-archive-2026-09-14-noliquid/`.

> **Correction, 2026-09-14.** The 2026-08-09 run requested the liquid phase as `'LIQUID:L'`;
> pycalphad names it `'LIQUID'` and the script dropped the unknown name silently, so every
> mpea-02b number in the earlier version of this note was computed for an alloy that could
> not melt. That is where "the α solvus sits at 1340 °C at every nickel content" came from:
> the last γ dissolved at 1340 °C in a solid that should already have been partly liquid.
> With the liquid phase present the carbon-bearing alloy melts before any single-phase α
> field opens, at every nickel content. `solvus()` was also redefined at the same time: it
> now reports the lowest temperature at which bcc is the *only* phase — no γ, no liquid —
> and reports the solidus in its own column, instead of measuring bcc against the solid
> total (which had let a partly molten alloy count as "single-phase α"). The mc_fe endpoints
> used the correct phase name in August and are unchanged.

Reviewer 3, Round-1 comment #9: *the reduction in Ni from 7.5 to 4 at.% may matter as much as
the carbon addition.* Fair, and the C = 0 control in `step_diagrams.py` could not answer it —
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

Per composition: a 1000–1400 °C sweep at 10 °C to locate the solid-state α solvus, the
solidus and the 1200 °C constitution, plus a 400–950 °C sweep at 25 °C to test whether more
nickel opens a usable solution-and-age window. 20 compositions × 62 temperatures = 1240
equilibria on mpea-02b (pdens 500), the only one of the three databases carrying Ni and C
together. PrecHiMn-04 has no nickel and cannot contribute. mc_fe (pdens 2000) is run at the
two nickel endpoints as a cross-check.

## Result 1 — with carbon present there is no single-phase α field in the solid state, at any nickel content

```
                   solid-state a-solvus     solidus      phases at 1200 C
Ni at%   C_measured   C_free       C_measured  C_free    C_measured (bcc / fcc)
  4.2      none        1150 C        1300 C     1380 C     71.1 / 28.9
  5.0      none        1160 C        1300 C     1370 C     69.0 / 31.0
  5.8      none        1170 C        1290 C     1370 C     66.7 / 33.3
  6.6      none        1180 C        1310 C     1360 C     64.1 / 35.9
  7.4      none        1190 C        1300 C     1350 C     61.2 / 38.8
  7.8      none        1190 C        1300 C     1350 C     59.6 / 40.4
```

With carbon at its measured value the alloy is still α + γ at the last solid temperature and
begins to melt at 1290–1310 °C (the ±10 °C scatter is the 10 °C grid), at **every nickel
content from 4.2 to 7.8 at.%**. There is no temperature at which it is single-phase α.
With carbon removed the field opens at 1150–1190 °C, some 160–230 °C below the solidus,
and the alloy is 100 % α at 1200 °C at every nickel content.

**Carbon decides whether the field exists at all. Nickel moves the carbon-free solvus by
≈40 °C — upward, the wrong way — and does nothing to create a field where carbon has
removed one.**

Worse for the nickel hypothesis: raising nickel at fixed carbon makes the alloy *more*
austenitic at 1200 °C, bcc falling 71.1 → 59.6 %. Restoring the benchmark's nickel would
have made the duplex problem marginally worse, not better.

## Result 2 — nickel controls how much B2, not whether α exists

Ordered-bcc mole fraction, C at the measured 0.45 at.% (unchanged from August — the liquid
phase plays no part below 1000 °C):

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

| series | Ni at.% | solid-state α solvus | solidus | 1200 °C |
|---|---|---|---|---|
| C_measured | 4.2 | none | **1240 °C** | 61.9 bcc / 38.1 fcc |
| C_measured | 7.8 | none | **1230 °C** | 75.8 bcc / 24.2 fcc |
| C_free | 4.2 | 1130 °C | 1250 °C | 100 % bcc |
| C_free | 7.8 | 1070 °C | 1270 °C | 100 % bcc |

The two databases now say the same thing about the carbon-bearing alloy: it melts while γ
is still present, so no single-phase α field exists in the solid state at either nickel
level. They differ on *where* it melts — mc_fe ≈1240 °C, mpea-02b ≈1300 °C — and that
difference is reported, not reconciled; nothing in the argument depends on it. With carbon
removed both open a single-phase α field well below the solidus and 1200 °C lies inside it.

**One disagreement, reported rather than reconciled.** At 1200 °C with carbon present,
added nickel makes the alloy slightly *more* austenitic in mpea-02b (bcc 71.1 → 59.6 %) and
slightly *more* ferritic in mc_fe (bcc 61.9 → 75.8 %). The databases agree that nickel does
not open the window and disagree on the sign of the small residual shift. The manuscript
therefore claims only that **nickel does not open the solution-treatment window**, not that
it measurably closes it further.

mc_fe returns no ordered bcc at any temperature for either composition — `BCC_B2` never
appears in its result set here — so the ordering trend of Result 2 rests on mpea-02b alone.

## The conclusion for the manuscript

> **Nickel sets how much B2 the alloy could form. Carbon sets whether there is ever an α
> matrix in which to form it coherently — and with carbon present there is none, at any
> nickel content, before the alloy melts.**

So R3#9's premise is answered rather than deflected: nickel matters, it is simply not the
element that closed the processing window, and no amount of nickel up to the benchmark's
own content reopens it while the carbon is there.

Written into **§3.4** (result, with the numbers) and **§4.2** (interpretation).

## Numerical honesty

- **Three of 1240 mpea-02b points did not converge**, all at 400–425 °C in the `C_measured`
  series (Ni 4.6 at 400 and 425 °C; Ni 5.0 at 425 °C), plus mc_fe Ni 4.2 at 400 °C.
  Reported as gaps, never as zeros.
- **The solidus scatters by ±10 °C along the nickel series** (1290–1310 °C) with no trend;
  that is the 10 °C grid and the pdens-500 global search near a phase boundary, not a
  nickel effect. Quote it as ≈1300 °C.
- **Grid dependence near the solidus is real in this system** and was arbitrated by Gibbs
  energy for the primary step diagrams (`../compare_gm.py`, `../refine_by_gm.py`): denser
  grids converge to a metastable single-phase γ state with a *higher* Gibbs energy than the
  duplex. The Ni scan was not re-run at other densities; its 1200 °C constitutions coincide
  with the GM-arbitrated primary run at Ni = 4.2 at.% (71.1 / 28.9), which is the self-check.
- **One genuine solver artifact, disclosed and worked around.** In `C_free` at Ni = 5.4 at.%,
  the single point at 1210 °C returns 100 % FCC, sandwiched between 100 % BCC at both 1200
  and 1220 °C, with no two-phase transition on either side. `solvus()` reports the first
  crossing together with a list of later excursions, so an artifact can neither shift the
  reported number nor be silently dropped.
- **Self-check.** At the measured nickel content the scan reproduces the ordering curve of
  the primary run (≈10 % ordered bcc at the bottom of the range, falling to zero by
  ≈875 °C), which is what `step_diagrams.py` and Fig. 9b already show.
