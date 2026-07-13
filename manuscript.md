# Abstract

Iron-based shape memory alloys (Fe-SMAs) offer a low-cost alternative to Nitinol, but their super-elastic response is highly sensitive to composition and processing. Large language model (LLM) deep-research agents can now propose new alloy compositions in seconds, raising the question of whether such proposals actually work once synthesized. Here we report the synthesis and mechanical characterization of an LLM-hypothesized Fe-Mn-Al-Si-Ni-C composition, benchmarked against an established super-elastic Fe-Mn-Al-Ni alloy processed under identical conditions. The AI-hypothesized alloy was readily castable but failed to exhibit super-elasticity under any condition tested, deforming instead like a conventional elastic metal. Synchrotron X-ray diffraction showed that this failure stems from a phase-stability mismatch: the AI alloy forms a stable dual-phase microstructure with a minor ordered Fe-Al phase that does not support the transformation pathway the benchmark alloy relies on, likely promoted by its elevated carbon content. We conclude that LLM-proposed alloy compositions cannot be assumed to work as intended and should be screened for competing phase stability and interstitial content before physical synthesis is attempted.

**Keywords:** Fe-based shape memory alloy; super-elasticity; AI-guided alloy design; synchrotron XRD; abnormal grain growth

---

# 1. Introduction

Materials discovery has been advanced by deep-learning models trained on first-principles thermodynamics. For example, DeepMind's GNoME predicted more than 2.2 million previously unreported crystal structures with high precision against DFT validation [@merchant2023gnome], and agentic large language models with deep-research capabilities can ingest decades of metallurgical literature and propose compositions in seconds [@comanici2025gemini; @xu2025deepresearch]. Together these tools raise the possibility of alloy design that supplements intuition-guided iteration with AI-proposed, thermodynamically screened candidates. Recent studies have begun applying such AI methods specifically to shape memory alloys, including data-driven composition screening [@aims2022], generative inverse design [@generativeinversion2025], and LLM-based hypothesis generation [@hu2024beyond]. However, whether these AI models practically work or not is yet to be tested. Current generative materials models typically optimize for thermodynamic stability (formation energy, convex-hull distance) but may not, in general, explicitly consider the kinetic barriers governing microstructure evolution during processing [@merchant2023gnome]. A composition whose target phase lies on the DFT convex hull might still be difficult to realize in practice. It is our interest to examine a large language model (LLM)-hypothesized shape memory alloy (SMA). To the best of our knowledge, experimentally validated studies on this topic remain very rare.

SMAs exhibit reversible martensitic transformations that enable two technologically important behaviors: the shape memory effect, in which thermally induced phase changes recover macroscopic deformation, and super-elasticity, in which stress-induced martensite reverts upon unloading [@otsuka2005physical; @lagoudas2008shape]. As the dominant commercial SMA, Nitinol, a near 50Ni-50Ti alloy, offers large recoverable strains of 6–8%, excellent cyclic stability, and biocompatibility, which make it widely used in medical devices, aerospace actuators, and damping applications [@duerig1999overview; @mohd2014nitinol]. However, due to its relatively high manufacturing cost, the application of Nitinol in structural engineering such as prestressing tendons for concrete and seismic dampers remains very limited.

Fe-based shape memory alloys offer a path to lower cost [@cladera2014ironbased]. The work of Omori *et al.* found that certain Fe-Mn-Al-Ni alloys were capable of large strain recovery at room temperature after abnormal grain growth (AGG) [@omori2011superelastic], where a bamboo-like grain structure, or single-crystal-diameter grains spanning the wire cross-section, is produced by cyclic heat treatments across the FCC γ ↔ BCC α phase boundary. Subsequent studies have associated such large grains with reduced inter-granular constraint and improved transformation reversibility in the BCC α / FCC γ system [@vollmer2016cyclic; @abuzaid2019femnnial]. However, achieving a bamboo-like grain structure poses significant challenges, especially at industrial scale. In this study, we adopted this alloy system, trained an AI with over 200 published papers on Fe-based SMAs along with other publicly available information, and asked the AI for lower-cost alternatives with the potential to exhibit super-elasticity with small grain sizes. We processed one of the AI-hypothesized compositions alongside the alloy reported by Omori *et al.* [@omori2011superelastic]. Because the processing history was kept identical for both alloys, compositional differences are the sole variable determining the final mechanical properties.

