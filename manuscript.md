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

Iron-based shape memory alloys (Fe-SMAs) are a promising low-cost alternative to Nitinol for civil-infrastructure and biomedical applications, but their pseudoelastic response is sensitive to composition and processing in ways that remain difficult to predict in advance. Large language model (LLM) deep-research agents, coupled with thermodynamic-stability databases, can now propose candidate compositions in seconds, which raises the practical question of whether such proposals survive physical synthesis. Here we report what may be the first synthesis and mechanical characterization of a novel Fe-Mn-Al-Si-Ni-C composition hypothesized by an LLM deep-research agent, benchmarked against the established Omori Fe-Mn-Al-Ni alloy processed under identical conditions; both compositions were verified by ICP-AES. The AI-hypothesized alloy (measured carbon 0.105 wt%, roughly ten times the 0.010 wt% of the benchmark) was readily castable but, on unloading from 2% applied strain, recovered only ≈0.5% strain — a value consistent with elastic springback alone, with no transformation plateau — across all four heat treatments examined. The benchmark recovered up to ≈0.9% under the same conditions, with a stress plateau characteristic of stress-induced α↔γ transformation. Synchrotron X-ray diffraction at the Shanghai Synchrotron Radiation Facility indicated that the AI alloy was a dual-phase mixture of γ-FCC austenite and an ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix that pseudoelasticity requires, and its pattern was essentially unchanged by 10% applied strain. We attribute the absence of pseudoelasticity primarily to the formation of a competing ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix, with the alloy's elevated carbon content promoting this BCC/B2-type ordering over the FCC austenite. These observations suggest that compositions proposed by this kind of LLM-agent route may benefit from explicit pre-synthesis screening of competing phases and interstitial content. A secondary, more tentative observation from the benchmark alloy is that shorter-residence continuous strand annealing may yield refined-grain microstructures with improved pseudoelastic recovery; this would warrant systematic study.

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
2. **Processing observation in the benchmark (exploratory).** As a side observation in the Omori benchmark, we examine whether continuous strand annealing with shorter hot-zone residence times might produce refined-grain microstructures with pseudoelastic recovery comparable to, or better than, longer treatments.

Our expectation at the outset was that the AI-hypothesized alloy would be thermodynamically stable per first-principles data but might nonetheless fail to show pseudoelasticity owing to process–structure–property couplings that are not captured by formation-energy optimization. The results below are broadly consistent with that expectation, although they should be read as a single case study rather than a general conclusion.

## 1.5 Contributions

This work reports what we believe to be the first physical synthesis and mechanical characterization of an Fe-SMA composition hypothesized by an LLM deep-research agent, benchmarked directly against the Omori reference alloy under identical processing. Prior AI-driven SMA work has used graph neural networks, Bayesian materials selection, and GAN-based inverse design, largely on NiTi-family alloys [@aims2022; @generativeinversion2025], and LLM-hypothesized compositions have been explored for high-entropy alloys and halide solid electrolytes [@hu2024beyond]; the intersection of LLM deep-research alloy design and Fe-based SMA synthesis appears not to have been reported previously. We also note, cautiously and as a secondary observation, that continuous strand-anneal processing rate may influence pseudoelastic recovery in the benchmark alloy.

---

# 2. Materials and Methods

## 2.1 Alloy design

The AI-hypothesized composition was generated by an LLM deep-research agent (Gemini 2.5 with the Deep Research tool [@comanici2025gemini]) prompted to propose an Fe-Mn-Al-based composition optimized for room-temperature pseudoelasticity. The agent was instructed to (i) reason from the Fe-Mn-Al-Ni family established by Omori and co-workers [@omori2011superelastic; @omori2017martensitic] as a starting point, (ii) consult thermodynamic-stability data, (iii) target β-NiAl/carbide precipitation as a strengthening pathway, and (iv) minimize cost by excluding cobalt and tantalum. The agent's output, after constraint-prompted refinement, is the composition designated here as the "AI alloy."

For direct benchmarking, a second composition based on the Omori Fe-Mn-Al-Ni reference [@omori2011superelastic] was synthesized under identical conditions. The compositions of both heats were verified after casting by inductively coupled plasma atomic emission spectroscopy (ICP-AES), with carbon and oxygen by inert-gas fusion (ASTM E1019); the measured chemistries are listed in **Table 1**. Measured Mn (31.78 wt% for the AI alloy) is consistent with the nominal target, indicating that evaporative Mn loss during arc melting was not significant.

