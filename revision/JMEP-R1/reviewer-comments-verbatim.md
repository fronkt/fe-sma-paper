# JMEP-26-07-50730 — decision and reviewer comments (verbatim)

Source: Gmail, "Journal of Materials Engineering and Performance - Decision on Manuscript ID JMEP-26-07-50730", onbehalfof@manuscriptcentral.com, 2026-10-12 18:37 UTC, to frankyc11223@gmail.com. Copied verbatim below the line. The reviewed version is the **July 2026 submission** ("Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy", `submissions/JMEP/`), not JMEP-26-09-52497.

Related: Vince Katona (ASM, 2026-10-12 18:53 UTC) asks Frank to choose **JMEP-26-07-50730.R1** (revision) **or** JMEP-26-09-52497 (new submission, slower); the other one will be withdrawn.

Decision: reviewers recommend publication with **major revision**. The AE also asks for a professional English edit. Changes must be highlighted (track changes or bold/colour) and a separate response document supplied. The letter says to check the Author Center for reviewer mark-up files that may be too large for email.

---

Associate Editor's Comments to Authors:
Thank you for submitting your manuscript to JMEP. Please address our reviewers' comments. Should you choose to submit a revision, you must highlight all changes made within your revised manuscript upon its return and provide a separate response document. Your response and revision will be re-evaluated by the reviewers and the editors.

Additionally, a revision of the English is recommended. Please enlist the aid of a professional editing service to correct the English. See JMEP author guidelines for examples of such services. It is the author's responsibility to provide a document that is clear and accurate on both technical content and English grammar and construction before the manuscript will be considered for publication in JMEP. We request your cooperation.

## Reviewer: 1

Comments to the Author for Editors review prior to sending
The authors have some interesting results but some further explanations are required for publication.

Put the keywords in alphabetical order

The AI developed alloy was processed in the same way as the established Fe-Mn-Al-Ni alloy to isolate only the effect of composition. However, could the process steps themselves be the reason for not obtaining the shape memory effect? Perhaps the authors should comment on this in the discussion.

Were alternative processing steps tried in order to possibly obtain the shape memory effect?

The AI developed alloy contains additional Si and C as compared to the Omori alloy. Where does this added Si and C appear? In the matrix or in some phases? Or someplace else?

How was the strain rate selected? Are shape memory alloys strain rate sensitive in their shape memory effect?

## Reviewer: 2

Comments to the Author for Editors review prior to sending
Overall Evaluation
The manuscript reports the synthesis and testing of an Fe-Mn-Al-Ni-Si-C wire composition proposed through a Gemini 2.5 Deep Research workflow, with an Fe43.5Mn34Al15Ni7.5 benchmark processed in parallel. The central negative result - the candidate alloy did not show a resolvable superelastic response under the reported conditions - is interesting and worth documenting. The work also has practical strengths: kilogram-scale melting, substantial thermomechanical processing, incremental tensile cycling, a comparison alloy, and access to synchrotron diffraction. A careful negative study could help establish realistic boundaries for using general-purpose LLMs in alloy design.
The present version nevertheless combines an underreported AI workflow with an exploratory experimental dataset. Several conclusions are broader than the design permits. In particular, one unsuccessful, human-selected output from one proprietary agent cannot establish the reliability of LLM alloy design as a class; identical nominal processing does not guarantee comparable or optimal microstructures for two different compositions; and the specific role assigned to carbon is not isolated from simultaneous changes in Fe, Mn, Al, Ni, and Si. The phase and deformation-mechanism interpretations also need more careful qualification. I therefore recommend major revision. Most of the points below can be addressed through fuller reporting of the work already performed, transparent acknowledgment of the study's scope, reanalysis of available data where practical, and conclusions commensurate with the evidence.

Major Comments and Questions

1. Title and scientific framing
The title currently describes the material as a 'Super-elastic ... Alloy,' although the central finding is that it was not superelastic. This is misleading and may cause readers to infer successful property realization. The standard spelling in the field is 'superelastic' rather than 'super-elastic.' The manuscript would also be more precise if it described the material as LLM-proposed or LLM-generated rather than broadly AI-hypothesized.
(a) Could the authors revise the title so that it states that the alloy was targeted for room-temperature superelasticity but failed to exhibit it? One possible formulation is: 'Experimental Evaluation of an LLM-Proposed Fe-Mn-Al-Ni-Si-C Alloy Targeted for Room-Temperature Superelasticity.'
(b) Could the Abstract and Conclusions distinguish clearly among (i) failure of this composition under the tested processing conditions, (ii) limitations of this particular deep-research workflow, and (iii) the much broader performance of AI-assisted alloy design?

