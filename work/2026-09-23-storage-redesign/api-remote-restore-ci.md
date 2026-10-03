# API46 remote restore CI failure

Run `37030949481` at API `46b3bf6f9549eaf579053bc296ebf19c417bb848`
completed with 117/118 tests passing. The sole failed script was
`storage/restore-after-reinstall-remote`. Its first two examples passed;
remote rollback then timed out after 900s and its dependent snapshot creation
returned 423 Locked. No unchanged rerun has been requested.

Implementer0 independently inspected the failed disposable fixture and public
source, without edits/tests/operations. Node2 ran chain9 transaction40/handle5221
ZFS send at 23:16:03 +0200. At 23:16:28 its StorageStatus updater raised
Timeout::Error during Bunny queue-delete continuation in RpcClient#close.
Thread.abort_on_exception caused daemon exit; the daemon restarted at23:16:30.
Node1's receive child completed and the temporary rollback dataset/snapshot
existed, but transaction40 never persisted completion. Receive-check and
apply-rollback remained waiting. Chain9 stayed queued/progress2 with VPS and
both DIPs locked. The later 423 follows the retained ResourceLock; it is not
freeze/strict admission evidence. A NULL started_at does not disprove execution:
the command persists timing only after completion.

The fixture sets zero send/receive startup delays through an in-memory remote
Config patch. Restart reloads the ordinary 90-minute defaults, exceeding the
15-minute test wait. This explains the delayed recovery from public source;
there is no failure-time post-restart queue dump. The acknowledgement-timeout
trigger remains unknown, and ensure cleanup may have masked an earlier RPC
body exception. The artifact lacks broker journal/mbuffer/thread diagnostics.
Earlier startup authentication errors are not established as the trigger.

RpcClient, StorageStatus, NodeBunny, send/receive, daemon CLI and fixture files
match upstream `878a0d10c`. The feature adds inventory queue/zpool configuration,
without changing these startup defaults. No evidence attributes the failure to
storage selectors, scheduler, provider or workspace rebase.

A separate bounded Node reliability follow-up should cover queue-delete timeout,
channel retirement/recovery and telemetry error isolation while preserving real
RPC errors. A persistent test-only zero-delay configuration can avoid restart
amplification; it cannot fix the daemon crash. After correction, rerun only this
scenario with broker/worker diagnostics. Never manually unlock the stalled
chain or treat a blind green rerun as evidence.

This limits storage readiness. The workspace composition's default API5c76 and
disabled storage profile are unchanged, so it does not block the separate
workspace rebase/package verification. Full storage acceptance remains pending.

Private evidence (no credentials copied):
`/tmp/storage-profile-api-broad-failure.a6echyos/failed.log` and
`/tmp/storage-profile-broad-artifact.fw6suvvl/artifacts/os-test-storage__restore-after-reinstall-remote-7dc51c6b`.
Relevant locations: node2-shell.log499,504-541; node1-shell.log862;
services-shell.log4027-4029; public RpcClient#close29-31, StorageStatus#run_updater
75-85, nodectld CLI177, remote-common.nix63-69.
