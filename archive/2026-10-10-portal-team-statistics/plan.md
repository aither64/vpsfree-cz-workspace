# 2026-10-10-portal-team-statistics

## Goal

Implement the accepted Team statistics and Codex-control plan. Show session-wide
conversation messages sent/received, tool calls and separate working, waiting
and idle time for the lead and retained team members. Make automatic waits clear
and allow model/effort choices during work, errors and execution holds.

## Affected repositories

- codex-web: aggregate activity metadata, automatic waits and compatibility.
- dev-workspace: member monitoring/statistics API and UI, durable held settings.
- workspace: composed runtime selection and the prerequisite instruction-size
  routing repair, preserving every existing rule; initiative documentation.
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

## Accepted compact-table follow-up

User requested implementation of the revised plan: fit the Team table at a
1280 px browser width with the ordinary sidebar. Separate Member, Activity, Sent,
Received, Tools, Working, Waiting, Idle, Model/reasoning and Actions columns. Place
roster/access metadata and abbreviated thread identity beneath Member; expose the
full ID by title and clipboard icon. Remove View messages and the Team transcript.
Use a popup settings editor for lead and ready members, bound to the clicked
member rather than Codex selection. Keep drafts across polling and uncertain
saves. Add-member role/model/reasoning share a desktop row, with an auto-width
button; small screens stack the controls.

Both reported sessions have native active status but unclassified recorder state.
Recover classification from fresh active/work evidence from the current connection
and turn. Record future coverage only, preserving unknown history and known waits.
An ambiguous unfinished turn says Turn in progress rather than inviting a prompt.
Existing activity and settings APIs and checkpoint formats remain compatible.
Keep native Codex unchanged, refresh composed selections, review the entire branch
series and redeploy aitherdev. No default-branch integration is authorized.


## Other team members working follow-up

Accepted on 2026-10-10: show a compact Codex-panel notice while the focused
member is idle or waiting. Include working, sleeping, waiting-for-team and
unclassified in-progress turns; exclude focused/removed/stopped/blocked members.
List three addresses then the remaining count. Preserve approval/answer requests,
replace idle waiting-for-instructions wording with Idle when others have ongoing
work, and suppress its attention dot. Existing team-stats API is shared with the
Team table every five visible seconds; stale observations after 15 seconds or a
failed read show unavailable status. No wire/persistence/provider change.

Tests cover member selection, automatic waits, blocked members, truncation,
completion, failed/delayed reads, page visibility, Chromium/Firefox and 1280/narrow
layouts. Update owning portal guide; quick checks, committed whole-branch review,
long browser/package/composition checks, then authorized aitherdev deployment.
Retain pins/provenance and branches; no default-branch integration authorization.
