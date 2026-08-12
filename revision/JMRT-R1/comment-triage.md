# JMRT-D-26-06169 — reviewer comment triage

**Manuscript:** *Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy*
**Decision:** major revision (R1 major revision · R2 revise · R3 "not in present form")
**Submitted PDF audited:** `C:\Users\frank\Downloads\JMRT-D-26-06169 (3).pdf` (28 pp, text extracted)
**Editing base:** `manuscript.md` (repo body matches the submitted text; the JMRT author block adds X. Wang)
**Prepared:** 2026-08-05

Verdict vocabulary:

| Tag | Meaning |
|---|---|
| **CONCEDE** | Reviewer is right — change the claim or the text. No new data needed. |
| **CONCEDE+DATA** | Reviewer is right, **and we already hold unpublished data that answers it.** |
| **CONCEDE+NEW** | Reviewer is right and it needs work we do not currently have. |
| **REBUT** | Answerable on the existing record without weakening the science. |
| **PARTIAL** | Concede the premise, push back on the remedy. |

---

## A. The four structural demands

All three reviewers converge on four things. Everything else is detail. Get these right and
the revision succeeds; get them wrong and R3 kills it on the second pass.

### A1. "Carbon is the culprit" is not supported by a two-alloy comparison
**R1#1 · R3#9 · R2 Abstract#3 · R2 R&D#2 → CONCEDE (claim) + one new analysis**

Five elements change at once. On a plain atomic-percent basis carbon is the *smallest* change
of all, which is why the singling-out reads as arbitrary. Measured compositions converted to at.%:

| | Fe | Mn | Al | Ni | Si | C | P |
|---|---|---|---|---|---|---|---|
| AI-alloy (measured) | 51.5 | 29.8 | 11.9 | 4.2 | 2.04 | 0.45 | – |
| Omori-alloy (measured) | 42.7 | 34.1 | 15.2 | 7.8 | <0.02 | 0.04 | 0.10 |
| **Δ (AI − Omori)** | **+8.8** | **−4.3** | **−3.3** | **−3.6** | **+2.0** | **+0.41** | **−0.10** |

Two moves, and they must be made together:

1. **Temper the causal claim** everywhere it appears (abstract, §4.1, conclusions, highlights,
   cover letter). The defensible statement is *"the composite compositional change moved the
   alloy across the γ/α stability boundary; carbon is the largest single contributor on a
   γ-stabilising-potency basis, but its role cannot be isolated without a C-free variant of the
   same composition."* Explicitly name the missing control experiment as future work — R1 asked
   for exactly that and will accept it being scoped out if it is named.
2. **Give the quantitative argument the manuscript currently lacks.** Carbon is small in at.%
   but large in potency. A Schaeffler-type nickel equivalent (Ni_eq = Ni + 30C + 0.5Mn) gives
   **32.7 for the AI-alloy vs 26.2 for the Omori-alloy**, of which the carbon term alone
   contributes **+13.5 vs +1.3** — an order of magnitude more γ-stabilising drive than the
   −3.6 at.% Ni removal takes away. This is *indicative only*: Schaeffler is calibrated on
   stainless steels, not Fe-Mn-Al, and must be labelled as such. It is a bridge, not a
   substitute for A2 below.

> ⚠️ Do not present the Ni_eq number as the primary evidence. It is a plausibility argument that
> buys the reviewers' patience while CALPHAD does the real work.

### A2. CALPHAD — the single highest-leverage piece of new work
**R1#2 · R2 R&D#2 · R2 Conclusion#4 · R3#2 · R3#9 → CONCEDE+NEW · BLOCKED, needs a decision**

Three independent reviewers ask for equilibrium phase calculations. One equilibrium step diagram
per alloy (mole fraction of phases vs temperature, 400–1400 °C) would simultaneously answer:

- R1#2 — is the "insufficient chemical driving force" claim quantitative?
- R1#1 / R3#9 — which element actually moves the γ/α boundary? (Run the AI composition with C
  set to zero. That is the control experiment *in silico*, and it costs nothing once the licence
  question is solved.)
