---
title: "Response to the Editor and Reviewers — JMEP-26-07-50730.R1"
---

**DRAFT 2026-10-12.** Items marked **[OPEN — …]** need a fact or decision from the person named (FC = Frank Cai, SC = S. Cai / Fort Wayne Metals records, JY = J. Yan). Bracketed draft wording inside an OPEN marker is a proposal, not a confirmed fact. Delete this paragraph before upload.

---

Manuscript ID: JMEP-26-07-50730.R1

Title: Absence of Superelasticity in an LLM-Hypothesized Fe-Mn-Al-Ni-Si-C Alloy: Tensile, Synchrotron and CALPHAD Assessment (originally "Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy")

Dear Dr. Asthana,

Thank you for the opportunity to revise our manuscript, and thank you to both reviewers for detailed and constructive reports. We have revised the manuscript throughout. Every comment is answered below, in order, with the location of the corresponding change in the revised manuscript.

## Summary of the revision

Reviewer 2 asked for fuller reporting of the work already performed, a transparent statement of the study's scope, reanalysis of available data where practical, and conclusions limited to the evidence. We have done all four. Since the original submission we have also completed work that bears directly on several comments:

1. **Replicate tensile tests.** Every condition of Table 2 is now the mean of three specimens, with one standard deviation (Section 2.4).
2. **Equilibrium calculations on the measured chemistry.** CALPHAD step diagrams in three independent open databases, a virtual carbon-free control, a nickel scan, and compositions inside the LLM's proposed window (new Sections 2.6 and 3.4, Tables 3 and 4, Fig. 9). Reviewer 2 (comment 5a) suggested this.
3. **Figures re-derived from the raw data.** Fig. 2 from the raw tensile exports; Figs. 4, 6 and 8 from the raw synchrotron detector frames.
4. **The complete LLM design report** (Online Resource 1), and a register of every specimen and calculation behind the figures and tables (Online Resource 2, Tables S1 and S2).
5. **The cyclic abnormal-grain-growth treatments**, now reported with their microstructure and tensile records (new Section 3.5, Fig. 1d, Fig. 10), and the drawing texture (Fig. 7) and the treated rod's diffraction (Fig. 8).

Preliminary results of this work appeared as a three-page extended abstract in the SMST 2026 proceedings (ASM International); it is now cited in Section 1. **[OPEN — FC: keep this disclosure (recommended).]**

Three errors in the original text are corrected: the gauge length was 127 mm, not 13 mm (a typographical error; the instrument records give 5.000 in); the α fraction is 34% (with 4% D0₃), not 37%; and the model was prompted, not trained.

Because most of the text has been rewritten, the marked-up manuscript shows the changes as tracked changes against the original submission. **[OPEN — FC: confirm the highlighting method. A Word comparison against the July file will mark nearly every paragraph; the alternative the letter allows is colored text for new material.]** The section map below gives the correspondence.

| Original submission | Revised manuscript |
|---|---|
| 1 Introduction | 1 Introduction (revised) |
| 2.1–2.5 Materials and experiments | 2.1–2.5 (expanded); **2.6 Equilibrium thermodynamic calculations (new)** |
| 3.1 Microstructure (Fig. 1a–c) | 3.1 (Fig. 1a–d; panel d new) |
| 3.2 Cyclic stress–strain response (Fig. 2, 3; Table 2) | 3.2 (Table 2 now n = 3) |
| 3.3 Synchrotron diffraction (Figs. 4–6) | 3.3 (Figs. 4–6 re-derived; Figs. 7, 8 new) |
| — | **3.4 Equilibrium phase stability (new; Fig. 9, Tables 3, 4)** |
| — | **3.5 Response to the abnormal-grain-growth treatment (new; Fig. 10)** |
| 4.1 Origin of the absence of transformation | 4.1 Interpreting the absence of stress-induced phase transformation |
| — | **4.2 The role of carbon (new)** |
| 4.2 Anneal-temperature dependence | 4.3 |
| 4.3 Implications for AI-guided alloy design | 4.4 |
| 5 Conclusions | 5 Conclusions (restructured: measured / interpreted / calculated / open) |
| — | Online Resource 1 (LLM report); Online Resource 2 (Tables S1, S2) |

