<!-- ARCHIVED 2026-10-14 from revision/JMEP-R1/comment-coverage.md (commit a5ae5b9). Written against the 52497 text (root manuscript.md, ~21k words). Superseded when R1 was rebased onto the July text on Song Cai's advice; kept for its answers and wording. -->

# JMEP-26-07-50730.R1 — how far the current text already answers the reviewers

Built 2026-10-12. Route chosen by Frank 2026-10-12: **revise 50730 (R1); withdraw 52497** (Gmail draft reply to V. Katona, `r-4143640730635266984`, unsent).

**Base text:** `front_JMEP.md` + `manuscript.md` = the JMEP-26-09-52497 text (≈21,000 words of body). **Reviewed text:** the July submission `submissions/JMEP/Cai_Fe-SMA_JMEP_manuscript.docx` (≈4,800 words including references; authors F.Y. Cai, S. Cai, J. Yan). Comments verbatim: `reviewer-comments-verbatim.md`.

Legend: **Done** = the 52497 text already answers the comment; the response only has to point to it. **Partial** = the substance is there, but a sentence, a table column or a stated limitation is still missing. **Gap** = not answered yet. **Who** = whose input is needed (FC = Frank, SC = Song Cai/FWM records, JY = J. Yan, repo = recoverable from files already in the repo, text = wording only).

## Reviewer 1