- R3#2 — why should this composition have been expected to be superelastic at all?
- R3#8 — is B2 NiAl even predicted to be stable in the AI-alloy at the ageing temperature?
- R2 Conclusion#4 — "integrate thermodynamic screening into AI-guided design": you can then
  *demonstrate* the screen that would have caught this, rather than recommending it abstractly.

**Blocker.** No CALPHAD capability on this machine — `pycalphad` is not installed and no `.tdb`
database is present. The physics needs a database with assessed Fe-Mn-Al-Ni-Si-C interactions
(TCFE/TCHEA class); free TDBs generally do not cover this sub-system reliably. Options, best first:

1. **Thermo-Calc via Purdue** — X. Wang is a co-author and Purdue MSE almost certainly holds a
   TCFE licence. One afternoon of someone's time. *Strongly preferred.*
2. **Thermo-Calc via Fort Wayne Metals** — S. Cai; industrial licences for TCFE are common.
3. **pycalphad + a published Fe-Mn-Al-C assessment** — free, but the assessment will not cover
   Ni and Si simultaneously, so the D0₃/B2 predictions would be the weakest part of the answer.
   Usable as a fallback for the γ/α boundary only, with the limitation stated.
4. **Decline, with reasons.** Viable but expensive: it concedes R3's strongest point and leaves
   A1 resting on a stainless-steel correlation. Only take this route if 1–3 all fail.

### A3. The AGG condition — answerable *today* with data already in the repo
**R1#4 · R3#4 → CONCEDE+DATA · highest value per unit effort in the whole revision**

Both reviewers correctly identify that the abnormal-grain-growth result is one sentence (§3.3,
line 92) with no figure, and R1 is right that it constitutes a **second, independent failure
mode**. What neither reviewer knows is that the data exists — it was cut during the
Materials & Design revision and is sitting in `figures/archive-2026-06-pre-MD-revision/`:

| File | What it shows |
|---|---|
| `Fig2b_AI_3cycle_AGG_microstructure.jpg` | AI-alloy after the 3-cycle AGG treatment |
| `Fig2c_Omori_3cycle_AGG_bamboo.jpg` | Omori-alloy, colour-etched — textbook bamboo grains spanning the wire |
| `Fig3b_AI_3cycle_AGG_cyclic.png` | AI-alloy cyclic σ–ε **in the AGG condition** (to ~9.2 %, fractured) |
| `Fig3c/3d_Omori_*_cyclic.png` | Omori cyclic curves at 1200 °C/5 min and /12 s — see A4 |

**This converts the manuscript's weakest paragraph into a new figure and a new subsection.**
Plan: promote to a new §3.4 "Response to the abnormal-grain-growth treatment", with a two-panel
micrograph figure (AI vs Omori after the identical 3-cycle route) and the AI AGG cyclic curve.

> ⚠️ **The current one-line claim is not what the micrograph shows, and Frank must confirm the
> reading before it goes in writing.** `Fig2b` does *not* show "no AGG". It shows large grains,
> several hundred µm across, some apparently spanning the wire — interrupted by a continuous
> band of fine equiaxed grains that arrests the migrating boundary. The honest description is
> **heterogeneous, arrested coarsening: no continuous bamboo structure formed because
> second-phase bands pinned the boundaries** — which is *precisely* the mechanism R1#4 asks for
> ("discuss how the multi-phase stability prevents grain boundary migration"). Side by side with
> the Omori bamboo micrograph it is the most persuasive figure available. But the sentence
> "did not exhibit AGG" must be rewritten, and Frank should verify the interpretation against
> the original micrograph set before we commit to it in print.

### A4. "Identical processing ⇒ composition is the sole variable" is invalid as written
**R3#1 · R3#5 · R3#7 · R1 (implicit) → CONCEDE (sentence) + REBUT (conclusion) + DATA**

