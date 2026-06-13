---
title: "Limited Room-Temperature Pseudoelasticity in an AI-Hypothesized Fe-Mn-Al-Si-Ni-C Alloy: Synthesis, Microstructure, and Cyclic Response"
author:
  - Frank Cai^1^
  - S. Cai^2^
  - J. Yan^3^
affiliations:
  - "^1^Homestead Senior High School, Fort Wayne, Indiana, United States"
  - "^2^Fort Wayne Metals, Fort Wayne, Indiana, United States"
  - "^3^Shanghai Synchrotron Radiation Facility, Shanghai, China"
corresponding: "Frank Cai, frankyc11223@gmail.com"
keywords:
  - Fe-based shape memory alloy
  - Pseudoelasticity
  - AI-guided alloy design
  - Synchrotron XRD
  - Abnormal grain growth
target_journal: Shape Memory and Superelasticity (Springer)
---

# Abstract

Iron-based shape memory alloys (Fe-SMAs) are a promising low-cost alternative to Nitinol for civil-infrastructure and biomedical applications, but their pseudoelastic response is sensitive to composition and processing in ways that remain difficult to predict in advance. Large language model (LLM) deep-research agents, coupled with thermodynamic-stability databases, can now propose candidate compositions in seconds, which raises the practical question of whether such proposals survive physical synthesis. Here we report what may be the first synthesis and mechanical characterization of a novel Fe-Mn-Al-Si-Ni-C composition hypothesized by an LLM deep-research agent, benchmarked against the established Omori Fe-Mn-Al-Ni alloy processed under identical conditions. The AI-hypothesized alloy was readily castable and thermodynamically stable, yet it exhibited essentially zero room-temperature pseudoelastic recovery across all four heat treatments examined; the benchmark, by contrast, showed a reversible response associated with stress-induced α↔γ activation. Synchrotron X-ray diffraction at the Shanghai Synchrotron Radiation Facility indicated that the AI alloy consisted of coexisting γ-FCC austenite and an ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix that pseudoelasticity requires, and its diffraction pattern was essentially unchanged by 10% applied strain. These observations suggest that the deformation is accommodated largely by dislocation slip, and that AI-guided composition proposals may benefit from explicit screening for competing phases and interstitial effects before synthesis. A secondary, more tentative observation from the benchmark alloy is that higher-feed-rate continuous strand annealing may yield refined-grain microstructures with improved pseudoelastic recovery; this would warrant systematic study.

**Keywords:** Fe-based shape memory alloy; pseudoelasticity; AI-guided alloy design; synchrotron XRD; abnormal grain growth

---

# 1. Introduction

## 1.1 Motivation: low-cost shape memory alloys

Shape memory alloys (SMAs) exhibit reversible martensitic transformations that enable two technologically important behaviors: the shape memory effect, in which thermally induced phase changes recover macroscopic deformation, and pseudoelasticity (superelasticity), in which stress-induced martensite reverts upon unloading [@otsuka2005physical; @lagoudas2008shape]. Nitinol (Ni-Ti) is the dominant commercial SMA, with recoverable strains of 6–8%, excellent cyclic stability, and biocompatibility, and it accounts for the majority of SMA use in medical devices, aerospace actuators, and damping applications [@duerig1999overview; @mohd2014nitinol]. However, Nitinol is expensive: titanium extraction is energy-intensive, and high-quality SMA wire requires vacuum-arc or vacuum-induction processing to avoid embrittling oxide and nitride phases [@otsuka2005physical].

Iron-based shape memory alloys offer a path to lower cost. Iron is one of the most abundant metals in the Earth's crust, and Fe-SMA processing can in principle leverage established steel-industry infrastructure (electric-arc melting, hot rolling, strand annealing) without strict vacuum requirements [@omori2011superelastic; @abuzaid2019femnnial]. Replacing scarce alloying elements with abundant Mn, Al, Si, and minor Ni may reduce both raw-material and processing costs [@omori2017martensitic]. The lower modulus and higher damping capacity of Fe-SMAs also make them attractive as structural-engineering prestressing tendons for concrete and as seismic dampers, applications where Nitinol's price has historically been prohibitive [@cladera2014ironbased].

## 1.2 The Omori benchmark

