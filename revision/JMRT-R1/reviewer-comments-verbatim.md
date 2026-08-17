# JMRT-D-26-06169 — verbatim reviewer comments

Recovered 2026-08-16 from the Editorial Manager comments page as pasted by Frank on
2026-08-08 (session transcript 44b9d541). This is the authoritative wording for the
response letters; `comment-triage.md` paraphrases these for planning. EM interface
text ("Reply to comment", "Show less", etc.) removed; comment text untouched.

Decision: major revision. R1 "major revisions" (Jul 27) · R2 "revise" (Jul 31) ·
R3 "not in present form" (Jul 28). Responses are submitted **per reviewer** — three
documents, each seen only by its reviewer.

---

## Reviewer 1 — July 27

This paper examines an LLM-hypothesized Fe-Mn-Al-Ni-Si-C composition and benchmarks its mechanical response against an established super-elastic Fe-Mn-Al-Ni alloy, employing synchrotron X-ray diffraction to rationalize the absence of super-elasticity. The topic is highly timely and carries significant implications for the growing field of AI-assisted alloy design, as it provides a rare experimental test of computationally generated hypotheses. The authors have collected a substantial dataset, and the finding that the AI-proposed alloy fails due to phase-stability mismatch rather than processing inadequacy is informative. However, despite the merits of this work, several aspects require systematic revision to strengthen the manuscript's clarity, logical flow, and evidential support. I believe that the paper is suitable for publication in this journal after major revisions. The specific revision comments are as follows:

1. The AI-designed alloy differs from the benchmark Omori alloy in multiple elemental concentrations simultaneously (Mn, Al, Ni, Si, and C are all varied). The authors attribute the failure of the AI-hypothesized composition primarily to its elevated carbon content and its destabilizing effect on the BCC parent phase. However, because this is a multi-variable compositional change, the specific role of carbon cannot be isolated. Without a designed control experiment—such as an AI-designed alloy variant without the 1000 ppm C addition—the assertion that "carbon is the main culprit" (as stated in the abstract and Section 4.1) remains speculative and insufficiently supported. The authors should either provide such a control or substantially temper their causal attribution, reframing the conclusion as a combined effect of the entire compositional modification.

2. The discussion of why the AI model failed (Section 4.3) is descriptive rather than diagnostic. The authors note that the model relied on thermodynamic and literature correlations, but they do not examine the model's specific reasoning pathway that led to the proposed composition. Did the model predict a BCC single-phase microstructure? Did it account for the formation of the D03 Fe3Al phase? A retrospective analysis using CALPHAD thermodynamic calculations (even a simple equilibrium phase diagram calculation for both alloys) would add significant quantitative rigor to the claim that the AI-designed alloy has insufficient chemical driving force for stress-induced transformation. Without such analysis, the "lessons learned" for AI-guided design remain vague.

3. The microstructural interpretation of the AI-designed alloy's deformation mechanisms lacks mechanistic depth. The authors assert that the absence of super-elasticity is due to "irreversible dislocation slip" rather than phase transformation, but they do not explain why this duplex FCC/BCC structure (62% γ, 34% α) preferentially deforms by slip. Is it the morphology of the two phases (e.g., lamellar or blocky) that constrains transformation? Or does the D03 Fe3Al phase pin dislocations in a way that suppresses the martensitic start stress? The authors should provide a more detailed mechanistic rationale linking the observed two-phase microstructure to the suppression of the transformation pathway.

4. The manuscript claims that the AI-designed alloy did not exhibit abnormal grain growth (AGG) even under the cyclic heat treatment intended to produce a bamboo-like structure. This observation, however, is buried in a single sentence in Section 3.3. Given that AGG is a central requirement for achieving super-elasticity in this alloy family, the fact that the AI-designed alloy fails to undergo AGG is a second, independent mode of failure. The authors should elevate this point, explicitly present the microstructure after the AGG treatment (which is currently absent from the figures), and discuss how the multi-phase stability prevents grain boundary migration—this would strengthen the case that the AI design is fundamentally incompatible with the processing route.

5. The terminology used throughout the manuscript—specifically "Al-alloy" and "Al-hypothesized"—is problematic because "Al" is also the chemical symbol for aluminum, which is a major constituent of the alloy under study (~6 wt.%). This ambiguity is confusing and detracts from readability. The authors should replace "Al" with "AI" (artificial intelligence) or "AI-designed" in all instances, including the title, abstract, and keywords, to clearly distinguish the alloy designation from elemental aluminum.

6. In Section 2.1, the authors state that Si was added for solid-solution strengthening and to influence stacking-fault energy. However, this rationale is not revisited in the Discussion. The authors should either provide a more detailed justification for the Si addition or acknowledge in hindsight that Si may have contributed to the phase-stability imbalance.

7. The mechanical testing section (Section 2.4) describes the heating stage for the shape-memory effect test as "to ≈200°C," but the heating rate and holding time are not specified. These details are critical for assessing whether the reverse transformation was fully triggered. The authors should provide this information.