R3 is straightforwardly correct on the metallurgy: identical nominal parameters do not produce
identical recrystallisation, grain size, texture, or precipitation state in two different
compositions. **Delete the sentence** at the end of §1 ("Because the processing history was kept
identical for both alloys, compositional differences are the sole variable determining the final
mechanical properties") and replace with the weaker, true statement — same *nominal* route, and
the observed difference is in response to that route.

But the *conclusion* survives, and there are three defences to deploy — in this order:

1. **The processing bias runs the wrong way for R3's objection.** The AI-alloy received the
   200 °C/3 h age known to improve pseudoelasticity in this family (Fig. 2f) and showed nothing.
   The Omori benchmark in Fig. 3b was 1200 °C/1 min **with no age at all** and still showed
   reverse transformation on heating. The route was, if anything, biased *in favour* of the
   AI-alloy. This is a genuine argument, not a dodge — make it explicitly.
2. **Add the Omori cyclic curves** (`Fig3c`, `Fig3d`) so the comparison R3#7 asks for is actually
   on the page instead of asserted. Currently only the AI-alloy gets a full cyclic panel set.
3. **Concede the scope limit** and name it: whether a *different* route (different ageing window,
   different solution temperature) could unlock transformation in this composition is untested,
   and the paper does not claim otherwise. This is R3#5's real point and it is correct.

> 🚩 **Integrity flag — read before drafting the response.** The 2026-08-03 memo analysis of
> RD0697-7 (the Omori benchmark) found that under this anneal + water-quench + no-age route the
> benchmark is itself only *marginally* superelastic: recoverable **transformation** strain of
> 0.44 % (20 fpm ≈ 12 s) and 0.09 % (0.8 fpm ≈ 5 min), against 5–8 % reported for this alloy;
> at 0.8 fpm the reverse transformation is absent, not merely degraded. The manuscript's Fig. 3b
> value (≈0.5 % recovery) is consistent with that and is honestly reported — but once the Omori
> cyclic curves are added per (2) above, a careful reviewer can compute this for themselves.
> **The revision must state the benchmark's modest recovery in numbers and own it**, framing the
> claim as *"no detectable transformation in the AI-alloy under a route that produced measurable,
> if modest, transformation in the benchmark."* Attempting to present the benchmark as strongly
> superelastic would not survive round two, and would be wrong.

---

## B. Comment-by-comment

### Reviewer 1 (9 comments — "major revisions")

| # | Topic | Verdict | Action |
|---|---|---|---|
| 1 | Carbon cannot be isolated | **CONCEDE** | See **A1**. Temper claim + Ni_eq argument + name the C-free control as future work. |
| 2 | §4.3 descriptive, not diagnostic; wants CALPHAD | **CONCEDE+NEW** | See **A2**. Also: answer the two direct questions — did the model predict single-phase BCC? did it consider D0₃? Retrieve the original Gemini Deep Research transcript and quote its predicted phase constitution. If the transcript is lost, say so. |
| 3 | No mechanistic depth on why duplex → slip | **CONCEDE** | Rewrite §4.1 ¶2 with the actual chain: (i) α is only ~34 % and present as *discrete blocky islands*, not a continuous parent, so transforming them requires the surrounding γ to accommodate the shape strain plastically — γ slip preempts transformation; (ii) γ yields at ≈500 MPa (1200 °C), far below any plausible σ_Ms for a composition this γ-rich; (iii) D0₃ Fe₃Al is a bulk ordered constituent (~4 %), not a coherent nanoscale dispersion, so it does not raise slip resistance the way B2 does in the benchmark. Answers R1's two literal questions (morphology? pinning?). |
| 4 | AGG buried; second failure mode; no figure | **CONCEDE+DATA** | See **A3**. New §3.4 + new figure. |
| 5 | "Al-alloy"/"Al-hypothesized" ambiguous with aluminium | **REBUT + adopt anyway** | **The manuscript says "AI" everywhere** — text extraction of the submitted PDF confirms 25×"AI alloy", 11×"AI-alloy", 6×"AI-guided", 5×"AI-hypothesized", 0×"Al-alloy". The reviewer misread the Editorial Manager rendering font, in which capital-I and lowercase-l are identical glyphs. Say so gracefully — and then **fix it anyway**, because in a paper about Fe-Mn-**Al** the ambiguity is real. Recommended: rename the alloys **"LLM-alloy"** and **"benchmark alloy"** throughout, reserving "AI-guided/AI-assisted" for the general field where no element symbol is adjacent. This single change also satisfies **R2 Title#1**. |
| 6 | Si rationale never revisited in Discussion | **CONCEDE** | Add a short §4.1 passage: Si is a strong BCC/α stabiliser and lowers SFE, so it was expected to *help*; the measured 2.04 at.% (half the intended 4 at.%, see R3#3) delivered neither the intended solid-solution strengthening nor a decisive shift in α stability, and may have contributed to D0₃ ordering (cite Heo, *MMTA* 43 (2012) 1731 — R3 handed us this reference). Acknowledge in hindsight. |
| 7 | SME test: heating rate and hold time missing | **CONCEDE** | Fill in §2.4. **Needs Frank/S. Cai** — retrieve the actual furnace/hot-air-gun ramp and dwell. Do not guess. |
| 8 | 0.06 wt% P in the benchmark — embrittlement? | **REBUT (courteously)** | 0.06 wt% ≈ 0.10 at.% P is below the level at which grain-boundary embrittlement is normally reported in Fe-Mn austenitic/duplex alloys, and the benchmark showed both good ductility and clear stress-induced transformation — so P did not preclude the reference behaviour. Note it can only have *degraded* the benchmark, making the AI-alloy-vs-benchmark contrast conservative. Add one sentence to §2.1 and a line to the limitations. |
| 9 | 33 % elongation exceptional? structural potential? | **CONCEDE (easy win)** | Yes — comment briefly. 33 % is respectable but not exceptional for duplex γ+α Fe-Mn-Al alloys, which is itself the point: the alloy is a credible *structural* material that simply is not an SMA. Cite Rahnama *Acta Mater.* 132 (2017) 627 and Saha *JOM* 74 (2022) 3181 — again handed over by R3#2, so one literature pass serves three comments. |

### Reviewer 2 (24 comments — "revise")

Mostly presentational; the cheapest reviewer to satisfy fully. Do **all** of it.

**Title (3)** — Adopt: *"Experimental Validation of an LLM-Hypothesized Fe-Mn-Al-Ni-Si-C Alloy:
Phase Stability Governs the Absence of Super-elasticity"* (or close). Satisfies #1 (LLM not AI),
#2 (experimental validation), #3 (phase stability) **and R1#5** in one stroke. Note the current
title is also arguably mis-parseable as claiming the alloy *is* super-elastic.

**Abstract (4)** — #1 state the novelty (first experimental test of an LLM-hypothesized SMA)
explicitly; #2 add numbers (recoverable strain ≈ 0 vs benchmark ≈ 0.5 %; σ₀.₂ 502–1948 MPa
across the anneal sweep; 62 % γ / 34 % α / 4 % D0₃); #3 justify rather than assert the carbon
role (see A1 — and keep the tempering consistent with §4.1); #4 add one clause on *why* the
benchmark works (coherent B2 NiAl in a continuous α parent).

**Introduction (4)** — #1 broaden beyond LLMs (add active learning / Bayesian optimisation /
GAN-based inverse design for alloys, 2023–2026); #2 sharpen the gap statement — prediction is
cheap, physical validation is rare, negative results rarer still; #3 the composition rationale
moves partly here and gets much stronger under **R3#2**; #4 add an explicit objectives-and-
hypothesis paragraph at the end. Note #4 will replace the deleted "sole variable" sentence (A4).

