# 2026-10-16-session-archive-local-first

## Goal

Implement the accepted archive reliability plan and deploy it to aitherdev.
Manual archival must finish locally after preserving recoverable work, with Git
tracking bookkeeping retried independently. Pending bookkeeping coalesces to
the latest tracking state when the session is revived.

## Affected repositories

- dev-workspace: recovery storage, cleanup, tracking synchronization, supervised
  lifecycle execution, CLI/portal status, contracts, tests and documentation.
- workspace: composed runtime selection and lifecycle/deployment instructions.
- vpsfree-cz-configuration: matching dev-workspace channel and aitherdev system.

## Approach

First resume the user's existing interrupted archive through its installed CLI,
without the portal deadline. Preserve its operation and recovery data. Develop
in dedicated feature worktrees. Use Git-backed clean checkout recovery, batch
retained object refs, target-specific content checks, durable background archive
execution, and a separate retryable tracking-sync queue. Keep normal ownership,
snapshot integrity, hooks and shared-index protections.

## Decisions

- User selected local closure before tracking Git commit success.
- User selected latest-state coalescing rather than separate commits for pending
  archive/revive transitions.
- User directed implementation and deployment through
  vpsfree-cz-configuration. This does not authorize default-branch integration.
- This thread created its own threadless initiative using --no-codex; it has no
  retained team roster. Lead owns design and implementation. Mandatory review
  uses the installed catalog fallback; long verification uses the site utility.

## Compatibility and deployment

Retain supported existing archive/revive journals, full snapshots, conversation
identity, cluster ownership and held coordination reservations. New recovery and
local-completion formats need explicit capability contracts and package guards.
Automatic archive eligibility and merge proofs remain. No database migration or
vpsAdminOS fleet update is intended. Recover forward; do not reset journals.
Prepare matching workspace composition and configuration channel pins, verify
them, then activate system before application profile under vpsfree:aitherdev.

## Documentation

Operators and maintainers need archive/revival, tracking-sync, interruption and
upgrade semantics in dev-workspace docs. Site rollout belongs in this session;
repeatable aitherdev operations belong in configuration docs. Keep workspace
instructions consistent with local closure semantics.

## Testing plan

Quick Ruby/Go/browser contract checks before committed independent review;
longer package, interruption, recovery, scale and deployment acceptance after
review. Test large clean checkouts, dirty/index/untracked/ignored recovery,
network/hook/master failures, revival during pending sync, interruption and
generation compatibility. Do not drop or curate the original session artifacts.
