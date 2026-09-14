# Response to Reviewer 3 — JMRT-D-26-06169R1, Round 2

**Status 2026-09-14: skeleton.** Each point is quoted verbatim from
`reviewer-comments-verbatim.md`; the replies are filled in as the corresponding manuscript
edits land (work plan in `tasks/todo.md`). Items marked ⟦…⟧ wait on S. Cai or on the E: drive.

We thank Reviewer 3 for a second careful reading. Before the point-by-point replies we
report a correction of our own, because it bears on point 6 and on several sentences the
reviewer quotes: in preparing this revision we found that the CALPHAD scripts used for
Revision 1 had silently omitted the liquid phase from two of the three databases. The
corrected calculations are described under point 6; every affected sentence is marked in the
tracked-changes file. The correction removes the inconsistency the reviewer identified and
strengthens the conclusion it was drawn from, but we state plainly that the temperatures
quoted in Revision 1 for the α solvus were wrong for that reason.

---

## Point 1 — rigor of the revised conclusions

> The revised manuscript has substantially changed the core conclusions and scientific
> interpretation of the original manuscript, going beyond ordinary supplementation and
> refinement. […] The authors should clearly state whether the original conclusions still
> hold and demonstrate that the revised core conclusions are supported by sufficiently
> reliable experimental evidence.

⟦reply — held / corrected / withdrawn-and-replaced table; §5 paragraph⟧

## Point 2 — contribution and novelty

> The three limitations listed by the authors in the Conclusions actually further weaken the
> current core conclusions regarding AI-guided alloy design and the scientific contribution
> of the manuscript. […] If the core contribution is only that "AI-proposed candidates should
> undergo CALPHAD and processing-window screening before experiments," the authors should
> explain the novelty of this conclusion relative to conventional alloy-design workflows.

⟦reply — contribution paragraph; the re-prompt declined with reasons⟧

## Point 3 — the cyclic heat-treatment route

> The cyclic heat-treatment route in Section 2.2 requires further clarification. […] the
> authors should also explain why a cyclic heat-treatment schedule close to that of the
> benchmark alloy was still adopted and what this treatment was expected to achieve in the
> LLM-alloy.

⟦reply — per-specimen schedules; Ref. 18 vs the Kassel-group schedule (Viebranz et al.
2024: 1225 °C/60 min ↔ 900 °C/15 min, three cycles, 5 K min⁻¹ ramps, air quench);
chronology and intent — route wording pending S. Cai⟧

## Point 4 — gauge length

> There is a clear inconsistency in the gauge length reported for the mechanical testing in
> Section 2.4. […] The authors must clarify whether 13 mm was a typographical error in the
> original manuscript, what gauge length was actually used for each figure, and which tests
> were repeated or which data were reprocessed.

⟦reply — gauge per dataset; Fig. 3 record pending S. Cai⟧

## Point 5 — scope of Fig. 3a

> Fig. 3a tests the LLM-alloy after treatment at 1200 °C × 1 min. […] The relevant
> conclusions should be strictly limited to the microstructural and processing conditions
> that were actually tested in this study.

⟦reply — bounded claims; three-level evidence statement⟧

## Point 6 — solvus, solidus and the databases

> In Section 3.4, the authors rely mainly on CALPHAD calculations to conclude that the
> single-phase α field of the LLM-alloy lies above approximately 1340 °C, while also citing
> an incipient melting temperature of approximately 1240 °C, and on this basis conclude that
> the single-phase α state is experimentally inaccessible. However, the former is an
> equilibrium thermodynamic prediction, whereas the latter is derived mainly from a single
> database, and different databases do not give consistent solidus predictions. These
> temperatures therefore should not be treated directly as established material properties.
> High-temperature DSC/DTA is recommended to verify the incipient melting temperature.

⟦reply — the liquid-phase omission and its correction; corrected numbers; why the argument
no longer rests on a solidus value; DTA declined with reasons; grid-arbitration disclosed⟧

## Point 7 — the 40-min and AGG conditions

> In Section 3.5, the evidence that the 1200 °C × 40 min condition and the AGG condition
> show "no phase transformation" remains insufficient. […] The authors are advised to
> provide directly the complete cyclic mechanical results and phase-constitution data for
> both the 1200 °C × 40 min condition and the AGG condition, rather than using the results
> from two conventionally annealed conditions as a substitute for direct experimental
> evidence from the AGG condition.

⟦reply — bracketing argument withdrawn; what exists per dataset; wire AGG heating test
(S. Cai); SEM-BSE point count (S. Cai); 40-min record heat identity (S. Cai)⟧

## Point 8 — measure Ms directly

> Section 4.1 proposes that the α→γ transformation may already have occurred during cooling
> and further speculates that Ms may be above room temperature. […] Ms should be measured
> directly.

⟦reply — reading demoted to a possibility; the EDS-partitioning argument; DSC named as
the test; result as a bound if it lands (S. Cai)⟧