**Experimental (3)** — #1 **document the LLM workflow reproducibly**: model version, date, the
actual prompt, the constraints given, and what the agent returned (the full candidate range, not
just the selected point). This is a reproducibility requirement for the paper's central premise
and R3#12 leans on it too. *Needs Frank to retrieve the original session.* #2 cite the tensile
standard — ASTM E8/E8M for metallic tension, with the fine-wire gauge deviation stated; if a
NiTi-style protocol was followed for the cyclic test, cite ASTM F2516 as the model. **Confirm
with S. Cai, do not assume.** #3 report replicate counts — how many specimens per condition in
Table 2, and scatter. *Needs the raw data (E: drive, see Blockers).*

**Results & Discussion (6)** — #1 quantitatively tie phase fraction to behaviour (folds into
A1/R1#3); #2 → **A2**; #3 **redraw Fig. 2** — the current panel axes have clipped tick labels
("2.5"→"2.", "10"→"1(") and the panels are too small; rebuild from source data at journal column
width; #4 Fig. 2e (1200 °C) — the text never refers to *any* Fig. 2 panel by letter; add
panel-by-panel narration and note that Table 2 has 8 conditions while Fig. 2 shows 6, so move
700/900/1100 °C to supplementary or add panels; #5 deepen the negative-result implications
(pairs with R3#12 — keep the two answers consistent); #6 martensite in the microstructure —
answer directly: **in Fe-Mn-Al-Ni the martensite product is the FCC γ phase and the parent is
BCC α, the reverse of conventional steels**; Rietveld resolved γ + α + D0₃ only, with no ε-HCP
or α′ present, and the γ present here is thermally stable retained γ, not stress-induced. This
distinction should be stated once in §3.3 — its absence is a genuine readability failure.

**Conclusions (4)** — #1 separate observation from interpretation (restructure into "we observed"
/ "we interpret"); #2 broader implications; #3 limitations of LLM-only composition selection;
#4 recommend thermodynamic pre-screening — **and if A2 lands, demonstrate it rather than
recommend it.** #2 and #3 must be reconciled with **R3#12**, which pushes in the opposite
direction; see the note below.

