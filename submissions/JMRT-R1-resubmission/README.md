# JMRT-D-26-06169 — R1 resubmission package

**Journal:** Journal of Materials Research and Technology
**Decision being answered:** major revision, 45 comments (R1 × 9, R2 × 24, R3 × 12)
**Package assembled:** 2026-08-09 · **manuscript pair rebuilt 2026-08-14** (S. Cai merge,
Fig. 2 rebuild, figure renumbering to 10, affiliation fix)

> ⚠️ **This package is not yet complete and must not be uploaded as it stands.**
> See *Not yet in this folder* below. The two manuscript files are current and correct;
> what is missing is the response letter and three human sign-offs.

---

## What is here

| File | Upload as | Notes |
|---|---|---|
| `Cai_Fe-SMA_JMRT_R1_marked-up.docx` | **Revised Manuscript (Marked-up)** | 461 tracked revisions — 221 insertions, 200 deletions, 40 formatting — against the file actually submitted. Includes the renumbered bibliography (24 → 35) and the ten-figure set. |
| `Cai_Fe-SMA_JMRT_R1_clean.docx` | **Revised Manuscript (Clean)** | Identical content with all revisions accepted. |
| `Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx` | *do not upload* | The original submission, kept here so the pair can be diffed without leaving the folder. |

Both revised files are byte-identical copies of
`revision/JMRT-R1/R1-manuscript/`, which is the build output directory. **Edit the source,
not these** — see *How to rebuild* below.

## Not yet in this folder

| Missing | Blocked on |
|---|---|
| **Response letters — three documents, one per reviewer** (portal takes per-reviewer responses, not 45 boxes; corrected by Frank from the portal 2026-08-12) | Tier 6 in `tasks/todo.md`; shared answers written out in full for each reviewer |
| **Updated `highlights.md`** and cover letter | Must match the tempered claims; currently still worded for the original submission |
| **Revision title sign-off** | Co-authors. Drafted in `front_JMRT.md`, flagged `NEEDS CO-AUTHOR SIGN-OFF` |
| **Generative-AI declaration sign-off** | Frank. The submitted version of this statement was **false**; the rewrite is in the manuscript but the scope is the authors' call, not a drafting decision |
| **Figures at production resolution** | Fig. 2 (rebuilt, 600 dpi) **is swapped in**, the AGG figure is built (now Fig. 10), and S. Cai's Figs. 1/5/7/8 are merged — but Figs. 1, 4, 6 and 8 are below Elsevier's 300-dpi floor (audit + remedies in `tasks/todo.md`, 2026-08-14). Ask S. Cai for the as-drawn Instron export (Fig. 2 gains it automatically) and higher-res Fig. 1 panels |
| **Supplementary Material: the LLM report** | §2.1 now promises the 41-page Gemini Deep Research report as Supplementary Material. The file is at `revision/JMRT-R1/llm-provenance/Gemini-DeepResearch_New-Fe-SMA-Alloy-Hypotheses_2025-06-04.pdf` and must be uploaded, or the promise removed |
| **§2.1 melt-and-draw description** | S. Cai. The process note shows the two alloys took materially different routes and that several specifics in §2.1 are wrong (ingot size, melt mass, hot-roll temperature, remelt). See `revision/JMRT-R1/processing/PROCESSING-AND-REPLICATES.md` §2 — this is the largest open correction in the paper |

## Status of the revision

**As of 2026-08-14: ~41 of 45 comments answered in the manuscript.** Still open: R1#7
(SME heating rate/hold — S. Cai), R2 Exp#2 (tensile standard — S. Cai, plus the
13 mm-vs-127 mm gauge discrepancy), title sign-off, and the three response letters.
Everything is enumerated in `tasks/todo.md`; every change is documented in
`revision/JMRT-R1/CHANGES-FROM-SUBMISSION.md` (§9 covers the 2026-08-14 S. Cai merge).

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
