# Archive replacement test can race receipt reconciliation

`TestArchiveJournalRetryRefusesASameKindReplacementWhileWaitingForTheLock`
can fail when its single status read returns the original running receipt at
phase prepared after the journal has been replaced. This occurred in GitHub
Check run 37510298035 and in focused `go test -mod=readonly` repetitions inside
Nix: 7/100 failures on the cluster-decoder feature and 20/100 on its unchanged
installed baseline 4c3ea2e.

Starting a lifecycle retry also queues a full display refresh. The fresh status
reader and display refresher both reconcile receipts through compare-and-swap.
The source and failure output indicate that the refresher can change the
original receipt between capture and acceptance, causing the reader to discard
its replacement proposal and return the current original receipt. Execution
still checks journal identity after the mutation lock. No archive code was
changed in that initiative, and rerunning CI does not resolve this race.

Inspect receipt identity and phase before attributing this failure to unrelated
portal changes. The baseline experiment and explanation are retained in
[the investigation](../../work/2026-10-06-cluster-status-metadata/ci-investigation.md).
