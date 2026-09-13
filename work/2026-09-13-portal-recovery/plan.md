# Portal recovery and repository summaries

## Goal and authorization

Implement the approved plan and deploy both changes to aitherdev. The user
authorized deployment through the configuration feature branch and chose to
keep message controls usable during an outage. Repository totals match the
existing commit list and Compare view, including preserved comparisons after
integration. Default-branch integration, archival and session deletion are not
part of this request.

## Components

- codex-web: reusable browser synchronization, bounded reads, SSE readiness and
  heartbeats, mounted UI connection notice, browser and handler tests.
- dev-workspace: use synchronization in the portal, connection notice, optional
  repository pagination, full comparison totals and API/browser tests.
- vpsfree-dev-workspace and workspace: package dependency pins only.
- vpsfree-cz-configuration: matching devWorkspace host-module pin and aitherdev
  build/deployment from the initiative branch.

## Conversation recovery

Add a shared createConversationSync controller for stream management, refresh
scheduling, freshness state, explicit retry and cleanup. Bound each refresh
cycle to 35 seconds, propagate cancellation, release gates in finally, and
discard superseded responses. Preserve send/upload/lifecycle semantics and
existing receipt reconciliation. Include queue reconciliation in the refresh
bound without replaying composer text or user actions.

Refresh on stream opening, window focus, visibility, pageshow, and online
events. Coalesce simultaneous triggers; after sleep replace stale requests and
connections. Emit named ready and heartbeat SSE events, retaining update
messages. Heartbeats every 20 seconds, watchdog every 5 seconds, stale after
45 seconds. Retry with exponential backoff from 1 to 30 seconds with jitter.
Refresh full snapshots every 60 seconds while visible, suspend periodic reads
while hidden, and refresh on return. Enable heartbeat enforcement only after
the server advertises it so old servers remain usable.

Show connection health separately from activity status, with an accessible
persistent warning, last successful refresh time and Retry now button. A stream
opening alone does not clear failed synchronization. Distinguish network errors
from HTTP/auth/service failures. Preserve content, drafts, attachments, answers
and scroll position. Keep message controls usable.

## Repository summaries

Show pagination only for page > 0 or hasMore, retaining Previous on the last
page. Above the commit list show the total commit count and existing formatted
ReviewStats (changed files, additions, deletions, and binary files if any).
Count the entire base..head range, including unpushed commits. Diffstats are the
net tree difference, not a sum of individual commits.

Extend single and batched history responses with an optional summary containing
commitCount and ReviewStats; expose an error when unavailable without losing
usable history or reporting missing counts as zero. Reuse comparisonFiles and
cache by canonical repository and immutable base/head. Keep pagination, totals,
base labels and head-change warnings tied to the same snapshot. Refresh commits
updates them together. Preserve existing Git resource limits.

## Compatibility and deployment

The SSE events and response fields are additive; older clients ignore them,
newer clients tolerate their absence. No persisted-state, comparison-record,
database, submission-receipt, App Server protocol or Nix option changes. No
coordinated node update. Rollback needs no migration and older packages can load
all state. Existing tabs need one reload to acquire the improved JavaScript.

Propagate pushed provider revisions through runtime, organization and workspace
packages. Pin configuration with confctl inputs channel set --commit
dev-workspace devWorkspace <runtime-revision>. Check deployment contract, build
application and cz.vpsfree/machines/aitherdev, dry-activate, and complete CI.
Record previous generations, activate the user-profile application using
workspace-host switch --source <workspace-feature-worktree>, then confctl switch
from the configuration feature worktree. Restore recorded generations if
deployment validation fails. Keep application deployment in the user profile.

## Verification

Quick Go/browser checks then committed mandatory review (all applicable lanes,
gpt-5.6-sol xhigh) before long integration acceptance. Test permanently stalled
reads, failed reads followed by silence, heartbeat loss, closed streams, races,
wake events, late replies, disposal, old servers and no duplicate submissions.
Test repository sizes 0, 1, 50, 51, 101; full totals, cancelling changes, renames,
binary files, unpushed/rebased/integrated comparisons, batch equivalence, summary
failure, and narrow layout. Browser acceptance in Firefox and Chromium includes
offline and silent stalls, missed final reply, preserved composer/answers/scroll.
After activation verify authenticated pages/assets, SSE recovery and summaries.
