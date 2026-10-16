# Integration refresh over a large tracking baseline

The selected 0.2.0 runtime integration driver stopped during preparation of
2026-10-16-update-codex with `recipe output exceeds protocol limit`. Ten shared
tracking commits had moved/updated 10,836 paths under work/, archive/ and notes/.
The installed workspace-pins recipe captures `git diff --name-only FROM TO`
through a 262,144-byte bound, so it cannot verify this large baseline difference.
No merge jobs had been submitted by that run.

Recovery used ordinary coordinator prepare/approve/submit commands. The workspace
feature was rebased in its own clean worktree; its complete feature diff remained
byte-identical, both ordered range-diff entries matched, and a retained independent
reviewer checked the exact deployed/final ranges for patch_equivalent release
lineage. Unchanged project snapshots and approvals were reused. Keep the failed
preparation journal and original sources; do not edit the ledger or resume the
superseded run after recovering separately. Record final job and release receipts
in the session. The package protocol limit itself was not changed.

Related evidence: work/2026-10-16-update-codex/workspace-rebase-verification.json,
workspace-rebase-review-report.md, and integration-completion.json.
