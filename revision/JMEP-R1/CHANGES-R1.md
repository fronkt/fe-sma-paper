# JMEP-26-07-50730.R1 — change ledger (against the 52497 text, `manuscript.md` at 8eaae5d)

Each entry: what changed, where, and the comment it answers. This ledger feeds the response letter. Changes against the JULY text (what the reviewers saw) are far larger; the letter needs a section map for those.

## Step 1 — text fixes (2026-10-12)

| ID | Where | Change | Answers |
|---|---|---|---|
| T1 | Keywords | Alphabetical; "superelasticity" | R1#1, R2#1 |
| T2 | Whole text + title (`front_JMEP.md`) | "super-elastic(ity)" → "superelastic(ity)" (20×), "pseudo-elastic(ity)" → "pseudoelastic(ity)" (8×) | R2#1 |
| T3 | Abstract | "processed in parallel"; Rietveld fractions "semi-quantitative"; "ex-situ pattern unchanged after 10% strain"; open question restated; closing scope sentence ("single-composition case study does not rate LLM alloy design generally"). Trimmed to 195 words (dropped the analyzed Mn/Al values and the test's name) | R2#1b, 14c, 15b, 18 |
| T4 | Sec. 1, para 1 | "AI-proposed, thermodynamically screened candidates" → machine-proposed candidates, some DFT-screened (GNoME), some, like this one, screened by no calculation | R2#2d |
| T5 | Sec. 2.1 + Table 1 | Table 1 now wt% (at%), conversion stated; caption: single analysis per heat, no analytical uncertainty reported. Text: Si shortfall's effect on phase stability pointed to Secs. 3.4/4.2; homogeneity within a heat not checked | R2#4a, 4b |
| T6 | Sec. 2.1 | Benchmark defined as "a reference composition processed in parallel, not a superelastic control whose treatment was optimized" — its transformation shows the route and tests can detect one | R2#7 |
| T7 | Sec. 2.4 | "No correction for load-train compliance or grip slip"; protocol "designed to reveal" superelasticity (was "reveals"); Table 2 read from incrementally cycled specimens, protocol-dependent; rate is quasi-static, rate sensitivity via latent heat [Shaw & Kyriakides 1995, new ref], weak in Fe-Mn-Al-Ni (0.53 MPa °C⁻¹ [Omori 2011]) | R1#5, R2#9a, 9d |
| T8 | Sec. 2.5; Fig. 6 caption | Transmission geometry, 4288² detector, 100 µm pixels, ≈1.83 m, geometry fitted from rings (<0.1%), CeO₂ frame gives same center; Fig. 6b normalization ÷1.625 (= 2.6/1.6) stated | R2#13a (part), 15d (part) |
| T9 | Sec. 3.1 | Grain sizes = visual estimates, not stereology; EDS qualitative, cannot see C, phase assignment rests on EDS + diffraction | R2#12b, 12c (part) |
| T10 | Sec. 3.2 | "rose monotonically" → "rose without a transformation plateau"; heating test = one specimen per alloy, "heating-induced (shape-memory) recovery, a single observation" | R2#10c, 11d |
| T11 | Sec. 3.3 | Fractions "semi-quantitative"; spots→arcs "consistent with" dislocation activity, not quantified, texture/grain sampling could contribute; heating test "narrows" (was "closes") the remaining route; D0₃ spatial scale unknown; κ not in an alternative model; benchmark transformation "rests on three observations, each limited" (was "not in question") | R2#14c, 15a–c, 16a–c, 7 |
| T12 | Sec. 4.1 | Textbook stabilizer list now explicitly insufficient for a six-element alloy; conclusion attributed to the multicomponent calculation. "reflects dislocation multiplication" → "consistent with … not quantified"; "deforms by slip" → "is interpreted to deform by slip" | R2#5d, 15c |
| T13 | Sec. 4.2 | "D0₃ … appears in the α constituent" → location and scale not determined | R2#16c |
| T14 | Sec. 4.3 | "monotonic tensile behavior" → "tensile properties"; regimes = interpretations, microstructures only at 1200 °C; Table 2 protocol qualification; "falls monotonically … as a result of grain growth" → "falls at each step … which we interpret as"; phase fractions/ordering/texture/cold work may also vary; elongation drop above 1000 °C exceeds scatter (SD ≤1.2%), cause unidentified, alternatives listed; modulus not used to infer structure; envelope comparison qualified | R2#9d, 10c, 17b, 17c, 17d |
| T15 | Sec. 4.4 | New paragraph: the failure chain link by link (proposal / down-selection / synthesis / processing) and what can be attributed to the LLM | R2#18a, 18b |
| T16 | Conclusions | "AI-guided" → "LLM"; Rietveld "semi-quantitative"; ex-situ qualifier on the unchanged pattern | R2#15b, 18 |
| T17 | Secs. 2.5, 3.2, 3.3, 4.1 | Consistency sweep after T11: "Quantitative refinement proved feasible" → "Refinement proved feasible"; "reflecting incomplete recrystallization" → "consistent with"; "a quantitative, if grain-statistics-limited, refinement" → "a semi-quantitative, grain-statistics-limited refinement"; "quantitative Rietveld refinement … reveals" → "semi-quantitative … indicates" | R2#14c, 17b |

Bibliography: `shaw1995niti` added to `references.bib` and `submissions/JMEP-R1/references-jmep.bib` (the R1 package folder; `jmep.csl` copied there). The 52497 package `submissions/JMEP-2026-09/` is untouched.

Checks (pandoc dry build, R1 bib + CSL): abstract 195 words; 0 unresolved citations; 0 mojibake; 0 "super-elastic"/"pseudo-elastic". Remaining "monotonically" (Sec. 3.4, a calculated trend) and "threshold" (Sec. 3.2, "rather than a measured recovery threshold") are deliberate.

### Flags for Frank

1. **T6/T11 benchmark framing** — adopts R2#7's "reference composition processed in parallel" without renaming the alloy. Revert if you want the JMRT-era stance.
2. **T7 "Table 2 read from incrementally cycled specimens"** rests on Table S1 (M1/M2 = cyclic tension). Confirm the August replicates were cyclic.
3. **T3 abstract** lost the analyzed Mn/Al values (still in Table 1/Sec. 2.1) and the test's name.
4. **Title** keeps "LLM-Hypothesized" (spelling fixed). R2 suggested "LLM-Proposed … Targeted for Room-Temperature Superelasticity" — your call; co-authors approve title changes.
5. **R1#5** — the text now says the rate is quasi-static, but not why it was chosen. The response needs the reason (lab practice? same as the NiTi-Cu work?).
