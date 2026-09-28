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

1. **What is the upstream defect?** A malformed custom regular expression passed to python-slugify’s CLI raised an uncaught traceback. The patch converts that invalid argument into an argparse usage error and exit code 2.

2. **How do you know the patch fixes a real issue?** The reproduction clones a pinned upstream revision and records failing malformed-regex cases before applying the patch. The same ten regression cases pass afterward.

3. **Why pin the upstream commit?** Upstream can change. Pinning makes the before/after comparison reproducible and prevents a future upstream fix from being mistaken for the effect of this patch.

4. **How is compatibility checked?** The focused regressions include valid expressions and Unicode-related inputs, and the upstream suite passed 125 tests with one skip. Full upstream release tooling was not claimed as executed.

5. **Was the contribution accepted?** No upstream submission or acceptance is claimed. This repository contains the patch, reproducer, attribution and a draft contribution write-up ready for human review.

## Independent exercise

Add a regression case for an invalid named backreference and explain why argparse should report it.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Prepared a reproducible python-slugify CLI validation patch with ten passing regression cases and a 125-pass upstream suite; contribution remains unsubmitted.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