The work that established polycrystalline Fe-SMAs as practical materials was Omori *et al.*'s 2011 demonstration of room-temperature superelasticity in Fe-Mn-Al-Ni following abnormal grain growth (AGG) [@omori2011superelastic]. A central microstructural feature of that work was *bamboo-like* grains, single-crystal-diameter grains spanning the wire cross-section, produced by cyclic heat treatments across the γ↔α phase boundary. Subsequent studies have associated such large grains with reduced inter-granular constraint and improved transformation reversibility in the BCC α / FCC γ system [@vollmer2016cyclic; @abuzaid2019femnnial]. We adopt this alloy, processed under matched conditions, purely as a benchmark against which to interpret the AI-hypothesized composition.

## 1.3 AI-guided alloy discovery and the prediction–processability question

Materials discovery has been reshaped by deep-learning models trained on first-principles thermodynamics. DeepMind's GNoME predicted more than 2.2 million previously unreported crystal structures with high precision against DFT validation [@merchant2023gnome], and agentic large language models with deep-research capabilities can ingest decades of metallurgical literature and propose novel compositions in seconds [@xu2025deepresearch; @comanici2025gemini]. Together these tools point toward alloy design that moves from intuition-guided iteration toward AI-proposed, thermodynamically screened candidates.

An open practical question is whether such AI-proposed compositions survive contact with physical processing. Current generative materials models typically optimize for thermodynamic stability (formation energy, convex-hull distance) but do not, in general, explicitly model the kinetic barriers governing which phases actually form during quenching and annealing, the interstitial chemistry arising from realistic carbon contents, or the processing-rate constraints that shape grain morphology [@merchant2023gnome]. A composition whose target phase lies on the DFT convex hull might still be difficult to realize in practice. To our knowledge this question has not previously been examined for an LLM-hypothesized SMA composition.

## 1.4 Aim and expectations

This work addresses a primary question and a secondary, exploratory one:

1. **Pseudoelastic response of an AI-hypothesized alloy.** When an LLM deep-research agent proposes a novel Fe-Mn-Al-Si-Ni-C composition targeting room-temperature pseudoelasticity, does the synthesized alloy exhibit that behavior, and if not, what microstructural features appear to be responsible?
2. **Processing observation in the benchmark (exploratory).** As a side observation in the Omori benchmark, we examine whether continuous strand annealing at higher feed rates might produce refined-grain microstructures with pseudoelastic recovery comparable to, or better than, slower treatments.

Our expectation at the outset was that the AI-hypothesized alloy would be thermodynamically stable per first-principles data but might nonetheless fail to show pseudoelasticity owing to process–structure–property couplings that are not captured by formation-energy optimization. The results below are broadly consistent with that expectation, although they should be read as a single case study rather than a general conclusion.

## 1.5 Contributions

This work reports what we believe to be the first physical synthesis and mechanical characterization of an Fe-SMA composition hypothesized by an LLM deep-research agent, benchmarked directly against the Omori reference alloy under identical processing. Prior AI-driven SMA work has used graph neural networks, Bayesian materials selection, and GAN-based inverse design, largely on NiTi-family alloys [@aims2022; @generativeinversion2025], and LLM-hypothesized compositions have been explored for high-entropy alloys and halide solid electrolytes [@hu2024beyond]; the intersection of LLM deep-research alloy design and Fe-based SMA synthesis appears not to have been reported previously. We also note, cautiously and as a secondary observation, that continuous strand-anneal processing rate may influence pseudoelastic recovery in the benchmark alloy.

---

# 2. Materials and Methods

## 2.1 Alloy design

The AI-hypothesized composition was generated by an LLM deep-research agent (Gemini 2.5 with the Deep Research tool [@comanici2025gemini]) prompted to propose an Fe-Mn-Al-based composition optimized for room-temperature pseudoelasticity. The agent was instructed to (i) reason from the Fe-Mn-Al-Ni family established by Omori and co-workers [@omori2011superelastic; @omori2017martensitic] as a starting point, (ii) consult thermodynamic-stability data, (iii) target β-NiAl/carbide precipitation as a strengthening pathway, and (iv) minimize cost by excluding cobalt and tantalum. The agent's output, after constraint-prompted refinement, is the composition designated here as the "AI alloy."

For direct benchmarking, a second composition based on the Omori Fe-Mn-Al-Ni reference [@omori2011superelastic] was synthesized under identical conditions. Both compositions are listed in **Table 1**.