8. In Table 1, the Omori-alloy contains an unexpected 0.06 wt.% phosphorus, and the authors note the source is unknown. While this may not affect the main conclusions, the authors should discuss whether this unintentional impurity could have influenced the mechanical behavior of the benchmark alloy (e.g., by grain-boundary embrittlement) and whether it complicates the direct comparison with the AI-designed alloy.

9. The peak elongation of the AI-designed alloy (≈33% at 1000°C) is remarkably high for a duplex alloy. While this is not central to the main conclusion, the authors could briefly comment on whether this ductility is exceptional and whether it suggests any potential for structural applications despite the lack of shape-memory functionality.

---

## Reviewer 2 — July 31

I go through the paper and my advising is mentioned in following.
The authors investigate "Fe-based shape memory alloy; super-elasticity; AI-guided alloy design; synchrotron XRD; abnormal grain growth". The structure of paper was arranged well and nicely written, but can find some mistake in this paper. The authors are advised to carefully read through the manuscript and correct these mistakes. Abstract clearly summarizes. Experimental procedure clearly described. Result was presented well, but there are few weaknesses in discussion part. Conclusions appropriate in view of the study objectives and results. However, although the study has been carried out accordingly, there are still errors and issues required to be rectified and listed as follow:

Title:

1- Suggestion and consider specifying "LLM-hypothesized" instead of the broader term "AI-hypothesized" for greater precision.
2- Adding the phrase "experimental validation" would better reflect the manuscript's main contribution.
3- The title is technically appropriate but could highlight the role of phase stability in the observed mechanical response.

Abstract:
1- The novelty of experimentally validating an LLM-generated alloy should be stated more explicitly.
2- Quantitative mechanical results (e.g., recoverable strain or yield strength) should be included to support the conclusions.
3- The influence of carbon on phase stability should be briefly justified rather than only suggested.
4- The abstract should briefly explain why the benchmark alloy exhibits super-elasticity while the AI alloy does not.

Introduction:
1- The literature review should include more recent studies on AI-driven alloy design beyond LLM applications.
2- The scientific gap between computational alloy prediction and experimental validation should be better defined.
3- The rationale for selecting this specific alloy composition should be explained more thoroughly.
4- The research objectives and hypotheses should be clearly stated at the end of the introduction.

Experimental procedure:
1- The alloy design workflow generated by the LLM should be described in sufficient detail to ensure reproducibility.
2- Standard No. of tensile test must be mentioned.
3- Statistical repeatability of the mechanical tests should be reported.

Results and Discussion:
1- The discussion should quantitatively correlate phase fractions with the observed mechanical behaviour.
2- The proposed role of carbon in suppressing super-elasticity should be supported by thermodynamic calculations.
3- Fig. 2 is small and unclearly.
4- Fig. 2 e, should be presented and discussed.
5- The implications of this negative result for future AI-assisted alloy design deserve deeper discussion.
6- Is there any formation Martensite phase in microstructure, this should be present and discuss.

Conclusion:
1- The conclusions should distinguish experimental observations from the authors' interpretations.
2- Emphasize the broader implications for AI-assisted materials discovery rather than this alloy alone.
3- Discuss the limitations of relying solely on LLM-generated compositions.
4- Include recommendations for integrating thermodynamic screening into AI-guided alloy design.

Therefore, in the submitted paper, the above mentioned comments will make it clear that the manuscript can be accepted for its publication, but required to revise.

---

## Reviewer 3 — July 28

Thank you for submitting the manuscript entitled "Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy". This study experimentally evaluates an AI-assisted alloy candidate and reports its lack of superelasticity under the tested conditions. However, the current manuscript does not provide sufficient evidence to support its main comparisons and mechanistic conclusions. In particular, the effects of heat treatment, grain structure, texture, and nanoscale precipitates have not been adequately characterized. Therefore, I do not recommend publication of the manuscript in its present form. The specific reasons are listed below:

1. The statement at the end of the Introduction that "because the processing history was kept identical for both alloys, compositional differences are the sole variable determining the final mechanical properties" is not valid from a materials-science perspective. It is not meaningful to compare the superelastic differences between the AI alloy and the Omori alloy solely by applying the same processing route, because identical external processing parameters do not mean that the two compositions achieve the same degree of recrystallization, grain size, grain orientation, texture, phase constitution, dislocation density, and precipitation state. The manuscript may state that the two alloys were subjected to the same nominal processing parameters, but further justification is required before the final performance differences can be attributed solely to chemical composition.

2. The basis for designing the candidate composition in Section 2.1 is questionable. Fe-Mn-Al-C, Fe-Mn-Al-Ni-C, and Fe-Mn-Al-Si-C systems with compositions similar to that studied here have mainly been investigated in the literature as low-density or lightweight structural steels. Their B2, DO3, and carbide phases are generally used to improve strength and ductility rather than to produce a reversible martensitic transformation. For example, Rahnama et al. investigated the effect of the B2 phase on the microstructure and mechanical properties of Ni-alloyed Fe-Mn-Al-C lightweight steels (Acta Materialia 132 (2017) 627–643); Saha et al. reported that NiAl-type nanoscale B2 precipitates are mainly located in the BCC regions of low-density Fe-Mn-Al-C steels (JOM 74 (2022) 3181–3190); and Heo et al. showed that Si can promote the formation of DO3 ordered phases and complex carbides in Fe-Mn-Al-C steels (Metallurgical and Materials Transactions A 43 (2012) 1731–1735). The authors should clearly explain why this alloy composition was selected for investigation and, given that many similar compositions mainly exhibit the microstructures and deformation behavior of lightweight steels, why this composition was expected to show room-temperature superelasticity.

