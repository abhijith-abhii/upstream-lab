# Upstream Lab

Reproduce and improve an open-source behavior for **open-source reviewers**.

Original topic: **Open Source Contribution** from [the source post](https://www.instagram.com/p/DdyMaogE4ud/).

> Local portfolio implementation developed with Codex assistance. Measured results and limitations are documented; no production adoption, revenue or hiring outcome is claimed.

## What works

- Pinned upstream
- failing regression
- patch
- isolated reproduction

[Demonstration guide](LEARNING_GUIDE.md) · [Verification notes](VERIFICATION.md) · [Learning and interview guide](LEARNING_GUIDE.md)

## Start

Python 3.12 is the validated Python runtime. Run commands from this repository directory. Windows users activate `.venv\Scripts\activate` instead of `source`.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python reproduce.py
```

## Demonstration

Install requirements and run python reproduce.py from a fresh checkout. Inspect reports/regression.json: malformed regex tests fail before the patch and pass afterward. The script refuses an already modified upstream clone.

## Architecture and decisions

Pinned upstream clone → baseline regression checks → focused patch → identical checks → recorded evidence.

Stack: Python · pytest.

1. Pin the upstream commit so the before/after comparison remains reproducible.
2. Validate regex syntax at the CLI boundary while returning the original valid pattern string.
3. Keep the patch separate from upstream source and preserve license and author attribution.

## Verification

```sh
python reproduce.py  # fresh var/upstream clone required
```

See [VERIFICATION.md](VERIFICATION.md) for actual executed checks, setup verification, model/data results and any outstanding environment limitations. The [recorded CI runs](reports/ci-verification.json) passed for the linked source revision.

## Data and attribution

Attributed upstream source. See [DATA_AND_SOURCES.md](DATA_AND_SOURCES.md) for provenance and usage notes. Original project code is MIT unless a preserved source file or dependency states otherwise. Model and third-party data licenses remain separate.

## Limitations and next improvement

Patch is prepared, not submitted or accepted. Tested on Python 3.12/macOS with the default text-unidecode backend; the full interpreter/backend release matrix was not run. No change to the frozen legacy slug algorithm.

Suggested extension: Add a regression case for an invalid named backreference and explain why argparse should report it.

## Honest portfolio use

This implementation and documentation were developed with substantial Codex assistance. Before presenting it, run the demonstration, explain the design choices, and complete the suggested independent modification. Do not describe generated code as work experience, an accepted upstream contribution, or a deployed production service.
