# CI topic patterns are shell input

The API workflow matrix uses YAML `patterns: |` scalars and expands each line
with an intentionally unquoted Bash loop. A comment indented inside that scalar
is data and becomes nonexistent RSpec path arguments. YAML parsing and a Ruby
`Dir.glob` checker that discards comments can miss the defect.

Place any explanatory comment outside the scalar. Validate with the exact
workflow expansion (`nullglob`, `globstar`, word splitting, glob expansion,
then per-topic `sort -u`), reject nonexistent files, and verify each tracked spec
is covered by exactly one topic. Overlapping patterns within a topic are valid.

The kernel-history general review found this before push. After removing the
comment, exact expansion covered 404 specs once with no nonexistent paths.
Related: `work/2026-09-14-kernel-history-fix/review-reconciliation.md` and
`verification.md`. The early simplified checker was not retained as a tool.
