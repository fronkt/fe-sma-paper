# Response to Reviewer 2

**Manuscript:** JMRT-D-26-06169, revised title *Experimental Validation of an LLM-Hypothesized Fe-Mn-Al-Ni-Si-C Alloy: Phase Stability Governs the Absence of Super-elasticity* (submitted as *Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy*)

We thank the Reviewer for a thorough, well-organized review. All twenty-four points have been acted on, and three of them are now the title of the paper. Section and figure numbers below refer to the revised manuscript; the revision adds Secs. 2.6, 3.4 and 3.5 and three figures (Figs. 7–9), so some numbering has shifted.

---

## Title

**Comment 1.** *Suggestion and consider specifying "LLM-hypothesized" instead of the broader term "AI-hypothesized" for greater precision.*

**Comment 2.** *Adding the phrase "experimental validation" would better reflect the manuscript's main contribution.*

**Comment 3.** *The title is technically appropriate but could highlight the role of phase stability in the observed mechanical response.*

**Response (1–3).** All three are adopted together: *Experimental Validation of an LLM-Hypothesized Fe-Mn-Al-Ni-Si-C Alloy: Phase Stability Governs the Absence of Super-elasticity*. This also repairs a defect in the submitted title, which could be mis-parsed as claiming the alloy *is* super-elastic. The test alloy is renamed the "LLM-alloy" throughout and the reference alloy the "benchmark alloy"; "AI-guided alloy design" is kept as a keyword, being the accepted name of the field.

## Abstract

**Comment 1.** *The novelty of experimentally validating an LLM-generated alloy should be stated more explicitly.*

**Response.** Stated in the abstract's second sentence: "the first experimental test of an LLM-hypothesized shape memory alloy carried from proposal through processing to mechanical and synchrotron characterization." The Introduction's gap statement is sharpened to match.

**Comment 2.** *Quantitative mechanical results (e.g., recoverable strain or yield strength) should be included to support the conclusions.*

**Response.** Added on both sides of the comparison: 0.2% proof stress from 1908 to 519 MPa across the anneal series and elongation peaking at 33%; strain recovery indistinguishable from elastic springback against ≈0.5% recoverable transformation strain in the benchmark; single-phase α at ≈1340 °C versus ≈1150 °C once carbon is deleted, and a ≈0.10 wt% carbon threshold against 0.010 wt% in the benchmark.

**Comment 3.** *The influence of carbon on phase stability should be briefly justified rather than only suggested.*

**Response.** In the submitted abstract the carbon claim was asserted; it is now justified by calculation. The abstract gives the mechanism and its basis: equilibrium CALPHAD across three independent databases, validated against the benchmark, shows the benchmark solution-treating to single-phase BCC α at 1200 °C while the LLM-alloy is two-phase there and reaches single-phase α only at ≈1340 °C, and deleting carbon alone lowers that field to ≈1150 °C. Full analysis in Secs. 2.6 and 3.4 (Fig. 9, Table 3), with the causal claim elsewhere tempered to what the calculation supports.

**Comment 4.** *The abstract should briefly explain why the benchmark alloy exhibits super-elasticity while the AI alloy does not.*

**Response.** The abstract now explains it through phase stability: the benchmark reaches the single-phase BCC α parent at 1200 °C; the LLM-alloy cannot reach it within its processing range, so the parent state on which stress-induced transformation depends is unavailable. The role of the coherent B2 precipitates within that parent is developed in Secs. 3.4 and 4.1.

## Introduction

**Comment 1.** *The literature review should include more recent studies on AI-driven alloy design beyond LLM applications.*

**Response.** The opening now surveys the family: property-targeted screening over databases and surrogate models (the AIMS framework for shape memory alloys), generative inverse design, and LLM-based hypothesis generation, alongside the GNoME-scale prediction work already cited. It closes on what they share — a composition that has never been made.

**Comment 2.** *The scientific gap between computational alloy prediction and experimental validation should be better defined.*

**Response.** A dedicated gap paragraph now follows (Sec. 1): generating candidates is cheap, testing one is not and is correspondingly rare, and publishing a candidate that *failed* is rarer still. It also names the specific technical gap — models that optimize thermodynamic stability need not check that the required phase fields are reachable by any route the laboratory can run.

**Comment 3.** *The rationale for selecting this specific alloy composition should be explained more thoroughly.*

