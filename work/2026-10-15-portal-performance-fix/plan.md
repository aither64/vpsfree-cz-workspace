# Portal CPU and long-conversation fix

Implement the approved plan. Baseline: ../2026-10-15-portal-cpu-investigation/findings.md.

## Scope and authorization

codex-web: bounded history transport and incremental activity.
dev-workspace: shared validated session catalog, direct resume admission, freshness.
workspace: nested runtime pin. vpsfree-cz-configuration: matching channel and aitherdev.
The user directed "you can deploy aitherdev using vpsfree-cz-configuration, merge
the fix and release", clarified release means the machine reservation, then said
"Implement the plan." Targets: refs/heads/master in all four repositories.
Deploy system then user profile, verify and release via coordinator finish.
No tags, GitHub releases, reboot, archive or deletion. User chose existing Codex
APIs and individual-message safeguards; no Codex fork or enormous-item support.

## Approach

Share validated file records, coalesced discovery and reverse thread ownership;
remove full workspace scans per resume and redundant summary reads.
Turn shells plus item pages replace full-turn activity reads. Incremental
aggregates/backfill avoid total conversation byte/turn ceilings. Separate bounded
history connections from live watches, adapt page size and back off failed reads.
Retain last good snapshots as stale; never silently truncate history/counts.

## Compatibility and deployment

No persistent schema/migration or native Codex 0.160.0 changes. Caches rebuild;
freshness JSON fields are additive. Preserve exact origin, capability, private
file, runtime authority, lifecycle, recovery, team and socket epoch checks.
Commit/quick-check, final independent branch review, then longer verification.
Publish and integrate exact final heads through coordinator. Configuration system
activation precedes matching user-profile application. Forward recovery retains
original attempts, artifacts and machine ownership until outcomes are proved.

## Documentation and verification

Owning project docs cover paging/backfill/freshness; rollout evidence stays here.
Test invalidation/ownership races, forks, long histories, oversized pages,
cancellation/retry/count accuracy, live sends/approvals and notifications.
Use fresh Luna/low watchers for long checks. Acceptance targets: <0.5 warmed
portal core averaged five minutes; cached activity/display p95 <1 second;
ten minutes without history-induced shared disconnects/503s. Prove every exact
final head integrated before releasing the aitherdev machine reservation.