**Authors.** **[OPEN — FC: if X. Wang is added, state it here with his contribution and attach the journal's authorship-change form. The Katona draft asks what the journal needs.]**

## Associate Editor

> Thank you for submitting your manuscript to JMEP. Please address our reviewers' comments. Should you choose to submit a revision, you must highlight all changes made within your revised manuscript upon its return and provide a separate response document. Your response and revision will be re-evaluated by the reviewers and the editors.

Thank you. All changes are highlighted in the marked-up manuscript as described above, and this document is the separate response.

> Additionally, a revision of the English is recommended. Please enlist the aid of a professional editing service to correct the English. …

**[OPEN — FC decision.]** Option A: "The revised manuscript was edited by [service] before resubmission." Option B: "The manuscript has been rewritten throughout and checked for grammar and clarity by the authors; we would be glad to use a professional service at the production stage if the editors judge it still necessary." (The Generative-AI declaration already discloses writing assistance.)

## Reviewer 1

> Put the keywords in alphabetical order

Done. The keywords are now: alloy design; CALPHAD; Fe-based shape memory alloy; large language model; phase stability; superelasticity; synchrotron XRD.

> The AI developed alloy was processed in the same way as the established Fe-Mn-Al-Ni alloy to isolate only the effect of composition. However, could the process steps themselves be the reason for not obtaining the shape memory effect? Perhaps the authors should comment on this in the discussion.

We agree that this cannot be excluded experimentally, and the revised manuscript says so. It addresses the question in three ways.

First, we no longer claim that a common route isolates composition. Identical nominal processing does not guarantee identical recrystallization, grain size, texture or precipitation in two compositions (Section 1, Section 4.1).

Second, the LLM-alloy was given a wider range of treatments than the benchmark, and none produced strain recovery (next comment).

Third, the new equilibrium calculations show that the processing question has a compositional root. The benchmark's route depends on solution treatment in a single-phase α field. In all three thermodynamic databases, the LLM-alloy has no single-phase α field at any temperature in the solid state: it is still α + γ when it begins to melt (Section 3.4, Tables 3 and 4). No choice of solution temperature can therefore reproduce the benchmark's starting state. Removing the alloy's 0.10 wt% carbon in the calculation restores that field (Section 4.2).

What remains untested is a solution-and-aging window optimized for this composition rather than inherited from the benchmark; Section 4.4 names it as open, and the Conclusions are worded so that they remain valid if such a route is later found.

> Were alternative processing steps tried in order to possibly obtain the shape memory effect?

Yes. They are now listed in Section 2.2 and reported in Sections 3.2 and 3.5:

- 1-minute strand anneals at seven temperatures, 600–1200 °C (Fig. 2, Table 2);
- the 200 °C/3 h age reported to develop pseudoelasticity in this family (Fig. 2h);
- prolonged holds at 1200 °C for 40 and 80 minutes (Fig. 1c, Fig. 10a, b);
- three cyclic abnormal-grain-growth schedules: two- and three-cycle 1200 ↔ 900 °C schedules on rod, and a four-cycle 1200 °C quartz-tube schedule on wire (Fig. 1d, Figs. 8 and 10);
- exposures at 1250 and 1300 °C, which caused severe oxidation and are not reported further.

No condition showed strain recovery beyond elastic springback on unloading, and the 1200 °C/1 min condition showed none on heating. The cyclic treatments coarsened the rod but did not produce a bamboo structure, and the coarsened conditions were brittle (Section 3.5).

> The AI developed alloy contains additional Si and C as compared to the Omori alloy. Where does this added Si and C appear? In the matrix or in some phases? Or someplace else?

This was not measured directly. EDS cannot quantify carbon and was used qualitatively. We have therefore added the calculated partitioning at the 1200 °C solution-treatment temperature, from the same three databases (Section 3.4). No carbide is stable at that temperature, so both elements are calculated to be in solid solution, and both concentrate in γ: carbon strongly (1.0–1.3 at% in γ against ≈0.1 at% in α, in all three databases) and silicon mildly (2.6–2.7 against 1.7–1.8 at%, in the two databases that carry silicon). The same calculation places aluminum in α and manganese in γ, which is the direction of the EDS contrast in Fig. 1b.

Carbides are calculated to be stable only well below the processing range (κ-carbide below ≈590 °C, M₂₃C₆ below ≈420 °C). None was detected by diffraction or SEM, which would not resolve a fine dispersion, and κ-carbide was not tested in an alternative refinement model, so a small fraction is not excluded (Sections 3.3, 3.4 and 4.2). Silicon may also have contributed to the D0₃ ordering that was observed, as reported for Si-bearing Fe-Mn-Al-C steels; we note this without claiming it (Section 4.2). Note also that only half the intended silicon was recovered in the melt (Table 1).

> How was the strain rate selected? Are shape memory alloys strain rate sensitive in their shape memory effect?

The crosshead speed was 0.25 in min⁻¹ on a 127 mm gauge, a nominal strain rate of 8.3 × 10⁻⁴ s⁻¹ (Section 2.4). The original text gave 1 × 10⁻³ s⁻¹ on a 13 mm gauge; the gauge was a typographical error, and the rate is now computed from the recorded crosshead speed and gauge. **[OPEN — FC: why this rate was chosen. Draft: "It is the quasi-static rate we use routinely for superelastic wire (ref. cai2024niticu)" — confirm the NiTi-Cu work used the same rate before saying so.]**

Yes, superelastic alloys are rate-sensitive, chiefly because the latent heat of transformation warms the specimen when it cannot be conducted away fast enough, which raises the stress needed to continue transforming (Shaw and Kyriakides, 1995, now cited). This changes the stress–strain response of an alloy that transforms; it does not suppress the transformation. The effect should also be weaker in Fe-Mn-Al-Ni, whose transformation stress depends only weakly on temperature (0.53 MPa °C⁻¹; Omori et al., 2011). At the quasi-static rate used, strain rate is not expected to bear on the absence of transformation. This is added to Section 2.4.

## Reviewer 2

> Overall Evaluation …

We thank the reviewer for a careful and constructive report, and for recognizing the value of a documented negative result. We have followed the reviewer's framing throughout: the revised manuscript treats the work as a single-composition case study, reports the processing and characterization records more fully, separates what was measured from what was calculated, interpreted or left open, and narrows the claims about carbon, transformation, precipitates, diffraction and AI-assisted design.

### 1. Title and scientific framing

> (a) Could the authors revise the title so that it states that the alloy was targeted for room-temperature superelasticity but failed to exhibit it? …

Yes. The title is now "Absence of Superelasticity in an LLM-Hypothesized Fe-Mn-Al-Ni-Si-C Alloy: Tensile, Synchrotron and CALPHAD Assessment". It states the negative result, uses the standard spelling (now used throughout), and names the model class (LLM) rather than AI in general. We kept "hypothesized" because the paper treats the composition as a hypothesis under test (Section 1). **[OPEN — FC: or adopt the reviewer's title, "Experimental Evaluation of an LLM-Proposed Fe-Mn-Al-Ni-Si-C Alloy Targeted for Room-Temperature Superelasticity"; co-authors sign off on either.]**

> (b) Could the Abstract and Conclusions distinguish clearly among (i) failure of this composition under the tested processing conditions, (ii) limitations of this particular deep-research workflow, and (iii) the much broader performance of AI-assisted alloy design?

Yes. The Abstract now separates measured, calculated and open results and ends: "This single-composition case study does not rate LLM alloy design generally." The Conclusions are organized the same way. The paragraph on the workflow attributes the limitation to "the workflow as it was run … and not a demonstrated limit on what an LLM can propose", and the final paragraph states the three limitations, including that one candidate cannot establish how often such workflows fail. Section 4.4 makes the same distinction.

### 2. Reproducibility and correct description of the LLM workflow

> (a) Did the authors actually fine-tune or otherwise train a model, upload a closed corpus for retrieval, or simply ask Gemini Deep Research to search public sources? …

We did not train or fine-tune any model. The composition came from one Gemini 2.5 Deep Research session, in which the agent retrieves and reads public sources at query time. **[OPEN — FC: confirm that no files were uploaded to the session.]** "Trained" has been removed, and the workflow is described in Sections 1 and 2.1 and in the Generative-AI declaration.

> (b) Could the authors provide … the complete verbatim prompt sequence, date and exact model/product version, settings available to the user, all sources retrieved, the full unedited model response, and the candidate composition ranges proposed?

The full, unedited report is supplied as Online Resource 1: *New Fe-SMA Alloy Hypotheses*, 41 pages, drawing on 76 sources, all accessed 19 May 2025 and exported 4 June 2025. It lists every source and gives all six candidate families with their composition ranges and performance targets. The product was Gemini 2.5 Deep Research. **[OPEN — FC: settings available to the user, e.g. "none beyond selecting Deep Research".]** The verbatim prompt was not preserved, and the report does not embed it. We state this as a limitation (Sections 2.1 and 5) rather than reconstructing the prompt from memory.

> (c) How were the 'over 200 papers' selected, deduplicated, quality-controlled, and supplied to the agent? …

**[OPEN — FC: where the "over 200 papers" figure came from.]** Draft: "The statement in the original text was inaccurate and has been removed. The agent's report draws on 76 sources, listed in Online Resource 1; [no separate corpus was supplied to it / the figure of 200 counted …]."

> (d) Could the authors state which thermodynamic database or computational tool the agent accessed? …

The agent accessed no thermodynamic database or computational tool, and its report contains no calculation. It recommends CALPHAD and DFT as future work, a recommendation now quoted in Section 4.4. The phrase "thermodynamically screened candidates" has been removed from Section 1. All CALPHAD calculations in the revised paper were made by the authors, on the measured chemistry, after the experiments (Sections 2.6 and 3.5).

### 3. Experimental design does not evaluate general LLM reliability

> (a) How many agent runs and candidate compositions were actually generated, and why was this specific point within the proposed range selected? …

The report proposes six candidate families and ranks them; the alloy was drawn from Hypothesis A2, ranked joint second, and the first-ranked candidate was not synthesized (Section 2.1). Section 2.1 also discloses that the composition was chosen by the authors, specified in atomic percent, and lies outside A2's own range in manganese and aluminum, on the austenite-favoring side. Section 3.4 examines the window itself by calculation. **[OPEN — FC: (i) how many agent runs; (ii) why A2 rather than the first-ranked family; (iii) how the specific point was chosen, and why it fell outside A2 in Mn and Al. Section 2.1 will carry the decision rule once known.]**

> (b) If the prompt was not repeated, could the authors state this clearly and identify run-to-run stochasticity as an untested limitation …

**[OPEN — FC: was the request repeated?]** If not: "The request was not repeated, and run-to-run variation in the agent's output is stated as untested (Section 4.4)", with the corresponding sentence added to Section 4.4.

> (c) Could the claims be reframed as an exploratory case study of one LLM-assisted hypothesis rather than an evaluation of 'current AI models' as a class?

Yes. Section 4.4 now states that one composition from one session, processed by one route, "is a case study of that composition … and still less an evaluation of AI-assisted alloy design as a practice"; references to "current AI models" as a class have been removed.

> (d) Could the Discussion place the agent's recommendation alongside transparent approaches reported in the recent literature …

Section 1 places LLM hypothesis generation beside property-targeted screening and generative inverse design. Section 4.4 now treats screening against the processing window by equilibrium calculation as an established step in conventional alloy design, which the workflow here omitted. It also adds a comparison with domain-trained language models, tool-using LLM agents and closed-loop studies (see 18c).

### 4. Nominal versus measured chemistry, composition basis, and cost objective

> (a) Could the authors report nominal and measured compositions in both wt.% and at.%, describe the analytical method and sampling location, and state whether the listed values represent one measurement or an average? …

Done. Table 1 now gives every composition in wt% with at% in parentheses. Its caption states the method (ICP-AES, carbon by ASTM E1019), the sampling (LLM-alloy on the finished wire, benchmark as cast), that each value is a single analysis of one sample per heat, and that no analytical uncertainty is reported. The reviewer's conversion is correct: the measured LLM-alloy is 51.5Fe-29.8Mn-11.9Al-4.2Ni-2.0Si-0.45C at%. The paper identifies the alloy by this measured composition throughout, and all calculations use it (Section 2.6).

> (b) What plausible processing or analytical factors could explain the large Si shortfall, and how might the deviation affect phase stability? …

The shortfall is consistent with oxidation loss of silicon during vacuum induction melting (Section 2.1). **[OPEN — SC: any other known cause, e.g. the form in which Si was charged.]** Its effect on phase stability was evaluated by calculation. The nominal composition, with its intended silicon, does not reach single-phase α at 1200 °C either, in the database that carries silicon (Section 3.4). Silicon at its measured level does not obstruct the α field once carbon is removed (Section 4.2). Section 2.1 now states that chemical homogeneity within a heat was not checked.

> (c) Could the authors quantify the raw-material cost reduction …

We make no cost claim. Lower cost was the objective of the request put to the agent, not an outcome we measured or claim; the Conclusions now say so explicitly ("cost was the objective of that request and is not evaluated here"). Because the alloy did not achieve the target property, we have not added a cost estimate, which would compare the price of a material that does not perform.

> (d) How does the unexpected 0.06 wt.% P in the Omori alloy affect the validity of the benchmark …

Section 2.1 reports the phosphorus (0.06 wt%, ≈0.10 at%; source unknown, most plausibly a residual from the melting stock). This is below the level at which grain-boundary embrittlement is normally reported in Fe-Mn austenitic and duplex alloys. Any effect could only degrade the benchmark, which makes the comparison conservative. Phosphorus is included in the calculations wherever the database carries it (mc_fe, Section 2.6). The benchmark is now described as a reference composition processed in parallel (comment 7), so its validity as a reference rests on the transformation it showed under the common route, not on optimized properties.

### 5. Carbon causality and multicomponent phase stability

> (a) Could the authors discuss phase stability using the measured chemistry and the best available thermodynamic and experimental literature? …

Done (Sections 2.6 and 3.4; Tables 3 and 4; Fig. 9). Equilibrium step diagrams were calculated on the measured chemistry in three independently assessed open databases, two of which reproduce the benchmark's single-phase α field without fitting. In all three, the LLM-alloy is α + γ at 1200 °C and begins to melt (≈1240–1295 °C) before any single-phase α field opens. Section 4.2 relates the alloy to the Ni-alloyed Fe-Mn-Al-C low-density steels, whose chemistry it shares.

> (b) In the absence of a compositionally matched carbon-free control, could the authors present carbon as one plausible contributor rather than the demonstrated primary cause of failure?

Yes. We added a virtual carbon-free control: the measured chemistry with carbon removed and every other element held fixed. It opens a single-phase α field at ≈1130–1160 °C in all three databases, and a nickel scan shows that restoring the benchmark's nickel does not open the field while carbon is present (Sections 3.4 and 4.2). On that basis the paper's claim is narrower than "carbon caused the failure": on the calculation, carbon closes the single-phase α field at the solution-treatment temperature. Whether that closure is the operative cause of the null result is left open (Sections 4.1 and 4.2). Casting the carbon-free heat is named as the direct experiment (Sections 4.2 and 4.4).

> (c) Were kappa carbides or other C-bearing phases considered …

Yes, in the calculations: κ-carbide is predicted only below ≈590 °C (≤2.4%), M₂₃C₆ only below ≈420 °C, and neither at or near 1200 °C (Section 3.4). Experimentally the question is unresolved, and the paper now says so: no carbide was detected by diffraction or SEM, which would not resolve a fine dispersion, and κ-carbide was not included in an alternative refinement model (Section 3.3).

> (d) Could the authors discuss the measured alloy using multicomponent thermodynamics rather than relying mainly on general ferrite/austenite stabilizer rules from a steel textbook?

Done. Section 4.1 now states that element-by-element stabilizer rules cannot decide the balance in a six-element alloy and attributes the conclusion to the multicomponent calculation. Section 4.2 shows that a Schaeffler-type nickel equivalent ranks the two alloys the wrong way round, and explains why.

### 6. Processing history and missing heat-treatment details

> (a) Could the authors provide a complete process-flow diagram and tabulated thermal-mechanical history for each tested condition …

Sections 2.1 and 2.2 now give the route: vacuum induction melting (≈2 kg) to ø50 mm ingots, EDM to ø13 mm rods, homogenization at 1000 °C for 16 h in argon, hot rolling at 850 °C in multiple passes, and cold drawing with intermediate anneals at 1000 °C in argon, to 0.36 mm (LLM-alloy) and 0.64 mm (benchmark) wire with ≈85% area reduction after the last process anneal. They also give every final heat treatment, including the cyclic schedules. Table S1 lists the condition of every tested specimen. **[OPEN — SC: hot-rolling reductions and pass schedule, redraw sequence, number and duration of intermediate anneals, cooling media. These go into a process table (Online Resource 2, new Table S3); entries not recorded will be stated as such.]**

> (b) What exactly was the 200 °C/3 h aging sequence in Fig. 2f …

(Now Fig. 2h.) The age followed the 1200 °C/1 min strand anneal (Section 2.2). **[OPEN — SC: quench medium and temperature after the anneal, transfer time, aging atmosphere, cooling after aging.]**

> (c) For the strand furnace, what were hot-zone length, line speed, temperature calibration, wire tension, argon oxygen level, and method used to verify that a 0.36 mm wire experienced the stated dwell temperature?

Line speed was 4 ft min⁻¹. Section 2.2 now states that "1 minute" is the nominal dwell, and that the time at temperature set by speed and hot-zone length was not measured separately, nor was the cooling rate on leaving the furnace. **[OPEN — SC: hot-zone length, temperature calibration, wire tension, argon purity.]**

> (d) Could the authors describe the observed surface condition after treatment, especially at 1200 °C, and discuss oxidation, decarburization, or surface depletion as possible limitations if these were not measured directly?

Treatments above 1200 °C caused severe oxidation and are not reported. Section 2.2 now states that surface oxidation and decarburization during treatments at or below 1200 °C were not measured, and Section 4.3 lists them among the possible causes of the lower elongation above 1000 °C. **[OPEN — FC/SC: any observed surface condition at 1200 °C, if recorded.]**

### 7. Validity of the comparison alloy as a positive functional control

> (a) Why was the key comparison made after 1200 °C/1 min rather than after the full AGG plus optimized aging route reported in the literature?

The heating test was applied to both alloys in the same condition, 1200 °C for 1 minute, the condition used throughout the anneal series. Both alloys were also given the cyclic abnormal-grain-growth treatment (Section 3.5), but the heating test was not applied to the treated material: the treated LLM-alloy rod fractured at 0.5–1.0% elongation, below the 3% loading of the heating protocol, and the treated wire was not tested this way (Section 3.5). We agree that the comparison therefore does not set the LLM-alloy against the benchmark at its best, and have changed the benchmark's description accordingly (below).

> (b) Do the authors have any existing cyclic data showing that the particular Omori-alloy condition used here exhibits superelastic unloading recovery? If not, could it be described more cautiously as a reference composition rather than as a validated positive control?

**[OPEN — FC: confirm that no benchmark cyclic unloading record exists for this condition.]** We have adopted the reviewer's description. Section 2.1 now defines the benchmark as "a reference composition processed in parallel, not a superelastic control whose treatment was optimized"; its transformation under the common route is used only as evidence that the route and tests can detect one. Section 3.2 describes its 0.5% recovery as a single observed heating-induced (shape-memory) recovery, and Section 3.3 now states that the benchmark's transformation rests on three observations, each limited on its own, rather than being "not in question".

> (c) What information is already available on the grain-size-to-wire-diameter ratio, grain morphology/orientation, aging condition, and phase constitution of the benchmark specimen used in Fig. 3? …

The specimen was 0.536 mm wire annealed at 1200 °C for 1 minute, with no aging (Table S1). No micrograph of the benchmark in this condition is reported, so its grain-size-to-diameter ratio, morphology and orientation are known only from the coarse, spotty diffraction of a specimen in the same condition (Fig. 4c). That pattern shows α with γ and B2 reflections; its phase fractions could not be refined. Section 3.3 now states these limitations.

> (d) If the present dataset does not establish a strong positive-control response, could the authors limit the comparison to a 'reference composition processed in parallel' …

Yes; see (b). The Abstract now reads "a benchmark Fe-Mn-Al-Ni alloy processed in parallel".

### 8. Transformation temperatures and phase state at the test temperature

> (a) Are transformation-temperature or phase-state data for these exact conditions already available? …

No transformation-temperature data are available for these conditions, and the manuscript states this (Sections 4.1, 4.4 and 5). The conclusions that would depend on parent-phase stability at room temperature are presented as an open question with two readings (Section 4.1). DSC of the strand-annealed wire, with the benchmark as control, is named as the test that would discriminate between them (Section 4.4).

> (b) Without direct thermal-transformation data, how can the proposed phase-stability explanation be presented as a plausible interpretation rather than a demonstrated mechanism?

It is now presented that way. Section 4.1 concludes that attributing the null result to the missing single-phase parent state is "an interpretation consistent with both readings but established by neither", and the Conclusions place it under "Open".

> (c) Could the authors report the actual laboratory test temperature and thermal history immediately before testing …

**[OPEN — SC/FC: laboratory temperature during testing, and the time and storage between heat treatment and test. If not recorded, Section 2.4 will say "laboratory ambient, not recorded".]**

### 9. Mechanical-test methodology and strain metrology

> (a) Was strain measured with an extensometer, video extensometry/DIC, grip separation, or crosshead displacement? How were machine compliance, grip seating, and slip corrected?

Strain is crosshead extension divided by the instrument gauge length, without extensometry. No correction for load-train compliance or grip slip was applied, so the moduli in Table 2 are apparent. Because crosshead strain over a short gauge is dominated by compliance, elongations measured on different gauges are not compared anywhere in the paper (Section 2.4). The anneal series was tested on a 127 mm gauge (the original "13 mm" was a typographical error).

> (b) Could the authors identify the test standard, frame, load cell, grips, preload, data rate, exact loading/unloading rates, unloading stress threshold, and environmental-temperature tolerance?

Section 2.4 gives the standard (broadly ASTM E8/E8M; the cyclic protocol is the purpose-designed method of our earlier work, Cai et al. 2024), the increment (nominally 1% strain per cycle), and the crosshead speed. **[OPEN — SC / E: drive records: Instron model, load cell, grips, preload, data rate, unloading endpoint (zero load or a set threshold), unloading rate, temperature tolerance.]**

> (c) How were E, 0.2% offset yield strength, UTS, elongation to fracture, recovered strain, residual strain, and hysteresis energy extracted from an incremental cyclic history? …

**[OPEN — FC/SC: how each property was extracted (software or by hand; which loading segment E and σ₀.₂ were taken from).]** Recovered and residual strain are reported only for the heating test, where they are defined in Section 3.2; hysteresis energy is not reported, because no transformation hysteresis was observed.

> (d) Were the Table 2 yield and tensile properties obtained from independent monotonic specimens or extracted from incrementally cycled specimens? …

From the incrementally cycled specimens. **[OPEN — FC: confirm, per Table S1.]** Section 2.4 now says so and identifies the values as protocol-dependent. Section 4.3 compares them with monotonic literature data only with that qualification.

### 10. Experimental scope, specimen count, and level of inference

> (a) How many specimens and independent melts or wire locations were represented for each condition? …

Each alloy is a single heat. Table S1 (Online Resource 2) lists every specimen behind every figure and table, with its heat, form, measured diameter, condition, test, gauge length and count. Every condition of Table 2 is now the mean of three specimens. The aged condition, the prolonged and cyclic conditions, and both heating tests are single specimens, and the text says so where each appears. Each diffraction condition is one specimen, with one or two frames (Section 2.5).

> (b) Where more than one specimen or acquisition was already obtained, could the individual values or observed range be reported? …

Table 2 reports mean ± one standard deviation over three specimens. Each panel of Fig. 2 shows one representative specimen, and the caption says so. Single observations are designated as such.

> (c) Could the authors describe the work explicitly as exploratory screening, replace inferential expressions such as 'threshold' and 'monotonically' with descriptive wording …

Done. Section 4.3 reads the anneal series "as a survey rather than a designed experiment". "Threshold" and "monotonically" have been replaced where they described measured trends, and claims of repeatability are confined to the replicated Table 2 values.

### 11. Interpretation of the loading-unloading-heating experiment

> (a) Could the authors provide a step-by-step control protocol showing whether force, crosshead position, or strain was controlled during heating, and clarify what 'continued to zero strain' means?

Section 2.4 now gives the sequence: the specimen was loaded to 3% strain, unloaded to zero stress, and the crosshead was then returned to its starting position (nominal zero strain); at the same time the specimen was heated to ≈200 °C at ≈50 °C s⁻¹ and held for ≈10 s, then reloaded. **[OPEN — SC: control mode during heating (crosshead position held?), heating method, and how temperature was measured.]**

> (b) How was specimen temperature monitored, what heating/cooling sequence was used, and were fixture expansion or machine compliance corrections applied? …

**[OPEN — SC: temperature monitoring and cooling before reloading.]** No compliance or fixture-expansion correction was applied (Section 2.4).

> (c) If the recorded data permit, could the authors … define exactly how the reported 0.5% recovery was obtained?

The 0.5% is the difference between the residual strain after unloading from 3% (≈2.2%) and the strain at which stress rises on reloading after heating (≈1.7%), as defined in Section 3.2. **[OPEN — SC: whether a temperature–time record exists; if not, Section 2.4 will say so.]**

> (d) Was the recovery observed in more than one cycle or specimen? If not, please describe it as a single observed heating-induced recovery, use 'shape-memory recovery' rather than 'superelasticity,' …

It is a single specimen per alloy (Table S1). Section 3.2 now describes it as "a single observation" of "heating-induced (shape-memory) recovery".

### 12. Scope and limitations of the microstructural evidence

> (a) Could the authors revise the microstructural discussion so that it clearly separates what is directly visible from phase and orientation inferences? …

Section 3.1 now separates what is visible (two constituents of different contrast, their morphology, coarsening with time) from the inferences drawn from them. It does not assign either constituent as the matrix, and names EBSD as the measurement that would settle the remaining questions. Orientation information already available is reported from the synchrotron data: the inverse pole figures of Fig. 7 (Section 3.3).

> (b) How were the quoted grain-size ranges estimated, and how many fields were inspected? …

They are visual estimates from the micrographs, not stereological measurements, and Section 3.1 now says so. **[OPEN — FC: number of fields inspected.]**

> (c) Could the authors report the acquisition conditions and available point or map data underlying the EDS interpretation …

Section 3.1 now states that EDS was used qualitatively, cannot measure carbon, and does not on its own identify crystal structure; the α/γ assignment rests on EDS, diffraction and the calculated partitioning together (Sections 3.1, 3.3 and 3.4). **[OPEN — SC: SEM/EDS acquisition conditions (kV, detector), and whether point or map data exist.]**

> (d) Were micrographs of the AGG-treated wire acquired? …

Yes. Fig. 1d (new) shows the 0.36 mm wire after the cyclic treatment, and Section 3.5 describes the treated rod. **[OPEN — FC: the rod micrographs (arrested coarsening, fine-grain band) and the benchmark bamboo wire are described as "not shown". Recommend adding them to Online Resource 2; otherwise the detailed rod description must be cut back.]**

### 13. Synchrotron geometry and acquisition details

> (a) Could the authors report detector, sample-detector distance, calibration procedure, exposure time, number of frames, specimen-to-beam geometry, background measurement, intensity normalization, and any specimen rotation/translation?

Section 2.5 now reports transmission geometry, a 4288 × 4288-pixel area detector with 100 µm pixels, a sample-to-detector distance of ≈1.83 m (refined to 1827.4 mm), beam centre and distance fitted from the rings themselves with a CeO₂ calibrant frame, and one or two frames per specimen. The exposure normalization of Fig. 6b is stated in its caption. **[OPEN — JY: detector model, exposure time, background measurement, whether the specimen was rotated or translated.]**

> (b) How was overspill from the 0.5 mm beam relative to the 0.36 mm wire handled, and was the same illuminated volume sampled before and after deformation?

**[OPEN — JY.]** Before and after deformation are separate specimens (Section 2.5), so the same volume was not sampled; Section 3.3 now notes that the different grains illuminated in a separate specimen could contribute to the observed changes.

> (c) Were the post-deformation specimens measured under zero load, and at what location relative to the gauge and fracture/plastic-localization region?

Under zero load, after unloading (Section 2.5). **[OPEN — JY/FC: location along the gauge relative to the fracture or neck.]**

> (d) How many specimens, positions, and diffraction acquisitions are represented for each condition? …

One specimen per alloy and condition, at one position, with one or two frames (Section 2.5; Table S1).

### 14. Rietveld refinement, texture, and phase-fraction reliability

> (a) Could the authors report the crystallographic models/space groups, lattice parameters, refined variables and constraints, background/peak functions, texture treatment, Rwp/Rp/chi-squared values, residual curves, and the numerical basis used for the reported phase fractions?

Section 2.5 now reports:
- the three-phase model and space groups, with lattice parameters fixed (values given);
- pseudo-Voigt profiles with a d-dependent Caglioti instrumental function and Popa anisotropic crystallite size;
- interpolated backgrounds, plus a sixth-order polynomial for the deformed pattern;
- the refined variables of each final refinement;
- E-WIMV texture at 2° and 5° ODF resolution.

R_wp and R_p are given in the Fig. 5 caption. We do not quote MAUD's goodness-of-fit value, which its weighting scheme does not make comparable to a conventional χ². The basis of the phase fractions is stated plainly. They were not varied in the final refinements: the undeformed pattern's were held at the values of an earlier refinement stage, and the deformed pattern's are not reported as a measurement. They therefore carry no least-squares uncertainty and are labelled semi-quantitative. **[OPEN — FC/SC: confirm the earlier refinement stage that produced 0.62/0.34/0.04. Residual (difference) curves: MAUD saved neither analysis with its spectra, so Song must re-export observed/calculated/difference curves from the sessions with the .esg data, for a figure in Online Resource 2.]**

> (b) Were the 72 azimuthal spectra refined simultaneously in MAUD to determine an orientation distribution, or were they independently fitted? How were the sector results combined into 62/34/4%?

Simultaneously, with the orientation distribution computed by E-WIMV (Section 2.5). The fractions are those of the whole multi-spectrum refinement, not an average of sector results.

> (c) Given the spotty rings and texture, could the authors discuss the limits of powder averaging and … label the absolute phase fractions as semi-quantitative?

Done. Section 3.3 discusses grain statistics in both alloys: they limit the LLM-alloy refinement and prevent refinement of the benchmark altogether. The fractions are labelled semi-quantitative in the Abstract, Section 3.3, Section 4.1 and the Conclusions.

> (d) Please reconcile the reported composition of approximately 62% FCC + 34% BCC + 4% DO3 on p. 8 with approximately 62% FCC + 37% BCC on p. 10.

Corrected. The refinement gives 62% γ, 34% α and 4% D0₃; "37%" was an error and has been removed.

### 15. What the ex situ diffraction data can and cannot establish

> (a) Could the authors recast the diffraction conclusion as evidence for the retained post-unloading state …

Yes. Section 3.3 now states that an ex-situ measurement after unloading cannot exclude a fully reversible transformation, and that the diffraction is corroboration of the mechanical evidence, not the other way round.

> (b) … could the authors make this limitation explicit throughout the Abstract, Discussion, and Conclusions and avoid excluding a transient reversible transformation?

Done. The Abstract now says "ex-situ", and the Conclusions state that a transformation reversing on unloading is bounded by the unloading curves rather than by diffraction. Those curves return no strain beyond elastic springback in any condition (Sections 3.2 and 3.5). An in-situ measurement is named as the direct test (Section 4.4).

> (c) Do the existing data support a quantitative line-broadening or texture comparison? If not, could dislocation multiplication and subgrain formation be presented as possible interpretations …

No line-profile analysis was made. The spots-to-arcs change is now described as "consistent with" dislocation activity. Sections 3.3 and 4.1 note that it was not quantified and that texture evolution and the different grains sampled could also contribute.

> (d) Why were different maximum strains used for the two alloys, and were intensities normalized …

**[OPEN — FC: why 10% for the LLM-alloy and 8% for the benchmark.]** The benchmark's post-deformation spectrum is divided by 1.625, the exposure ratio recorded with the data, and the Fig. 6 caption now says so; the other spectra are as measured. The before/after comparisons are qualitative, and the text treats them so.

### 16. Identification and role of B2, DO3, and possible carbide precipitates

> (a) What direct evidence in the existing dataset supports the identification and spatial scale of B2, DO3, or carbide-related features? …

The identification rests on superlattice intensities, now quantified in Section 3.3. The D0₃-only {111} reflection is present in the LLM-alloy at a signal-to-noise ratio of 16–27 across four patterns and absent from the benchmark. The B2-allowed {200} reflection in the LLM-alloy is at most ≈0.3 of the benchmark's intensity, and is fully accounted for by D0₃. Spatial scale is not established. Section 3.3 states that transmission electron microscopy or atom-probe tomography would be required, and the assignments are treated as tentative at the nanoscale.

> (b) How unique are the superlattice reflections assigned to B2 and DO3, and were possible overlaps with the FCC/BCC matrix or carbide reflections tested in alternative refinement models?

The {200} position is shared by B2 and D0₃; the {111} reflection is D0₃-only, which is why it is the discriminating measurement (Section 3.3). κ-carbide was not tested in an alternative refinement model, and Section 3.3 now says that its presence at a small fraction is therefore not excluded.

> (c) Is the DO3 phase a coarse constituent, an intragranular precipitate, or an ordering state within the BCC matrix? …

This cannot be decided from the present data. Sections 3.3 and 4.2 now say so and refer to "an ordered D0₃ phase of unknown spatial scale".

> (d) Without direct precipitate evidence, could the authors avoid claiming that the matrix 'lacks sufficient resistance to plastic flow' specifically because B2 is absent?

Done. That sentence has been removed. Section 4.1 now states only that there is no evidence the D0₃ raises the resistance to plastic flow in the way B2 does in the benchmark, and places B2 among several factors that bear on reversibility.

### 17. Overinterpretation of phase stability, recrystallization, and grain growth

> (a) Could the authors replace 'stable state at 1200 °C' with the narrower statement 'retained at room temperature after the stated 1200 °C treatment and cooling' …

Done. The diffraction results are described throughout as the state "as quenched from 1200 °C". Section 4.1 discusses explicitly whether the γ formed at temperature or on cooling, and leaves this open.

> (b) Could the recovery, recrystallization, and grain-growth regimes be presented as interpretations of the mechanical trends …

Done. Section 4.3 now states that microstructures were examined only after the 1200 °C anneals, so the regimes are "interpretations of the mechanical trends rather than observed microstructural stages", and the individual statements are worded as interpretations.

> (c) Could the Discussion consider plausible alternatives for the decrease in elongation above 1000 °C …

Done. Section 4.3 now notes that the decrease (33.0 → 25.6%) exceeds the specimen scatter (one standard deviation ≤1.2%), and that its cause is not identified. Coarsening, surface oxidation or decarburization, quench effects and changes in phase fractions are all possible, and none was measured across the series.

> (d) Please revise the single-phase strength-ductility statement and account explicitly for evolving multiphase fractions, ordering, texture, and prior cold work.

Done. The phrase has been removed. Section 4.3 now states that in this duplex wire, phase fractions, ordering and texture may also change across the series and the effect of prior cold work is not separated, so grain size need not be the only variable.

### 18. Scope of the Discussion and Conclusions on AI-assisted alloy design

> (a) Could the authors rewrite Section 4.3 around the specific failure chain observed here …

Done (now Section 4.4). The section opens by stating the workflow as it was run: the request, the six ranked families, the choice of one, a composition outside its range, and no phase-stability calculation between report and melt. A new paragraph then follows the failure chain link by link.

> (b) Which failure can actually be attributed to the language model, and which may instead arise from synthesis deviation or non-optimized processing? …

The same paragraph answers this directly.

- **The proposal.** The carbon-bearing compositions sampled inside the agent's own window cannot, on calculation, be solution-treated to single-phase α at 1200 °C, so the obstacle is not peculiar to the composition melted. This link is attributable to the model.
- **The human down-selection.** The melt lies outside the window in Mn and Al. That deviation moves the alloy in the observed direction but, on calculation, does not decide the outcome.
- **Synthesis.** Half the silicon was lost, but the nominal composition does not reach single-phase α either.
- **Processing.** The route was not optimized for this composition, and this link remains open.

The omitted screening calculation is attributed to the workflow, not to the model, which recommended it.

> (c) Could the authors compare their workflow with recent studies that use explicit datasets, specialized language models, CALPHAD/physics constraints, quantitative benchmarks, and/or closed-loop experimental validation?

Done. A new paragraph in Section 4.4 compares the workflow with four kinds of approach:
- domain-trained language models with explicit datasets and quantitative test errors (AlloyBERT; AlloyGPT, trained on CALPHAD-generated records);
- LLM agents that call physics tools (AtomAgents, atomistic simulation; an agentic system using Thermo-Calc calculations);
- adaptive and active-learning loops closed on experiment (Xue et al., NiTi-based SMAs, 36 compositions over nine loops; Rao et al., high-entropy Invar alloys);
- data-driven SMA selection confirmed experimentally (the AIMS framework).

In those workflows a calculation or an experiment stands between the proposal and the decision to pursue it. The single-shot, tool-free workflow tested here had no such step. Seven references have been added or cited.

> (d) Please formulate conclusions that remain valid if another processing route were later found to produce superelasticity in this same nominal composition.

Done. The measured conclusions are confined to "the conditions reported". Section 4.1 states that "what is not claimed is that the composition is incapable of superelasticity under any processing". The calculated conclusion, the absence of a single-phase α field in the solid state, is a property of the composition rather than of a route, and is presented as calculated.

> Final Recommendation to the Authors …

We thank the reviewer again. We have made the AI workflow auditable as far as the surviving record allows and stated where it does not; clarified the experimental and processing records; defined the sampling; and separated direct observations from calculated results, interpretations and open questions.

Sincerely,

Frank Y. Cai, on behalf of all authors
School of Engineering Technologies, Purdue University
cai485@purdue.edu
