# Independent re-analysis of the SSRF patterns

Run 2026-08-05 from the raw integrated data on `E:\FE-SMA\synchrotron.chi` (8 patterns).
Scripts `index_patterns.py`, `plot_superlattice.py`; output `index_results.txt`,
`superlattice_window.png`.

Sample identities from `E:\FE-SMA\2026-1\sample list.txt` and the column headers of
`E:\FE-SMA\2026-1\CS\spectra.xlsx`:

| | alloy | condition |
|---|---|---|
| Sam1 | **697-6 = LLM-alloy** | 3-cycle AGG, 1200 °C/1 h WQ |
| Sam5 / Sam6 | 697-6 = LLM-alloy | 1200 °C / 4 fpm F72, 0 % / 10 % strain |
| Sam7 / Sam8 | **697-7 = benchmark** | 1200 °C / 4 fpm F72, 0 % / 8 % strain |

The manuscript's "1200 °C for 1 minute" is the 1200 °C / 4 fpm F72 continuous anneal —
worth stating precisely in §2, since 4 fpm through a 72-inch hot zone is ≈1.5 min.

---

## 1. The manuscript's phase identification is CORRECT, and now it is quantified

This is the important result, and it reverses a concern raised from the CALPHAD run alone.

The low-angle window at 2θ = 2.1–2.5° is diagnostic because **a bcc + fcc mixture puts no
intensity there whatsoever**. Only an ordered phase can produce a peak. Two positions
matter:

- **2θ = 2.155°, d = 3.347 Å — D0₃ (111).** Unique to D0₃. B2 cannot produce it.
- **2θ = 2.489°, d = 2.898 Å — B2 (100) = D0₃ (200).** Shared by both.

Measured peak height as a percentage of the strongest reflection:

| pattern | D0₃ (111) @ 2.155° | B2 (100) / D0₃ (200) @ 2.489° |
|---|---|---|
| Sam1 (LLM, AGG) | **0.93 %** | 0.95 % |
| Sam1 repeat | **1.03 %** | 1.00 % |
| Sam5 (LLM, 4 fpm) | **0.82 %** | 1.06 % |
| Sam6 (LLM, 10 % strain) | 0.49 % | 0.51 % |
| Sam7 (benchmark) | 0.29 % *(baseline)* | **3.85 %** |
| Sam7 repeat | 0.20 % *(baseline)* | **7.18 %** |
| Sam8 (benchmark, 8 % strain) | 0.08 % *(baseline)* | 0.54 % |

Read the pattern:

- **The benchmark shows superlattice intensity at 2.489° only, and nothing at 2.155°.**
  That is the signature of **B2** — exactly the coherent β-NiAl the manuscript says the
  benchmark relies on.
- **The LLM-alloy shows superlattice intensity at *both* positions, in roughly equal
  measure, reproducibly across three independent patterns.** D0₃ produces both; B2 cannot
  produce the first. That is the signature of **D0₃**.

So the manuscript's central structural claim — *the benchmark forms B2, the LLM-alloy forms
D0₃ instead* — is supported by the raw diffraction data, independently of the refinement.
The intensities are small (≈1 %) but they sit on a flat 0.2 % baseline, they are reproducible
across exposures, and they are alloy-specific in the correct direction.

### What this gives the response letter

R3#8 said absence of a B2 peak does not prove absence of B2. Correct — and now answerable
with numbers rather than a concession:

> B2 (100) reaches 3.9–7.2 % of the strongest reflection in the benchmark and does not rise
> above 1.1 % in the LLM-alloy, against a baseline of 0.2 %. Whatever B2 exists in the
> LLM-alloy is therefore at least 4–7× less abundant, and the ~1 % intensity that is present
> at that position is fully accounted for by D0₃ (200), since D0₃ (111) — which B2 cannot
> produce — appears at the same strength in the same patterns.

## 2. Every reflection indexes to bcc + fcc. There is no unindexed phase.

With bcc a = 2.89816 Å and fcc a = 3.64862 Å (the MAUD values), all peaks in all eight
patterns index within 1 %, out to fcc (420) and bcc (321). No third *majority* phase exists.

A useful crystallographic check: those two cells give **12.17 Å³/atom (bcc) and 12.14 Å³/atom
(fcc)** — matching to 0.2 %. Two chemically distinct equilibrium phases would not generally
agree that closely. A near-volume-invariant pair is what a **displacive (martensitic)**
relationship looks like. See §4.

## 3. ⚠️ The 62 / 34 / 4 numbers cannot be reproduced from anything on E:

Searched the whole drive: no MAUD `.par`, no GSAS, no refinement project of any kind. The
only refinement artifact is `697-6-7 Fe-Mn-Al-Ni-Si/X-ray fitting.jpg` (2025-11-26), which
shows a MAUD fit containing **exactly two phases** — bcc a = 2.89816, fcc a = 3.64862, **no
D0₃** — and reports **70.3 % fcc** for run #30573 (from the earlier Nov-2025 beamtime,
`D:\APS_EXP\2025-11\SAMPLE 9\30573.tif`).

