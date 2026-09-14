# Step-diagram results — what they say about the manuscript

**Run 2026-09-14, liquid phase included and grid-arbitrated.** 400–1400 °C in 10 °C steps,
three databases, three alloys each. Raw data `step_diagrams.csv`, logs `step_diagrams.txt`
(mpea-02b and PrecHiMn-04 re-run) and the archived mc_fe log, figures `step_*.png`, paper
figure `../../../../figures/Figure_9.png`. **Supersedes the 2026-08-05 run**, archived in
`../results-archive-2026-09-14-noliquid/`.

> **Correction, 2026-09-14.** The August scripts requested the liquid phase as `'LIQUID:L'`
> for mpea-02b and PrecHiMn-04; pycalphad names it `'LIQUID'`, `run()` filtered the unknown
> name out silently, and the log's `absent : LIQUID:L` line went unread for five weeks. Both
> databases were therefore computed for an alloy that could not melt. The consequences in the
> earlier version of this note and in manuscript Revision 1: the "≈1340 °C" (mpea-02b) and
> "≈1390 °C" (PrecHiMn-04) α solvi of the LLM-alloy, "mpea-02b returns no liquid at all below
> 1400 °C", the "databases disagree on the solidus" paragraph, the benchmark's "1120 → 1400 °C"
> window, and the Ni-scan and A2-window solvi. **Unchanged:** every 1200 °C phase fraction
> (Table 3), every ordering result below ≈1100 °C, the κ / M₂₃C₆ / D0₃ statements, and the
> whole of mc_fe, which used the correct name. `run()` now refuses to proceed when LIQUID,
> the bcc phase or the fcc phase is missing from a database.
>
> **Second correction found while fixing the first.** Near the solidus of the LLM-alloy the
> converged state depends on the density of the composition grid the global minimiser starts
> from, and the denser grid is *not* reliably the lower-energy one (`gm_comparison.txt`,
> `prechimn_dense_check.txt`). For the affected bands the state of lowest molar Gibbs energy
> across a ladder of densities was kept (`../refine_by_gm.py`; every candidate's GM is in
> `gm_refined_log.txt` and `gm_refined_log-only.txt`). Details in the artifacts section.

---

## 1. Headline, corrected: the carbon-bearing alloy melts before it is ever single-phase α — in all three databases

| LLM-alloy | mpea-02b | PrecHiMn-04 | mc_fe |
|---|---|---|---|
| 1200 °C | 71.1 α + 28.9 γ | 64.5 α + 35.5 γ | 61.9 α + 38.1 γ |
| last solid temperature, constitution | 1290 °C: 92.6 α + 7.4 γ | ≥1250 °C: 75.0 α + 25.0 γ | 1230 °C: 66.0 α + 34.0 γ |
| first liquid | 1300 °C (3.7 %) → α + L | 1300 °C (19 %) | 1240 °C (9.6 %) → α + γ + L |
| solid-state single-phase α field | **none** | **none** | **none** |
| solidus (0.5 % liquid) | ≈1295 °C | ≈1295 °C | ≈1240 °C |

The three assessments differ on where melting starts, by ≈55 °C, and agree that γ is still
present when it does. The manuscript's claim is therefore stronger and simpler than in
Revision 1: not "the α field lies above the annealing limit" but "there is no single-phase α
field in the solid state at all." Nothing rests on a solidus value.

**The carbon-free control (every other element fixed):**

| C removed | mpea-02b | PrecHiMn-04 | mc_fe |
|---|---|---|---|
| single-phase α field | 1150–1370 °C | 1160–1290 °C | 1130–1240 °C |
| solidus | ≈1375 °C | ≈1295 °C | ≈1245 °C |
| 1200 °C | 100 α | 100 α | 100 α |

A window 130–220 °C wide where the carbon-bearing alloy has none. The 1150 / 1160 / 1130 °C
opening temperatures are exactly what the August run gave — the liquid phase plays no part
there.

**The benchmark (the control that validates the databases):**

