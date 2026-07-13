# Limited Room-Temperature Pseudoelasticity in an AI-Hypothesized Fe-Mn-Al-Si-Ni-C Alloy: Synthesis, Microstructure, and Cyclic Response

Frank Cai
Homestead High School, Fort Wayne, Indiana, US
frankyc11223@gmail.com

S. Cai
Fort Wayne Metals, Fort Wayne, Indiana, US
song_cai@fwmetals.com

J. Yan
Shanghai Synchrotron Radiation Facility, Shanghai, China

*Target venue: Shape Memory and Superelasticity (Springer)*

---

## Introduction

Nickel-titanium (Ni-Ti) alloys currently dominate the shape memory alloy (SMA) market because of their superior superelasticity and shape memory effect. Their adoption in cost-sensitive industries, however, is limited by the high cost of titanium and by demanding vacuum processing. Iron-based shape memory alloys (Fe-SMAs) are an attractive alternative: iron is abundant and inexpensive, and Fe-SMA wire can in principle be made on conventional steel-processing equipment. The breakthrough that made polycrystalline Fe-SMAs practical was Omori's 2011 demonstration of room-temperature superelasticity in Fe-Mn-Al-Ni after abnormal grain growth (AGG), in which large "bamboo" grains reduce inter-granular constraint [1]. We use that alloy here only as a processing benchmark.

This study takes a different route to composition selection. A large language model (LLM) deep-research agent was used to hypothesize a cost-effective Fe-SMA composition by synthesizing decades of metallurgical literature together with first-principles stability data [3,6]. Tools of this kind can propose candidate compositions in seconds, which raises a practical question for a wire producer: do such AI-proposed compositions survive physical synthesis and develop useful pseudoelasticity? Generative materials models typically optimize for thermodynamic stability but do not account for the kinetic, interstitial, and processing-rate factors that decide which phases actually form in the shop. This paper reports the synthesis, thermomechanical processing, microstructure, and cyclic-tensile behavior of one such AI-hypothesized Fe-Mn-Al-Si-Ni-C wire, benchmarked against the Omori alloy under matched processing.

## Materials and Methods

The candidate composition was selected with an LLM deep-research agent (Gemini 2.5 Deep Research) [6]. The agent was asked to start from the Fe-Mn-Al-Ni family [1], to consult thermodynamic-stability data, to target β-NiAl and carbide precipitation for strengthening, and to avoid cobalt and tantalum for cost. Its output, designated the "AI alloy," together with the Omori benchmark, is given in Table 1.

**Table 1. Target compositions (wt%).**

| Element | AI alloy | Omori benchmark |
|---------|----------|-----------------|
| Fe | bal. | bal. |
| Mn | 31.78 | 36.49 |
| Al | 6.24 | 8.00 |
| Si | 1.11 | — |
| Ni | 4.81 | 8.94 |
| C | 0.105 | 0.010 |

Ingots were arc-melted under argon and remelted at least five times for homogeneity. Material was hot-rolled at 850 °C and cold-drawn to a final wire diameter of 0.014" (≈0.36 mm), with intermediate annealing at 900–1000 °C under H₂/Ar to restore ductility between draws. Severe work hardening, oxidation sensitivity, and a tendency toward brittleness made the drawing route demanding; samples were sealed in evacuated quartz tubes before high-temperature anneals, and residual oxide was stripped in a dilute acid bath before testing.

Four heat treatments were applied to both alloys: a standard 1200 °C / 1 min anneal with water quench; a 3-cycle AGG treatment (1200 °C / 30 min + room temperature / 10 min, ×3, then 1200 °C / 1 h, water quench); and continuous strand annealing at 1200 °C over a range of feed rates (0.8, 4, and 20 ft/min). Polished wire cross-sections were imaged on a Clemex Vision PE optical microscope. Cyclic tensile tests were run on an Instron servohydraulic frame in displacement control (6 mm gauge length, strain rate 1 × 10⁻³ s⁻¹), loading to 8–10% strain and unloading to zero force; pseudoelastic recovery was taken as recovered strain divided by applied strain. To check for a stress-induced phase transformation, synchrotron X-ray diffraction (XRD) was carried out before and after deformation at beamline BL12SW of the Shanghai Synchrotron Radiation Facility (SSRF), λ = 0.125870 Å [2]. Two-dimensional Debye–Scherrer patterns were azimuthally integrated to 1D profiles and indexed against reference Fe, Fe-Al, and γ-austenite phases.

## Results and Discussions

The AI alloy is dual-phase in every condition tested. After the 1200 °C / 1 min anneal (Fig. 1a) it shows a refined dual-phase morphology with irregular boundaries; after 3-cycle AGG (Fig. 1b) one phase coarsens while the second remains as fine dispersed regions. The dual-phase structure never resolves to single-phase austenite, which suggests the AI composition does not support the transforming matrix that pseudoelasticity requires. For comparison, the Omori benchmark develops the expected bamboo-grain morphology after AGG (Fig. 1c) and an acicular ferrite structure after the short anneal (Fig. 1d).

![**Figure 1.** Optical micrographs of polished wire cross-sections. a) AI alloy after 1200 °C / 1 min: refined dual-phase morphology; b) AI alloy after 3-cycle AGG: growth in one phase only, dual-phase structure retained; c) Omori benchmark after 3-cycle AGG: bamboo-grain morphology; d) Omori benchmark after 1200 °C / 1 min: acicular ferrite.](figures/Fig2_microstructure_composite.png)