**Table 1.** Measured chemical compositions (ICP-AES; C and O by ASTM E1019) of the AI-hypothesized alloy and the Omori benchmark, in wt%. "n.r.": not reported in that analysis.

| Element | AI alloy | Omori benchmark |
|---------|---------------------|----------------------------|
| Fe      | balance (55.83)     | balance (46.51)            |
| Mn      | 31.78               | 36.49                      |
| Al      | 6.24                | 8.00                       |
| Si      | 1.11                | <0.01                      |
| Ni      | 4.81                | 8.94                       |
| P       | n.r.                | 0.062                      |
| C       | 0.105               | 0.010                      |
| O       | 0.0004              | <0.001                     |

Co, Ta, Ti, Cr, and Mo were each below 0.01 wt% in the benchmark, confirming the cost-driven exclusion of cobalt and tantalum. The most consequential difference between the two alloys is carbon: the AI composition contains 0.105 wt% C, roughly ten times the 0.010 wt% of the working benchmark (Sec. 4.1).

## 2.2 Synthesis

Alloy ingots were produced by arc-melting elemental constituents of nominal purity ≥99.9% under an argon atmosphere. Each ingot was inverted and remelted a minimum of five times to ensure compositional homogeneity. Following arc melting, ingots were hot-rolled at 850 °C in multiple passes to reduce thickness, and subsequently cold-drawn to a final wire diameter of 0.014 in. (≈0.36 mm). Severe work hardening during cold drawing necessitated intermediate annealing at 900–1000 °C under flowing H₂/Ar to restore ductility between draw passes.

Surface oxidation during high-temperature processing was mitigated by encapsulating samples in evacuated quartz tubes prior to anneal cycles. For samples that experienced oxidation despite encapsulation, a dilute acid bath was used to chemically strip the oxide layer before mechanical testing.

## 2.3 Heat treatments

Four distinct heat-treatment conditions were applied across the two alloys to probe the microstructural and pseudoelastic response (**Table 2**).

**Table 2.** Heat-treatment conditions.

| Condition | Description | Hot-zone residence | Applied to |
|-----------|-------------|--------------------|------------|
| Standard anneal | 1200 °C / 1 min, water quench | — | AI, Omori |
| 3-cycle AGG     | (1200 °C / 30 min + RT / 10 min) × 3, followed by 1200 °C / 1 h, water quench | — | AI, Omori |
| Strand anneal (≈5 min)  | Continuous strand furnace, 1200 °C | ≈5 min | AI, Omori |
| Strand anneal (≈1 min)  | Continuous strand furnace, 1200 °C | ≈1 min | AI, Omori |
| Strand anneal (≈12 s)   | Continuous strand furnace, 1200 °C | ≈12 s  | AI, Omori |

The 3-cycle AGG condition follows the abnormal-grain-growth protocol of Omori *et al.* [@omori2011superelastic], designed to produce bamboo-like single-crystal-diameter grains. The strand-anneal conditions span a range of hot-zone residence times — ≈5 min, ≈1 min, and ≈12 s in the ≈4 ft continuous hot zone used here — and are intended to probe the range over which conventional industrial throughputs might replace the slow batch AGG cycle.

## 2.4 Metallography

Wire cross-sections were embedded in cold-mount epoxy and ground sequentially with silicon-carbide papers from 180 grit through 800 grit. Final polishing used a 0.25 µm OP-S aluminum-oxide suspension on an automated polishing wheel until a scratch-free mirror finish was achieved. Polished cross-sections were imaged on a Clemex Vision PE optical microscope under bright-field illumination at magnifications between 100× and 1000×.

## 2.5 Mechanical testing

Cyclic tensile tests were performed on an Instron servohydraulic testing frame in displacement control. Wire specimens were tested with a 6 mm gauge length using pneumatic grips. Each specimen was loaded to a target tensile strain (8% for the Omori benchmark, 10% for the AI alloy) at a nominal strain rate of 1 × 10⁻³ s⁻¹, held briefly at peak strain, and then unloaded to zero force. Pseudoelastic recovery was quantified as the ratio of recovered strain on unloading to applied peak strain.

