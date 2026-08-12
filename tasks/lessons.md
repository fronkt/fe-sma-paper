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

## Look for the primary artifact before writing around its absence

The Gemini Deep Research report was listed as a blocker (D3) for weeks on the assumption it
was lost, and §2.1 was written to paraphrase a prompt nobody had. It was sitting on the E:
drive the whole time, in the same folder as the chemistry certificates, under a filename
whose trailing underscore is the signature of a Google Docs export.

**Why:** the paraphrase was not merely thin, it was wrong. The manuscript claimed the
composition came from "within one of the AI-suggested composition ranges"; it is outside that
range on two of six elements, one of them aluminium by a third. A reviewer given the report as
Supplementary Material would have found that in ten minutes.

**How to apply:** when a blocker is "the source file is probably gone", spend ten minutes
searching for it before writing prose that assumes its absence. Search by *artifact signature*
(exporter naming conventions, producer metadata, modification dates) as well as by keyword —
`grep -ri gemini` found nothing; `ls` in the right folder found it immediately. And check the
date: the report's export timestamp and the ingot request in the process note are the same day.

## Reconstruct the table from the raw data, not just the summary report

Table 2 was verified twice against the Instron PDF and passed. It only came apart when the raw
CSV traces were reduced independently: the elongation column reproduces exactly on a 127 mm
gauge, and §2.4 claimed 13 mm.

**Why:** a summary report and the paper can agree with each other and both be describing the
measurement wrongly. The independent check is the one that recomputes the reported quantity
from the rawest available input.

**How to apply:** when a method section states a parameter that also appears implicitly in the
data (gauge length, area, rate), close the loop. Here two independent routes agreed — the
elongation column and the stated strain rate both imply 5 in — which is what made the
correction safe to make without asking anyone.

## Test the counterfactual before reporting the deviation

Finding that the melt sat outside the agent's proposed range was the session's most alarming
result: it threatened to convert "the AI's composition failed" into "we didn't build the AI's
composition." The right response was not to soften the prose but to run the window and find
out — and the window fails everywhere, for a reason (carbon) the agent specified itself.

**Why:** disclosing a deviation without testing whether it mattered invites exactly the
objection the disclosure was meant to pre-empt, and hands the reviewer the stronger reading.

**How to apply:** when a newly found fact undermines a paper's central claim, cost out the
calculation that would settle it before writing a single hedged sentence. Two hours of CPU
turned a liability into a result.

## A published panel is a claim about a specimen — measure it before you defend it

`Fig2b` was defended, discussed and re-cropped for two journal submissions as "the LLM-alloy
after AGG". Measured against its own scale bar it is 868 µm across, and the wire it was
supposed to be is 360 µm. The correct 0.36 mm panel was on the same drive, in the same folder,
unused. The whole published Fig. 2 pair — LLM rod against benchmark wire — was never
like-for-like.

**Why:** figure filenames are captions someone typed once, not measurements. Every other layer
of review takes the filename at face value, so nothing downstream can catch this; the check has
to happen at the image.

**How to apply:** before writing a sentence about a micrograph, measure the specimen against the
bar burned into that panel and reconcile it with a dimension the paper states independently.
Here the benchmark panel measuring 630 µm against the recorded 0.0253 in stock is what proved
the method sound and made the 868 µm anomaly trustworthy — check a panel you expect to pass, not
only the one you suspect.

## Apply a correction's standard to the rest of the same figure set, immediately

Having caught `Fig2b`, the archived cyclic panels went under the same test. `Fig3b` matches no
row in any of the eight Instron reports on the drive, so it stayed out of this revision. It
would have been incoherent to publish an unidentified panel in the revision that corrects
another panel for being unidentified.

**Why:** a correction sets a standard. Applying it to one file and not its siblings is worse
than not having found it — it produces a document that looks audited and is not.

**How to apply:** when a provenance failure is found, enumerate every artifact of the same class
in the same commit and run the same check. Report the ones that fail as held, with the evidence,
rather than quietly keeping them.

## Ask what the submission system actually wants before designing around it

The plan carried "all 45 comments need an individual reply box" for two weeks, and shaped the
response-letter strategy around cross-referencing shared answers between reviewers. JMRT takes
one response *per reviewer*. Cross-referencing across reviewers would have sent Reviewer 1 to a
reply they cannot see.

**Why:** this was inferred from the review letter's structure, never verified against the portal,
and it silently changed a deliverable's shape.

**How to apply:** any claim about an external system's requirements is an assumption until
someone with the account confirms it. Mark it as an assumption in the plan, and ask early —
the cost of asking is one line, the cost of being wrong is a rewritten deliverable.

## Two mechanisms that co-occur in one alloy are not one mechanism

New evidence (S. Cai, 2026-08-12) says the LLM-alloy's diffraction pattern after the AGG
treatment is *spottier* than Fig. 4a, not "similar" to it — the grains coarsened. My first read
was that this cut against Sec. 3.5. It does not. The paper's claim is that the treatment does not
produce **bamboo** structure, and coarsening is a different thing. In the benchmark the two arrive
together, which is exactly why they get conflated.

**Why:** in the reference system the mechanisms are correlated, so a single word ("coarsening")
was doing duty for both. The moment an alloy separates them, the shared word turns a correct
claim into a wrong one — in either direction, and the wrong ones are equally easy to write.

**How to apply:** when the whole point of a result is that alloy B behaves unlike alloy A, list
the phenomena that are welded together in A and check each is named separately in the text. Here
that was grain *size* versus grain *span/shape*; Sec. 3.5 now says which one it is claiming, in
the sentence that makes the claim.

## Ask why a target is a target before writing its absence as a failure

Sec. 3.5 was written so that the LLM-alloy "neither transforms nor accepts the grain
structure" — the missing bamboo counted as a second, independent failure. Frank: bamboo
does not give enough elongation in this alloy. The 1200 °C/40 min condition is already at
1.4 % and nearly breaks, so bamboo was never something worth achieving here. AGG was run to
complete the benchmark comparison, and what it grew was the duplex structure.

**Why:** I inherited the benchmark's goal structure along with its processing route. In the
Omori alloy bamboo *is* the target, so its absence reads as failure; I never checked whether
the target transfers. The disproof was already inside the repo — `instron-reports-extracted.txt`
rows 11 and 12, same diameter, same age, 11.0 % against 1.4 %.

**How to apply:** when a paper's structure is "alloy B put through alloy A's route," every
goal in that route is an assumption about B, not a fact. Before writing "B failed to achieve
X," ask what X would be worth to B — and look for the condition already in the data that
answers it. A negative result is only as good as its account of what would have counted as
success.
