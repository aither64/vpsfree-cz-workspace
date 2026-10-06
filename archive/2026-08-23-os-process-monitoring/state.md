---
lifecycle: complete
---
# 2026-08-23-os-process-monitoring

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-08-23-os-process-monitoring`
  - integration branch: `merge/2026-08-23-os-process-monitoring`
  - feature and integration worktrees removed after merge
  - base: `origin/master`
    `1adf7d860ee81adc42ac2a8ecaf53499a083de63`
- Read-only reference to `repos/vpsadminos.git` for osctl-exporter metric
  semantics.

## Status

Implementation committed at `7cd45c867e3a9823f2e7d627c6e153cdc079489b`.
Quick verification, the mandatory standalone change review, and both broader
monitor builds are complete. The review finding was fixed, the feature branch
was fast-forwarded into `master`, and both branches are pushed at the same
commit. Nothing has been deployed.

## Commands run

- Verified the active development-session slug and top-level workspace state.
- Fetched `origin/master` in the canonical bare
  `vpsfree-cz-configuration` repository.
- Inspected repository-local instructions, monitor scrape jobs, node and infra
  rule groups, Alertmanager routes/inhibition, and node-exporter collector
  selection.
- Inspected node-exporter upstream source for the semantics of
  `node_processes_pids` and `node_processes_threads`.
- Inspected osctl-exporter source and libosctl cgroup readers for
  `osctl_container_processes_pids`/`pids.current` semantics.
- Downloaded public Munin weekly, monthly, and yearly process/thread graphs for
  all listed hosts and extracted their legends.
- Attempted a read-only current Prometheus query through
  `mon1.int.prg.vpsfree.cz`; SSH authentication was unavailable, so no private
  Prometheus data was accessed.
- Created the feature worktree through `bin/dev-session`. The command reported
  missing ambient Overcommit gems after checkout, but the branch and worktree
  were created successfully.
- Verified the repository's existing Overcommit hooks and ran
  `nix develop -c bundle exec overcommit --version`: passed with Overcommit
  0.72.0.
- Added node process and thread alert tiers, infra warning/critical process
  tiers, and a focused Prometheus rule check.
- Ran
  `nix build path:.#checks.x86_64-linux.process-count-prometheus-rules --no-link`:
  passed after correcting expected template labels to include the source metric
  name.
- Ran `nix develop -c bundle exec overcommit --run`: Nixfmt and RuboCop passed.
- Ran `nix flake check path:.`: both Prometheus rule checks and the development
  shell check passed. The expected warning about the custom `confctl` flake
  output was unchanged.
- Committed the implementation as `d06cbbba` (`monitoring: alert on high
  process and thread counts`). The commit contains the alert rules and their
  directly supporting promtool check as one logical monitoring change.
- Mandatory standalone review result:
  - no Blocking findings;
  - one Important test-coverage finding: wrong-job assertions covered only
    warning tiers, and the no-infra-fatal test was not structurally strong;
  - no Advisory findings;
  - decision: fix the test coverage and amend the existing implementation
    commit before broader builds.
- Addressed the review finding by asserting the exact infra process-rule
  inventory and absence of fatal severity in Nix, and by checking every
  process/thread severity against high `job="mon"` inputs.
- Re-ran the focused process-count check and Overcommit: passed. Amended the
  implementation commit to `7cd45c86`.
- Re-ran `nix flake check path:.` after the review fix: passed from cache with
  the expected custom-output warning.
- An initial `confctl build cz.vpsfree/containers/prg/int.mon1` stopped at the
  interactive confirmation because the command was not given `-y`; no build or
  remote state change occurred.
- Ran `nix develop -c confctl build -y
  cz.vpsfree/containers/prg/int.mon1`: passed, generation
  `2026-08-23--12-52-00`.
- Ran `nix develop -c confctl build -y
  cz.vpsfree/containers/prg/int.mon2`: passed, generation
  `2026-08-23--12-53-06`.
- Fetched `origin/master` before pushing; it remained at the recorded base, so
  no rebase was necessary.
- Pushed `2026-08-23-os-process-monitoring` over SSH. Remote head was verified
  at `7cd45c867e3a9823f2e7d627c6e153cdc079489b`.
- Queried GitHub Actions for the feature branch: no runs exist because the
  repository currently has only the scheduled/manual dependency-update
  workflow, with no push or pull-request validation workflow.
- Created a fresh integration worktree and branch from the current
  `origin/master`, then fast-forwarded it to the feature commit with
  `git merge --ff-only 2026-08-23-os-process-monitoring`.