**Response.** Treated at three levels. Sec. 1 states the agent's hypothesis in its own terms (reduced Ni for cost, Si to stabilize the α parent, ≈1000 ppm C for interstitial strengthening, no bamboo structure required). Sec. 2.1 documents its provenance — Hypothesis A2, ranked joint second of six families, its composition window, and the fact that the melt lies outside that window in Mn and Al, a deviation then tested by calculation in Sec. 3.4. Sec. 2.1 also places the composition in the literature it actually sits in, the Ni-alloyed Fe-Mn-Al-C low-density steels.

**Comment 4.** *The research objectives and hypotheses should be clearly stated at the end of the introduction.*

**Response.** Done. The Introduction now ends on the hypothesis paragraph and an explicit objective: "to determine not merely whether that hypothesis holds but where precisely it fails: Secs. 3.1–3.3 establish what the alloy did, Secs. 3.4 and 4.2 establish why, and Sec. 4.4 asks what a design workflow would have had to do differently." This replaces a closing sentence another reviewer identified as overclaiming.

## Experimental procedure

**Comment 1.** *The alloy design workflow generated by the LLM should be described in sufficient detail to ensure reproducibility.*

**Response.** Sec. 2.1 now gives the agent and configuration (Gemini Deep Research), the report's compilation date (4 June 2025), its sources (76, accessed 19 May 2025), its six candidate families and their ranking, the composition window of the hypothesis selected, and its performance target (5–8% recoverable strain at 400–700 MPa). The entire 41-page report is supplied as **Supplementary Material**, so the reader has the generative artifact itself. One element is unrecoverable and the revision says so: the verbatim prompt was not preserved and the report does not embed it.

**Comment 2.** *Standard No. of tensile test must be mentioned.*

**Response.** Sec. 2.4 now states this. Specimen handling and the monotonic-tension elements broadly follow ASTM E8/E8M; the cyclic protocol is not a standardized test but a purpose-designed method for fine superelastic wire, cited to the publication describing it on the same apparatus and gauge (Cai et al., *Shape Mem. Superelasticity* 10 (2024) 460–472). ASTM F2516 is deliberately not cited: it prescribes a different cycle for NiTi and would misdescribe what was done. Sec. 2.4 also gives the parameters — displacement control, 127 mm gauge, 0.25 in min⁻¹ (8.3 × 10⁻⁴ s⁻¹), strain from crosshead extension without extensometry, so the moduli are apparent rather than true.

**Comment 3.** *Statistical repeatability of the mechanical tests should be reported.*

**Response.** Based on the Reviewer's comment, we carried out additional heat treatments and tensile testing so that every condition is now replicated. Table 2 is updated: each entry is the mean of three specimens with one standard deviation, and the caption states that each data point is the average of three samples (Sec. 2.4 reports the same). The replicates confirm the sweep rather than change it — every ranking is preserved and the largest relative standard deviation is ≈6.5%, against a ≈3.7× range in strength and ≈16× in elongation. Where scatter is itself informative it is reported as such: it is large in the abnormal-grain-growth condition, and Sec. 3.5 reads it as evidence of boundary cracking.

## Results and Discussion

**Comment 1.** *The discussion should quantitatively correlate phase fractions with the observed mechanical behaviour.*

**Response.** Sec. 4.1 now makes the correlation explicit in three steps. A structure that is ≈62% γ is mostly the *product* phase of this family's transformation (parent BCC α → martensite FCC γ, now spelled out in Sec. 3.3), leaving the ≈34% α as the only parent available. The calculated 1200 °C equilibrium (62–71% α, Table 3), inverted against the measured quenched state, indicates a partial α → γ transformation ran on cooling. The yield strengths of Table 2 (≈520–675 MPa) then set the stress at which slip in the majority γ preempts transformation of the α it surrounds. The ≈4% D0₃ correlates negatively: as a bulk constituent rather than a coherent dispersion it supplies none of the slip resistance nanoscale B2 supplies in the benchmark.

**Comment 2.** *The proposed role of carbon in suppressing super-elasticity should be supported by thermodynamic calculations.*

**Response.** This is the largest single addition to the revision. New Secs. 2.6 and 3.4, with Fig. 9 and Table 3, give equilibrium CALPHAD step diagrams for both alloys from 400 to 1400 °C, computed from the measured chemistries in three independently assessed open databases and validated against the benchmark, whose single-phase α field and ≈20% ordered bcc they reproduce without fitting. The carbon result comes from a virtual control — the measured chemistry with carbon deleted — now plotted as **Fig. 9c** beside the measured composition so the restored α field can be read directly. All three databases agree: ≈0.10 wt% carbon moves the α solvus by ≈190 °C, the difference between a solution treatment that cannot be run and one that can. A nickel scan separates the other suspect element cleanly — nickel does not move the solvus; it controls the amount of ordered bcc.

