---
title: "Process-Aware Limits of AI-Guided Alloy Design: A Computational and Experimental Audit of an LLM-Hypothesized Fe-Mn-Al-Si-Ni-C Shape Memory Alloy"
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
  - AI-guided materials discovery
  - Reality gap
  - Pseudoelasticity
  - Synchrotron XRD
  - Abnormal grain growth
target_journal: Shape Memory and Superelasticity (Springer)
---

# Abstract

Iron-based shape memory alloys (Fe-SMAs) are a promising low-cost alternative to Nitinol for civil-infrastructure and biomedical applications, but their pseudoelastic response is sensitive to composition and processing in ways that remain difficult to predict *a priori*. Recent advances in AI-guided materials discovery, particularly large language model (LLM) deep-research agents combined with thermodynamic-stability databases such as GNoME, raise the question of whether such tools can autonomously propose pseudoelastic Fe-SMA compositions that survive physical synthesis. Here we test this directly by synthesizing, characterizing, and computationally auditing a novel Fe-Mn-Al-Si-Ni-C composition hypothesized by an LLM deep-research pipeline, alongside the established Omori Fe-Mn-Al-Ni benchmark. The AI-hypothesized alloy was thermodynamically stable but exhibited essentially zero room-temperature pseudoelastic recovery across all heat treatments examined, in contrast to the benchmark which showed reversible α↔γ activation. Synchrotron X-ray diffraction at the Shanghai Synchrotron Radiation Facility (λ = 0.12587 Å) and a custom JARVIS-DFT cosine-matching pipeline identified a B2 AlFe-type phase as the dominant constituent of the AI alloy, with a DFT formation energy of −0.358 eV/atom: 0.163 eV/atom more stable than the targeted L2₁ Heusler matrix. This quantifies a measurable "reality gap" between formation-energy optimization and processable pseudoelasticity. A secondary finding, obtained from the Omori benchmark, is that high-feed-rate continuous strand annealing (20 ft/min, 1200 °C) produces refined-grain microstructures with approximately twice the pseudoelastic recovery of conventional bamboo-grain samples produced by slow abnormal grain growth: a result directly counter to the prevailing paradigm in the Fe-SMA literature. We argue that next-generation materials AI must integrate kinetic, interstitial, and processing-rate constraints into its reasoning loops, and we propose a low-cost DFT cross-validation step as a pre-synthesis screen.

**Keywords:** Fe-based shape memory alloy; AI-guided materials discovery; reality gap; pseudoelasticity; synchrotron XRD; abnormal grain growth

---

# 1. Introduction

## 1.1 Motivation: low-cost shape memory alloys

Shape memory alloys (SMAs) exhibit reversible martensitic transformations that enable two technologically important behaviors: the shape memory effect, in which thermally induced phase changes recover macroscopic deformation, and pseudoelasticity (superelasticity), in which stress-induced martensite reverts upon unloading [@otsuka2005physical; @lagoudas2008shape]. Nitinol (Ni-Ti) is the dominant commercial SMA, with recoverable strains of 6–8%, excellent cyclic stability, and biocompatibility, and it accounts for the majority of SMA use in medical devices, aerospace actuators, and damping applications [@duerig1999overview; @mohd2014nitinol]. However, Nitinol is expensive: titanium extraction is energy-intensive, and high-quality SMA wire requires vacuum-arc or vacuum-induction processing to avoid embrittling oxide and nitride phases [@otsuka2005physical].

Iron-based shape memory alloys offer a path to dramatically lower cost. Iron is one of the most abundant metals in the Earth's crust, and Fe-SMA processing can leverage established steel-industry infrastructure (electric-arc melting, hot rolling, strand annealing) without strict vacuum requirements [@omori2011superelastic; @abuzaid2019femnnial]. Replacing scarce alloying elements (Co, Ta, Ni in Nitinol-grade quantities) with abundant Mn, Al, Si, and minor Ni reduces both raw-material and processing costs [@omori2017martensitic]. Beyond direct cost savings, the lower modulus and higher damping capacity of Fe-SMAs make them attractive as structural-engineering prestressing tendons for concrete and as seismic dampers for steel-frame buildings, applications where Nitinol's price has historically been prohibitive [@cladera2014ironbased].

## 1.2 The Omori paradigm

The breakthrough that established polycrystalline Fe-SMAs as practical materials was Omori *et al.*'s 2011 demonstration of room-temperature superelasticity in Fe-Mn-Al-Ni after abnormal grain growth (AGG) [@omori2011superelastic]. The key microstructural feature was *bamboo-like* grains, single-crystal-diameter grains spanning the full wire cross-section, produced by cyclic heat treatments above and below the γ↔α phase boundary that drive grain-boundary mobility. Subsequent work established that bamboo grains are necessary because the large transformation strain anisotropy of the BCC α / FCC γ pair leads to severe inter-granular stress concentrations and brittle failure when many grains span the cross-section [@vollmer2016cyclic; @abuzaid2019femnnial]. The bamboo-grain paradigm has since dominated Fe-SMA research and industrial scale-up: virtually all published high-performance Fe-Mn-Al-Ni wires are produced via slow AGG heat treatments measured in minutes-per-foot rather than feet-per-minute, an industrially undesirable bottleneck.

