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