---

# 2. Materials and Experiments

## 2.1 Alloy design and synthesis

The AI-hypothesized composition was generated by an LLM deep-research agent (Gemini 2.5 with the Deep Research tool [@comanici2025gemini]) prompted to propose an Fe-Mn-Al-based composition optimized for room-temperature super-elasticity. The agent was instructed to (i) reason from the Fe-Mn-Al-Ni family established by Omori and co-workers [@omori2011superelastic; @omori2017martensitic] as a starting point and search for even cheaper alternatives, (ii) consult thermodynamic-stability data, (iii) target β-NiAl/carbide precipitation as a strengthening pathway, and (iv) minimize cost by excluding cobalt and tantalum. Within one of the AI-suggested composition ranges, we selected a composition of 50Fe-30Mn-12Al-4Ni-4Si (at%) with an additional 1000 ppm C, where the Fe, Mn, Al, and Ni are intended to form a BCC parent phase and β (NiAl-type) precipitates. Ni content is kept moderate to lower cost. Si is added to strengthen the parent BCC matrix through solid-solution strengthening; Si is also known to increase resistance to slip in ferritic structures and could potentially modify the stability or morphology of β precipitates, or influence stacking-fault energy. C is added for interstitial strengthening of the parent phase and possible formation of very fine, dispersed carbides. For direct comparison, a second alloy of composition 43.5Fe-34Mn-15Al-7.5Ni (at%), based on the work of Omori *et al.* [@omori2011superelastic], was synthesized under identical conditions. These alloys are hereafter named the AI-alloy and Omori-alloy, respectively.

Using high-purity raw elements, about 2 kg of each alloy was melted in a vacuum induction furnace and cast into ø50 mm ingots. Alloy chemistries are listed in **Table 1**. For both alloys, the actual chemistries measured by inductively coupled plasma atomic emission spectroscopy (ICP-AES) are very close to the nominal values, except that Si is lower in the AI-alloy and unexpected P is present in the Omori-alloy; the source of the P is unknown. Several ø13 mm rods were cut from the cast ingots by electrical discharge machining (EDM). These rods were homogenized at 1000 °C for 16 hours in argon atmosphere, then hot-rolled at 850 °C in multiple passes to reduce thickness, and subsequently cold-drawn to a final wire diameter of 0.36 mm. Severe work hardening during cold drawing necessitated intermediate annealing at 1000 °C under argon to restore ductility between draw passes. The amount of cold drawing was ≈85% area reduction after the last process anneal.

**Table 1.** Chemistries (in wt%) of the two alloys as measured by inductively coupled plasma atomic emission spectroscopy (ICP-AES). Carbon was measured by ASTM E1019. Elements present at less than 0.01 wt% are not listed.

| Element | AI-alloy (nominal) | AI-alloy (actual) | Omori-alloy (nominal) | Omori-alloy (actual) |
|---------|---------------------|---------------------|-------------------------|-------------------------|
| Fe      | 54.5                | 55.83               | 47.08                   | 46.51                   |
| Mn      | 32.3                | 31.78               | 36.43                   | 36.49                   |
| Al      | 6.4                 | 6.24                | 7.9                      | 8.00                     |
| Ni      | 4.6                 | 4.81                | 8.59                     | 8.94                     |
| Si      | 2.2                 | 1.11                | –                        | <0.01                    |
| C       | 0.1                 | 0.105               | –                        | 0.01                     |
| P       | –                   | –                   | –                        | 0.06                     |

