# 2026-10-03-infra-monitoring

## Goal

I'd like to change prometheus alerts regarding job="infra".

First, there are thtree kinds of infra machines: VPS (containers on vpsadminos), VMs and physical machines. I'd like the critical disk space alerts to send sms only for VMs and physical machines. VPS use vpsAdmin's dataset auto-expansion, so running out of diskspace is not critical, it is automatically sorted. It should however keep sending email alerts, so that we're aware of it.

Secondly, I'd like the critical disk space alerts on infra to fire a bit later. I don't know the numbers yet, so make a suggestion based on current critical/fatal values.

I'd also like to reduce cpu load alerts on staging/playground nodes, so they're not as strict as on production systems (locations prg and brq).

You'll find the cluster and monitoring configuration in vpsfree-cz-configuration. Look it over and suggest solutions.

## Affected repositories

- `vpsfree-cz-configuration`: central Prometheus target generation, common disk
  alerts, node load alerts, and Alertmanager routes.
- This turn is an investigation and proposal. No configuration implementation,
  feature branch, build, deployment, or integration is authorized by the request.

## Approach

Inspect the fetched remote default branch through the canonical bare clone.
Keep the proposal and evidence here until the operator chooses the policy.
Substantive implementation requires an appropriate retained/catalog team;
the lead retains coordination and delegates application changes.

### Observed configuration

Inspected `origin/master` at
`2a3e6a977db4464b585e413839953f08f57521f7` on 2026-10-03.
The findings describe repository configuration, not a verified live deployment.

| Alert | Current condition | Hold time | Source |
| --- | --- | --- | --- |
| FilesystemLowFreeSpace | available space < 20% | 5m | `modules/clusterconf/monitor/rules/common.nix:208` |
| FilesystemCritFreeSpace | available space <= 10% | 5m | `modules/clusterconf/monitor/rules/common.nix:227` |
| NodeFatalRootfsFreeSpace | root available space <= 5%, job=nodes only | 5m | `modules/clusterconf/monitor/rules/nodes.nix:520` |
| ZpoolLowFreeSpace | pool capacity >= 85% | 1h | `modules/clusterconf/monitor/rules/common.nix:53` |
| ZpoolCritFreeSpace | pool capacity >= 90% | 120m | `modules/clusterconf/monitor/rules/common.nix:71` |
| ZpoolFatalFreeSpace | pool capacity >= 95% | 30m | `modules/clusterconf/monitor/rules/common.nix:90` |

There is no filesystem fatal alert for `job="infra"`. The common ZFS-pool
alerts are separate from filesystem capacity alerts and apply where those
metrics exist. Several ZFS annotations contain older percentages; expressions
are the authority. Node pool dataset alerts also have separate absolute free
space thresholds and are outside the proposed disk changes.

`modules/clusterconf/monitor/default.nix:139` selects infra targets from
monitored machines without node metadata, excluding monitoring servers.
Targets have alias, fqdn, domain, location, os, and custom monitoring labels.
They currently have no generated VPS/VM/physical discriminator. A non-null
`metaConfig.container` identifies managed VPS containers. Both VMs and physical
machines have null container metadata, which is sufficient for their shared
SMS policy. NixOS is used by all three kinds and is not a suitable discriminator.
For example, aitherdev and em1 import the QEMU guest profile; the APUs are
physical machines. Monitor containers mon1/mon2 use the separate monitorings job.

`modules/clusterconf/alerter/default.nix:303` routes warning, critical and fatal
alerts to email, then critical/fatal alerts to Telegram, then to both SMS
recipients. Critical SMS delivery has recipient-specific daytime windows;
fatal SMS delivery has no daytime restriction. The disk rules request hourly
repeats. Severity inhibition is global per alertclass and instance, so retaining
critical severity preserves the existing warning inhibition behavior.

The CPU/load policy is in `modules/clusterconf/monitor/rules/nodes.nix`:

| Signal | prg/brq and currently pgnd | stg |
| --- | --- | --- |
| Hypervisor CPU warning | > 80% for 10m | > 80% for 50m |
| vpsAdminOS hypervisor CPU critical | > 90% for 10m | > 90% for 50m |
| Five-minute load warning | > 300 for 5m | > 300 for 10m |
| Five-minute load critical | > 1000 for 5m | > 1000 for 10m |
| Five-minute load fatal | > 2000 for 5m | > 2000 for 10m |
| Overall load excluding top five VPS | > 400 for 5m | > 400 for 10m |

Production selectors currently exclude only stg, so pgnd receives production
rules. These node alerts concern job=nodes/role=hypervisor, separately from the
infra job mentioned in the disk request. The playground inventory is
`cluster/cz.vpsfree/nodes/pgnd/node1/module.nix:44`; staging has node1 and node2.

## Decisions

The following are recommendations, not accepted implementation decisions.

1. Generate an `is_vps="true"|"false"` target label for infra from whether
   container metadata is present. The required notification distinction is
   VPS versus the two kinds that retain SMS; a manual VM/physical taxonomy is
   unnecessary for this change.
2. Keep VPS disk alerts critical and preserve email, hourly repetition,
   inhibition, and existing Telegram delivery. Insert a terminal blackhole
   route after the email/Telegram routes and before either SMS route, matching
   job=infra, is_vps=true, severity=critical and alertclass=fsavail. This skips
   only SMS for the requested alerts. Do not silence or inhibit the whole alert,
   downgrade all VPS alerts, or blackhole it before email delivery.
