# 2026-10-19-session-archive-refresh-fix

## Goal

Repair explicit and automatic archival of uncommitted session tracking, preserve
unchanged index DOM during refresh, deploy on aitherdev and retry the failed
archive of 2026-09-22-team-test-2 (tracking files have no prior commit).

## Affected repositories

- dev-workspace: lifecycle validation, portal reconciliation and regressions.
- workspace: matching nested runtime selection.
- vpsfree-cz-configuration: matching dev-workspace channel and aitherdev activation.

## Approach

Remove committed-history requirements for local-first archive operations in
preflight and finalization; preserve old synchronous journals and all ownership,
integrity, inactivity, hold, cleanliness and merge proofs. Reuse keyed operation
rows and session cards, updating only changed displayed values and order. User
explicitly wants live updates without replacing identical elements, with no
selection-based refresh pause. See design.md for implementation and verification.

## Decisions

## Compatibility and deployment

No API, CLI, database, protocol, manifest, journal or receipt schema changes.
Existing tracking receipts retain archive/revival proofs. Old synchronous
operations keep their commit prerequisite. New and old browsers use the same API.
Deploy matching configuration host contract then workspace application profile
under coordinator ownership, without reboot. Recovery is forward-only. No fleet
or node update. Feature/default integration requires separate user direction.

## Documentation

Update runtime archive recovery guidance for operators and lifecycle maintainers;
keep exact rollout evidence and transient checks in this initiative.

## Testing plan

Regression coverage for uncommitted and partial tracking, all automatic tiers,
interruption/retry, sync failure/recovery, revival and unchanged shared Git state.
Real Chromium/Firefox selection and DOM identity tests across full/progress index
refresh and neighboring changes. Quick checks, committed independent review,
then packaged lifecycle/browser tests and coordinated deployment acceptance.
