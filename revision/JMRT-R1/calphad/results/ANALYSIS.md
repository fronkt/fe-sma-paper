# Step-diagram results — what they say about the manuscript

Run 2026-08-05. 400–1400 °C in **10 °C steps**, 1571 equilibrium points across three
databases. Raw data `step_diagrams.csv`, log `step_diagrams.txt`, figures `step_*.png`.

*(First pass used 20 °C steps; re-run at 10 °C reproduces every round-temperature value
exactly, so the numbers below are grid-independent.)*

**A cleaner statement of the carbon effect than any single-temperature snapshot:** in
mpea-02b the single-phase α field opens at **~1150 °C without carbon and ~1340 °C with
it**. Carbon pushes the solution-treatment window ~190 °C higher — out of the practical
range for this process.

Three alloys per database: the benchmark as measured, the LLM-alloy as measured, and the
LLM-alloy with carbon removed and **every other element held fixed** — the in-silico
C-free variant R1#1 asks for and R3#9 challenges.

> Supersedes the earlier smoke test, which double-entered phases the databases reject by
> default. Those numbers should not be quoted.

---

## 1. The databases reproduce the benchmark — so their verdict on the test alloy counts

| | single-phase α window | B2 available on ageing |
|---|---|---|
| mc_fe (all six elements + P) | **950 → 1370 °C** | — (BCC_B2 not stabilised) |
| mpea-02b (no Si) | **1120 → 1400 °C** | **19–22 %, 400–1050 °C** |

Omori's 1200 °C solution treatment lands squarely inside a single-phase α field in both
databases, and mpea-02b independently predicts the ~20 % coherent B2 the benchmark's
superelasticity depends on. Nothing about the benchmark was fitted here — this is the
control coming out right.

## 2. Headline: carbon alone destroys the solution-treatment window. Confirmed three times.

Equilibrium at **1200 °C**, the actual processing temperature:

| | mpea-02b | PrecHiMn-04 | mc_fe |
|---|---|---|---|
| Benchmark | **100 % α** | *(no Ni)* | **100 % α** |
| LLM-alloy | 71 % α + 29 % γ | 65 % α + 36 % γ | 62 % α + 38 % γ |
| **LLM-alloy, C removed** | **100 % α** | **100 % α** | **100 % α** |

Three independent assessments, three different element sets — one carrying Si, one
carrying Ni, one carrying both plus P — agree without exception. Delete 0.45 at.% carbon
and the LLM composition solution-treats single-phase exactly like the benchmark.

This is the strongest result of the revision. It is the control experiment R1#1 asked for,
it answers R3#9's "why single out carbon over Ni" (Ni is held fixed here), and it converts
R2 Concl#4's *recommendation* to pre-screen thermodynamically into a *demonstration*.

**State the limit too:** carbon is decisive at the solution-treatment temperature, not
everywhere. At 800–900 °C the C-free alloy still holds 38–44 % γ in mc_fe. The honest
claim is that carbon closes the single-phase α window the processing route depends on,
while the lower Al and Ni of the base composition move the α/γ boundary independently.

## 3. "The LLM-alloy cannot form B2" is too strong — and the true statement is better

mpea-02b, ordered B2 fraction:

- **Benchmark:** ~19–22 %, flat from 400 °C to ~1050 °C.
- **LLM-alloy:** ~10 % at 400 °C, falling to **zero by ~850 °C**.

So the alloy does have a B2 field. It is roughly half the magnitude and closes ~200 °C
lower. Combined with §2, the mechanism sharpens into something a reviewer cannot easily
attack: **there is no temperature at which this composition can be solution-treated to
single-phase α and then aged into coherent B2.** The benchmark has both windows and they
overlap; the LLM-alloy has neither in a usable place.

This also defuses R3#8 (absence of a peak ≠ absence of phase) — we stop claiming zero.

## 4. D0₃ is not an *equilibrium* phase here — but it is really there

> **Revised 2026-08-05 after the E: drive came online.** An earlier version of this section
> said the manuscript's D0₃ assignment was unsupported. That was wrong and is withdrawn.
> Independent re-analysis of the raw SSRF patterns shows a reproducible D0₃ (111)
> superlattice reflection in the LLM-alloy and not in the benchmark — see
> `revision/JMRT-R1/xrd/ANALYSIS.md` §1.

