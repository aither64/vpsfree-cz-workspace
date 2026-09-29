---
lifecycle: active
---

# 2026-09-29-portal-performance

## Status

- Phase: reviewed recovery amendment and downstream repinning before deployment. All four original feature heads are reviewed, pushed, and built; Codex-web, generic runtime, and vpsFree extension CI are green. The user authorized repair/resumption of the two paused `tracking_committed` archive journals and default-branch integration after the remaining deployment, acceptance, and final-review gates.
- The archive blocker is isolated and the recovery amendment is committed at dev-workspace `fbd7a9e390b563f83d1787e2cddbd516eefeb558`: Codex 0.155.0 `thread/list` omits some archived team-member threads, so the package now uses exact `thread/read` metadata and bounded rollout-header proof plus a narrow packaged `recover-archive` adapter. The high-risk four-lane review found one Blocking and two Important issues; all three were corrected and their focused host tests pass. No live journal mutation is in progress.
- Current selected package pins `codex-web` e92dd887c888 and `dev-workspace` 3b570f0a8b75; App Server is 0.155.0.
- Pre-rollout `workspace-host status` package: `/nix/store/zpfyl4kkdmv6c7r8a0r6rl1s4wpikkla-dev-workspace-0.2.0`; retain its revision as recovery evidence. Earlier-profile `workspace-host rollback` is intentionally refused for team compatibility; recovery needs a newer forward-compatible package.
- Five full-thread reads of `2026-09-27-newadmin-integration` through the local portal socket each returned 19,897,949 bytes in 2.67–3.32 seconds on September 29. Three fresh authenticated Chromium page loads first rendered a transcript message in 12.36–12.54 seconds, each with 1,023 rendered messages.
- The repeatable `browser-benchmark.cjs` harness passed syntax and a two-load baseline: 12.09–12.45 seconds usable, no failures, one legacy `/thread` response per load, no page responses or HTTP errors. Full 30-load acceptance remains pending after deployment.
- The automatic archive worker's September 29 17:01–17:04 CEST run consumed 3m11.852s wall time and 21.484s CPU according to its systemd journal. This is passive baseline evidence, not a scan started by this initiative.
- During the next scheduled scan at 18:01 CEST (3m53.874s wall, 23.025s CPU), two authenticated benchmark loads did not render a transcript message within 30 seconds (33.862 and 33.420 seconds to report failure). Both remained at “Connecting to conversation…” with the loading placeholder, despite one legacy `/thread` HTTP response each, no HTTP error responses and no page exceptions. Nearby portal logs show canceled thread reads and transition-lock timeouts in queue reconciliation. These are baseline failures, not acceptance samples; the exclusive transition-lock holder remains unproven.
- The deployed old package reproduced the transition-lock contention directly during the 21:01 CEST scheduled scan. A `dev-session team assign` for this session waited beyond its 45-second timeout while the scan was active and completed only after the scan emitted its result at 21:04:53. This confirms that the old passive scan can delay unrelated session commands; it does not identify any separate historical lock holder.
- A second root lead turn independently relayed architect feedback while this CLI lead was coordinating. It confirmed it made no file edits, commits, tests, pushes, deployments or lifecycle changes and agreed to remain idle. This CLI lead remains the single coordinator.
- The CLI lead reviewed and ratified `design.md`'s non-renewable 60-second maximum age for rollout-derived display metadata, with a normal append-writer assumption, best-effort 4 KiB probe, authoritative server checks and required expiry/rebuild tests. The due-rebuild CPU/browser benchmark is a gate; the limit is not proof against arbitrary in-place rollout edits.
- Codex-web GitHub Actions `Check` run `36620678434` passed for corrected feature head `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`.
- The full `dev-workspace` package build passed at `9db7bc844a0332b7e00d21536c3bebf835928ece` in 3m14s. Its primary suite completed 342 runs and 3,611 assertions with zero failures or errors; adjacent suites completed 8/33 and 97/544 with zero failures or errors. The logged Git identity error is an expected exercised subprocess failure inside the passing test suite, not a build failure.
- Dev-workspace GitHub Actions `Check` run `36624756200` passed for exact feature head `9db7bc844a0332b7e00d21536c3bebf835928ece`. vpsFree extension `Check` run `36625520975` passed for exact feature head `7e6fdd140e144611658acb6e7610a5ccf668a0f2` after an 8m55s flake job.

## Phase checklist

- [x] Scope and success criteria agreed.
- [x] Architect design brief and socket/browser baseline.
- [x] Implementation and focused local checks.
- [x] Independent review and long verification/CI.
- [x] Archive-proof recovery fix, quick checks, and independent review.
- [ ] Live user-profile deployment and acceptance.
- [ ] Final whole-history readiness review and authorized default-branch integration.

## Next actions

- Push the reviewed dev-workspace recovery head, repin the vpsFree extension and workspace package, then build a rooted candidate and use the supported adapter to resume the two user-authorized journals.
- Retry the reviewed user-profile switch, then execute live latency, scan-contention, and metadata-rebuild acceptance.
- Perform the final complete-history and migration-readiness review after the whole pin chain and live evidence are complete, then integrate the authorized feature heads into their default branches in dependency order.

## Documentation

- `plan.md` records intent and compatibility; `design.md` owns the technical and verification brief. `rollout.md` is a prepared, unexecuted aitherdev switch/recovery record. The plan now distinguishes legacy recent-20-turn `/thread` from all-history paging and uses forward-package recovery rather than unsupported profile rollback.

