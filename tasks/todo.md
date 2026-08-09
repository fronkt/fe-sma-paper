# JMRT major revision — JMRT-D-26-06169

Reviews received 2026-07-27 (R1), 2026-07-28 (R3), 2026-07-31 (R2). 45 comments total.
Full analysis: `revision/JMRT-R1/comment-triage.md`.
Previous phase-ordered draft of this plan: `tasks/todo-archive-2026-08-05-jmrt-phase-ordered.md`.

**Ordered easiest → hardest.** Tiers 0–1 need nothing but a text editor. Tier 2 needs
files already in this repo. Tier 3 is now unblocked (see the CALPHAD note below).
Tiers 4–5 need other people.

**Status (2026-08-08, evening): Tier 0 executed in `manuscript.md`. Tiers 1–6 open.**

> ✅ **AUTHOR LIST — RESOLVED 2026-08-08.** `front_JMRT.md` now exists with all four
> authors (Frank Y. Cai¹\*, S. Cai², **X. Wang³**, J. Yan⁴). Two things inside it still
> need a human: the **revision title** (changed to the R2-Title-compliant one, needs
> co-author sign-off) and the **duplicate affiliations 1 and 3** (identical Purdue text,
> left exactly as submitted because renumbering the author block is a co-author call).
>
> Everything else diffs clean against the submitted PDF: §2.5, §3.1, §3.2, §3.3 and the
> §4 base text were word-for-word identical. The only body-text differences were the
> intentional CALPHAD additions and the two §4.1 deletions logged below.

> 🔴 **RIETVELD FILES ARRIVED 2026-08-08 — and they change §2.5/§3.3.** Full analysis in
> `revision/JMRT-R1/xrd/RIETVELD-FILES-ANALYSIS.md`. Headlines:
>
> 1. **62/34/4 belongs to sample 5, the undeformed specimen** — §3.3's attribution is
>    correct and that question is closed.
> 2. **But those fractions were never refined.** In `sample-5-2.prn.lst` all three phase
>    fractions are `not refinable`, all scale factors pinned at 1.0, and the twelve refined
>    parameters are instrument geometry plus Popa crystallite size. The values are exactly
>    0.62 / 0.34 / 0.04 in a file that reports elsewhere to eight significant figures.
>    **There are no ESDs on the published fractions because nothing was refined.**
> 3. **Where fractions *were* refined (zip1, sample 6), D0₃ came out 1.56(11) %, not 4 %.**
>    α landed on 34.68(14) %, almost exactly the published value. The 4 % is not robust.
> 4. Lattice parameters are fixed in every run; `goodness_of_fit_all` ≈0.085 is not a
>    usable χ² and must not be quoted.
> 5. Good news: it really is MAUD 2.33, and **E-WIMV ODF texture refinement is present in
>    all three runs across all 73 spectra** — the texture concern is answered.
>
> **Frank chose zip2 as canonical.** Consequence: neither panel of the new Fig. 5 has
> refined fractions, so the before/after supports only the *qualitative* claim.
> **The one blocking question is where sample 5's 0.62/0.34/0.04 came from.**

> **CALPHAD blocker D1 is CLEARED (2026-08-05).** Thermo-Calc is no longer required.
> `pycalphad` 0.11.2 is installed and verified on this machine, and three open TDB
> databases cover the system. A smoke test already reproduces the benchmark alloy's
> known single-phase-α solution treatment at 1200 °C and shows that removing carbon
> from the LLM composition restores exactly that behaviour. See
> `revision/JMRT-R1/calphad/README.md` for the setup and the first results.

---

## Tier 0 — free fixes (minutes each, zero dependencies)

Pure text edits. Nothing here can be wrong for reasons outside the manuscript.

**All executed 2026-08-08 unless marked otherwise.** Verified by grep against `manuscript.md`.

