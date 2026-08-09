# Was the failure caused by deviating from the agent's range? — no

**Script:** `../agent_window.py` · **Data:** `agent_window.csv`, `agent_window.txt`
**Run:** 2026-08-09 · **Context:** `../../llm-provenance/LLM-PROVENANCE.md`

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
route (wt.% → at.% → renormalise). It must reproduce what the earlier runs already published, and it
does, exactly:

| | this script | published (Table 3 / `ANALYSIS.md`) |
|---|---|---|
| mc_fe, 1200 °C | **62.1 α / 37.9 γ** | 61.9 α / 38.1 γ |
| mc_fe, C-free solvus | **1130 °C** | 1130 °C |
| mc_fe, liquid onset | **1240 °C** | ≈1240 °C |

Nothing downstream would be interpretable without that check passing.

## Result 1 — no composition in the window opens the field (mpea-02b)

| point (wt.%) | α solvus | phases at 1200 °C |
|---|---|---|
| as made — Mn 32.3, Al 6.4, Ni 4.6, C 0.1 | 1330 °C | 76.0 α + 24.0 γ |
| **A2 midpoint** — Mn 25, Al 10, Ni 4.5, C 0.2 | **1380 °C** | 86.7 α + 13.3 γ |
| **A2 ferritic corner** — Mn 20, Al 12, Ni 6, C 0.1 | **1230–1240 °C** | 98.2 α + 1.8 γ, *ordered* |
| **A2 austenitic corner** — Mn 30, Al 8, Ni 3, C 0.3 | **none ≤1400 °C** | 64.0 α + 36.0 γ |

Aluminium alone, everything else at measured values:

| Al wt.% | 6.4 | 7.1 | 7.8 | 8.5 | 9.2 | 9.9 | 10.6 | 11.3 | 12.0 |
|---|---|---|---|---|---|---|---|---|---|
| α solvus (°C) | 1330 | 1320 | 1310 | 1300 | 1290 | 1280 | 1280 | 1270 | 1270 |
| α at 1200 °C (%) | 76.0 | 84.2 | 89.0 | 91.9 | 93.8 | 95.2 | 96.1 | 96.8 | 97.3 |

Four things follow.

1. **The midpoint of the agent's own window is *worse* than what was made** — 1380 °C against
   1330 °C — because taking the middle of the range takes the middle of its **carbon** range with
   it, 0.2 wt.% instead of 0.1. Carbon dominates, exactly as Sec. 4.2 argues.
2. **The best corner the window allows still does not reach.** Its solvus is bracketed 1230–1240 °C
   (1220 °C is 99.3 % α + 0.7 % γ; 1230 °C did not converge; 1240 °C is single-phase), above the
   1200 °C ceiling that §2.2 sets from oxidation and furnace contamination. Worse for the design,
   the bcc there is **ordered**, so that corner delivers a B2 matrix rather than the disordered α
   parent with coherent B2 precipitates that the route requires.
3. **Aluminium moves the phase balance a lot and the solvus very little.** Going the full distance
   to the window's ceiling adds 21 points of α at 1200 °C but buys only 60 °C of solvus, and never
   crosses the annealing limit. The Al deviation is real and it does push toward austenite — it is
   simply not what closed the window.
4. **The carbon that closes it was the agent's own specification, and the melt took the minimum.**
   A2 permits 0.1–0.3 wt.% C; the heat was made at 0.1. Every other carbon content in the window is
   worse. The paper's central claim therefore does not rest on the Mn/Al deviation at all.

## Result 2 — mc_fe agrees on the conclusion by a different route

All six elements, `pdens=2000`, named points only:

| point | Si wt.% | liquid onset | α solvus | 1200 °C |
|---|---|---|---|---|
| measured *(control)* | 1.11 | 1240 °C | 1250 °C | 62.1 α + 37.9 γ |
| as made | 2.20 | **1180 °C** | 1200 °C | 72.1 α + **27.9 liquid** |
| A2 midpoint | 2.50 | **1100 °C** | 1140 °C | 61.4 α + **38.6 liquid** |
| A2 ferritic corner | 4.00 | **1010 °C** | 1030 °C | 43.4 α + **56.6 liquid** |
| A2 austenitic corner | 1.00 | 1230 °C | none ≤1400 °C | **100 γ** |

**No point in the window is single-phase α at 1200 °C here either** — three are partly molten and
the fourth is fully austenitic. That is the same conclusion mpea-02b reaches, by a different
mechanism, which is the useful kind of agreement.

**The disagreement is on the solidus, and it is large.** mpea-02b returns no liquid at all below
1400 °C for any of these compositions; mc_fe puts 28–57 % liquid at 1200 °C for three of them. The
same disagreement is already disclosed in §3.4 for the measured composition and is not resolved
here.

**A side result worth recording.** In mc_fe the liquid onset tracks silicon almost monotonically —
1240 °C at 1.11 wt.% Si, 1180 at 2.20, 1100 at 2.50, 1010 at 4.00 — with the other elements varying
much less between those points. Taken at face value it says the alloy would have been partly molten
at its own solution-treatment temperature had silicon come in at the intended 2.2 wt.% instead of
the 1.11 wt.% actually recovered; the shortfall that §2.1 reports as a melting loss would then be
the thing that made the alloy processable.

That is a striking claim and it should be held loosely, for three reasons: it rests on one database;
the other database contradicts it outright; and mc_fe's solidus already looks low against the
processing record, since wire was annealed at 1200 °C for up to 40 min and at 1250 °C for 5 and
20 min and was still testable afterwards. The one piece of evidence pointing the other way is that
elongation collapses in exactly that range — 23.9 % after 1200 °C, 12.5 % after 1250 °C/5 min,
6.3 % after 1250 °C/20 min — which is what incipient grain-boundary liquation would do, though
§2.2 attributes it to oxidation and furnace contamination. Not resolvable from the present data;
recorded so it is not lost.

## Numerical honesty

- **One non-converged point on the load-bearing number.** mpea-02b, C_measured, A2 ferritic corner,
  1230 °C. The solvus is therefore reported as the bracket 1230–1240 °C rather than as a value.
  It does not affect the conclusion, which needs only that it lies above 1200 °C, and 1220 °C is
  resolved and is not single-phase.
- **mc_fe non-convergence is extensive at high temperature** — most points above ≈1350 °C, and
  1280–1400 °C for the ferritic corner. All of it lies well above the melting onset, where the
  answer is already established, so it does not touch any reported quantity. It is why mc_fe
  α-solvus values in the table above should be read as "first temperature at which bcc is the only
  *solid*", not as a solid-state solvus.
- **mpea-02b carries no silicon**, which is folded into iron. Weakest at the ferritic corner, where
  Si reaches 6.8 at.%. This is the main reason the mc_fe cross-check was run at all.
- **The A2 corners are not equally likely compositions.** They are the extremes of a stated range,
  used to bracket it. No claim is made that anyone would have melted them.