- Ran `nix flake check path:.` from the integration worktree: passed with the
  expected custom-output warning.
- Ran the two broader monitor builds from the integration worktree: mon1 passed
  as generation `2026-08-23--14-51-09`, and mon2 passed as generation
  `2026-08-23--14-52-14`.
- Fetched immediately before integration and confirmed that upstream `master`
  still pointed at the recorded base commit.
- Pushed the fast-forwarded integration head over SSH to `origin/master` and
  verified that remote `master` and the remote feature branch both point at
  `7cd45c867e3a9823f2e7d627c6e153cdc079489b`.
- Queried GitHub Actions for the merged commit: no runs exist because there is
  no push or pull-request validation workflow in this repository.

## Results

### Existing Prometheus behavior

- `modules/clusterconf/monitor/rules/nodes.nix` has alerts for node-wide `D`
  and zombie process states and per-VPS `D`/zombie states. It has no alert for
  total processes, total PIDs, or total threads.
- vpsAdminOS nodes explicitly enable node-exporter's `processes` collector, so
  they already expose `node_processes_pids`, `node_processes_state`,
  `node_processes_threads`, and related limits. The current production
  vpsAdminOS input resolves node-exporter 1.11.1 through its pinned nixpkgs.
- NixOS containers explicitly disable default collectors and do not list
  `processes`. Their processes and threads are already included in the
  vpsAdminOS host totals, so their collector configuration will remain
  unchanged. Infra alerts will apply only where `job="infra"` already exposes
  the metric.
- Alertmanager inhibits lower severities with the same non-empty `alertclass`
  and `instance`, so one shared class is required for the three threshold
  levels.

### Public Munin evidence

The following process totals were read from the public weekly graphs on
2026-08-23. The node2 maximum is the incident; its current value is after the
manual reset.

| Host | Current | Weekly maximum |
| --- | ---: | ---: |
| `backuper2.prg` | 16.64k | 16.78k |
| `node1.pgnd` | 4.76k | 5.04k |
| `node1.stg` | 6.15k | 6.35k |
| `node19.prg` | 19.82k | 21.25k |
| `node2.stg` | 5.77k | 210.76k |
| `node20.prg` | 18.58k | 19.87k |
| `node21.prg` | 20.88k | 22.02k |
| `node22.prg` | 24.39k | 27.88k |
| `node23.prg` | 28.78k | 30.62k |
| `node24.prg` | 28.42k | 32.85k |
| `node25.prg` | 26.95k | 28.40k |
| `node5.brq` | 19.06k | 19.97k |
| `node6.brq` | 8.72k | 9.28k |

- Highest unaffected current-week maximum: approximately 32.85k on
  `node24.prg`.
- One-year maxima show approximately 41.78k on `node24.prg` and a brief 52.70k
  maximum on `node22.prg`. A 50k warning therefore needs a hold time to avoid
  reacting to short historical peaks.
- `node2.stg` reached approximately 210.76k processes and 430.20k threads in
  the incident, compared with a post-reset process count around 5.8k.
- Current-week unaffected thread maxima are approximately 97.89k; a separate
  thread/task alert deserves consideration because kernel task exhaustion is
  not fully represented by process-leader counts.
- Public Munin contains the vpsAdminOS nodes and `backuper2`, not the ordinary
  infra/monitor containers. The lower infra thresholds therefore require a
  private Prometheus baseline after enabling the collector.

### Implemented thresholds

- Nodes: warning above 50k for 5 minutes, critical above 60k for 2 minutes,
  fatal above 100k for 1 minute.
- Infra: warning above 2k for 10 minutes and critical above 4k for 5 minutes;
  no fatal alert.
- Node threads/tasks: warning above 150k for 5 minutes, critical above 200k for
  2 minutes, fatal above 300k for 1 minute.
- Node notification repeats for both process and thread families are 15
  minutes at warning, 10 minutes at critical, and 5 minutes at fatal.

## Open questions

- None for the agreed monitoring-rule implementation. Per-VPS task alerts and
  enforced `pids.max` containment remain explicitly out of scope.

## Cleanup

- No production or deployment state was changed. The configuration repository's
  `master` and feature branch were the only remote writes.
- The temporary Munin graph directory and transient SSH known-host files were
  removed.
- Transient Nix development-shell `.bin`, `.bundle`, and RuboCop cache paths
  were removed from both worktrees before removal.
- The feature and integration worktrees were removed after the successful
  merge. Their local branches and the remote feature branch were retained in
  accordance with workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