2. Reproducibility and correct description of the LLM workflow
The AI method is the manuscript's claimed novelty, yet it is not reproducible. The text also states that the authors 'trained an AI with over 200 published papers,' whereas Section 2.1 describes prompting a pre-trained Gemini 2.5 Deep Research agent. Retrieval, uploaded context, prompt engineering, and model training/fine-tuning are not interchangeable. Recent alloy-specific language-model studies report their datasets, model versions, prompt/input representation, candidate-generation logic, benchmarks, and validation procedures. A proprietary deep-research conversation can still be studied, but its complete audit trail is essential.
(a) Did the authors actually fine-tune or otherwise train a model, upload a closed corpus for retrieval, or simply ask Gemini Deep Research to search public sources? Please replace 'trained' with the technically correct description and specify the workflow architecture.
(b) Could the authors provide, preferably as Supplementary Information, the complete verbatim prompt sequence, date and exact model/product version, settings available to the user, all sources retrieved, the full unedited model response, and the candidate composition ranges proposed?
(c) How were the 'over 200 papers' selected, deduplicated, quality-controlled, and supplied to the agent? Were they actually ingested in the relevant run, and can the list and access method be reported?
(d) Could the authors state which thermodynamic database or computational tool the agent accessed? If no CALPHAD or DFT calculation was actually executed, references to 'thermodynamically screened candidates' should be removed or clearly labeled as literature-based reasoning rather than computed screening.

3. Experimental design does not evaluate general LLM reliability
Only one composition, chosen by the authors from one model-suggested range, was synthesized. This is a legitimate exploratory design, but it supports a single-case appraisal rather than a performance evaluation of LLM alloy design as a class. The manuscript should therefore distinguish the model's proposal, the authors' down-selection, synthesis fidelity, processing choices, and the final experimental outcome.
(a) How many agent runs and candidate compositions were actually generated, and why was this specific point within the proposed range selected? Please disclose the available candidate set and the human decision rule.
(b) If the prompt was not repeated, could the authors state this clearly and identify run-to-run stochasticity as an untested limitation rather than implying that a representative model performance was measured?
(c) Could the claims be reframed as an exploratory case study of one LLM-assisted hypothesis rather than an evaluation of 'current AI models' as a class?
(d) Could the Discussion place the agent's recommendation alongside transparent approaches reported in the recent literature, such as expert selection, literature-nearest-neighbor reasoning, or CALPHAD-informed screening, without requiring a new computational benchmark for this manuscript?

4. Nominal versus measured chemistry, composition basis, and cost objective
The proposed design is specified in at.%, but Table 1 reports only wt.%. More importantly, the measured Si content is 1.11 wt.% rather than the nominal 2.20 wt.%, a deviation of about 50%. Conversion of the reported measured chemistry gives approximately Fe51.5Mn29.8Al11.9Ni4.2Si2.0C0.45 at.% (minor unreported elements excluded), not Fe50Mn30Al12Ni4Si4 plus carbon. Thus, the material that was tested differs materially from the nominated LLM composition. The paper also calls the alloy lower-cost without presenting a cost function or numerical comparison.
(a) Could the authors report nominal and measured compositions in both wt.% and at.%, describe the analytical method and sampling location, and state whether the listed values represent one measurement or an average? If formal uncertainty was not determined, this limitation can simply be acknowledged.
(b) What plausible processing or analytical factors could explain the large Si shortfall, and how might the deviation affect phase stability? Please avoid assuming chemical homogeneity beyond what was actually checked.
(c) Could the authors quantify the raw-material cost reduction using stated prices, date, purity assumptions, and mass basis? Does the comparison include yield losses and any additional processing burden?
(d) How does the unexpected 0.06 wt.% P in the Omori alloy affect the validity of the benchmark, grain-boundary behavior, and mechanical response?