To characterize the AI alloy more broadly, monotonic incremental-cyclic tensile tests to failure were also performed on the final 0.36 mm AI-alloy wire after continuous strand annealing (≈1 min hot-zone residence) at temperatures from 600 to 1250 °C, after selected 200 °C post-anneal aging treatments, and after the 3-cycle AGG treatment. Tensile strength and elongation were taken directly from the recorded curves; yield strength (0.2% offset) and elastic modulus (initial loading slope) were extracted from the calibrated stress–strain data. Strain was computed from crosshead displacement over a 5 in gauge length.

## 2.6 Synchrotron X-ray diffraction

Synchrotron XRD measurements were performed at the ultra-hard X-ray multifunctional application beamline BL12SW of the Shanghai Synchrotron Radiation Facility (SSRF) [@ssrf2024bl12sw], in collaboration with co-author J. Yan. The incident wavelength was λ = 0.125870 Å (photon energy ≈98.5 keV), and the sample-to-detector distance was 1827.486 mm with a 100 µm × 100 µm pixel area detector. Two-dimensional Debye–Scherrer patterns were collected from each specimen before and after tensile deformation to test for a stress-induced phase transformation. Each 2D pattern was azimuthally integrated to produce a one-dimensional intensity-versus-2θ profile, and reflections were indexed by comparison with reference Fe, Fe-Al, and γ-austenite phases.

---

# 3. Results

## 3.1 Microstructure

Optical micrographs of polished wire cross-sections for the four most informative heat-treatment conditions are shown in **Fig. 1**.

After the standard 1200 °C / 1 min anneal, the AI alloy (**Fig. 1a**) exhibits a highly refined dual-phase morphology with irregular grain boundaries and no single dominant phase. Following the 3-cycle AGG treatment (**Fig. 1b**), the AI alloy continues to show a dual-phase structure: grain growth occurred only in one of the two phases, while the second phase remained as fine, dispersed regions. The dual-phase character persisted across every AI-alloy condition examined, which suggests that the AI's predicted composition did not support single-phase austenite formation under any of the heat treatments tested in this study.

The Omori benchmark behaves differently. After 3-cycle AGG (**Fig. 1c**), it develops the bamboo-like grain morphology consistent with the established Fe-Mn-Al-Ni literature [@omori2011superelastic; @vollmer2016cyclic], with grain diameters spanning a substantial fraction of the wire cross-section. The 1200 °C / 1 min condition (**Fig. 1d**) yields an acicular ferrite microstructure.

![**Fig. 1.** Optical micrographs of polished wire cross-sections under four representative heat-treatment conditions. (a) AI alloy after the standard 1200 °C / 1 min anneal: highly refined dual-phase morphology with irregular grain boundaries (scale bar ≈100 µm). (b) AI alloy after 3-cycle AGG: grain growth in one phase only; the dual-phase structure persists (scale bar 400 µm). (c) Omori benchmark after 3-cycle AGG: bamboo-like grain morphology (scale bar 200 µm). (d) Omori benchmark after 1200 °C / 1 min strand anneal: acicular ferrite microstructure (scale bar 200 µm). All images acquired on a Clemex Vision PE optical microscope under bright-field illumination.](figures/Fig2_microstructure_composite.png)

## 3.2 Cyclic stress–strain response

Cyclic tensile stress–strain curves for representative specimens are shown in **Fig. 2**.

Representative recovered-strain and peak-stress values, read from the incremental cyclic curves at a common 2% reference cycle, are summarized in **Table 3**. The AI alloy in both the 1200 °C / 1 min (**Fig. 2a**) and 3-cycle AGG (**Fig. 2b**) conditions recovered only ≈0.5% strain on unloading from the 2% cycle (a recovery ratio of ≈25%). Loading exhibited a monotonically rising stress with no defined transformation plateau, and the recovered strain is comparable to the elastic strain σ/E expected at the unload stress (≈0.4–0.5% at ≈650 MPa for E ≈ 150 GPa). In other words, the recovery is consistent with elastic springback alone, with no resolvable pseudoelastic contribution; this behavior was the same across all AI-alloy heat treatments examined, including loading as far as ≈24% total strain (Table 3).