## 1.3 AI-guided alloy discovery and the prediction–processability gap

Materials discovery has been transformed in the last three years by deep-learning models trained on first-principles thermodynamics. DeepMind's GNoME predicted more than 2.2 million previously unreported crystal structures with >80% precision against DFT validation [@merchant2023gnome], expanding the catalog of stable inorganic phases by an order of magnitude. In parallel, agentic large language models with deep-research capabilities (e.g., Gemini Deep Research, OpenAI o-series with browsing) can ingest decades of metallurgical literature and propose novel compositions in seconds [@xu2025deepresearch; @comanici2025gemini]. Combined, these tools suggest a near-term future in which alloy design moves from intuition-guided iteration to AI-proposed, DFT-screened candidates.

A critical question, however, is whether AI-proposed compositions survive contact with physical processing. Current generative materials models, including GNoME, optimize for thermodynamic stability (formation energy, convex hull distance) but do not explicitly model the *kinetic* barriers that govern which phases actually form during quenching and annealing, nor the *interstitial chemistry* that arises from realistic carbon and nitrogen contamination, nor the *processing-rate* constraints that determine grain morphology [@merchant2023gnome]. The consequence is that an AI may propose an alloy whose target phase lies on the DFT convex hull but is kinetically inaccessible: a "reality gap" between digital prediction and physical realization. To our knowledge, this gap has not yet been quantified for an LLM-hypothesized SMA composition.

## 1.4 Research questions and hypotheses

We address two questions in this work:

1. **Reality gap.** When an LLM deep-research agent, constrained by GNoME-style stability data, proposes a novel Fe-Mn-Al-Si-Ni-C composition targeting room-temperature pseudoelasticity, does the resulting alloy exhibit the target behavior? If not, what is the dominant mode of failure, and can it be diagnosed computationally from synchrotron diffraction data alone?
2. **Grain-size paradigm.** Does the bamboo-grain requirement established by Omori and co-workers hold across all continuous-processing regimes, or can high-feed-rate strand annealing produce refined-grain microstructures with comparable or superior pseudoelastic recovery?

Our working hypotheses, stated up front, were: (H1) the AI-hypothesized alloy would be thermodynamically stable per DFT but would fail to exhibit pseudoelasticity owing to unmodeled process–structure–property couplings; (H2) bamboo grains would outperform refined grains, consistent with the established literature.

Both hypotheses are addressed below. H1 is confirmed; H2 is rejected.

## 1.5 Contributions

This work makes three contributions. First, to our knowledge it is the first reported physical synthesis and characterization of an Fe-SMA composition hypothesized by an LLM deep-research agent, with direct benchmarking against the Omori reference alloy under identical processing. Prior AI-driven SMA discovery efforts have used graph neural networks, Bayesian materials selection, and GAN-based inverse design on NiTi-family alloys [@aims2022; @generativeinversion2025], and LLM-hypothesized compositions have been experimentally validated for high-entropy alloys and halide solid electrolytes [@hu2024beyond], but the intersection of LLM deep-research alloy design and Fe-based SMA synthesis has not previously been reported. Second, it introduces a computational auditing pipeline (automated synchrotron peak detection, Bragg-law wavelength normalization, JARVIS-DFT cosine matching, and DiffractGPT structure prediction) that diagnoses the thermodynamic root cause of pseudoelastic failure from a single `.chi` diffraction file. Third, it presents evidence that refined-grain microstructures produced by high-feed-rate continuous strand annealing can exceed the pseudoelastic recovery of conventional bamboo grains, opening a route to commercially scalable Fe-SMA wire production.

---

# 2. Materials and Methods

## 2.1 Alloy design

The AI-hypothesized composition was generated by an LLM deep-research agent (Gemini 2.5 with the Deep Research tool [@comanici2025gemini]) prompted to propose an Fe-Mn-Al-based composition optimized for room-temperature pseudoelasticity. The agent was instructed to (i) reason from the Fe-Mn-Al-Ni family established by Omori and co-workers [@omori2011superelastic; @omori2017martensitic] as a starting point, (ii) consult thermodynamic-stability data from the GNoME database [@merchant2023gnome], (iii) target β-NiAl/carbide precipitation as a strengthening pathway, and (iv) minimize cost by excluding cobalt and tantalum. The agent's output, after constraint-prompted refinement, was the composition designated here as the "AI alloy."

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

