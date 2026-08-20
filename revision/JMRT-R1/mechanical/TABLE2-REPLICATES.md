# Table 2 becomes n = 3 — the 2026-08-20 replicate run

**Source:** `table2-n3-source-2026-08-20.docx` in this folder, a byte copy of the file
F. Cai supplied on 2026-08-20 (`C:\Users\frank\Downloads\table 2-1.docx`). Its caption
reads: *"Mechanical properties of AI alloy after heat treatment for 1 minute at different
temperatures. 3 samples were tested for each heat treatment conditions."*

**What happened.** R2 Experimental #3 asked for statistical repeatability. Until now the
answer was a concession: Table 2 was n = 1, §2.4 said so, and the R2 letter argued that
single measurements were adequate for the paper's purpose (see
`../processing/PROCESSING-AND-REPLICATES.md` §1, which remains the record of the
as-submitted state). F. Cai ran the extra heat treatments and tensile tests on
2026-08-20, so every anneal condition is now replicated and the concession is withdrawn.

## The new values (mean ± SD, n = 3) against the as-submitted single measurements

| Condition | σ₀.₂ n=1 | σ₀.₂ n=3 | UTS n=1 | UTS n=3 | Elong. n=1 | Elong. n=3 | E n=1 | E n=3 |
|---|---|---|---|---|---|---|---|---|
| As drawn | 1528 | 1587.9 ± 63.7 | 1925 | 1936.6 ± 19.2 | 2.0 | 2.0 ± 0.1 | 143.7 | 138.5 ± 5.1 |
| 600 °C | 1948 | 1908.0 ± 29.2 | 2293 | 2254.3 ± 27.3 | 2.3 | 2.2 ± 0.1 | 157.4 | 155.7 ± 2.2 |
| 700 °C | 1683 | 1635.3 ± 35.9 | 2009 | 1876.0 ± 9.4 | 2.2 | 2.2 ± 0.0 | 164.8 | 156.1 ± 2.0 |
| 800 °C | 1167 | 1151.1 ± 11.3 | 1216 | 1208.6 ± 5.2 | 24.0 | 26.1 ± 1.7 | 155.5 | 151.4 ± 2.9 |
| 900 °C | 944 | 936.3 ± 5.5 | 1078 | 1081.5 ± 2.5 | 29.7 | 30.6 ± 0.6 | 152.2 | 153.1 ± 1.4 |
| 1000 °C | 673 | 674.8 ± 1.5 | 967 | 977.8 ± 7.7 | 33.4 | 33.0 ± 0.3 | 155.6 | 156.0 ± 2.0 |
| 1100 °C | 556 | 570.6 ± 10.3 | 947 | 970.3 ± 16.5 | 29.7 | 29.1 ± 0.6 | 156.8 | 161.9 ± 3.6 |
| 1200 °C | 502 | 518.7 ± 11.8 | 938 | 968.3 ± 21.4 | 23.9 | 25.6 ± 1.2 | 163.0 | 161.2 ± 5.5 |

Every trend the paper reads off Table 2 survives: σ₀.₂ and UTS still fall monotonically
from 800 to 1200 °C, elongation still peaks at 1000 °C, the 800 °C recrystallization
discontinuity is if anything sharper (elongation 2.2 → 26.1 % rather than 2.2 → 24.0 %),
and no ranking of conditions changes. Ranges: σ₀.₂ 518.7–1908.0 MPa (3.68×), elongation
2.0–33.0 % (16.5×). Largest relative SD in the table: 6.5 % (elongation at 800 °C); in the
strength columns, 4.0 % (as-drawn σ₀.₂).

## Structure of the scatter — and one cell that does not fit it

Computing `|old single value − new mean| / (new ±)` for all 32 cells gives a striking
result: **30 of them land between 1.33 and 1.50, clustered on 1.40–1.42**, which is √2 to
within the rounding of the table.

That is not a coincidence, and it has a simple mechanical reading. If two of the three
specimens agree closely with each other and the third — the original 2025 specimen — sits
off to one side, then for three values `{x, y, y}` the ratio `|x − mean| / σ_pop` is
**exactly √2**, whatever the magnitudes. So the table is consistent with: the two new
2026-08-20 specimens reproducing each other tightly, the 2025 specimen offset from them,
and the reported ± being a population standard deviation (Excel `STDEVP`, not `STDEV`).
The corollary is that √2 is the ceiling for that ratio, so a value above it cannot be a
member of its own triplet.

**Two cells break the pattern, both at 700 °C:**

| cell | old | new | ratio | note |
|---|---|---|---|---|
| 700 °C UTS | 2009 | 1876.0 ± 9.4 | **14.15** | fits at 1.415 if the ± is **94**, not 9.4 |
| 700 °C E | 164.8 | 156.1 ± 2.0 | **4.35** | fits at 1.41 only if the ± were ≈6.2 |

The source file prints the 700 °C UTS uncertainty as `1876.0±94` — the only cell without
a decimal place. It was read as a dropped decimal point and F. Cai confirmed **9.4** on
2026-08-20, which is what the manuscript currently carries. The ratio analysis above
points the other way: **±94 is the value that matches the internal structure of every
other cell in the table**, and ±9.4 is the one number in 32 that is off by an order of
magnitude. This is flagged rather than silently changed — it is a one-cell edit either
way, and it is F. Cai's data. The 700 °C modulus is anomalous under either reading and is
worth a look at the same time.

## Fig. 2 is not rebuilt

F. Cai confirmed that the specimen already plotted in each Fig. 2 panel is one of the
three now averaged, so the curves stand and only the caption changed ("Each panel shows
one representative specimen of the three tested per condition; the values in Table 2 are
means over all three"). Note that the ratio analysis above is consistent with that for 30
of 32 cells and inconsistent with it for the two 700 °C cells named — i.e. if the 700 °C
UTS really is ± 9.4, then the specimen plotted in **Fig. 2b** is not one of the three
averaged in that row.

## What is *not* in the repository

The raw Instron exports for the 2026-08-20 replicate run are not on this machine — only
the summary table above. The as-submitted single measurements are traceable to
`Fe-SMA-FC.is_tcyclic` (9/8/2025) spools 3–9 on `E:\FE-SMA\`, documented in
`../processing/PROCESSING-AND-REPLICATES.md` §1; the new run has no equivalent trace here
yet. If a reviewer asks for the underlying curves, they have to come from S. Cai's or
F. Cai's records.

Two open points from the as-submitted record are unaffected and still open: the σ₀.₂ and
E columns are derived from the raw curves rather than printed by the Instron report (the
offset strain measure and modulus fit range are still undocumented), and the "As drawn"
row has never been located in the eight original reports.
