---
lifecycle: active
---

# 2026-10-28-archive-observer-investigation

## Status

Investigation complete; final evidence record and handoff being reconciled.
Confirmed active native watcher rejection by the managed retry-admission guard.
No application code, target-session records, lifecycle receipts or agents changed.

- [x] Establish separate investigation identity and scope.
- [x] Locate exact archive worker error and failure stage.
- [x] Correlate native child identity, active interval and retained roster.
- [x] Trace source regression and inspect missing test coverage.
- [x] Propose bounded correction, regression cases and recovery approach.
- [ ] Finish tracking checkpoint and handoff.

## Next actions

Deliver findings. Future implementation should separate lifecycle stop authority
from managed turn admission, then test through the configured CLI client. The
affected archive remains unperformed by this investigation.

## Documentation

[findings.md](findings.md) contains evidence, source references and the proposal.
Reusable diagnosis: `notes/dev-workspace/2026-10-28-archive-active-native-watcher.md`.
No project documentation change: existing archive contract already promises
shutdown of proven native descendants. Routine investigation is exempt from
automatic independent change review.

## Repositories

No feature branch or registered worktree. Read-only source inspected at runtime
`4a002f52c3b55099540aa99708d5fcf29f7b2456`, used by the failing deployed package.

## Commands run

`dev-session current` initially reported no current session; both identity
variables were absent. After explicit creation, current matches the new slug
with both identity variables supplied. `team list` confirms there is no valid
lead thread for this deliberately threadless tracking session; no team adopted.
Read worker systemd journal, selected JSON metadata, target watcher session_meta
and task lifecycle events, source and tests. No tests or archive retries run.

## Results

Worker failed 2026-10-28 10:38:22 UTC (11:38:22 CET) with
`managed admission is outside the retained team`. Native watcher
`/root/master_ci_finish` was active until 11:54:23 UTC and absent from the retained
roster, as intended. `Interrupt` uses the managed retry resolver, which rejects
that native child. Tracking and all five checkouts remain; no archive journal,
cleanup sidecar or tracking-sync receipt exists for the target.

## Open questions

Whether a fresh archive attempt now succeeds has not been tested. The identified
watcher has finished, so this specific active-interruption trigger is gone; fresh
validation can still reveal another blocker.

## Cleanup

No lifecycle cleanup authorized or performed. Preserve the original browser
receipt, recovery hold and held prompts. Investigation session remains open.