3. For infra filesystems, lower the critical free-space threshold to <= 7.5%
   and extend the hold from 5m to 10m. This lies between the current critical
   10% and the node root filesystem fatal reference of 5%. Keep the warning
   at < 20% for 5m. Do not add an infra fatal filesystem alert in this change.
4. If covering the common pool-capacity alerts as well, move infra-only ZFS
   critical capacity from >= 90% to >= 92%, retaining 120m. Keep fatal at
   >= 95% for 30m. Containers do not expose the host pool as their own disk;
   underlying node pool alerts continue to page normally. Retain all non-infra
   disk thresholds. Correct descriptions for the changed rules.
5. Use a shared relaxed policy for locations stg and pgnd. Start with CPU
   warning > 90% and critical > 95%, both for 50m, while prg/brq retain their
   existing 80%/90% and 10m. Retain boot suppression and alertclass=cpuload.
6. For raw load averages, start with warning > 600 for 15m, critical > 1500
   for 15m, and overall load > 800 for 15m on stg/pgnd. Keep the relaxed fatal
   escape condition > 2000 for 10m. This reduces routine noise without moving
   the existing staging fatal threshold. Production remains unchanged.

The load numbers are conservative starting points relative to current values,
not calibrated recommendations from observed workload history. Review recent
stg/pgnd series before deployment. CPU saturation and load average are different
signals; high runnable/I/O-blocked task counts can persist independently of CPU
utilization. Keep I/O-wait and unrelated failure alerts outside this relaxation.

Implementation details to retain:

- Split infra disk rules from the common rules with disjoint job selectors, so
  changes do not relax nodes or monitoring servers. Prefer preserving the disk
  alert name and alertclass where practical.
- Select relaxed nodes with `location=~"stg|pgnd"`, and exclude both from the
  existing strict rules. Inspect the inventory before choosing a positive
  production-only selector, to avoid losing future or unknown locations.
- Preserve location in CPU aggregation and remove the staging rules' hardcoded
  `location="stg"` alert label when extending them to pgnd.
- Existing CPU rules use `irate(...[5m])`. Consider a separate, explicitly
  assessed move to `rate(...[5m])` for smoother utilization; this also changes
  firing behavior and should not silently change production in this request.

Prometheus's [routing documentation](https://prometheus.io/docs/alerting/latest/configuration/#route)
confirms the sibling-route ordering/continue behavior used by the proposal.
Its [alert rule documentation](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
defines the continuous hold period, and its
[query function documentation](https://prometheus.io/docs/prometheus/latest/querying/functions/#irate)
recommends rate for alerts instead of irate. The installed pinned versions still
need configuration validation during implementation.

## Compatibility and deployment

- No database, API, client, daemon protocol, persistent format, or vpsAdminOS
  update is required. Rollback can load existing state. The proposed change
  affects generated central Prometheus and Alertmanager configuration only.
- An extra target label changes time-series and alert identity. Existing
  pending alerts may restart and old alert instances may resolve during rollout.
  Retaining alertclass preserves the intended inhibition relationships.
- VPS dataset auto-expansion is an operator-provided premise. The filesystem
  selector also covers `/run` and `/nix/store`; `/run` is normally tmpfs and is
  not fixed by dataset expansion. Record this limitation and consider a separate
  memory-backed filesystem alert rather than assuming every VPS filesystem grows.
- Deploy the narrow route exception to both alerts1/alerts2 first, then deploy
  target labels and rules to both mon1/mon2. An old monitor without the VPS label
  continues the old SMS behavior, so suppression is not complete until both
  monitors are updated. Old Alertmanager versions ignore the new label.
- No coordinated fleet/node update is needed. Rolling back monitor rules/labels
  or Alertmanager routes restores the old notification policy; document and
  verify alert identity changes during rollback.
- Building/deploying remains separate from explicit repository/master
  integration approval. The user has requested suggestions only in this turn.

## Documentation

Readers are the infrastructure operators and the future implementation team.
The proposal and evidence belong in this session plan while policy is undecided;
current progress belongs in state.md. No owning-project documentation update is
useful yet because there is no accepted behavior or implementation change.
If implemented, put a short explanation beside the route and relaxed policy
and record the individual rollout in this session.

## Testing plan

No build, rule evaluation, routing test, or deployment was run for this proposal.
Implementation acceptance should cover:

- Promtool threshold and hold-time boundaries for infra disk and stg/pgnd load;
  unchanged production, nodes, and monitorings behavior.
- Routing fixtures proving VPS critical disk alerts still reach email/Telegram
  and neither SMS receiver, while VM/physical alerts retain SMS; unrelated VPS
  critical alerts retain SMS. Check hourly repeats and inhibition semantics.
- Generated infra labels from representative container, VM, and physical
  inventory entries; pgnd retains its location after CPU aggregation.
- Quick checks and hooks, committed changes, then mandatory independent review
  including the whole branch and the explicit conclusion that no migrations exist.
- Central monitoring/alerter configuration builds under the repository Nix
  environment, delegated to the required fresh verification watcher; dry
  activation and controlled deployment only when that work is authorized.
