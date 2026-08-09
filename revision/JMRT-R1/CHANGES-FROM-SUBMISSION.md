# What changed between the submitted manuscript and the JMRT R1 revision

**Manuscript:** JMRT-D-26-06169 · *Mechanical Responses of an AI-Hypothesized
Super-elastic Fe-Mn-Al-Ni-Si-C Alloy*
**Submitted:** 2026-07-15 · **Decision:** major revision (R1 major · R2 revise · R3 not
in present form), 45 comments
**Baseline for every number below:** commit `54c0bb2`, the state of `manuscript.md`
matching the submitted DOCX. Archived copy:
`revision/JMRT-R1/as-submitted/Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx`
**This document current as of:** 2026-08-09

Companion documents:

| File | What it holds |
|---|---|
| `revision/JMRT-R1/comment-triage.md` | The 45 comments, verdict and planned action for each |
| `tasks/todo.md` | Live status, tier by tier, with what is still blocked and on whom |
| `revision/JMRT-R1/xrd/RIETVELD-FILES-ANALYSIS.md` | Why the published phase fractions are not yet quotable |
| `revision/JMRT-R1/calphad/results/ANALYSIS.md` | CALPHAD method, results, and stated limitations |

---

## 1. The headline numbers

| | Submitted | Now | |
|---|---|---|---|
| Body words | 4,118 | **10,774** | +162 % |
| Figures | 6 | **7** | Fig. 7 new; Fig. 5 replaced with a two-panel version |
| Tables | 2 | **3** | Table 3 new |
| References | 24 | **35** | every new entry verified against Crossref by DOI |
| Numbered sections | 14 | **18** | §2.6, §3.4, §4.2 new; old §4.2/§4.3 renumbered to §4.3/§4.4 |
| Tracked revisions vs. submission | — | **339** | 180 insertions, 159 deletions |

### Where the words went

```
§4.2 The role of carbon                  NEW    +1,166
§3.4 Equilibrium phase stability         NEW      +866
§4.1 Origin of the absence…             +794    →  1,150
§4.4 Implications (was §4.3)             +482    →    768
§2.6 Equilibrium calculations            NEW      +598
§5   Conclusions                         +477    →    634
§3.3 Synchrotron diffraction             +688    →  1,079
§1   Introduction                        +405    →    875
§4.3 Anneal dependence (was §4.2)        +308    →    678
§2.1 Alloy design and synthesis          +226    →    728
§3.2 Cyclic stress–strain response       +217    →    776
Declarations                             +141    →    252
Abstract                                 +126    →    308
§2.5 Synchrotron X-ray diffraction       +110    →    230
§3.1 Microstructure                       +43    →    241
§2.2, §2.3, Acknowledgments                 0    unchanged
```

---

## 2. The six substantive additions

### 2.1 CALPHAD — the largest single body of new work

