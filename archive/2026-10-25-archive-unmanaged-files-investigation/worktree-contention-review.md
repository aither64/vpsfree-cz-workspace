**No Blocking, Important or Advisory findings.** The follow-up may proceed to the planned packaged archive/CI verification.

Reviewed the complete unmerged range from `b974f2f3f83792a494610d1ea03f3d69e97bc1a4` through `b75a6a1065449743b6a3c2f859b44bc32fefdc40`, including both commits, final diff, documentation and failure evidence. All four review lanes applied at high risk.

The locking change is bounded and correct. [dev-session:2675](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace/libexec/dev-session:2675) enables the new behavior only for worktree registration. After failed EX/NB admission, a successful SH/NB probe permits waiting for EX; a stable exclusive holder retains the existing busy refusal. Other callers retain their defaults.

The probe samples lock compatibility, rather than establishing holder identity. Linux flock conversion releases SH while waiting for EX, allowing competing upgraders to progress. Another writer can intervene before EX acquisition, so validation must occur afterward. The implementation preserves that ordering, including provider admission, lifecycle checks, current authority selection, manifest validation and Git mutations. It introduces no new lock-order dependency, persisted authority or generic retry framework.

The native fixture correction in [codex_runtime_test.rb:296](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace/test/dev_session/codex_runtime_test.rb:296) correctly establishes explicit threadless tracking before starting a fixture that already contains a checkout. Production refusal of manifestless retained state remains unchanged. Its separate commit is appropriate because the corrected baseline test reproduces the pre-existing fixture error.

The evidence establishes a reproducible reader-contention defect and its correction: actual portal queue/reconcile SH admission causes the pre-fix busy error; the fixed path waits on the same device/inode, leaves the checkout absent before EX, permits unrelated registration and completes real Git checkout creation after release. It does **not** identify the historical CI holder or explain the separate portal shutdown timeout.

Independent quick verification passed in the repository Nix environment:

- New Go/Ruby boundary regression: **web 1.623 seconds**, including writer refusal.
- Focused Ruby worktree, observation, writer and native tmux tests: **10 tests, 178 assertions**, no failures, errors or skips.
- Disposable probe through the real helper: two simultaneous shared-probe upgraders completed.
- Full-range whitespace check passed; worktree remained clean.

The trusted-local-operator boundary remains unchanged. Remote validation and authorization are unaffected. CLI syntax, lock paths, receipts, journals, protocols and package contracts remain compatible. The existing helper owns the mechanism, and the worktree guide documents its supported behavior proportionately.

The complete new series is:

1. `2a58cf4937d035dd8688aaae92d9e997c3efdb63` — bounded registration fix, documentation and boundary regression.
2. `b75a6a1065449743b6a3c2f859b44bc32fefdc40` — independent native fixture correction.

**No obsolete unmerged approaches or redundant fixup history remain. No repeated dependency, input or generated-update streams exist. No migrations or transitional migrations.** No further consolidation is required. The previously merged, deployed and consumed four-commit history must remain intact.

Packaged verification on this follow-up remains outstanding. The portal shutdown timeout remains unresolved, and this report does not establish CI or deployment completion. The selected profile still resolves to the previously verified `bhi44p5i…` artifact; this follow-up has not been selected.

Review performed directly and read-only under the retained `gpt-6.1-sol` / `xhigh` assignment, without nested agents, source edits, long checks, deployment or merges.