**Comment 3.** *Fig. 2 is small and unclearly.*

**Response.** Fig. 2 has been rebuilt from the raw Instron records rather than rescaled: eight panels at 600 dpi at column width, uniform axes, legible ticks (the submitted version clipped "2.5" to "2."). The caption now states what stress and strain are computed from, including the measured per-spool diameters and the 127 mm gauge.

**Comment 4.** *Fig. 2 e, should be presented and discussed.*

**Response.** Done, and the defect was broader: the submitted text referred to no Fig. 2 panel by letter and showed six of the eight Table 2 conditions. The rebuilt figure presents all seven annealed conditions plus the aged one, (a)–(h), and Sec. 3.2 walks through them, including the panel named — 1000 °C, where yielding falls to ≈675 MPa and the series reaches its elongation peak. The narration closes on the feature common to all eight: every unloading segment is straight, parallel to the elastic line, and returns no strain beyond σ/E.

**Comment 5.** *The implications of this negative result for future AI-assisted alloy design deserve deeper discussion.*

**Response.** Sec. 4.4 is substantially expanded, and the new calculations turn a general caution into a concrete prescription: an equilibrium step diagram evaluated not for whether the desired phase exists but for whether the phase fields the *intended route* requires overlap the temperatures at which that route can be run. It also records that the agent's own report recommended CALPHAD screening without performing it — placing the failure in the workflow's termination rather than the model's knowledge — and bounds the scope explicitly to one composition, one session, one route.

**Comment 6.** *Is there any formation Martensite phase in microstructure, this should be present and discuss.*

**Response.** The submitted manuscript never stated what "martensite" *is* in this family, whose convention is the reverse of that familiar from carbon steels; Sec. 3.3 now says so explicitly — the parent is BCC α and the martensite formed from it is FCC γ, so an alloy rich in γ has *less* parent available to transform, not more. On the direct question: the refinement resolved γ, α and D0₃ Fe₃Al and nothing else, with no ε-HCP or α′ needed to fit any pattern from either alloy, and the γ in the annealed LLM-alloy is thermally stable retained γ, unchanged by 10% deformation (Figs. 4a–b, 6a). Secs. 3.1 and 4.1 go one step further in the direction the question points: the lath-like morphology of Fig. 1d and the inversion between the calculated α-majority equilibrium and the measured γ-majority state both suggest part of the γ formed thermally on cooling, i.e. the martensite start lies above room temperature. Calorimetry is named as the confirming experiment.

## Conclusion

**Comment 1.** *The conclusions should distinguish experimental observations from the authors' interpretations.*

**Response.** The Conclusions are restructured to enforce the separation: an observation paragraph ("What was observed is the following" — castability, the 1908→519 MPa sweep, the 33% elongation peak, no departure from elastic springback in any condition, the benchmark's ≈0.5% recovery, the diffraction results), then a separate interpretation paragraph, then the calculation-based diagnosis with its evidential status stated, and finally three limitations.

**Comment 2.** *Emphasize the broader implications for AI-assisted materials discovery rather than this alloy alone.*

**Response.** The Conclusions now state it as a transferable procedure rather than a sentiment: screen LLM-proposed compositions for competing phase stability and interstitial content before synthesis, by an equilibrium calculation checked against the intended route's temperature window. We should be transparent that another referee pressed in the opposite direction, toward narrowing the paper to an alloy case study. The revision splits the claim: the *experimental* findings are bounded as a case study, while the *methodological* claim, resting on the diagnosis rather than the sample size, is retained and emphasized as the Reviewer asks.

**Comment 3.** *Discuss the limitations of relying solely on LLM-generated compositions.*

**Response.** The limitations paragraph now names the specific limitation this case demonstrates: composition-only reasoning is blind to the distinction that decided it — not whether a phase is stable, but whether the temperature at which it becomes stable can be reached in the available equipment. An LLM reasoning from literature correlations has no reliable way to represent that constraint, and instructing it to consult thermodynamic data did not supply one: its report recommended CALPHAD screening without performing it.

**Comment 4.** *Include recommendations for integrating thermodynamic screening into AI-guided alloy design.*

**Response.** Adopted, and now demonstrated rather than merely recommended. Sec. 4.4 specifies the screen concretely — the two-part step-diagram test against the processing window, requiring no proprietary software and no measurement on the candidate itself. Sec. 4.2 shows it operating on this alloy, rejecting the composition where the intended 1200 °C treatment is found to lie ≈140 °C below the single-phase field. The abstract's final sentence carries it in one line.

---

We thank the Reviewer again; the twenty-four comments were unusually actionable, and the manuscript is measurably better for all of them.
