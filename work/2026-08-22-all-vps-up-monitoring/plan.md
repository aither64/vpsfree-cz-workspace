# 2026-08-22-all-vps-up-monitoring

## Goal

Continuously detect VPSes for which vpsAdmin has auto-start enabled but which
are not running in osctld. Delay notifications until the shared hypervisor boot
grace and a per-condition persistence interval have elapsed, and include every
affected VPS ID in the Alertmanager notification.

## Affected repositories

- `vpsadmin`: vpsAdmin owns the desired `autostart_enable` value; nodectld is
  the integration boundary that already compares the vpsAdmin VPS inventory
  with osctld containers and exports node-local Prometheus metrics.
- `vpsfree-cz-configuration`: Prometheus rules and Alertmanager policy are
  deployed from this repository.

`vpsadminos` was inspected, but no vpsAdminOS change is needed in the first
version. nodectld already receives the complete osctld container export.

## Approach

1. Add `autostart_enable` to the existing internal VPS status-check RPC.
2. Reconcile the authoritative vpsAdmin setting with one `osctl ct ls`
   snapshot in nodectld's existing two-minute VPS status pass.
3. Publish a thread-safe, immutable reconciliation snapshot through nodectld's
   existing node-exporter textfile collector. Export a stable per-VPS
   unsatisfied series, a separate reason series, aggregates, freshness, check
   success, and vpsAdmin/osctld auto-start drift diagnostics.
4. Record one shared 30-minute hypervisor boot signal in Prometheus. Reuse it
   for `HypervisorBooting` and gate the new alerts on its cleared state.
5. Alert once per affected VPS after ten minutes, so Alertmanager groups the
   alerts by node while its existing Telegram template prints every VPS ID.
   Alert separately when the reconciliation check is failing or stale.

## Compatibility and deployment

The implementation supports rolling upgrades. The RPC field and metrics are
additive. Old nodectld ignores the added field. New nodectld treats the field's
absence in a non-empty old-API response as an unsuccessful check, so it cannot
misinterpret missing data as auto-start disabled. Old nodes emit no new series
and therefore cannot produce false per-VPS alerts.

No persisted container configuration format needs to change. If central
vpsAdmin persistence is proposed, its schema and rollback behavior must be
called out separately. A node-local design should avoid a database migration.

## Testing plan

- Unit-test desired/actual reconciliation for running, stopped, transitional,
  missing, drifted, missing-RPC-field, and failed-check cases.
- Test Prometheus output and alert expressions, including no alert inside the
  boot grace, a delayed consolidated alert after the convergence deadline,
  resolution after a late start, a newly enabled post-boot VPS, and
  mixed-version metric absence.
- Add a vpsAdminOS/vpsAdmin integration scenario that deliberately prevents one
  auto-start container from starting while another succeeds.
- If per-container queued/active state is added later, test interleaved external
  queue work, retries, removal, cancellation, and the maximum pending timeout.

## Findings

### Desired state

vpsAdmin is the authoritative source of the member-visible desired state:
`vpses.autostart_enable`. A normal start/restart enables it and a normal stop
disables it. nodectld applies the same state to osctld using `osctl ct set/unset
autostart`.

The two copies can temporarily or permanently diverge when a transaction fails
part-way through or an operator changes osctld directly. The reconciliation
should therefore use vpsAdmin as desired state and report OS-side drift
separately.

### Observed state and boot timing

osctld loads a pool, marks it active, and asynchronously submits the containers
selected by `AutoStart::Plan#start` to a per-pool `ContinuousExecutor`. It
retries each failed start five times. The daemon and pool can be reported
initialized/active while those commands are still running.

The executor is intentionally continuous rather than a bounded boot queue.
External callers can use `ct start --queue` at any time, and these commands are
submitted to the same executor as the pool-import auto-start commands. Queue
idleness therefore cannot represent completion of boot-time auto-start; the
executor may receive unrelated work indefinitely.

