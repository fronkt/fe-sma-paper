# Fe-SMA SMS Paper

Source files for the journal manuscript:

**"Limited Room-Temperature Pseudoelasticity in an AI-Hypothesized Fe-Mn-Al-Si-Ni-C Alloy: Synthesis, Microstructure, and Cyclic Response"**

Target venue: *Shape Memory and Superelasticity* (Springer).

## Layout

| Path | Contents |
|------|----------|
| `manuscript.md`                                | Master markdown source |
| `references.bib`                               | BibTeX bibliography (31 entries) |
| `springer.csl`                                 | Springer basic author-date citation style |
| `Cai_Fe-SMA_SMS_manuscript.docx`               | Word output (Chicago author-date) |
| `Cai_Fe-SMA_SMS_manuscript_SpringerStyle.docx` | Word output (Springer style) |
| `figures/Fig*`                                 | Final composites + individual panels (300–600 dpi); manuscript figures Fig. 1–4 |
| `figures/captions.md`                          | Full caption text and assembly notes |
| `figures/build_composites.py`                  | PIL script that regenerates the 2×2 composites |
| `figures/sources/`                             | Native-resolution source images |
| `figures/sources/poster_media/`                | All images extracted from the ISEF poster `.pptx` |

## Rebuild the .docx

```powershell
# Springer-style (Shape Memory and Superelasticity)
pandoc manuscript.md `
  --from markdown+yaml_metadata_block `
  --to docx `
  --citeproc `
  --bibliography references.bib `
  --csl springer.csl `
  --output Cai_Fe-SMA_SMS_manuscript_SpringerStyle.docx

# Default (Chicago author-date)
pandoc manuscript.md `
  --from markdown+yaml_metadata_block `
  --to docx `
  --citeproc `
  --bibliography references.bib `
  --output Cai_Fe-SMA_SMS_manuscript.docx
```

## Rebuild composite figures

```powershell
cd figures
python build_composites.py
```

## Authors

- Frank Cai — Homestead Senior High School, Fort Wayne, IN, USA (corresponding)
- S. Cai — Fort Wayne Metals, Fort Wayne, IN, USA
- J. Yan — Shanghai Synchrotron Radiation Facility, Shanghai, China

This paper repo: <https://github.com/fronkt/fe-sma-paper>
