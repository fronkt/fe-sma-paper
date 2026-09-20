# Changes from Revision 1 (uploaded 2026-08-21) to Revision 2 — ledger

Companion to `reviewer-comments-verbatim.md` (R3's eight points), `response-R3.md`,
`response-R1-R2.md`, `CoverLetter-R2.md`. Manuscript edits were applied by
`apply_r2_edits.py` (41 checked string replacements, 2026-09-20) on top of the #6 edits of
commit ba9c89f (2026-09-14). Pair: 547 tracked revisions against the R1 clean file.

## 1. Corrections of our own (owned in the letters)

| # | What was wrong | Found how | Fix |
|---|---|---|---|
| 1 | CALPHAD scripts requested `'LIQUID:L'`; pycalphad dropped the unknown phase silently, so mpea-02b and PrecHiMn-04 could not melt. Revision-1 solvi ≈1340/≈1390 °C were artifacts. | Adversarial check 2026-09-14 (`disposition-check-2026-09-14.md`), confirmed in `calphad/results/step_diagrams.txt`. | Scripts fixed, all scans re-run with liquid, GM-arbitrated; Fig. 9 redrawn, **Table 4 new**, every solvus/solidus sentence reworded (commit ba9c89f). |
| 2 | §3.5 "11.0% → 1.4%" 40-min rod comparison attributed to the LLM-alloy. The record (`697-7-SMA-constant.is_tcyclic-697-7.pdf`, exports beside `stress strain-697-7.xlsx`, 0.040 in rod = the benchmark drawing chain) is the benchmark's. | Tag noted 2026-09-14; the spreadsheet name and the diameter chain seen on the mounted E: drive 2026-09-20. | Withdrawn. Replaced by the LLM-alloy wire record: Fe-SMA-FC spool 11 (1200 °C/4 fpm + age, 25.5%) vs spool 15 (40 min + age, 0.8%) and spool 16 (80 min, 0.5%), 127 mm gauge. **S. Cai to confirm** (email). |
| 3 | R1-round belief that no heating-test record existed and that "every Instron header prints 5.000 in". | `E:\FE-SMA\mechanical\Fe-SMA-TENSILE-HEAT.is_tcyclic` (2026-01-20) found 2026-09-20; its traces reproduce Fig. 3 (benchmark 0.0211 in, 4.47% max, 753 MPa; LLM 0.01387 in). Gauges across the ten reports: 5.000 / 2.000 / 1.000 / 0.236 in. | Fig. 3 caption carries diameters and 127 mm; §2.4 gives the gauge per dataset. Record copied to `mechanical/raw-exports/`. |
| 4 | "1006 MPa at 11.9%" three-cycle specimen quoted without its 6.0 mm gauge. | `Frankie-Fe-SMA-6mm gauge lenght testing.is_tcyclic-697-6.pdf`. | Gauge stated; not compared with 127 mm strains (§2.4, §3.5, Fig. 10e). |
| 5 | Front matter carried "[ZIP — confirm]" placeholders. | Frank's 2026-09-15 edit of the R1 clean DOCX in Word dropped them. | `front_JMRT.md` now matches. |

## 2. Point-by-point (R3)

| Pt | Manuscript change | Where |
|---|---|---|
| 1 | Held / corrected / withdrawn-and-replaced table in the letter; §5 gets two paragraphs on the order in which the evidence arrived and what was reinterpreted; "locate the cause" → "indicate the cause" (abstract), "identify the origin" → "indicate the origin" (§5). | Abstract, §5 |
| 2 | §4.4 ¶1 rewritten (limitation of the workflow as run, not of what an LLM can propose); second-session test declined with reason (§4.4 ¶3); new contribution paragraph (three claims + "the check is not claimed as new"); §4.4 last sentence rewritten; §1 "200 papers" → 76 sources retrieved at query time; §5 Limitation 2 restated on the record (prompt unpreserved). | §1, §4.4, §5 |
| 3 | §2.2 rewritten: per-specimen schedules (rod 2-/3-cycle 1200 ↔ 900 °C; quartz-tube 4 × 1200 °C/30 min + cold zone, no 900 °C step, Fig. 1d wire "on the processing log"; benchmark argon 5 × 1200 ↔ 900 + 1 h); exposures above 1200 °C disclosed (1250 °C × 5/20 min, 1300 °C cycle); Ref 18 "same type", Viebranz 2024 cited for the rod schedule; §3.5 ¶1 chronology (AGG runs 2025, CALPHAD 2026) and intent; mechanism paragraph reworded (no leg of the cycle in single-phase α). | §2.2, §3.5, Fig. 1 caption |
| 4 | 13 mm = typo; §2.4 gauge per dataset (127 / 6.0 / 25.4 mm); Fig. 3 record located; Fig. 2 caption diameters 0.348–0.359 mm; Table 2 caption names gauge, E apparent; letter table of datasets; repeats (Aug-2026 replicates) and reprocessing (Fig. 2 re-plot only) enumerated. | §2.4, captions |
| 5 | Conditions enumerated where the conclusion is drawn (abstract, §3.2, §3.3, §3.5, §4.1); §3.2 "regardless of heat-treating condition" removed; §4.1 opens with the three-level statement (measured / calculated / not claimed); "unavailable at any temperature" → "on the equilibrium calculation … in the solid state". | Abstract, §2.4, §3.2, §3.3, §3.5, §4.1 |
| 6 | Done 2026-09-14 (liquid included; Table 4; Fig. 9; §2.6 grid arbitration disclosed). DTA declined with reason. | §2.6, §3.4, §4.1, §4.2, §4.4, §5 |
| 7 | Bracketing paragraph withdrawn; **new Fig. 10** (six records from raw exports, gauges stated); 40-min record corrected (item 2 above); heating test on cyclic condition stated as not done, rods fracture below 3%, wire test requested; phase fractions for 40-min / Fig. 8 stated as not refined; §3.5 ¶8/¶9/¶12/¶13 rewritten; quartz-tube wire retained ductility (≈26% at 25.4 mm gauge) → "loss of ductility follows the coarsening, not the treatment as such". | §3.5, §2.4, §4.1, §4.4, §5 |
| 8 | Ms reading demoted to one of two open readings; EDS partitioning stated as non-discriminating; EBSD+EDS / areal fraction named; DSC named in §4.1 and §4.4 with its limit; §3.1 Widmanstätten sentence bounded; three "equilibrium, not incompletely transformed" sentences reworded (§3.3, §3.5, §4.1); "precisely what is observed" → "in kind, though not in proportion"; "retained γ" → "present before loading". | §3.1, §3.3, §3.5, §4.1, §4.4 |

## 3. Numbers introduced this round and their sources

| Statement | Source |
|---|---|
| Fig. 3 diameters 0.352 / 0.536 mm, 127 mm gauge, 20 Jan 2026 | `mechanical/raw-exports/Fe-SMA-TENSILE-HEAT.is_tcyclic.txt` (spools 2 / 1) |
| 40 min + age 0.8%, 80 min 0.5%, 1 min + age 25.5% (0.36 mm wire, 127 mm) | Fe-SMA-FC spools 15, 16, 11 (`instron-reports-extracted.txt`; raw CSVs in `raw-exports/`) |
| 1250 °C × 5 / 20 min: 12.5 / 6.3% | Fe-SMA-FC spools 13, 14 |
| 1300 °C cycle wire fractured below 4% | Fe-SMA-oct-11-25 spool 6 (report 4.1%, incl. post-fracture travel; curve fractures ≈3.5%) |
| Two-cycle rods 568 / 608 MPa, 1.0%, one unloading each | Fe-SMA-FC spools 17, 18 |
| Three-cycle + age rod 478 MPa, 0.5% (127 mm); 1006 MPa, 11.9%, eight unloadings (6.0 mm) | Fe-SMA-FC spool 19; Frankie-6mm spool 2 |
| Quartz-tube wire 1020 MPa, eight unloadings, fracture ≈26% on 25.4 mm (report prints 51.3% = post-fracture crosshead travel) | Fe-SMA-oct-11-25 spool 2 |
| Fig. 2 spool diameters 0.348–0.359 mm | `rebuild_figure2.py` SPOOLS (0.01370–0.01415 in) |
| 76 sources in the agent's report | `revision/JMRT-R1/llm-provenance/` |

## 4. Phrase checks used on the clean DOCX (all passed 2026-09-20)

present: "Fig. 10", "Table 4.", "Viebranz", "Three levels of evidence", "quartz tube", "25.5% to 0.8%".
absent: "[ZIP", "11.0%", "200 published", "1340", "locate the cause", "regardless of heat-treating",
"incompletely transformed", "reading the present data favor", "eight anneal conditions".

## 5. Still open (not blocking upload; declared in the letters)

- Wire AGG + 3% loading–unloading–heating test — S. Cai (R3 #7).
- DSC for Ms — S. Cai (R3 #8).
- SEM-BSE areal fraction on the 40-min mount — S. Cai (R3 #7, optional).
- S. Cai's confirmation of the four record readings (40-min report heat; schedules per specimen; 1300 °C and oct-11-25 spools 3–5; Fig. 8 specimen).
- ~~Frank: gauge of the 2026-08-20 replicates~~ — confirmed 127 mm by Frank, 2026-09-20.
- Abstract is 281 words (R1 was 276).