`osctl pool autostart queue` is insufficient as a readiness gate: it exposes
only commands waiting in the executor, not commands already executing. With
the default parallelism of two, the queue can be empty while up to two
containers are still starting or retrying. Waiting for the whole executor to
become empty is also incorrect, because later external work would extend or
prevent the supposed boot-completion boundary.

The fixed `HypervisorBooting` rule currently assumes 40 minutes. That is useful
as a broad inhibitor but is not an exact completion signal: completion can be
much earlier, while a large or slow node can take longer.

### Existing comparison paths

- osctl-exporter reads the complete osctld container export, including its
  `autostart` boolean, but currently exports only runtime state and resource
  metrics.
- nodectld's `VpsStatus` fetches the expected VPS inventory from vpsAdmin and
  compares it with `osctl ct ls` every 120 seconds. It currently receives no
  desired auto-start value and drops expected VPSes that are absent from
  osctld.
- vpsAdmin stores the last status sent for each existing container. An expected
  VPS that is absent from osctld sends no update, so an old `is_running=true`
  row can survive a host reboot. A central query must add a boot-generation or
  freshness check; `is_running` alone is unsafe.

## Recommended design

Treat the requirement as a desired-state convergence SLO, not as completion of
the continuous osctld executor. Reconcile continuously in nodectld and delay
notifications using node/pool age plus condition persistence.

### 1. Reconcile desired and actual state in nodectld

Extend the existing `list_vps_status_check` RPC result with
`autostart_enable` and the osctld pool name. Extend `VpsStatus` (or a small
adjacent reconciler that shares its inventory/ct-list snapshot) to classify
each expected auto-start VPS on every pass:

- `running`: present and in osctld state `running`;
- `starting`: present and in a transitional runtime state;
- `stopped`: present but not running;
- `missing`: vpsAdmin expects it, but osctld did not load it;
- `autostart_drift`: the vpsAdmin and osctld auto-start booleans differ.

Publish the result through nodectld's existing `/run/metrics/nodectld.prom`
textfile as both aggregates and per-VPS diagnostic series:

- `nodectld_vps_autostart_check_success`;
- `nodectld_vps_autostart_check_last_success_timestamp_seconds`;
- `nodectld_vps_autostart_expected{pool}`;
- `nodectld_vps_autostart_unsatisfied_count{pool,reason}`;
- `nodectld_vps_autostart_unsatisfied{pool,vps_id}`;
- `nodectld_vps_autostart_unsatisfied_reason{pool,vps_id,reason}`;
- `nodectld_vps_autostart_mismatch{pool,vps_id,vpsadmin,osctld}`.

Keep `reason` off the primary unsatisfied series so a runtime-state change does
not reset the alert's `for` timer. Match containers by pool and VPS ID, deriving
the osctld pool from the first component of `pool_fs`. Only `running` satisfies
the desired state. Missing containers have reason `missing`; present
non-running containers use their osctld state as the reason.

Do not reuse a stale comparison after an RPC or osctld failure. Remove or mark
the result unavailable and use the success timestamp for a separate stale-check
alert. The normal node/down and osctld/down alerts cover complete
unavailability.

This placement remains preferable because nodectld already is the explicit
vpsAdmin/vpsAdminOS integration boundary. It detects both start failures and
containers missing entirely from osctld without adding vpsAdmin database
columns or making the generic osctl exporter understand vpsAdmin policy.

### 2. Share the boot grace and alert per VPS

There is no exact global "auto-start finished" timestamp. Define the supported
availability objective instead: after a node has been up for 30 minutes, every
auto-start-enabled VPS must be running. Record that state once as
`vpsfree_hypervisor_booting` and make both `HypervisorBooting` and the new rules
consume it. If `node_boot_time_seconds` is absent, the recorded series is also
absent and the new alerts stay suppressed.

The Prometheus expression should require all of:

