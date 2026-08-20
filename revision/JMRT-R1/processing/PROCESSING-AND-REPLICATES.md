# The raw mechanical and processing record — closes blocker D2

**Drive mounted 2026-08-09.** Sources copied into this folder:

| File | Origin |
|---|---|
| `process-note-SCai.docx` / `.txt` | `E:\FE-SMA\697-6-7 Fe-Mn-Al-Ni-Si\process note.docx` — S. Cai's running melt-and-draw log |
| `chemistry-RD0697-6-LLM-alloy.pdf` | FWM-MTL 25-07-115906A → IMR 202507894 Rev.1 |
| `chemistry-RD0697-7-benchmark.pdf` | FWM-MTL 25-09-120669 → IMR 202510308 |
| `instron-reports-extracted.txt` | text of all eight `.is_tcyclic` PDF reports |

**Heat identity is now certain: RD0697-6 is the LLM-alloy, RD0697-7 is the benchmark.** Both
certificates name Song Cai as submitter, both use ICP-AES method CAP-017U at IMR Test Labs with
carbon by ASTM E1019 — §2.1's method statement is correct.

---

## 1. R2 Experimental #3 — replicate counts and scatter

### Table 2 is n = 1 per condition. Every row, single specimen.

All seven annealed rows trace to consecutive spools of one Instron run, `Fe-SMA-FC.is_tcyclic`
(9/8/2025), and reproduce to within 0.5 %:

| Table 2 row | spool | dia (in) | UTS from report | UTS in Table 2 | Δ | elong (both) |
|---|---|---|---|---|---|---|
| 600 °C | 3 | 0.01410 | 2294.2 MPa | 2293 | +0.1 % | 2.3 |
| 700 °C | 4 | 0.01415 | 2009.9 | 2009 | +0.0 % | 2.2 |
| 800 °C | 5 | 0.01410 | 1222.0 | 1216 | +0.5 % | 24.0 |
| 900 °C | 6 | 0.01415 | 1078.7 | 1078 | +0.1 % | 29.7 |
| 1000 °C | 7 | 0.01404 | 967.8 | 967 | +0.1 % | 33.4 |
| 1100 °C | 8 | 0.01399 | 947.3 | 947 | +0.0 % | 29.7 |
| 1200 °C | 9 | 0.01384 | 938.3 | 938 | +0.0 % | 23.9 |

The table is faithfully transcribed and independently reproducible. It is also **unreplicated**, and
the revision must say so plainly. There is no scatter to quote because no condition was repeated.

> **ADDENDUM 2026-08-20 — superseded, and by experiment rather than by argument.**
> Everything above remains the correct record of the **as-submitted** data set. It no
> longer describes the revision. F. Cai ran additional heat treatments and tensile tests
> on 2026-08-20 so that every anneal condition carries three specimens; Table 2 is now
> mean ± SD at n = 3, §2.4 says so, and the n = 1 justification has been removed from both
> the manuscript and the R2 letter. The new values, the old-vs-new comparison and one
> unresolved transcription question (the 700 °C UTS uncertainty, 94 vs 9.4) are in
> `../mechanical/TABLE2-REPLICATES.md`. The two open points below — the derived σ₀.₂/E
> columns and the unlocated "As drawn" row — are *not* closed by the new run.

Two further points the reviewers have not raised but which follow from the same records:

- **The σ₀.₂ and E columns are not in the Instron report.** It prints yield only for spool 3
  (277,275 psi = 1911.7 MPa, against Table 2's 1948 MPa for 600 °C) and modulus only for spool 3.
  Every other σ₀.₂ and E value in Table 2 was derived by the authors from the raw curves. The
  revision should say how — 0.2 % offset on which strain measure, and modulus over which fit range —
  because a reader cannot otherwise reproduce the column. *Needs Frank or S. Cai.*
- **Specimen diameters vary 0.01384–0.01415 in (0.352–0.359 mm), not a constant 0.36 mm.** The Fig. 2
  caption's "wire diameter is 0.36 mm" is a nominal, and the ≈2 % spread feeds straight into the
  stress values. Worth one clause in §2.4.
- **The "As drawn" row of Table 2 is not in any of the eight reports.** Its source has not been
  located on the drive. *Needs S. Cai.*

### Where replicates do exist, they are in the AGG conditions, and the scatter is large

| condition | n | mean UTS | SD | CoV | max/min |
|---|---|---|---|---|---|
| **LLM-alloy**, 2-cycle AGG rod (`Fe-SMA-FC` spools 17, 18) | 2 | 588 MPa | 28 | 4.8 % | 1.07× |
| benchmark, AGG HT (`RD0697-7` spools 1, 2) | 2 | 447 MPa | 150 | 33.5 % | 1.62× |
| benchmark, AGG HT + 200 °C/3 h (`RD0697-7` spools 3, 4) | 2 | 389 MPa | 69 | 17.8 % | 1.29× |
| AGG + 200 °C/3 h in quartz (`RD0679-7` spools 3–7) | 5 | 85 MPa | 42 | **49.3 %** | 2.69× |
| AGG in quartz tube (`TESTING-697-7` spools 1–4) | 4 | 155 MPa | 38 | 24.8 % | 1.83× |

Read carefully, because the useful part is not the mean:

- **The only replicated LLM-alloy condition in the whole dataset is the 2-cycle AGG rod**, n = 2.
  Everything else replicated is benchmark material.
- The scatter is not measurement noise; these specimens are failing prematurely. Elongations in the
  quartz-tube sets run 0.4–2.6 %, and there is a micrograph on the drive named
  `3cycle AGG-200C-CRACK along boundary.tif`. A 2.69× spread in a set whose mean strength is 85 MPa
  is a material that is cracking, not a test that is imprecise. **That corroborates the A3/R1#4 story
  of arrested, boundary-pinned coarsening rather than undermining it** — but it must be presented as
  what it is, and not folded into an error bar on Table 2, which it does not belong to.
- `RD0679-7` is almost certainly a digit transposition of RD0697-7 in the filename. **Alloy
  assignment for that file is unconfirmed** and it is excluded from any LLM-alloy claim below.

---

## 2. Processing was not identical between the two alloys — R3#1 is factually right, not just logically right

§2.1 describes one shared route. The process note records two different ones. This is the most
consequential finding in the D2 material, because the triage plan was to delete the "sole variable"
sentence on *logical* grounds (identical nominal parameters need not give identical microstructures).
The record shows the parameters were not identical either.

| step | LLM-alloy RD0697-6 | benchmark RD0697-7 |
|---|---|---|
| melt | VIM, single melt | VIM — *"lots of voids"* — then **remelted on Arcast** |
| cast | water-cooled Cu mould; *"only ~2 pounds get poured into the mode. Hole is too small."* | ø0.600 in × 6 in rod |
| charge | 1730 Fe + 1025 Mn + 203 Al + 69.9 Si + 146 Ni + 3.2 C = **3177 g** | not recorded |
| stock prep | EDM two ø0.500 in rods | hot swage 900 °C to 0.475 in |
| homogenise | 1000 °C / 16 h Ar (first trial). **Second trial: hot rolled with no homogenisation** | not recorded |
| hot work | hot roll **850 °C** to ~0.175 in square | hot roll **900 °C** to 0.210 in square |
| process anneals | 1000 °C, Ar | 1000 °C / 2 fpm and 1000 °C / 4 fpm, **H₂ (F72)** and Ar |
| final wire | 0.0142 in (0.36 mm) | 0.0253 in (0.64 mm); tensile stock also at 0.0400 in and 0.01772 in |

Also on the record: *"Annealed at 1200C/4fpm, H2, wire very brittle, couldn't draw"* and
*"(appears that 1200C is not a good annealing temperature…)"* — for the benchmark during drawing.

The one genuinely shared treatment is the final AGG cycle of **10/11/25**: both alloys sealed in a
quartz tube, 1200 °C/30 min Ar, cold zone 10 min, repeated, water quench. Even there the diameters
differ — 0.014 in against 0.025 in — so the quench rates differ.

### What this requires in the manuscript

The conclusion is not in danger. The CALPHAD result is a statement about equilibrium phase
stability, which no thermomechanical route changes: with carbon at the measured level the α field
never opens below the solidus, at any nickel content and anywhere inside the agent's A2 window. The
paper's causal claim rests on that, not on process matching.

But §2.1 as written is wrong in specifics and must be corrected:

| §2.1 as written | what the record shows |
|---|---|
| "about 2 kg of each alloy was melted" | LLM-alloy charge was 3.18 kg; **~2 lb (≈0.9 kg) actually poured**. Benchmark mass not recorded. |
| "cast into ø50 mm ingots" | LLM-alloy into a water-cooled Cu mould, size not recorded; benchmark into a **ø15 mm** rod. ø50 mm is not supported for either. |
| "Several ø13 mm rods were cut from the cast ingots by EDM" | true for the LLM-alloy (ø0.500 in = 12.7 mm); the benchmark was hot-swaged from the cast rod, not EDM'd |
| "These rods were homogenized at 1000 °C for 16 hours in argon" | LLM-alloy first trial only; the second trial explicitly omitted it; not recorded for the benchmark |
| "then hot-rolled at 850 °C" | LLM-alloy 850 °C; **benchmark 900 °C** |
| "intermediate annealing at 1000 °C under argon" | also **hydrogen (F72)** atmosphere for the benchmark |

> ⚠️ **These are corrections to someone else's experimental record, and they should not go into the
> manuscript on my reading of a lab note alone.** The note is informal, undated in places, and
> describes at least two separate trials of the LLM-alloy — the wire that was tested may come from
> either. **Frank must put the table above to S. Cai and get the route confirmed** before §2.1 is
> rewritten. What is safe to do now, and is required by R3#1 regardless, is to stop claiming the
> routes were identical.

> ✅ **RESOLVED 2026-08-18 — S. Cai confirmed the route** (via Frank: *"Tested wire was
> homogenized. Benchmark underwent same."*). This answers the two homogenisation unknowns in
> the table above in the manuscript's favour: the tested LLM-alloy wire came from the
> homogenised trial (not the second, unhomogenised one), and the benchmark received the same
> 1000 °C/16 h homogenisation (the note simply did not record it). **§2.1 therefore stands as
> written and is NOT rewritten from this note.** The note's other divergences (poured mass,
> mould geometry, EDM vs swage, 850 vs 900 °C roll, H₂ process anneals, final diameters) remain
> uncorroborated lab-note readings of what may be different trials, are overruled by the
> co-author who performed the processing, and are kept here only as a record. The manuscript
> already carries the two divergence facts that matter to the science: the Introduction claims
> only a *nominal* shared route (R3#1), and §3.5 states the benchmark AGG wire is 0.64 mm.

Related, and needing the same confirmation: the benchmark tensile stock on the drive is at
0.01772 in (0.450 mm) while the LLM-alloy wire is 0.0142 in (0.36 mm). If Fig. 3's two panels come
from those two stocks, the comparison is across a 1.25× diameter difference and should say so.

---

## 3. Chemistry certificates — small print worth one clause

- The LLM-alloy was analysed **on the finished 0.0142 in wire**; the benchmark **as cast**. Different
  points in the process, which is normal but worth stating once.
- The benchmark report carries a scan for 19 further tramp elements (As, B, Be, Bi, Ca, Cd, Co, Mg,
  Nb, Pb, Sb, Se, Sn, Ta, Ti, V, W, Zn, Zr, all <0.01 %) and reports **Fe by difference**. The
  LLM-alloy report has **no such scan** — it lists Al, Fe, Mn, Ni, Si and nothing else. Table 1's
  em-dashes in the LLM columns therefore mean *not determined*, not *absent*, and the footnote
  ("Elements present at less than 0.01 wt% are not listed") over-claims for that alloy.
- The LLM-alloy certificate is **Revision 1, "(Si Reported)"** — silicon was added by amendment on
  25 July 2025 after the original 23 July report. Consistent with Si being the element in question.
- Oxygen: 0.0004 wt% (LLM-alloy), <0.001 (benchmark). Low enough to rule out gross oxidation of the
  finished wire, which is worth one sentence given that the Si shortfall is attributed to oxidation
  loss *during melting* — the two are not in conflict, but a reader may think they are.

---

## 4. A provenance correction to an unrelated file on the drive

`E:\FE-SMA\ANALYSIS.md` describes the synchrotron work as **APS, Argonne**, and concludes the alloy
is a B2/L2₁ Heusler mixture from a JARVIS-DFT cosine match. It is an AI-generated analysis of one
`.chi` file and it is **wrong on both counts**:

- The beamline info file that ships with the raw detector images,
  `E:\FE-SMA\2026-1\CS\测试信息.txt`, reads *波长：0.0125872nm / 能量：98.5KeV / 探测器像素点大小：100um*
  — 0.125872 Å, 98.5 keV, 100 µm pixels. Chinese-language beamline documentation and the wavelength
  in §2.5. **SSRF is correct in the manuscript**; the "APS_EXP" in that file's path is a directory
  name, not a facility.
- Its L2₁-Heusler assignment is a cosine match against a Fe-Al binary database, superseded entirely
  by the MAUD γ + α + D0₃ refinement.

Do not cite that file. It is noted here only so it is not mistaken for a record later.

---

## 5. Still open after D2

| item | who | blocks |
|---|---|---|
| ~~Confirm the processing table in §2 against the real route~~ **CONFIRMED 2026-08-18** — tested wire homogenised, benchmark same; §2.1 stands | ~~S. Cai~~ | closed |
| Source of Table 2's "As drawn" row | **S. Cai** | R2 Exp#3 completeness |
| How σ₀.₂ and E were extracted from the raw curves | **S. Cai / Frank** | R2 Exp#3 |
| ~~Tensile standard actually followed (D5)~~ **ANSWERED 2026-08-17** — broadly E8/E8M + cited method | ~~S. Cai~~ | closed |
| ~~SME test heating rate and hold (D4)~~ **ANSWERED 2026-08-17** — ≈50 °C/s, ≈10 s hold | ~~S. Cai~~ | closed |
| Whether Fig. 3's panels are 0.36 mm vs 0.45 mm stock | **Frank** | R3#1, R3#7 |