So the published numbers come from a refinement that is not on this drive. Three separate
figures are in play and none of them agree:

| source | fcc | bcc | D0₃ |
|---|---|---|---|
| manuscript §3.3 | ≈62 % | ≈34 % | ≈4 % |
| manuscript §4.1 | ≈62 % | ≈**37** % | — |
| `X-ray fitting.jpg` MAUD fit | **70.3 %** | — | *phase not in the model* |

**Action:** find the refinement that produced 62/34/4 — most likely on a co-author's machine
(J. Yan at SSRF, or S. Cai). Until it is in hand, the most-cited quantitative claim in the
paper is not reproducible, and a reviewer asking for the fit statistics cannot be answered.
Note that adding a ~4 % D0₃ phase to a two-phase model is exactly the kind of change that
would move fcc from 70.3 % toward 62 %, so the two results are plausibly the same data
refined twice — but that has to be shown, not assumed.

## 4. The phase fractions are texture-limited — and the CALPHAD tension is real

Sam1-NO7325 and Sam1-NO7328 are **the same specimen, two exposures**. Their fcc(111)/bcc(110)
intensity ratios are 0.52 and 1.24 — a factor of 2.4 apart. These are drawn wires with strong
fibre texture, and single-pattern intensities are dominated by which grains happen to satisfy
the Bragg condition. The manuscript's 72-spectrum azimuthal average (§2.5) is the right
treatment; this just shows why the refinement file matters so much.

That said, the qualitative picture is unambiguous and consistent across every pattern:

- **benchmark** — bcc-dominant: fcc(111) is only 23–34 % of bcc(110)
- **LLM-alloy** — fcc-rich: fcc(111) is 100–124 % of bcc(110)

So the LLM-alloy really is fcc-rich at room temperature. **This eliminates the
"transposed fractions" hypothesis** raised from the CALPHAD run — the raw data agrees with
the manuscript on which phase dominates.

Which leaves the other explanation, now the leading one:

> CALPHAD puts the LLM-alloy at **62–71 % bcc at 1200 °C** in all three databases. The
> measurement, on material quenched from 1200 °C, is fcc-rich. In this system **γ-fcc is the
> martensite product**. The natural reading is that a substantial fraction of the α present
> at temperature transformed to γ *during the quench* — i.e. **M_s lies above room
> temperature**.

If that holds it is a better explanation for the absence of superelasticity than the one
currently in the manuscript: the transformation has already run to completion before the
specimen is ever loaded, so there is nothing left to induce. It also follows directly from
carbon raising γ-stability, which ties the whole paper together.

Supporting, not yet conclusive: the 0.2 % atomic-volume match (§2); the fcc(200)/fcc(111)
ratio varying strongly between exposures, as expected for variant-selected martensite; and
the manuscript's own observation that the AGG-treated material gives a similar pattern.

**Cheapest decisive test: a DSC scan for M_s.** Second cheapest: look for martensite
morphology in the existing micrographs of the 1200 °C/4 fpm material
(`Fe-SMA-FC-1200C4FPM F72.jpg`, already on E:).

⚠️ Note this also undercuts the §3.3 sentence "the AI alloy after AGG heat treatment showed
a similar pattern, indicating that the multi-phase microstructure is a stable state of this
alloy at 1200 °C." If both specimens were quenched, both would transform the same way on
cooling, so the similarity says nothing about the state *at* 1200 °C. Soften it.

## 5. Corrections to the CALPHAD write-up

- The claim that **D0₃ is not supported** was wrong, and is withdrawn. Diffraction shows it.
  What survives is narrower and still worth stating: D0₃ is not an *equilibrium* phase at
  this composition, so it forms as a metastable ordering product on cooling. Also note the
  only database that models D0₃ (PrecHiMn-04) **contains no Ni**, and Ni strongly conditions
  B2/D0₃ ordering in Fe-Al — so that calculation was never a strong test to begin with.
- The **"transposed fractions"** hypothesis is withdrawn (§4 above).
- The **quench-martensite** hypothesis is strengthened and is now the leading explanation.

## 6. What the 62/34/4 refinement should look like (Fig. 5)

### The crystallography that governs the figure

Fig. 5 labels three phases. Their reflections are **not independent**:

| | cell | reflections |
|---|---|---|
| FCC(γ) | a = 3.64862 Å | {111} 3.424°, {200} 3.954°, {220} 5.593° |
| BCC(α) | a = 2.89816 Å | {110} 3.520°, {200} 4.981°, {211} 6.104° |
| Fe₃Al D0₃ | a = 5.79632 Å = **2 × a_bcc** | {111} 2.155°, {200} 2.489°, {220} 3.520°, {311} 4.128°, {400} 4.981°, {331} 5.425°, {422} 6.104° |

