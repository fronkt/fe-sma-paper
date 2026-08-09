# Lessons — fe-sma-paper

Patterns worth not repeating. Reviewed at the start of a session on this project.

---

## 2026-08-09 · Check an empirical correlation on its defined basis before quoting it

**What happened.** `revision/JMRT-R1/comment-triage.md` proposed answering R1#1 and R3#9
with a Schaeffler-type nickel equivalent, quoting **Ni_eq = 32.7 (LLM) vs 26.2
(benchmark)** with the carbon term contributing +13.5 vs +1.3. Those numbers were computed
from **atomic** percent. Schaeffler is defined in **weight** percent. Recomputed correctly:

| basis | LLM | benchmark | difference |
|---|---|---|---|
| at.% (as planned) | 32.60 | 26.05 | **+6.55** — supports the paper |
| wt.% (as defined) | 23.85 | 27.48 | **−3.63** — contradicts the paper |

The at.% version inflates the carbon term roughly four-fold, because at.% is much larger
than wt.% for a light interstitial. Applied correctly the correlation ranks the *benchmark*
as the more austenite-stabilised alloy, which is backwards from both the CALPHAD result and
the diffraction. Had the plan been executed as written, a number that flips sign under
correct application would have gone into a manuscript already under hostile review.

**Why it happened.** The formula was carried over from a planning document without being
recomputed, and the manuscript's own compositional discussion is in at.%, so at.% was the
unit closest to hand. The plan even labelled the number "indicative only" and named the
stainless-steel calibration as the caveat — which created a false sense that the risk had
been assessed, when the actual defect was a unit error, not a calibration limit.

**Rule.** Before quoting any empirical metallurgical correlation — Ni/Cr equivalents, SFE
regressions, Ms formulae, Hall–Petch constants — state its defined basis (wt.% vs at.%),
its calibration range, and its element set, then evaluate it on that basis and check the
sign of the answer against what is already known. If it disagrees with the physics-based
result, that disagreement is the finding; do not quietly pick the basis that agrees.

**How it was resolved.** §4.2 now reports the correlation *and its failure*, with the three
reasons it fails here (no aluminium term; the wt.%/at.% sensitivity of the carbon term;
Cr_eq ≈ 0–1.7 against a calibration band of 15–30 because neither alloy contains chromium).
That is a stronger answer to R1#1 and R3#9 than the correlation would have been, because a
composition-only potency heuristic pointing the wrong way is exactly the failure mode the
paper is about.

---

## 2026-08-08 · Do not promote an unrefined number, however long it has been in the draft

**What happened.** The 62 / 34 / 4 phase fractions had been in the manuscript through
several submissions and were about to go into the abstract because R2 Abstract#2 asked for
them. S. Cai's MAUD files showed all three fractions marked `not refinable`, scale factors
pinned at 1.0, no ESDs, and the one run that *did* refine them putting D0₃ at 1.56(11) %
rather than 4 %.

**Rule.** A number's residence time in a draft is not evidence for it. Before a value is
promoted to a more prominent position — abstract, title, highlights — check the artifact it
came from, not the draft that carries it. Withhold and ask rather than guess at honest
wording; the wording depends on the answer.

---

## 2026-08-08 · Verify a check before reporting a failure

**What happened.** Several verification passes reported MISSING for content that was
present. Two distinct causes: pandoc's markdown export wraps lines at ~72 characters, so
multi-word search phrases straddle a newline; and `python-docx`'s `inline_shapes` does not
traverse `<w:ins>`/`<w:del>`, so a tracked-changes document reported "0 images" while the
package contained 8 media files and 13 `<w:drawing>` elements.

**Rule.** A failing check on work that should have succeeded is first a suspect check.
Normalise whitespace before matching, and confirm against the underlying artifact (unzip
the DOCX) before reporting a defect to the user. Related: a search string using `DO3`
(letter O) will miss `D0₃` (zero plus subscript) — normalise notation in the checker, not
just in the document.

---

## 2026-08-08 · Round-trip UTF-8 through explicit encoders on Windows

**What happened.** A global find-and-replace across `manuscript.md` using PowerShell
`Get-Content -Raw` / `Set-Content` produced 106 mojibake sequences and zeroed every γ and
α. A later `-Encoding utf8` write added a BOM.

**Rule.** For any programmatic edit of a manuscript file, read and write through
`[System.IO.File]::ReadAllText/WriteAllText` with `New-Object System.Text.UTF8Encoding($false)`,
or use Python with an explicit `encoding='utf-8'`. Afterwards, count γ / α / ° / ₃ and
assert zero occurrences of `â€` and `Ã`. Git is the safety net: commit before a global
rewrite so `git checkout --` can undo it.

---

## 2026-08-08 · Hand-editing the DOCX does not work once tracked changes exist

**What happened.** Direct Word COM find-and-replace against the submitted manuscript missed
targets — Word's `Find` cannot match across existing `<w:ins>`/`<w:del>` markup — and the
six new CALPHAD references renumbered the bibliography 24 → 30, which no find/replace gets
right.

**Rule.** Edit `manuscript.md`, render with pandoc using the submitted DOCX as
`--reference-doc`, then let Word `CompareDocuments` generate the tracked changes. Also:
`front_JMRT.md` must not end with a `---` horizontal rule, or pandoc parses it as a second
YAML metadata block on concatenation and silently truncates the build. Use `***`.

---

## 2026-08-08 · Write git commit messages to a file

**What happened.** A PowerShell here-string containing double quotes split the commit
message into arguments, producing `pathspec ... did not match` errors.

**Rule.** `git commit -F <file>` for anything longer than one line.