5. Carbon causality and multicomponent phase stability
The manuscript repeatedly assigns the failed transformation primarily to elevated carbon. That interpretation is plausible but is not isolated by the present comparison because Fe, Mn, Al, Ni, Si, and C all change, and the measured Si content also differs substantially from the target. In Fe-Mn-Al-Ni(-C), phase stability and precipitation are strongly coupled. Carbon may stabilize FCC regions and participate in kappa-carbide chemistry, but the available data cannot rank its effect against reduced Ni and Al, added Si, or altered matrix/precipitate partitioning. The main need is therefore to moderate causality rather than to undertake a new alloy series.
(a) Could the authors discuss phase stability using the measured chemistry and the best available thermodynamic and experimental literature? If CALPHAD results already exist, they would be informative; otherwise, a carefully qualified literature-based discussion would be sufficient.
(b) In the absence of a compositionally matched carbon-free control, could the authors present carbon as one plausible contributor rather than the demonstrated primary cause of failure?
(c) Were kappa carbides or other C-bearing phases considered in the existing diffraction or microscopy analysis? If the available resolution cannot establish their presence or absence, please label this aspect as unresolved rather than requiring a definitive phase assignment.
(d) Could the authors discuss the measured alloy using multicomponent thermodynamics rather than relying mainly on general ferrite/austenite stabilizer rules from a steel textbook?

6. Processing history and missing heat-treatment details
The processing route is central to the study but is not sufficiently reproducible. Hot-rolling reductions, pass schedule, redraw sequence, intermediate-anneal duration and frequency, strand-furnace residence control, cooling method, argon purity/flow, and actual specimen temperature are absent. The 200 °C/3 h aged condition shown in Fig. 2f is not defined in Section 2.2. The phrase 'fast cooling' is also insufficient for a quench-sensitive Fe-Mn-Al-Ni system.
(a) Could the authors provide a complete process-flow diagram and tabulated thermal-mechanical history for each tested condition, including reductions, pass temperatures, reheating, intermediate anneals, cooling media/rates, and the final 85% area reduction?
(b) What exactly was the 200 °C/3 h aging sequence in Fig. 2f: preceding solution treatment, quench medium and temperature, transfer time, atmosphere, and cooling after aging?
(c) For the strand furnace, what were hot-zone length, line speed, temperature calibration, wire tension, argon oxygen level, and method used to verify that a 0.36 mm wire experienced the stated dwell temperature?
(d) Could the authors describe the observed surface condition after treatment, especially at 1200 °C, and discuss oxidation, decarburization, or surface depletion as possible limitations if these were not measured directly?

7. Validity of the comparison alloy as a positive functional control
The reference alloy is described as an established superelastic benchmark, but the specific condition compared in Fig. 3 was heat treated at 1200 °C for only 1 min and recovered only about 0.5% on heating after a 3% loading cycle. This is not the large unloading recovery typically associated with a validated superelastic positive control. Because abnormal grain growth, quenching, crystallographic orientation, and low-temperature aging can strongly affect this alloy family, the present sample is best treated as a reference composition processed in parallel unless the authors already possess evidence that this exact condition was functionally optimized.
(a) Why was the key comparison made after 1200 °C/1 min rather than after the full AGG plus optimized aging route reported in the literature?
(b) Do the authors have any existing cyclic data showing that the particular Omori-alloy condition used here exhibits superelastic unloading recovery? If not, could it be described more cautiously as a reference composition rather than as a validated positive control?
(c) What information is already available on the grain-size-to-wire-diameter ratio, grain morphology/orientation, aging condition, and phase constitution of the benchmark specimen used in Fig. 3? Where these quantities were not measured, please state the limitation.
(d) If the present dataset does not establish a strong positive-control response, could the authors limit the comparison to a 'reference composition processed in parallel' and avoid claiming validation against an established superelastic benchmark?

8. Transformation temperatures and phase state at the test temperature
No DSC, dilatometry, electrical-resistance, or thermomagnetic data are reported for the exact tested conditions. Consequently, the transformation temperatures, thermal hysteresis, and parent-phase stability at room temperature remain unknown. This absence does not preclude publication of an exploratory negative result, but it limits how confidently the room-temperature response can be attributed to a particular phase state or transformation pathway.
(a) Are transformation-temperature or phase-state data for these exact conditions already available? If not, could the authors state this explicitly and avoid conclusions that depend on knowing the parent-phase stability at room temperature?
(b) Without direct thermal-transformation data, how can the proposed phase-stability explanation be presented as a plausible interpretation rather than a demonstrated mechanism?
(c) Could the authors report the actual laboratory test temperature and thermal history immediately before testing rather than only 'room temperature'?

