# The LLM session, recovered — closes blocker D3

**Artifact:** `Gemini-DeepResearch_New-Fe-SMA-Alloy-Hypotheses_2025-06-04.pdf` (41 pp., 750 KB)
**Found:** 2026-08-09, `E:\FE-SMA\697-6-7 Fe-Mn-Al-Ni-Si\New Fe-SMA Alloy Hypotheses_.pdf`
**Extracted text:** `transcript-extracted-text.txt` (pypdf; 114,890 chars)

Answers **R1#2** (what did the model actually predict? did it consider D0₃?),
**R2 Experimental#1** (document the workflow reproducibly), and bears directly on **R3#12**.

---

## 1. What the artifact is, and what it is not

| | |
|---|---|
| Title (PDF metadata) | *New Fe-SMA Alloy Hypotheses* |
| Producer | `Skia/PDF m138 Google Docs Renderer` — a Deep Research report exported to Google Docs, then to PDF |
| PDF ModDate | **2025-06-04 10:39:30 −04:00** |
| Sources cited | **76**, every one stamped *"accessed May 19, 2025"* |
| Structure | 9 sections + Works Cited; §7 carries the six hypothesised alloy families; Table 4 is the summary |

Two dates, and they matter. The literature sweep ran on **19 May 2025**; the document was exported
on **4 June 2025**. S. Cai's process note opens with *"Request a 5-6 pounds ingot based on Al
suggestion: **(6/4/25)**"* followed by the composition that was melted. The ingot was requested the
same day the report was exported. Provenance between the artifact and the heat is therefore firm.

> **The verbatim prompt is not recoverable from this artifact.** A Deep Research report does not
> embed the user's query, and a search of all 41 pages returns no prompt-like text. The model,
> the tool, the dates, the full candidate set and the complete reasoning are documented; the exact
> wording of the request is not. §2.1 must say so rather than paraphrase a prompt it cannot quote.
> What §2.1 currently describes as four instructions given to the agent should be reworded as a
> description of what the report addressed, unless Frank can recover the session itself.

---

## 2. The six candidates the agent actually proposed

From Table 4, verbatim ranges, **wt.%**, Fe balance in every case:

| ID | Proposed range | Target precipitate | Predicted strain / stress |
|---|---|---|---|
| **A1** | Mn 25–35, Al 10–15, Ni 2–5, Cr 3–8, C 0.1–0.5 *or* V 0.5–2 | β (Ni,Cr)Al + MX/M_xC_y | 4–7 %, 300–600 MPa |
| **A2** | **Mn 20–30, Al 8–12, Si 1–4, Ni 3–6, B 0.005–0.05 *or* C 0.1–0.3** | β Ni(Al,Si), 5–15 nm coherent | **5–8 %, 400–700 MPa** |
| **B1** | Mn 15–25, Si 4–7, Cr 8–15, Ni 0–2, V 0.5–1.5, C 0.1–0.4 | (V,Cr)C, γ↔ε | 3–6 %, 250–500 MPa |
| **B2** | Mn 15–25, Si 4–7, Cr 8–15, Al 1–3, N 0.05–0.2 &/or C 0.1–0.3 | AlN, Cr(C,N) | 2–5 %, 200–450 MPa |
| **C1** | Al 5–12, Cr 5–15, Mn 10–25, C 0.5–1.5 | κ-(Fe,Mn,Cr)₃AlC | 3–6 %, 300–600 MPa |
| **C2** | Al 3–8, Mn 15–30, N 0.1–0.5 | AlN / (Mn,Al)N_x | 2–4 %, 250–500 MPa |

**The agent's own priority order (§8.2) put A2 second, not first.** Its ranked recommendation was:

1. **B1** — *"appears highly promising… the base Fe-Mn-Si-Cr system is very low cost, and the V-C
   precipitation strategy has already demonstrated significant PE"*
2. **A1 and A2** — *"offer a good chance of success by modifying the known Fe-Mn-Al-Ni system"*
3. C1  4. B2 and C2

The alloy that was synthesised is **A2**, the joint-second recommendation. The agent's first choice
was never made. That is a legitimate thing to have done — A2 builds on the Omori family the group
already had a benchmark for — but the paper should not describe the tested composition as *the*
agent's recommendation.

---

## 3. The composition made was outside the window it was drawn from

