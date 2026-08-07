<!--
ARCHIVED 2026-08-05. Superseded by tasks/todo.md, which re-orders the same work
from easiest to hardest and folds in the CALPHAD feasibility result.
Provenance: this was the first-pass JMRT revision plan, organised by manuscript
phase (Phase 0 unblock -> Phase 5 verify), written the same day the reviews were
triaged. Its blocker D1 ("secure Thermo-Calc access") was resolved on the same
day by a different route -- pycalphad + open TDB databases -- so the phase
ordering here no longer reflects the real critical path. Kept verbatim.
-->

# JMRT major revision — JMRT-D-26-06169

Reviews received 2026-07-27 (R1), 2026-07-28 (R3), 2026-07-31 (R2).
Full analysis: `revision/JMRT-R1/comment-triage.md`. Previous phase archived at
`tasks/todo-archive-2026-07-reformat.md`.

**Status: plan drafted, not yet approved. No manuscript edits made.**

---

## Phase 0 — unblock (Frank)

- [ ] D1 **Secure CALPHAD access** — Thermo-Calc + TCFE via X. Wang (Purdue) or S. Cai (FWM).
      Blocks the answer to R1#2, R3#2, R3#9, R2 R&D#2, R2 Concl#4.
- [ ] D2 Reconnect the **E: drive** (`E:\FE-SMA\` — raw Instron exports, synchrotron/MAUD files)
- [ ] D3 Locate the **original Gemini 2.5 Deep Research transcript** (prompt, constraints,
      candidate ranges, predicted phase constitution)
- [ ] D4 Get the **SME test heating rate and hold time** from S. Cai (R1#7)
- [ ] D5 Confirm the **tensile test standard** actually followed (R2 Exp#2)
- [ ] D6 Check whether **micrographs exist at intermediate anneal temperatures** (R3#11)
- [ ] D7 Confirm the **AGG micrograph interpretation** — arrested/heterogeneous coarsening
      pinned by second-phase bands, vs the current "no AGG" one-liner (A3)
- [ ] D8 Decide **whether any new experiments are feasible** (DSC, EBSD, TEM/APT,
      200 °C-aged benchmark) — sets the scope and timeline of the whole revision

## Phase 1 — new analysis

- [ ] CALPHAD equilibrium step diagrams, both alloys, 400–1400 °C *(blocked on D1)*
- [ ] CALPHAD control run: AI composition with C set to zero — the in-silico C-free variant
      that R1#1 asks for *(blocked on D1)*
- [ ] Ni-equivalent arithmetic written up as the bridging quantitative argument, with its
      stainless-steel-calibration limitation stated (A1)
- [ ] Estimate the **B2 detection limit** of the synchrotron measurement from the Rietveld
      refinement, to bound the "no B2" claim quantitatively (R3#8) *(blocked on D2)*
- [ ] Replicate counts and scatter for Table 2 *(blocked on D2)*
- [ ] Recompute and report both alloys in **measured** at.% as their working identity (R3#3)

## Phase 2 — figures

- [ ] **New AGG figure** — AI-alloy vs Omori-alloy after the identical 3-cycle route, from
      `figures/archive-2026-06-pre-MD-revision/Fig2b_*` and `Fig2c_*` (A3) *(needs D7)*
- [ ] **Add AI-alloy AGG cyclic curve** (`Fig3b_AI_3cycle_AGG_cyclic.png`) (R1#4, R3#4)
- [ ] **Add Omori cyclic curves** (`Fig3c_*`, `Fig3d_*`) so R3#7's comparison is on the page —
      with honest transformation-strain numbers, see the integrity flag in A4
- [ ] **Rebuild Fig. 2** from source data — clipped tick labels, panels too small, and
      700/900/1100 °C missing relative to Table 2 (R2 R&D#3/#4) *(blocked on D2)*
- [ ] Update `figures/captions.md`

## Phase 3 — manuscript rewrite

- [ ] **Title** → LLM-hypothesized + experimental validation + phase stability (R2 Title#1-3, R1#5)
- [ ] **Rename alloys** → "LLM-alloy" / "benchmark alloy" throughout; keep "AI-guided" only for
      the general field. Removes the Al/AI ambiguity for good (R1#5)
- [ ] **Abstract** — novelty, numbers, justified carbon role, why the benchmark works (R2 Abs#1-4)
- [ ] **§1** — delete the "sole variable" sentence (R3#1); broaden the AI-design literature
      (R2 Intro#1); sharpen the gap (R2 Intro#2); add explicit objectives/hypotheses (R2 Intro#4)
- [ ] **§2.1** — position against the lightweight-steel literature and cite Rahnama 2017,
      Saha 2022, Heo 2012 (R3#2); document the LLM workflow reproducibly (R2 Exp#1) *(needs D3)*;
      fix the Si "very close to nominal" claim (R3#3); add the P note (R1#8)
- [ ] **§2.4** — tensile standard (R2 Exp#2) *(needs D5)*; SME heating rate + hold (R1#7)
      *(needs D4)*; fix the ambiguous unload/zero-strain wording (self-audit #6)
- [ ] **New §3.4** — response to the AGG treatment (R1#4, R3#4)
- [ ] **§3.3** — state that in this system martensite is FCC γ and the parent is BCC α, and
      that no ε-HCP or α′ was detected (R2 R&D#6); soften every "no B2" to a
      detection-limit-bounded statement (R3#8)
- [ ] **§4.1** — temper the carbon causality (R1#1, R3#9, A1); add the mechanistic chain for why
      duplex → slip (R1#3); revisit Si in hindsight (R1#6); soften "relies on B2" (R3#10);
      **fix the 34 %/37 % α inconsistency** (self-audit #1)
- [ ] **§4.2** — downgrade recovery/recrystallisation/growth from conclusion to inference; delete
      "single-phase-controlled structural metal" (wrong for a two-phase alloy) (R3#11)
- [ ] **§4.3** — reposition: bounded experimental claim, retained methodological claim; state n=1;
      say plainly that the agent proposed a lightweight-steel composition while believing it was
      proposing an SMA (R3#2, R3#12, R2 R&D#5)
- [ ] **§5** — separate observation from interpretation; broader implications; LLM-only
      limitations; thermodynamic pre-screening *demonstrated* if D1 lands (R2 Concl#1-4)
- [ ] Comment on the 33 % elongation and structural potential (R1#9)
- [ ] Resolve the matrix/island vs 62 %/34 % contradiction (self-audit #2)
- [ ] Fix element ordering title vs abstract (self-audit #3)
- [ ] Update `highlights.md` and the JMRT cover letter to match the tempered claims

## Phase 4 — response letter

- [ ] Point-by-point reply to all 45 comments (R1×9, R2×24, R3×12) — JMRT requires a reply in
      every box, so cross-reference shared answers rather than leaving any blank
- [ ] R1#5: note graciously that the manuscript already reads "AI" (PDF text extraction confirms
      25×"AI alloy", 0×"Al-alloy" — a rendering-font collision), and that we adopted "LLM-" anyway
- [ ] R2-vs-R3 tension on generalisation: address the conflict explicitly to the editor (A-note)
- [ ] Marked-up manuscript with changes tracked

## Phase 5 — verify

- [ ] Every numeric claim in the revised text re-checked against source data
- [ ] Phase fractions consistent across §3.3, §4.1, abstract
- [ ] All new citations resolve via citeproc; rebuild the DOCX
- [ ] Read-through against the reviewer list — confirm no comment left unanswered
- [ ] Commit and push

---

## Review

*(to be filled in after the revision ships)*