- [x] **Rename alloys throughout** → "LLM-alloy" / "benchmark alloy"; "AI-guided" and
      "AI-assisted" kept for the general field. 52 occurrences renamed, 0 stale.
      *(closes R1#5, R2 Title#1)*
- [x] **34 % / 37 % α inconsistency** — already correct in the repo (§4.1 reads ≈34 %).
      The **submitted PDF** carries the ≈37 % error, so this must still be called out in
      the response letter as a correction. *(self-audit #1)*
- [x] Resolve the **matrix / island contradiction** — §3.1 now declines to name either
      constituent as the matrix, and says why (a 2-D section through an interpenetrating
      duplex structure cannot establish 3-D continuity). Consequential edits made in §4.1 ¶2
      and ¶3, where the matrix assignment was load-bearing. *(self-audit #2, R1#3)*
- [x] **Element ordering** — abstract now reads Fe-Mn-Al-Ni-Si-C, matching the title.
- [x] Delete the **"composition is the sole variable"** sentence in §1, replaced with the
      weaker true statement plus a forward reference to §4.1 *(R3#1)*
- [x] Fix **"very close to nominal"** for Si — §2.1 now reports the ≈50 % Si recovery
      honestly and attributes it to oxidation loss in VIM *(R3#3)*
- [x] Adopt **measured at.%** as the LLM-alloy's working identity
      (51.5Fe-29.8Mn-11.9Al-4.2Ni-2.0Si-0.45C), stated in §2.1 *(R3#3)*
- [~] Soften **"the benchmark relies on B2"** — prose done in §4.1 (now "contribute to,
      rather than solely determine", with R3's full list of factors). **Citations NOT added:**
      Omori *APL* 101 (2012) 231907 and La Roca *JALCOM* 708 (2017) 422 are not in
      `references.bib` and adding entries without verified author lists would be worse than
      omitting them. See the new "Citations to add" item in Tier 1. *(R3#10)*
- [x] Delete **"single-phase-controlled structural metal"** → "a structural metal whose
      flow stress is grain-size controlled" *(part of R3#11)*
- [x] Add the **0.06 wt.% P note** for the benchmark, with the conservative-comparison
      argument *(R1#8)*
- [x] Add a paragraph on the **33 % elongation at 1000 °C** — respectable but not
      exceptional for duplex γ+α Fe-Mn-Al, which is the point: a serviceable structural
      metal that is not an SMA *(R1#9)*
- [~] **Revisit Si in the Discussion** — §4.2 already exonerates Si thermodynamically.
      Still missing the second half of the triage answer: that the measured 2.04 at% (half
      the intent) delivered neither the intended solid-solution strengthening nor a decisive
      shift in α stability, and may have contributed to D0₃ ordering. Blocked on the **Heo
      2012** citation. *(R1#6)*
- [x] Fix the ambiguous **"unloaded to zero stress, and continued to zero strain"** in §2.4
      — now "unloaded to zero stress, after which the crosshead was returned to its starting
      position (nominal zero strain)". **Confirm with S. Cai (D5)** that this is what was
      done. *(self-audit #6)*

### New Tier 0 items created by the Rietveld files (done 2026-08-08)

- [x] **§2.5** — MAUD version 2.33 named, three-phase model spelled out with its fixed
      lattice parameters, E-WIMV ODF treatment described and justified by the wire's fibre
      texture, profile residuals cross-referenced to §3.3.
- [x] **Fig. 5 → two panels**, new caption with R_wp/R_p for each and the fixed cells.
      Figure file swapped; the old single-panel version is archived at
      `figures/archive-2026-08-08-Figure_5-single-panel.jpg`.
- [x] **§3.3** — explains the R_wp gap between panels (21.4 % vs 12.5 %) by grain
      statistics: the undeformed wire is beaded, deformation subdivides grains and improves
      powder averaging. Consistent with the benchmark argument two paragraphs later.
- [x] **Declarations** — the generative-AI statement was **false as submitted** ("No
      generative AI tools were used to draft, edit, or otherwise prepare the text").
      Rewritten to separate the two roles: Gemini as the study method, and AI assistance in
      the CALPHAD scripting, Rietveld extraction and drafting of this revision.
      🔴 **Frank must verify the scope of this statement before submission — it is the
      authors' declaration to make, not a drafting decision.**

### Held back deliberately — do NOT write until S. Cai answers

- [ ] 🔴 **The §3.3 phase-fraction sentences.** §3.3 and §4.1 still present 62/34/4 as
      the output of quantitative Rietveld refinement. Per the analysis above it was not
      refined. Nothing was changed, because the honest wording depends entirely on his
      answer to "where did 0.62/0.34/0.04 come from?"
- [ ] 🔴 **Any before/after phase-fraction comparison** in §3.3 (62→60.8, 34→35.1,
      4→4.05). Same reason.
- [ ] **Soften the "≈4 % D0₃ bulk constituent" argument** in §4.1 once the above resolves —
      a refinement of the same specimen put it at 1.6 %.

## Tier 1 — writing, no new data (one focused session)

- [ ] 🔴 **Citations to add to `references.bib`** — five references the reviewers supplied
      or the answers depend on, none of which is currently in the bib. Each needs its full
      author list and exact title looked up; do not guess them.
      | Key needed | Reference | Unblocks |
      |---|---|---|
      | `omori2012apl` | Omori *et al.*, *Appl. Phys. Lett.* **101** (2012) 231907 | R3#10 |
      | `laroca2017jalcom` | La Roca *et al.*, *J. Alloys Compd.* **708** (2017) 422 | R3#10 |
      | `rahnama2017acta` | Rahnama *et al.*, *Acta Mater.* **132** (2017) 627–643 | R3#2, R1#9 |
      | `saha2022jom` | Saha *et al.*, *JOM* **74** (2022) 3181–3190 | R3#2, R1#9 |
      | `heo2012mmta` | Heo *et al.*, *Metall. Mater. Trans. A* **43** (2012) 1731–1735 | R1#6, R3#2 |
- [ ] **Title** → LLM-hypothesized + experimental validation + phase stability
      *(drafted in `front_JMRT.md`; needs co-author sign-off)*
      *(R2 Title#1-3, R1#5)*
- [ ] **Abstract** — state novelty explicitly, add recoverable strain and yield strength
      numbers, justify rather than suggest the carbon role, explain why the benchmark is
      superelastic and this alloy is not *(R2 Abs#1-4)*
- [ ] **§1** — broaden the AI-alloy-design literature beyond LLMs *(R2 Intro#1)*; define the
      prediction-vs-validation gap *(R2 Intro#2)*; expand the composition rationale
      *(R2 Intro#3)*; state objectives and hypotheses at the end *(R2 Intro#4)*
- [ ] **§3.3** — state plainly that in this system the parent is BCC α and the martensite
      product is FCC γ, and that no ε-HCP or α′ was detected *(R2 R&D#6)*
- [ ] **§3.3** — soften every "no B2" to a detection-limit-bounded statement *(R3#8)*
      *(the actual number is a Tier 4 item; write the sentence now, insert the value later)*
- [ ] **§4.1** — temper carbon causality: composite compositional change, C largest single
      contributor on a γ-stabilising-potency basis, not isolable from two alloys
      *(R1#1, R3#9, R2 Abs#3)*
- [ ] **§4.1** — add the mechanistic chain for why a 62 % γ / 34 % α duplex deforms by slip
      *(R1#3)*
- [ ] **§4.2** — downgrade recovery / recrystallisation / grain growth from conclusion to
      inference; say what evidence would settle it *(R3#11)*
- [ ] **Ni-equivalent arithmetic** written up as the bridging quantitative argument, with its
      stainless-calibration limitation stated *(supports R1#1, R3#9)*
- [ ] **Read Rahnama 2017, Saha 2022, Heo 2012**, then position §2.1 and §4.3 against the
      lightweight-steel literature — the composition sits in the Fe-Mn-Al-C field where
      B2/D0₃/κ serve strength and ductility, not reversible transformation *(R3#2 — the
      single strongest comment in all three reviews)*
- [ ] **§4.3 reposition** — bounded experimental claim (n = 1 case study, AI merely the
      candidate source) + retained methodological claim (LLM compositions need
      thermodynamic pre-screening) *(R3#12, R2 R&D#5)*
- [ ] **§5** — separate observation from interpretation; broader implications; LLM-only
      limitations; recommend thermodynamic pre-screening *(R2 Concl#1-4)*
- [ ] Update **`highlights.md`** and the **JMRT cover letter** to match the tempered claims

## Tier 2 — needs files already in this repo

Highest value per unit effort in the whole plan. The data exists; it was cut during the
Materials & Design revision.

- [ ] **D7 — Frank confirms the AGG micrograph reading.** The archived image does not show
      "no AGG"; it shows large grains, some apparently spanning the wire, arrested by a
      continuous band of fine equiaxed grains — heterogeneous coarsening pinned by
      second-phase bands. This is exactly the mechanism R1#4 asks about. **Blocks the two
      items below.**
- [ ] **New AGG figure** — LLM-alloy vs benchmark after the identical 3-cycle route, from
      `figures/archive-2026-06-pre-MD-revision/Fig2b_*` and `Fig2c_*` *(R1#4, R3#4)*
- [ ] **New §3.4 "Response to the abnormal-grain-growth treatment"** — currently one
      sentence; R1 correctly calls it a second, independent failure mode *(R1#4, R3#4)*
- [ ] **Add the LLM-alloy AGG cyclic curve** (`Fig3b_AI_3cycle_AGG_cyclic.png`)
- [ ] **Add the benchmark cyclic curves** (`Fig3c_*`, `Fig3d_*`) so R3#7's comparison is on
      the page *(R3#7)*
      > ⚠️ **Integrity flag.** The 2026-08-03 memo found the benchmark itself gives only
      > 0.44 % (20 fpm) and 0.09 % (0.8 fpm) recoverable transformation strain against
      > 5–8 % in the literature, and at 0.8 fpm reverse transformation is absent. Once these
      > curves are on the page a reviewer can compute this. State the number and own it.
      > Frame the claim as *"no detectable transformation in the LLM-alloy under a route
      > that produced measurable, if modest, transformation in the benchmark."*
- [ ] Update `figures/captions.md`

## Tier 3 — CALPHAD (unblocked, ~a day of compute + a day of writing)

Answers five comments across all three reviewers at once, and is the difference between
conceding R3#12 and winning it.

- [x] Set up `revision/JMRT-R1/calphad/` — fetch script, scripts, CSV results, figures
- [x] **Equilibrium step diagrams, both alloys, 400–1400 °C** — 791 points, three databases.
      Both databases carrying Ni reproduce the benchmark's single-phase α solution window
      *(R1#2, R2 R&D#2)*
- [x] **C = 0 control run** — **all three databases agree that removing carbon alone
      restores the single-phase α window at 1200 °C** *(R1#1, R3#9)*
- [x] **B2 stability check** — order parameter extracted from site fractions. Benchmark holds
      19–22 % ordered B2 from 400–1050 °C; the LLM-alloy holds ~10 % at 400 °C falling to
      zero by ~850 °C. "Cannot form B2" is too strong; "no usable solution + age window" is
      correct and stronger *(R3#8, R1#2)*
- [x] **κ-carbide check** — predicted at only ~2 %, only below 580 °C. Right compositional
      field, carbon an order of magnitude too low to precipitate κ *(R3#2)*
- [x] **Cross-validate across the three databases** — agreement is exact on the C = 0 result
- [x] **Model limitations** documented in `results/ANALYSIS.md`, with the numerical artifacts
- [ ] **Ni sensitivity run** — vary Ni 4.2 → 7.8 at.% at fixed C, to complete the answer to
      R3#9. The C = 0 run already holds Ni fixed, so this is confirmatory rather than load-bearing
- [x] **Figures cleaned and artifacts resolved.** Re-run at 10 °C spacing (numbers
      unchanged, so they are grid-independent). Absent phases now plot as zero instead of
      being omitted, so lines rise from and return to 0. The partitioned bcc is drawn as one
      continuous curve with the ordered portion shaded, which removes the false
      "B2 vanishes / α appears" step at the order–disorder transition. The mc_fe/LLM
      spurious 100 % γ spikes were re-computed at higher grid density and cross-checked
      across four densities. Only two disclosed items remain: a 0.1–0.2 % phantom liquid set
      in mc_fe/benchmark, and 400–430 °C non-convergence in mc_fe/LLM
- [x] Decide which figure goes in the paper — mpea-02b, rebuilt for publication by
      `calphad/make_paper_figure.py` → `figures/Figure_7.png`. Alloy names match the
      manuscript (Omori-alloy / AI-alloy), one shared legend, 1200 °C marked on each panel
- [x] **§4.4 / §5** — the methodological claim is now demonstrable rather than asserted: the
      failure was predictable from free tools in an afternoon *(R2 Concl#4)*

### Written into the manuscript (2026-08-06)

- [x] **§2.6 Equilibrium thermodynamic calculations** — engine, version, the three databases
      and why three, measured-chemistry inputs, the C-free virtual alloy, four stated
      limitations. New refs: `otis2017pycalphad`, `lukas2007calphad`, `hallstedt2017mpea`,
      `hallstedt2023mpea`, `prechimn04`, `mcfe`
- [x] **§3.4 Equilibrium phase stability** — Fig. 7 + Table 3 (1200 °C fractions, three
      databases × three alloys). Benchmark control, AI-alloy duplex, C-free restoration,
      carbides and the D0₃ equilibrium result
- [x] **§4.1 extended** — three new paragraphs connecting calculation to observation: the
      duplex prediction matches Fig. 1b/4a/5 and explains the 40-min and AGG insensitivity;
      the α/γ majority discrepancy stated plainly; D0₃ as metastable; the ordered-bcc field
      unavailable in an α matrix
- [x] **§4.2 The role of carbon** (new; old 4.2/4.3 → 4.3/4.4) — the in-silico control, the
      ~190 °C solvus shift, Si and Ni exonerated, the stated limit that carbon is decisive at
      the process temperature and not everywhere, κ/lightweight-steel positioning
- [x] Abstract and Conclusions updated; Data availability now covers the calculation scripts
- [ ] **Two deletions from §4.1 to confirm with S. Cai** — the "lacks the chemical driving
      force" sentence (superseded: the parent phase is never formed, so driving force is not
      the operative limit) and the "Fe₃Al extracts Fe and Al from the matrix" sentence
      (weak, and harder to sustain now that D0₃ is shown to be metastable rather than
      equilibrium). Both were removed, not reworded
- [ ] **Generative-AI declaration** — the Declarations section still states that no
      generative AI was used to prepare the manuscript text. Sections 2.6, 3.4, 4.1 and 4.2
      were drafted with AI assistance, so that statement must be updated before resubmission

### Revisions after review (2026-08-07 / 08)

- [x] **wt% vs at%** — Fig. 7 panels never stated their unit, so the compositions looked
      inconsistent with Table 1 (which is wt%). Conversion re-verified from Table 1: it
      reproduces the figure exactly. Chemistries now live in the caption with the unit named
- [x] **mpea-02b Si renormalization disclosed** — the database carries no Si, so Si is
      dropped and the remainder renormalized; §2.6 now gives the composition actually
      solved, Fe–30.5Mn–12.2Al–4.3Ni–0.46C, and notes the ≤0.6 at% shift
- [x] **B2 shading is a partition, not a phase** — confirmed `ordered ≤ total` at every
      temperature in both alloys. Below ≈1090 °C the benchmark bcc is *fully* ordered, so
      equilibrium there is B2 + γ, **not** coherent B2 in an α matrix. §3.4, §4.1 and the
      Conclusions were corrected: the coherent nanostructure is the kinetically arrested
      approach to that equilibrium, reached by quenching single-phase α and ageing it
- [x] **Experimental C-free heat named as future work** in §4.2 — the paper previously had
      no future-work statement at all, while R1#1 had asked for exactly that control
- [x] **S. Cai, 2026-08-08 — Fig. 7 reduced to two panels.** Carbon-free panel removed; the
      result is unchanged and now carried by Table 3 (all three databases) plus explicit
      solvus numbers in §3.4. Panels labelled by role (benchmark / LLM-hypothesized) instead
      of by chemistry. Legend moved below the axes in both the paper figure and the
      diagnostic `plot_step_diagrams.py`, where per-panel legends had sat on the curves
- [ ] **Wording check for S. Cai** — panels read "(a) Omori-alloy / benchmark" and
      "(b) AI-alloy / LLM-hypothesized", keeping the short names §2.1 defines while carrying
      his descriptors. Trivial to switch to his literal "Omori Benchmark" / "LLM-Hypothesized"
      if he prefers, but then §2.1's naming should change with it

## Tier 3b — independent XRD re-analysis (done 2026-08-05, E: drive online)

Read `revision/JMRT-R1/xrd/ANALYSIS.md` before editing any text.

- [x] **The manuscript's phase identification is CONFIRMED from the raw patterns.** The
      benchmark shows superlattice intensity only at B2 (100) (3.9–7.2 % of the strongest
      reflection); the LLM-alloy shows it at *both* D0₃ (111) — which B2 cannot produce —
      and D0₃ (200), reproducibly across three patterns, on a 0.2 % baseline. Benchmark
      forms B2, LLM-alloy forms D0₃, exactly as claimed *(§4.1)*
- [x] **R3#8 answerable with a number, not a concession** — B2 in the LLM-alloy is bounded
      at ≥4–7× less abundant than in the benchmark, and the ~1 % at that position is
      accounted for by D0₃ (200)
- [x] **All reflections index to bcc + fcc**, out to fcc (420) and bcc (321). No unindexed
      majority phase
- [x] Two earlier concerns **withdrawn**: the "transposed fractions" reading (the raw data
      agrees the LLM-alloy is fcc-rich) and "D0₃ unsupported" (it is supported; it is simply
      not an *equilibrium* phase, and the only database modelling D0₃ has no Ni)
- [ ] Use `xrd/superlattice_window.png` as a new figure — it makes the B2-vs-D0₃ contrast
      visible in one panel and directly answers R3#8

### 🔴 Three items that must be settled before text is written

- [ ] **The 62 / 34 / 4 refinement is not on the E: drive.** No MAUD, GSAS or refinement
      project anywhere. The only artifact is `X-ray fitting.jpg` (2025-11-26): a **two-phase**
      fit (bcc + fcc, **no D0₃**) reporting **70.3 % fcc**. And §3.3 says 34 % α while §4.1
      says 37 %. Three numbers, no agreement, and the fit statistics cannot be produced if a
      reviewer asks. **Get the refinement from J. Yan (SSRF) or S. Cai.**
      > **S. Cai, 2026-08-08 — partly answered.** Fig. 5 is the **heat-treated (undeformed)**
      > specimen, 1200 °C / 1 min; the caption and §3.3's use of it are correct. The
      > `Rietveld-sample 6.jpg` filename is not the SSRF `Sam6` numbering. Still outstanding:
      > the file itself, R_wp/GoF, ESDs, and the 34 vs 37 vs 70.3 reconciliation.
- [ ] **Take up S. Cai's offer of a refinement of the deformed specimen (Sample 6).** A
      before/after pair under the same phase model turns "relative peak intensities are
      essentially unchanged" (currently qualitative, Fig. 6a) into **phase fractions before and
      after 10 % strain** — quantitative proof of no stress-induced transformation in the AI
      alloy, which is the paper's central claim. Also cross-checks the 62/34/4 numbers.
      Only meaningful **with ESDs**: without them, 62 → 61 says nothing *(R1#3, R2 R&D#1)*
- [x] **Benchmark refinement / B2 detection limit from a fit — CLOSED, not obtainable.**
      S. Cai: the Omori alloy grain-grows heavily at 1200 °C, its rings break into a few
      discrete spots (visible in **Fig. 4c, d**), and no Rietveld model can be matched to it.
      R3#8 must therefore be answered from the raw superlattice ratios in `xrd/ANALYSIS.md`
      (≥4–7× bound), not from a refinement. **Written into §2.5 and §3.3 on 2026-08-08**
- [ ] **M_s may be above room temperature.** CALPHAD puts the LLM-alloy at 62–71 % bcc at
      1200 °C; the quenched material is fcc-rich; γ is the martensite product in this system.
      If α transformed to γ *during the quench*, the alloy is already martensitic before
      loading — a better explanation for the absence of superelasticity than the current one,
      and a direct consequence of carbon raising γ-stability. **Cheapest test: DSC.** Second
      cheapest: look for martensite morphology in `Fe-SMA-FC-1200C4FPM F72.jpg`, already on E:
- [ ] **Soften the §3.3 AGG inference** — "a similar pattern indicates the multi-phase
      microstructure is a stable state at 1200 °C" does not follow if both specimens were
      quenched, since both would transform identically on cooling

### Housekeeping found on E:

- [ ] **Rotate the AtomGPT API key** — it sits in plaintext in `E:\FE-SMA\fe_sma_xrd_notes.txt`,
      and that same file recommends pushing the directory to GitHub
- [ ] Do **not** cite `E:\FE-SMA\ANALYSIS.md` or the DiffractGPT/JARVIS output. It mislabels
      bcc fundamentals as B2 evidence, inverts its own 2θ→d conversions, and headers the data
      "APS, Argonne" when the manuscript and `synchrfig.docx` both say SSRF
- [ ] Confirm the beamline attribution in one line — raw `.tif` paths read `C:\APS_EXP\...`
      while everything else says SSRF BL12SW. Presumably a local folder convention, but a
      reviewer given the raw files would ask
- [ ] State the anneal precisely in §2: "1200 °C for 1 min" is the 1200 °C / **4 fpm F72**
      continuous anneal, ≈1.5 min in a 72-inch hot zone

## Tier 4 — needs other people or the E: drive

Start the asks now; they have the longest latency in the plan.

- [ ] **D4** SME test heating rate and hold time — Song Cai *(R1#7)*
- [ ] **D5** tensile test standard actually followed — Song Cai *(R2 Exp#2)*
- [ ] **D6** do micrographs exist at intermediate anneal temperatures? — Song Cai *(R3#11)*
- [ ] 🔴 **D2 — reconnect the E: drive** (`E:\FE-SMA\` — raw Instron exports, synchrotron/MAUD
      files). **Promoted to blocking by the CALPHAD results**: the MAUD refinement is the only
      way to settle whether the 62/34 phase fractions are transposed and what the 4 % minor
      phase actually is. Also unblocks the three items below
- [ ] **Replicate counts and scatter** for Table 2 *(R2 Exp#3)* *(needs D2)*
- [ ] **Rebuild Fig. 2** from source — clipped tick labels, panels too small, and
      700/900/1100 °C missing relative to Table 2 *(R2 R&D#3, R2 R&D#4)* *(needs D2)*
- [ ] **B2 detection limit** estimated from the Rietveld refinement, to bound "no B2"
      quantitatively *(R3#8)* *(needs D2)*
- [ ] **D3** locate the original **Gemini 2.5 Deep Research transcript** — prompt,
      constraints, candidate ranges, predicted phase constitution. Needed to document the
      LLM workflow reproducibly *(R2 Exp#1)*, and to answer R1#2's sharpest question: did
      the model predict single-phase BCC, and did it account for D0₃? If the transcript is
      unrecoverable, say so plainly and describe the workflow from memory, flagged as such

## Tier 5 — new experiments (decide, then mostly decline with reasons)

- [ ] **D8 — decide feasibility with Song Cai.** Each item below is a real ask on someone
      else's furnace time
- [ ] EBSD on the anneal series — would settle §4.2 properly *(R3#11)*
- [ ] TEM or APT for B2 below the XRD detection limit *(R3#8)*
- [ ] DSC for transformation temperatures *(supports R3#10)*
- [ ] Benchmark alloy given the 200 °C/3 h age, for a like-for-like ageing comparison
      *(R3#5)*
- [ ] Cast a **C-free variant** of the LLM composition — the only thing that fully answers
      R1#1 experimentally. Expensive. **The Tier 3 C = 0 run is the honest substitute and
      should be offered as such**
- [ ] For anything declined: write the reason in the response letter rather than leaving it
      unaddressed — a reasoned decline reads far better than silence

## Tier 6 — response letter and verification

- [ ] Point-by-point reply to **all 45 comments** (R1×9, R2×24, R3×12). JMRT requires a reply
      in every box, so cross-reference shared answers rather than leaving any blank
- [ ] **R1#5** — note graciously that the manuscript already reads "AI" (PDF text extraction
      gives 25× "AI alloy", 0× "Al-alloy"; it is a rendering-font collision in Editorial
      Manager) and that we adopted "LLM-" anyway
- [ ] **Frame the Omori alloy as a control, not a subject** *(S. Cai, 2026-08-08)*. Where a
      comment presses on the benchmark's transformation behaviour, answer: it is the
      reference condition, not the object of study; its superelasticity is established across
      the literature and reproduced here (Figs. 3b, 6b); we neither need nor claim a
      quantitative phase-fraction measurement for it. The paper's question is why the
      **AI alloy** — same processing — does not transform and is γ-dominated
- [ ] **R2-vs-R3 conflict on generalisation** — R2 Concl#2 wants broader AI implications,
      R3#12 wants them narrowed. Name the tension to the editor and land on the split:
      bounded experimental claim, retained methodological claim
- [x] **Marked-up manuscript with changes tracked** *(2026-08-08)* —
      `revision/JMRT-R1/R1-manuscript/Cai_Fe-SMA_JMRT_R1_marked-up.docx` (252 tracked
      revisions: 136 insertions, 116 deletions) and `..._clean.docx`. Built by rendering
      `manuscript.md` with the **submitted DOCX as pandoc's `--reference-doc`** so styling
      carries over, then Word `CompareDocuments` against the submitted file. Doing it this
      way rather than hand-editing was necessary because the six new CALPHAD references
      renumber the whole bibliography (24 → 30), which no manual find/replace gets right.
      The submitted original is untouched; archived at
      `revision/JMRT-R1/as-submitted/Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx`.
      Verified: all sections present, 0 stale "AI-alloy"/"Omori alloy", references
      renumbered to 30, 3 tables, 7 figures, encoding intact (95 °, 63 α, 37 γ, 0 mojibake).
- [ ] Every numeric claim re-checked against source data
- [ ] Phase fractions consistent across §3.3, §4.1, abstract
- [ ] All new citations resolve via citeproc; rebuild the DOCX
- [ ] Read-through against the full reviewer list — confirm no comment left unanswered
- [ ] Commit and push

---

## Review

*(to be filled in after the revision ships)*