Comparing A2's range against the heat, all in wt.%:

| Element | A2 proposed | melted (nominal) | measured (ICP-AES) | verdict |
|---|---|---|---|---|
| Mn | 20 – 30 | 32.3 | 31.78 | **above the ceiling** |
| Al | **8 – 12** | **6.4** | **6.24** | **below the floor, by 1.6–1.8 wt.%** |
| Si | 1 – 4 | 2.2 | 1.11 | inside (measured near the floor) |
| Ni | 3 – 6 | 4.6 | 4.81 | inside |
| C | 0.1 – 0.3 | 0.1 | 0.105 | inside, **at the floor** |

The aluminium gap is the large one, and it is larger than the wt.% figures make it look. In this
alloy's context A2's **8–12 wt.% Al is 14.9–21.5 at.%**; the wire contains **11.9 at.%**. The alloy
holds roughly **four-fifths of the minimum aluminium the agent specified and two-thirds of its
midpoint** — and 12 at.% Al is also below the Omori benchmark's 15 at.%. Aluminium is the strongest
ferrite stabiliser present, so the deviation runs in the austenite-forming direction, which is the
direction of the observed failure.

**§2.1 currently reads "Within one of the AI-suggested composition ranges, we selected a composition
of 50Fe-30Mn-12Al-4Ni-4Si (at%)". That sentence is not accurate and must be corrected.** The
composition is inside the window on Si, Ni and C, and outside it on Mn and Al. Left as written it is
exactly the kind of claim a round-two reviewer with the transcript in hand would take apart, and the
transcript is about to become supplementary material.

---

## 4. Would a composition inside the window have worked? No.

The deviation in §3 raises the obvious question, and it decides how strongly the paper may state its
conclusion. It was tested rather than argued: `../calphad/agent_window.py`, results in
`../calphad/results/AGENT-WINDOW.md`. The short answer:

**Every composition inside the agent's own A2 window fails the same way the alloy failed, and for
the same reason.** With carbon anywhere in the range the agent specified, no point in the window has
a single-phase α field at the 1200 °C solution treatment:

| point (wt.%) | α solvus | phases at 1200 °C |
|---|---|---|
| as made — Mn 32.3, Al 6.4, Ni 4.6, C 0.1 | 1330 °C | 76.0 α + 24.0 γ |
| A2 midpoint — Mn 25, Al 10, Ni 4.5, C 0.2 | **1380 °C** | 86.7 α + 13.3 γ |
| A2 most-ferritic corner — Mn 20, Al 12, Ni 6, C 0.1 | 1230–1240 °C | 98.2 α + 1.8 γ |
| A2 most-austenitic corner — Mn 30, Al 8, Ni 3, C 0.3 | **none ≤1400 °C** | 64.0 α + 36.0 γ |

Three things follow, and all three help the paper.

1. **The midpoint of the agent's window is *worse* than what was made** — solvus 1380 °C against
   1330 °C — because moving to the middle of the range means taking the middle of the carbon range
   too, 0.2 wt.% instead of 0.1. Carbon dominates, exactly as Sec. 4.2 argues.
2. **Even the most ferrite-favouring corner the window permits does not open an accessible field.**
   Its solvus is bracketed 1230–1240 °C (1220 °C is 99.3 % α + 0.7 % γ; 1230 °C did not converge;
   1240 °C is single-phase), still above the 1200 °C treatment — and §2.2 records that annealing
   above 1200 °C caused severe oxidation or furnace contamination, so the extra 30–40 °C was not
   available in practice. That corner is also 20 wt.% Mn / 12 wt.% Al / 6 wt.% Ni, nothing like the
   heat that was cast.
3. **The carbon that closes the window was the agent's own specification, and the melt took the
   minimum it allowed.** A2 permits 0.1–0.3 wt.% C; the heat was made at 0.1. Every other carbon
   choice inside the window is worse. The paper's central claim therefore does not depend on the
   Mn/Al deviation at all.

One caveat, stated rather than buried: mpea-02b cannot carry silicon, so Si was folded into iron for
this scan. That is least defensible at the ferritic corner, where Si reaches 6.8 at.%. An mc_fe
cross-check carrying all six elements is running against the four named points; see
`AGENT-WINDOW.md` for the outcome.

---