The cyclic-tensile behavior follows directly from the microstructure. In both the standard-anneal and AGG conditions (Fig. 2a, b) the AI alloy shows essentially no recovery on unloading: stress rises monotonically with no transformation plateau, and unloading retraces a near-elastic slope to negligible recovered strain. There is no "flag-shaped" hysteresis. This response is consistent with deformation by irreversible dislocation slip rather than reversible stress-induced martensitic transformation, and it was the same across all AI-alloy heat treatments. The Omori benchmark, by contrast, shows the expected pseudoelastic hysteresis where the bamboo or refined-grain microstructure develops (Fig. 2c, d).

![**Figure 2.** Cyclic tensile stress–strain response. a) AI alloy after 1200 °C / 1 min and b) after 3-cycle AGG: monotonic loading, no transformation plateau, negligible recovery on unloading; c) Omori benchmark after 1200 °C / 5 min and d) after 1200 °C / 12 s strand anneal: pseudoelastic hysteresis with a stress plateau. Arrows in c, d mark residual unrecovered strain.](figures/Fig3_stressstrain_composite.png)

Synchrotron XRD confirms the mechanism. The AI alloy consists of an FCC γ-phase together with an ordered B2/DO₃ Fe₃Al secondary phase, rather than the single BCC-forming matrix of a working Fe-SMA. More tellingly, the 1D and 2D patterns are essentially unchanged between 0% and 10% applied strain (Fig. 3a; Fig. 4a, b): no new reflections appear and the ring positions do not shift. In a functional SMA, deformation triggers a phase change that appears as new peaks or intensity shifts; its absence here is direct evidence that the wire accommodates strain by slip, not transformation. The Omori benchmark behaves as expected, with its sharp diffraction spots broadening into partial arcs after deformation (Fig. 3b; Fig. 4c, d), the signature of variant activation in a stress-induced transformation.

![**Figure 3.** Azimuthally integrated synchrotron XRD (SSRF BL12SW, λ = 0.125870 Å), undeformed vs. deformed. a) AI alloy: coexisting FCC γ-austenite and ordered B2/DO₃ Fe₃Al; 0% and 10% strain patterns essentially superimposed. b) Omori benchmark: BCC α-dominated pattern with β-NiAl (B2) reflections; after 8% strain the {111}γ reflection intensifies, consistent with stress-induced γ formation.](figures/Fig4_XRD_1D_AI_vs_Omori.jpg)

![**Figure 4.** Two-dimensional Debye–Scherrer synchrotron patterns. a) AI alloy at 0% and b) 10% strain: ring positions and intensities preserved, no transformation. c) Omori benchmark at 0% and d) 8% strain: discrete spots broaden into partial arcs, the signature of variant activation in a partial martensitic transformation.](figures/Fig5_XRD_2D_composite.png)

Two factors most likely explain the missing transformation. First, the ordered B2/Fe-Al phase is thermodynamically favorable for this reduced Fe-Al chemistry, so it tends to win the phase competition during solidification and annealing. Second, the 0.105 wt% carbon, intended as a strengthening interstitial, instead helps stabilize BCC/B2 over FCC austenite through interstitial ordering [5]; even modest carbon contents are known to do this in Fe-Mn-Al alloys. The critical stress to trigger transformation therefore appears to exceed the slip stress, and the wire yields plastically. The practical reading is that the AI optimized for a stable composition but not for a processable, transforming one — current models lack the process–structure–property context that decides functional performance, and AI-proposed compositions may benefit from a competing-phase and interstitial screen before any metal is melted.

As a separate and more tentative observation on the benchmark, a short 1200 °C / 12 s strand-anneal (refined small grains) appeared to recover roughly twice the strain of a 1200 °C / 5 min condition on the same chemistry. This may indicate a useful processing window in which sufficiently fine grains aid variant selection, but it rests on few specimens and feed rates and is not by itself evidence against the established role of large grains [1,4]. A systematic feed-rate study would be needed before drawing any conclusion. We also note that phase fractions here are qualitative; Rietveld refinement and EBSD are planned to quantify them.

## Conclusions

An Fe-Mn-Al-Si-Ni-C composition hypothesized by an LLM deep-research agent was synthesized, processed into fine wire, and tested alongside the Omori benchmark under identical conditions. The AI alloy was castable and thermodynamically stable but showed essentially no room-temperature pseudoelasticity in any of four heat treatments. Microstructural and synchrotron-XRD evidence indicate that it remained a dual-phase γ-FCC + ordered B2/Fe-Al material whose diffraction pattern did not change under load, so deformation was accommodated by slip rather than by the targeted stress-induced transformation, possibly compounded by carbon stabilization of BCC/B2. A tentative benchmark observation that refined-grain processing may improve recovery warrants systematic study. Taken together, the results suggest that present-day AI models optimize for theoretical stability but lack the process–structure–property and manufacturability context needed to predict functional SMA performance; integrating processing data and a competing-phase screen into the AI reasoning loop may help bridge the gap between digital discovery and industrial application.

## References

[1] T. Omori et al., "Superelastic effect in polycrystalline ferrous alloys," Science, 333 (2011) 68-71.

[2] K. Yang, Z.H. Dong, C.Y. Zhou, Z.L. Zhao, D.X. Liang, S.C. Cao, A.G. Li, "Ultrahard X-ray multifunctional application beamline at the SSRF," Nucl. Sci. Technol., 35 (2024) 98.

[3] A. Merchant et al., "Scalable deep learning for materials discovery," Nature, 624 (2023) 80-85.

[4] C. Vollmer et al., "On the effect of titanium on quenching sensitivity and pseudoelasticity in an Fe-Mn-Al-Ni shape memory alloy," Scr. Mater., 162 (2019) 442-446.

[5] C. Zener, "Theory of strain interaction of solute atoms," Phys. Rev., 74 (1948) 639-647.

[6] G. Comanici et al., "Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, and long context," arXiv:2507.06261 (2025).
