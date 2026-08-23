# 2026-08-22-all-vps-up-monitoring

## Repositories

- `vpsadmin`
  - branch: `2026-08-22-all-vps-up-monitoring`
  - worktree: removed after integration
  - base: `origin/master` at `d8ce525fa`
  - head: `b12f41859a9ae198224cd6ca63eddbcdd0371db8`
  - merged to `master`: `b12f41859a9ae198224cd6ca63eddbcdd0371db8`
- `vpsadminos`
  - branch: `2026-08-22-all-vps-up-monitoring`
  - worktree: removed after integration
  - base: `origin/staging` at `97a8c8fc6`
  - no changes or remote feature branch
- `vpsfree-cz-configuration`
  - branch: `2026-08-22-all-vps-up-monitoring`
  - worktree: removed after integration
  - original base: `origin/master` at `3bd35c6c`
  - rebased base: `origin/master` at `2106aa2b`
  - head and merged `master`:
    `1adf7d860ee81adc42ac2a8ecaf53499a083de63`

## Status

The implementation has been fast-forwarded and pushed to both affected
repositories' `master` branches. The configuration points both the production
`vpsadmin` channel and the `staging` role's vpsAdmin channel at the merged
vpsAdmin revision. Quick verification, executable Prometheus rule tests, both
repositories' mandatory hook suites, the mandatory change review, and the
end-to-end VM integration test pass. The feature branches remain locally and
on their affected repositories' remotes; all initiative worktrees are removed.

## Implementation

- The internal `list_vps_status_check` RPC now returns `autostart_enable`.
- nodectld reconciles the vpsAdmin inventory and osctld container list in its
  existing VPS status pass. It matches on osctld pool and VPS ID and retains an
  immutable, mutex-protected snapshot.
- Failed checks clear all current per-VPS and aggregate data while retaining
  the last-success timestamp. A non-empty old API response without the new
  field is explicitly rejected.
- The nodectld textfile exporter publishes success, freshness, expected count,
  stable per-VPS unsatisfied state, separate reasons and counts, and desired vs
  actual auto-start drift.
- Prometheus records `vpsfree_hypervisor_booting` once with a 30-minute
  threshold. `HypervisorBooting`, the per-VPS availability alert, and the
  check-failure alert share that signal.
- `VpsAutostartNotRunning` preserves `fqdn`, `alias`, `pool`, and `vps_id`, so
  existing Alertmanager grouping sends one node notification whose Telegram
  alert loop includes every affected VPS ID.
- Added `vps/autostart-monitoring`, an RSpec-style bridge-network VM scenario
  which reboots a node with two auto-start VPSes, blocks one with a persistent
  pre-start hook, checks the exact per-VPS metric, and verifies resolution.
- No vpsAdminOS code was changed.

## Commands run

- `bin/dev-session current`
- `bin/dev-session worktree add 2026-08-22-all-vps-up-monitoring ...`
- Read all three repository-local `AGENTS.md` files.
- Searched and inspected osctld auto-start, pool import, continuous executor,
  osctl-exporter collectors, nodectld VPS/node status reporting and metrics,
  the vpsAdmin monitoring plugin and Prometheus export task, and production
  Prometheus/Alertmanager rules.
- Inspected relevant file history and verified all project remotes use SSH.
- Ran focused API and libnodectld RSpec tests in their Nix development shells.
- Ran RuboCop on all changed Ruby files.
- Ran `ruby tests/ci-selection-test.rb` and evaluated
  `vps/autostart-monitoring` with the `ci`, `vps-basic`, and `monitoring` tag
  filter.
- Built `cz.vpsfree/containers/prg/int.mon1` with `confctl build -y`; the build
  included and passed Prometheus `checkrules` and `checkconfig` derivations.
- Ran the complete Overcommit pre-commit hook suite in both affected
  repositories before committing.
- Ran the mandatory change review with one standalone fresh-context reviewer.
- Built the `vps-autostart-prometheus-rules` flake check, which runs both
  `promtool check rules` and `promtool test rules` against the production Nix
  rule groups.