## 2.2 Heat treatments

To test the effect of heat-treating temperature on mechanical properties, cold-drawn wires were heat treated in a strand furnace filled with argon at temperatures between 600 and 1200 °C for a dwell time of 1 to 40 minutes, followed by fast cooling to room temperature. In addition, to produce a bamboo-like microstructure, wires were heat treated at 1200 °C for 30 minutes followed by water quench, then re-heated to 900 °C and held for 15 minutes; this cycle was repeated three times before a final heat treatment at 1200 °C for 60 minutes followed by water quench. The same heat treatment has been used by others to promote abnormal grain growth [@omori2016agg]. Heat treatment above 1200 °C caused severe oxidation or furnace contamination.

## 2.3 Metallography

Wire cross-sections were embedded in cold-mount epoxy and ground sequentially with silicon-carbide papers from 180 grit through 800 grit. Final polishing used a 0.25 µm OP-S aluminum-oxide suspension on an automated polishing wheel until a scratch-free mirror finish was achieved. Polished cross-sections were imaged on a Clemex Vision PE optical microscope under bright-field illumination at magnifications between 100× and 1000×. In addition, scanning electron microscopy (SEM) and energy-dispersive spectroscopy (EDS) were used to study microstructure and local chemistry.

## 2.4 Mechanical testing

Room-temperature cyclic tensile testing was performed on an Instron in displacement control. During the test, each specimen was cyclically loaded to fracture with a 1% strain increment for each cycle. The sample gauge length was 13 mm and the strain rate was 1 × 10⁻³ s⁻¹. This test reveals the material's super-elasticity. A special loading–unloading–heating cyclic tensile test was also conducted to evaluate any potential shape-memory response. In this case, selected samples were loaded to 3% strain, unloaded to zero stress, and continued to zero strain. At the same time, the sample was heated to ≈200 °C to trigger any potential reversal of martensite to austenite. In this test, any shape-memory effect would be revealed during the heating stage, which causes the reloading stress to rise at a lower deformation strain.

## 2.5 Synchrotron X-ray diffraction

To identify phase constitution and potential phase change, synchrotron XRD measurements were performed at the ultra-hard X-ray multifunctional application beamline BL12SW of the Shanghai Synchrotron Radiation Facility (SSRF) [@tai2024ssrf; @yang2024ssrf]. The incident wavelength was λ = 0.12587 Å with a beam size of 0.5 × 0.5 mm². Two-dimensional Debye–Scherrer patterns were collected from each specimen before and after tensile deformation to test for any potential phase transformation. These 2D images were processed using FIT2D [@hammersley1998fit2d], where diffraction data were sliced at 5-degree intervals along the 360-degree azimuth and integrated to generate 72 diffraction spectra, which were then fitted by Rietveld refinement [@rietveld1969] in MAUD software [@lutterotti1997maud] to identify phase constitutions, volume fractions, and crystal orientations of the different phases.

---

# 3. Experiment Results

## 3.1 Microstructure

**Fig. 1a** shows the microstructure of the AI alloy after heat treatment at 1200 °C for 1 minute. The material exhibits a highly refined, fine-grained equiaxed microstructure with average grain diameters well under 20 µm. Scanning electron microscopy (**Fig. 1b**) identifies this morphology as an intimate mixture of a matrix (darker grey area) interlocked with blocky islands (brighter areas). EDS analysis detected higher Al content in the matrix but more Mn in the blocky islands, suggesting that the AI alloy has a dual-phase structure, where the Al-rich areas are likely BCC α-phase and the Mn-rich areas are FCC γ-phase. Prolonging the annealing duration to 40 minutes at the same temperature (**Fig. 1c**) induces drastic grain-boundary migration driven by the reduction of total interfacial free energy, resulting in severe grain growth and structural coarsening: the initial fine network is completely replaced by a coarse morphology with individual grains exceeding 100 µm in width. However, the dual-phase nature remains unchanged even after prolonged heat treatment at this temperature, as discussed further below.

