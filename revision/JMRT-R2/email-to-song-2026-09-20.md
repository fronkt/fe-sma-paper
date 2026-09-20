# Email to S. Cai — updated 2026-09-20 (supersedes `email-to-song-2026-09-14.md`, which was never sent)

**To:** song_cai@fwmetals.com (confirm). **Gmail draft** `r-8156261437952857119` updated 2026-09-20 with this text — Frank sends, and attaches
`submissions/JMRT-R2-resubmission/Cai_Fe-SMA_JMRT_R2_marked-up.docx` and `…response-reviewer-3.docx`.
**Subject:** Fe-SMA JMRT revision — draft ready, 4 things to confirm + 2 tests (due Sept 22)

---

Hi Song,

JMRT sent the Fe-SMA paper back as a major revision, due September 22. Reviewers 1 and 2 are done (R2 recommends acceptance). Reviewer 3 has eight points, and I have drafted the full revision and the response — marked-up manuscript and the R3 letter attached. Most of it is writing, but a few things rest on your record, and I want you to confirm them before I upload.

What the E: drive already settled:

- The Fig. 3 record is the "Fe-SMA-TENSILE-HEAT" run of Jan 20, 2026 — 5 in gauge, spool 1 = 697-7 at 0.0211 in, spool 2 = 697-6 at 0.01387 in, both 1200C/4fpm. The traces reproduce both panels, so R3's gauge question (13 mm vs 127 mm) is answered: 13 mm was a typo, everything in Figs. 2 and 3 is 127 mm. Nothing needed from you there.

Four things to confirm:

1. The 40-minute rod record. §3.5 of the R1 manuscript said the LLM alloy rod went from 11.0% to 1.4% elongation after 1200 °C/40 min + age. Those rows are in "697-7-SMA-constant.is_tcyclic-697-7.pdf" (0.040 in rod, 500–1200 °C sweep, row 9 hydrogen), and its exports folder holds your "stress strain-697-7.xlsx". The file tag, the spreadsheet name and the 0.040 in diameter (your 697-7 drawing chain) all say benchmark, so I have treated it as benchmark and withdrawn those numbers. In their place I used the LLM wire spools from Fe-SMA-FC: spool 11 (1200C/4fpm + 200C/3h, 25.5%) vs spool 15 (1200C/40m + 200C/3h, 0.8%) and spool 16 (1200C/80m, 0.5%). Please confirm the 697-7-SMA-constant report is the benchmark. If it is actually 697-6, tell me and I will put the rod numbers back.

2. The AGG schedules as I have now written them in §2.2: LLM rod (≈1–1.3 mm) 1200C/30m WQ + 900C/15m, ×2 with a final 1200C/30m WQ, or ×3 with a final 1200C/60m WQ; the 10/11/25 quartz-tube run with both alloys (697-6 at 0.014 in, 697-7 at 0.025 in), 1200C/30m in Ar then cold zone 10 min, four holds, water quench, no 900 °C step; and the benchmark 0.64 mm wire in argon, 1200C/30m ↔ 900C/10m five times then 1200C/1 h. Is that right? I have written that the Fig. 1d wire (FeMnAlNiSiC-3 cycle AGG ht.jpg, 0.36 mm) is from the quartz-tube run — correct?

3. Two runs I found on the drive that are in no note: the "FeMnAlNiSiC-1300C-3 time" wire (oct-11-25 spool 6, and the 697-6-WQ micrographs "1300C30m-RT10m-2cycle-1300c45m"), and oct-11-25 spools 3–5, which are labelled LLM alloy but are 0.02075 in — the benchmark diameter. What were they? I have only used spool 2 (LLM, 0.01402 in, the quartz-tube wire) in the new Fig. 10, and I mention the 1300 °C exposure in §2.2 as one of the runs above 1200 °C.

4. The SSRF AGG diffraction specimen (Fig. 8): was that rod or wire, and from which run?

Tests R3 asks for — I have told the editor both are outstanding and asked for an extension on them only if the editor wants them:

a) One 0.36 mm LLM wire through the quartz-tube AGG cycle, then the 3% loading–unloading–heating test, same as Fig. 3. R3 rejected the argument that the 1-min and 40-min conditions bracket the AGG condition. The rods fracture below 1%, so only the wire can carry this test.

b) DSC on the 1200C/4fpm LLM wire, −150 °C to 500 °C or higher, benchmark wire as control. R3 wants Ms measured. I would report it as a bound whichever way it comes out.

c) Optional: if the 1200C/40m mount still exists, an SEM-BSE areal fraction of α vs γ (R3 wants phase fractions for Fig. 1a vs 1c). If it does not exist, I have already said so.

One more thing. I found a bug in our CALPHAD scripts: the liquid phase was silently dropped from two of the three databases, so the 1340 °C and 1390 °C solvus values in §3.4 were computed for an alloy that could not melt. With liquid included the alloy starts melting at about 1240–1300 °C while γ is still present, so there is no single-phase α field in the solid state in any database; the carbon-free variant is single-phase α from about 1130–1160 °C up to its solidus. The conclusion gets cleaner, but every quoted temperature changed, and Fig. 9 and a new Table 4 carry the corrected numbers. I have owned the error in the response.

Thanks,
Frank