### Reviewer 3 (12 comments — the hostile review)

| # | Topic | Verdict | Action |
|---|---|---|---|
| 1 | "Sole variable" claim invalid | **CONCEDE** | See **A4**. Delete the sentence. |
| 2 | Why expect superelasticity from a *lightweight-steel* composition? | **CONCEDE+NEW (literature)** | The strongest scientific comment in all three reviews, and it is fair. Fe-Mn-Al-(Ni)-(Si)-C at these levels is the low-density-steel field, where B2/D0₃/κ-carbide serve strength and ductility, not reversible transformation. **Add a paragraph to §2.1 or §1** positioning the composition against that literature and stating plainly what the agent was reasoning from and why it expected transformation behaviour anyway. Cite the three references R3 supplied: Rahnama *Acta Mater.* **132** (2017) 627–643; Saha *JOM* **74** (2022) 3181–3190; Heo *MMTA* **43** (2012) 1731–1735. *This comment is also, in substance, the paper's real finding* — the agent proposed a lightweight-steel composition while believing it was proposing an SMA. Say that out loud in §4.3; it converts the objection into the result. |
| 3 | Si is 1.11 vs 2.2 wt% — "very close to nominal" is false | **CONCEDE** | Correct and embarrassing. Fix three ways: (i) delete "very close to the nominal values" and report the deviation honestly (Si recovered at ≈50 % of intent, consistent with oxidation loss in vacuum induction melting); (ii) **define the alloy by its measured composition** — 51.5Fe-29.8Mn-11.9Al-4.2Ni-2.0Si-0.45C (at.%) — and use that everywhere the nominal is currently used as the alloy's identity; (iii) note that the benchmark *is* close to nominal (42.7Fe-34.1Mn-15.2Al-7.8Ni measured vs 43.5-34-15-7.5 nominal), so only one alloy carries this caveat. |
| 4 | AGG results incomplete; key specimens not the AGG condition | **CONCEDE+DATA** | See **A3**. Also concede the second half: the Fig. 2/3 specimens were *not* AGG-treated, and say why (the AGG route did not produce the target structure — which is itself the result). |
| 5 | Route may simply be wrong for this composition | **PARTIAL** | See **A4**. Concede the scope limit explicitly; deploy the ageing-asymmetry argument; add "optimisation of the ageing window for this composition" to future work. Do **not** claim the route was optimal. |
| 6 | Ex-situ XRD cannot exclude fully reversible transformation | **PARTIAL — already partly addressed** | §3.3 already concedes this ("Although an ex-situ measurement made after unloading cannot, on its own, exclude a fully reversible transformation…"). Strengthen by pointing out the *mechanical* argument is the decisive one: a fully reversible transformation that reverts on unloading would produce recoverable strain, and Figs. 2/3 show none beyond elastic springback. XRD is corroborating, not primary. Then add in-situ/loading-stage XRD to future work. |
| 7 | No corresponding stepwise cyclic curves for the benchmark | **CONCEDE+DATA** | Add `Fig3c`/`Fig3d`. Read the integrity flag in **A4** first. |
| 8 | Absence of a B2 peak ≠ absence of B2 | **PARTIAL — needs one new analysis** | Logically correct; we cannot prove absence. Two-part answer: (i) soften every "no B2" statement to "no B2 superlattice reflections were resolved above the detection limit of the present measurement"; (ii) **estimate that detection limit from the Rietveld refinement** and quote it — a number turns a weak concession into a quantitative bound. Then concede that TEM/APT would be required to exclude a fine dispersion, and put it in future work. *Requires the synchrotron/MAUD files (E: drive).* |
| 9 | Ni 7.5→4 at.% may matter as much as C | **CONCEDE** | See **A1** — same answer as R1#1, and the two must be worded consistently. The Ni_eq arithmetic addresses this head-on: Ni's −3.6 at.% is worth −3.6 Ni_eq units against carbon's +13.5. |
| 10 | "Relies on B2" is too absolute | **CONCEDE (trivial)** | Reword §4.1 to "B2 precipitates contribute to, rather than solely determine, transformation reversibility", and add the list R3 supplies — parent-phase stability, transformation temperature, grain size, orientation, texture, and the competition between transformation stress and plastic yield stress. Cite Omori *APL* 101 (2012) 231907 and La Roca *JALCOM* 708 (2017) 422. |
| 11 | §4.2 recovery/recrystallisation/growth read from tensile data alone | **CONCEDE** | Fair. Either (a) present grain-size measurements per anneal temperature if micrographs exist, or (b) downgrade the language from conclusion to inference ("the trends are *consistent with*…"), and remove "fully recrystallized" and "single-phase-controlled structural metal" as definitive statements. **"Single-phase-controlled" is doubly wrong** — this alloy is explicitly two-phase; that phrase should go regardless. Prefer (a) if micrographs exist; check with Frank. |
| 12 | Overgeneralises from n=1; reposition as a case study | **PARTIAL — the one place to push back** | Concede the overreach: soften §4.3 and the conclusions from "AI models cannot yet capture…" to "this candidate, under this route, did not…", and state n=1 plainly. **But do not accept full repositioning to a pure alloy case study** — that would strip the paper of the contribution the editor and R1 explicitly valued ("highly timely", "rare experimental test of computationally generated hypotheses"). Middle position: the *experimental* claims are a case study; the *methodological* claim — that LLM-proposed compositions require thermodynamic pre-screening before synthesis — is supported because the failure mode was diagnosable and generic (an equilibrium calculation would have caught it). If A2 lands, this argument becomes demonstrable rather than rhetorical, and R3#12 becomes winnable. **If A2 does not land, concede more ground here.** |