Because the D0₃ cell is exactly the bcc cell doubled:

> **D0₃{220} ≡ BCC{110}, D0₃{400} ≡ BCC{200}, D0₃{422} ≡ BCC{211}** — identical positions.

You can see this in the submitted figure: the BCC and Fe₃Al tick labels sit at the same
2θ for those three. Which means:

**The entire 34 % α / 4 % D0₃ split is determined by two weak superlattice peaks —
D0₃{111} at 2.155° and D0₃{200} at 2.489° — and nothing else.** Everything at higher angle
is shared and carries no information about the α/D0₃ partition.

### The problem with the figure as submitted

Measured heights of those two peaks (this work, §1): **0.5–1.1 % of the strongest
reflection.** On Fig. 5's colour scale that region is uniform dark blue. **The figure labels
a phase whose entire evidence is invisible in it.** A reviewer checking Fig. 5 sees tick
marks over apparently empty space — which is the mirror image of R3#8's complaint about
claiming absence of B2.

### What it should show

1. **An inset or second panel over 2.0–2.7 °, intensity expanded ~50–100× (or log)**,
   with data and fit, so the D0₃{111} and {200} peaks are actually visible. This is the
   evidence for the third phase.
2. **The benchmark on the same axes.** This is the strongest structural argument in the
   paper and it is currently not made anywhere:

   | | D0₃{111} @ 2.155° (D0₃ only) | {200} @ 2.489° (B2 or D0₃) | {222} @ 4.311° |
   |---|---|---|---|
   | LLM-alloy (4 patterns) | **0.49–1.02 %, S/N 16–27** | 0.50–1.06 %, S/N 15–24 | absent |
   | benchmark, undeformed | 0.19–0.28 %, S/N 2.3–2.9 → **absent** | **3.83–7.17 %, S/N 54–112** | **0.55–0.61 %, S/N 8–15** |

   The benchmark has the B2-allowed reflections and **not** the D0₃-only one → B2.
   The LLM-alloy has the D0₃-only reflection at the same strength as {200} → D0₃.
   `superlattice_window.png` already plots this.
3. **Refinement statistics**: R_wp, R_p, GoF/χ², refined lattice parameters
   (a_bcc = 2.89816 Å, a_fcc = 3.64862 Å) and **ESDs on the phase fractions**. None are
   currently reported. Both R2 and R3 would reasonably ask.
4. **An honest uncertainty on the 4 %.** With the α/D0₃ split resting on peaks at ~1 % of
   maximum, the standard deviation on that 4 % is plausibly of the same order as the value.
   Say so — it costs nothing and pre-empts the obvious attack.
5. **A difference curve** (data − fit), which is standard for a Rietveld figure.

### Two discrepancies to resolve

- **Which specimen is Fig. 5?** The file you sent is named `Rietveld-sample 6.jpg`, and
  Sample 6 is the **10 %-strained** LLM-alloy. The caption says only "heat treated at
  1200 °C for 1 minute", and §3.3 uses the result as the *undeformed* phase constitution.
  If the refinement is on the deformed specimen, both the caption and the argument need
  fixing.
- **The version you sent is an earlier draft.** It has only two phase rows — FCC(γ) and
  Fe₃Al, **no BCC(α) row** — and it labels the 5.4 ° reflection `{311}`, repeating the
  label used at 4.1 °. The submitted Fig. 5 adds the BCC(α) row and correctly reads
  {400} {331} {422}. So the submitted figure is the better one; just make sure the draft
  does not get reused.
- Still unreconciled: §3.3 says 34 % α, §4.1 says 37 %, and the only surviving fit
  (`X-ray fitting.jpg`) is a **two-phase** model giving **70.3 % fcc** with no D0₃ at all.

## 7. Two housekeeping items found on the drive

- `E:\FE-SMA\ANALYSIS.md` and the DiffractGPT/JARVIS scripts are **exploratory work that
  should not be cited**. That file mis-assigns the fundamental bcc (110)/(200)/(211)
  reflections as evidence of B2 ordering, concludes "B2 dominant" from cosine pattern
  matching, gets its own 2θ → d conversions wrong (it labels 3.52° as fcc(111) when 3.52° is
  bcc(110)), and headers the data as "APS, Argonne" when `synchrfig.docx` and the manuscript
  both say **SSRF**. The raw `.tif` paths read `C:\APS_EXP\...`, which is presumably a local
  folder-naming convention — worth one line of confirmation, because a reviewer given the
  raw files would ask.
- `E:\FE-SMA\fe_sma_xrd_notes.txt` contains a **live AtomGPT API key in plaintext**, and the
  same file recommends pushing that directory to GitHub. Rotate it and remove it from the
  notes.
