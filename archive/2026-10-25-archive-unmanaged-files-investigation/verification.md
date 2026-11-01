# Archive preparation verification

Final source head: `5e4e99dfecfda94da47c10cd154dfa98269a6533`.
Base: `9634151b9836311c331a58880fbb4c46133fd98f`.
No deployment or master integration occurred.

## Accepted evidence

- Focused Ruby archive batch: 13 tests / 375 assertions passed. Readiness,
  read-only authority and parent permissions: 6 tests / 104 assertions passed.
- Focused Go preparation/native identity tests passed; the latest CLI/native
  regression run passed (command 0.062s, teamruntime 2.048s).
- Full aggregate Ruby checks proved complete unique shard coverage. The final
  package built and passed Go, browser contract, native/protocol and packaging
  prerequisites. CI fast job passed on the final head.
- [CI run 40215486144](https://github.com/aither64/dev-workspace/actions/runs/40215486144)
  archive job passed. VM derivation:
  `/nix/store/r8ihzf3w880nbbllsjpxymy3zi395bp9-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
  Test script: 498.14s. The external Responses provider is synthetic; the portal,
  browser, Ruby CLI, systemd worker and native App Server are shipped components.
  Native shell cleanup, held inference across restart, unrelated creation,
  archive/revive, lock contention, worker interruption, preflight permissions,
  post-removal journal recovery and offline tracking sync all passed.
  Full local log: `ci-5e4e99df-archive-passed.log`.
- Older-reader VM passed, exit 0, test script 402.31s. It ran the installed
  predecessor portal binary against a candidate's parked receipt, proved the
  original receipt/attempt and retryable failure, then resumed the candidate
  and completed the same native repair/archive request. The selected package
  and native server did not change. This isolates receipt compatibility rather
  than claiming a complete host rollback. Log: `compatibility-check.log`;
  reproducible ad hoc fixture: `prepare-compatibility-vm.py`,
  `compatibility-session-archive.nix`, `compatibility-check.nix`.
- Final tree clean, `git diff --check` passed, remote exact-head proof and fresh
  upstream fetch passed, and the saved comparison binds the final base/head.

## Diagnosed failures and scope

Local packaged batch 5 used the exact archive VM derivation that passed in CI,
but its browser hydration exceeded the existing 30s response wait before any
archive POST. Captured page/assets/API responses were HTTP 200 with no JavaScript
errors. The compatibility run used a private copy of the same browser driver
with a 120s deadline and passed native cleanup/archival locally. The production
browser driver and shipped app are unchanged by this deadline adjustment.
Evidence remains in `packaged-checks-5.log`.

Earlier failed batches exposed and led to fixes for a missing module in the
Ruby package-layout test fixture, a missing readiness response in an existing Go
command double, an absent generic-package managed preset in the VM fixture and
a real missing-roster result case in the new native CLI helper. Details and
exact historical heads/logs are in implementation-history.md. No failed run was
accepted as evidence of success or retried without inspecting its failure.

Creation CI first attempt failed on its existing fallback-name collision test:
`session is changing: resource temporarily unavailable`. The unchanged creation
installer failed its nonblocking destination runtime exclusive lock. A reader
of the previous fallback session is a plausible competing holder; the job did
not identify the exact holder. No archive preparation exists in
that suite. Logs were inspected before rerunning only that failed job.
Evidence: `ci-5e4e99df-failed.log`. Attempt 2 failed earlier, creating an
approved-plan destination: `initialize session: error: another dev-session
command is changing 2026-10-25-explicit`. Its source-lock path is unchanged and
no archive preparation was active. Evidence: `ci-5e4e99df-attempt2-failed.log`.
Both failures were inspected. No further blind rerun was requested. The exact
competing lock holder is unresolved; baseline CI runs 40204833852 and 40191223335
passed, so pre-existence is inferred from unchanged inactive archive paths,
not a reproduced failing baseline. Whole-suite CI remains red and deployment
readiness is not claimed. The archive-specific acceptance is successful.

There are no owned running local runners or guests. Nix test drivers performed
normal guest cleanup. Raw logs/generated ad hoc fixtures stay local and untracked;
Markdown records retain compact evidence and the relevant conclusions.

## Creation contention follow-up (supersedes the earlier unresolved assessment)

The user requested root-cause fixes for both CI failures. Deterministic real
Go/Ruby regressions reproduce both messages with an identified normal portal
queue/reconcile SH holder. The plan subprocess proves the same device/inode as
that holder. The two independent causes and fixes are documented in
creation-contention-findings.md. The original CI holder PIDs remain unavailable;
this is causal reproduction, not retrospective PID attribution.

Fix commits a27fd38e and b974f2f3 follow the two reviewed archive commits. New
regressions pass, including exact custom-name collision, suffix/replay identity,
plan wait/replacement/cancellation and real journal recovery without the source.
Related Go preparation/fork/plan tests pass in 12.803s; 9 Ruby source/binding and
recovery regressions pass with 117 assertions. Independent review is clear in
creation-contention-review.md after all intended changes were committed. It
independently reran the new tests (web 3.091s) and those Ruby regressions.

Fresh CI run 40223710351 covers head
b974f2f3f83792a494610d1ea03f3d69e97bc1a4. It builds fast/package checks and runs
packaged creation/archive native VMs. It completed successfully on attempt 1: creation, archive and fast jobs passed; the standard master/manual-only host job was skipped. Prior passing
archive/older-reader checks remain evidence for 5e4e99df, not a substitute for
final-head acceptance. No schema or protocol changed in the contention fixes.

## Final acceptance result

CI run 40223710351 completed successfully at the exact final head
b974f2f3f83792a494610d1ea03f3d69e97bc1a4 on its first attempt. Packaged creation,
archive and fast/package checks all passed. Creation job 121260557495, archive
job 121260557803, fast job 121260557763. The host VM job was skipped under its
normal master/manual guard. No failed job was rerun for this final head.

The fresh watcher returned pass, exit 0, after 1226.2 seconds. Raw status and
exact job conclusions are retained locally in creation-contention-ci-result.json;
creation-contention-ci-watch.log/status preserve observation. The reviewer and
watcher both completed without edits to source or new deployments. Source tree
cleanliness, full-range whitespace and exact remote head proof passed.

Earlier failed CI attempts remain historical evidence of the now reproduced and
fixed causes; they do not describe final readiness. No verification remains
running. Integration and deployment are still pending explicit direction.

## Authorized deployment verification (2026-10-25)

See rollout.md for exact system/profile artifacts, ownership, commands and recovery.
Downstream final independent review (deployment-review.md) found no Blocking or
Important issues; its documentation pointer advisory was corrected. Complete
one-pin histories accepted, with no repeated streams, obsolete history or migrations.

Final configuration/workspace builds and deployment-contract check passed in
672.5s. Compatibility preparation passed before machine acquisition. Both
activation commands returned 0; exact live system/profile/application identities
matched the prepared artifacts. Configured systemd/firewall health checks passed.
Portal health/index/Operations/session pages and native model endpoint returned
200. Codex/tmux PIDs were preserved. Live isolated Luna/low naming passed in 2139ms.

Selected-package disposable archive acceptance passed (100.0s): ready 6/6,
one unmanaged marker blocker with terminal preserved and Operations HTTP 200,
ready 6/6 after exact fixture cleanup, then portal archive complete on attempt 1
and terminal retired. Fixture tracking-sync status later confirmed synced/no error.
No live lead was created; retained-lead repair/restart coverage is the passed
final-head packaged CI. See deployment-archive-watcher.md and compact JSON evidence.
All watcher/native policies were confirmed from actual launch metadata.
Temporary build links removed after selection, no guest started and no owned
verification operation remains. Machine claim is intentionally retained because
feature lineage is unmerged; deployment is complete and does not grant merge approval.