The Omori benchmark shows a stress plateau and greater recovery in the conditions that develop bamboo or refined-grain microstructures (**Fig. 2c, d**). At the same 2% reference cycle, the 1200 °C / 12 s condition recovered ≈0.92% strain (≈46%), roughly twice the ≈0.49% (≈25%) of the 1200 °C / 5 min condition, and exceeding the elastic strain — indicating a genuine pseudoelastic component. We treat this comparison cautiously, as it rests on single specimens (n = 1 per condition); it is considered further in Sec. 4.3.

**Table 3.** Cyclic-tensile metrics for both alloys, computed from the calibrated incremental stress–strain curves of **Fig. 2**. Recovered strain and recovery ratio are reported at a common 2% applied-strain cycle present in all tests; peak stress is the maximum stress reached over the full test. Values are single-specimen (n = 1 per condition); a statistically resolved study is identified as future work (Sec. 4.4).

| Alloy | Condition | Max applied strain (%) | Peak stress (MPa) | Recovered strain at 2% (%) | Recovery at 2% (%) |
|-------|-----------|------------------------|-------------------|----------------------------|--------------------|
| AI    | 1200 °C / 1 min  | 23.9 | 938  | 0.45 | 22.5 |
| AI    | 3-cycle AGG      | 9.2  | 817  | 0.50 | 25.0 |
| Omori | 1200 °C / 5 min  | 9.6  | 805  | 0.49 | 24.7 |
| Omori | 1200 °C / 12 s   | 7.1  | 1201 | 0.92 | 45.9 |

For the AI alloy the recovered strain at 2% matches the elastic springback and there is no transformation plateau; the Omori 12 s condition is the only case in which recovery clearly exceeds the elastic strain.

![**Fig. 2.** Cyclic tensile stress–strain response. (a) AI alloy after the standard 1200 °C / 1 min anneal: monotonic loading with no transformation plateau; recovered strain on unloading (≈0.5% at the 2% cycle) is consistent with elastic springback alone (Table 3). (b) AI alloy after 3-cycle AGG: response qualitatively identical to (a), indicating that AGG processing did not restore pseudoelasticity in the AI composition. (c) Omori benchmark after 1200 °C / 5 min strand anneal: partial pseudoelastic recovery with developing hysteresis. (d) Omori benchmark after 1200 °C / 12 s strand anneal (refined small-grain microstructure): pronounced pseudoelastic hysteresis and a distinct stress plateau. Red arrows in (c, d) mark the residual unrecovered strain after unloading. Panels (c) and (d) are the ≈5 min and ≈12 s strand-anneal specimens of the Omori benchmark, respectively; one representative specimen per condition.](figures/Fig3_stressstrain_composite.png)

Beyond the cyclic conditions of Table 3, monotonic tensile-to-failure tests on the final 0.36 mm AI-alloy wire give a broader picture of how heat treatment governs its mechanical properties (**Table 4**). The response is strongly anneal-dependent: low strand-anneal temperatures (600–700 °C) leave the wire high-strength but brittle (tensile strength up to ≈2290 MPa at only ≈2% elongation, reflecting incomplete recrystallization of the cold-drawn wire), whereas annealing at 800–1200 °C progressively softens the wire and restores ductility, with elongation peaking near 33% at 1000 °C. The elastic modulus stays in the ≈150–165 GPa range across the well-annealed conditions. Post-anneal aging at 200 °C produces only minor changes. Importantly, none of these treatments altered the cyclic behaviour of Sec. 3.2 — the AI wire deforms plastically with no pseudoelastic plateau regardless of anneal temperature — consistent with the dual-phase structure identified below (Sec. 3.3).

**Table 4.** Monotonic tensile properties of the AI-alloy wire (0.36 mm diameter) as a function of strand-anneal temperature, including two extended 1250 °C holds, three 200 °C post-anneal aging treatments, and the 3-cycle abnormal-grain-growth (AGG) condition. Tensile strength and elongation are read directly from the stress–strain curves; yield strength (0.2% offset) and modulus (initial elastic slope) are extracted from the same calibrated data. Values are single-specimen (n = 1) measurements; strain is crosshead-displacement based, so the absolute moduli — and especially the two 1250 °C values, which were affected by grip compliance — should be read as approximate. For the AGG condition, tensile strength and elongation are from the dedicated monotonic AGG specimen, while the yield strength and modulus are taken from the companion incremental-cyclic AGG specimen of Table 3, whose resolved low-strain loading region supplies those quantities. None of these treatments produced a pseudoelastic plateau (cf. Table 3).