**Table 1.** Target chemical compositions of the AI-hypothesized and Omori-benchmark alloys (wt%).

| Element | AI alloy (697-6 / 697-7) | Omori benchmark |
|---------|--------------------------|-----------------|
| Fe      | balance                  | balance         |
| Mn      | 31.78                    | 36.49           |
| Al      | 6.24                     | 8.00            |
| Si      | 1.11                     | —               |
| Ni      | 4.81                     | 8.94            |
| P       | —                        | 0.062           |
| C       | 0.105                    | 0.010           |

## 2.2 Synthesis

Alloy ingots were produced by arc-melting elemental constituents of nominal purity ≥99.9% under an argon atmosphere. Each ingot was inverted and remelted a minimum of five times to ensure compositional homogeneity. Following arc melting, ingots were hot-rolled at 850 °C in multiple passes to reduce thickness, and subsequently cold-drawn to a final wire diameter of 0.014 in. (≈0.36 mm). Severe work hardening during cold drawing necessitated intermediate annealing at 900–1000 °C under flowing H₂/Ar to restore ductility between draw passes.

Surface oxidation during high-temperature processing was mitigated by encapsulating samples in evacuated quartz tubes prior to anneal cycles. For samples that experienced oxidation despite encapsulation, a dilute acid bath was used to chemically strip the oxide layer before mechanical testing.

## 2.3 Heat treatments

Four distinct heat-treatment conditions were applied across the two alloys to probe the microstructural and pseudoelastic response (**Table 2**).

**Table 2.** Heat-treatment conditions.

| Condition | Description | Applied to |
|-----------|-------------|------------|
| Standard anneal | 1200 °C / 1 min, water quench | AI, Omori |
| 3-cycle AGG     | (1200 °C / 30 min + RT / 10 min) × 3, followed by 1200 °C / 1 h, water quench | AI, Omori |
| Strand anneal, low FPM | Continuous strand furnace, 1200 °C, 0.8 ft/min throughput | AI, Omori |
| Strand anneal, high FPM | Continuous strand furnace, 1200 °C, 4 and 20 ft/min throughput | AI, Omori |

The 3-cycle AGG condition follows the abnormal-grain-growth protocol of Omori *et al.* [@omori2011superelastic], designed to produce bamboo-like single-crystal-diameter grains. The strand-anneal conditions span low-to-high continuous feed rates (0.8, 4, and 20 ft/min) and are intended to probe the range over which conventional industrial throughputs might replace the slow batch AGG cycle.

## 2.4 Metallography

Wire cross-sections were embedded in cold-mount epoxy and ground sequentially with silicon-carbide papers from 180 grit through 800 grit. Final polishing used a 0.25 µm OP-S aluminum-oxide suspension on an automated polishing wheel until a scratch-free mirror finish was achieved. Polished cross-sections were imaged on a Clemex Vision PE optical microscope under bright-field illumination at magnifications between 100× and 1000×.

## 2.5 Mechanical testing

Cyclic tensile tests were performed on an Instron servohydraulic testing frame in displacement control. Wire specimens were tested with a 6 mm gauge length using pneumatic grips. Each specimen was loaded to a target tensile strain (8% for the Omori benchmark, 10% for the AI alloy) at a nominal strain rate of 1 × 10⁻³ s⁻¹, held briefly at peak strain, and then unloaded to zero force. Pseudoelastic recovery was quantified as the ratio of recovered strain on unloading to applied peak strain.

## 2.6 Synchrotron X-ray diffraction

Synchrotron XRD measurements were performed at the ultra-hard X-ray multifunctional application beamline BL12SW of the Shanghai Synchrotron Radiation Facility (SSRF) [@ssrf2024bl12sw], in collaboration with co-author J. Yan. The incident wavelength was λ = 0.125870 Å (photon energy ≈98.5 keV), and the sample-to-detector distance was 1827.486 mm with a 100 µm × 100 µm pixel area detector. Two-dimensional Debye–Scherrer patterns were collected from each specimen before and after tensile deformation to test for a stress-induced phase transformation. Each 2D pattern was azimuthally integrated to produce a one-dimensional intensity-versus-2θ profile, and reflections were indexed by comparison with reference Fe, Fe-Al, and γ-austenite phases.

---

# 3. Results

## 3.1 Microstructure

Optical micrographs of polished wire cross-sections for the four most informative heat-treatment conditions are shown in **Fig. 1**.

