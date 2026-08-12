# Which specimen is in which AGG micrograph — closes D7

**Written 2026-08-12, with the E: drive mounted.** This settles blocker **D7** and, in doing so,
corrects the archived Fig. 2 panel set. Every identification below is by md5 against the file on
the drive; every size is measured from the panel's own burned-in scale bar.

Companion documents: `PROCESSING-AND-REPLICATES.md` (heat identity, replicate counts, the two
processing routes) and `../comment-triage.md` §A3 (the reviewer comments this answers).

---

## 1. The archived panels, matched by hash

`figures/archive-2026-06-pre-MD-revision/` against
`E:\FE-SMA\697-6-7 Fe-Mn-Al-Ni-Si\micorstructure\`. All four are exact matches, so the archive is
not a re-render or a crop of anything — it is the microscope output.

| Archived panel | md5 | Source file on E: |
|---|---|---|
| `Fig2a_AI_1200C_1min_microstructure.jpg` | `f57642ad…` | `Fe-SMA-FC-1200C4FPM F72.jpg` |
| `Fig2b_AI_3cycle_AGG_microstructure.jpg` | `8b2d9e63…` | `Fe-SMA-3 CYCLE AGG.jpg` |
| `Fig2c_Omori_3cycle_AGG_bamboo.jpg` | `0e40c85c…` | `697-7\3 cycle AGG heat treated in Argon\FeMnAlNi-AGG-2.jpg` |
| `Fig2d_Omori_1200C_1min_acicular.jpg` | `bcf48d27…` | `697-7\697-7-1200c4fpm-3.jpg` |

Two conventions on the drive, both confirmed against the chemistry certificates and the Instron
report filenames in `PROCESSING-AND-REPLICATES.md`:

- **`Fe-SMA-FC…`, `FeMnAlNiSiC…`, `697-6…` = RD0697-6, the LLM-alloy.** `Fe-SMA-FC.is_tcyclic-697-6.pdf`
  ties the "FC" prefix to heat 697-6 directly.
- **`FeMnAlNi…` (no Si, no C), `697-7…` = RD0697-7, the benchmark.**

`Fig2a` is additionally the **1200 °C / 4 fpm F72** strand-anneal condition, not a static "1 min"
hold — the filename says so. That confirms the open item in `tasks/todo.md` about stating the
anneal precisely in §2.

---

## 2. Measured specimen sizes, and the problem they expose

Method: the blue rule in the bottom-right overlay is located by colour within that panel only
(searching the whole frame picks up colour-etched grains), its pixel length is converted using the
label read off the overlay, and the specimen band is measured perpendicular to its principal axis
so that a diagonally mounted wire is not measured along its projection. Script:
`scratchpad/measure_agg.py`.

| Panel | Alloy | Bar | Measured band | Stock it matches |
|---|---|---|---|---|
| `Fig2c` / new (a) `FeMnAlNi-AGG-2.jpg` | benchmark | 200 µm | **≈570–630 µm** | 0.0253 in = **0.64 mm** final benchmark wire ✔ |
| new (b) `FeMnAlNiSiC-3 cycle AGG ht.jpg` | LLM | 200 µm | **330 µm** | 0.0142 in = **0.36 mm** final LLM wire ✔ |
| `Fig2b` / new (c) `Fe-SMA-3 CYCLE AGG.jpg` | LLM | 400 µm | **868 µm** | **not the 0.36 mm wire** — see below |

### The finding

**`Fig2b`, the panel the manuscript has been calling the LLM-alloy after AGG, is not the 0.36 mm
wire.** A longitudinal section cannot be wider than the wire it was cut from, and 868 µm is 2.4×
0.36 mm. The panel is rod stock.

Which rod is an inference, not a hash match, and is labelled as such. The only AGG-treated LLM
stock in the processing record above wire gauge is the 0.0508 in (1.29 mm) rod of the 8/31/25
trial, and the only 3-cycle AGG *mechanical* specimen recorded for heat 697-6 is spool 2 of
`Frankie-Fe-SMA-6mm gauge lenght testing.is_tcyclic-697-6.pdf`, labelled `3CYCLE agg+200c3hr` at
**0.0418 in = 1.06 mm**. An off-axis longitudinal section through a 1.06 mm rod gives an 868 µm
chord at 0.30 mm from the axis, which is an ordinary amount of polish-down. **1.06 mm rod is the
best supported reading; 1.29 mm rod is the alternative; 0.36 mm wire is excluded.**

The same 1.06 mm scale appears in `3cycle AGG-200C-CRACK along boundary.tif`, whose wire measures
≈1.08 mm against its own 250 µm bar — the same specimen class, imaged in stereo.

### Consequence for the paper

The published Fig. 2 pair was **never like-for-like**: it set an LLM-alloy rod beside a benchmark
wire and read the difference as a difference between alloys. The correct 0.36 mm panel existed on
the drive the whole time and was not used.

This is not a retraction of the conclusion. The correct panel shows *less* coarsening than the
rod does, so the claim that the LLM-alloy does not develop a bamboo structure is strengthened, not
weakened. But the comparison as drawn could not have supported it, and the revision must present
the sizes rather than leave them implicit.

---

## 3. D7, answered

> **D7 — Frank confirms the AGG micrograph reading.** Frank's instruction (2026-08-12) is to agree
> with the reviewers. The evidence supports that without qualification.

R1#4 and R3#4 are right on both counts, and the record is stronger than the reviewers could have
known from the submitted paper:

1. **AGG is a second, independent failure mode**, not a footnote. After the identical three-cycle
   1200 °C route the benchmark bamboos completely — new panel (a), grains spanning the full 0.64 mm
   section with boundaries running straight across — and the LLM-alloy at 0.36 mm does not coarsen
   at all: new panel (b) is a fine, banded, heavily elongated duplex structure across the whole
   330 µm width, with no grain approaching the section width.

2. **The mechanism is boundary pinning by the second phase**, which is exactly what the
   CALPHAD result predicts. Panel (c), the rod, is the informative one: coarsening *did* start
   there, producing grains that locally span the section, and it is arrested along a continuous
   band of fine equiaxed grains that was never consumed. A duplex α + γ alloy at its solution
   temperature has a second phase available to pin boundaries; the benchmark, single-phase α at
   1200 °C, does not.

3. **The AGG condition is also mechanically damaged.** From `PROCESSING-AND-REPLICATES.md`: the
   LLM-alloy 2-cycle AGG rod gives 568 and 608 MPa at 1.0 % elongation (n = 2), and the quartz-tube
   AGG sets run 85–155 MPa at 24.8–49.3 % CoV with elongations of 0.4–2.6 %. Panel (d) shows why —
   cracks along boundaries on the wire surface after AGG + 200 °C/3 h. A 2.69× spread about an
   85 MPa mean is a material that is cracking, not a test that is imprecise.

---

## 4. What is deliberately still open

- **The archived cyclic panels `Fig3b/c/d` are not published in this pass.** `Fig3b`
  (`Fig3b_AI_3cycle_AGG_cyclic.png`, ≈460 MPa yield, ≈810 MPa peak, fracture at 9.2 %) does not
  match any row of the eight Instron reports on the drive: the closest 697-6 AGG entries are
  1.293 mm/568 MPa/1.0 %, 1.293 mm/608 MPa/1.0 %, and 1.062 mm/1006 MPa/11.9 %. Its specimen is
  therefore unidentified, and it would be inconsistent to publish it in the same revision that
  corrects `Fig2b` for exactly this reason. The AGG mechanical result goes into §3.5 as numbers
  from the reports, which are traceable.
- **Which furnace run produced panel (a).** The drive holds two benchmark 3-cycle AGG folders,
  `3 cycle AGG heat treated in Argon` and `3 cycle AGG in QUARTZ TUBE`; the 10/11/25 note describes
  a quartz-tube run under argon, so the folder names do not separate them. Both are three-cycle
  1200 °C argon treatments, which is all the caption claims. The quartz-tube images are under-etched
  and were not usable regardless.
- **Panel (c)'s rod diameter**, per §2 above — 1.06 mm against 1.29 mm. The caption says "rod stock,
  ≈1 mm" rather than picking one.

## 5. Why bamboo is not a target for this alloy (added 2026-08-12)

Source: S. Cai, 2026-08-12, and `instron-reports-extracted.txt`
(`Frank-SMA-constant.is_tcyclic`, 2025-09-22, ≈1 mm rod, 0.03998 in).

| Spool row | Condition | Elong. [%] |
|-----------|-----------|-----------|
| 8  | 1200 °C / 1 min, no age      | 9.1  |
| 11 | 1200 °C / 1 min, + 200 °C/3 h | 11.0 |
| 12 | 1200 °C / 40 min, + 200 °C/3 h | **1.4** |

Rows 11 and 12 differ only in anneal time: same diameter, same age. Elongation falls
by a factor of eight. The 40-minute microstructure is Fig. 1c (grains > 100 µm).

The 2-cycle AGG rod specimens (568 and 608 MPa at 1.0 % elongation, Sec. 3.5) are the
same effect reached by a different route.

Consequence: coarsening embrittles this alloy well before bamboo dimensions (a grain
spanning the full 360 µm section) are approached. The AGG treatment was run because the
benchmark comparison required it, not because bamboo was a goal for the LLM-alloy. What
AGG produced was growth of the duplex structure — both constituents coarsening together,
still interlocked. Sec. 3.5 and Sec. 4.2 now say this; earlier drafts wrote the absent
bamboo as a second failure, which it is not.

Caveat to carry: rows 8/11/12 are ≈1 mm rod. Table 2 is 0.36 mm wire and gives 23.9 % at
1200 °C / 1 min. The 11.0 → 1.4 comparison is internally valid (constant diameter and age)
but is not a wire result, and Sec. 3.5 states the diameter for that reason.

## 6. Why no AGG-condition cyclic stress–strain will be run (2026-08-12)

Decision: S. Cai / F. Cai, 2026-08-12. **Not doing it.**

Grounds — a bracketing argument, not unavailability:

- In grain size the AGG condition lies **above the 1 min anneal and below the 40 min anneal**
  at 1200 °C. Both bounds are already characterised mechanically (§3.5 table above).
- Neither bound shows any transformation. Every unloading segment in Fig. 2 is straight and
  parallel to the elastic loading line; recovery never exceeds σ/E.
- A curve bracketed by two curves that each show no transformation cannot show one. It can
  differ only in strength and ductility, and the sign of both is fixed by the 11.0 % → 1.4 %
  elongation loss between the bounds.
- Independently: specimens fracturing at ~1 % elongation cannot be cycled meaningfully, and a
  loop measured on a cracked specimen (Fig. 8d) is not interpretable as transformation.

**Caveat — this bracket is judgement, not measurement.** No grain-size measurement of the AGG
condition against the 1 min and 40 min conditions exists in the record. It is also
geometry-dependent: Fig. 8b (0.36 mm wire) sits near the 1 min end, Fig. 8c (≈1 mm rod) nearer
the 40 min end. Measuring all three from micrographs already in hand is roughly an hour's work
and would convert the strongest paragraph of the R3#4 reply from judgement to data. Recommended
before submission. Stated in §3.5 and in `response-AGG.md`.
