# Automatic session archival

## Goal and accepted policy

Implement and deploy an hourly auto-archive worker with CLI and portal controls.
Apply tiers in order: explicitly complete after 24 idle hours (complete archive),
active with all registered branches merged after 168 hours (complete archive),
active with no registered repositories and no owned worktrees after 336 hours
(abandoned archive). Already abandoned sessions remain manual. A persistent
Keep open hold overrides all tiers. Retained registrations prevent the empty
session tier even after physical worktree removal.

## Components and implementation

- dev-workspace: policy/observation storage, CLI scanner, existing archive runner
  integration, thread activity CLI, user timer, host lifecycle management, portal
  status/hold controls and tests/docs.
- vpsfree-dev-workspace: generic runtime dependency pin.
- workspace: standing policy authorization in AGENTS.md and consuming pin.
- vpsfree-cz-configuration: user authorizes aitherdev deployment if host changes
  prove necessary; the application itself remains in its existing user profile.

Store versioned policy, holds, observations and operation receipts outside the
workspace in host-owned persistent storage, bound to workspace/session identity.
Preserve existing manifest, authority and archive journal schemas. Reuse the
existing journaled archive, exact merge proofs, cleanup and recovery; never bypass
normal checks or adopt a manual pending operation. Recheck automatic eligibility
under transition and session locks. Resume only matching automatic operation IDs.
Use bounded external calls, sequential archive execution and per-session results.

CLI: dev-session auto-archive scan [--dry-run] [--json], enable/disable, and
hold/release SLUG [--as-is]. Dry runs do not update observation/policy state or
start lifecycle operations. Portal exposes current rule, earliest eligibility,
hold, blockers and last result through existing authenticated mutation patterns.

## Activity and defaults

Activity includes conversation changes, content changes to plan/state and
declared artifacts, registration changes and feature-head changes. Dirty
worktrees block archival; returning to clean resets inactivity. Ignore visits,
polling, timestamp-only writes, routine runtime metadata and unrelated upstream
default-branch advances. Observe content/identities rather than generic mtimes.
Persist observations through restarts. First enablement, re-enable, releasing a
hold and revival get fresh periods. Unknown or malformed activity, creation in
progress, active turns, queued messages and pending requests block new archives.
Enable only this workspace after dry-run inspection; defaults elsewhere disabled.
Disabling prevents new archives; already prepared journals retain normal recovery.

## Compatibility and deployment

No project APIs, database schemas, daemon protocols, container/node configuration
or coordinated node upgrades change. Old packages ignore the new sidecar state.
Manage new timer/worker through register, suspend, unregister, switch and rollback
so old generations cannot leave a new worker running. Existing journal schema
keeps interrupted archives recoverable by supported older packages.
Update generic runtime, extension pin, then consuming workspace pin. Deploy from
the initiative worktrees through workspace-host switch; use configuration branch
deployment only if host changes are required. Preserve branches and leave this
initiative open for follow-up. No session archive/delete requested for this work.

## Verification

Focused Ruby/Go/browser tests: exact 24/168/336-hour boundaries and precedence,
activity reset/noise, fresh periods, holds/revival/restarts, dirty/unmerged/missing
refs and retained registrations, empty sessions, unavailable Codex/queued input,
conflicting operations, races with holds/messages/branch changes/package switches,
crash recovery and unrelated shared changes. Commit and run mandatory high-risk
review in all four lanes (gpt-5.6-sol xhigh) before packaged/live integration.
Validate disposable sessions, timer lifecycle, upgrade and rollback. Inspect
branch GitHub Actions, dry-run deployed candidates, then enable fresh observation.

## Goal

## Affected repositories

## Approach

## Compatibility and deployment

## Testing plan