| Anneal temperature | Yield strength (MPa) | Tensile strength (MPa) | Elongation (%) | Modulus (GPa) |
|--------------------|----------------------|------------------------|----------------|---------------|
| 600 °C             | 1379 | 2293 | 2.3  | 157 |
| 700 °C             | 1330 | 2009 | 2.2  | 163 |
| 800 °C             | 1164 | 1221 | 24.0 | 154 |
| 900 °C             | 944  | 1078 | 29.7 | 152 |
| 1000 °C            | 673  | 967  | 33.4 | 156 |
| 1100 °C            | 556  | 947  | 29.7 | 157 |
| 1200 °C            | 502  | 938  | 23.9 | 163 |
| 1250 °C (5 min)    | 361  | 661  | 12.5 | 121 |
| 1250 °C (20 min)   | 395  | 589  | 6.3  | 79  |
| 1200 °C + 200 °C / 1 h  | 518 | 945 | 25.2 | 157 |
| 1200 °C + 200 °C / 3 h  | 505 | 934 | 25.5 | 160 |
| 1200 °C + 200 °C / 20 h | 503 | 891 | 14.9 | 164 |
| 3-cycle AGG (+200 °C / 3 h) | 448 | 1006 | 11.9 | 124 |

## 3.3 Synchrotron diffraction and phase identification

The mechanical result above — a dual-phase microstructure (Sec. 3.1) with no resolvable pseudoelastic recovery (Sec. 3.2) — is the primary evidence that the AI alloy does not undergo a stress-induced transformation. Synchrotron XRD (**Fig. 3**) was used to corroborate this and to identify the constituent phases.

The AI alloy (**Fig. 3a**) exhibits a multi-peak pattern indexable to coexisting FCC γ-austenite and an ordered B2/DO₃ Fe₃Al phase, confirming the dual-phase character inferred from the micrographs and confirming that the targeted single transforming matrix did not form. Comparison of the ex-situ 0% and 10% strain patterns shows that peak positions and relative intensities are essentially unchanged: no new reflections appear and none disappear. We note that an ex-situ measurement made after unloading cannot, on its own, exclude a fully reversible transformation that reverts on unloading; here, however, the absence of any mechanical recovery (Table 3) together with the unchanged dual-phase pattern points consistently to deformation by dislocation slip rather than transformation. The presence of an ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix is itself consistent with the absence of recovery (Sec. 4.1).

The Omori benchmark (**Fig. 3b**) presents a BCC α-dominated pattern with ordered β-NiAl (B2) precipitate reflections in the undeformed state. After 8% applied strain, the {111}γ reflection intensifies and the overlapping {200}α / {200}B2 cluster redistributes in intensity, consistent with stress-induced γ formation and partial variant activation.

![**Fig. 3.** Azimuthally integrated synchrotron XRD patterns comparing the undeformed (0% strain) and deformed (post-tensile-test) states. (a) AI alloy: pattern indexable to coexisting FCC γ-austenite ({111}γ, {200}γ, {220}γ) and ordered B2/DO₃ Fe₃Al phase ({220}Fe₃Al, {400}Fe₃Al); the 0% and 10% strain patterns are essentially superimposed, indicating deformation by dislocation slip rather than phase transformation. (b) Omori benchmark: BCC α-dominated pattern with ordered β-NiAl (B2) precipitate reflections; after 8% strain the {111}γ reflection intensifies and the {200}α / {200}B2 cluster redistributes, consistent with stress-induced γ formation. Data collected at SSRF beamline BL12SW with λ = 0.125870 Å.](figures/Fig4_XRD_1D_AI_vs_Omori.jpg)

Two-dimensional Debye–Scherrer patterns recorded directly on the SSRF area detector are shown in **Fig. 4**. The AI alloy rings (**Fig. 4a, b**) are virtually identical before and after deformation: ring positions, widths, and azimuthal intensity distributions are preserved, again indicating the absence of a transformation. The Omori benchmark rings shift from sharp, discrete spots in the undeformed state (**Fig. 4c**) to broader, partially arced rings after deformation (**Fig. 4d**), a signature of variant activation and increased mosaic spread accompanying partial martensitic transformation.

