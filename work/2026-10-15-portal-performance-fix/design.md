# Design and verification brief

Owner: initiating lead, xhigh. No retained team roster.

## Catalog

One workspace catalog shared by portal and interactive/observer clients.
Cache strictly validated records against device/inode, mode/owner, size, mtime
and ctime; validate before/after parsing, retry mixed reads, clone caller values.
Coalesce List discovery once per second; Find validates both roots directly.
Reverse thread ownership comes from current recovery records (lead and active
members). Admission checks selected current manifest, recovery, lifecycle and
socket epoch; missing, ambiguous or changed ownership denies. Coalesce discovery
on unknown lookup without reparsing unchanged records. Reuse loaded summaries.

## History and activity

Shared two-worker read-only history transport, one RPC per connection, no
subscriptions/resume/answers. Start item pages at 32; halve on size rejection to
one and retain safe sizes. Retry the same cursor. Keep 64 MiB individual-message
safeguards, cancellation and explicit local failure at one item. Owner closes it.

Use turn shells and item pages for exact counts. Cache/fold finalized aggregates;
refresh new/current items. Backfill is resumable, fair, incomplete until finished.
Remove total-turn and cumulative fork byte ceilings; preserve lineage, cursor
progress and timing uncertainty. Preserve legacy recent-transcript semantics.
Keep last successful activity value/time after failure. Optional stale/refreshing
flags; never generate fresh notifications from stale data. Retry 2–60 s with
jitter per thread. Browser stats preserve transcript usability.

## Compatibility and delivery

No persisted formats/migrations or native Codex change. In-memory caches rebuild,
JSON additions remain compatible. Preserve all authority and lifecycle contracts.
One final codex-web pin into runtime; matching runtime into workspace/config.
System before profile activation; verify native/tmux continuity and recover
forward under original attempts. Complete four master integration proofs and
explicit deployment/review completion before releasing the reservation.

## Checks

Quick Go/browser checks then committed whole-branch final review (general,
architecture, scope, risk/compatibility lanes; consolidated pins, no migrations).
After review run packaged/protocol/live checks and builds under policy watchers.
Test invalidation, replacement, duplicates, lifecycle/member/socket changes,
concurrent refresh, >64 MiB aggregate pages, >100k turns, fork/revert scope,
retries/cancellation and exact counts. Oversized items must not disconnect watches.
Verify history navigation, sends, approvals, team stats and notifications.
Live targets: <0.5 warmed portal core over five minutes, cached responses p95
<1 s, ten minutes without history-induced shared disconnects/503s.
