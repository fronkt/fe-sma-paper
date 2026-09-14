# Was the failure caused by deviating from the agent's range? — no

**Script:** `../agent_window.py` · **Data:** `agent_window.csv`, `agent_window.txt`
**Run:** 2026-09-14, liquid phase included. **Supersedes** the 2026-08-09 run, archived in
`../results-archive-2026-09-14-noliquid/`. **Context:** `../../llm-provenance/LLM-PROVENANCE.md`

> **Correction, 2026-09-14.** The 2026-08-09 run requested the liquid phase as `'LIQUID:L'`,
> which pycalphad does not recognise, and dropped it silently; every mpea-02b "solvus" in
> the earlier version of this note (1330 °C as made, 1380 °C at the midpoint, 1230–1240 °C
> at the ferritic corner, "none ≤1400 °C" at the austenitic corner, and the whole aluminium
> row) was the temperature at which the last γ dissolved in an alloy that could not melt.
> `solvus()` now reports a *solid-state* single-phase bcc field (no γ, no liquid) and the
> solidus separately. The mc_fe rows used the correct phase name in August and are unchanged.

The recovered design report proposes, as Hypothesis A2, the range the alloy was drawn from:

> Fe (bal.), **Mn 20–30, Al 8–12, Si 1–4, Ni 3–6**, and either B 0.005–0.05 or **C 0.1–0.3**, wt.%

The alloy melted — Fe-32.3Mn-**6.4Al**-4.6Ni-2.2Si-0.1C wt.% — is inside that range in Si, Ni and C
and **outside it in Mn (above) and Al (well below)**. Aluminium is the strongest ferrite stabiliser
present, so the deviation points toward austenite, which is the direction of the observed failure.
Until that is tested, the paper cannot distinguish *"the proposed composition was unsound"* from
*"the composition we made was not the proposed one."*

## Design

Two series against the 1200 °C solution treatment, each run with carbon at the measured level and
again with carbon removed:

| series | what it isolates |
|---|---|
| `Al_scan` | Al alone, stepped 6.4 → 12.0 wt.% from the as-made composition, Fe balancing |
| `A2_points` | compositions genuinely *inside* the window: its midpoint and its two extreme corners |

Corners are chosen on ferrite-forming tendency rather than arbitrarily — the ferritic corner takes
Al and Ni high with Mn and C low, the austenitic corner the reverse — so together they bracket
everything the window permits.

**Control.** The measured composition is included as a fifth point and reached by this script's own
route (wt.% → at.% → renormalise). It must reproduce what the primary run gives, and it does:

| | this script | primary run (`step_diagrams.py`, Table 3) |
|---|---|---|
| mpea-02b, 1200 °C | **71.0 α / 29.0 γ** | 71.1 α / 28.9 γ |
| mpea-02b, solid-state α solvus / solidus | **none / 1300 °C** | none / ≈1295 °C |
| mpea-02b, C-free solvus | **1150 °C** | 1150 °C |
| mc_fe, 1200 °C | **62.1 α / 37.9 γ** | 61.9 α / 38.1 γ |
| mc_fe, liquid onset | **1240 °C** | ≈1240 °C |

Nothing downstream would be interpretable without that check passing.

## Result 1 — no composition in the window has a solid-state single-phase α field (mpea-02b)

| point (wt.%) | solid-state α solvus | solidus | phases at 1200 °C |
|---|---|---|---|
| as made — Mn 32.3, Al 6.4, Ni 4.6, C 0.1 | **none** | 1300 °C | 76.0 α + 24.0 γ |
| **A2 midpoint** — Mn 25, Al 10, Ni 4.5, C 0.2 | **none** | 1290 °C | 86.7 α + 13.3 γ |
| **A2 ferritic corner** — Mn 20, Al 12, Ni 6, C 0.1 | 1240 °C, *and the bcc is ordered B2* | 1330 °C | 98.2 **ordered** bcc + 1.8 γ |
| **A2 austenitic corner** — Mn 30, Al 8, Ni 3, C 0.3 | **none** | 1320 °C | 64.0 α + 36.0 γ |

Aluminium alone, everything else at measured values:

| Al wt.% | 6.4 | 7.1 | 7.8 | 8.5 | 9.2 | 9.9 | 10.6 | 11.3 | 12.0 |
|---|---|---|---|---|---|---|---|---|---|
| solid-state α solvus (°C) | none | none | none | none | none | none | none | 1270* | none |
| solidus (°C) | 1300 | 1290 | 1290 | 1300 | 1290 | 1280 | 1280 | 1280 | 1270 |
| α at 1200 °C (%) | 76.0 | 84.2 | 89.0 | 91.9 | 93.8 | 95.2 | 96.1 | 96.8 | 97.3 |

\* a single 10 °C step between the last γ and the first liquid — grid resolution, not a window.

Four things follow.

1. **The midpoint of the agent's own window is no better than what was made.** It still has no
   solid-state single-phase α field, because taking the middle of the range takes the middle of its
   **carbon** range with it, 0.2 wt.% instead of 0.1. Carbon dominates, exactly as Sec. 4.2 argues.