~2,630 new words, one new figure, one new table. Three reviewers independently asked for
equilibrium calculations (R1#2, R2 R&D#2, R3#2). New **§2.6** gives the method — pycalphad
0.11.2 against three open databases (mpea-02b, PrecHiMn-04, mc_fe v2.059), measured
chemistries as input, four stated limitations. New **§3.4** gives the results with
**Fig. 7** and **Table 3**. New **§4.2** builds the carbon argument on them.

The load-bearing result: **deleting carbon alone moves the α solvus from ≈1340 °C to
≈1150 °C and restores 100 % α at 1200 °C — in all three databases independently.** The
benchmark's single-phase α field is reproduced without being fitted, which is what
licenses applying the calculation to the test alloy.

Consequence for the paper's argument: the failure is no longer "insufficient driving
force for transformation" but "no accessible heat treatment produces the parent phase at
all." That is a stronger and more defensible claim, and it makes R2 Concl#4 demonstrable
instead of hortatory — the screen that would have caught this composition takes minutes
on a desktop with free tools.

Answers R1#1, R1#2, R3#2, R3#9, R2 R&D#2, R2 Concl#4.

### 2.2 Rietveld and synchrotron XRD

**§2.5** nearly doubled and **§3.3** nearly tripled. MAUD 2.33 named, the three-phase
model spelled out with its fixed lattice parameters, E-WIMV ODF texture treatment
described and justified by the wire's fibre texture, profile residuals reported per
panel. **Fig. 5 replaced** with S. Cai's two-panel version (undeformed and deformed);
the old single-panel figure is archived at
`figures/archive-2026-08-08-Figure_5-single-panel.jpg`.

Two specific reviewer wins:

- **R3#8 now has a number rather than a concession.** Every "no B2" was softened to a
  detection-limit-bounded statement, and the bound is quantified from the raw
  superlattice intensities: B2 in the LLM-alloy is **at least four times less abundant**
  than in the benchmark (D0₃-only {111} at 0.49–1.02 %, S/N 16–27, against the
  benchmark's 0.19–0.28 % at S/N 2.3–2.9).
- **R2 R&D#6** answered directly: in this system the parent is BCC α and the martensite
  product is FCC γ — the reverse of carbon steels — and no ε-HCP or α′ was needed to fit
  any pattern.

§3.3 also now explains the R_wp gap between the two Fig. 5 panels (21.4 % vs 12.5 %) by
grain statistics: the undeformed wire is beaded, and deformation subdivides grains and
improves powder averaging.

### 2.3 Lightweight-steel positioning (R3#2)

The strongest scientific comment in all three reviews, answered in four places after
reading the three papers R3 supplied rather than citing them blind:

- **§2.1** places the measured chemistry in both alloy fields where it is introduced: the
  same Ni-Al pairing at essentially the same Ni level as Fe-15Mn-10Al-0.8C-5Ni and
  Fe-16Mn-9Al-0.9C-5Ni, differing chiefly in ~2× the Mn and ~⅛ the carbon.
- **§4.1** reframes D0₃ from an unexplained metastable oddity into the ordering product
  this alloy family is *known* to give, with Saha's evidence that nanoscale NiAl B2 is
  only marginally stable at 1200 °C in a γ-majority Ni-alloyed FeMnAlC steel.
- **§4.2** states the core answer: both families are built from the same four elements
  and give the same ordered phases, but put them to opposite purposes — reversible
  transformation in one, strengthening of a structure never meant to transform in the
  other.
- **§4.3** shows Table 2's 1000–1200 °C conditions sitting inside the low-density-steel
  property envelope on all three measures.

**Heo 2012 was the find of this pass.** It reports that substituting Si for Al in a
Fe-Mn-Al-C low-density steel is undesirable *because* Si promotes (Fe,Mn)₅(Si,Al)C
together with the **(Fe,Mn)₃(Al,Si) D0₃ ordered phase in ferrite**, with serious loss of
ductility. D0₃ in α is exactly what this alloy formed, so **R1#6 (the unrevisited Si
rationale) now has a documented mechanism instead of a shrug** — stated as a documented
second role the design rationale never engaged with, explicitly *not* as a causal claim,
since two heats with no Si-free control cannot separate a Si contribution from an Fe-Al
one.

### 2.4 Reviewer-driven writing

- **Abstract** (R2 Abs#1, 2, 4): novelty stated as the first experimental test of an
  LLM-hypothesized SMA; mechanical numbers added (σ₀.₂ 1948 → 502 MPa, 33 % elongation,
  ≈0.5 % benchmark recovery); one clause on *why* the benchmark works. The additions took
  it to 341 words, over a typical Elsevier cap, so it was tightened to **292** with all
  three additions verified still present.
- **§1** (R2 Intro#1–4): the field broadened into its three cited families — property-
  targeted screening, generative inverse design, LLM hypothesis generation — rather than
  LLMs alone; a sharpened gap statement on why validated candidates are rare and
  published failures rarer still; the agent's own hypothesis stated in its own terms
  before it is examined, with an objectives paragraph.
- **§3.2** (R2 R&D#4): panel-by-panel narration of Fig. 2, with the mapping verified
  against the figure itself — (a) as drawn, (b) 600, (c) 800, (d) 1000, (e) 1200 °C,
  (f) 1200 + 200 °C/3 h. The Table 2 eight-conditions vs Fig. 2 six-panels gap is now
  stated and justified rather than left silent.
- **§4.4 and §5** (R3#12, R2 R&D#5, R2 Concl#1–3): the n = 1 scope conceded explicitly
  while the methodological claim is retained on the strength of the diagnosis rather than
  the sample size; a paragraph on what a diagnosed negative result is good for;
  conclusions split into observation and interpretation with three stated limitations.

### 2.5 Naming and title

**52 occurrences renamed** to **LLM-alloy** and **benchmark alloy** throughout, with
"AI-guided" and "AI-assisted" retained for the general field where no element symbol is
adjacent (R1#5, R2 Title#1). Zero stale occurrences remain.

The **revision title** is drafted in `front_JMRT.md` and flagged
`NEEDS CO-AUTHOR SIGN-OFF`:

> Experimental Validation of an LLM-Hypothesized Fe-Mn-Al-Ni-Si-C Alloy: Phase Stability
> Governs the Absence of Super-elasticity

It closes R2 Title#1 (LLM not AI), #2 (experimental validation), #3 (phase stability) and
R1#5 in one change, and fixes a mis-parse no reviewer raised: in the submitted title
"super-elastic" grammatically modifies "Alloy", so the title asserted the very thing the
paper disproves.

### 2.6 Declarations

The submitted generative-AI statement read *"No generative AI tools were used to draft,
edit, or otherwise prepare the text."* **That was false as submitted.** It has been
rewritten to separate the two roles: Gemini as the object of study, and AI assistance in
the CALPHAD scripting, Rietveld extraction and drafting of this revision.

> 🔴 **Frank must verify the scope of this statement before submission.** It is the
> authors' declaration to make, not a drafting decision.

Data availability was also extended to cover the calculation scripts.

---

## 3. Six errors corrected that no reviewer caught

1. **Phase-fraction inconsistency.** §4.1 said α ≈ 37 %, §3.3 said ≈ 34 %. Since
   62 + 34 + 4 = 100, 37 was wrong. The submitted PDF carries the error, so it must be
   flagged as a correction in the response letter.
2. **Matrix / island contradiction.** §3.1 called the Al-rich darker region the "matrix"
   and assigned it to BCC α, while §3.3 made γ the majority phase at 62 %. A 34 % phase
   described as continuous matrix while the 62 % phase is "blocky islands" is at best
   confusing. §3.1 now declines to name either constituent as the matrix and says why: a
   2-D section through an interpenetrating duplex structure cannot establish 3-D
   continuity. Consequential edits followed in §4.1 ¶2 and ¶3, where the matrix
   assignment was load-bearing. **R1#3 came within one sentence of finding this.**
3. **"Very close to nominal" for Si**, which was recovered at ≈50 % of intent. Caught by
   R3#3. §2.1 now reports the shortfall honestly and attributes it to oxidation loss in
   vacuum induction melting.
4. **Element ordering** differed between title (Fe-Mn-Al-Ni-Si-C) and abstract
   (Fe-Mn-Al-Si-Ni-C). The abstract was brought into line with the title.
5. **One `DO₃`** (letter O) against 20 correct `D0₃` (zero). Normalized.
6. **§2.4 ambiguity** — "unloaded to zero stress, and continued to zero strain" is
   ambiguous about what was controlled. Rewritten as "unloaded to zero stress, after
   which the crosshead was returned to its starting position (nominal zero strain)".
   ⚠️ Still needs S. Cai's confirmation (D5) that this is what was done.

Also fixed, outside the manuscript: `front_JMRT.md` ended with a `---` horizontal rule,
which pandoc parses as the start of a **second YAML metadata block** when concatenated
with `manuscript.md`. It was silently breaking the build. Changed to `***`, which renders
identically and never starts YAML.

---

## 4. What was deliberately NOT changed

### The 62 / 34 / 4 phase fractions

§3.3 and §4.1 still present these as the output of quantitative Rietveld refinement, and
they are still absent from the abstract where **R2 Abstract#2 explicitly asks for them**.

This is deliberate. S. Cai's MAUD files, analysed in
`revision/JMRT-R1/xrd/RIETVELD-FILES-ANALYSIS.md`, show that those numbers were **never
refined**:

- all three phase fractions are marked `not refinable` in `sample-5-2.prn.lst`;
- all scale factors are pinned at 1.0;
- the twelve refined parameters are instrument geometry plus Popa crystallite size;
- the values are *exactly* 0.62 / 0.34 / 0.04 in a file that reports elsewhere to eight
  significant figures — so **there are no ESDs, because nothing was refined**;
- the one run that *did* refine fractions put D0₃ at **1.56(11) %**, not 4 %, with α at
  34.68(14) %, almost exactly the published value.

Promoting an unrefined number to page one is the exposure this analysis found. The honest
wording depends entirely on S. Cai's answer to a single question — **where did
0.62 / 0.34 / 0.04 come from?** — so nothing was guessed.

That one answer unblocks three comments: R1#3, R2 Abstract#2 and R2 R&D#1.

### Other deliberate holds

- **Any before/after phase-fraction comparison** in §3.3 (62→60.8, 34→35.1, 4→4.05).
  Same reason. Neither panel of the new Fig. 5 has refined fractions, so the before/after
  pair currently supports only the qualitative claim.
- **The "≈4 % D0₃ bulk constituent" argument** in §4.1, pending the same answer.
- **`behaviour` (5) vs `behavior` (7)** — a pre-existing mix in text the reviewers already
  read. Fixing it would add tracked-change noise the editor has to read for no reviewer
  benefit; copyediting will catch it.

---

## 5. Reviewer scorecard

**29 of 45 answered** at the time of writing. The remaining 16, grouped by what unblocks
them, are enumerated in `tasks/todo.md`:

| Group | Comments | Blocked on |
|---|---|---|
| A | R1#1, R3#5, R3#6, R3#9 | nothing — in progress |
| B | R1#4, R3#4, R3#7 | Frank's D7 call on the AGG micrograph, and the R3#7 integrity decision |
| C | R1#3, R1#7, R2 Abs#2, R2 Exp#2, R2 R&D#1 | S. Cai — chiefly the phase-fraction question |
| D | R1#2 (part), R2 Exp#1, R2 Exp#3, R2 R&D#3 | the Gemini transcript (D3) and the E: drive (D2) |

---

## 6. How the deliverables are built

Hand-editing the DOCX was tried and abandoned for two reasons: the eleven new references
renumber the whole bibliography (24 → 35), which no find/replace gets right; and Word's
`Find` cannot match across existing revision markup, so edits silently miss once tracked
changes are present.

The working method:

1. `cat front_JMRT.md manuscript.md > full_JMRT.md`
2. `pandoc` with `--citeproc`, `--bibliography=references.bib`,
   `--csl=elsevier-with-titles.csl`, and **the submitted DOCX as `--reference-doc`** so
   the styling carries over
3. Word `CompareDocuments` against the submitted file, which produces proper tracked
   changes including the renumbered citations
4. `Revisions.AcceptAll()` on a copy for the clean version

The comparison script lives in the session scratchpad as `compare.py`. Note that this
Word build's `CompareDocuments` has **no `CompareMoves` parameter** — position 15 is the
`BSTR` author name — so the call must be positional with 17 arguments, not 18.
