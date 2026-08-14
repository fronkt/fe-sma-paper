# JMRT major revision — JMRT-D-26-06169

Reviews received 2026-07-27 (R1), 2026-07-28 (R3), 2026-07-31 (R2). 45 comments total.
Full analysis: `revision/JMRT-R1/comment-triage.md`.
Previous phase-ordered draft of this plan: `tasks/todo-archive-2026-08-05-jmrt-phase-ordered.md`.

**Ordered easiest → hardest.** Tiers 0–1 need nothing but a text editor. Tier 2 needs
files already in this repo. Tier 3 is now unblocked (see the CALPHAD note below).
Tiers 4–5 need other people.

**Status (2026-08-08, late): Tier 0 complete. Tier 1 complete except the two §4.1 carbon-
causality items and the Ni-equivalent arithmetic. Tier 3 complete except the Ni sensitivity
run. Tiers 2, 4, 5, 6 open. 29 of 45 reviewer comments answered, 6 partial, 6 blocked on
S. Cai or Frank, 4 untouched (R1#4, R3#4, R3#7 need only the D7 micrograph call).**

> **2026-08-14 — S. Cai's 08-13 package merged; figures renumbered to 10.** Full account in
> `CHANGES-FROM-SUBMISSION.md` §9. His DOCX was built on the as-submitted manuscript, so only
> his *additions* were ported: four-panel Fig. 1 (new AGG panel d + lamellar/EBSD caveat in
> §3.1), new Fig. 7 (γ/α inverse pole figures + §3.3 texture paragraph), new Fig. 8 (AGG
> diffraction image, now cited where §3.3 described it), AGG-suppression mechanisms in §3.5,
> P source unknown in §2.1, tenfold carbon contrast in the abstract. CALPHAD figure is now
> **Fig. 9** (his requested number), AGG collage **Fig. 10**. **NOT merged, per Frank:** his
> §4.3 CALPHAD interpretation ("both alloys primarily α at 1200 °C… cannot be explained by
> phase stability"), which Table 3/Fig. 9 contradict — needs a conversation with S. Cai
> before resubmission. Optional open item: a citation for the drawn-wire fiber-texture
> statement in §3.3 (his draft had an empty bracket; left uncited as textbook knowledge).

> **Two small consistency fixes made in passing (2026-08-08).** One §3.3 occurrence of the
> ordered phase was written `DO₃` (letter O) against 20 correct `D0₃` — normalized. Two
> `aluminium` spellings introduced in the new §4.2 text were changed to `aluminum` to match
> the pre-existing §2.3 usage. **Left alone deliberately:** `behaviour` (5) vs `behavior` (7)
> is a pre-existing mix in text the reviewers already read; fixing it would add tracked-change
> noise the editor has to read for no reviewer benefit. Copyediting will catch it.
>
> Also: `front_JMRT.md` ended with a `---` horizontal rule, which pandoc parsed as the start
> of a second YAML metadata block when concatenated with `manuscript.md`. Changed to `***`
> (renders identically, never starts YAML). This was silently corrupting the build.

> ✅ **AUTHOR LIST — RESOLVED 2026-08-08.** `front_JMRT.md` now exists with all four
> authors (Frank Y. Cai¹\*, S. Cai², **X. Wang³**, J. Yan⁴). Two things inside it still
> need a human: the **revision title** (changed to the R2-Title-compliant one, needs
> co-author sign-off) and ~~the **duplicate affiliations 1 and 3**~~ — **RESOLVED
> 2026-08-14 with co-author agreement**: merged into a single Purdue superscript 1
> (Frank Y. Cai¹, S. Cai², X. Wang¹, J. Yan³), SSRF renumbered 4 → 3.
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
- [x] Soften **"the benchmark relies on B2"** — prose done in §4.1 ("contribute to, rather
      than solely determine", with R3's full list of factors). **Citations now added**
      *(2026-08-08)*: `omori2012apl` on the coherent-B2 microstructure, and `laroca2017jalcom`
      behind a new clause noting that the precipitates are not a purely mechanical
      contribution — by drawing Ni and Al out of solution they change the matrix composition
      and therefore its transformation temperatures. *(R3#10)*
- [x] Delete **"single-phase-controlled structural metal"** → "a structural metal whose
      flow stress is grain-size controlled" *(part of R3#11)*
- [x] Add the **0.06 wt.% P note** for the benchmark, with the conservative-comparison
      argument *(R1#8)*
- [x] Add a paragraph on the **33 % elongation at 1000 °C** — respectable but not
      exceptional for duplex γ+α Fe-Mn-Al, which is the point: a serviceable structural
      metal that is not an SMA *(R1#9)*
- [x] **Revisit Si in the Discussion** *(2026-08-08)* — §4.2 exonerated Si thermodynamically;
      a new paragraph now adds the second half, that exoneration is not the same as inertness.
      At 2.04 at% (half the intent) Si delivered neither the solid-solution strengthening it
      was specified for nor a decisive shift in α stability, while Heo *et al.* document it as
      a promoter of the (Fe,Mn)₃(Al,Si) D0₃ ordered phase in ferrite — the phase actually
      observed. Stated as a documented second role that the design rationale never engaged
      with, explicitly **not** as a causal claim (two heats, no Si-free control). *(R1#6)*
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

### Held back deliberately — RESOLVED 2026-08-14

- [x] 🟢 **The hold is lifted: Frank confirms the 62/34/4 fractions WERE refined**
      (2026-08-14), superseding `xrd/RIETVELD-FILES-ANALYSIS.md`'s "not refinable" reading,
      which was drawn from the single `.lst` file that reached the repo. The manuscript's
      existing quantitative wording stands unchanged. Remaining ask (not blocking): have
      the refinement file on hand in case a reviewer requests fit statistics or ESDs, and
      reconcile the zip1/sample-6 run that returned D0₃ at 1.56(11) % if a reviewer pushes
      on the ≈4 % figure.

## Tier 1 — writing, no new data (one focused session)

- [x] 🔴 **Citations added to `references.bib`** *(2026-08-08)* — all five verified against
      Crossref by DOI (exact volume/page match, author lists as deposited, not guessed).
      Bibliography now 30 → **35**; all resolve through citeproc with no unresolved keys.
      | Key | Reference | Unblocks |
      |---|---|---|
      | `omori2012apl` | Omori, Nagasako, Okano, Endo, Kainuma, *APL* **101** (2012) 231907 — "Microstructure and martensitic transformation in the Fe-Mn-Al-Ni SMA with B2-type coherent fine particles" | R3#10 |
      | `laroca2017jalcom` | La Roca, Baruj, Sobrero, Malarría, Sade, *JALCOM* **708** (2017) 422–427 — "Nanoprecipitation effects on phase stability of Fe-Mn-Al-Ni alloys" | R3#10 |
      | `rahnama2017acta` | Rahnama, Kotadia, Sridhar, *Acta Mater.* **132** (2017) 627–643 — "Effect of Ni alloying on … two duplex light-weight steels" | R3#2, R1#9 |
      | `saha2022jom` | Saha *et al.* (11 authors), *JOM* **74** (2022) 3181–3190 — "Revealing the localization of NiAl-type nano-scale B2 precipitates within the BCC phase…" | R3#2, R1#9 |
      | `heo2012mmta` | Heo, Song, Park, Bhadeshia, Suh, *MMTA* **43** (2012) 1731–1735 — "Influence of silicon in low density Fe-C-Mn-Al steel" | R1#6, R3#2 |
      >
      > **All three lightweight-steel papers were read, not just cited.** The findings that
      > mattered:
      > - **Heo 2012 is the R1#6 answer.** Substituting Si for Al in a Fe-Mn-Al-C low-density
      >   steel is reported as *undesirable* because Si promotes (Fe,Mn)₅(Si,Al)C **and the
      >   (Fe,Mn)₃(Al,Si) D0₃ ordered phase in ferrite**, with serious loss of ductility.
      >   **D0₃ in α is exactly what this alloy formed.** Si now has a documented mechanism
      >   in the manuscript instead of a shrug.
      > - **Rahnama 2017**: Fe-15Mn-10Al-0.8C-5Ni vs the same without Ni. Ni is added
      >   *specifically* to form NiAl B2; α→B2 ordering is treated as an embrittlement
      >   liability to manage, not a mechanism to exploit. Also states that B2 **and D0₃** are
      >   both known ordering products of this steel family, and gives the family property
      >   envelope (YS 500–940 MPa, UTS 710–1020 MPa, elongation 8–78%).
      > - **Saha 2022**: Fe-16Mn-9Al-0.9C-5Ni, γ-majority with banded BCC — the same
      >   constitution as the LLM-alloy. Nanoscale NiAl B2 sits *inside* the BCC constituent
      >   and shows **limited stability at 1200 °C** (coarsens at 1110 °C, breaks up by 1200 °C).
      >   Independent support for §4.1's claim that no useful B2 is available on this route.
      >
      > Optional further citation, **not added** (would go beyond the five the reviewers
      > named): the 2025 review "B2-strengthened Fe-Mn-Al-C-Ni steels as a promising
      > environmentally friendly structural material", *Crit. Rev. Solid State Mater. Sci.*,
      > doi:10.1080/10408436.2025.2542362 — a single citation establishing Fe-Mn-Al-C-Ni as a
      > recognised structural-steel family. Frank's call.
- [ ] **Title** → LLM-hypothesized + experimental validation + phase stability
      *(drafted in `front_JMRT.md`; needs co-author sign-off)*
      *(R2 Title#1-3, R1#5)*
- [x] **Abstract** *(2026-08-08)* — state novelty explicitly, add recoverable strain and yield strength
      numbers, justify rather than suggest the carbon role, explain why the benchmark is
      superelastic and this alloy is not *(R2 Abs#1-4)*
- [x] **§1** *(2026-08-08)* — broaden the AI-alloy-design literature beyond LLMs *(R2 Intro#1)*; define the
      prediction-vs-validation gap *(R2 Intro#2)*; expand the composition rationale
      *(R2 Intro#3)*; state objectives and hypotheses at the end *(R2 Intro#4)*
- [x] **§3.3** *(2026-08-08)* — state plainly that in this system the parent is BCC α and the martensite
      product is FCC γ, and that no ε-HCP or α′ was detected *(R2 R&D#6)*
- [x] **§3.3** *(2026-08-08, with the number)* — soften every "no B2" to a detection-limit-bounded statement *(R3#8)*
      *(the actual number is a Tier 4 item; write the sentence now, insert the value later)*
- [ ] **§4.1** — temper carbon causality: composite compositional change, C largest single
      contributor on a γ-stabilising-potency basis, not isolable from two alloys
      *(R1#1, R3#9, R2 Abs#3)*
- [ ] **§4.1** — add the mechanistic chain for why a 62 % γ / 34 % α duplex deforms by slip
      *(R1#3)*
- [x] **§4.3** *(2026-08-08; renumbered 4.2->4.3)* — downgrade recovery / recrystallisation / grain growth from conclusion to
      inference; say what evidence would settle it *(R3#11)*
- [x] **Ni-equivalent arithmetic** *(2026-08-09)* — **and the plan for it was wrong.**
      This file previously specified Ni_eq = 32.7 (LLM) vs 26.2 (benchmark) with the carbon
      term at +13.5 vs +1.3. Those were computed on **at.%**; Schaeffler is defined on
      **wt.%**. Recomputed on the correct basis the ranking *reverses*:
      | basis | LLM | benchmark | Δ |
      |---|---|---|---|
      | at.% (as planned) | 32.60 | 26.05 | **+6.55** — supports the paper |
      | wt.% (as defined) | 23.85 | 27.48 | **−3.63** — contradicts the paper |
      >
      > Written into §4.2 as the correlation **and its failure**, with the three reasons:
      > no aluminium term, though Al is 6.2/8.0 wt% and the strongest ferrite stabiliser
      > present; the wt.%/at.% sensitivity of the carbon term (3.2 units vs 13.5); and
      > Cr_eq ≈ 1.7 and 0.0 against a Schaeffler calibration band of 15–30, because neither
      > alloy contains chromium. This is a **stronger** answer to R1#1 and R3#9 than the
      > correlation would have been — a composition-only potency heuristic pointing the
      > wrong way is exactly the failure mode the paper is about. Logged in
      > `tasks/lessons.md`. *(supports R1#1, R3#9)*
- [x] **Read Rahnama 2017, Saha 2022, Heo 2012, then position §2.1 and §4.3 against the
      lightweight-steel literature** *(2026-08-08)* *(R3#2 — the single strongest comment in
      all three reviews)*. Four places changed:
      - **§2.1** — the measured chemistry is now placed in both fields at the point it is
        introduced: same Ni-Al pairing at essentially the same Ni level as Fe-15Mn-10Al-0.8C-5Ni
        and Fe-16Mn-9Al-0.9C-5Ni, differing chiefly in ~2× the Mn and ~⅛ the C.
      - **§4.1** — D0₃ reframed from an unexplained metastable oddity into the ordering
        product this alloy family is *known* to give, with Saha's evidence that NiAl B2 is
        only marginally stable at 1200 °C in a γ-majority Ni-alloyed FeMnAlC steel.
      - **§4.2** — a new paragraph stating the core R3#2 answer: the two families are built
        from the same four elements and give the same ordered phases, but put them to
        opposite purposes (reversible transformation vs. strengthening in a structure never
        intended to transform). Lands on "a composition can sit in two literatures at once
        while satisfying the design intent of only one."
      - **§4.3** — Table 2's 1000–1200 °C conditions shown to sit inside the low-density-steel
        property envelope on all three measures; the colder anneals are outside it for
        reasons of *form* (0.36 mm wire at ≈85% drawing reduction), not chemistry.
        Conclusion: an unoptimized member of the first family, not a failed member of the second.
- [x] **§4.4 reposition** *(2026-08-08; section renumbered 4.3->4.4)* — bounded experimental claim (n = 1 case study, AI merely the
      candidate source) + retained methodological claim (LLM compositions need
      thermodynamic pre-screening) *(R3#12, R2 R&D#5)*
- [x] **§5** *(2026-08-08)* — separate observation from interpretation; broader implications; LLM-only
      limitations; recommend thermodynamic pre-screening *(R2 Concl#1-4)*
### Writing pass 2026-08-08 — also completed

- [x] **R2 R&D#4** — panel-by-panel narration of **Fig. 2** added to §3.2, with the panel
      mapping verified against the figure itself: (a) as drawn, (b) 600, (c) 800, (d) 1000,
      (e) 1200 °C, (f) 1200 °C + 200 °C/3 h. The 700/900/1100 °C gap between Table 2's eight
      conditions and Fig. 2's six panels is now stated and justified in text.
- [x] **R2 R&D#5** — a paragraph in §4.4 on what a diagnosed negative result is actually
      good for, which is the part of this comment that was not already covered.
- [x] **Abstract length checked** — the additions took it to 341 words, over a typical
      Elsevier cap, so it was tightened to **292** with all three reviewer-requested
      additions (novelty, numbers, why-the-benchmark-works) verified still present.

> ⚠️ **Deliberately NOT added to the abstract: the 62/34/4 phase fractions**, which
> R2 Abstract#2 also asks for. Promoting an unrefined number to page one is exactly the
> exposure identified in xrd/RIETVELD-FILES-ANALYSIS.md. Add them once S. Cai answers.
### Group A writing pass (2026-08-09)

- [x] **R3#5 — the route may be wrong for this composition.** New §4.1 paragraph making the
      ageing asymmetry explicit: the LLM-alloy *received* the 200 °C/3 h age reported to
      improve pseudo-elasticity in this family and showed nothing (Fig. 2f, indistinguishable
      from the unaged Fig. 2e), while the benchmark of Fig. 3b received **no age at all** and
      still transformed. The shared route is therefore biased in the LLM-alloy's favour and
      the null result cannot be blamed on a withheld treatment — while conceding that no
      route was optimised for either alloy.
- [x] **R3#6 — ex-situ XRD cannot exclude a fully reversible transformation.** §3.3 rewritten
      to put the evidence in order: a transformation reversible enough to leave no diffraction
      signature would still have produced recoverable strain *during* unloading, and every
      unloading segment across eight anneal conditions returns nothing beyond σ/E; Fig. 3a's
      heating step closes the retained-martensite route. The mechanical measurement is primary,
      diffraction corroborative. What ex-situ genuinely cannot do — observe under load — is
      named and sent to future work.
- [x] **Future-work trio named explicitly in §4.4** (serves R3#5 and R3#6 together): an ageing
      window optimised for this composition rather than inherited from the benchmark; an
      in-situ/loading-stage diffraction measurement; and the experimental carbon-free heat.
      With the reason none of them is expected to overturn the diagnosis — it rests on where
      the α field lies, a property of the composition rather than the treatment.
- [x] **R3#9 Ni sensitivity run — done, and the answer is emphatic** *(2026-08-09)*.
      `calphad/ni_sensitivity.py`, 20 compositions × 62 temperatures on mpea-02b. Full
      write-up in `calphad/results/NI-SENSITIVITY.md`.
      - **With C at the measured 0.45 at%, the α solvus does not move at all: 1340 °C at
        every Ni from 4.2 to 7.8 at%**, not one 10 °C grid step. Removing C puts it at
        1150–1190 °C at every Ni. **Carbon ≈190 °C; nickel ≈0 °C.**
      - Raising Ni at fixed C makes 1200 °C *more* austenitic (bcc 71.1 → 59.6 %), so
        restoring the benchmark's nickel would have made the duplex problem slightly worse.
      - Ni does control **how much** ordered bcc forms — 5.5 → 13.9 % at 700 °C — but always
        coexisting with 86–94 % γ, never as coherent B2 in an α matrix.
      - The line for the paper: **nickel sets how much B2 the alloy could form; carbon sets
        whether there is ever an α matrix to form it in.** Not competing explanations.
      - Written into §3.4 (result) and §4.2 (interpretation, replacing the one-line
        "held at its measured value in the control").
      - Disclosed: 5 of 1240 points non-converged (400–425 °C, low Ni), reported as gaps not
        zeros; one solver artifact at C-free/Ni 5.4/1210 °C, which the first version of
        `solvus()` let shift that entry from 1160 to 1220 °C. Fixed and disclosed inline.
      - ⏳ **mc_fe endpoint cross-check still running** (pdens=2000, 6 elements, ~8 GB). Not
        load-bearing — mpea-02b is the only database with Ni and C together and is the
        primary throughout. Add its section to NI-SENSITIVITY.md if/when it lands.

- [ ] Update **`highlights.md`** and the **JMRT cover letter** to match the tempered claims

## Tier 2 — needs files already in this repo

Highest value per unit effort in the whole plan. The data exists; it was cut during the
Materials & Design revision.

**Executed 2026-08-12 on Frank's instruction to agree with the reviewers.** Full working in
`revision/JMRT-R1/processing/AGG-MICROGRAPH-PROVENANCE.md`.

- [x] **D7 — CLOSED.** Frank's call is to agree with the reviewers, and the drive supports it
      without qualification. It also exposed a bigger problem than D7 asked about: **the
      archived `Fig2b` is not the 0.36 mm wire.** It measures 868 µm against its own 400 µm
      bar, so it is rod stock (≈1 mm, most likely the 0.0418 in 3-cycle specimen). The
      published Fig. 2 pair set an LLM-alloy *rod* beside a benchmark *wire*. The correct
      0.36 mm panel was on the drive unused and measures 330 µm.
- [x] **New AGG figure** — `figures/Figure_8.jpg`, built by `figures/build_agg_figure.py` from
      `figures/sources-AGG/`: (a) benchmark 0.64 mm bamboo, (b) LLM 0.36 mm no coarsening,
      (c) LLM ≈1 mm rod arrested at a fine-grain band, (d) boundary cracks after AGG + age.
      *(R1#4, R3#4)*
- [x] **New §3.5 "Response to the abnormal-grain-growth treatment"** — written. Numbered 3.5,
      not 3.4 as planned here: §3.4 Equilibrium phase stability already existed, and placing
      the AGG section after it both avoids renumbering Figs. 4–7 and lets the AGG result be
      read as the consequence of the equilibrium one. *(R1#4, R3#4)*
- [ ] ⏸️ **LLM-alloy AGG cyclic curve** (`Fig3b_AI_3cycle_AGG_cyclic.png`) — **held, not
      published.** Its ≈460 MPa yield / ≈810 MPa peak / 9.2 % fracture matches no row of the
      eight Instron reports on the drive (nearest 697-6 AGG entries: 1.293 mm/568 MPa/1.0 %,
      1.293 mm/608 MPa/1.0 %, 1.062 mm/1006 MPa/11.9 %). Publishing an unidentified panel in
      the same revision that corrects `Fig2b` for being unidentified would not be coherent.
      **Unblocks the moment its spool is named.** The AGG mechanical result is in §3.5 as
      report numbers instead, which are traceable.
- [x] **Benchmark cyclic curves** (`Fig3c_*`, `Fig3d_*`) — added as panels (c) and (d) of
      Fig. 3 by `figures/build_fig3_with_benchmark.py`. Appended to Fig. 3 rather than made a
      new figure because they are the same test on the same alloys, and a new figure in §3.2
      would renumber Figs. 4–7 for 26 cosmetic tracked changes. *(R3#7)*
      > ✅ **Integrity flag discharged.** §3.2 now states in the body text that the benchmark
      > gives ≈0.44 % (12 s) and ≈0.09 % (5 min) recoverable transformation strain against
      > 5–8 % in the literature, that at 5 min reverse transformation is close to absent, and
      > frames the claim as *"no detectable transformation in the LLM-alloy under a route that
      > produced measurable, if modest, transformation in the benchmark."*
- [x] Update `figures/captions.md` — it had drifted (still "AI alloy"/"Omori alloy", two panels
      behind on Fig. 3). Now **derived**: `python figures/extract_captions.py` regenerates it
      from `manuscript.md`, so it cannot drift again.

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

- [ ] *(downgraded from blocking 2026-08-14 — Frank confirms the refinement was done; what
      remains is obtaining the file itself for the record)* **The 62 / 34 / 4 refinement is
      not on the E: drive.** No MAUD, GSAS or refinement
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
- [x] **Rebuild Fig. 2 — DONE 2026-08-14** (E: reconnected). `figures/Figure_2.png` is now
      written by `revision/JMRT-R1/mechanical/rebuild_figure2.py` from the raw
      `Fe-SMA-FC.is_tcyclic` exports: **all eight annealed panels** (600–1200 °C + aged, so
      R2 R&D#4's missing 700/900/1100 °C curves are now shown rather than excused),
      per-spool diameters, 127 mm gauge, explicit tick locators (the R&D#3 clipping fix).
      Reconstruction check reproduces every Table 2 UTS/elongation to ≤0.5%. §3.2 narration
      re-lettered (1200 °C is now **2g**, aged **2h**). **The as-drawn panel is gone**: no
      raw trace for it exists anywhere on the drive; it stays as a Table 2 row. Old 6-panel
      figure archived at `figures/archive-2026-08-14-Figure_2-six-panel.jpg`. ⚠️ Response
      letter: state that Fig. 2 was rebuilt from raw exports and the as-drawn condition
      is tabulated (and ask S. Cai for the as-drawn export if he has it — it can be added
      as a ninth panel automatically). *(R2 R&D#3, R2 R&D#4)*
- [ ] **B2 detection limit** estimated from the Rietveld refinement, to bound "no B2"
      quantitatively *(R3#8)* *(needs D2)*
- [ ] **Figure print-resolution audit (2026-08-14).** Repo-built figures are fine
      (Fig. 2 = 600 dpi, Fig. 3 = 484, Fig. 9 = 513, Fig. 10 = 484, all at 190 mm double
      column). Four supplied files are below Elsevier's 300-dpi floor even at 90 mm single
      column: **Fig. 4** (796 px wide → 225 dpi), **Fig. 6** (767 px → 216 dpi),
      **Fig. 8** (475 px → 134 dpi), and **Fig. 1** (1195 px → 337 dpi at single column
      but only ~217 dpi at the 140 mm a 4-panel montage wants). Fig. 5 (277 dpi @ 90 mm)
      and Fig. 7 (315 dpi @ 90 mm, plus an overlapping colorbar label) are borderline-OK
      at single column. Remedies: Fig. 6 is rebuildable from the .chi spectra on E:;
      Figs. 1/4/8 need re-export from source (SSRF tifs in `E:\FE-SMA\2026-1\`, micrograph
      originals) or higher-res files from S. Cai. Not reviewer-blocking (only Fig. 2 was
      named), but production will bounce them at acceptance.
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

- [ ] Point-by-point reply covering **all 45 comments** (R1×9, R2×24, R3×12), submitted as
      **three responses — one per reviewer, not one per comment**. *(Corrected 2026-08-12 by
      Frank, who has the portal open; an earlier note here and in `comment-triage.md` §C7 said
      the portal wanted 45 individual boxes.)* Practical consequence: each reviewer gets one
      continuous document that numbers their own comments and answers them in order, so shared
      answers are written out once per reviewer rather than cross-referenced across reviewers —
      a reviewer must not be sent to another reviewer's reply to find their answer
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
- [x] **Marked-up manuscript with changes tracked** *(2026-08-08; rebuilt after the writing
      pass and the reference pass)* —
      `revision/JMRT-R1/R1-manuscript/Cai_Fe-SMA_JMRT_R1_marked-up.docx` (**339 tracked
      revisions: 180 insertions, 159 deletions**; was 252, then 300) and `..._clean.docx`.
      Bibliography now 35 entries. Built by rendering
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