![**Fig. 1.** Microstructure of the AI alloy after heat treatment: (a) 1200 °C, 1 min, optical; (b) 1200 °C, 1 min, SEM; (c) 1200 °C, 40 min, optical.](figures/Figure_1.jpg)

## 3.2 Cyclic stress–strain response

Cyclic tensile stress–strain curves for the AI alloy after heat treatment at different temperatures are shown in **Fig. 2**, and the corresponding data are listed in **Table 2**. This information reveals a broad picture of how heat treatment governs the alloy's mechanical properties. The response is strongly anneal-dependent: low strand-anneal temperatures (600–700 °C) leave the wire high-strength but brittle (tensile strengths of ≈2009–2293 MPa and yield strengths of ≈1683–1948 MPa, but elongation of only ≈2%), reflecting incomplete recrystallization of the cold-drawn wire, whereas annealing at 800–1200 °C progressively softens the wire and restores ductility, with elongation peaking near 33% at 1000 °C. The elastic modulus, E, stays in the ≈150–165 GPa range across the well-annealed conditions. Across all AI-alloy heat treatments examined, the stress–strain curves rose monotonically with no defined transformation plateau, and the recovered strain on unloading is comparable to the elastic strain (σ/E) expected at the unload stress. In other words, the strain recovery is consistent with elastic springback alone, with no resolvable pseudo-elastic contribution. It has been reported that aging at 200 °C can improve the pseudo-elasticity of Fe-Mn-Al-Ni alloy [@tanaka2010science; @vollmer2019natcomm]; this was not the case for the AI alloy (**Fig. 2f**).

**Table 2.** Mechanical properties of the AI alloy after heat treatment for 1 minute at different temperatures.

| Temp. (°C) | σ₀.₂ (MPa) | UTS (MPa) | Elong. (%) | E (GPa) |
|------------|------------|-----------|------------|---------|
| As drawn   | 1528       | 1925      | 2.0        | 143.7   |
| 600        | 1948       | 2293      | 2.3        | 157.4   |
| 700        | 1683       | 2009      | 2.2        | 164.8   |
| 800        | 1167       | 1216      | 24.0       | 155.5   |
| 900        | 944        | 1078      | 29.7       | 152.2   |
| 1000       | 673        | 967       | 33.4       | 155.6   |
| 1100       | 556        | 947       | 29.7       | 156.8   |
| 1200       | 502        | 938       | 23.9       | 163.0   |

![**Fig. 2.** Cyclic stress–strain curves of the AI alloy after annealing for 1 minute at various temperatures. Wire diameter is 0.36 mm. Panel (f) shows the stress–strain response of the annealed-plus-aged sample.](figures/Figure_2.jpg)

**Fig. 3** compares the stress–strain behavior of the AI and Omori alloys during cyclic loading–unloading–heating deformation. In this test, any residual stress-induced martensite present at zero stress should transform back to austenite upon heating, causing the reloading stress to rise at a strain lower than the last unloading strain. This is exactly what happened in the Omori alloy: **Fig. 3b** shows that its residual strain after unloading from 3% deformation is ≈2.2%, and upon reloading, stress rises at a strain of ≈1.7%. This 0.5% strain recovery caused by heating is evidence of stress-induced martensite transformation in the Omori alloy — the stress-induced martensite was stable enough to survive unloading but transformed back to austenite upon heating. By contrast, **Fig. 3a** shows no strain recovery of the AI alloy during this test, indicating that it deforms plastically with no pseudo-elasticity regardless of heat-treating condition. We conclude that the microstructure of the AI alloy is very stable and that stress-induced phase transformation is not one of its active deformation mechanisms.

![**Fig. 3.** Loading–unloading–heating tests of (a) the AI alloy and (b) the Omori alloy. Samples were heat treated at 1200 °C for 1 minute. Black arrows show the deformation path; the red arrow highlights the strain recovery caused by heating.](figures/Figure_3.jpg)