- a fresh nodectld comparison;
- node uptime greater than the boot grace, joined on `fqdn`;
- one per-VPS unsatisfied series;
- persistence for another 10 minutes using the rule's `for` duration.

Put the recorded boot condition in the alert expression rather than only
inhibiting the alert with `HypervisorBooting`; otherwise the Prometheus `for`
timer can run during inhibition and notify immediately when the inhibitor
disappears. Each alert retains `fqdn`, `alias`, `pool`, and `vps_id` labels.
The existing Alertmanager grouping produces one node notification and the
existing Telegram template lists every firing alert and its labels, including
the affected VPS IDs.

The same rule naturally handles changes after boot. A newly auto-start-enabled
VPS begins its own 10-minute persistence period immediately, while unrelated
work continually added to the osctld queue has no effect on it. A start that is
still queued after the overall boot deadline is itself a failure to meet the
availability objective, so it should not suppress the alert indefinitely.

### 3. Optionally expose per-VPS start activity

For better diagnostics, osctld could expose waiting and executing start command
IDs, not just the currently waiting queue. nodectld could then classify an
unsatisfied VPS as `start_pending` rather than `stopped`. This must remain a
diagnostic or have a hard maximum pending duration; repeated external enqueueing
of one VPS must not suppress its availability alert forever. Unrelated queued
containers must never affect another VPS's alert timer.

The current generic `LxcStartFailed` event can remain an immediate root-cause
signal, while the new alert reports the durable availability impact. If the
event is too noisy during boot, inhibit it with `HypervisorBooting`; do not tie
the inhibition to continuous queue activity.

## Alternatives

### A. Coordinated boot epoch and barrier

If an exact completion signal is required, all systems that can enqueue
boot-related starts must participate in a protocol: create a boot epoch, tag
every related command, explicitly close registration after every producer is
done, and declare the epoch terminal after all tagged commands finish. Untagged
later queue work remains independent.

This is the only exact global boundary, but it couples osctld, node boot
orchestration, declarative container services, and any other producer. It is
substantially more complex than the monitoring requirement warrants.

### B. Pool-import cohort only

`AutoStart::Plan#start` selects a finite snapshot during pool import, so osctld
could tag and account for just those commands even though they share the
continuous executor. This is useful diagnostic information about import-time
autostart failures.

It is not a node-ready signal: declarative services and other external systems
can add legitimate boot-related starts afterward. Do not use completion of this
cohort as the primary alert gate.

### C. Pure vpsAdminOS/Prometheus check

Expose `osctl_container_autostart_enabled{pool,id}` and compare it with the
runtime state after the boot grace. This is a small generic vpsAdminOS health
rule, but it cannot detect a vpsAdmin VPS whose configuration failed to load
into osctld and trusts the potentially drifted OS-side auto-start flag.

### D. Central vpsAdmin monitor/exporter

Compare `autostart_enable` with fresh `VpsCurrentStatus` centrally. This is
authoritative but needs explicit freshness or boot-generation handling because
missing containers leave stale status rows. It is more complex than performing
the same comparison in nodectld and does not improve the alert outcome.

## Deployment order

1. Deploy the additive RPC field to central vpsAdmin services.
2. Deploy nodectld to staging nodes and verify the reconciliation metrics.
3. Deploy the shared 30-minute boot recording rule and the per-VPS and stale
   check alerts. Shortening `HypervisorBooting` from 40 to 30 minutes also
   makes its existing inhibited guest-container alerts eligible ten minutes
   earlier.
4. Roll nodectld to production nodes and validate convergence and alert
   resolution during a controlled failure.
5. Optionally add per-container queued/executing diagnostics in osctld and
   osctl-exporter without making queue idleness an alert gate.

The RPC and metrics are additive and require no vpsAdmin database migration or
persisted container-format change. Old nodectld ignores the new RPC fields; old
nodes do not emit the new metric and are excluded by the alert selector.
