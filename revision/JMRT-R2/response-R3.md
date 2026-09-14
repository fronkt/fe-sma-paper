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

The reviewer is right that the two temperatures quoted in Revision 1 could not both be
treated as material properties, and the reason is more serious than a difference between
databases: the 1340 °C figure was wrong. In preparing this response we found that the scripts
used for the mpea-02b and PrecHiMn-04 calculations had requested the liquid phase under a
name the software does not recognise (the database type suffix had been carried into the
phase name), and that the unknown name had been dropped silently. Those two databases were
therefore evaluated for an alloy that could not melt, which is why one of them appeared to
place a single-phase α field at 1340 °C and to "return no liquid below 1400 °C" while the
third, correctly configured, database placed the solidus at 1240 °C. The apparent
disagreement between databases on the solidus was an artifact of that omission. We have
corrected the scripts, re-run every calculation in the paper with the liquid phase present,
archived the superseded results, and rewritten every sentence that quoted a solvus or solidus
(abstract; Secs. 2.6, 3.4, 4.1, 4.2, 4.4 and 5; Table 3 is unchanged; a new Table 4 gives the
solid-state α field and solidus per database; Fig. 9 is redrawn with the liquid fraction).

With the liquid phase included the three databases agree on the point that matters. In
mpea-02b the LLM-alloy is still 7.4% γ at 1290 °C and the first liquid appears at 1300 °C,
so the alloy passes from α + γ directly to α + liquid; in PrecHiMn-04 it is two-phase at
1250 °C and melts from ≈1295 °C; in mc_fe it is two-phase at 1230 °C and melts from
≈1240 °C. **In none of the three does a single-phase α field open before melting begins.**
The carbon-free control, by contrast, is single-phase α from ≈1130–1160 °C up to its
solidus in all three (Table 4). The revised argument therefore no longer rests on a solidus
value at all: it rests on the absence of a single-phase α field anywhere in the solid state,
which the three assessments return unanimously even though they differ on where melting
starts (≈1240 versus ≈1295 °C). That difference is now reported as such in Sec. 3.4 and
nothing depends on it.

We also disclose, in Sec. 2.6, one numerical subtlety the re-run exposed, because it bears
on the reliability the reviewer asks about. Near the solidus of this alloy the global
Gibbs-energy minimisation converged to different states from different starting grids, and
the denser grid was not always the lower-energy one; for those temperatures the state of
lowest Gibbs energy across a ladder of grid densities was retained, and every arbitration is
logged with the archived scripts. The 1200 °C constitutions of Table 3 were confirmed to be
the lowest-energy states in every database.

On high-temperature DSC/DTA: we agree it is the direct measurement of the incipient melting
temperature, and we name it as such in the text. We have not performed it for this revision
because the corrected argument does not use the solidus as a number — only the fact, common
to all three databases, that the alloy is still two-phase when it starts to melt — and
because no instrument was available to us within the revision period. We would be glad to
add the measurement should the editor consider it necessary.

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