After the standard 1200 °C / 1 min anneal, the AI alloy (**Fig. 1a**) exhibits a highly refined dual-phase morphology with irregular grain boundaries and no single dominant phase. Following the 3-cycle AGG treatment (**Fig. 1b**), the AI alloy continues to show a dual-phase structure: grain growth occurred only in one of the two phases, while the second phase remained as fine, dispersed regions. The dual-phase character persisted across every AI-alloy condition examined, which suggests that the AI's predicted composition did not support single-phase austenite formation under any of the heat treatments tested in this study.

The Omori benchmark behaves differently. After 3-cycle AGG (**Fig. 1c**), it develops the bamboo-like grain morphology consistent with the established Fe-Mn-Al-Ni literature [@omori2011superelastic; @vollmer2016cyclic], with grain diameters spanning a substantial fraction of the wire cross-section. The 1200 °C / 1 min condition (**Fig. 1d**) yields an acicular ferrite microstructure.

![**Fig. 1.** Optical micrographs of polished wire cross-sections under four representative heat-treatment conditions. (a) AI alloy after the standard 1200 °C / 1 min anneal: highly refined dual-phase morphology with irregular grain boundaries (scale bar 0.004 in.). (b) AI alloy after 3-cycle AGG: grain growth in one phase only; the dual-phase structure persists (scale bar 400 µm). (c) Omori benchmark after 3-cycle AGG: bamboo-like grain morphology (scale bar 200 µm). (d) Omori benchmark after 1200 °C / 1 min strand anneal: acicular ferrite microstructure (scale bar 200 µm). All images acquired on a Clemex Vision PE optical microscope under bright-field illumination.](figures/Fig2_microstructure_composite.png)

## 3.2 Cyclic stress–strain response

Cyclic tensile stress–strain curves for representative specimens are shown in **Fig. 2**.

The AI alloy in both the 1200 °C / 1 min (**Fig. 2a**) and 3-cycle AGG (**Fig. 2b**) conditions displays essentially zero pseudoelastic recovery on unloading. Loading exhibits a monotonically rising stress with no defined transformation plateau, and unloading retraces a near-linear-elastic slope down to negligible recovered strain. This macroscopic behavior is consistent with plastic deformation by dislocation slip rather than stress-induced martensitic transformation (SIMT), and it was observed across all AI-alloy heat treatments examined.

The Omori benchmark shows the expected pseudoelastic response in the conditions that develop bamboo or refined-grain microstructures (**Fig. 2c, d**). As a secondary observation, the 1200 °C / 12 s strand-anneal condition (refined small grains) appears to recover roughly twice the strain of the 1200 °C / 5 min condition under the same applied strain. We treat this comparison cautiously, as it rests on a small number of specimens; it is considered further in Sec. 4.3.

![**Fig. 2.** Cyclic tensile stress–strain response. (a) AI alloy after the standard 1200 °C / 1 min anneal: monotonic loading with no transformation plateau and essentially zero recoverable strain on unloading, consistent with dislocation slip. (b) AI alloy after 3-cycle AGG: response qualitatively identical to (a), indicating that AGG processing did not restore pseudoelasticity in the AI composition. (c) Omori benchmark after 1200 °C / 5 min strand anneal: partial pseudoelastic recovery with developing hysteresis. (d) Omori benchmark after 1200 °C / 12 s strand anneal (refined small-grain microstructure): pronounced pseudoelastic hysteresis and a distinct stress plateau. Red arrows in (c, d) mark the residual unrecovered strain after unloading.](figures/Fig3_stressstrain_composite.png)

## 3.3 Synchrotron diffraction and phase identification

Azimuthally integrated synchrotron XRD patterns are shown in **Fig. 3** for the AI alloy and the Omori benchmark before and after deformation.

The AI alloy (**Fig. 3a**) exhibits a multi-peak pattern indexable to coexisting FCC γ-austenite and an ordered B2/DO₃ Fe₃Al phase. Comparison of the 0% and 10% strain patterns shows that peak positions and relative intensities are essentially unchanged: no new reflections appear, none disappear, and the dual-phase signature is preserved. This is a direct, diffraction-level indication that the macroscopic strain in **Fig. 2a, b** is accommodated by dislocation slip rather than by a phase transformation. The presence of an ordered B2/DO₃ Fe-Al phase, rather than the single transforming matrix that pseudoelasticity requires, is consistent with the absence of recovery; this competing B2/Fe-Al phase is thermodynamically favorable for the alloy's reduced chemistry, and a modest carbon content can further stabilize BCC/B2 over FCC austenite [@zener1948; @bhadeshia2010steels].