The 3-cycle AGG condition follows the abnormal-grain-growth protocol of Omori *et al.* [@omori2011superelastic], designed to produce bamboo-like single-crystal-diameter grains. The strand-anneal conditions span low-to-high continuous feed rates (0.8, 4, and 20 ft/min) and are intended to probe the limit at which conventional industrial throughputs can replace the slow batch AGG cycle.

## 2.4 Metallography

Wire cross-sections were embedded in cold-mount epoxy and ground sequentially with silicon-carbide papers from 180 grit through 800 grit. Final polishing used a 0.25 µm OP-S aluminum-oxide suspension on an automated polishing wheel until a scratch-free mirror finish was achieved. Polished cross-sections were imaged on a Clemex Vision PE optical microscope under bright-field illumination at magnifications between 100× and 1000×.

## 2.5 Mechanical testing

Cyclic tensile tests were performed on an Instron servohydraulic testing frame in displacement control. Wire specimens were tested with a 6 mm gauge length using pneumatic grips. Each specimen was loaded to a target tensile strain (8% for the Omori benchmark, 10% for the AI alloy) at a nominal strain rate of 1 × 10⁻³ s⁻¹, held briefly at peak strain, and then unloaded to zero force. Pseudoelastic recovery was quantified as the ratio of recovered strain on unloading to applied peak strain.

## 2.6 Synchrotron X-ray diffraction

Synchrotron XRD measurements were performed at the ultra-hard X-ray multifunctional application beamline BL12SW of the Shanghai Synchrotron Radiation Facility (SSRF) [@ssrf2024bl12sw], in collaboration with co-author J. Yan. The incident wavelength was λ = 0.125870 Å (photon energy ≈98.5 keV), and the sample-to-detector distance was 1827.486 mm with a 100 µm × 100 µm pixel area detector. Two-dimensional Debye-Scherrer patterns were collected from each specimen before and after tensile deformation. Each 2D pattern was azimuthally integrated using Fit2D to produce a one-dimensional intensity-versus-2θ profile, written in `.chi` format.

For database comparison, synchrotron 2θ values were converted to Cu Kα-equivalent 2θ using Bragg's law:
$$
d = \frac{\lambda_{\text{sync}}}{2\sin\theta_{\text{sync}}}, \qquad
2\theta_{\text{CuK}\alpha} = 2\arcsin\!\left(\frac{\lambda_{\text{CuK}\alpha}}{2d}\right),
$$
with λ_CuKα = 1.54056 Å. Reflections corresponding to Cu Kα-equivalent 2θ > 90° were discarded as unphysical for database matching.

## 2.7 Computational audit pipeline

A custom Python pipeline (released under an open-source license at the GitHub repository associated with this work) was developed to audit the AI's compositional hypothesis against first-principles thermodynamics directly from synchrotron data. The pipeline executes four stages (**Fig. 1**):

1. **Peak detection.** Raw `.chi` profiles are loaded with automatic header parsing, normalized to unit intensity, and processed with the SciPy `find_peaks` routine using prominence-based filtering (prominence threshold 0.01–0.05 depending on signal-to-noise).
2. **Wavelength normalization.** Detected peaks are converted from the synchrotron geometry to Cu Kα-equivalent 2θ using the Bragg-law relations above.
3. **JARVIS-DFT cosine matching.** The experimental peak set is scored by cosine similarity against simulated XRD patterns for 166 Fe-Al candidates from the JARVIS-DFT database [@choudhary2020jarvis]. The top-ranked candidates are reported with formation energies and space-group assignments.
4. **DiffractGPT structure prediction (optional).** When an AGAPI key is provided, the peak set and chemical formula are passed to DiffractGPT [@choudhary2024diffractgpt], which returns a predicted POSCAR crystal structure. Without an API key, the pipeline falls back to the local JARVIS match.

Formation energies of competing phases (L2₁ MnAlFe₂, B2 AlFe, B2 AlFe₃) were retrieved directly from JARVIS-DFT for cross-validation of the AI's composition prediction against first-principles thermodynamics.

![**Fig. 1.** Schematic of the custom computational audit pipeline for synchrotron peak analysis. Synchrotron `.chi` files enter the peak-detection stage (SciPy prominence-filtered peak finding, with Bragg-law conversion of synchrotron 2θ to Cu Kα-equivalent 2θ), feed into both a pattern-matching branch (JARVIS-DFT database, cosine-similarity scoring over 166 Fe-Al candidates) and a structure-prediction branch (DiffractGPT inference of crystal structure from formula + peak data), and terminate in a cross-validation step against JARVIS-DFT formation energies and competing-phase thermodynamic stability.](figures/Fig1_pipeline_schematic.png)

---

# 3. Results

## 3.1 Microstructure