2. **The best corner the window allows does reach a single-phase field — 40 °C above the annealing
   ceiling, and of the wrong kind.** At Mn 20, Al 12, Ni 6, C 0.1 wt.% the bcc becomes the only
   phase at 1240 °C, but it is **ordered B2** there, so that corner delivers a B2 matrix rather
   than the disordered α parent with coherent B2 precipitates that the route requires.
3. **Aluminium moves the phase balance a lot and never opens the field.** Going the full distance
   to the window's ceiling adds 21 points of α at 1200 °C, but the alloy still melts (1270–1300 °C)
   with γ present. The Al deviation is real and it does push toward austenite — it is simply not
   what closed the window.
4. **The carbon that closes it was the agent's own specification, and the melt took the minimum.**
   A2 permits 0.1–0.3 wt.% C; the heat was made at 0.1. Every other carbon content in the window
   is worse. The paper's central claim therefore does not rest on the Mn/Al deviation at all.

With carbon removed, the same points all open a single-phase α field far below the solidus:
1140 °C as made, 1000–1010 °C at the three A2 points (the bottom of the scanned window), and the
aluminium row runs 1140 → 1000 °C; the solidus sits at ≈1380 °C throughout.

## Result 2 — mc_fe agrees on the conclusion by a different route

All six elements, `pdens=2000`, named points only (unchanged from August):

| point | Si wt.% | liquid onset | solid-state α solvus | 1200 °C |
|---|---|---|---|---|
| measured *(control)* | 1.11 | 1240 °C | none | 62.1 α + 37.9 γ |
| as made | 2.20 | **1180 °C** | none | 72.1 α + **27.9 liquid** |
| A2 midpoint | 2.50 | **1110 °C** | none | 61.4 α + **38.6 liquid** |
| A2 ferritic corner | 4.00 | **1020 °C** | none | 43.4 α + **56.6 liquid** |
| A2 austenitic corner | 1.00 | 1240 °C | none | **100 γ** |

**No point in the window is single-phase α at 1200 °C here either** — three are partly molten and
the fourth is fully austenitic. That is the same conclusion mpea-02b reaches, by a different
mechanism, which is the useful kind of agreement.

**The databases still differ on the solidus of the silicon-rich window points, by up to 300 °C.**
mpea-02b (no silicon; folded into iron) melts them at 1290–1330 °C; mc_fe puts 28–57 % liquid at
1200 °C for three of them, its liquid onset tracking silicon almost monotonically — 1240 °C at
1.11 wt.% Si, 1180 at 2.20, 1110 at 2.50, 1020 at 4.00. For the *measured* composition, where
silicon is 1.11 wt.%, the two agree to within ≈55 °C (1240 vs ≈1295 °C). The difference for the
window points is reported, not reconciled; nothing in the conclusion depends on which is right.

**A side result worth recording.** Taken at face value the mc_fe silicon trend says the alloy would
have been partly molten at its own solution-treatment temperature had silicon come in at the
intended 2.2 wt.% instead of the 1.11 wt.% actually recovered; the shortfall that §2.1 reports as a
melting loss would then be the thing that made the alloy processable. That is a striking claim and
it should be held loosely: it rests on one database, and mc_fe's solidus already looks low against
the processing record, since wire was annealed at 1200 °C for up to 40 min and at 1250 °C for 5 and
20 min and was still testable afterwards. The one piece of evidence pointing the other way is that
elongation collapses in exactly that range — 23.9 % after 1200 °C, 12.5 % after 1250 °C/5 min,
6.3 % after 1250 °C/20 min — which is what incipient grain-boundary liquation would do, though
§2.2 attributes it to oxidation and furnace contamination. Not resolvable from the present data;
recorded so it is not lost.

## Numerical honesty

- **The ferritic-corner solvus is now a value, not a bracket.** In August 1230 °C failed to
  converge; with the liquid phase present it converges (1230 °C is still not single-phase; 1240 °C
  is). Unchanged in what matters: it lies above the 1200 °C ceiling.
- **One isolated excursion** in the C-free aluminium row (Al 7.8 wt.%: 1290 °C returns 100 % γ
  between single-phase bcc on both sides) is a solver flip of the kind `solvus()` is built to
  report rather than absorb; the solvus quoted is the first crossing.
- **Grid dependence near the solidus is real in this system**; the primary step diagrams were
  arbitrated by Gibbs energy across several grid densities (`../compare_gm.py`,
  `../refine_by_gm.py`). The window scan was run at pdens 500 only, the density that returned the
  lower-energy state in every arbitrated case, and its control point reproduces the arbitrated
  primary run.
- **mc_fe non-convergence is extensive at high temperature** — most points above ≈1350 °C, and
  1280–1400 °C for the ferritic corner. All of it lies well above the melting onset, where the
  answer is already established, so it does not touch any reported quantity.
- **mpea-02b carries no silicon**, which is folded into iron. Weakest at the ferritic corner, where
  Si reaches 6.8 at.%. This is the main reason the mc_fe cross-check was run at all.
- **The A2 corners are not equally likely compositions.** They are the extremes of a stated range,
  used to bracket it. No claim is made that anyone would have melted them.
