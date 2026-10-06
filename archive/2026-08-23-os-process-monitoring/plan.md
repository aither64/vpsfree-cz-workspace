# 2026-08-23-os-process-monitoring

## Goal

Add early warning for process storms before they make a vpsAdminOS node or an
infrastructure system unresponsive. The immediate incident to cover is the
2026-08-22/23 `node2.stg.vpsfree.cz` outage, where one VPS drove the host to
approximately 210,000 processes and 430,000 threads.

## Affected repositories

- `vpsfree-cz-configuration`
  - `modules/clusterconf/monitor/rules/nodes.nix`
  - `modules/clusterconf/monitor/rules/infra.nix`
  - focused Prometheus rule tests under `tests/prometheus/` and their flake
    check registration

No vpsAdminOS, exporter, API, database, protocol, or generated-client change
is required for host-wide node alerts. The already enabled node-exporter
`processes` collector provides `node_processes_pids` and
`node_processes_threads` on vpsAdminOS nodes.

## Approach

### Existing coverage

Prometheus currently has process-state alerts, but no total process-count
alert:

- node-wide uninterruptible (`D`) processes at critical and fatal levels;
- node-wide zombie processes at warning level;
- per-VPS uninterruptible and zombie process alerts.

The `nodes` scrape job already receives `node_processes_pids`. This metric is
the direct node-exporter count of processes and matches the total-process
concept shown by Munin closely enough for the proposed thresholds. Do not sum
per-state metrics when the exporter already publishes the total directly.

### Proposed node rules

Add three rules to the existing `nodes` rule group:

| Alert | Expression | `for` | Severity | Repeat |
| --- | --- | --- | --- | --- | --- |
| `NodeWarnProcessCount` | `node_processes_pids{job="nodes"} > 50000` | `5m` | `warning` | `15m` |
| `NodeCritProcessCount` | `node_processes_pids{job="nodes"} > 60000` | `2m` | `critical` | `10m` |
| `NodeFatalProcessCount` | `node_processes_pids{job="nodes"} > 100000` | `1m` | `fatal` | `5m` |

Give all three rules `alertclass = "processes_total"`. Existing Alertmanager
inhibition will then suppress warning behind critical and critical behind
fatal for the same instance. Do not add a boot-age condition: a node that has
more than 50,000 processes shortly after boot is still operationally relevant,
and the warning hold time is sufficient to discard short startup peaks.

Use annotations which explicitly say that this is the total host process
count, include the value and labels, and point responders toward per-container
`osctl_container_processes_pids`/`osctl ct ls -o nproc` data for attribution.
The latter is cgroup `pids.current` and therefore counts tasks, including
threads; it is useful for finding the responsible VPS but is not numerically
identical to the host process count.

### Proposed infrastructure rules

Use a separate, lower tier for non-user-workload systems:

| Alert | Expression | `for` | Severity | Repeat |
| --- | --- | --- | --- | --- | --- |
| `InfraWarnProcessCount` | `node_processes_pids{job="infra"} > 2000` | `10m` | `warning` | `1h` |
| `InfraCritProcessCount` | `node_processes_pids{job="infra"} > 4000` | `5m` | `critical` | `10m` |

Do not add a fatal infra alert. Do not enable the process collector in NixOS
containers or monitors: their workloads are already included in the
vpsAdminOS host totals, which is sufficient for this initiative. The infra
rules apply only to `job="infra"` targets which already expose the metric.

### Node thread/task rules

The incident involved approximately twice as many threads as processes. A
thread-only storm could remain below the process thresholds while exhausting
the host task limit. Add a parallel node tier on `node_processes_threads`:

| Alert | Expression | `for` | Severity | Repeat |
| --- | --- | --- | --- | --- | --- |
| `NodeWarnThreadCount` | `node_processes_threads{job="nodes"} > 150000` | `5m` | `warning` | `15m` |
| `NodeCritThreadCount` | `node_processes_threads{job="nodes"} > 200000` | `2m` | `critical` | `10m` |
| `NodeFatalThreadCount` | `node_processes_threads{job="nodes"} > 300000` | `1m` | `fatal` | `5m` |

Use a separate `processes_threads` alert class so responders can distinguish
process growth from thread growth. Both families may fire concurrently.

## Compatibility and deployment

- Node alerting is configuration-only and uses an existing metric. Rules can
  be deployed to both Prometheus servers without changing nodes.
- There is no persisted-state, database, API, protocol, or on-disk format
  change. Rollback removes the rules without leaving incompatible state.
- Deploy and verify both `mon1` and `mon2`; alert evaluation must remain
  equivalent on the redundant monitors.

## Testing plan

- Add focused Prometheus rule tests for values below, at, and above every
  threshold, including each `for` duration and the common `alertclass`.
- Confirm that each severity family uses one alert class for the existing
  Alertmanager inhibition behavior, while processes and threads use distinct
  classes.
- Evaluate/build both monitor configurations so the generated rule file is
  accepted by Prometheus.
- Verify that infra tests select only `job="infra"` and that no fatal infra
  rule is present.
- Run repository hooks and quick checks, commit the intended changes, then run
  the mandatory standalone change review before longer/broader builds.
- After deployment, verify the rule status and query results on both Prometheus
  servers and watch for alert noise during the first week.