Optical micrographs of polished wire cross-sections for the four most informative heat-treatment conditions are shown in **Fig. 2**.

After the standard 1200 °C / 1 min anneal, the AI alloy (**Fig. 2a**) exhibits a highly refined dual-phase morphology with irregular grain boundaries and no single dominant phase. Following the 3-cycle AGG treatment (**Fig. 2b**), the AI alloy continues to show a dual-phase structure: grain growth occurred only in one of the two phases, while the second phase remained as fine, dispersed regions. The dual-phase character persisted across every AI-alloy condition examined, indicating that the AI's predicted composition does not support single-phase austenite formation under any of the heat treatments tested in this study.

The Omori benchmark behaves differently. After 3-cycle AGG (**Fig. 2c**), the Omori alloy develops the bamboo-like grain morphology consistent with the established Fe-Mn-Al-Ni paradigm [@omori2011superelastic; @vollmer2016cyclic], with grain diameters spanning a substantial fraction of the wire cross-section. The 1200 °C / 1 min condition (**Fig. 2d**) yields an acicular ferrite microstructure: a grain size large enough to permit partial martensitic nucleation but insufficient to support fully unconstrained transformation. By contrast, a 1200 °C / 12 s strand-anneal condition (not shown in Fig. 2) produces a uniformly refined small-grain microstructure, which is the configuration responsible for the highest pseudoelastic recovery measured in this work (Sec. 3.2).

![**Fig. 2.** Optical micrographs of polished wire cross-sections under four representative heat-treatment conditions. (a) AI alloy after the standard 1200 °C / 1 min anneal: highly refined dual-phase morphology with irregular grain boundaries (scale bar 0.004 in.). (b) AI alloy after 3-cycle AGG: grain growth in one phase only; the dual-phase structure persists (scale bar 400 µm). (c) Omori benchmark after 3-cycle AGG: bamboo-like grain morphology consistent with the Omori paradigm (scale bar 200 µm). (d) Omori benchmark after 1200 °C / 1 min strand anneal: acicular ferrite microstructure (scale bar 200 µm). All images acquired on a Clemex Vision PE optical microscope under bright-field illumination.](figures/Fig2_microstructure_composite.png)

## 3.2 Cyclic stress–strain response

Cyclic tensile stress–strain curves for representative specimens are shown in **Fig. 3**.

The AI alloy in both the 1200 °C / 1 min (**Fig. 3a**) and 3-cycle AGG (**Fig. 3b**) conditions displays essentially zero pseudoelastic recovery on unloading. Loading exhibits a monotonically rising stress with no defined transformation plateau, and unloading retraces a linear-elastic slope down to negligible recovered strain. The macroscopic behavior is consistent with plastic deformation by dislocation slip rather than stress-induced martensitic transformation (SIMT). This response is invariant across all AI-alloy heat treatments examined.

The Omori benchmark shows the expected pseudoelastic response in conditions that develop the bamboo or refined-grain microstructures (**Fig. 3c, d**). Importantly, the 1200 °C / 12 s strand-anneal condition (refined small grains) exhibits approximately twice the total recovered strain of the 1200 °C / 5 min condition (larger grain growth, closer to the conventional bamboo paradigm) under identical applied strain. This direct comparison, performed on the same alloy chemistry with the only variable being strand-anneal residence time, is the central observation of Sec. 4.3.

![**Fig. 3.** Cyclic tensile stress–strain response. (a) AI alloy after the standard 1200 °C / 1 min anneal: monotonic loading with no transformation plateau and essentially zero recoverable strain on unloading, consistent with dislocation slip. (b) AI alloy after 3-cycle AGG: response qualitatively identical to (a), confirming that AGG processing does not restore pseudoelasticity in the AI composition. (c) Omori benchmark after 1200 °C / 5 min strand anneal (larger grain growth): partial pseudoelastic recovery with developing hysteresis. (d) Omori benchmark after 1200 °C / 12 s strand anneal (refined small-grain microstructure): pronounced pseudoelastic hysteresis, a distinct stress plateau, and approximately twice the total recovered strain of the 5 min condition under identical applied strain. Red arrows in (c, d) mark the residual unrecovered strain after unloading.](figures/Fig3_stressstrain_composite.png)

## 3.3 Synchrotron diffraction

### 3.3.1 One-dimensional patterns

Azimuthally integrated synchrotron XRD patterns, converted to Cu Kα-equivalent 2θ, are shown in **Fig. 4** for the AI alloy and the Omori benchmark before and after deformation.

The AI alloy (**Fig. 4a**) exhibits a five-peak pattern indexable to a coexisting FCC γ-austenite and B2/DO₃-ordered Fe₃Al phase. Comparison of the 0% strain and 10% strain patterns shows that peak positions and relative intensities are essentially unchanged: no new reflections appear, no existing reflections disappear, and the dual-phase signature is preserved. This is a direct diffraction-level confirmation that the macroscopic strain in **Fig. 3a, b** is accommodated by dislocation slip rather than by a phase transformation.

