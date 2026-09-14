# Archive — `calphad/results/` as of 2026-09-14, BEFORE the liquid-phase correction

Copied verbatim from `../results/` on 2026-09-14, before the mpea-02b and PrecHiMn-04
calculations were re-run with the liquid phase included.

**Why.** `step_diagrams.py`, `ni_sensitivity.py` and `agent_window.py` requested `'LIQUID:L'`.
pycalphad names the phase `'LIQUID'` (the TDB type suffix is not part of the name), and `run()`
filtered the unknown name out silently — `step_diagrams.txt` lines 8 and 57 read
`absent  : LIQUID:L`. Every mpea-02b and PrecHiMn-04 number in this folder was therefore computed
for an alloy that could not melt. The mc_fe numbers used the correct name and are unaffected.

**Wrong in this folder:** the 1340 °C (mpea-02b) and 1390 °C (PrecHiMn-04) α solvi of the
LLM-alloy; "mpea-02b returns no liquid at all below 1400 °C"; every mpea-02b solvus in
`NI-SENSITIVITY.md` and `AGENT-WINDOW.md`; the "databases disagree on the solidus" reading;
`step_mpea-02b.png` and `step_PrecHiMn-04.png` above ≈1290 °C.

**Unchanged:** every 1200 °C phase fraction (manuscript Table 3); the ordering results below
≈1100 °C; the κ / M₂₃C₆ / D0₃ statements; all mc_fe sections, including the pdens-2000 refinement
(`mc_fe_llm_refined.csv`, `retry_log.txt`) and its splice into `step_diagrams.csv`.

Do not quote from this folder. The corrected run is in `../results/`; the first liquid-included
check that found the defect is `../../../JMRT-R2/calphad-liquid-check-2026-09-14/`.
