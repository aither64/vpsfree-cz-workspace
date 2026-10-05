---
lifecycle: active
---
# vpsf-status index render freshness and CPU use

## Status

- Initiative started on 2026-05-31.
- Goal: investigate `VpsfStatusIndexRenderStale` and optimize per-second index
  pre-render CPU usage.

## Repositories and branches

| Repository | Branch | Worktree |
| --- | --- | --- |
| `vpsf-status` | `2026-05-31-vpsf-status-render-stale` | `worktrees/2026-05-31-vpsf-status-render-stale/vpsf-status` |
| `vpsfree-cz-configuration` | `2026-05-31-vpsf-status-render-stale` | `worktrees/2026-05-31-vpsf-status-render-stale/vpsfree-cz-configuration` |

## Commands and results

- `git --git-dir=repos/vpsf-status.git remote -v`: origin already uses SSH.
- `git --git-dir=repos/vpsfree-cz-configuration.git remote -v`: origin already
  uses SSH.
- `git --git-dir=repos/vpsf-status.git symbolic-ref refs/remotes/origin/HEAD`:
  default branch is `origin/master`.
- `git --git-dir=repos/vpsfree-cz-configuration.git symbolic-ref refs/remotes/origin/HEAD`:
  default branch is `origin/master`.
- `git --git-dir=repos/vpsf-status.git fetch origin master`: fetched current
  upstream.
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin master`:
  fetched current upstream; `origin/master` advanced from `6d223481` to
  `5c6f69e4`.
- Created worktree `worktrees/2026-05-31-vpsf-status-render-stale/vpsf-status`
  on branch `2026-05-31-vpsf-status-render-stale` at `origin/master`
  (`5f6db13`).
- Created worktree
  `worktrees/2026-05-31-vpsf-status-render-stale/vpsfree-cz-configuration` on
  branch `2026-05-31-vpsf-status-render-stale` at `origin/master`
  (`5c6f69e4`).
- Read repository-local `AGENTS.md` files in both worktrees.
- `rg VpsfStatusIndexRenderStale` in `vpsfree-cz-configuration`: alert lives in
  `modules/clusterconf/monitor/rules/vpsfree-web.nix` and fires when
  `vpsfstatus_index_last_render_timestamp_seconds{job="vpsf-status"}` is absent
  or older than 300 seconds.
- `go test ...` in the ambient shell failed because `gcc` was missing for cgo;
  reran through `nix develop`.
- `nix develop -c go test -run '^$' -bench 'BenchmarkRouteIndex(Fallback|PreRendered)$' -benchmem -count 3`:
  cold index fallback rendered in about 65-75 ms/op with about 5.1 MB/op and
  about 57.5k allocs/op in the small test fixture; pre-rendered serving took
  about 0.53-0.61 ms/op with about 526 KB/op and 16 allocs/op.
- `nix develop -c go test -run '^$' -bench 'BenchmarkRouteIndexFallback$' -benchmem -cpuprofile /tmp/vpsf-status-index-cpu.pprof -memprofile /tmp/vpsf-status-index-mem.pprof -count 1`:
  profile baseline collected. CPU profile showed most cold-render time in
  `html/template` execution, with `gzipBytes` also visible. Memory profile
  showed major allocation sources in template buffer growth, gzip writer setup,
  and `newCachedResponse`.
- Removed generated benchmark binary `vpsf-status.test`.

## Current findings

- The renderer runs every second (`indexRenderInterval = time.Second`) and fully
  rebuilds the index, creates a cached response, and pre-compresses gzip output.
- The alert metric is only updated after a successful render. If rendering is
  continuously slow, stuck, or failing, the alert cannot distinguish the cause.
- In the benchmark fixture, the expensive path is mostly HTML template
  execution plus gzip generation. Production has more configured entities than
  the small fixture, so production cost can be higher.
- The ticker loop uses `time.NewTicker(1s)`. If renders take longer than the
  interval, the loop can effectively render back-to-back, increasing sustained
  CPU use.

## Implementation

- Implemented in `vpsf-status`; `vpsfree-cz-configuration` remains unchanged.
- Committed `vpsf-status` changes as `c6fab24`:
  `Render index body on status changes`.
- Split index rendering into an expensive cached body and a cheap per-request
  shell/header. The `Rendered at` value now represents response assembly time,
  while the cached body can remain unchanged.
- Replaced the fixed one-second render ticker with event-driven render requests
  from status checks, notice checks, outage refreshes, API refreshes, and
  initialization. Requests are coalesced and throttled to at most one render
  attempt per second.
- Added a deterministic visible-input signature for the cached body. Unchanged
  signatures skip body rendering unless the 240-second keepalive is due.
- Added an internal history version that advances when probe history changes,
  so promoted/closed incidents can trigger body refreshes even if current status
  fields are otherwise unchanged.
- Kept `vpsfstatus_index_last_render_timestamp_seconds`, now set on successful
  body-render completion.
- Added metrics:
  `vpsfstatus_index_last_render_attempt_timestamp_seconds`,
  `vpsfstatus_index_render_duration_seconds`,
  `vpsfstatus_index_render_failures_total`, and
  `vpsfstatus_index_render_skips_total`.
- Changed gzip generation to use pooled `gzip.BestSpeed` writers and added
  streaming gzip support for the partial index response.
- Added focused tests for unchanged-body skips, changed-body renders,
  keepalive renders, throttle delay, and render failures preserving the last
  good body.

## Validation

- `nix develop -c gofmt -w ...`: formatted changed Go files.
- `nix develop -c go test ./...`: passed.
- `nix develop -c go test -run '^$' -bench 'BenchmarkRouteIndex(Fallback|PreRendered)$' -benchmem -count 3`:
  - cold index body render: about 49-53 ms/op, about 4.75 MB/op;
  - pre-rendered index route: about 1.5-1.7 ms/op in `httptest`.
  The pre-rendered route benchmark includes response-recorder buffering of the
  large HTML page; production writes the cached body as streamed chunks.
- Preview server:
  - `ip -4 -o addr show dev br0`: `172.16.106.40/24`.
  - Generated `/tmp/vpsf-status-preview-config.json` from `config-sample.json`
    with `listen_address = "172.16.106.40:8080"`.
  - `nix develop -c go build -o /tmp/vpsf-status-preview-bin .`.
  - Running `/tmp/vpsf-status-preview-bin /tmp/vpsf-status-preview-config.json`
    in an exec session.
  - `curl -I --max-time 5 http://172.16.106.40:8080/`: returned `HTTP/1.1 200 OK`.
