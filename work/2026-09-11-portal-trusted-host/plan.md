# 2026-09-11-portal-trusted-host

## Goal

Simplify the trusted development-host substrate and redesign the portal for a
persistent left navigation, a full-height conversation, a visible bottom composer,
message timestamps, reliable scrolling, and live repository/artifact updates.
Deploy reviewed feature revisions to aitherdev. Keep branches and the session open;
default-branch integration and archival are not part of this implementation.

## Affected repositories

- codex-web: optional transcript timestamps and reusable renderer formatting.
- dev-workspace: portal interface, live metadata, local trust-model instructions,
  host reconciliation and focused CI.
- vpsfree-dev-workspace: narrowly scoped local integration/migration guidance,
  migration CI scheduling, and generic runtime pin.
- workspace: organization package pin only; do not edit workspace-wide AGENTS.md.
- vpsfree-cz-configuration: aitherdev host-module pin through confctl.

Use branch/worktree group `2026-09-11-portal-trusted-host` throughout.

## Approach

### Instruction boundary

Instruction edits are limited to dev-workspace and local guidance in
vpsfree-dev-workspace. Do not change workspace-wide instructions, codex-web
instructions, configuration-repository instructions, shared review skills or
references, or unrelated repositories' policies. In dev-workspace, document that
the local operator is trusted with host administration; root/user ownership is
operational, not containment of that operator. Exclude defenses solely against
an already compromised operator's filesystem manipulation. Retain remote-input,
authentication, authorization, secrets, concurrency, data-integrity, recovery,
and rollback guarantees. Explicitly exclude the developed projects from this
trust assumption. Organization guidance applies only to workspace integration
and namespace migration, preserving KB approval rules and guest/host boundaries.

### Host and CI

Remove hostile ancestor/alias/bind-mount/hardlink/inode-substitution machinery.
Keep ordinary configured-path validation, final type/symlink checks, ownership,
flock, atomic updates, certificate validation, and interrupted-operation recovery.
Keep current ownership, weekly renewal, credentials, layouts, legacy PKI,
certificate generations and migration markers. No cleanup migration.
Replace the exhaustive attacker VM with an activation/idempotency/TLS/auth/
renewal/recovery/rollback smoke test; cover certificate and malformed-state cases
cheaply. Keep fast checks on every push and run organization migration VM on
relevant contract/migration changes or manual dispatch. Measure cold CI, target
under 20 minutes with VM acceleration; verify official action versions.

### Portal

Use a viewport-height shell with persistent vertical session navigation and
session identity/actions in the left sidebar. Keep current dark styling.
Compact visible icon rail on narrow screens; accessible labels, keyboard
navigation, existing section hash URLs and lifecycle dialogs. Session list only
on index, where archive starts collapsed and creation/operations appear right.
Update index membership in place without losing drafts.
Codex has a compact header containing All/Messages/Activity, a scrollable
transcript and a bottom composer. Composer appears only in Codex. Bound queue,
pending requests, and receipt status above the composer. Remove prominent
successful acceptance notices without changing durable receipt handling.
Explicitly follow after send/steer/implement/manual queue start; manual upward
scroll pauses following. Passive updates preserve reading position. Queueing
alone reveals the queue without forcing transcript navigation. Retain activity
disclosure and per-filter scroll state.
Add read-only session details usable without a Codex thread. Refresh curated
artifacts, repository discovery and counts every 15 seconds while visible, on
section activation and refocus. Reuse templates/status caching and preserve
artifact selection/preview position; keep existing content on refresh errors.

### Timestamps

Add optional `timestamp` (RFC3339) and `timestampApproximate` transcript fields.
Use item start, completion, or canonical record time from live lifecycle events
and the existing bounded rollout read; fallback to marked approximate turn time,
then Time unavailable. No new database, history cache or fork-lineage traversal.
Both renderers show muted local HH:mm, date separators, full local timestamp
tooltips and an approximation explanation; keep transcript order unchanged.

## Compatibility and deployment

No persisted schema/layout change; preserve existing credentials and rollback
generations. New transcript fields and session-details route are additive.
Remote-client and guest boundaries stay unchanged. This work does not require
coordinated vpsAdminOS node updates or database/client/daemon protocol migrations.
Commit and pin providers before consumers: codex-web -> dev-workspace ->
vpsfree-dev-workspace -> workspace package. Change aitherdev host-module pins
through confctl from its feature worktree. Use normal workspace-host transition,
NixOS dry activation then switch. Verify TLS/auth, portal/App Server, renewal and
profile/NixOS rollback compatibility. Deployment is already authorized.

## Testing plan

Focused Go/Ruby/JavaScript/protocol/Nix checks, timestamp fallback/stability,
durable send reconciliation, follow-state behavior and late repository/artifact
registration. Real browser checks on desktop, short laptop and narrow screens,
including queues, approvals, filters, archived sessions and index drafts.
All intended changes committed and quick checks passed before unchanged
mandatory-change-review workflow: high risk, applicable general/architecture/
scope/risk lanes, gpt-5.6-sol xhigh. Then long host/migration/package checks,
GitHub Actions feedback and authorized deployment. Apply writing skill to copy.