- Ran `./test-runner.sh test vps/autostart-monitoring` using the exact suite
  path. The earlier derivation-name selector `vps-autostart-monitoring` matched
  zero tests and was not treated as validation.
- Fetched the current default branches and rebased the configuration feature
  branch onto the advanced configuration `origin/master` in its Nix shell.
- Ran `confctl inputs channel update --commit vpsadmin`, followed by
  `confctl inputs channel update --commit staging vpsadmin`.
- Created fresh detached integration worktrees for vpsAdmin and configuration,
  fast-forwarded them with `git merge --ff-only`, reran focused verification,
  and pushed `HEAD:master` from those worktrees.

## Results

- osctld starts a per-pool asynchronous `AutoStart::Plan` during pool import.
  `Daemon#initialized` is set after work is queued, not after it finishes.
- The public auto-start queue contains waiting commands only; starts currently
  executing in worker threads are not included. An empty queue is therefore
  not a reliable completion signal.
- The per-pool executor is continuous. External `ct start --queue` calls use
  the same executor and can add work indefinitely, so whole-executor idleness
  is not a valid boot-time auto-start completion signal.
- The pool-import call to `AutoStart::Plan#start` does select a finite container
  snapshot, but it is not a complete node-boot cohort: declarative services and
  other external producers can add legitimate boot-related work afterward.
- osctld retries each failed start five times with increasing cooldowns and
  logs the final failure, but does not expose a durable lifecycle/completion
  state or result summary.
- osctl-exporter already exports per-container runtime state every 30 seconds.
  Its osctld input contains the `autostart` boolean, but no metric exposes it.
- nodectld already fetches the expected VPS inventory from vpsAdmin and compares
  it with osctld's container list every 120 seconds. The RPC response does not
  include desired auto-start state, and missing containers are currently not
  published as VPS status updates.
- vpsAdmin's current-status table can remain stale across node boots for a VPS
  missing from osctld, so `is_running` alone is not a complete central check.
- Production monitoring already has a fixed 40-minute `HypervisorBooting`
  inhibitor and an immediate event-based `LxcStartFailed` alert. Neither proves
  that the complete desired VPS set is running after the auto-start pass.
- Corrected recommendation: continuously reconcile vpsAdmin desired state with
  osctld actual state in nodectld, then alert when it has not converged after a
  node-uptime grace and a persistence interval. Do not infer readiness from the
  lifecycle or idleness of the continuous executor. Exact completion would
  require a coordinated epoch/barrier protocol across every queue producer.
- The `vpsfree-cz-configuration` worktree-add command exited after its
  post-checkout Overcommit hook could not load ambient Ruby gems. The worktree
  and branch were nevertheless created successfully and remain clean; no
  commit or hook bypass was attempted.
- The libnodectld development shell's shared `/tmp/dev-ruby-gems` tree had
  empty gem directories despite installed specifications. Focused specs were
  rerun successfully with an isolated bundle path. The reusable workaround is
  recorded in
  `notes/vpsadmin/2026-08-22-libnodectld-dev-shell-stale-gems.md`.
- Focused API RPC specs: 6 examples, 0 failures.
- Focused reconciliation, VpsStatus, and exporter specs: 13 examples,
  0 failures.
- CI selector tests: 16 runs, 55 assertions, 0 failures.
- Monitoring build generations `2026-08-22--22-08-37`,
  `2026-08-23--10-32-54`, and the final integration-worktree generation
  `2026-08-23--10-37-08` completed for
  `cz.vpsfree/containers/prg/int.mon1`.
- vpsAdmin commit: `b12f41859a9ae198224cd6ca63eddbcdd0371db8`.
- The configuration functional commit was rebased from `9e0370ea` to
  `6f106966` after `origin/master` advanced with two mechanical input updates.
- Configuration channel commits, kept exactly as generated by `confctl`:
  - `ce1ff07b inputs: update vpsadminServices to b12f4185`
  - `1adf7d86 inputs: update vpsadminStaging to b12f4185`
- Final configuration commit:
  `1adf7d860ee81adc42ac2a8ecaf53499a083de63`.