PrecHiMn-04 is the only database here that models D0₃ (`BCC_4SL`, four sublattices), and its
ordered bcc comes back tagged disordered A2 at every temperature. At ~12 at.% Al the
composition sits well below the Fe₃Al D0₃ field (~25 at.% Al).

Two reasons not to lean on that result. First, **PrecHiMn-04 contains no Ni**, and Ni
strongly conditions B2/D0₃ ordering in Fe-Al — so this was never a strong test. Second, the
diffraction evidence is direct and the calculation is indirect.

The defensible statement, and a more interesting one than either extreme: **D0₃ forms in the
LLM-alloy as a metastable ordering product on cooling, not as an equilibrium phase.** That
is consistent with both the diffraction and the thermodynamics, and it fits the quench
picture in §5.

R1#2 asked whether the model accounted for D0₃. The answer: at equilibrium D0₃ is not
expected at this composition, yet it forms — which is exactly the kind of kinetic outcome a
composition-only screening step cannot anticipate.

## 5. ⚠️⚠️ The measured phase fractions run opposite to every calculation

- **Measured** (Rietveld, specimen quenched from 1200 °C / 1 min): **62 % γ-FCC, 34 % α-BCC**, 4 % D0₃
- **Calculated at 1200 °C:** **62–71 % α-BCC, 29–38 % γ-FCC** — all three databases
- **The manuscript's own §3.1** calls the α the *matrix* and the γ *blocky islands*

A 34 % matrix hosting 62 % islands is already odd on its face; it was flagged in the
comment triage as self-audit #2. CALPHAD now makes it pointed: the microstructural
description and the thermodynamics agree with each other, and both disagree with the
reported Rietveld fractions.

Two readings were on the table. **Reading (a) is now eliminated** — see
`revision/JMRT-R1/xrd/ANALYSIS.md` §4: the raw patterns independently show the LLM-alloy is
fcc-rich (fcc(111) at 100–124 % of bcc(110)) and the benchmark bcc-rich (23–34 %). The
manuscript has the majority phase right.

**~~(a) The Rietveld fractions are transposed.~~** Withdrawn 2026-08-05.

**(b) They are correct, and γ formed during the quench.** In this system γ is the
*martensite product*, so α → γ on cooling is not exotic. That would put M_s above room
temperature, and it is a **better explanation for the absence of superelasticity than the
one currently in the manuscript**: the transformation has already run to completion before
the specimen is ever loaded, so there is nothing left to induce. It is also exactly what
carbon raising γ-stability would predict.

Reading (b) is attractive and must not be asserted without evidence. It is testable: the
quenched material should show martensite morphology, the γ reflections should be broadened
or faulted, and a DSC scan would place M_s directly. Note also that mc_fe's *equilibrium*
at 700–1000 °C is ~62 % γ / 38 % α, numerically close to the measurement — record that as a
coincidence to check, not as support.

Either way this is the highest-priority item in the revision, and it promotes **D2
(reconnect the E: drive) from Tier 4 to blocking.**

## 6. κ-carbide: a clean answer to R3#2

Both PrecHiMn-04 and mc_fe carry κ-(Fe,Mn)₃AlC. It is predicted at **~2 %, and only below
~580 °C**.

So R3#2 is right that the composition sits in the Fe-Mn-Al-C lightweight-steel field, and
right that κ/B2/D0₃ are that field's characteristic phases — but this alloy carries
0.45 at.% C (≈0.1 wt.%), an order of magnitude below the 1–1.5 wt.% those steels use to
precipitate κ. **The composition lands in the lightweight-steel field at a carbon level too
low to collect that field's strengthening, while still high enough to lose the SMA field's
transformation.** It gets carbon's γ-stabilisation penalty without κ's benefit. That is a
substantive reply, not a concession.

---

## 7. Which database to trust on ordering — diffraction settles it

The three databases disagree about B2, and the disagreement is resolvable against
measurement rather than by preference:

| | B2 predicted for the benchmark | B2 measured (this work) |
|---|---|---|
| **mpea-02b** | **~20 %, flat 400–1050 °C** | — |
| mc_fe | **none at any temperature** — `BCC_B2` is never stable in 303 equilibria | — |
| PrecHiMn-04 | *(no Ni — cannot be run)* | — |
| **SSRF diffraction** | — | **B2 (100) at 3.8–7.2 % of the strongest reflection** |

The benchmark demonstrably contains B2 — that is the whole basis of its superelasticity,
and `revision/JMRT-R1/xrd/ANALYSIS.md` §1 measures it directly. **mpea-02b reproduces
that; mc_fe does not.** So mpea-02b is the database to quote for anything involving
ordering, and mc_fe should be used only for the α/γ balance and for carrying Si and P.

State this in the paper as a strength rather than hiding it: the database that was
independently validated against the benchmark's known B2 is the one whose predictions for
the LLM-alloy are reported.

Note also that `BCC_B2` in mc_fe is an independent (non-partitioned) phase, whereas
mpea-02b models B2 as an ordered partition of A2. The partitioned treatment is the
physically correct one for a continuous order–disorder transition, which is a second
reason to prefer mpea-02b here.

## Numerical artifacts — what was fixed, and what remains

### Fixed

- **mc_fe / LLM-alloy, spurious 100 % γ spikes at 850 and 980 °C, plus outright failures at
  840, 890, 990 and 1190 °C.** Cause: 7 components and a difficult γ/α miscibility region
  under-sampled at `pdens = 500`. Re-computed over 780–1280 °C at `pdens = 2000`
  (`refine_mc_fe.py`, spliced by `splice_refined.py`, which prints every value it replaces).
  The result is a smooth γ 62.5 % → 57.2 % ramp across 780–1000 °C with no spikes.
  Two points that the denser grid then failed at (780, 800 °C) were retried across four
  alternative densities (`retry_failures.py`); **all four converged and all four agreed**
  on 62.5 % γ / 37.5 % α, matching both neighbours and the original coarse run. Densities
  used per point are logged in `retry_log.txt`.
- **mpea-02b / benchmark, apparent B2 "spike" to 68 % near 1080 °C.** This was not a
  numerical artifact but a *plotting* one: B2_BCC is a partitioned phase, and drawing its
  ordered and disordered composition sets as separate curves made a continuous
  order–disorder transition look like one phase vanishing and another appearing. The total
  bcc fraction is smooth through it. Now plotted as one bcc curve with the ordered portion
  shaded beneath.
- **Lines beginning and ending in mid-air.** Absent phases were being omitted rather than
  plotted as zero, so a phase entering at a boundary started at whatever value the first
  grid point inside its field happened to take. Now zero-filled.

### Remaining — disclose these, do not quietly clean them

- **mc_fe / benchmark:** a spurious 0.1–0.2 % `LIQUID` composition set persists 500–900 °C.
  It failed to vanish and does not perturb the majority phases. Not refined, because the
  benchmark result (single-phase α, 950–1370 °C) is unaffected.
- **mc_fe / LLM-alloy: 400–430 °C does not converge** at any density tried. Below the
  processing range and outside every claim made here; drawn as a grey band.
- **PrecHiMn-04 below ~600 °C is unusable here** — it returns 83–100 % β-Mn, which is an
  extrapolation artifact: the database is assessed for high-Mn steels at far lower Al than
  12 at.%. Its value in this work is the D0₃ test, the κ test, and the high-temperature α
  window. Say so rather than showing the low-T region.
- pycalphad warns that the partitioned-B2 magnetic contribution is not correctly
  substituted into the disordered part (pycalphad PR #311). Cross-check against mc_fe,
  which models B2 independently.
- Equilibrium is not the as-quenched state, and 1 min at 1200 °C may not reach it. This
  matters directly for §5 above.

## Suggested figure

`step_mpea-02b.png` is the paper figure: three panels, left to right — benchmark, LLM-alloy,
LLM-alloy without carbon. The argument reads off it in one glance. The benchmark's flat
~20 % B2 band under a single-phase α roof, the LLM-alloy with neither, and the C-free
variant with the roof restored.

Use mc_fe as the supporting/cross-check figure since it carries all six elements plus P,
and PrecHiMn-04 only for the D0₃ and κ statements.
