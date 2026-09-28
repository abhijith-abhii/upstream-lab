# Upstream Lab — learning guide

## What it does

Reproduce and improve an open-source behavior. The intended user is open-source reviewers. Pinned upstream clone → baseline regression checks → focused patch → identical checks → recorded evidence.

## Run and demonstrate

Follow the README installation block, then: Install requirements and run python reproduce.py from a fresh checkout. Inspect reports/regression.json: malformed regex tests fail before the patch and pass afterward. The script refuses an already modified upstream clone.

## Important files

- `upstream.json` — pinned source and submission status.
- `reproduce.py` — isolated before/after harness.
- `patches/validate-cli-regex.patch` — proposed code change.
- `tests/test_cli_regression.py` — CLI behavior coverage.

## Three engineering decisions

1. Pin the upstream commit so the before/after comparison remains reproducible.
2. Validate regex syntax at the CLI boundary while returning the original valid pattern string.
3. Keep the patch separate from upstream source and preserve license and author attribution.

## Five interview questions

1. **What problem does this project solve, and what is its unit of work?** Explain reproduce and improve an open-source behavior, identify open-source reviewers as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Pin the upstream commit so the before/after comparison remains reproducible. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Validate regex syntax at the CLI boundary while returning the original valid pattern string. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Keep the patch separate from upstream source and preserve license and author attribution. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Patch is prepared, not submitted or accepted. Tested on Python 3.12/macOS with the default text-unidecode backend; the full interpreter/backend release matrix was not run. No change to the frozen legacy slug algorithm. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a regression case for an invalid named backreference and explain why argparse should report it.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated reproduce and improve an open-source behavior using Python · pytest, with pinned upstream and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
