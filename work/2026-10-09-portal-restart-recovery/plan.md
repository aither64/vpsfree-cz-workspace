# 2026-10-09-portal-restart-recovery

## Goal

Restore portal sessions after host runtime loss while retaining their exact
Codex conversation and keeping all saved work dormant until the user acts.
User approved implementation and aitherdev deployment via configuration; never
reboot aitherdev. No default-branch integration is authorized.

## Affected repositories

- dev-workspace: durable recovery intent, canonical terminal recovery, portal
  coordinator, held-conversation boundaries, API, UI, tests and documentation.
- codex-web: minimal cold-thread activation and goal/queue primitives as needed.
- workspace: composed runtime selection in a dedicated feature worktree.
- vpsfree-cz-configuration: matching devWorkspace channel input and host rollout.
- vpsfree-dev-workspace extension remains selected at its existing revision.

## Approach

Persist exact session identity and automatic-restoration intent outside /run.
Automatically rebuild sessions previously running; expose Resume/Retry for
stopped sessions and failures. Restore terminal windows and runtime authority
without loading retained native threads. Cold history remains readable and the
composer remains usable. Hold root and team members against subscriptions,
background instruction reconciliation, settings fallbacks and CLI auto-resume.

Send records an idempotent native queue entry before activation. Continue loads
saved queue/goal work, or queues one explicit continuation prompt when neither
exists. Preserve native queue order and exact conversation identity. Portal-only
restart must retain already live threads without interrupting them.

## Decisions

- User selected automatic restoration plus a manual Resume button.
- User selected waiting for explicit action before interrupted work continues.
- User selected holding all saved work, including queues and active goals.
- Ordinary runtime authority and lifecycle journal schemas remain unchanged;
  private persistent recovery state carries intent and held status.
- Identity ambiguity and unfinished lifecycle operations fail visibly; transient
  app-server connectivity retries with bounded concurrency and backoff.
- No task replay, transcript reset, inferred ownership or real host reboot.

## Compatibility and deployment

Keep persisted manifests, retained thread IDs, native rollout history, team
rosters, queues and lifecycle journals compatible. Seed restore intent only from
exact verified live authority and terminal identity on first upgrade; existing
stopped sessions require manual action. Package transitions must preserve holds
and refuse a target that cannot honor pending recovery state. Configuration and
application use the same exact published runtime revision; install application
through the existing user profile, never through system configuration.

Publish feature branches, run independent committed-deliverable review after
quick checks, then long tests and builds. Build host configuration, dry-activate
and switch without reboot, then switch the composed workspace user profile.
Keep feature branches unmerged pending explicit repository/target approval.

## Documentation

Document cold restoration and explicit activation in generic runtime docs, the
supported upgrade/rollback boundary and repeatable operations. Store exact
rollout revisions and execution evidence here rather than in feature guidance.

## Testing plan

Quick unit checks cover durable identity, restart intent, cold gating, async
idempotency, request-loss retries and UI states. After final review, run complete
Nix checks and native fixtures with a mock inference provider proving zero
inference after runtime loss even with queues/goals. Verify original history,
queue ordering, team holds, exact authority, live portal-only restart, failed
identity isolation and explicit Send/Continue. Disposable fixtures may restart;
the real aitherdev host may not. Verify final composed deployment pins and live
service health using only an owned smoke session.