## 5. R1#2's two direct questions, answered from the source

**"Did the model predict single-phase BCC?"**

Not in those words. The phrase *"single-phase"* appears **nowhere in the 41 pages**. What A2 says is:

> *"Fe, Mn, Al, Ni: Form the bcc parent phase and β (NiAl-type) precipitates."*
> *"Primary: Coherent, nano-scale β (B2-ordered, Ni(Al,Si)-type or (Ni,Si)Al-type) precipitates,
> 5-15 nm."*

So it specified **a bcc parent with coherent 5–15 nm B2 precipitates** — the Omori microstructure —
and it never issued a phase-fraction prediction, a phase-diagram calculation, or a solution-treatment
window for any of the six candidates. It named the microstructure it wanted without establishing that
the composition could produce it. That, and not a wrong number, is the failure mode the paper should
report.

**"Did it consider D0₃?"**

**No. Zero occurrences of `D0₃`, `DO3`, `D03` or `Fe₃Al` in the entire report.** The phase that
actually formed is absent from the reasoning that produced the composition.

This is not ignorance of ordered Fe-Al chemistry in general — **κ-carbide appears 24 times**, and
Hypothesis **C1** is built entirely on κ-(Fe,Mn,Cr)₃AlC in an Fe-Al-Cr-Mn-C alloy at Al 5–12 wt.%.
The agent knew that Fe-Al-Mn-C forms ordered carbides at aluminium levels *bracketing the one that
was eventually melted*. It simply never connected that knowledge to A2, where it kept Al high enough
(8–12 wt.%) that the β-NiAl reasoning was self-consistent. The failure is one of transfer between its
own hypotheses, which is a sharper and more interesting finding than "the model did not know".

**A third question worth answering, which no reviewer asked:** the agent explicitly recommended the
calculation that would have caught this.

> §8.3: *"Computational tools, such as CALPHAD for phase diagram prediction and precipitate
> stability, and Density Functional Theory (DFT) for understanding precipitate-matrix coherency and
> energetics, **should be employed to guide experimental design** and accelerate the development
> process."*

That is the only occurrence of "CALPHAD" in the report — a recommendation for future work, not
something the agent performed. It changes the shape of the paper's methodological claim, and
improves it. The honest version is not *"the LLM failed to consider thermodynamics"* but
**"the LLM proposed compositions it had not thermodynamically screened, flagged that screening as
necessary, and the recommendation was not acted on before melting."** That is a workflow failure
with a named, generic, cheap fix — which is precisely the methodological contribution R3#12 disputes,
now defensible on the record instead of by assertion.

---

## 6. What has to change in the manuscript

| § | Change | Driver |
|---|---|---|
| 2.1 | Replace "Within one of the AI-suggested composition ranges, we selected…" with the true relation: drawn from Hypothesis A2, inside it on Si/Ni/C, outside on Mn and Al, with the Al figure given | §3 above |
| 2.1 | State model + tool + dates (Gemini 2.5 Deep Research; sources accessed 19 May 2025, report 4 June 2025; 76 sources; six candidates) and say the verbatim prompt is not preserved | R2 Exp#1 |
| 2.1 | Reword the four "instructions" — they describe the report's content, not a quotable prompt | §1 above |
| 2.1 / 4.4 | A2 was the agent's **joint-second** choice; B1 was first and was never made | §2 above |
| 3.4 / 4.2 | Add the window result: no point inside A2 opens the α field, and the midpoint is worse than what was made | §4 above |
| 4.1 | The agent never predicted D0₃ — quote the zero count; note κ-carbide was in its C1 reasoning but not transferred | R1#2 |
| 4.4 | Reframe from "the model could not capture" to "the model did not screen what it itself said should be screened" | R3#12 |
| SI | Attach the report as supplementary material | R2 Exp#1 |

## 7. Still open

- **The verbatim prompt.** Only Frank's Gemini account history can supply it. If it is gone, §2.1
  says so — and that is itself a finding about AI-assisted design provenance worth one sentence.
- **Which Gemini model served the 19 May 2025 run.** §2.1 currently cites Gemini 2.5. The artifact
  does not record a model string; the citation is to the Gemini 2.5 report [@comanici2025gemini].
  Confirm, or soften to "the Gemini Deep Research tool as deployed in May 2025".
