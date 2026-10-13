# JMEP-26-07-50730.R1 — what is still needed, by person (2026-10-12)

Each item names the reviewer comment and where the answer goes. "Not recorded" is an acceptable answer for any fact; the paper will then say so.

## Frank — facts and decisions

**Decisions**
1. **Highlighting method** (AE): tracked changes against the July file (nearly every paragraph marked) or colored text for new material?
2. **English editing** (AE): paid service, or the statement in the letter?
3. **X. Wang as author**: yes/no (Katona draft asks the procedure).
4. **Title** (R2#1a): keep "Absence of Superelasticity in an LLM-Hypothesized …", or the reviewer's "Experimental Evaluation of an LLM-Proposed … Targeted for Room-Temperature Superelasticity"?
5. **Benchmark wording** (R2#7): keep "a reference composition processed in parallel" (step 1, T6/T11) or revert?
6. **Rod and bamboo-benchmark micrographs** (R2#12d): add them to Online Resource 2, or cut the detailed rod description in Section 3.5 back to what Fig. 1d shows?
6b. **SMST 2026 extended abstract** (Cai & Cai, ASM, pp. 11–13, published 2026-05-04, DOI 10.31399/asm.cp.smst2026p0011): it predates the July submission and was not cited there; the 52497 cover letter called it a poster. Now cited in Section 1 and disclosed in the letter — keep (recommended) or remove?

**Facts only you have**
7. **R2#3a** — how many Gemini sessions/runs; why Hypothesis A2 rather than the first-ranked family; how the exact composition was chosen and why it fell outside A2 on Mn (32.3 vs ≤30 wt%) and Al (6.4 vs ≥8 wt%). *This is the reviewer's most pointed question.*
8. **R2#3b** — was the request ever repeated?
9. **R2#2a/2b** — were any files uploaded to the session? Any settings beyond choosing Deep Research?
10. **R2#2c** — where did "over 200 papers" (July text) come from? The report lists 76 sources.
11. **R1#5** — why 0.25 in/min (8.3 × 10⁻⁴ s⁻¹)? Same rate as the NiTi-Cu paper?
12. **R2#9c** — how σ₀.₂, UTS, elongation and E were taken from the cyclic records (Bluehill? by hand? which loading segment?).
13. **R2#9d** — confirm the August n = 3 replicates were cyclic tests (Table S1 says so).
14. **R2#7b** — confirm no cyclic *unloading* record of the benchmark exists for the 1200 °C/1 min condition.
15. **R2#12b** — roughly how many micrograph fields were looked at for the grain sizes.
16. **R2#15d** — why 10% strain for the LLM-alloy and 8% for the benchmark before diffraction.
17. **R2#14a** — the earlier refinement stage that produced 0.62/0.34/0.04 (your 08-14 confirmation): ask Song whether its file still exists.

## Song (Fort Wayne Metals records)

18. **R2#6a — process table**: hot-rolling reductions and pass schedule; redraw sequence; number and duration of intermediate anneals at 1000 °C; cooling medium after homogenization, hot rolling and intermediate anneals.
19. **R2#6b — the 200 °C/3 h age**: quench medium/temperature after the 1200 °C strand anneal, transfer time, aging atmosphere, cooling after aging.
20. **R2#6c — strand furnace**: hot-zone length, temperature calibration, wire tension, argon purity/flow.
21. **R2#6d** — any surface oxidation seen after 1200 °C.
22. **R2#4b** — anything besides oxidation that could explain the Si loss (form in which Si was charged?).
23. **R2#8c** — lab temperature during testing; time/storage between heat treatment and test.
24. **R2#9b — tensile set-up**: Instron model, load cell capacity, grips, preload, data rate, unloading endpoint (zero load or a set threshold), unloading speed. (Also on the E: drive Bluehill files.)
25. **R2#11a–c — heating test**: how the wire was heated (≈50 °C/s rules out a furnace), how temperature was measured, what the machine held during heating (crosshead position?), whether a temperature–time record exists.
26. **R2#12c — SEM/EDS**: instrument, kV, detector; are point or map data available?
27. **R2#14a — residual curves**: re-export observed/calculated/difference curves for both refinements from MAUD with the .esg data (the saved analyses do not store spectra).

## J. Yan (SSRF)

28. **R2#13a** — detector model, exposure time per frame, background (empty-beam/air) measurement, any specimen rotation or translation.
29. **R2#13b** — how the 0.5 mm beam vs 0.36 mm wire overspill was handled.
30. **R2#13c** — where along the gauge the deformed specimens were measured (relative to fracture/neck).

## Claude (in progress)

31. ~~**R2#18c / 3d** — literature comparison~~ DONE 2026-10-12 (Section 4.4 paragraph; 6 new verified refs + existing `aims2022`; A-Lab dropped — 2026 author correction, not alloys; SteelBERT dropped — abstract unreadable without a proxy).
32. After answers: fill the OPEN markers in `response-to-reviewers.md`, apply the matching manuscript edits, build the R1 package (manuscript, tracked/highlighted file vs July, letter DOCX, ESM2 with Table S3 and the new calculation row), and update Table S2 with `phase_compositions_1200.py`.