- Preview server stopped; `172.16.106.40:8080` is no longer listening.
- Pushed `vpsf-status` feature branch:
  `origin/2026-05-31-vpsf-status-render-stale` at `c6fab24`.
- GitHub workflow check for the pushed `vpsf-status` branch:
  `gh workflow list --repo vpsfreecz/vpsf-status` showed only
  `Update dependencies` and `Dependency Graph`; the branch had no workflow runs
  and commit `c6fab24` had zero check runs. There are no push/PR workflows to
  wait for in this repository.
- Created temporary detached master worktree
  `worktrees/2026-05-31-vpsf-status-render-stale/vpsf-status-master-merge`,
  fast-forwarded it from `origin/master` to
  `2026-05-31-vpsf-status-render-stale`, and ran
  `nix develop -c go test ./...`: passed.
- Pushed `vpsf-status` master:
  `origin/master` advanced from `5f6db13` to
  `c6fab2476b3dfabf379b64a50d275b33b241f72a`.
- Removed the temporary `vpsf-status-master-merge` worktree.
- In `vpsfree-cz-configuration`, ran
  `nix develop -c confctl inputs channel update --commit --no-editor vpsf-status`.
  This created commit `26794047`:
  `inputs: update vpsfStatus to c6fab247`.
- Pushed `vpsfree-cz-configuration` branch
  `origin/2026-05-31-vpsf-status-render-stale` at `26794047`.
- `gh workflow list --repo vpsfreecz/vpsfree-cz-configuration` showed only
  `Daily update`; the pushed configuration branch had no workflow runs.