![**Fig. 4.** Two-dimensional Debye–Scherrer synchrotron diffraction patterns recorded directly on the SSRF area detector. (a) AI alloy at 0% strain: sharp, discrete diffraction spots indexed to {111}γ, {200}γ, {220}γ on the γ-FCC subpattern and {220}Fe₃Al, {400}Fe₃Al on the DO₃ subpattern. (b) AI alloy at 10% strain: ring positions, widths, and azimuthal intensity distributions are preserved with no detectable redistribution, consistent with the absence of phase transformation indicated by Fig. 3a. (c) Omori benchmark at 0% strain: discrete spots indicating coarse, well-oriented grains. (d) Omori benchmark at 8% strain: spots transition to broader, partially arced rings, the signature of variant activation accompanying partial martensitic transformation.](figures/Fig5_XRD_2D_composite.png)

---

# 4. Discussion

## 4.1 Why the AI alloy may not have transformed: carbon-stabilized ordering

The most likely explanation is the formation of a competing ordered phase. The AI alloy formed an ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix that pseudoelasticity requires. For the alloy's Fe-Al-rich chemistry this ordered constituent is thermodynamically favoured, so under the processing conditions used here the intended transforming matrix does not win the phase competition; the available aluminium partitions into the ordered Fe₃Al (B2/DO₃) phase, producing the dual-phase γ-FCC + Fe₃Al structure seen in every condition (Sec. 3.1) and in the diffraction patterns (Sec. 3.3). The targeted β-NiAl/carbide strengthening constituents did not form; the alloy is dominated instead by ordered Fe-Al.

A key contributing factor is the alloy's carbon content, which at 0.105 wt% is roughly ten times the 0.010 wt% of the benchmark. Carbon occupies octahedral interstitial sites of BCC iron and the B2 sublattice and lowers their free energy through Zener-style interstitial ordering [@zener1948; @bhadeshia2010steels]; even modest carbon contents are known to stabilize the BCC/B2 constituent relative to FCC austenite, compounding the preference for the observed dual-phase microstructure. A full confirmation would require CALPHAD modelling of the Fe-Mn-Al-Ni-Si-C system and quantitative carbon-partitioning measurements, neither of which was performed here. (Magnetic effects during high-temperature processing may also play a minor role but are not constrained by our data.)

Taken together, these factors are consistent with the macroscopic response of **Fig. 2a, b** and **Fig. 3a**: with no transformable matrix available, the critical stress for stress-induced transformation in the AI alloy is not reached before dislocation slip, so the wire accommodates strain plastically and recovers only its elastic strain on unloading.

## 4.2 A pre-synthesis screening loop for the LLM-agent route

We are cautious about generalizing from a single composition, and we restrict the following to the specific LLM-deep-research route used here rather than to AI-guided design in general. For that route, the failure mode we observed — the intended transforming matrix that never formed because a competing ordered Fe-Al phase, promoted by the alloy's chemistry and elevated carbon content, dominated instead — could plausibly have been caught before any metal was melted. We suggest a short, deterministic screening loop to run on the agent's output prior to synthesis:

1. **Phase-stability check.** For the proposed chemistry, compute the equilibrium (or near-equilibrium) phase assemblage by CALPHAD over the full element set, and confirm that the targeted strengthening phase is actually stable at the proposed composition and is not displaced by a competing ordered phase (here, Fe₃Al/B2).
2. **Stoichiometry check.** Verify that the proposed level of each targeted strengthening or precipitate-forming element is sufficient, relative to established working alloys, for the intended phase to form rather than a competing ordered phase, flagging proposals that fall outside the literature range.
3. **Interstitial check.** Evaluate the effect of the proposed interstitial content (C, N, O) on the matrix phase balance at the concentrations actually specified.
4. **Processing-route check.** Confirm that the intended anneal/residence-time schedule can plausibly reach the target microstructure.

Only compositions that pass these checks would proceed to synthesis. Each step uses information already available in standard thermodynamic databases and the Fe-SMA literature; what was missing in the present case was the step connecting the agent's proposal back to that information.

## 4.3 A tentative processing observation in the benchmark