9. Mechanical-test methodology and strain metrology
The mechanical results cannot presently be reproduced or evaluated metrologically. The Instron model, load-cell capacity/accuracy, grips, gauge-length definition, strain measurement, sampling rate, preload, unloading endpoint, cycle count, and applicable standard are not given. The statement that the test was run in displacement control does not establish how engineering strain was measured. Crosshead displacement over a 13 mm gauge length can bias modulus and recovery through machine compliance and grip slip, especially for 0.36 mm wire.
(a) Was strain measured with an extensometer, video extensometry/DIC, grip separation, or crosshead displacement? How were machine compliance, grip seating, and slip corrected?
(b) Could the authors identify the test standard, frame, load cell, grips, preload, data rate, exact loading/unloading rates, unloading stress threshold, and environmental-temperature tolerance?
(c) How were E, 0.2% offset yield strength, UTS, elongation to fracture, recovered strain, residual strain, and hysteresis energy extracted from an incremental cyclic history? Please provide definitions and representative construction lines.
(d) Were the Table 2 yield and tensile properties obtained from independent monotonic specimens or extracted from incrementally cycled specimens? If the latter, please identify them as protocol-dependent values and avoid direct comparison with standard monotonic properties without qualification.

10. Experimental scope, specimen count, and level of inference
The manuscript does not state clearly how many specimens, heats, or independent measurements underlie each result, and Section 4.2 describes the dataset as a 'single-specimen survey.' A limited dataset can still be appropriate for an exploratory screening study, especially when kilogram-scale alloy processing and synchrotron access are involved. The presentation should, however, distinguish single observations from repeatable trends and avoid numerical precision or mechanistic generalization beyond the sampling actually performed.
(a) How many specimens and independent melts or wire locations were represented for each condition? Please provide the actual counts, even when n = 1.
(b) Where more than one specimen or acquisition was already obtained, could the individual values or observed range be reported? Where only one observation exists, a transparent n = 1 designation is sufficient.
(c) Could the authors describe the work explicitly as exploratory screening, replace inferential expressions such as 'threshold' and 'monotonically' with descriptive wording, and reserve claims of repeatability for quantities supported by repeated observations?

11. Interpretation of the loading-unloading-heating experiment
The special test is not described clearly enough to distinguish free recovery, constrained recovery stress, thermal expansion, grip slack, and reloading. The sequence 'unloaded to zero stress, and continued to zero strain' is mechanically ambiguous. Figure 3 appears to show a zero-stress horizontal segment followed by reloading, but it does not provide strain-temperature-time or stress-temperature-time histories. Moreover, heating-induced recovery is evidence of a shape-memory response, whereas superelasticity is recovery during unloading at a fixed test temperature.
(a) Could the authors provide a step-by-step control protocol showing whether force, crosshead position, or strain was controlled during heating, and clarify what 'continued to zero strain' means?
(b) How was specimen temperature monitored, what heating/cooling sequence was used, and were fixture expansion or machine compliance corrections applied? If some quantities were not recorded, please state this limitation.
(c) If the recorded data permit, could the authors show or describe the stress-strain-temperature sequence more explicitly and define exactly how the reported 0.5% recovery was obtained?
(d) Was the recovery observed in more than one cycle or specimen? If not, please describe it as a single observed heating-induced recovery, use 'shape-memory recovery' rather than 'superelasticity,' and avoid implying demonstrated repeatability.

12. Scope and limitations of the microstructural evidence
The optical/SEM images show two contrast regions and substantial coarsening, but the evidence is primarily qualitative. Expressions such as 'well under 20 µm' and 'exceeding 100 µm' should be linked to the method actually used to estimate size. Qualitative EDS enrichment does not by itself unambiguously assign A2/BCC and FCC constituents or establish whether grains span the 0.36 mm wire diameter. Crystallographic orientation is important in this alloy family, but it need not be newly measured for this paper if the authors clearly delimit the conclusions that can be drawn without it.
(a) Could the authors revise the microstructural discussion so that it clearly separates what is directly visible from phase and orientation inferences? Please report any grain-size, phase-map, or orientation information already available, without making new EBSD measurements a prerequisite.
(b) How were the quoted grain-size ranges estimated, and how many fields were inspected? If no formal stereological measurement was made, please use approximate qualitative wording.
(c) Could the authors report the acquisition conditions and available point or map data underlying the EDS interpretation, while acknowledging the limitations of EDS for carbon and for definitive phase identification?
(d) Were micrographs of the AGG-treated wire acquired? If not, please state that the AGG microstructure was not directly documented and avoid detailed claims about its grain structure.