- `nix develop -c confctl build -y cz.vpsfree/machines/prg/apu` failed on an
  unrelated local prerequisite:
  `/srv/iso-images/systemrescue-11.01-amd64.iso` does not exist.
- `nix build --no-link github:vpsfreecz/vpsf-status/c6fab2476b3dfabf379b64a50d275b33b241f72a#vpsf-status`:
  passed.

## Open questions

- Whether production stale alerts disappear after deploying the event-driven
  renderer. New attempt/failure/skip/duration metrics should distinguish render
  failures from lack of updates.
- 2026-06-01 production follow-up: a stale alert was still observed overnight.
  Live `https://status.vpsf.cz/metrics` exposes the new index render metrics,
  so deployment and metrics export are present. At 2026-06-01 11:21 CEST,
  `vpsfstatus_index_last_render_timestamp_seconds` was fresh, render failures
  were zero, and `vpsfstatus_index_render_duration_seconds` was about 0.56s.
  Next diagnostic step is querying Prometheus history around the alert for
  render age, attempt age, failures, skips, and the `ALERTS` series.
- Diagnosis: Prometheus `up{job="vpsf-status"}` was 0 for about one scrape
  interval. The render timestamp was not stale; the instant `absent()` clause
  fired because the scrape failure made the metric absent at evaluation time.
- Updated `vpsfree-cz-configuration` alert rule
  `VpsfStatusIndexRenderStale` to use
  `absent_over_time(vpsfstatus_index_last_render_timestamp_seconds{job="vpsf-status"}[5m])`
  and
  `time() - max_over_time(vpsfstatus_index_last_render_timestamp_seconds{job="vpsf-status"}[5m]) > 300`.
  This preserves the 300-second render-staleness threshold while requiring the
  metric to be missing for five minutes before the absence branch fires.
- Validation for alert-rule follow-up:
  - Prometheus accepted the updated expression in a minimal rules file.
  - `nix-instantiate --parse modules/clusterconf/monitor/rules/vpsfree-web.nix`:
    passed.
  - `git diff --check`: passed.
- Created and pushed `vpsfree-cz-configuration` commit `be5bd80a`:
  `monitor: tolerate transient vpsf-status scrape failures`.
- User confirmed the production issue was solved by the alert-rule diagnosis
  and requested merging/pushing/cleanup.
- `vpsfree-cz-configuration` `origin/master` advanced meanwhile to
  `a5355f8b`, so the feature branch was rebased on top of it. The rebased
  commits are:
  - `e9324ee1 inputs: update vpsfStatus to c6fab247`
  - `a38c85ec monitor: tolerate transient vpsf-status scrape failures`
- Force-pushed the rebased `vpsfree-cz-configuration` feature branch with
  `--force-with-lease`.
- Created temporary detached master worktree
  `worktrees/2026-05-31-vpsf-status-render-stale/vpsfree-cz-configuration-master-merge`
  from `origin/master`, fast-forwarded it to
  `2026-05-31-vpsf-status-render-stale`, and pushed `origin/master` to
  `a38c85ecedb3b7c84e041776e21cc80c99c90d45`.
- Verified remote refs after merge:
  - `vpsf-status` `master` and
    `2026-05-31-vpsf-status-render-stale` both point to
    `c6fab2476b3dfabf379b64a50d275b33b241f72a`.
  - `vpsfree-cz-configuration` `master` and
    `2026-05-31-vpsf-status-render-stale` both point to
    `a38c85ecedb3b7c84e041776e21cc80c99c90d45`.

## Cleanup

- `vpsf-status-master-merge` temporary worktree removed after pushing master.
- Removed temporary and feature worktrees for this initiative:
  - `worktrees/2026-05-31-vpsf-status-render-stale/vpsf-status`
  - `worktrees/2026-05-31-vpsf-status-render-stale/vpsfree-cz-configuration`
  - `worktrees/2026-05-31-vpsf-status-render-stale/vpsfree-cz-configuration-master-merge`
- Removed the empty `worktrees/2026-05-31-vpsf-status-render-stale`
  directory.
- Keep local and remote feature branches unless explicitly asked to delete them.
