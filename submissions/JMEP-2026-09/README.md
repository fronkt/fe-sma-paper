# JMEP submission package (2026-09-28)

Journal of Materials Engineering and Performance (Springer/ASM), ScholarOne:
https://mc.manuscriptcentral.com/jmep. Retargeted after the JMRT rejection of 2026-09-28.
Source: `front_JMEP.md` + `manuscript.md` (the JMRT round-2 text as submitted is archived at
`revision/JMRT-R2/manuscript-JMRT-R2-as-submitted-2026-09-21.md`).

| File | Upload as |
|---|---|
| `Cai_Fe-SMA_JMEP_manuscript.docx` | Main document: text, declarations, references, figure captions, tables (figures embedded after them for review) |
| `figures/Figure_1.tif` … `Figure_10.tif` | Figures, one per item |
| `ESM1_LLM-design-report.pdf` | Online Resource 1. JMEP lists .pdf as excluded; if ScholarOne refuses it, ask the editorial office |
| `ESM2-tables.docx` | Online Resource 2 (Tables S1 specimen/record register, S2 calculation register) |
| `CoverLetter.docx` | Cover letter |

Rebuild: `python submissions/JMEP-2026-09/build_jmep.py` from the repo root (uses the JMEP copies
`references-jmep.bib` and `jmep.csl` in this folder; checks 10 images, 4 tables, abstract < 200 words).