| benchmark | mpea-02b | mc_fe |
|---|---|---|
| single-phase α field | 1140–1320 °C | 950–1360 °C |
| solidus | ≈1325 °C | ≈1375 °C |
| B2 on ageing | 19–22 %, 400–1050 °C | none (BCC_B2 never stable) |

Omori's 1200 °C solution treatment lands inside a single-phase α field in both, with more
than 100 °C to spare on either side, and mpea-02b independently predicts the ≈20 % coherent
B2 the benchmark's superelasticity depends on. Nothing about the benchmark was fitted.

These numbers are in manuscript **Table 4** (new in Round 2); Table 3 (1200 °C) is unchanged.

## 2. Carbon alone decides whether the field exists. Confirmed three times.

Delete 0.45 at.% carbon and the LLM composition solution-treats single-phase exactly like the
benchmark, in three independent assessments with three different element sets. This is the
control experiment R1#1 asked for in Round 1, it answers R3#9's "why single out carbon over
Ni" (Ni held fixed here; see `NI-SENSITIVITY.md` for Ni varied), and it converts
R2 Concl#4's *recommendation* to pre-screen thermodynamically into a *demonstration*.

**State the limit too:** carbon is decisive at the solution-treatment temperature, not
everywhere. At 800–900 °C the C-free alloy still holds 38–44 % γ in mc_fe and is fully
austenitic in mpea-02b. The honest claim is that carbon removes the single-phase α window
the processing route depends on, while the lower Al and Ni of the base composition move the
α/γ boundary independently.

## 3. "The LLM-alloy cannot form B2" is too strong — and the true statement is better

mpea-02b, ordered B2 fraction (unchanged from August):

- **Benchmark:** ~19–22 %, flat from 400 °C to ~1050 °C.
- **LLM-alloy:** ~10 % at 400 °C, falling to **zero by ~850 °C**.

The alloy does have a B2 field, roughly half the magnitude and closing ~200 °C lower.
Combined with §1: **there is no temperature at which this composition can be solution-treated
to single-phase α and then aged into coherent B2.** The benchmark has both windows and they
overlap; the LLM-alloy has neither in a usable place.

## 4. D0₃ is not an *equilibrium* phase here — but it is really there

PrecHiMn-04 is the only database here that models D0₃ (`BCC_4SL`), and its ordered bcc comes
back tagged disordered A2 at every temperature. At ~12 at.% Al the composition sits well below
the Fe₃Al D0₃ field. The diffraction evidence for D0₃ is direct
(`revision/JMRT-R1/xrd/ANALYSIS.md` §1) and the calculation is indirect; the defensible
statement is that **D0₃ forms in the LLM-alloy as a metastable ordering product on cooling,
not as an equilibrium phase** — exactly the kind of kinetic outcome a composition-only
screening step cannot anticipate.

## 5. The measured phase fractions run opposite to every calculation — still open, and now R3#8

Measured (Rietveld, quenched from 1200 °C / 1 min): **62 % γ, 34 % α**, 4 % D0₃.
Calculated at 1200 °C: **62–71 % α, 29–38 % γ**, all three databases, confirmed as the
lowest-energy states (`gm_comparison.txt`). The two agree that the alloy is duplex and
disagree on which phase dominates. Reading (b) of the August note — γ formed during the
quench, Ms above room temperature — is what Reviewer 3 (Round 2, point 8) asks us to measure
rather than assert. Round-2 disposition: demote it to one of two possibilities, state the
EDS-partitioning argument against a martensitic origin of the excess γ, name DSC as the test.

## 6. κ-carbide: a clean answer to R3#2 (Round 1)

Both PrecHiMn-04 and mc_fe carry κ-(Fe,Mn)₃AlC. It is predicted at **~2 %, and only below
~580 °C**. The composition lands in the lightweight-steel field at a carbon level too low to
collect that field's strengthening, while still high enough to lose the SMA field's
transformation. Unchanged from August.

## 7. Which database to trust on ordering — diffraction settles it

The benchmark demonstrably contains B2 (SSRF: B2 (100) at 3.8–7.2 % of the strongest
reflection). mpea-02b reproduces that; mc_fe never stabilises `BCC_B2`. So mpea-02b is the
database to quote for anything involving ordering, and mc_fe is used for the α/γ balance and
for carrying Si and P. Unchanged from August; the paper figure is mpea-02b for this reason.

