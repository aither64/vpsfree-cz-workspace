# 2026-10-10-portal-team-statistics

## Goal

Implement the accepted Team statistics and Codex-control plan. Show session-wide
conversation messages sent/received, tool calls and separate working, waiting
and idle time for the lead and retained team members. Make automatic waits clear
and allow model/effort choices during work, errors and execution holds.

## Affected repositories

- codex-web: aggregate activity metadata, automatic waits and compatibility.
- dev-workspace: member monitoring/statistics API and UI, durable held settings.
- workspace: composed runtime selection and documentation of this initiative.
- vpsfree-cz-configuration: matching dev-workspace channel and aitherdev deployment.

## Approach

Extend existing observer/recorder rather than create a second timing service.
Preserve latest-turn counts and add aggregate conversation counts. Count distinct
user/assistant/plan items and issuing-thread tools; paginate all own history.
Observe ready members independently of browser connections. Expose a dedicated
team-stats endpoint, separate from roster forms, with independent member errors.

Use item lifecycle evidence for sleep and subagent waiting, retaining blocking
user-input/approval distinctions. Idle covers gaps between turns, including the
period before a first assignment. Never assume unobserved turn time is work.

Remove busy/idle gates from model and effort editing, but retain existing gates
for collaboration-mode changes. Native updates apply to subsequent turns. Held
choices persist without native activation and apply during explicit activation.
Serialize changes, preserve member roster settings, and reconcile uncertain saves.

## Decisions

- User selected conversation messages, separate waiting, and session totals.
- User explicitly selected saving model choices during stopped/restart-held states.
- Include lead and retained members; do not invent persistent members for native
  utility subagents. Retain removed-member statistics.
- Do not change the native Codex package/version for this feature.
- User authorized implementation and deployment, but no default-branch integration.

## Compatibility and deployment

Keep API additions optional and existing latest-turn semantics intact. Preserve
session manifests, lifecycle journals, recovery records and submission receipts.
New telemetry/deferred-setting records are private, identity-bound and versioned.
Old records remain readable; absent historical evidence is explicitly partial.
No database or service wire migration is planned. Fork statistics exclude inherited
history. Existing forward-only package switching remains the recovery contract.

Publish exact feature heads and update codex-web -> dev-workspace -> composed
workspace/configuration selections. Keep the extension input unchanged. Check
composition with bin/check-dev-workspace-deployment. Deploy aitherdev host substrate
through confctl from the configuration feature branch, then select the application
from its user profile. Prefer the supported live package switch, preserving active
turns and recovery holds. Do not archive this initiative or merge default branches.

## Documentation

Readers: portal users, library consumers and operators. Update codex-web technical
reference and dev-workspace portal/session documentation for totals, wait reasons,
held settings and compatibility. Keep exact rollout details here in rollout.md.
Apply the main-agent user-facing writing workflow before committing interface copy.

## Testing plan

Use each repository's Nix tools. Cover historical pagination/deduplication, forks,
unused/removed members, sleep/subagent/user waits, overlaps and missing coverage.
Cover model saves during active/error/held states, newest-choice precedence,
uncertain outcomes, restarts and explicit activation before resumed work. Cover
API ownership, independent failures and browser draft/staleness behavior. Run quick
checks, commit all intended changes, inventory history, and obtain independent
mandatory review before long package/integration checks and deployment. Long checks
are owned by a fresh utility watcher. Record exact results and deployment evidence.
