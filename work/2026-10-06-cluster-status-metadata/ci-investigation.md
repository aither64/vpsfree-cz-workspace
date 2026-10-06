# Archive-test CI failure

Runtime feature e3315a483f3d3536d492ecbe40f2655449cf630f passed its full local
`nix flake check --no-update-lock-file --print-build-logs` operation. GitHub
[Check 37510298035](https://github.com/aither64/dev-workspace/actions/runs/37510298035)
failed in `TestArchiveJournalRetryRefusesASameKindReplacementWhileWaitingForTheLock`
at server_test.go:3665. The assertion expected replacement journal B's paused
receipt, but read journal A's running receipt with phase prepared. The full
failed CI log is runtime-ci.log.

The cluster change touches only cluster/status.go, cluster/status_test.go and
docs/workspace-portal.md. `git diff 4c3ea2e e3315a4 -- portal/internal/web`
is empty. The failing test does not exercise the cluster decoder. Repeating
this exact test 100 times in the repository Nix environment produced seven
failures on the feature in 3.152 seconds. Repeating it against the installed
baseline source 4c3ea2eb3b82b572e86f23ec7f9e53a0f1dc6a0c produced twenty
failures in 3.745 seconds; see archive-baseline-test.log and its exit artifact.

The source explains the observed race. Starting the retry queues a full display
refresh. The test replaces the journal and makes one fresh status call.
`lifecycleOperationForSlug` captures the current receipt, reads the journal,
then accepts reconciliation only if the receipt is still unchanged. A concurrent
display refresh can update A from starting to prepared between capture and
acceptance. The compare-and-swap discards the caller's proposal and returns the
now-current A receipt, which the test immediately rejects. This explanation is
inferred from the code and the matching receipt printed by every captured
failure. Execution separately rechecks journal identity and immutable evidence
after acquiring the mutation lock, before invoking dev-session.

The existing archive-status race is outside this decoder fix. Do not interpret
a successful CI rerun as fixing it. The reproduced baseline failure and unchanged
archive sources allow a rerun to supply verification for the reviewed decoder
patch without attributing this archive failure to that patch.
