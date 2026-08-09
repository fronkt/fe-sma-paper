# JMRT-D-26-06169 — R1 resubmission package

**Journal:** Journal of Materials Research and Technology
**Decision being answered:** major revision, 45 comments (R1 × 9, R2 × 24, R3 × 12)
**Package assembled:** 2026-08-09

> ⚠️ **This package is not yet complete and must not be uploaded as it stands.**
> See *Not yet in this folder* below. The two manuscript files are current and correct;
> what is missing is the response letter and three human sign-offs.

---

## What is here

| File | Upload as | Notes |
|---|---|---|
| `Cai_Fe-SMA_JMRT_R1_marked-up.docx` | **Revised Manuscript (Marked-up)** | 386 tracked revisions — 202 insertions, 184 deletions — against the file actually submitted. Includes the renumbered bibliography (24 → 35). |
| `Cai_Fe-SMA_JMRT_R1_clean.docx` | **Revised Manuscript (Clean)** | Identical content with all revisions accepted. |
| `Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx` | *do not upload* | The original submission, kept here so the pair can be diffed without leaving the folder. |

Both revised files are byte-identical copies of
`revision/JMRT-R1/R1-manuscript/`, which is the build output directory. **Edit the source,
not these** — see *How to rebuild* below.

## Not yet in this folder

| Missing | Blocked on |
|---|---|
| **Point-by-point response letter** (all 45 boxes) | Groups B–D in `tasks/todo.md`; the JMRT portal requires a reply in every box, so shared answers must be cross-referenced rather than left blank |
| **Updated `highlights.md`** and cover letter | Must match the tempered claims; currently still worded for the original submission |
| **Revision title sign-off** | Co-authors. Drafted in `front_JMRT.md`, flagged `NEEDS CO-AUTHOR SIGN-OFF` |
| **Generative-AI declaration sign-off** | Frank. The submitted version of this statement was **false**; the rewrite is in the manuscript but the scope is the authors' call, not a drafting decision |
| **Figures at final resolution** | Fig. 2 **has been rebuilt** from the raw Instron exports — `revision/JMRT-R1/mechanical/Figure_2_rebuilt.png` — with the clipped tick labels fixed and all eight anneal conditions shown, but it is not swapped in yet because the as-drawn trace is missing from the drive (S. Cai). The AGG figure (R1#4, R3#4) is unbuilt pending Frank's D7 reading |
| **Supplementary Material: the LLM report** | §2.1 now promises the 41-page Gemini Deep Research report as Supplementary Material. The file is at `revision/JMRT-R1/llm-provenance/Gemini-DeepResearch_New-Fe-SMA-Alloy-Hypotheses_2025-06-04.pdf` and must be uploaded, or the promise removed |
| **§2.1 melt-and-draw description** | S. Cai. The process note shows the two alloys took materially different routes and that several specifics in §2.1 are wrong (ingot size, melt mass, hot-roll temperature, remelt). See `revision/JMRT-R1/processing/PROCESSING-AND-REPLICATES.md` §2 — this is the largest open correction in the paper |

## Status of the revision

29 of 45 comments answered. The remaining 16 are enumerated by blocker in
`tasks/todo.md`, and every change made so far is documented in
`revision/JMRT-R1/CHANGES-FROM-SUBMISSION.md`.

One item to carry into the response letter deliberately: **the 62 / 34 / 4 phase
fractions are not yet quotable.** S. Cai's MAUD files show they were never refined — all
three marked `not refinable`, scale factors pinned at 1.0, no ESDs — and the one run that
did refine them put D0₃ at 1.56(11) % rather than 4 %. They were therefore left out of the
abstract even though R2 Abstract#2 asks for them. See
`revision/JMRT-R1/xrd/RIETVELD-FILES-ANALYSIS.md`.

## How to rebuild these two files

Do not hand-edit the DOCX. The eleven new references renumber the whole bibliography,
which no find/replace gets right, and Word's `Find` cannot match across existing revision
markup so edits silently miss once tracked changes are present.

From the repository root:

```bash
cat front_JMRT.md manuscript.md > full_JMRT.md
pandoc full_JMRT.md --citeproc \
  --bibliography=references.bib \
  --csl=elsevier-with-titles.csl \
  --reference-doc=revision/JMRT-R1/as-submitted/Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx \
  -o revised_styled.docx
```

Then run Word `CompareDocuments` (the as-submitted file as the original, `revised_styled.docx`
as the revision) to produce the marked-up copy, and `Revisions.AcceptAll()` on a duplicate
for the clean copy. Working script: `compare.py` in the session scratchpad.

Two traps worth remembering:

- `front_JMRT.md` must **not** end in a `---` horizontal rule. Concatenated with the
  manuscript, pandoc reads it as the start of a second YAML metadata block and the build
  silently truncates. Use `***`.
- This Word build's `CompareDocuments` has **no `CompareMoves` parameter** — position 15 is
  the `BSTR` author name. Call it positionally with 17 arguments, not 18.
