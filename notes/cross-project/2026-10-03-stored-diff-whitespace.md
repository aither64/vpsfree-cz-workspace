# Whitespace checks on stored unified diffs

Adding a raw Git diff as a tracking artifact can make the coordination
repository's diff --check flag its blank context lines: unified diff syntax
represents an unchanged blank line with a space prefix. That is patch data,
not a source whitespace defect.

Preserve raw patch bytes for comparison with the independent review. Check
ordinary metadata separately and verify each saved diff equals Git's actual
explicit base-to-head diff. Run source whitespace checks in the owning repo.
Observed in work/2026-10-03-newadmin-exception; no hook was disabled.
