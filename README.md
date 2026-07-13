# Fe-SMA Paper

Source files for the manuscript:

**"Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy"**

Rejected by *Materials & Design* (Elsevier) in July 2026 (no reviewer comments provided — appears to be a scope-based decision). Reformatted for four candidate journals; see `submissions/` for the ready-to-submit packages. `manuscript.md` is the single shared body — it reflects the full science content actually reviewed by Materials & Design (SEM/EDS, Rietveld phase-fraction quantification, loading-unloading-heating shape-memory test), which is more complete than any earlier commit in this repo's history.

## Layout

| Path | Contents |
|------|----------|
| `manuscript.md`         | Shared body: Abstract → Declarations. No title/author block (that's per-journal, see below). |
| `references.bib`        | BibTeX bibliography, 24 entries — exactly the refs cited in the submitted text. |
| `front_{SMS,JAC,MSEA,MMTA}.md` | Per-journal title page (author/affiliation block formatted to each journal's convention). |
| `springer.csl`          | Springer author-date style (used by SMS). |
| `elsevier-with-titles.csl` | Elsevier numbered style with article titles (used by JAC and MSE:A — same parent style Materials & Design itself uses, so references need no reformatting for those two). |
| `mmta.csl`               | Metallurgical and Materials Transactions A numbered style, no article titles. |
| `highlights.md`          | 5 highlight bullets (≤85 characters each), used for JAC and MSE:A. |
| `figures/Figure_1.jpg`–`Figure_6.jpg` | The 6 print-ready figures actually reviewed by Materials & Design. |
| `figures/captions.md`    | Current figure captions. |
| `figures/archive-2026-06-pre-MD-revision/` | Superseded pre-revision figure set, kept for reference. |
| `archive-2026-06-pre-MD-revision/` | Superseded pre-revision manuscript .docx/.md files, kept for reference. |
| `submissions/{SMS,JAC,MSEA,MMTA}/` | Assembled, ready-to-submit packages (manuscript, cover letter, figures, tables, highlights/graphical abstract where applicable). |

## Target journals

| Folder | Journal | Citation style | Notes |
|--------|---------|-----------------|-------|
| `SMS`   | *Shape Memory and Superelasticity* (Springer, IF 2.4) | author-date | Original target; exact scope match. |
| `JAC`   | *Journal of Alloys and Compounds* (Elsevier, IF 6.7) | numbered, with titles | Highlights + graphical abstract included. |
| `MSEA`  | *Materials Science and Engineering: A* (Elsevier, IF 7.0) | numbered, with titles | Highlights + graphical abstract included; closest broad-scope sibling to Materials & Design. |
| `MMTA`  | *Metallurgical and Materials Transactions A* (Springer/TMS-ASM) | numbered, no titles | Title page includes full mailing address; continuous line numbering added. |

## Rebuild the docx packages

```powershell
pandoc front_SMS.md manuscript.md --from markdown+yaml_metadata_block --to docx `
  --citeproc --bibliography references.bib --csl springer.csl `
  --resource-path=. --output submissions/SMS/Cai_Fe-SMA_SMS_manuscript.docx

pandoc front_JAC.md manuscript.md --from markdown+yaml_metadata_block --to docx `
  --citeproc --bibliography references.bib --csl elsevier-with-titles.csl `
  --resource-path=. --output submissions/JAC/Cai_Fe-SMA_JAC_manuscript.docx

pandoc front_MSEA.md manuscript.md --from markdown+yaml_metadata_block --to docx `
  --citeproc --bibliography references.bib --csl elsevier-with-titles.csl `
  --resource-path=. --output submissions/MSEA/Cai_Fe-SMA_MSEA_manuscript.docx

pandoc front_MMTA.md manuscript.md --from markdown+yaml_metadata_block --to docx `
  --citeproc --bibliography references.bib --csl mmta.csl `
  --resource-path=. --output submissions/MMTA/Cai_Fe-SMA_MMTA_manuscript.docx
```

MMT-A additionally needs continuous line numbering re-applied after any rebuild (python-docx injects `w:lnNumType` into the section properties — see `tasks/todo.md` for the one-off script used).

## Still needs a human pass before actual submission

- **Fort Wayne Metals and SSRF mailing addresses** in `front_MMTA.md` have placeholder ZIP/postal codes — MMT-A's title page requires exact city/state/zip (or city/country/postal code). Confirm and fill in.
- **Ref [18]** (Yang *et al.*, SSRF beamline paper) is cited with a truncated author list ("and others") because that's how it was cited in the Materials & Design submission. MMT-A's style guide asks for full author lists with no "et al." — worth tracking down the complete author list before that submission.
- Each journal's online submission system (title, abstract, keywords, suggested reviewers) still needs to be filled in by hand — this repo only produces the files, not the portal metadata.

## Authors

- Frank Y. Cai — School of Engineering Technologies, Purdue University, West Lafayette, Indiana, USA (corresponding), cai485@purdue.edu
- S. Cai — Fort Wayne Metals, Fort Wayne, Indiana, USA
- J. Yan — Shanghai Synchrotron Radiation Facility, Shanghai, China

This paper repo: <https://github.com/fronkt/fe-sma-paper>
