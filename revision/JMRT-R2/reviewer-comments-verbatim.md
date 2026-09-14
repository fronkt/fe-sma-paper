# JMRT-D-26-06169R1 — Revision-1 reviewer verdicts, verbatim

**Source:** `Downloads/JMRT-D-26-06169-reviews.zip`, downloaded from Editorial Manager 2026-09-14
(`JMRT-D-26-06169-reviews.pdf`, 17 pp., plus `Initial submission/Reviewer 2/Comments list-…-Author.doc`,
which is R2's Round-1 list already recorded in `../JMRT-R1/reviewer-comments-verbatim.md`).
Copies of both files: `from-EM-2026-09-14/`.
**Extraction:** pypdf text layer of the PDF, pp. 4, 9–10, 16–17. Page-number artefacts removed;
nothing else altered.

The PDF also contains the Round-1 reports (already archived under `../JMRT-R1/`) and our 21-Aug
responses as the editor saw them. The **decision letter is not in this package** — it was sent to
the R1 corresponding address, cai485@purdue.edu.

---

## Reviewer 1 — Revision 1, 25/08/2026

No comment.

---

## Reviewer 2 — Revision 1, 03/09/2026

I have now reviewed the revised version of the above-mentioned manuscript, which was resubmitted by the authors in response to my previous comments and those of the other reviewers.

I am pleased to state that the authors have comprehensively and satisfactorily addressed all the points raised in my initial review.

In my opinion, the current version represents a substantial improvement over the original submission. The study is now methodologically sound, the data support the conclusions drawn, and the findings are of sufficient novelty and interest to the readership of Journal of Materials Research and Technology.

Given that the authors have fully resolved all previous issues and that the manuscript now meets the journal's standards for quality and originality, I recommend acceptance of this paper in its current form.

---

## Reviewer 3 — Revision 1, 04/09/2026

The authors have revised the manuscript in response to the previous round of comments, but several issues remain that directly affect the manuscript's core conclusions regarding the absence of super-elasticity and the underlying material mechanisms:

1. The revised manuscript has substantially changed the core conclusions and scientific interpretation of the original manuscript, going beyond ordinary supplementation and refinement. Although revising conclusions in light of new evidence is a normal scientific process, such a marked change also indicates that the original manuscript drew overly definitive conclusions on the basis of insufficient evidence, raising concerns about the rigor of the scientific argument. The authors should clearly state whether the original conclusions still hold and demonstrate that the revised core conclusions are supported by sufficiently reliable experimental evidence.

2. The three limitations listed by the authors in the Conclusions actually further weaken the current core conclusions regarding AI-guided alloy design and the scientific contribution of the manuscript. The authors have acknowledged that this study involves only one candidate composition, one LLM session, and one processing route; whether a different processing window could enable phase transformation in this composition has not been tested; and the carbon-free control has only been virtually evaluated by calculation. More importantly, the authors argue that a key reason for the present failure is that the AI did not determine "whether the temperature required for the desired phase stability could actually be reached under the available equipment and processing conditions," and they point out that a simple equilibrium phase-diagram pre-screening could have excluded this candidate before melting. If the problem arises mainly because the design workflow did not incorporate phase-diagram information, processing temperature, and equipment constraints, rather than because AI itself is unable to propose a candidate with super-elasticity, then what this study actually demonstrates is closer to an incomplete AI prompting and subsequent human-screening workflow, rather than a new scientific limitation of AI-guided alloy design itself. In fact, the manuscript does not test whether explicitly including the single-phase α field, transformation temperatures, CALPHAD results, and actual processing temperatures at the prompting and screening stages would yield a different or even viable candidate. The authors therefore need to clarify what the actual scientific contribution of this study is. If the core contribution is only that "AI-proposed candidates should undergo CALPHAD and processing-window screening before experiments," the authors should explain the novelty of this conclusion relative to conventional alloy-design workflows.

3. The cyclic heat-treatment route in Section 2.2 requires further clarification. The Methods state that the specimen was held at 1200 °C, water quenched, and then reheated to 900 °C. The authors should clarify whether this was the actual experimental route and whether it is consistent with the Omori-type cyclic heat treatment in Ref. 18 that traverses the α/α+γ phase fields. Since the revised manuscript argues that the LLM-alloy cannot obtain a single-phase α parent phase at 1200 °C, the authors should also explain why a cyclic heat-treatment schedule close to that of the benchmark alloy was still adopted and what this treatment was expected to achieve in the LLM-alloy.

4. There is a clear inconsistency in the gauge length reported for the mechanical testing in Section 2.4. The original manuscript stated 13 mm, whereas the revised manuscript changes this to 127 mm and states that strain was calculated as crosshead extension/127 mm. The two values differ by nearly a factor of ten, yet Fig. 3 still uses the original curves. The authors must clarify whether 13 mm was a typographical error in the original manuscript, what gauge length was actually used for each figure, and which tests were repeated or which data were reprocessed. This issue directly affects the reliability of the strain, recoverable strain, and related conclusions.

5. English: Fig. 3a tests the LLM-alloy after treatment at 1200 °C × 1 min. At this point, the material is already a γ-majority FCC/BCC duplex microstructure, and the fraction of BCC parent phase available for the stress-induced α→γ transformation is clearly insufficient. Therefore, Fig. 3a can only demonstrate, in the first instance, that this specific microstructural state does not exhibit obvious super-elasticity; it cannot directly prove that the composition itself is incapable of exhibiting super-elasticity. The relevant conclusions should be strictly limited to the microstructural and processing conditions that were actually tested in this study.

6. In Section 3.4, the authors rely mainly on CALPHAD calculations to conclude that the single-phase α field of the LLM-alloy lies above approximately 1340 °C, while also citing an incipient melting temperature of approximately 1240 °C, and on this basis conclude that the single-phase α state is experimentally inaccessible. However, the former is an equilibrium thermodynamic prediction, whereas the latter is derived mainly from a single database, and different databases do not give consistent solidus predictions. These temperatures therefore should not be treated directly as established material properties. High-temperature DSC/DTA is recommended to verify the incipient melting temperature.

7. In Section 3.5, the evidence that the 1200 °C × 40 min condition and the AGG condition show "no phase transformation" remains insufficient. The authors report only that the elongation of the condition corresponding to Fig. 1c decreases to 1.4%, but do not present the complete cyclic stress–strain curves, loading–unloading–heating curves, recoverable strain or residual strain data for this condition, nor do they quantitatively compare the α/γ phase fractions in Fig. 1a and Fig. 1c. The authors further use the absence of transformation in the 1 min and 40 min conditions to infer that the AGG condition would likewise show no transformation, but the AGG condition itself was not subjected to the same cyclic super-elasticity testing. The authors are advised to provide directly the complete cyclic mechanical results and phase-constitution data for both the 1200 °C × 40 min condition and the AGG condition, rather than using the results from two conventionally annealed conditions as a substitute for direct experimental evidence from the AGG condition.

8. Section 4.1 proposes that the α→γ transformation may already have occurred during cooling and further speculates that Ms may be above room temperature. Since this explanation has become an important mechanism used to account for the γ-majority phase constitution at room temperature and the absence of super-elasticity, Ms should be measured directly.