13. Synchrotron geometry and acquisition details
The diffraction experiment is underreported. The stated 0.5 × 0.5 mm² beam is larger than the 0.36 mm wire diameter, so part of the beam may miss the specimen or interrogate fixtures/background. Detector type and distance, calibration standard, exposure, transmission/rotation geometry, illuminated gauge location, background subtraction, normalization, and repeat acquisition are not specified. These details matter for comparing intensities and phase fractions before and after deformation.
(a) Could the authors report detector, sample-detector distance, calibration procedure, exposure time, number of frames, specimen-to-beam geometry, background measurement, intensity normalization, and any specimen rotation/translation?
(b) How was overspill from the 0.5 mm beam relative to the 0.36 mm wire handled, and was the same illuminated volume sampled before and after deformation?
(c) Were the post-deformation specimens measured under zero load, and at what location relative to the gauge and fracture/plastic-localization region?
(d) How many specimens, positions, and diffraction acquisitions are represented for each condition? Please identify explicitly when a pattern is based on a single specimen and position.

14. Rietveld refinement, texture, and phase-fraction reliability
The undeformed patterns are strongly spotty and the wires are evidently textured/coarse-grained. Under these conditions, integrated intensities may not satisfy powder-averaging assumptions, and absolute Rietveld phase fractions can be biased by grain statistics and preferred orientation. A recent in situ HE-XRD study on FeMnAlNi explicitly cautions that strong texture can make absolute martensite fractions unreliable. Figure 5 does not show the conventional observed, calculated, background, and difference curves or any fit quality indicators. It is also unclear whether the 72 azimuthal sectors were refined independently or jointly with a texture model.
(a) Could the authors report the crystallographic models/space groups, lattice parameters, refined variables and constraints, background/peak functions, texture treatment, Rwp/Rp/chi-squared values, residual curves, and the numerical basis used for the reported phase fractions?
(b) Were the 72 azimuthal spectra refined simultaneously in MAUD to determine an orientation distribution, or were they independently fitted? How were the sector results combined into 62/34/4%?
(c) Given the spotty rings and texture, could the authors discuss the limits of powder averaging and, if adequate grain statistics cannot be established from the existing acquisition, label the absolute phase fractions as semi-quantitative?
(d) Please reconcile the reported composition of approximately 62% FCC + 34% BCC + 4% DO3 on p. 8 with approximately 62% FCC + 37% BCC on p. 10.

15. What the ex situ diffraction data can and cannot establish
The manuscript appropriately notes that ex situ diffraction after unloading cannot exclude a fully reversible transformation. Nevertheless, later wording treats unchanged peaks as confirmation that stress-induced transformation was inactive and interprets the spot-to-arc evolution as dislocation multiplication and subgrain formation. Peak intensity changes can also arise from texture evolution, specimen positioning, illuminated grain statistics, and variant reorientation. Broadening requires quantitative analysis, while subgrains/dislocations require corroborating microscopy or line-profile evidence. The AI and Omori alloys were also compared after different maximum strains (10% versus 8%).
(a) Could the authors recast the diffraction conclusion as evidence for the retained post-unloading state rather than proof that no transient transformation occurred during loading?
(b) Because new in situ loading measurements are not essential for an appropriately bounded ex situ study, could the authors make this limitation explicit throughout the Abstract, Discussion, and Conclusions and avoid excluding a transient reversible transformation?
(c) Do the existing data support a quantitative line-broadening or texture comparison? If not, could dislocation multiplication and subgrain formation be presented as possible interpretations rather than established observations?
(d) Why were different maximum strains used for the two alloys, and were intensities normalized so that before/after comparisons are quantitative rather than visual?