The Omori benchmark (**Fig. 3b**) presents a BCC α-dominated pattern with ordered β-NiAl (B2) precipitate reflections in the undeformed state. After 8% applied strain, the {111}γ reflection intensifies and the overlapping {200}α / {200}B2 cluster redistributes in intensity, consistent with stress-induced γ formation and partial variant activation.

![**Fig. 3.** Azimuthally integrated synchrotron XRD patterns comparing the undeformed (0% strain) and deformed (post-tensile-test) states. (a) AI alloy: pattern indexable to coexisting FCC γ-austenite ({111}γ, {200}γ, {220}γ) and ordered B2/DO₃ Fe₃Al phase ({220}Fe₃Al, {400}Fe₃Al); the 0% and 10% strain patterns are essentially superimposed, indicating deformation by dislocation slip rather than phase transformation. (b) Omori benchmark: BCC α-dominated pattern with ordered β-NiAl (B2) precipitate reflections; after 8% strain the {111}γ reflection intensifies and the {200}α / {200}B2 cluster redistributes, consistent with stress-induced γ formation. Data collected at SSRF beamline BL12SW with λ = 0.125870 Å.](figures/Fig4_XRD_1D_AI_vs_Omori.jpg)

Two-dimensional Debye–Scherrer patterns recorded directly on the SSRF area detector are shown in **Fig. 4**. The AI alloy rings (**Fig. 4a, b**) are virtually identical before and after deformation: ring positions, widths, and azimuthal intensity distributions are preserved, again indicating the absence of a transformation. The Omori benchmark rings shift from sharp, discrete spots in the undeformed state (**Fig. 4c**) to broader, partially arced rings after deformation (**Fig. 4d**), a signature of variant activation and increased mosaic spread accompanying partial martensitic transformation.

![**Fig. 4.** Two-dimensional Debye–Scherrer synchrotron diffraction patterns recorded directly on the SSRF area detector. (a) AI alloy at 0% strain: sharp, discrete diffraction spots indexed to {111}γ, {200}γ, {220}γ on the γ-FCC subpattern and {220}Fe₃Al, {400}Fe₃Al on the DO₃ subpattern. (b) AI alloy at 10% strain: ring positions, widths, and azimuthal intensity distributions are preserved with no detectable redistribution, consistent with the absence of phase transformation indicated by Fig. 3a. (c) Omori benchmark at 0% strain: discrete spots indicating coarse, well-oriented grains. (d) Omori benchmark at 8% strain: spots transition to broader, partially arced rings, the signature of variant activation accompanying partial martensitic transformation.](figures/Fig5_XRD_2D_composite.png)

---

# 4. Discussion

## 4.1 Why the AI alloy may not have transformed

Several mutually reinforcing factors appear to explain why the AI-hypothesized composition did not exhibit room-temperature pseudoelasticity.

First, the alloy formed a competing ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix that pseudoelasticity requires. For the alloy's reduced Fe-Al chemistry, this B2/Fe-Al phase is thermodynamically favorable, so under the processing conditions used here the intended transforming matrix does not appear to win the phase competition. This is consistent with the dual-phase microstructure observed in every condition (Sec. 3.1) and with the unchanged diffraction pattern under load (Sec. 3.3).

Second, the carbon content (0.105 wt%) likely contributes to stabilizing BCC/B2 relative to FCC austenite. Carbon sits on octahedral interstitial sites of BCC iron and the B2 sublattice and lowers their free energy through Zener-style interstitial ordering [@zener1948; @bhadeshia2010steels]; even modest carbon contents are known to suppress the FCC → BCC transformation behavior in Fe-Mn-Al alloys, which may compound the preference for the observed dual-phase microstructure.

A possible additional factor is magnetic disorder during high-temperature processing. If the target ordered phase is ferrimagnetic with a Curie temperature below the anneal temperature, the absence of a directional magnetic field during cooling could prevent single-variant selection. We regard this as a secondary consideration rather than a primary cause.