## 3.3 Synchrotron diffraction and phase identification

Synchrotron XRD of samples before and after deformation is shown in **Fig. 4**. **Fig. 5** shows good overall agreement between the experimental data (lower half) and the results of Rietveld refinement (upper half) for the AI alloy. Based on this result, the AI alloy is estimated to consist of ≈62% FCC γ-phase, ≈34% BCC α-phase, and ≈4% DO₃ Fe₃Al phase. Its diffraction patterns before and after deformation are essentially the same (**Fig. 4a, b**), and relative peak intensities (**Fig. 6a**) are essentially unchanged: no new diffraction peaks appear and none disappear. Although an ex-situ measurement made after unloading cannot, on its own, exclude a fully reversible transformation that reverts on unloading, the absence of any mechanical recovery (**Figs. 2 and 3**) together with the unchanged multi-phase pattern points consistently to deformation by dislocation slip rather than stress-induced phase transformation. The shift from sharp, discrete spotty patterns in the undeformed state (**Fig. 4a**) to broader, partially arced rings after deformation (**Fig. 4b**) can be attributed to dislocation activity, which results in peak broadening and/or the formation of tiny sub-grains. In comparison, the Omori alloy presents a BCC α-dominated pattern with FCC γ-phase and ordered β-NiAl (B2) precipitate diffractions in the undeformed state (**Fig. 4c**); after 8% applied strain, the {111}γ reflection intensifies and the overlapping {200}α redistributes in intensity (**Fig. 4d**), consistent with stress-induced γ formation and partial variant activation. The change in peak intensity after deformation of the Omori alloy is also clearly shown in **Fig. 6b**.

It is worth noting that the AI alloy after AGG heat treatment showed an X-ray diffraction pattern similar to **Fig. 4a**, indicating that the multi-phase microstructure is a stable state of this alloy at 1200 °C.

![**Fig. 4.** 2D synchrotron X-ray diffraction images of (a) AI alloy annealed at 1200 °C for 1 min, (b) annealed AI alloy after 10% tensile strain, (c) Omori alloy annealed at 1200 °C for 1 min, and (d) annealed Omori alloy after 8% tensile strain.](figures/Figure_4.jpg)

![**Fig. 5.** Comparison between synchrotron X-ray diffraction data (lower half) and results of Rietveld refinement (upper half) for the AI alloy heat treated at 1200 °C for 1 minute.](figures/Figure_5.jpg)

![**Fig. 6.** Azimuthally integrated X-ray diffraction spectra of (a) the AI alloy and (b) the Omori alloy before and after deformation. Samples were heat treated at 1200 °C for 1 minute before deformation.](figures/Figure_6.jpg)

---

# 4. Discussion

## 4.1 Origin of the absence of stress-induced phase transformation

The failure of the AI-hypothesized alloy (50Fe-30Mn-12Al-4Ni-4Si at% with 1000 ppm C) to exhibit super-elasticity or a shape-memory response can be attributed to a fundamental misalignment between its phase stability and its active deformation mechanisms. In Fe-Mn-Al-Ni shape-memory systems, super-elastic behavior is contingent upon a reversible, stress-induced martensitic transformation from a BCC α parent phase to FCC γ martensite. However, quantitative Rietveld refinement of the synchrotron XRD data reveals that the AI-alloy is structurally dominated by the γ-phase (≈62%), whereas the α-phase accounts for only ≈37% of the volume fraction (Sec. 3.3). Compared to the Omori alloy (43.5Fe-34Mn-15Al-7.5Ni at%), the AI alloy has less Mn, Al, and Ni, but higher Fe, Si, and C. It is known that Fe, Si, and Al stabilize the BCC α-phase, while Mn, Ni, and C stabilize the FCC γ-phase [@bhadeshia2010steels]. The original hypothesis was that these chemistry changes would not alter the phase constitution or stability, and that the additional C could also increase material strength to impede dislocation slip and promote stress-induced phase transformation. In practice, this chemistry modification favors the FCC crystal structure and raises γ-phase stability — adding C appears to be more consequential than the changes in other elements. It is also worth noting that formation of the minor Fe₃Al phase extracts Fe and Al from the matrix, which could further decrease α-phase stability. Consequently, the AI alloy lacks the chemical driving force necessary to trigger a stress-induced phase transformation.