As a secondary observation (Sec. 3.2, Table 3), the 1200 °C / 12 s strand-anneal condition on the Omori benchmark recovered ≈0.92% strain at the 2% reference cycle, against ≈0.49% for the 1200 °C / 5 min condition on the same chemistry — roughly a factor of two, with only the shorter-residence condition exceeding the elastic strain. This is consistent with the possibility that, within a bounded processing window, sufficiently refined grains embedded in a coherent matrix may aid favorable variant selection, and that faster strand-anneal conditions may retain a finer, more shearable precipitate dispersion. We emphasize that this rests on single specimens (n = 1 per condition) and three residence times and should be regarded as preliminary; it is not, on its own, evidence against the role of large grains established in the Fe-Mn-Al-Ni literature [@omori2011superelastic; @vollmer2016cyclic]. A systematic residence-time study with replicates would be needed to assess whether it reflects a reproducible processing window.

## 4.4 Limitations

Several limitations should be noted before drawing broader conclusions.

First, the mechanical metrics in **Table 3** are single-specimen reads (n = 1 per condition) taken from calibrated cyclic curves; recovered strains are approximate (±0.2% strain). A statistically resolved study with replicates and error bars is needed before any value is treated as a design figure.

Second, phase fractions are reported qualitatively rather than quantitatively. Full Rietveld refinement on the SSRF data would convert the qualitative diffraction comparisons into absolute phase fractions; this refinement is in progress and will be reported separately.

Third, the diffraction comparison is ex situ (measured before and after testing, not under load). While the combination of zero mechanical recovery and an unchanged dual-phase pattern is internally consistent, in-situ loading would more directly exclude a reversible transformation; this is planned future work.

Fourth, the processing observation in Sec. 4.3 rests on a limited set of hot-zone residence times (≈5 min, ≈1 min, and ≈12 s) and single specimens per condition; it should not be elevated from observation to design rule without a systematic study. Electron backscatter diffraction (EBSD) was also not performed, and would directly resolve variant selection and grain-boundary character in the refined-grain Omori specimens.

Fifth, the AI's composition was not iterated. The behavior reported here is for a single LLM-proposed composition; whether iterative feedback would converge to a successful Fe-SMA composition is an open question that this study does not address.

---

# 5. Conclusions

We synthesized and mechanically tested an Fe-Mn-Al-Si-Ni-C composition proposed by an LLM deep-research agent, alongside the established Omori Fe-Mn-Al-Ni benchmark, in a single experimental campaign with identical processing. Three cautious conclusions follow.

1. The AI-hypothesized alloy was readily castable but, on unloading from 2% applied strain, recovered only ≈0.5% — consistent with elastic springback alone and with no transformation plateau — across all four heat treatments examined, including loading as far as ≈24% strain. Its cyclic response is consistent with deformation by dislocation slip rather than stress-induced martensitic transformation.
2. The absence of pseudoelasticity is attributed primarily to the formation of a competing ordered B2/DO₃ Fe-Al phase rather than the single transforming matrix, with the alloy's elevated carbon content (0.105 wt%, roughly ten times the benchmark) promoting BCC/B2-type ordering over the FCC austenite. Synchrotron XRD confirms the resulting dual-phase γ-FCC + Fe₃Al structure and shows its pattern essentially unchanged by 10% applied strain. Full confirmation of the carbon contribution awaits CALPHAD modelling of the Fe-Mn-Al-Ni-Si-C system.
3. As a secondary, preliminary observation, refined-grain (shorter-residence strand-anneal) processing of the benchmark recovered roughly twice the strain of the longer-residence condition (≈0.9% vs ≈0.5% at 2% applied); this would warrant systematic investigation before any design conclusion is drawn.

More broadly, for the specific LLM-deep-research route used here, this single case study suggests that proposed compositions may benefit from a short pre-synthesis screen (Sec. 4.2) — checking competing phases, key-element stoichiometry, and interstitial content — before synthesis. We present these findings as a starting point rather than a general result, and note that further replication and characterization are needed.

---

# Acknowledgments

The authors thank Fort Wayne Metals for providing access to arc-melting, hot-rolling, cold-drawing, and metallography facilities, and for technical guidance throughout alloy synthesis. The authors also thank the Shanghai Synchrotron Radiation Facility for beam time at BL12SW.

---

# Declarations

**Funding.** No external funding was received for this work.

**Competing interests.** The authors declare no competing interests.

**Data availability.** ICP-AES and interstitial-gas (ASTM E1019) chemistry certificates for both heats, raw synchrotron diffraction data, Instron cyclic-tensile export data, and metallographic images are available from the corresponding author on reasonable request.

---

<!-- REFERENCES TO FOLLOW IN BIBLIOGRAPHY BUILD -->
