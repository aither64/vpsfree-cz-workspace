# 2026-09-29-portal-performance

## Goal

Make the vpsFree.cz workspace portal usable on large, active conversations without repeatedly fetching and rendering full recent history or letting archive observation obstruct interaction. On aitherdev, the `2026-09-27-newadmin-integration` conversation should show recent messages and controls within two seconds at p95 across 30 browser loads, including during an archive scan. Older history must remain accessible on demand.

## Affected repositories

- `codex-web`: capability-checked paged transcript API and Codex App Server client.
- `dev-workspace`: portal browser, archive observation, activity refresh, diagnostics, and package pin.
- `vpsfree-dev-workspace`: pin the reviewed generic runtime for the complete site package.
- This coordination workspace: feature-worktree flake pin and rollout records.
- `vpsfree-cz-configuration` is not changed: aitherdev's NixOS host module is separate from the user-profile portal application.

## Approach

Start from the revisions in the currently selected workspace profile and preserve the one-way pin chain. The architect writes `design.md` with interfaces, invariants, failure handling, and verification before substantive edits. The implementer makes assigned application changes. The lead owns coordination, baseline and rollout. Keep the existing full transcript API for compatibility; add a bounded newest-100-item page with older-page cursors, browser incremental reconciliation, independent queue/pending recovery, and bounded activity refresh. Make passive auto-archive observation compatible with portal's shared session access, retaining exclusive locking and fresh revalidation for actual archival.

## Decisions

- User selected end-to-end portal scope and a live aitherdev rollout.
- Initial view is the newest 100 items with “Load older”; no history is discarded.
- Live acceptance target is p95 at or below two seconds for a usable recent view, not the full archive.
- No feature content enters any repository default branch without later, repository-specific integration direction.

## Compatibility and deployment

Keep persistent manifest, runtime authority, activity, and archive-journal formats unchanged. Preserve authorization on every paged request; browser input never selects a thread, socket, or directory. Old browser/server combinations retain the full `/thread` path, and a new browser must remain usable after profile rollback. Validate the selected Codex App Server 0.155.0 request/response protocol. Build and switch the complete package from this workspace's feature worktree via `workspace-host switch --source`; retain `workspace-host rollback` and the previous package generation. No NixOS host-module update or `confctl` deployment is planned. The site's application can run from feature revisions; deployment is not merge approval.

## Documentation

Explain paged conversation semantics in `codex-web`, portal UX and operational diagnostics in `dev-workspace`, and preserve individual baseline, rollout, and recovery evidence in this initiative. Do not copy site-specific paths into generic docs.

## Testing plan

Record before/after request size, latency, browser first-usable time, CPU, scan duration, and lock failures without saving conversation content. Cover long and active histories, pagination/reconnect/cursor failure, receipts and uploads, queue-reconcile failure, old/new browser-server mixtures, archive lock concurrency and fail-closed policy. Run focused checks and commits, then mandatory independent review before long Nix suites, CI, and live tests. Use a fresh Luna/low watcher for long verification. Roll back the profile if live acceptance fails.