- Prometheus semantic rule tests pass. They cover the shared boot signal at,
  before, and without its 30-minute boundary; per-VPS alert identity and
  annotations; two simultaneous VPS alerts; condition resolution; a VPS first
  becoming unsatisfied after boot; fresh, failed, and stale checks; old nodes
  without nodectld metrics; nodes without the boot metric; and a reason-label
  transition that does not restart the primary alert timer.
- `vps/autostart-monitoring` passed: 1 test successful in 1045.4 seconds. The
  vpsAdmin services VM and vpsAdminOS node used existing kernel outputs; no
  local kernel derivation was built.
- Pushed `2026-08-22-all-vps-up-monitoring` to both affected SSH remotes. The
  configuration branch required a force-with-lease after the rebase; no queued
  or running workflows existed for its superseded head.
- The feature-branch vpsAdmin CI produced four successful workflows. The
  integration workflow failed only because self-hosted runner
  `gh-runner1.int.vpsadminos.org` lost communication; GitHub had no job logs or
  artifacts, and the user confirmed the failure coincided with the node2.stg
  outage. Run IDs: CI `32599780231`, libnodectld `32599780246`, RuboCop
  `32599780254`, API topics `32599780255`, and i18n `32599780263`.
- Fast-forwarded and pushed vpsAdmin `master` from `d8ce525fa` to `b12f41859`.
  Focused API specs passed with 6 examples and focused libnodectld specs passed
  with 13 examples from the fresh integration worktree before push.
- Fast-forwarded and pushed configuration `master` from `2106aa2b` to
  `1adf7d86`. The production Prometheus-rule flake check and the monitoring-host
  `confctl build` passed from the fresh integration worktree before push.
- vpsAdmin `master` CI for `b12f41859` started as expected. RuboCop,
  libnodectld specs, and i18n health are successful; API topic specs and the
  selected integration workflow are in progress at the time of this update.
  Run IDs: CI `32628417831`, RuboCop `32628417844`, API topics `32628417868`,
  libnodectld `32628417859`, and i18n `32628417808`.
- The configuration repository has no push-triggered workflow for this change.

## Mandatory change review

The reviewer found no blocking correctness, compatibility, security, or
Alertmanager-label issue. The initial review was a conditional pass because the
first revision had syntax checks for the Prometheus rules but no executable
semantic alert tests. The production-importing promtool tests were added in the
same configuration commit. A follow-up review identified and then verified the
last two guard vectors: an unsatisfied VPS with a failed but fresh check, and an
unsatisfied VPS with a successful but stale check. The reviewer confirmed that
the condition is fully resolved and no significant semantic coverage gap
remains.

The reviewer also noted that the VM scenario removes its failure hook after the
first exported failure sample. Semantic timing and state-transition coverage is
provided by the rule tests, while the VM remains responsible for the end-to-end
producer and reboot path.

## Decisions

- vpsAdmin's `autostart_enable` is authoritative; osctld's copy is a drift
  diagnostic.
- Reconciliation runs continuously in the existing nodectld status pass. It is
  independent of the continuous osctld start queue.
- The shared `HypervisorBooting` threshold is shortened from 40 to 30 minutes
  and recorded once for reuse by all related rules.
- Availability alerts are per VPS and include `vps_id`; Alertmanager's existing
  node grouping and Telegram loop consolidate them without losing IDs.
- The stable alert series excludes the changing failure reason. A separate
  reason series and aggregate expose diagnosis without resetting alert time.
- `LxcStartFailed` remains an immediate root-cause signal.
- No vpsAdminOS change or persistent-state migration is required in version 1.

## Cleanup

The two feature worktrees, the unchanged vpsAdminOS reference worktree, and the
two temporary integration worktrees were clean and removed. The vpsAdmin and
configuration feature branches remain locally and remotely; the unchanged
vpsAdminOS reference branch remains local. Temporary hook/dev-shell files were
moved recoverably to `/tmp/vps-autostart-generated.55z1SQ`. The initiative
worktree group directory is removed.
