# Fe-SMA SMS Paper

Source files for the journal manuscript:

**"Process-Aware Limits of AI-Guided Alloy Design: A Computational and Experimental Audit of an LLM-Hypothesized Fe-Mn-Al-Si-Ni-C Shape Memory Alloy"**

Target venue: *Shape Memory and Superelasticity* (Springer).

## Layout

| Path | Contents |
|------|----------|
| `manuscript.md`                                | Master markdown source (5,300+ words) |
| `references.bib`                               | BibTeX bibliography (31 entries) |
| `springer.csl`                                 | Springer basic author-date citation style |
| `Cai_Fe-SMA_SMS_manuscript.docx`               | Word output (Chicago author-date) |
| `Cai_Fe-SMA_SMS_manuscript_SpringerStyle.docx` | Word output (Springer style) |
| `figures/Fig1–Fig5_*`                          | Final composites + individual panels (300–600 dpi) |
| `figures/captions.md`                          | Full caption text and assembly notes |
| `figures/build_composites.py`                  | PIL script that regenerates the 2×2 composites |
| `figures/sources/`                             | Native-resolution source images |
| `figures/sources/poster_media/`                | All images extracted from the ISEF poster `.pptx` |

## Rebuild the .docx

```powershell
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

## Companion repo

The computational audit pipeline used in this paper lives at <https://github.com/frankcai222/fe-sma-xrd>.

This paper repo: <https://github.com/fronkt/fe-sma-paper>