Furthermore, mechanical and structural analyses indicate that the AI-alloy accommodates macroscopic deformation via irreversible dislocation slip rather than phase transitions. Whereas the Omori-alloy relies on coherent, ordered β-NiAl (B2) precipitates within its BCC matrix to suppress permanent slip and promote transformation reversibility, the AI-alloy instead forms a DO₃ Fe₃Al phase. Without the precipitation-hardening effect provided by fine B2 precipitates, the matrix lacks sufficient resistance to plastic flow. This is confirmed by the post-deformation synchrotron XRD patterns, where the transition from sharp, discrete spots to broad, partially arced rings reflects dislocation multiplication and sub-grain formation. Thus, the microstructural state of the AI-alloy remains highly stable at 1200 °C, favoring dislocation- or twinning-mediated plasticity over stress-induced martensitic transformation.

## 4.2 Anneal-temperature dependence of mechanical properties

Although the AI alloy did not show super-elastic behavior, its monotonic tensile behavior varies strongly with annealing temperature, and the trends are exactly those expected for a cold-drawn wire passing through recovery, recrystallization, and grain growth. Reading these as a single-specimen survey, three regimes emerge.

At the lowest temperatures (600–700 °C) the wire is very strong but essentially brittle: tensile strengths of ≈2009–2293 MPa and yield strengths of ≈1683–1948 MPa, but elongation of only ≈2%. These temperatures are below the recrystallization range of the heavily cold-drawn wire, so annealing here drives only recovery (relief of residual drawing stresses and partial rearrangement of the dislocation substructure) without nucleating new strain-free grains. The high dislocation density retained from cold drawing is what sustains the high strength, and the small ductility gains in this window reflect stress relief rather than any genuine restoration of formability; the wire still fractures soon after yield.

The abrupt change near 800 °C marks the onset of recrystallization. Elongation jumps from 2.2% at 700 °C to 24.0% at 800 °C, while tensile strength falls from 2009 to 1216 MPa and yield strength from 1683 to 1167 MPa. This discontinuity — rather than a smooth softening — is the signature of recrystallization: new equiaxed, strain-free grains nucleate and consume the deformed matrix, removing most of the stored dislocation content and abruptly restoring ductility. It is this recrystallization threshold, not a gradual process, that makes ductility appear only above ≈800 °C.

From 800 to 1200 °C the wire is fully recrystallized and the dominant process is grain growth. Yield strength falls monotonically with temperature (1167 → 502 MPa) as a result of continuous grain growth; larger grains allow more uniform slip, which raises elongation to a peak of ≈33% near 1000 °C. In other words, across this regime, increasing grain size simultaneously decreases strength and increases ductility — the classic strength–ductility trade-off of a single-phase-controlled structural metal. Above 1000 °C, elongation eases back slightly (29.7% at 1100 °C, 23.9% at 1200 °C), which we attribute to excessive coarsening reducing uniform elongation even as the matrix continues to soften. Throughout the sweep, the elastic modulus stays within ≈150–165 GPa, as expected for a structure-insensitive property of an essentially unchanged multi-phase mixture.

## 4.3 Implications for AI-guided alloy design