The Omori benchmark (**Fig. 4b**) presents a BCC α-dominated pattern with ordered β-NiAl (B2) precipitate reflections in the undeformed state. After 8% applied strain, the {111}γ reflection intensifies and the overlapping {200}α / {200}B2 cluster redistributes in intensity. These intensity shifts are consistent with stress-induced γ formation and partial variant activation of the precipitate-coherent transformation.

![**Fig. 4.** Azimuthally integrated synchrotron XRD patterns converted to Cu Kα-equivalent 2θ, comparing the undeformed (0% strain) and deformed (post-tensile-test) states. (a) AI alloy: five-peak pattern indexable to coexisting FCC γ-austenite ({111}γ, {200}γ, {220}γ) and ordered B2/DO₃ Fe₃Al phase ({220}Fe₃Al, {400}Fe₃Al); the 0% and 10% strain patterns are essentially superimposed, indicating deformation by dislocation slip rather than phase transformation. (b) Omori benchmark: BCC α-dominated pattern with ordered β-NiAl (B2) precipitate reflections; after 8% strain the {111}γ reflection intensifies and the {200}α / {200}B2 cluster redistributes in intensity, consistent with stress-induced γ formation and partial variant activation. Data collected at SSRF beamline BL12SW with λ = 0.125870 Å.](figures/Fig4_XRD_1D_AI_vs_Omori.jpg)

### 3.3.2 Two-dimensional patterns

Two-dimensional Debye–Scherrer patterns recorded directly on the SSRF area detector are shown in **Fig. 5** for the same four specimen states. The AI alloy rings (**Fig. 5a, b**) are virtually identical before and after deformation: ring positions, widths, and azimuthal intensity distributions are preserved. The Omori benchmark rings shift from sharp, discrete diffraction spots in the undeformed state (**Fig. 5c**) to broader, partially arced rings in the deformed state (**Fig. 5d**). The transition from spotty to arced rings is the signature of variant activation and increased mosaic spread accompanying partial martensitic transformation.

![**Fig. 5.** Two-dimensional Debye–Scherrer synchrotron diffraction patterns recorded directly on the SSRF area detector for the same four specimen states. (a) AI alloy at 0% strain: sharp, discrete diffraction spots indexed to {111}γ, {200}γ, {220}γ on the γ-FCC subpattern and {220}Fe₃Al, {400}Fe₃Al on the DO₃ subpattern. (b) AI alloy at 10% strain: ring positions, widths, and azimuthal intensity distributions are preserved with no detectable redistribution, consistent with the absence of phase transformation indicated by Fig. 4a. (c) Omori benchmark at 0% strain: discrete spots indicating coarse, well-oriented grains. (d) Omori benchmark at 8% strain: spots transition to broader, partially arced rings, the signature of variant activation and increased mosaic spread accompanying partial martensitic transformation.](figures/Fig5_XRD_2D_composite.png)

### 3.3.3 Phase fraction analysis

Quantitative comparison of phase-peak intensities before and after deformation for all four sample pairs is summarized in **Table 3**.

**Table 3.** Relative change in integrated peak intensity for the {111}γ, B2/Fe₃Al, and β-NiAl reflections between the undeformed and deformed states, for both alloys under both AGG and 4 ft/min strand-anneal conditions. Positive values indicate intensity increase; negative values indicate decrease.

| Sample | Condition | Δ{111}γ | ΔB2/Fe₃Al | Δβ-NiAl | Phase transformation? |
|--------|-----------|---------|-----------|---------|----------------------|
| AI alloy   | 3-cycle AGG, 0 → 10% strain  | +49.7%  | −28.4%   | +23.7% | No (texture redistribution only) |
| AI alloy   | 4 FPM strand, 0 → 10% strain | +32.2%  | +51.3%   | −17.1% | No (texture redistribution only) |
| Omori      | 4 FPM strand, 0 → 8% strain  | +27.3%  | +40.7%   | −83.8% | Yes (α → γ, irreversible) |
| Omori      | 3-cycle AGG, 0 → 8% strain   | −43.1%  | −0.6%    | +1.3%  | No (γ suppression in bamboo grains) |

The relative intensity changes in the AI-alloy entries are interpreted as texture redistribution under load (preferred orientation development) rather than phase transformation, because (i) no new reflections appear in the 1D patterns, (ii) the 2D ring positions are unchanged, and (iii) the changes are of the wrong sign and magnitude to be consistent with an α → γ or B2 → L1₀ transformation pathway.

## 3.4 Computational audit and Reality-Gap quantification

