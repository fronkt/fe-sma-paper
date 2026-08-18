"""Rebuild Fig. 3 — REVERTED 2026-08-18 to the two-panel (a)/(b) form.

History: R3#7 asked for corresponding stepwise cyclic curves for the benchmark, and
on 2026-08-12 the two archived Omori panels (1200 C/5 min and 12 s) were appended as
(c)/(d). On 2026-08-18 F. Cai reversed that call: the paper's purpose is to test
whether the LLM-hypothesized alloy can transform, the Omori alloy's superelasticity
is established literature, and its role here is a protocol control only — which
panel (b) (0.5% heating recovery) already demonstrates. The R3#7 response now argues
that position instead of presenting the curves; see response-to-reviewer-3.md.

The (c)/(d) panels remain in `archive-2026-06-pre-MD-revision/` and the four-panel
composite is archived as `archive-2026-08-18-Figure_3-four-panel.jpg` should the
editor insist.

Panels (a)/(b) are carried over as `archive-2026-08-12-Figure_3-two-panel.jpg`,
which already carries its own "a)" / "b)" labels, upscaled to the same 3624-px
width as the sibling repo-built figures (its effective resolution is set by the
1200-px source either way — same situation as Fig. 1, and rebuildable from raw
only via S. Cai's SME-test exports).
"""
from pathlib import Path
from PIL import Image

HERE = Path(__file__).parent
TARGET_DPI = 600
PANEL_W = 1800
GAP = 24


def main():
    src = Image.open(HERE / "archive-2026-08-12-Figure_3-two-panel.jpg").convert("RGB")
    w = 2 * PANEL_W + GAP
    out_img = src.resize((w, round(src.height * w / src.width)), Image.LANCZOS)
    out = HERE / "Figure_3.jpg"
    out_img.save(out, dpi=(TARGET_DPI, TARGET_DPI), quality=95, optimize=True)
    print(f"wrote {out.name}  ({out_img.size[0]}x{out_img.size[1]} px, "
          f"{out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