## Numerical artifacts — what was fixed, and what remains

### Fixed on 2026-09-14

- **The liquid phase** (see the correction box). Verified present in both re-run phase
  lists (`step_diagrams.txt` lines 8 and 57 now list `LIQUID`; no `absent` line).
- **Grid-basin dependence near the solidus of the LLM-alloy.** `compare_gm.py`: at
  1150–1300 °C in mpea-02b and at 1200 °C in PrecHiMn-04 the pdens-500 duplex (or α + L)
  state has a lower GM than the 100 % γ state that pdens 2000–3000 converge to — e.g.
  mpea-02b 1290 °C: −109 378.5 (α + γ) vs −109 144.3 J/mol (γ); PrecHiMn-04 1200 °C:
  −100 985.8 vs −100 898.6 J/mol. `recheck_prechimn_dense.py`: a 12 000-point two-phase grid
  still lands in the γ basin at 1200 °C, so density is not the cure. `refine_by_gm.py`
  therefore keeps the lowest-GM state across a ladder of densities per temperature and splices
  it into the CSV. Pass 1 (500/1000/2000/3000) replaced the mpea-02b 1330–1340 °C rows
  (γ + L → α + L, the continuous melting sequence). Pass 2 (13 grids, 300–3000) found the
  PrecHiMn-04 duplex at 1210–1250 °C on the 1500-point grid alone, with lower GM than the
  γ-only state every other grid returned (1210 °C: −101 881.6 vs −101 786.9 J/mol); α rises
  64.5 → 75.0 % across that band. Pass 3 (10 further grids, 1300–4000, chosen around the
  one that had worked) changed nothing: across the 23 grids tried, no duplex with lower GM
  than the γ-only state was found at 1260–1290 °C, so those rows stand as γ-only in the CSV
  and in `step_PrecHiMn-04.png`.
- **mc_fe / LLM-alloy 780–1280 °C** at pdens 2000 (August refinement, unchanged and kept).
- **Plotting** of partitioned B2 and zero-filling of absent phases (August, unchanged).

### Remaining — disclose, do not quietly clean

- **PrecHiMn-04 / LLM-alloy, 1260–1290 °C, is recorded as 100 % γ and is not believed.**
  A drop from 75.0 % α at 1250 °C to zero at 1260 °C is not a continuous two-phase
  equilibrium; it is the same missed-minimum signature that pass 2 resolved at 1210–1250 °C,
  and 23 grids did not resolve it here. The true diagram in this database is almost
  certainly α + γ up to the solidus with α still rising, as in the other two databases. The
  manuscript therefore quotes PrecHiMn-04 only as "two-phase at least to 1250 °C, melting
  from ≈1295 °C", which is true on either reading, and Table 4's "none" for its solid-state
  α field holds on either reading too (a γ-only band is not an α field).
- **The Ni-scan and A2-window runs were not grid-arbitrated** (pdens 500 only, the density
  that returned the lower-energy state in every arbitrated case); their control points
  reproduce the arbitrated primary run.
- **mc_fe / benchmark:** a spurious 0.1–0.2 % `LIQUID` composition set persists 500–900 °C;
  below the 0.5 % solidus threshold and it does not perturb the majority phases.
- **mc_fe / LLM-alloy: 400–430 °C does not converge**; drawn as a grey band.
- **PrecHiMn-04 below ~600 °C is unusable here** (83–100 % β-Mn, an extrapolation artifact).
- pycalphad warns that the partitioned-B2 magnetic contribution is not correctly substituted
  into the disordered part (pycalphad PR #311). Cross-checked against mc_fe.
- Equilibrium is not the as-quenched state (§5).

## Suggested figure

`../../../../figures/Figure_9.png` (mpea-02b; benchmark, LLM-alloy, LLM-alloy without carbon)
now carries the liquid curve. The argument reads off it in one glance: the benchmark's flat
~20 % B2 band under a single-phase α roof that runs to the solidus; the LLM-alloy's γ
persisting until the liquid takes it; the C-free variant with the roof restored.