The AI-guided alloy design did not achieve the intended super-elastic or shape-memory behavior because the model primarily relied on thermodynamic and literature-based correlations rather than a complete understanding of the complex phase-transformation mechanisms required for functional Fe-based SMAs. As shown in this study, the AI-hypothesized alloy developed a stable multiphase microstructure consisting mainly of FCC γ and BCC α phases, and neither mechanical testing nor synchrotron diffraction provided evidence of stress-induced martensitic transformation; deformation was instead accommodated largely by conventional dislocation slip. Although the composition appeared reasonable from a thermodynamic and strengthening perspective, the AI model was unable to accurately predict the delicate balance among phase stability, transformation driving force, defect structure, precipitation behavior, and processing history that governs pseudo-elasticity. This outcome highlights a current limitation of AI-assisted alloy design: available models are often trained on composition–property relationships and equilibrium thermodynamics, while kinetic effects and microstructure evolution during manufacturing remain insufficiently represented.

Nevertheless, AI-assisted alloy design is likely to become increasingly successful. As larger experimental databases become available and models begin to incorporate processing history, microstructural evolution, kinetic simulations, and deformation mechanisms alongside thermodynamic calculations, AI will be able to make more physically informed predictions. Future materials-design frameworks that integrate first-principles calculations, phase-field modeling, CALPHAD databases, high-throughput experiments, and machine learning may better capture the conditions required for martensitic transformations and functional properties. Rather than replacing metallurgical expertise, AI is expected to serve as a powerful tool for rapidly narrowing the compositional search space, generating testable hypotheses, and accelerating discovery. The present study should therefore be viewed not as a failure of AI itself, but as evidence that current AI models have not yet fully captured the complexity of structure–processing–property relationships in shape memory alloys.

---

# 5. Conclusions

An AI-guided deep-research workflow was used to design a low-cost Fe-Mn-Al-based alloy targeting room-temperature super-elasticity. The proposed alloy was successfully synthesized and compared with the benchmark Fe-Mn-Al-Ni alloy reported by Omori *et al.* under identical processing conditions. The AI-designed alloy developed a stable dual-phase FCC/BCC microstructure and exhibited deformation primarily through dislocation slip rather than stress-induced martensitic transformation. Consequently, neither super-elasticity nor shape-memory behavior was observed, whereas the reference alloy showed clear evidence of transformational deformation.

These results highlight an important limitation of current AI-assisted alloy design. While AI can rapidly generate compositionally plausible alloy candidates based on thermodynamic considerations and literature knowledge, it does not yet fully capture the complex interactions among composition, processing, microstructure evolution, and deformation mechanisms that govern shape-memory performance. Nevertheless, this work demonstrates the value of experimentally validating AI-generated hypotheses and suggests that future models incorporating kinetic effects, phase transformations, and processing history may become powerful tools for accelerated alloy discovery.

---

# Acknowledgments

The authors thank Fort Wayne Metals for providing access to melting, hot-rolling, cold-drawing, and metallography facilities, and for technical guidance throughout alloy synthesis.

S. Cai also thanks his colleagues Andrew Michael for melting the alloys and Todd Darley for SEM analysis. Synchrotron X-ray diffraction was carried out on beamline BL12SW at the Shanghai Synchrotron Radiation Facility (SSRF) under proposal No. 2024-SSRF-PT-505463. The authors acknowledge beamline BL12SW (http://cstr.cn/31124.02.SSRF.BL12SW) of the SSRF for experimental support. Data analysis was performed using the FIT2D and MAUD software.

---

# Declarations

**Funding.** No external funding was received for this work.

**Competing interests.** The authors declare no competing interests.

**Generative AI use.** An LLM deep-research agent (Google Gemini 2.5, Deep Research) was used to hypothesize the AI-alloy composition under study, as described in Sec. 2.1; this use is a study method, not a manuscript-preparation aid. No generative AI tools were used to draft, edit, or otherwise prepare the text of this manuscript.

**Data availability.** ICP-AES and interstitial-gas (ASTM E1019) chemistry certificates for both heats, raw synchrotron diffraction data, Instron cyclic-tensile export data, and metallographic images are available from the corresponding author on reasonable request.

---

<!-- REFERENCES TO FOLLOW IN BIBLIOGRAPHY BUILD -->