## Repositories

- `codex-web`: `worktrees/2026-09-29-portal-performance/codex-web`, branch `2026-09-29-portal-performance`, base `e92dd88`, pushed feature head `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`.
- `dev-workspace`: `worktrees/2026-09-29-portal-performance/dev-workspace`, same branch, base `3b570f0`, committed local head `fbd7a9e390b563f83d1787e2cddbd516eefeb558` with the exact `d210d3f7` pin, archive-proof recovery amendment, final vendor hash, and exact parsed pin-selection guard.
- `vpsfree-dev-workspace`: `worktrees/2026-09-29-portal-performance/vpsfree-dev-workspace`, same branch, base `bd96168`, reviewed and pushed pin head `7e6fdd140e144611658acb6e7610a5ccf668a0f2`.
- Workspace: `worktrees/2026-09-29-portal-performance/workspace`, same branch, base `979ef666`, reviewed local pin head `238ee9a684579e732fd3bab3c37409c892a05ebe`.

## Commands run

- `dev-session start 2026-09-29-portal-performance --as-is --team delegated --goal-file ... --no-attach --json` created this initiative.
- `dev-session current` matched the complete session/workspace environment identity.
- `dev-session team list 2026-09-29-portal-performance --as-is` verified ready design, implementation, and review members with saved write/read access.
- Fetched all three canonical SSH remotes and created the three registered project worktrees plus the workspace feature worktree.
- Five `curl --unix-socket ... /codex/conversations/2026-09-27-newadmin-integration/thread` requests measured the current full-thread path without saving content.
- Three authenticated headless Chromium loads of the live target page measured first rendered transcript messages without saving conversation content.
- The browser benchmark harness recorded timings and response counts only; its two-load smoke check used the current live profile.
- `architect0` completed `design.md`, including optional paging, turn-aware cursors, archive lock order, verification and recovery. The first `codex-web` slice was assigned to `implementer0` (Sol/xhigh, workspace-write).
- `implementer0` delivered the bounded page reader, optional authenticated HTTP endpoint, browser client helper, focused tests, exact 0.155.0 schema corpus and reference documentation. Its focused Go, Node, schema, format and whitespace checks passed; this lead repeated format, Node syntax and whitespace checks. Nix daemon/socket checks were blocked in the member sandbox, and live multi-item cursor semantics remain unverified.
- Committed `codex-web` feature revision `0fad2e1` after the focused checks and an editorial clarification in `docs/reference.md`; fetched current SSH `origin/master` (no divergence) and pushed only the feature branch. No default branch was changed.
- Codex-web GitHub Actions `Check` run `36598475658` for exact feature head `0fad2e1` completed successfully. This is early CI feedback, not independent review or live acceptance.
- Assigned `implementer0` the portal page rendering, queue/pending decoupling, refresh and compatibility slice in `dev-workspace`; archive observation is a later separate assignment.
- Verified the pinned `codex-web` Go pseudo-version against the real module proxy; its module and go.mod checksums match the implementer's temporary local proxy. The `dev-workspace` pin and portal source are still uncommitted and under implementation.
- Discovered and installed the exact provisional Go vendor hash `sha256-7524Wrzk0O1Zwg5v8GqrM1GFjnTqnCzBz29D11xSVuk=` for the current `codex-web` page-API pin. The final shared-helper revision will require a new exact pin and hash.
- The portal's focused Node paging contract and JavaScript syntax checks pass. A full focused Go web-package run exposed one stale source marker; the implementer corrected it and the exact test now passes.
- Implemented passive automatic-archive observation with shared transition/session locks, one combined Codex observation process, bounded known-busy blockers and fail-closed unknown results. Actual archival retains exclusive locking and rechecks root activity, team members, worktrees, registered branch heads, hold and policy before writing its journal.
- Host checks pass for the combined observer table, real shared/exclusive `flock` behavior, malformed observations, and activity/worktree/member/hold/branch-head races. Ruby evidence totals 17 assertions for lock behavior, 48 for lock/malformed behavior, 86 for activity/worktree/member/hold races and 20 for branch movement; focused Go fake-socket coverage passes after its member-sandbox socket limitation was bypassed on the host.
- The recovery amendment quick checks pass: full host `go test ./internal/workspacecodex ./internal/teamruntime ./cmd/workspace-portal`, focused archive/team/CLI Go checks, five Ruby host recovery tests with 63 assertions, four lifecycle retry tests with 83 assertions, Ruby syntax, Go formatting and `git diff --check`.

## Results

- Initial team roster: `architect0` (Astra/xhigh, write), `implementer0` (Sol/xhigh, write), `reviewer0` (Sol/xhigh, read-only).
- Mandatory recovery review: High risk; General, Architecture and repetition, Scope and proportionality, and Risk and compatibility lanes; retained `reviewer0` on saved `gpt-6-sol`/xhigh. One Blocking active-sibling regression and two Important source/root-only compatibility findings were fixed in `fbd7a9e` and directly reverified. No migrations; no superseded committed recovery approach.

## Open questions

- No user decision is currently needed. The architect flagged many-short-turn page latency, exact live cursor behavior, archived-rollout identity races and predecessor/helper compatibility as verification risks. The exact historic exclusive transition-lock holder remains unidentified; add diagnostics rather than attributing it to the archive scan.

## Cleanup

- Preserve active session, branches, and worktrees until separately authorized lifecycle action.