| # | Comment | Status | Where / what is missing | Who |
|---|---|---|---|---|
| 1 | Keywords alphabetical | Gap | Reorder; also spell "superelasticity" (R2#1) | text |
| 2 | Could the processing be the cause? | Done | Sec. 1 (route ≠ controlled isolation), 4.1 "What is not claimed", aging-asymmetry paragraph, 4.4 open tests | — |
| 3 | Alternative processing tried? | Done | Sec. 2.2 (600–1200 °C sweep, 40/80 min, 1250/1300 °C), 200 °C/3 h age, three cyclic AGG schedules, Fig. 10 | — |
| 4 | Where do the added Si and C go? | Partial | C: carbides calculated stable only <590 °C, none detected (3.4, 4.2); Si: possible D0₃ promoter (4.2). Missing: a direct statement on partitioning. Calculated α/γ phase compositions at 1200 °C exist in the pycalphad output and can be quoted; EDS for Si only if Song's SEM data has it; EDS cannot see C | repo, SC |
| 5 | Strain-rate choice; rate sensitivity of SMAs | Partial | Rate given (8.3 × 10⁻⁴ s⁻¹, Sec. 2.4). Missing: why this rate (quasi-static, same as the cai2024niticu protocol) and one sentence + citation on rate sensitivity (latent heat/self-heating; the null result is not a rate artifact at quasi-static rate) | text |

## Reviewer 2

| # | Topic | Status | Where / what is missing | Who |
|---|---|---|---|---|
| 1 | Title, "superelastic" spelling, LLM-proposed; abstract scope | Partial | Title already states the failure. Change "Super-elasticity/super-elastic" → "superelasticity/superelastic" (17 lines of the body, plus title and ESM2); consider "LLM-Proposed"; add one scope clause to the abstract (one composition, one route) | text |
| 2 | LLM workflow reproducibility; "trained"; 200 papers; thermodynamic screening | Partial | Done: query-time retrieval, not training (Sec. 1); full report = Online Resource 1; dates; prompt not preserved (disclosed, Sec. 2.1); agent ran no CALPHAD (4.1, 4.4). Missing: (i) the response must reconcile July's "over 200 papers" with the report's 76 sources; (ii) the intro still says "thermodynamically screened candidates", the phrase R2 objected to | FC (200), text |
| 3 | Number of runs/candidates; human decision rule | Gap | Six families and A2 = joint second are stated (2.1), and so is the single session (4.4). **Missing: why A2 over the top-ranked candidate, and why a composition point outside A2 in Mn and Al.** Only Frank knows this | FC |
| 4 | Nominal vs measured chemistry; at%; n; Si loss; cost; P | Partial | Done: measured at% in the text, method, sampling location (Table 1 caption), Si loss cause (oxidation, VIM), P paragraph, n = 1 per heat (Table S1). Missing: at% columns in Table 1; "one analysis, no stated uncertainty" in the main text; a homogeneity limitation; cost — either a dated raw-material comparison or a statement that the paper makes no cost claim | text, FC (cost) |
| 5 | Carbon causality; multicomponent thermo; κ | Done | CALPHAD in three databases on the measured chemistry, calculated C-free control, the Schaeffler heuristic shown to fail (4.2), carbon's role as cause left open (4.1, 4.2), κ calculated <590 °C. Minor: Sec. 4.1 still leans on the textbook stabilizer list (bhadeshia) in one sentence; soften | text |
| 6 | Processing history; aging details; strand furnace; surface | Gap | Present: homogenization 1000 °C/16 h, hot roll 850 °C, intermediate anneals 1000 °C, ≈85% RA, 4 ft/min. Missing: hot-roll reductions/passes, redraw sequence, intermediate-anneal times/count, cooling media, aging atmosphere/quench, hot-zone length, temperature calibration, wire tension, Ar purity, surface condition at 1200 °C, decarburization. Process-flow table (no figure needed). Unknowns stated as "not recorded" | SC |
| 7 | Benchmark as positive control | Partial + **decision** | The benchmark showed 0.5% heating recovery and XRD intensity change; its 1200 °C/1 min state is not bamboo (stated, 3.5). R2 asks to call it a "reference composition processed in parallel" unless unloading-recovery data exist. Missing: benchmark grain size/morphology for the Fig. 3 specimen (only XRD spottiness), and the decision on terminology. Recommend: adopt "reference alloy processed in parallel" in claims; keep the 0.5% as what it is | FC, SC |
| 8 | Transformation temperatures; test temperature | Partial | DSC absence and the interpretive status are stated (4.1, 4.4, Conclusions). Missing: the actual lab temperature (or "laboratory ambient, not recorded") and the time between heat treatment and test | SC/FC |
| 9 | Test metrology | Partial | Done: crosshead strain, no extensometer, apparent E, gauge per dataset, E8/E8M + purpose protocol, rate. Missing: Instron model, load cell, grips, preload, data rate, unloading endpoint, no compliance/slip correction applied (say so), **definitions of how σ₀.₂, UTS, elongation and E were extracted from a cyclic record**, and **whether the Table 2 replicates were cyclic or monotonic** | E: drive / SC, FC |
| 10 | Specimen counts; exploratory wording | Done (+wording) | Table S1 register, n = 3 in Table 2, n = 1 elsewhere. Wording: "threshold" and "monotonically" remain at lines 85, 254, 256; "exactly those expected" (250) | text |
| 11 | Heating-test protocol | Partial | Done: sequence (3% → zero stress → crosshead returned → heat ≈200 °C at ≈50 °C/s, ≈10 s); 0.5% defined (2.2 → 1.7%); n = 1 per alloy (Table S1); called shape-memory recovery. Missing: heating method, temperature measurement, control mode during heating, fixture expansion | SC |
| 12 | Microstructure evidence | Partial | Done: Sec. 3.1 separates seen from inferred. Missing: how "well under 20 µm" / ">100 µm" were estimated (visual, fields inspected); EDS acquisition conditions; the rod and benchmark-bamboo micrographs are cited as "not shown" — either show them (Online Resource) or cut the detailed claims. Images exist from the JMRT Fig. 10 work | FC, SC, repo |
| 13 | Synchrotron acquisition | Gap (half recoverable) | From repo: 4288 × 4288 detector, 100 µm pixels, distance ≈1.83 m from the r = 18275·tan 2θ calibration, CeO₂ calibrant frame NO7412, benchmark exposure normalization ÷1.625. From J. Yan: detector model, exposure time, transmission geometry, beam overspill, background, specimen location relative to fracture | repo, JY |
| 14 | Rietveld details | Partial | Done: models, space groups, fixed lattice parameters, simultaneous E-WIMV refinement of 72 sectors, R_wp/R_p, 62/34/4 consistent (the July 37% is gone). Missing: background/peak functions and refined variables (in the MAUD `.par` files in `revision/JMRT-R1/xrd/from-scai/`), a conventional observed/calculated/difference plot (Online Resource), the word "semi-quantitative" | repo, text |
| 15 | Limits of ex-situ diffraction | Partial | Sec. 3.3 already treats the pattern as the retained state and leans on the unloading curves. Fix: Sec. 4.1 still asserts the spots-to-arcs change "reflects dislocation multiplication and sub-grain formation" → "is consistent with"; soften "closes the remaining route"; state why 10% vs 8% strain and the ÷1.625 normalization | text, FC |
| 16 | B2/D0₃/carbide identification | Partial | Done: quantified superlattice intensities and S/N, B2 bound, TEM/APT named. Missing: D0₃ spatial scale unknown (say so; the "appears in the α constituent" sentence in 4.2 goes beyond the data); κ reflections not tested in an alternative model (say so) | text |
| 17 | Over-interpretation of anneal trends | Partial | Done: 17a ("as quenched", the on-cooling reading). Missing: Sec. 4.3 still asserts grain growth as the cause and gives a single cause for the elongation drop above 1000 °C; add alternatives (oxidation, decarburization, quench, scatter) and the multiphase/texture/cold-work caveat | text |
| 18 | Scope of AI-design claims | Partial | Done: scoped as a case study (4.4, Conclusions); conclusions survive another route working (4.1). Missing: an explicit attribution of each link (LLM proposal / human choice outside A2 / Si loss in melting / processing) and a short comparison with specialized-LM, CALPHAD-constrained and closed-loop studies (new references, verified) | text + lit |

**Associate editor:** professional English editing requested; changes highlighted; separate response document. Reviewer mark-up files may be in the Author Center (check). No due date in the letter (check the Author Center).

## Tally (23 numbered comments)

Done: R1#2, R1#3, R2#5, R2#10 — 4. Partial: R1#4, R1#5, R2#1, 2, 4, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18 — 16 (most need only text or repo facts). Gap: R1#1 (trivial), R2#3, R2#6 — 3.

No new experiment is required; R2 says so explicitly. Facts that only people hold: R2#3 (FC), R2#6 and #11 (SC), R2#13 (JY), plus R2#9's instrument details (E: drive or SC).

## Process items

1. **Author list:** July = 3 authors; 52497 = 4 (X. Wang added). Adding at revision needs the editor's approval (asked in the Katona draft).
2. **Length:** ≈4,800 → ≈21,000 words. A tracked comparison against July will read as a full rewrite; plan to submit a highlighted version plus a statement that the text was rewritten, with a section map. Consider a trimming pass (the measured/calculated/open caveats repeat across Secs. 3.3, 3.5, 4.1, 4.4 and 5).
3. **English editing:** decide between a paid service and a statement in the response letter.
4. **Reusable answers:** `revision/JMRT-R2/response-R3.md` and `submissions/JMRT-R1-resubmission/response-to-reviewer-*.md` already answer the gauge, DSC, Omori-control, Rietveld and n = 1 questions.