3. Table 1 shows that the actual Si content of the AI alloy is 1.11 wt.%, whereas the nominal content is 2.2 wt.%; the actual value is approximately half of the designed value. Considering that Si is intended by the authors to strengthen the matrix and regulate phase stability and precipitate formation, this deviation cannot be described as "very close to the nominal values." Strictly speaking, the claimed nominal composition requires further verification in this study.

4. Section 2.2 describes a cyclic heat treatment for abnormal grain growth. However, the main text only briefly states that the XRD pattern of the AGG-treated sample is similar to Fig. 4a, without presenting the grain size, formation of bamboo-like grains, grain orientation, texture, or corresponding cyclic stress-strain results after this treatment. The key mechanical specimens in Figs. 2 and 3 were not in this cyclic heat-treated condition. The key heat treatment specifically included in the Methods does not enter the core evidence chain, and the reporting of the results is incomplete.

5. Section 2.2 also raises a question regarding the applicability of the processing route. The formation, size, and distribution of B2 nanoscale precipitates depend on the specific composition, aging temperature, cooling rate, and subsequent aging treatment. After the composition is changed to one containing Si and C with a lower Ni content, the optimum precipitation window may be entirely different. Directly applying the heat treatment used for the Omori alloy to the new composition can only show that the two alloys respond differently under the same treatment. Further study is required to determine whether this processing route is suitable for the new alloy and whether it can demonstrate that the new alloy itself cannot form an appropriate B2 nanoscale phase or exhibit superelasticity.

6. Section 2.5 uses ex-situ XRD before deformation and after unloading. For a superelastic material, stress-induced martensite may form during loading and reverse completely during unloading. Therefore, similar diffraction patterns before loading and after unloading do not necessarily exclude a reversible phase transformation during loading. More direct evidence should be provided to confirm the deformation mechanism.

7. Section 3.2 systematically presents only the cyclic curves of the AI alloy and does not provide fully corresponding stepwise cyclic loading-unloading curves for the Omori alloy. Many factors affect superelastic performance. The authors should ensure that the grain size, orientation, texture, and precipitation state of the two alloys are characterized on a corresponding basis before comparing their properties.

8. The identification of B2 and DO3 in Section 3.3 cannot support the nanoscale precipitation mechanism proposed in the manuscript. Whether the absence of an obvious B2 peak in the AI alloy proves the complete absence of B2 still requires further discussion. The authors should assess whether the heat-treatment route used for the AI alloy is appropriate and use additional characterization methods to determine whether the B2 phase is present.

9. Section 4.1 mainly attributes the absence of superelasticity to the stabilization of the FCC γ phase by C. However, the contents of Fe, Mn, Al, Ni, Si, and C all differ simultaneously between the AI alloy and the Omori alloy, and the reduction of Ni from 7.5 at.% to 4 at.% may also significantly affect B2 precipitation and parent-phase stability. How can the authors identify C as the main factor based on only two compositions in which multiple elements vary simultaneously?

10. The statement about B2 in Section 4.1 is too absolute. "Omori-alloy relies on coherent, ordered β-NiAl (B2) precipitates" may easily imply that B2 is the sole or necessary condition for superelasticity. Appropriate nanoscale B2 precipitates in conventional Fe-Mn-Al-Ni alloys do indeed help increase resistance to slip and improve transformation reversibility (Omori et al., Applied Physics Letters 101 (2012) 231907; La Roca et al., Journal of Alloys and Compounds 708 (2017) 422–427). However, superelasticity also depends on parent-phase stability, transformation temperature, grain size, grain orientation, texture, and the competition between transformation stress and plastic yield stress.

11. Section 4.2 interprets 600-700 °C as recovery, 800 °C as the onset of recrystallization, and 800-1200 °C as grain growth after complete recrystallization. However, these interpretations are based mainly on changes in strength and elongation and lack corresponding microstructural and EBSD evidence at each temperature. The statements "from 800 to 1200 °C the wire is fully recrystallized" and "single-phase-controlled structural metal" should not be presented as definitive conclusions without direct evidence.

12. The discussion in Section 4.3 overgeneralizes the limitations of AI-assisted design. This study examines only one candidate selected by the researchers from a range proposed by the model. At most, the current results show that this specific candidate and the processing route used in this study did not achieve the target performance. The manuscript should be repositioned as a case study of the composition-processing-microstructure-property relationships of a specific Fe-Mn-Al-Ni-Si-C alloy, with AI treated only as the source of the candidate rather than as the basis for the main generalized conclusion of the manuscript.

In summary, in summary, the current manuscript has not yet met the publication standards of this journal.