16. Identification and role of B2, DO3, and possible carbide precipitates
The proposed design specifically targets B2-NiAl/carbide precipitation, and the discussion attributes failure to substitution of B2 by DO3-Fe3Al. Yet precipitate size, morphology, coherency, number density, composition, and matrix partitioning are not measured. Nanometric B2 precipitates that control thermoelasticity may not be reliably quantified from the displayed bulk patterns alone. Moreover, recent Fe-Mn-Al-Ni-based work shows that ordered precipitate chemistry, volume fraction, and stability - and in some modified systems DO3-related precipitation - can have more nuanced effects than a simple B2-good/DO3-bad dichotomy.
(a) What direct evidence in the existing dataset supports the identification and spatial scale of B2, DO3, or carbide-related features? If nanoscale confirmation is unavailable, could these assignments and their proposed roles be described as tentative rather than definitive?
(b) How unique are the superlattice reflections assigned to B2 and DO3, and were possible overlaps with the FCC/BCC matrix or carbide reflections tested in alternative refinement models?
(c) Is the DO3 phase a coarse constituent, an intragranular precipitate, or an ordering state within the BCC matrix? Please align terminology with the spatial scale actually observed.
(d) Without direct precipitate evidence, could the authors avoid claiming that the matrix 'lacks sufficient resistance to plastic flow' specifically because B2 is absent?

17. Overinterpretation of phase stability, recrystallization, and grain growth
Room-temperature ex situ XRD after a 1200 °C treatment does not establish the equilibrium or instantaneous phase state at 1200 °C; the observed mixture may form or change during cooling. Similarly, recovery below 800 °C, an abrupt recrystallization threshold near 800 °C, continuous grain growth from 800 to 1200 °C, and excessive coarsening above 1000 °C are inferred mainly from mechanical-property changes, although micrographs are shown only for 1200 °C at two times. The phrase 'single-phase-controlled structural metal' also conflicts with the explicitly multiphase interpretation.
(a) Could the authors replace 'stable state at 1200 °C' with the narrower statement 'retained at room temperature after the stated 1200 °C treatment and cooling,' because the present ex situ data do not establish the phase state at the treatment temperature?
(b) Could the recovery, recrystallization, and grain-growth regimes be presented as interpretations of the mechanical trends, with clear acknowledgment that microstructures were not measured across the complete 600-1200 °C series?
(c) Could the Discussion consider plausible alternatives for the decrease in elongation above 1000 °C, including surface damage, oxidation, grain-boundary phases, quench effects, or specimen-to-specimen variation, without assigning a unique mechanism from the current data?
(d) Please revise the single-phase strength-ductility statement and account explicitly for evolving multiphase fractions, ordering, texture, and prior cold work.

18. Scope of the Discussion and Conclusions on AI-assisted alloy design
Section 4.3 extrapolates from one unsuccessful candidate to broad limitations of 'available models' and 'current AI models.' The study did not evaluate a trained materials model, calculate model accuracy, compare multiple LLMs, or separate failures of prompt design, retrieval, human selection, synthesis fidelity, thermodynamic screening, and heat-treatment optimization. The negative result remains worthwhile, but it should be presented as a falsified candidate hypothesis and a lesson in workflow verification, not as a statistically supported assessment of AI alloy design.
(a) Could the authors rewrite Section 4.3 around the specific failure chain observed here: model/retrieval proposal, human down-selection, deviation between nominal and realized chemistry, processing, measured phases, and mechanical response?
(b) Which failure can actually be attributed to the language model, and which may instead arise from synthesis deviation or non-optimized processing? Please distinguish these alternatives explicitly.
(c) Could the authors compare their workflow with recent studies that use explicit datasets, specialized language models, CALPHAD/physics constraints, quantitative benchmarks, and/or closed-loop experimental validation?
(d) Please formulate conclusions that remain valid if another processing route were later found to produce superelasticity in this same nominal composition.

Final Recommendation to the Authors
The manuscript contains a valuable idea and a potentially publishable negative result. The most convincing revision would make the AI workflow auditable, clarify the experimental and processing records, define the limited sampling honestly, and separate direct observations from mechanistic hypotheses. An extensive new experimental program is not necessary if the authors appropriately narrow the claims concerning carbon, transformation behavior, precipitates, diffraction mechanisms, and the general reliability of AI-assisted alloy design. With these changes and a transparent account of the available evidence, the study could provide a useful, balanced contribution to the emerging literature on AI-assisted materials design and to the processing-structure-property understanding of Fe-Mn-Al-Ni-based alloys.
