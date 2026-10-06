# 2026-09-29-portal-performance

## Goal

Make the vpsFree.cz workspace portal usable on large, active conversations without repeatedly fetching and rendering full recent history or letting archive observation obstruct interaction. On aitherdev, the `2026-09-27-newadmin-integration` conversation should show recent messages and controls within two seconds at p95 across 30 browser loads, including during an archive scan. Older history must remain accessible on demand.

## Affected repositories

- `codex-web`: capability-checked paged transcript API and Codex App Server client.
- `dev-workspace`: portal browser, archive observation, activity refresh, diagnostics, and package pin.
- `vpsfree-dev-workspace`: pin the reviewed generic runtime for the complete site package.
- This coordination workspace: feature-worktree flake pin and rollout records.
- `vpsfree-cz-configuration`: pin the reviewed host module and set the aitherdev-only bcrypt cost used by system-owned portal authentication.

## Approach

Start from the revisions in the currently selected workspace profile and preserve the one-way pin chain. The architect writes `design.md` with interfaces, invariants, failure handling, and verification before substantive edits. The implementer makes assigned application changes. The lead owns coordination, baseline and rollout. Keep the existing recent-20-full-turn `/thread` API for compatibility; add a bounded newest-100-item page with older-page cursors, browser incremental reconciliation, independent queue/pending recovery, and bounded activity refresh. Make passive auto-archive observation compatible with portal's shared session access, retaining exclusive locking and fresh revalidation for actual archival. After the deployed paging path passes functionally but misses the latency gate, expose a bounded host-module bcrypt-cost option with the generic default unchanged at 12 and set cost 5 only for aitherdev's generated 256-bit random workspace credential.

## Decisions

- User selected end-to-end portal scope and a live aitherdev rollout.
- Initial view is the newest 100 items with “Load older”; no history is discarded.
- Live acceptance target is p95 at or below two seconds for a usable recent view, not the full archive.
- The user authorized integration of the final reviewed feature heads into their repositories' default branches after all remaining verification, deployment, live-acceptance and whole-history gates pass.

## Compatibility and deployment

Keep persistent manifest, runtime authority, activity, archive-journal, database, protocol and session formats unchanged. Preserve authorization on every paged request; browser input never selects a thread, socket, or directory. Old browser/server combinations retain the legacy `/thread` path, and a new browser falls back to it only when paging is explicitly unsupported. Validate the selected Codex App Server 0.155.0 request/response protocol. Build and switch the complete package from this workspace's feature worktree via `workspace-host switch --source`. The host intentionally rejects earlier-profile `workspace-host rollback` because team registration is forward-only; recovery requires a newer forward-compatible package that restores the prior application behavior. Preserve the previous generation as evidence, not as a directly selectable rollback target.

The auth follow-up is a separate NixOS system change. Add `services.dev-workspaces.auth.bcryptCost` with integer bounds 4 through 17 and default 12, and set 5 only on aitherdev. The exact declared cost participates in htpasswd validation, forcing atomic regeneration while preserving the existing password, TLS state, permissions and nginx Basic Auth boundary. Pin the reviewed dev-workspace revision and site option together through `confctl inputs`, build and dry-activate only aitherdev, then deploy through the supported confctl switch. A compatible system rollback regenerates cost 12 from the unchanged password and can restore the old latency; do not edit credential files manually. System deployment, user-profile deployment and default-branch integration remain distinct gates.

## Documentation

Explain paged conversation semantics in `codex-web`, portal UX and operational diagnostics in `dev-workspace`, and preserve individual baseline, rollout, and recovery evidence in this initiative. Do not copy site-specific paths into generic docs.

## Testing plan

Record before/after request size, latency, browser first-usable time, CPU, scan duration, and lock failures without saving conversation content. Cover long and active histories, pagination/reconnect/cursor failure, receipts and uploads, queue-reconcile failure, old/new browser-server mixtures, archive lock concurrency and fail-closed policy. Run focused checks and commits, then mandatory independent review before long Nix suites, CI, and live tests. Add deterministic exact-cost and password-verification checks without portable wall-clock assertions; use the existing VM test for 12 -> 5 -> 12 -> 5 regeneration, idempotence, authentication and atomic failure behavior. Use a fresh Luna/low watcher for long verification, configuration builds, deployment waits and live overlap tests. After the system switch, require five ten-verification cost-5 batches below the 0.5-second diagnostic budget on an otherwise quiet aitherdev, then repeat 30 no-scan and 30 overlapping dry-run-scan browser loads with p95 usable at or below two seconds and no load failures. Deploy a newer recovery package if application acceptance fails; do not use forbidden earlier-profile rollback.
