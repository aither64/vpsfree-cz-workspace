# 2026-08-11-staging-cpu-monitoring

## Goal

Reduce transient Prometheus CPU-utilization and load-average notifications for
the development/test hypervisors in location `stg`, while keeping non-staging
behavior unchanged and retaining Alertmanager severity inhibition.

## Affected repositories

- `vpsfree-cz-configuration`
  - branch: `2026-08-11-staging-cpu-monitoring`
  - worktree:
    `worktrees/2026-08-11-staging-cpu-monitoring/vpsfree-cz-configuration`

## Approach

- Match staging nodes using the existing Prometheus target label
  `location="stg"`. The current targets are `node1.stg.vpsfree.cz` and
  `node2.stg.vpsfree.cz`; future nodes in the same location inherit the policy.
- Exclude `location="stg"` from the existing alerts so their names and timing
  continue to describe all non-staging nodes.
- Add uniquely named staging variants:
  - `HypervisorHighCpuLoadStaging`: 80% CPU for 50 minutes;
  - `HypervisorCritOsCpuLoadStaging`: 90% CPU for 50 minutes;
  - `NodeHighLoadStaging`: load 300 for 10 minutes;
  - `NodeCritLoadStaging`: load 1000 for 10 minutes;
  - `NodeFatalLoadStaging`: load 2000 for 10 minutes;
  - `NodeOverallCritLoadStaging`: overall load 400 for 10 minutes.
- Preserve `alertclass="cpuload"` and `alertclass="loadavg"`, severity,
  frequency, boot guards, annotations, and the overall-load top-five VPS
  exclusion. Add `location="stg"` as a static label to the staging rules.
- Leave CPU iowait, storage/infra CPU, ZFS, and SSH fallback load alerts
  unchanged.

## Compatibility and deployment

- There are no schema, API, protocol, generated-client, or persistent-state
  changes.
- Alertmanager inhibition remains compatible: it compares `alertclass` and
  `instance`, both of which are preserved. No inhibition rule changes are
  required.
- Deploy both Prometheus containers close together. Mixed monitor versions are
  safe, but an older monitor can still fire the previous staging alerts during
  rollout.
- Staging nodes themselves do not need to be updated. Rollback restores the
  previous Prometheus rule definitions.

## Testing plan

- Evaluate the Nix rule file and inspect the twelve unique default/staging
  alert names, mutually exclusive location selectors, thresholds, durations,
  labels, and annotations.
- Validate the evaluated Prometheus rules using `promtool check rules
  --lint-fatal` from `nixpkgs#prometheus.cli`.
- Install and run the repository Overcommit hooks through `nix develop`.
- After the focused commit and quick checks, run the required standalone
  `mandatory-change-review` and resolve or discuss significant findings.
- Build `cz.vpsfree/containers/prg/int.mon1` and
  `cz.vpsfree/containers/prg/int.mon2` with `confctl`.
