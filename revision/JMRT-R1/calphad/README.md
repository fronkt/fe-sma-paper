# CALPHAD for the JMRT revision

Answers R1#2, R3#2, R3#9, R2 R&D#2 and R2 Concl#4 — the five comments that all ask,
in different words, for a thermodynamic calculation the submitted manuscript does not have.

**Verdict (2026-08-05): feasible on this machine today. Thermo-Calc is not required.**

## Engine

`pycalphad` 0.11.2, installed with `pip install pycalphad` (Python 3.12.10, Windows).
No Fortran toolchain, no licence, no institutional account.

OpenCalphad was the original candidate and would also work — it reads the same TDB format
and ships a precompiled Windows binary — but pycalphad was chosen because it installs in one
command, scripts cleanly, and makes every number in the revision reproducible from a file in
this folder. Anything computed here is portable to OpenCalphad or Thermo-Calc unchanged,
since the database format is shared.

**The engine was never the constraint. The database was.**

## Databases

None of these ship with the code; `fetch_databases.py` downloads them from the pycalphad
project's own database collection. They are *not* committed here — see Licensing below.

| Database | Elements | Ordering / carbides | Use |
|---|---|---|---|
| **mpea-02b** (Hallstedt, HEA v2b, 2017) | Al C Co Cr Fe Mn Ni — *no Si* | `B2_BCC` partitioned over `A2_BCC`, `FCC_4SL`, `KAPPA_E21` | **Primary.** Only database covering Fe-Mn-Al-**Ni**-**C** together, i.e. both B2-NiAl and the carbon effect |
| **PrecHiMn-04** | Al C Fe Mn N Nb Si Ti V — *no Ni* | `BCC_4SL` (A2/B2/**D0₃**), `KAPPA_E21`, cementite, M23C6, M7C3 | Cross-check. The only one with **D0₃** and with Si. Purpose-built for the Fe-Mn-Al-C lightweight-steel field R3#2 says this alloy belongs to |
| **mc_fe v2.059** (MatCalc open Fe) | 24 elements incl. all six **plus P** | `BCC_A2`/`BCC_B2`, cementite, M23C6, M7C3, κ | Cross-check. Broadest element coverage — the only one that can carry Si, C and the benchmark's 0.06 wt.% P at once. Weakest on ordering (2 sublattices, no D0₃) |

No single public database covers Fe-Mn-Al-Ni-Si-C *and* models B2, D0₃ and κ. Using three
and reporting where they agree is the honest answer, and is a stronger claim than one
proprietary run — agreement across independent assessments is evidence of robustness.

Also downloaded and rejected: `COST507` (has all six elements but is assessed for the
Al-rich corner, not Fe-rich), `iron-04` (no Al), `mc_al` (no C), `mc_ni` (Ni-base),
`steel1` (no Mn, Al, Ni).

## Results

**Full step diagrams are done — see `results/ANALYSIS.md`.** 400–1400 °C, 791 points,
three databases, three alloys each. That document is the one to read; it carries the
findings, the two problems the calculations expose in the manuscript, and the numerical
artifacts to disclose.

Headline: all three databases agree that at 1200 °C the benchmark is single-phase α, the
LLM-alloy is not, and **removing carbon alone restores the single-phase α window**.

Run it with:

    python fetch_databases.py
    python step_diagrams.py      # ~15 min
    python plot_step_diagrams.py

### Superseded — the original smoke test

`smoke_test.py` was the feasibility probe and its numbers **should not be quoted**. It
passed `FCC_A1`/`BCC_A2` alongside their ordering-aware twins `A1_FCC`/`A2_BCC`/`B2_BCC`,
but mpea-02b declares `DEFAULT-COM REJECT_PHASE FCC_A1 BCC_A2` — those are duplicate
descriptions of the same phases, so several phases were entered twice. It is kept only
because it is what established that the route was viable at all.

| | 1200 °C | 900 °C | 600 °C |
|---|---|---|---|
| **Benchmark** (Fe-34.2Mn-15.2Al-7.8Ni-0.04C) | BCC 100 % | FCC 81 %, B2 19 % | FCC 58 %, B2 22 %, β-Mn 20 % |
| **LLM-alloy** (Fe-30.4Mn-12.2Al-4.3Ni-0.46C) | **BCC 71 %, FCC 29 %** | FCC 100 % | FCC 92 %, B2 8 % |
| **LLM-alloy, C set to zero** | **BCC 100 %** | FCC 100 % | FCC 92 %, B2 8 % |

Two things worth the revision:

1. **The database reproduces the benchmark.** Omori's route solution-treats at 1200 °C
   expecting single-phase α, and the calculation returns exactly that. A database that gets
   the control right is a database whose verdict on the test alloy can be quoted.

2. **Carbon alone accounts for the γ at the solution-treatment temperature.** At 1200 °C the
   LLM composition is 71 % BCC + 29 % FCC; delete the carbon and it is 100 % BCC — identical
   to the benchmark. Every other element is held fixed. This is the C-free control R1#1 asks
   for, and it supports the manuscript's central claim rather than undermining it.

But note the nuance, which is more accurate than the submitted manuscript's story: at 900 °C
*both* LLM variants are fully austenitic, so carbon is not the whole explanation across the
range. Carbon controls the constitution **at the temperature where the processing route
actually operates**; the lower Al and Ni of the base composition move the α/γ boundary too.
Write it that way — it survives scrutiny and the simpler version does not.

## Caveats to state in the manuscript

- **Si is absent from mpea-02b** (2.04 at.% in the LLM-alloy). Si stabilises ferrite, so
  including it would push toward BCC — the omission is conservative in the direction that
  matters. Confirm against PrecHiMn-04, which has Si.
- pycalphad warns that the **partitioned B2_BCC magnetic contribution** is not correctly
  substituted into the disordered part (pycalphad PR #311). Disclose it; cross-check B2
  fractions against mc_fe, which uses a different model.
- `B2_BCC` is the *partitioned* phase and is reported by that name whether or not it is
  ordered. **At 1200 °C it is almost certainly the disordered A2 state.** Extract site
  fractions and compute the order parameter before claiming B2 anywhere.
- Equilibrium is not the as-quenched state. Say so.

## Files

- `fetch_databases.py` — downloads the databases into `db/`
- `smoke_test.py` — the feasibility check above
- `db/` — not committed, see below

## Licensing

The TDB files are **deliberately not committed to this repository.** They are third-party
assessments under their authors' terms (mc_fe is free for academic use; redistribution is a
separate question). Fetch them, cite the original assessment papers in the manuscript, and
keep this repo clean of files we do not have the right to redistribute.