Taken together, these factors are consistent with the macroscopic response of **Fig. 2a, b** and **Fig. 3a**: the critical stress to trigger SIMT in the AI alloy appears to exceed the yield stress for dislocation slip, so the wire accommodates strain plastically and shows little recoverable component on unloading.

## 4.2 Implications for AI-guided composition proposals

We are cautious about generalizing from a single composition. Nonetheless, the present case suggests that AI-proposed alloy compositions may benefit from explicit pre-synthesis screening — in particular, comparison of the target phase against the full set of competing phases accessible by the proposed synthesis route, and consideration of interstitial elements such as carbon at the concentrations actually present. The relevant thermodynamic and metallurgical information is largely available in existing databases and literature; what appears to be missing is a step that connects the compositional proposal back to processing-route and interstitial constraints before physical synthesis is committed.

## 4.3 A tentative processing observation in the benchmark

As a secondary observation (Sec. 3.2), the 1200 °C / 12 s strand-anneal condition on the Omori benchmark appeared to recover roughly twice the strain of the 1200 °C / 5 min condition on the same chemistry. This is consistent with the possibility that, within a bounded processing window, sufficiently refined grains embedded in a coherent matrix may aid favorable variant selection, and that faster strand-anneal conditions may retain a finer, more shearable precipitate dispersion. We emphasize that this observation rests on a limited number of specimens and feed rates and should be regarded as preliminary; it is not, on its own, evidence against the role of large grains established in the Fe-Mn-Al-Ni literature [@omori2011superelastic; @vollmer2016cyclic]. A systematic feed-rate study with replicates would be needed to assess whether it reflects a reproducible processing window.

## 4.4 Limitations

Several limitations should be noted before drawing broader conclusions.

First, phase fractions are reported qualitatively rather than quantitatively. Full Rietveld refinement on the SSRF data would convert the qualitative diffraction comparisons into absolute phase fractions; this refinement is in progress and will be reported separately.

Second, the processing observation in Sec. 4.3 rests on a limited set of feed rates (0.8, 4, and 20 ft/min) and limited replicates per condition; it should not be elevated from observation to design rule without a systematic study.

Third, electron backscatter diffraction (EBSD) was not performed. EBSD on the refined-grain Omori specimens would directly resolve variant selection and grain-boundary character.

Fourth, the AI's composition was not iterated. The behavior reported here is for a single LLM-proposed composition; whether iterative feedback would converge to a successful Fe-SMA composition is an open question that this study does not address.

---

# 5. Conclusions

We synthesized and mechanically tested an Fe-Mn-Al-Si-Ni-C composition proposed by an LLM deep-research agent, alongside the established Omori Fe-Mn-Al-Ni benchmark, in a single experimental campaign with identical processing. Three cautious conclusions follow.

1. The AI-hypothesized alloy was readily castable and thermodynamically stable, yet it showed essentially no room-temperature pseudoelastic recovery across all four heat treatments examined. Its cyclic response is consistent with deformation accommodated by dislocation slip rather than stress-induced martensitic transformation.
2. Synchrotron XRD indicates that the AI alloy consisted of coexisting γ-FCC austenite and an ordered B2/DO₃ Fe-Al phase rather than a single transforming matrix, and its diffraction pattern was essentially unchanged by 10% applied strain. This competing phase, possibly compounded by carbon-driven stabilization of BCC/B2, may explain the absence of transformation.
3. As a secondary, preliminary observation, refined-grain processing of the benchmark alloy may improve pseudoelastic recovery; this would warrant systematic investigation before any design conclusion is drawn.

More broadly, this single case study suggests that AI-guided alloy proposals may benefit from explicit screening for competing phases and interstitial effects before synthesis. We present these findings as a starting point rather than a general result, and note that further replication and characterization are needed.

---

# Acknowledgments

The authors thank Fort Wayne Metals for providing access to arc-melting, hot-rolling, cold-drawing, and metallography facilities, and for technical guidance throughout alloy synthesis. The authors also thank the Shanghai Synchrotron Radiation Facility for beam time at BL12SW.

---

# Declarations

**Funding.** No external funding was received for this work.

**Competing interests.** The authors declare no competing interests.

**Data availability.** Raw synchrotron diffraction data, Instron cyclic-tensile export data, and metallographic images are available from the corresponding author on reasonable request.

---

<!-- REFERENCES TO FOLLOW IN BIBLIOGRAPHY BUILD -->
