# Contribution prepared for review

Upstream: https://github.com/un33k/python-slugify · commit `866401ea6b346d7575cf941bc73ad32a362e34aa` · MIT license.

## Reproducible problem

`python -m slugify --regex-pattern '[' 'hello world'` raises a Python traceback and exits 1. Invalid command-line input should produce a concise usage error. The patch validates regex syntax with argparse, returns the unchanged string for valid patterns, and exits 2 with an actionable message for invalid patterns. Both legacy and modern algorithms remain untouched.

## Review scope

One CLI source file changes. Regression tests cover five malformed patterns, three valid patterns, and both algorithms. `reproduce.py` runs the same tests before and after applying the patch at the pinned upstream revision. The JSON report contains actual results.

## Proposed upstream PR

Title: Validate --regex-pattern through argparse

Invalid regex patterns currently escape as tracebacks. Compile the supplied pattern in an argparse type validator and report syntax failures as usage errors. Preserve the original pattern string for existing slugification behavior. Add regression coverage for malformed patterns and valid legacy/modern invocations.

Status: patch prepared locally; no issue or pull request submitted; not accepted upstream. The original library remains the work of its upstream authors. Abhijith's portfolio contribution is the reproduction harness, regression coverage, and focused patch, developed with Codex assistance.