The synchrotron peak set from the AI-alloy 3-cycle AGG sample was processed through the pipeline of Sec. 2.7. The top-ranked JARVIS-DFT phase matches and their DFT formation energies are listed in **Table 4**.

**Table 4.** Top JARVIS-DFT phase matches for the AI-alloy synchrotron pattern, with cosine similarity and formation energy. Adapted from the JARVIS-DFT database [@choudhary2020jarvis].

| Rank | JVASP ID    | Formula    | Space group | Cosine score | E_form (eV/atom) | Role |
|------|-------------|------------|-------------|--------------|------------------|------|
| 1    | JVASP-99748 | AlFe₃      | Pm-3m (B2)  | **0.606**    | −0.179           | Dominant experimental phase |
| 2    | JVASP-99397 | TiAlFe₂    | P4/mmm      | 0.452        | −0.441           |  |
| 3    | JVASP-8743  | TiAlFe₂    | Fm-3m (L2₁) | 0.433        | −0.497           | AI target phase analogue (Heusler) |
| 4    | JVASP-15000 | AlFe       | Pm-3m (B2)  | 0.388        | **−0.358**       | Secondary B2 contributor |
| 5    | JVASP-86274 | Al₆Fe      | Cmcm        | 0.348        | −0.213           |  |

The dominant cosine match (rank 1, score 0.606) is to a B2-ordered AlFe₃ phase. The L2₁ Heusler analogue ranks third in cosine similarity (0.433), confirming that an L2₁ component is present in the diffraction signal but is not the majority phase. Among the binary Fe-Al phases relevant to the AI alloy's reduced chemistry, B2 AlFe (JVASP-15000) has a DFT formation energy of −0.358 eV/atom, while the L2₁ MnAlFe₂ Heusler target (JVASP-18826) has a formation energy of −0.195 eV/atom [@choudhary2020jarvis]. The B2 phase is therefore 0.163 eV/atom more thermodynamically stable than the AI's target L2₁ matrix.

We refer to this 0.163 eV/atom offset as the *Reality Gap*: a quantitative thermodynamic margin, accessible from a single synchrotron `.chi` file and a public DFT database, that was invisible to the AI's formation-energy-only optimization because the AI proposed the L2₁ phase without comparing its stability to the full set of competing binary phases accessible during arc-melt solidification. The carbon content of 0.105 wt% in the AI composition further stabilizes BCC/B2 over FCC austenite through Zener-style interstitial ordering on octahedral sites, compounding the thermodynamic preference for the observed dual-phase microstructure [@zener1948; @bhadeshia2010steels].

---

# 4. Discussion

## 4.1 Why the AI alloy failed: thermodynamic and kinetic origins of the Reality Gap

Three mutually reinforcing mechanisms explain the failure of the AI-hypothesized composition to exhibit room-temperature pseudoelasticity.

First, **thermodynamic competition in the binary Fe-Al limit**. The DFT formation energies of the candidate phases retrieved from JARVIS [@choudhary2020jarvis] place B2 AlFe at −0.358 eV/atom and the target L2₁ MnAlFe₂ Heusler at −0.195 eV/atom. The B2 phase is therefore 0.163 eV/atom more stable than the AI's intended matrix. Because formation energy varies by less than this margin across most reasonable Mn and Ni substitutions in the binary, no realistic alloying perturbation of the AI's composition can invert the phase ordering. The L2₁ Heusler is a real stable phase, but it cannot win the phase competition against B2 under the processing conditions used here.

Second, **interstitial stabilization of BCC/B2 by carbon**. The AI's prompt included carbon (0.1–0.3 wt%) as a strengthening interstitial intended to nucleate carbide precipitates. In practice, carbon sits on octahedral interstitial sites of BCC iron and the B2 sublattice, lowering BCC and B2 free energy relative to FCC austenite through the well-known Zener ordering mechanism [@zener1948; @bhadeshia2010steels]. Even modest carbon contents (≥0.05 wt%) are sufficient to suppress the FCC → BCC transformation temperature significantly in Fe-Mn-Al alloys, and the 0.105 wt% present in the AI alloy compounds the thermodynamic preference for the observed dual-phase microstructure.

Third, **magnetic disorder during AGG cooling**. The L2₁ MnAlFe₂ Heusler is a ferrimagnet with a Curie temperature near 800 K and a DFT magnetic moment of 2.04 µB per formula unit. The 3-cycle AGG anneal at 1200 °C exceeds this Curie temperature, and the absence of a directional magnetic field during cooling prevents single-variant martensitic selection on cooling. While magnetic coupling is not the primary driver of failure, it precludes the magnetic-shape-memory pathway that has been exploited successfully in related Ni-Mn-Ga and Ni-Mn-In systems [@otsuka2005physical].