> ⚠️ **R2 and R3 pull in opposite directions.** R2 Conclusion#2 wants *broader* AI implications;
> R3#12 wants them *narrowed* to a case study. The response letter must handle this explicitly —
> acknowledge the tension to the editor, and land on the split above (bounded experimental claim,
> retained methodological claim). Do not silently give each reviewer a different paper.

---

## C. Self-audit — problems the reviewers did *not* catch

These will surface in round two if they are not fixed now.

1. **Phase-fraction inconsistency.** §3.3 reports ≈34 % α; §4.1 reports "the α-phase accounts for
   only ≈37 %". 62 + 34 + 4 = 100, so **34 % is correct and "≈37 %" is an error.** Fix §4.1.
2. **Matrix/island assignment contradicts the phase fractions.** §3.1 calls the Al-rich *darker*
   region the "matrix" and assigns it to BCC α, with Mn-rich "blocky islands" as FCC γ — but §3.3
   makes γ the majority phase at 62 % and α the minority at 34 %. A 34 % phase described as the
   continuous matrix while the 62 % phase is "blocky islands" is at best confusing and at worst a
   swapped assignment. **Resolve before submission** — quantify area fractions from the micrograph,
   or reword. R1#3 comes within one sentence of finding this.
3. **Element ordering differs between title and abstract** — title "Fe-Mn-Al-Ni-Si-C", abstract
   "Fe-Mn-Al-Si-Ni-C". Trivial, but it is on page one.
