# Status render alert review

## Requested outcome

The user first requested diagnosis of repeated `VpsfStatusIndexRenderStale`
notifications, then asked for an improvement that keeps the 60-second scrape
interval. The latest instruction explicitly permits a larger margin because
the alert should signal a serious issue rather than a fluke.

Acceptance: preserve the scrape interval and application behavior; avoid paging
on normal four-minute cached-render cycles and brief collection delays; retain
alerting on sustained render stalls and missing metrics, with prompt recovery.

## Repository and committed scope

- Initiative: `2026-09-07-vpsfstatus-index-stale-2`.
- Tracking: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-07-vpsfstatus-index-stale-2/`.
- Plan/state: `plan.md`, `state.md`; investigation evidence: `investigation.md`
  and `metrics-summary.json` in that directory.
- Repository worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-07-vpsfstatus-index-stale-2/vpsfree-cz-configuration`.
- Base: `e26f0a3360e1a20e76c3c0ef4193448584a8c1bb`.
- Head: `0297b0c3bfcec0a4cc0e32fa294c996bfe978afa`.
- One functional commit includes the production alert change, its explanatory
  annotation, focused promtool fixtures and the existing-style flake check
  wrapper. The tests and wrapper specifically validate this rule's changed
  timing, so they belong with its behavior rather than as a separate feature.

The rule moves from the 300-second `vpsfree-web` group to its own 60-second
`vpsf-status` group. Render age must exceed 600 seconds instead of 300, and
either branch must remain active for two minutes before firing. Missing-metric
lookback remains five minutes. Alert name, severity, notification frequency,
query label behavior and all other web alerts remain unchanged.

## Ownership and consumers

Configuration owns the alert policy and the `vpsf-status` scrape job.
`modules/clusterconf/monitor/default.nix` imports all groups from
`rules/vpsfree-web.nix`. Enabled production monitoring containers are
`cz.vpsfree/containers/prg/int.mon1` and `int.mon2`; their alerters are `int.alerts1`
and `int.alerts2`. The `frequency = "1h"` label remains the routing interface.

`vpsf-status` owns the render-success timestamp metric. Its pinned source
`587cd65bb02e6dddea7f6b6409e42a15f36ab4fb` can be inspected in the canonical
bare repo `/home/aither/workspace/ai/vpsfree.cz/repos/vpsf-status.git`.
`index.go` uses a 240-second unchanged-body keepalive and exports a completion
timestamp. Separate locale bodies share the gauge. The public endpoint was
observed to render around every 242 seconds with zero render failures.

No provider code, metric name/meaning, endpoint, scrape job, protocol, database,
persisted state or dependency pin changes. Current configuration pins:
`nixpkgsStable=a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`,
`confctl=7bee58a52372b95c2198ce3f2a719807a3c2c66b`.

## Verification so far

- Installed/signed Overcommit hooks in `nix develop`.
- `nix build .#checks.x86_64-linux.vpsf-status-prometheus-rules --no-link -L`
  passed: production JSON parsed as seven rules, all six scenarios passed.
- Cases cover scrape/evaluation phase mismatch (301-second observed age), a
  missed scrape (361-second observed age), continued scraping of a stalled
  render timestamp, recovery during confirmation, prolonged absence and
  missing-metric recovery.
- `overcommit --run`: Nixfmt and RuboCop passed. Commit hooks passed; TextWidth
  warned above its advisory 72-column limit, while all message lines obey the
  repository/workspace 80-column limit.
- `git diff --check` passed. Worktree contains only generated untracked
  `.bin/`, `.bundle/` and `.rubocop_cache/` from the development shell/hooks in
  addition to committed source; they are not part of the review.
- Full scoped `confctl build` runs for both monitoring containers wait for
  mandatory review. No push or deployment occurred.

## Risk and boundaries

Risk classification: high, because this changes the timing of a critical
operational alert, including detection and recovery during rolling deployment.
Use `gpt-5.6-sol`, `xhigh` reasoning for every lane. Required lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility.

The intentional delay is about 12-13 minutes from last observed render to
firing for a continuously scraped stuck timestamp, and about 7-8 minutes from
last sample to firing for absent metrics. Alertmanager notification waits are
additional. The actual stale-age condition uses a strict `> 600` comparison.

Both Prometheus instances may update independently. Until both update, the old
instance can still emit the previous noisy alert. Rollback restores the old
configuration and timing. No coordinated status-service rollout or data
migration is required. Moving groups/adding a pending period can restart alert
state during reload; this is acceptable for the deliberately more conservative
policy and requires no state conversion.

Non-goals: changing scrape frequency, changing body keepalive or timestamp
semantics, smoothing the graph, restructuring other monitoring policies,
introducing generic test infrastructure, and production deployment. Historical
Prometheus authentication was unavailable, so the diagnosis does not claim all
past notifications had this cause. The current timing failure mechanism is
reproduced and the new policy is directly tested.

Perform your assigned lane independently. Read the local AGENTS.md, the
mandatory-change-review skill and the lane reference; inspect the committed
diff and relevant consumers. Do not edit source and do not spawn subagents.
