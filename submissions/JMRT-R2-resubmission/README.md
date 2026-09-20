# JMRT-D-26-06169R1 — Round-2 resubmission package

**Journal:** Journal of Materials Research and Technology
**Decision being answered:** major revision on Revision 1 (R1 "no comment", R2 "accept",
R3 eight points), **due 2026-09-22**
**Package assembled:** 2026-09-20. Manuscript pair built the same day against the
Revision-1 clean file the reviewers read (**547 tracked revisions**: 288 insertions,
258 deletions, 1 formatting).

> **Two items are outstanding and are declared as such** in the cover letter and in the
> Reviewer-3 response (points 7 and 8): the loading–unloading–heating test on the
> quartz-tube-cycled 0.36 mm wire, and DSC for Ms. Both have been put to S. Cai
> (Gmail draft, Frank sends). The manuscript no longer relies on either. If either lands
> before upload, add it as a bound in the terms given in the R3 response and rebuild.
>
> **Before upload, Frank:** (1) read the R3 response and the cover letter; (2) send the
> Song email and fold in his answers to the four record questions (40-min rod heat,
> AGG schedules per specimen, the 1300 °C / oct-11-25 spool identities, the Fig. 8
> specimen) — the manuscript is written from the drive record and each of those is
> stated as the record holds it; (3) ~~confirm the replicate gauge~~ — confirmed 127 mm by
> Frank, 2026-09-20; (4) upload (Frank: submitting 2026-09-20).

## What is here

| File | Upload as | Notes |
|---|---|---|
| `Cai_Fe-SMA_JMRT_R2_marked-up.docx` | **Revised Manuscript (Marked-up)** | 547 tracked revisions against the R1 clean file (`revision/JMRT-R1/R1-manuscript/Cai_Fe-SMA_JMRT_R1_clean.docx`). |
| `Cai_Fe-SMA_JMRT_R2_clean.docx` | **Revised Manuscript (Clean)** | All revisions accepted. 10 images, 4 tables, 38-entry bibliography. |
| `figures/Figure_1.jpg` … `Figure_10.png` (10 files) | **Figure**, one per item, in order | Each byte-identical (SHA-256) to the image embedded in the clean DOCX (checked at packaging). **Fig. 10 is new** (`figures/build_fig10_cyclic_records.py`, from the raw exports in `revision/JMRT-R2/mechanical/raw-exports/`). |
| `figures/Table_1.docx` … `Table_4.docx` | **Table**, only if the portal asks for tables separately | All four are inline in the manuscript DOCX. **Table 4 is new** (solid-state α field and solidus per database); Table 2's caption now names the gauge. |
| `Cai_Fe-SMA_JMRT_R2_response-reviewer-{1,2,3}.docx` | **Response to Reviewers**, one per reviewer | Built by plain pandoc from `response-to-reviewer-{1,2,3}.md` (sources: `revision/JMRT-R2/response-R3.md`, `response-R1-R2.md`). R3's eight points quoted verbatim; R1/R2 are short notes. |
| `CoverLetter.docx` / `.md` | **Cover Letter** | Owns the two corrections (liquid phase; 40-min record attribution) and declares the two outstanding measurements with an extension request for those items only. |
| `Highlights.docx` | **Highlights** | One word changed ("tested state" → "condition reported"). |
| `Supplementary-Material_LLM-design-report.pdf` | **Supplementary Material** | Unchanged from R1. |

Working copies of the pair, the R3 response and the cover letter were also copied to
`C:\Users\frank\Downloads\` (2026-09-20).

## How to rebuild

From the repository root (pandoc concatenates; never pre-concatenate with PowerShell):

```bash
pandoc front_JMRT.md manuscript.md --citeproc --bibliography=references.bib \
  --csl=elsevier-with-titles.csl --resource-path=. \
  --reference-doc=revision/JMRT-R1/as-submitted/Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx \
  -o revision/JMRT-R2/R2-manuscript/revised_styled.docx
python revision/JMRT-R2/R2-manuscript/build_docx_pair.py revision/JMRT-R2/R2-manuscript/revised_styled.docx
```

Word must have no documents open. Verify afterwards: **10 images, 4 tables, 0 `[@`,
non-zero α/γ, 0 `Â`**, and the phrase checks in `revision/JMRT-R2/CHANGES-R1-TO-R2.md`.
The Round-2 text edits themselves are the checked list in
`revision/JMRT-R2/apply_r2_edits.py` (already applied; re-running it will fail on purpose
because the old strings are gone).
