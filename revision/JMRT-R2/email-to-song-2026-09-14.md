# Draft email to S. Cai — 2026-09-14 (Frank sends; not sent by Claude)

**To:** song_cai@fwmetals.com — address taken from `archive-2026-06-pre-MD-revision/manuscript_SCai_style.md`
(June 2026); confirm before sending. A copy of this text is in Frank's Gmail drafts.
**Subject:** Fe-SMA JMRT revision — 3 questions on the record + 3 tests (due Sept 22)

---

Hi Song,

JMRT sent the Fe-SMA paper back as a major revision, due September 22. Reviewers 1 and 2 are done (R2 recommends acceptance). Reviewer 3 has eight points. Most of them are writing, but a few need things only you have. Three questions on the record first, then the tests.

1. Which heat is the 40-minute rod record? The Instron report "697-7-SMA-constant.is_tcyclic-697-7.pdf" (0.040 in rod, 5 in gauge) carries the 1200 °C/1 min, 1200 °C + 200 °C/3 h, and 1200 °C/40 min + 200 °C/3 h rows that §3.5 reports as the LLM-alloy going from 11.0 % to 1.4 % elongation. The file is tagged 697-7, and row 9 is "1200 C 2FPM – HYDROGEN ATM". Is that report the LLM-alloy (697-6) or the benchmark (697-7)? If it is the benchmark, I will withdraw the 40-minute paragraph.

2. The AGG route as actually run, per specimen. R3 asks whether "1200 °C, water quench, reheat to 900 °C" was the real route and how it compares with Omori's continuous-cooling cycle. Your notes show two schedules: rod — 1200 °C/30 min WQ, 900 °C/15 min, repeated 2 or 3 times, final 1200 °C/30 or 60 min WQ; and the 10/11/25 quartz-tube run on the 0.36 mm wire (the Fig. 1d specimen) — 1200 °C/30 min in Ar, out to the cold zone for 10 min, four times, water quench, with no 900 °C step. Is that right? Which specimens got which schedule, and was the benchmark 0.64 mm wire cycled the same way?

3. The Fig. 3 Instron record. R3 flags that Fig. 3 still shows the original curves while the gauge length in the text changed from 13 mm to 127 mm. None of the eight Instron reports I have contains the loading–unloading–heating test. Can you send that record, or tell me the gauge length, wire diameter and test date for both panels (LLM-alloy and benchmark)?

Tests R3 asks for:

a) Needed: one 0.36 mm LLM-alloy wire through the AGG schedule, then the 3 % loading–unloading–heating test, same as Fig. 3. R3 rejected the argument that the 1-min and 40-min conditions bracket the AGG condition and wants it tested directly. If it cannot be done by the 22nd, I will ask the editor for an extension on this one item and submit the rest.

b) If the 1200 °C/40 min mount still exists: an SEM-BSE point count of α vs γ (R3 wants phase fractions for Fig. 1a vs 1c). If it does not exist, I will say so.

c) Optional: DSC on the 1200 °C/1 min LLM-alloy wire, −150 °C to 500 °C or higher, with a benchmark wire as the control. R3 wants Ms measured directly. I would report it as a bound whichever way it comes out.

One more thing you should know. I found a bug in our CALPHAD scripts: the liquid phase was silently dropped from two of the three databases, so the 1340 °C and 1390 °C solvus values in §3.4 were computed for an alloy that could not melt. With liquid included, the alloy starts melting at about 1295 °C while γ is still present, so there is no single-phase α field in the solid state in any of the three databases; the carbon-free variant is single-phase α from about 1150 °C up to its solidus. The conclusion gets cleaner, but every quoted temperature changes, and I am redoing Fig. 9 and Table 3 now. R3 also recommended high-temperature DTA; I am declining that with reasoning, since the argument no longer rests on a solidus number.

Thanks,
Frank