The macroscopic consequence is the response observed in **Fig. 3a, b** and **Fig. 4a**: the critical stress to trigger stress-induced martensitic transformation in the AI alloy exceeds the yield stress for dislocation slip, so the wire accommodates strain plastically and shows no recoverable component on unloading. The Reality Gap is therefore not an artifact of incomplete characterization but a quantitative, predictable consequence of a thermodynamic offset that the AI's training data did not surface.

## 4.2 What process-aware AI must add

The Reality Gap diagnosed above is fundamentally a *modeling* gap rather than a *data* gap. The relevant DFT formation energies are present in JARVIS-DFT and were retrievable in seconds; the relevant carbon-stabilization literature is decades old [@zener1948]. What was missing was a reasoning loop that connected the AI's compositional proposal back to (i) the full set of competing phases accessible by the proposed synthesis route, (ii) the interstitial chemistry of carbon during arc-melt solidification, and (iii) the magnetic state of the target phase during high-temperature processing.

A "process-aware" generative materials AI should therefore integrate at least the following capabilities:

1. **Convex-hull comparison across competing phases**, not formation-energy ranking of the target phase in isolation. The 0.163 eV/atom offset diagnosed here would have been flagged automatically by a routine convex-hull lookup over the Fe-Al binary.
2. **Interstitial-corrected stability surfaces** for non-stoichiometric impurities (C, N, B) at concentrations comparable to the proposed composition. ALIGNN-class predictors trained on substitutional + interstitial datasets are a near-term path to this capability [@choudhary2021alignn].
3. **Processing-rate and feed-rate constraints** that determine which microstructural pathway is accessible at industrial throughputs. Current generative models output a composition; they do not output a *processing recipe* compatible with continuous manufacturing, and the small-grain result in Sec. 3.2 demonstrates that processing-route choice is decisive.
4. **Magnetic-state coupling** for SMAs whose target phase is ferromagnetic or ferrimagnetic, particularly when AGG cycles cross the Curie temperature.

We emphasize that these capabilities are not aspirational: each can be implemented today as a deterministic post-prompt check against existing public databases (JARVIS, GNoME, Materials Project), prior to commissioning physical synthesis.

## 4.3 The small-grain paradigm: an unexpected processing window

The cyclic-tensile result in **Fig. 3c, d**, that a 1200 °C / 12 s strand-anneal condition produces approximately twice the pseudoelastic recovery of a 1200 °C / 5 min condition on the same Omori-benchmark chemistry, is in direct tension with the bamboo-grain requirement that has dominated the Fe-Mn-Al-Ni literature since 2011 [@omori2011superelastic; @vollmer2016cyclic; @abuzaid2019femnnial]. Two mechanistic explanations are plausible and not mutually exclusive.

First, **grain-boundary constraint on variant selection**. The bamboo-grain paradigm was originally motivated by the observation that severe inter-granular stress concentrations in fine polycrystals lead to premature brittle failure. However, when grains are small enough that several grains span the cross-section but each grain is fully embedded in a coherent matrix, grain-boundary constraint can *select* favorable martensitic variants and suppress the accumulation of unrecoverable plastic strain. The 12 s strand-anneal microstructure, with its uniformly refined grain morphology, may sit in a window in which constraint aids variant selection without driving intergranular cracking.

Second, **suppression of precipitate coarsening**. The β-NiAl precipitate intensity decreases by 83.8% in the 4 FPM Omori sample on deformation (**Table 3**, row 3), consistent with stress-induced precipitate shearing or dissolution. In a slower AGG cycle, β-NiAl precipitates coarsen and become more difficult to shear, which raises the threshold for the cooperative precipitate-coherent transformation. Faster strand-anneal conditions may retain a finer, more shearable precipitate dispersion that lowers the SIMT threshold.

Both mechanisms predict that the small-grain regime is a *processing window* bounded above and below: too slow a feed rate yields bamboo grains with coarsened precipitates, while too fast a feed rate fails to relieve work-hardening from cold drawing and reintroduces the as-drawn dislocation density. Mapping this window quantitatively across 0.8, 4, and 20 FPM (and ideally additional feed rates) is the most immediate experimental follow-up to this work.

The broader significance of this finding is that the bamboo-grain requirement, which has been treated as a material-physics constraint, is at least partially a processing-route artifact. If high-feed-rate continuous strand annealing can deliver pseudoelastic performance equal to or better than slow batch AGG, then Fe-SMA wire production becomes compatible with conventional steel-wire infrastructure, removing what has been the principal economic objection to industrial Fe-SMA scale-up.

## 4.4 Computational auditing as a pre-synthesis screen