4. **Fig. 2 axis labels are clipped** in the submitted figure ("2.5"→"2.", "10"→"1("). R2#3 noticed
   the size; the clipping is worse and needs a rebuild from source data, not a rescale.
5. **Table 2 lists 8 anneal conditions; Fig. 2 shows 6 panels.** 700 / 900 / 1100 °C curves are
   absent without comment.
6. **§2.4 wording** — "unloaded to zero stress, and continued to zero strain" is ambiguous about
   what was controlled. Rewrite alongside the R1#7 fix.
7. **Reviewer 2 is not mentioned in the "Opposed Reviewers" workflow** — irrelevant to science.
   ~~The JMRT portal requires a reply to every comment; all 45 need an individual reply box.~~
   **Corrected 2026-08-12 by Frank, from the portal itself: the response is submitted per
   *reviewer*, not per comment — three responses, not forty-five boxes.** Each reviewer's
   document should number that reviewer's own comments and answer them in order, and an answer
   shared between reviewers must be written out in full for each of them rather than
   cross-referenced, since no reviewer sees another's reply.

---

## D. Blockers and decisions needed from Frank

| # | Blocker | Blocks | Note |
|---|---|---|---|
| D1 | **CALPHAD access** — Thermo-Calc via Purdue (X. Wang) or Fort Wayne Metals (S. Cai) | A2, R1#2, R3#2, R3#9, R2 Concl#4, and the strength of the R3#12 rebuttal | The single most consequential decision in this revision. |
| D2 | **E: drive not mounted** — `E:\FE-SMA\` holds raw Instron exports and synchrotron/MAUD files | R2 Exp#3 (replicates/scatter), R3#8 (B2 detection limit), Fig. 2 rebuild from source data, A4 integrity numbers | Reconnect the drive; nothing else needed. |
| D3 | **Original Gemini Deep Research transcript** | R1#2 (what did the model actually predict?), R2 Exp#1 (reproducible workflow), R3#12 | If lost, say so in the paper — that is itself a lesson about AI-assisted design provenance. |
| D4 | **SME test heating rate + hold time** | R1#7 | Ask S. Cai. Do not guess. |
| D5 | **Tensile standard actually followed** | R2 Exp#2 | Ask S. Cai. |
| D6 | **Micrographs at intermediate anneal temperatures?** | R3#11 (grain size vs temperature) | If they exist, R3#11 is answered with data instead of hedged language. |
| D7 | **Confirm the AGG micrograph interpretation** | A3 | Frank's call on whether "arrested/heterogeneous coarsening" is the right reading of `Fig2b`. |
| D8 | **New experiments feasible at all?** (DSC for Ms/Mf/As/Af; EBSD; TEM/APT; 200 °C-aged benchmark) | R3#8, R3#11, and the depth of every mechanistic answer | Determines whether this is a text-and-analysis revision or a new-data revision. Sets the timeline. |

---

## E. Recommended response strategy in one paragraph

Concede generously on framing (carbon causality, "sole variable", AGG reporting, Si deviation,
the lightweight-steel positioning) — these cost nothing scientifically and they are all correct.
Spend the real effort on three things: **the CALPHAD calculation (D1)**, **the AGG figure and
subsection built from data already in hand (A3)**, and **the Omori cyclic curves with honest
transformation-strain numbers (A4)**. Push back in exactly two places: R1#5, where the manuscript
already says "AI" (graciously, and fix the ambiguity anyway), and R3#12, where full repositioning
to a case study would discard the contribution the other reviewers valued. Everything else in
Reviewer 2's list is presentational and should be done completely — a fully satisfied second
reviewer is worth more than a partially satisfied third.
