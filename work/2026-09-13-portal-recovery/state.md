---
lifecycle: active
---

# Portal recovery state

User approved implementation and deployment to aitherdev. No merge/archive/delete
authorization. New initiative: 2026-09-13-portal-recovery. No prior active session
belongs to this process (dev-session current failed; DEV_SESSION_SLUG unset).
Shared root is master with unrelated changes; preserve them.

## Repositories

All five use branch 2026-09-13-portal-recovery and worktree group
worktrees/2026-09-13-portal-recovery/: codex-web, dev-workspace,
vpsfree-dev-workspace, workspace, vpsfree-cz-configuration. Creation pending.

## Investigation

Browser source at codex-web ee9ab42 and dev-workspace 8a43d3b matches embedded
bytes in the running portal binary. Read-only Node probes executed extracted
production refresh code: a stuck read blocks five later triggers with status
still active; a rejected refresh schedules zero retries. Shared GETs have no
default browser deadline. Standalone mount listens for a ready event the server
does not emit and has no open handler. Heartbeats are SSE comments invisible to
JavaScript. Portal activity and connection status share one badge.

Repository history page size is 50. Pagination is unconditional. ReviewStats
and comparisonFiles already compute/caches net line totals. History has no
total count. Existing snapshots preserve comparisons after integration.

## Progress and next steps

Approved plan recorded. Commit initial tracking, start session, fetch upstream,
create/register worktrees, then implement. Verification/review/CI/deployment
pending. No changes to application code or deployment have been made.
