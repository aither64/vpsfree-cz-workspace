# Naming source intake

Read-only intake of the two explicitly authorized `2026-10-20-workspace-session-naming` worktrees for owner session `2026-10-24-workspace-session-ui`.

| Repository | Exact source HEAD | Comparison base | Source files captured |
| --- | --- | --- | --- |
| dev-workspace | `529e075ad07e2d967a8af4902584e37527115454` | `10bb047513c82d1310e8fcaa797e8772f948dd8a` | 18 |
| codex-web | `801099102ef9af4a82c1f3853c53d6b442ecd4dc` | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` | 6 |

Both worktrees were present and clean: no staged or unstaged changes, non-ignored untracked files, or ignored implementation candidates in the repository source/doc/test roots. HEADs and cached source remote refs match the known published heads. No extra unfinished local/unpublished source was found. This is a point-in-time observation, not a lock against later edits or a fresh remote publication check. Comparison bases are merge-bases with cached `origin/master`, not asserted historical initiative bases.

The raw NUL-delimited porcelain/index snapshots, index metadata/hash, binary-safe committed/staged/unstaged source diffs, exact commit inventory, and source file SHA-256/mode/mtime metadata are in each repository folder. `source/` contains hash-bound copies of the relevant implementation, documentation and tests. Final verification compares each snapshot and working file with its HEAD blob; see `final-verification.json`. Source metadata and Git state did not change during these checks.

Runtime scope includes `d328def7` bounded naming retry, naming docs and creation tests; adjacent source commits `5f922701` archive readiness diagnostics, `447aeda8` retirement cancellation preservation, and `529e075a` creation lock-refusal diagnostics remain explicit for architect disposition. The old dependency-only commit `6c963d70` and its `flake.nix`, `flake.lock`, `nix/workspace-portal.nix`, `portal/go.mod` and `portal/go.sum` bytes are excluded from candidate source diffs/copies; their path disposition remains recorded in the manifest. No old consumer pin is proposed for integration.

Client scope is the single `8010991` commit: native ephemeral retry ownership, private proof for safe fresh attempts, focused/native fixtures, reference text and request corpus. This intake makes no API design or integration decision.

Only source Git metadata/files in those two named worktrees and canonical objects were read. No source writes, index/ref changes, fetch/push, foreign team contact, lifecycle action, native process, test or build occurred. Credentials, runtime state, transcripts and unrelated session records/worktrees were not read. The old additive state test remains handed to owner0 and untouched.
