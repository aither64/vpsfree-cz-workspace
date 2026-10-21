# Design and verification brief

Lead owns application changes (no retained roster). High-risk lifecycle/destructive-operation change; use all four independent review lanes after commits and quick checks.

Runner lifecycle request context scopes waiting to one slug/operation, including revive internal start and reacquisition. Existing non-lifecycle writers stay nonblocking. Acquire package transition, provider creation admission, creation lock, then exclusive slug lock. Wait only in lock acquisition; emit one waiting notice per blocked lock. Background automatic work remains nonblocking with a typed busy outcome and no persisted proof-failure diagnostic.

At request entry capture the tracking directory incarnation and retained root, or original journal/cleanup operation identity for recovery. A portal request uses its saved receipt target and operation identity. Under the first exclusive slug lock recheck target, current journal ownership and the exact portal authorization/attempt. Subsequent revive acquisitions recheck authorization and existing journal checks remain authoritative. Preserve generation locking and deadlines. Authorization callbacks are internal Ruby arguments; public CLI and persisted schemas remain unchanged.

Portal executeLifecycleOperation no longer takes the conversation mutation mutex before invoking the executor. The exclusive runtime lock already excludes all conversation mutations (which retain shared runtime lock until completion), preventing the existing mutex/runtime inversion. Existing target checks before launch remain; executor rechecks after waiting.

Archive waiting uses existing schema-1 archive progress keyed by its portal operation ID. Waiting is presentation, never journal evidence. Preserve independent supervised workers, duplicate receipt coalescing and restart reconciliation. No automatic whole-command retries.

Quick tests: runner concurrency fixtures use pipes/queues and owned temporary lock files; exercise creation/shared/exclusive contention, incarnation/root/journal replacement, resumed operations and revive reacquisition. Go regression holds the conversation mutex while executing lifecycle and verifies the executor proceeds and retains transition exclusion. Automatic busy scan leaves cached state byte-identical. Browser labels and VM cover waiting/archive/restart/roundtrip. Full package and session-archive-lifecycle VM run only after independent review.

Consumers: installed workspace-host dispatch; portal supervised archive and direct delete/revive; automatic archive; Ruby source tests; site composed runtime; aitherdev host module. No schema changes/migrations or Codex changes. Rollout exact published runtime through both consumer locks, matching contract check, coordinated system then profile activation. Recover forward, preserve roots and journals. User authorized deployment and original retained archive retry, not master integration.

User steering: successful archive must release its machine reservations. This
supersedes the previous retain-deployed-reservations lifecycle rule for archive.
Release at local archive completion atomically with the exact owner lifecycle
receipt, including idempotent completion replay of predecessor receipts. Keep
holds through incomplete cleanup and running/uncertain deployment recovery;
cancel queued jobs, retain deployment artifacts/history and do not reacquire on
revive. Deletion retains its prior semantics. No merge proof or review-finish
ceremony is required to release an explicitly archived session. Focused store
regressions pass (4 tests/19 assertions). Runtime coordinator docs own this policy.
