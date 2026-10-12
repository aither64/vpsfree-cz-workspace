# Selected recipients for machine alerts: investigation and proposal

Initial investigation, subsequently implemented after user approval. See
[current state](state.md), [final design](design.md) and [review](review.md).
No production deployment has occurred. The user first requested an
aitherdev-only solution, then asked for a generic way to mark systems whose
alerts should go only to selected users.

## Current configuration

Investigated fetched `vpsfree-cz-configuration` `origin/master` at
`8e4da52c55f1d4396547630d1d4de518f8255619`. The relevant monitoring files
match the canonical local master at `23412037590f1d31b85a53410946a18b36db8bc8`.

- `modules/cluster/default.nix` defines per-machine monitoring metadata, but
  currently has no recipient selection.
- `modules/clusterconf/monitor/default.nix` labels aitherdev's exporter and
  ping targets with `fqdn=aitherdev.int.vpsfree.cz` and `alias=aitherdev.int`.
- `modules/clusterconf/monitor/rules/infra.nix` preserves FQDN explicitly in
  CPU and I/O aggregations. Filesystem, systemd and exporter-down alerts retain
  it from their input series.
- `modules/clusterconf/alerter/default.nix` sends warning/critical/fatal mail
  to three addresses, critical/fatal alerts to shared Telegram, and SMS to
  aither and snajpa. Aither's critical SMS window is 07:00–22:00 Europe/Prague;
  fatal SMS is unrestricted. Rule-specific frequency overrides apply.
- Both `cz.vpsfree/containers/prg/int.alerts1` and `int.alerts2` use the same
  alerter module. Both monitors send to the configured Alertmanager replicas.

## Recommended interface

Add `monitoring.alertRecipients` to cluster machine metadata:

```nix
cluster."cz.vpsfree/machines/aitherdev".monitoring.alertRecipients = [ "aither" ];
```

Other systems can select several registered users, for example
`[ "aither" "snajpa" ]`. The default `null` preserves existing team routing.
A nonempty list replaces team recipients for that system. Reject empty lists
and unknown users at evaluation time; this setting is not a silencing switch.
Normalize duplicate/order handling so contact and receiver names stay stable.

Keep a small shared contact registry in `data/monitoring.nix`, imported by
`data/default.nix`. Store email addresses and references to existing SMS
receivers/daytime policies, not credentials. Aither's email is
`aither@havefun.cz`, with the existing `sms-aither` route. Users without an SMS
contact receive email. Shared Telegram is excluded for selected-recipient
systems; private Telegram can be added when individual chat IDs are configured.
Do not require private Telegram setup for the initial feature.

## Route generation

Generate exclusive branches from marked machine metadata, before the ordinary
team routes. Each branch matches existing machine identity labels and has
`continue = false`. Within the branch:

1. Route `severity=none` to the existing blackhole.
2. Deliver warning/critical/fatal mail to the selected users only, retaining
   mail timing and `intervalRoutes` frequency overrides.
3. Deliver critical/fatal SMS only to selected users with configured SMS,
   retaining their existing daytime and fatal policies.
4. Set the branch's fallback receiver to selected-user email, so a missing or
   unexpected severity cannot inherit root `team-mail`.

Use shared helpers for mail and per-user SMS route construction so default and
exclusive routing share timing definitions. Preserve unmarked systems' current
routes and receivers. Email children continue to SMS siblings *inside* the
exclusive branch; the branch itself must never continue into team siblings.
Inactive SMS routes must also remain inside that branch.

Alertmanager documents that matching children stop subsequent sibling traversal
when `continue=false`, and unspecified route settings inherit from the parent:
[routing configuration](https://prometheus.io/docs/alerting/latest/configuration/#route).

Do not introduce recipient labels on every metric. Custom `monitoring.labels`
are absent from ping-target construction, and CPU/I/O aggregations discard
arbitrary extra labels. Generating routes from existing identity avoids new
time series, modified alert identities, monitor deployment and rule edits.

## Identity boundaries for a generic implementation

An exact primary FQDN covers aitherdev's current host alerts. Broader support
must cover the existing alternate identity paths explicitly:

- Node management probes use `<host>-mgmt.<location>.<domain>` as `fqdn`.
  Include the generated management identity for marked nodes.
- Download-pool checks identify their subject with `node_fqdn`, not `fqdn`.
  Generate subject-label routes ahead of scrape-host routes, and ensure a
  subject alert cannot be captured by a monitoring/API host's recipient policy.
- Public HTTP/service and global aggregate alerts without machine identity
  keep their service/team routing. Marking one host does not implicitly claim
  an entire public service or its dependent systems.
- Custom identity-label overrides must be checked when selecting a system;
  reject conflicting overrides or explicitly support their effective identity.

Tests should establish these supported identity classes. Inventory other
cross-system API metrics before claiming that every event associated with a
marked node is covered; labels inferred from alert descriptions are insufficient.

## Implementation scope and acceptance checks

Likely files: cluster metadata option; shared contact registry and import;
alerter route helpers/generation; aitherdev's `module.nix`; monitoring policy
documentation; existing Prometheus configuration/routing fixtures.

Extend `tests/prometheus/infra-monitoring-config.nix` and
`tests/prometheus/infra-monitoring-routing.sh`. The config fixture currently
asserts exactly five routes by numeric position and will need to distinguish
default routes from generated exclusive routes.

Check exact receiver sets for default, one-user and multiple-user policies;
warning/critical/fatal/none and missing severity; both daytime and nighttime;
hourly/daily overrides; resolved configuration; exporter, filesystem, systemd
and CPU identities; management probes and node-subject identities. Include
lookalike/unknown hosts, conflicting identity labels, invalid recipients and
empty selections. For exclusive policies, assert the absence of team mail,
shared Telegram and unselected SMS. Existing offline `amtool` tests verify
receiver selection but do not exercise delivery, daytime activation, timers or
inhibition; add appropriate assertions or a controlled clock check for those
policies instead of claiming offline routing verifies them.

Implementation should use the pinned Nix shell and mandatory hooks, commit all
intended changes, pass quick checks, then receive retained independent final
review including complete branch history and the no-migration conclusion.
Long checks/builds follow review under the utility-watcher workflow. Evaluate
the focused monitoring config check and build both Alertmanager machines;
review activation changes before a separately authorized rollout.

## Compatibility, deployment and recovery

Only both Alertmanager replicas need new runtime configuration. Metadata and
contact definitions are evaluation inputs; no aitherdev, exporter, monitor or
fleet update is required if existing identity labels remain unchanged. No API,
client, daemon protocol, database schema or persisted-state migration is needed.

During mixed Alertmanager configurations, an old replica can still send team
notifications. The exclusive policy is effective only after both replicas use
the new configuration. Verify loaded routes/reload health on both replicas and
then verify delivery with controlled alerts if separately authorized. Routing
changes can cause fresh notification groups/repeats. Existing state is retained.

Restoring both prior Alertmanager configurations restores team delivery and can
read the existing state. No state deletion or schema rollback is necessary.
No implementation, review, build or deployment was performed in this investigation.
