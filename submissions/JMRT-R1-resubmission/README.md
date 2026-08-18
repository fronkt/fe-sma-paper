# JMRT-D-26-06169 — R1 resubmission package

**Journal:** Journal of Materials Research and Technology
**Decision being answered:** major revision, 45 comments (R1 × 9, R2 × 24, R3 × 12)
**Package assembled:** 2026-08-09 · **manuscript pair rebuilt 2026-08-18** (S. Cai merge,
Fig. 2 rebuild, figure renumbering to 10, affiliation fix; Engler & Randle texture
reference and AI-declaration trim on 08-16; S. Cai's 08-17 answers — SME heating
≈50 °C/s with ≈10 s hold, and the ASTM E8/E8M + method-citation sentence — into §2.4;
Figs. 4/6/8 rebuilt from raw SSRF data at 400 dpi on 08-18)

> ✅ **Uploadable content is complete and every co-author blocker is closed.**
> The manuscript pair and all three response letters are current, correct and
> placeholder-free; S. Cai signed off on the revision title and confirmed the
> §2.1 processing route on 2026-08-18. The only thing owed before upload is
> **Frank's read-through of the three response letters** (~30–45 min).

---

## What is here

| File | Upload as | Notes |
|---|---|---|
| `Cai_Fe-SMA_JMRT_R1_marked-up.docx` | **Revised Manuscript (Marked-up)** | 452 tracked revisions — 217 insertions, 195 deletions, 40 formatting — against the file actually submitted. Includes the renumbered bibliography (24 → 37) and the ten-figure set. |
| `Cai_Fe-SMA_JMRT_R1_clean.docx` | **Revised Manuscript (Clean)** | Identical content with all revisions accepted. |
| `Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx` | *do not upload* | The original submission, kept here so the pair can be diffed without leaving the folder. |
| `Cai_Fe-SMA_JMRT_R1_response-reviewer-{1,2,3}.docx` | **Response to Reviewers** (one per reviewer — the portal takes per-reviewer responses) | Drafted 2026-08-16 from `response-to-reviewer-{1,2,3}.md` (edit the .md, rebuild with pandoc). **Placeholders filled 2026-08-17 from S. Cai's email**: R1 comment 7 (≈50 °C/s to ≈200 °C, ≈10 s hold) and R2 Experimental comment 2 (broadly ASTM E8/E8M; cyclic protocol is a purpose-designed method cited to Cai et al., Shape Mem. Superelasticity 10 (2024) 460–472). The same facts are in manuscript §2.4 and the pair is rebuilt. Awaiting Frank's read-through only. Verbatim comments in `revision/JMRT-R1/reviewer-comments-verbatim.md`. |

Both revised files are byte-identical copies of
`revision/JMRT-R1/R1-manuscript/`, which is the build output directory. **Edit the source,
not these** — see *How to rebuild* below.

## Not yet in this folder

| Missing | Blocked on |
|---|---|
| ~~Response letters~~ — **complete 2026-08-17, see above** | Frank's read-through only |
| ~~Updated `highlights.md` and cover letter~~ — **done 2026-08-17**: `Highlights.docx` + `CoverLetter.docx` in this folder, worded for the revision | Frank's read-through |
| ~~Revision title sign-off~~ — **signed off 2026-08-18** by S. Cai ("Title is fine with me"), flag in `front_JMRT.md` updated | — |
| **Figures at production resolution** | **Figs. 4, 6, 8 FIXED 2026-08-18** — rebuilt from the raw SSRF detector frames and .chi integrations on E: at 400 dpi (`figures/build_fig4_6_8_from_ssrf.py`; pair rebuilt and re-synced). Only **Fig. 1** remains below the floor (~217 dpi at 140 mm) — needs S. Cai's higher-res micrograph originals; Figs. 5/7 are borderline-OK. Not submission-blocking |
| ~~Supplementary Material: the LLM report~~ — **staged 2026-08-17** as `Supplementary-Material_LLM-design-report.pdf` in this folder | Upload it with the package (item type: Supplementary Material) |
| ~~§2.1 melt-and-draw description~~ — **confirmed 2026-08-18** by S. Cai: tested wire was homogenized, benchmark underwent the same. §2.1 stands as written; the process note's other divergences were readings of a different trial and are overruled by the co-author who ran the processing (see `PROCESSING-AND-REPLICATES.md` §2 addendum) | — |

## Status of the revision

**As of 2026-08-18: all 45 comments answered and every co-author blocker closed.**
R1#7 and R2 Exp#2 were closed with S. Cai's 08-17 email (heating ≈50 °C/s, ≈10 s hold;
broadly E8/E8M with the cyclic method cited to his 2024 SMS paper). The gauge length stays
127 mm — the raw Instron exports print "Gage Length 5.00000 in" (= 127.0 mm exactly) and
S. Cai's own published method (SMS 10 (2024) 460) says 127 mm; "130 mm" is metric
rounding of the same 5-inch setting. On 08-18 S. Cai signed off on the revision title and
confirmed the §2.1 route (tested wire homogenized; benchmark the same), so §2.1 stands as
written and no rebuild was needed — the pair remains at 452 revisions. Still open: only
Frank's read-through of the letters, then upload.
Everything is enumerated in `tasks/todo.md`; every change is documented in
`revision/JMRT-R1/CHANGES-FROM-SUBMISSION.md` (§9 covers the 2026-08-14 S. Cai merge,
§11 the 2026-08-17 closure).

~~The 62 / 34 / 4 phase fractions are not yet quotable~~ — **superseded 2026-08-14:
Frank confirms the fractions were refined** (the "not refinable" reading came from the
single `.lst` file in the repo). The manuscript's quantitative wording stands; optionally
add the fractions to the abstract, which R2 Abstract#2 asked for. Keep the refinement
file at hand in case a reviewer requests fit statistics.

## How to rebuild these two files

Do not hand-edit the DOCX. The eleven new references renumber the whole bibliography,
which no find/replace gets right, and Word's `Find` cannot match across existing revision
markup so edits silently miss once tracked changes are present.

From the repository root (pandoc concatenates the two inputs itself — do **not**
pre-concatenate with PowerShell `Get-Content`, which reads UTF-8-without-BOM as ANSI and
mojibakes every α, γ and °; this happened on 2026-08-14 and produced a 621-"revision"
compare full of encoding diffs):

```bash
pandoc front_JMRT.md manuscript.md --citeproc \
  --bibliography=references.bib \
  --csl=elsevier-with-titles.csl \
  --reference-doc=revision/JMRT-R1/as-submitted/Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx \
  -o revised_styled.docx
python revision/JMRT-R1/R1-manuscript/build_docx_pair.py revised_styled.docx
```

`build_docx_pair.py` (now in the repo, no longer a scratchpad orphan) runs Word
`CompareDocuments` with named COM arguments, prints the revision counts, writes the
marked-up copy, then `AcceptAll()` for the clean copy. Verify afterwards: 10 images,
3 tables, 0 stale alloy names, 0 `[@` keys, and **non-zero α/γ counts** (the encoding
canary).

Two traps worth remembering:

- `front_JMRT.md` must **not** end in a `---` horizontal rule. Concatenated with the
  manuscript, pandoc reads it as the start of a second YAML metadata block and the build
  silently truncates. Use `***`.
- This Word build's `CompareDocuments` has **no `CompareMoves` parameter** — position 15 is
  the `BSTR` author name. Call it positionally with 17 arguments, not 18.