A practical contribution of this work, separable from the specific Fe-SMA findings, is that the entire diagnostic chain, from a raw synchrotron `.chi` file to a quantitative Reality Gap in eV/atom, can be executed in under a minute on a laptop using only public databases and open-source code. The peak-detection, Bragg-law wavelength normalization, JARVIS cosine match, and formation-energy lookup steps require no proprietary software and no GPU. For research programs evaluating AI-proposed compositions before committing to weeks of arc-melting, hot-rolling, and synchrotron beam time, this kind of pre-synthesis or post-synthesis audit is a low-cost screen with a high information yield.

A natural extension is to invert the workflow: rather than auditing failed AI compositions post hoc, the same pipeline can be invoked *during* the AI's compositional search to penalize candidates whose target phase is thermodynamically dominated by a binary competitor. We expect this kind of differentiable convex-hull penalty to become standard in next-generation alloy-design agents.

## 4.5 Limitations

Several limitations of the present work should be noted before drawing broader conclusions.

First, **phase fractions are reported qualitatively rather than quantitatively**. Full Rietveld refinement on the SSRF `.chi` files using GSAS-II or FullProf would convert the relative intensity changes in **Table 3** into absolute phase fractions and reduce the dependence on cosine-similarity scoring. This refinement is in progress and will be reported separately.

Second, **the small-grain paradigm is established here on a limited set of feed rates** (0.8, 4, and 20 ft/min) and limited replicates per condition. A systematic feed-rate sweep with replicates and statistical error bars is needed before the result can be elevated from observation to design rule.

Third, **electron backscatter diffraction (EBSD) was not performed** in this work. EBSD on the small-grain Omori specimens would directly resolve variant selection and grain-boundary character distribution, which would test the constraint-on-variant-selection mechanism proposed in Sec. 4.3.

Fourth, **the AI's composition was not iterated**. The Reality Gap is reported for a single LLM-proposed composition; whether iterative feedback (DFT screening in the LLM's reasoning loop) would converge to a successful Fe-SMA composition is an open question that this study does not address.

---

# 5. Conclusions

We have synthesized, mechanically tested, and computationally audited an Fe-Mn-Al-Si-Ni-C composition proposed by an LLM deep-research agent, alongside the established Omori Fe-Mn-Al-Ni benchmark, in a single experimental campaign with identical processing. Four conclusions follow.

1. **The Reality Gap is real and quantifiable.** The AI-hypothesized composition is thermodynamically stable on the DFT convex hull but fails to exhibit room-temperature pseudoelasticity. The root cause is a 0.163 eV/atom thermodynamic offset between the target L2₁ Heusler matrix and a B2 AlFe-type competing phase, compounded by carbon-driven Zener stabilization of BCC/B2 at the alloy's interstitial chemistry. This offset is fully accessible from public DFT databases and would have been flagged by a routine convex-hull check.
2. **Process-aware materials AI requires four additional capabilities** beyond formation-energy ranking: convex-hull comparison against competing phases, interstitial-corrected stability surfaces, processing-rate awareness, and magnetic-state coupling for ferromagnetic targets. Each is implementable as a deterministic post-prompt check today.
3. **The bamboo-grain paradigm is not universal.** A 1200 °C / 12 s continuous strand-anneal condition on the Omori benchmark produces refined-grain microstructures with approximately twice the pseudoelastic recovery of a 1200 °C / 5 min condition, in direct contradiction to the prevailing requirement for slow abnormal grain growth. This opens a commercially scalable processing window for Fe-SMA wire that is compatible with conventional steel-wire infrastructure.
4. **Synchrotron-to-DFT computational auditing is a low-cost pre-synthesis screen.** The full pipeline from a raw `.chi` file to a quantitative Reality Gap requires no proprietary software and runs in under a minute on a laptop, making it suitable for routine deployment alongside generative alloy-design agents.

The overall message is that AI-guided alloy discovery, in its current generation, requires explicit integration of kinetic, interstitial, and processing-rate constraints before its proposals can be trusted to survive physical synthesis. The Reality Gap reported here is not an indictment of AI materials discovery: it is a diagnostic that points to the specific capabilities that the next generation of process-aware materials agents must acquire.

---

# Acknowledgments

The authors thank Fort Wayne Metals for providing access to arc-melting, hot-rolling, cold-drawing, and metallography facilities, and for technical guidance throughout alloy synthesis. The authors also thank the Shanghai Synchrotron Radiation Facility for beam time at BL12SW. JARVIS-DFT and DiffractGPT are public resources of the NIST Materials Genome Initiative and AtomGPT.org respectively. No conflicts of interest are declared.

---

# Data and code availability

The custom Python pipeline used for peak detection, wavelength normalization, JARVIS cosine matching, and DiffractGPT inference is publicly available at <https://github.com/frankcai222/fe-sma-xrd>. Raw synchrotron `.chi` files, Instron cyclic-tensile export data, and metallographic images are available from the corresponding author on reasonable request.

---

<!-- REFERENCES TO FOLLOW IN BIBLIOGRAPHY BUILD -->
