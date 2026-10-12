# Generic machine alert recipients

Lead-owned design and verification brief, recorded before implementation.
Scope authorized by the user's "ok, proceed with implementation" follow-up.
Lead investigates, designs and implements at retained Sol/xhigh settings;
ready `reviewer0` remains read-only at retained Astra/xhigh settings.

## Scope, interfaces and files

- Add nullable `cluster.<machine>.monitoring.alertRecipients`. Default `null`
  retains team delivery. A nonempty list of registered user IDs replaces it.
  Normalize order/duplicates; reject empty lists, unknown users and conflicting
  custom `monitoring.labels.fqdn` overrides on selected systems.
- Add a non-secret `data/monitoring.nix` contact registry and expose it through
  `data/default.nix`. Define current team email recipients and aither/snajpa's
  existing SMS daytime settings once. Private sachet configuration retains the
  transport destinations; new SMS contacts require matching sachet receivers.
- Generate exclusive routes and selected email receivers in
  `modules/clusterconf/alerter/default.nix`. Reuse mail and SMS route helpers
  for normal and exclusive policies. Preserve existing team receiver names,
  destination addresses, group timings, repeats and resolved notifications.
- Enable `[ "aither" ]` in aitherdev's `module.nix`.
- Extract the existing management-FQDN calculation into `lib/monitoring.nix`,
  used by both alerter and monitor. Monitor output must remain unchanged.
- Update `docs/services/monitoring.md` and focused Prometheus test fixtures;
  add a dedicated recipient check to flake checks if that keeps fixtures clear.

## Identity and routing invariants

1. Use existing identity labels without introducing metric/alert recipient
   labels. CPU/I/O aggregations retain FQDN but discard arbitrary custom labels.
2. Match `node_fqdn` first when it identifies the subject. Host-FQDN routes
   additionally require missing/empty `node_fqdn`, so an unselected node's
   alert cannot inherit the marked API/monitor host's policy.
3. Match exact primary FQDNs and existing generated management FQDNs for nodes.
   Do not use broad hostname-prefix regexes or alert-description matching.
4. Exclusive branches precede team routes and set `continue=false`. Their
   mail/SMS children may continue only among siblings within that branch.
5. Preserve `severity=none` blackholing. Branch fallback is selected-user mail,
   including missing/unknown severity; it must never inherit `team-mail`.
6. Warnings use selected mail; critical/fatal also use selected registered SMS.
   Critical keeps each user's existing daytime window; fatal remains always
   active. Frequency overrides and `send_resolved=true` retain current values.
7. Selected policies exclude shared Telegram. Unmarked systems retain existing
   team mail, shared Telegram and SMS behavior.
8. Generate routes and receivers only from ordinary (`carrier == null`)
   inventory records. Carried netboot copies share their node's metadata and
   must not duplicate receiver names. The regression uses pinned confctl's
   real expansion over ordinary real-cluster metadata.

## Implementation boundaries

Public HTTP/service and aggregate alerts without machine identity retain team
routing. Per-machine policy does not imply ownership of dependent systems,
public services or an entire development cluster. Handle existing `node_fqdn`
subjects explicitly, but do not infer subjects from names or descriptions.
No private Telegram transport, secrets changes, input updates, API/exporter
changes, integration into master or production deployment are authorized here.

## Compatibility, deployment and recovery

Only both Alertmanager replicas need the new runtime configuration. Machine
metadata is consumed at evaluation; exporter, monitor and aitherdev runtime
output must not change. No coordinated fleet updates are required. Defaults
preserve existing destinations; generated route paths may create new groups
and repeats. Old Alertmanager replicas can continue team delivery until both
are updated, so readiness for production use requires both configurations.

No schemas, persisted formats, API/client/CLI contracts, protocol formats or
migrations change. Existing Prometheus/Alertmanager state remains readable by
old and new versions. Rollback to both previous alerter configurations restores
team delivery without deleting state. A separately authorized rollout should
build, inspect activation, deploy both replicas and verify reload/routing health.
Implementation authorization does not include integration or live delivery tests.

## Acceptance criteria and quick checks

- Real aitherdev metadata selects aither. Null, normalized multi-user, empty,
  unknown and conflicting-FQDN selections have the documented evaluation result.
- Actual Alertmanager `amtool` checks exact selected/default receiver sets for
  warning/critical/fatal/none and missing/unknown severity, hourly/daily frequency,
  primary/management/node-subject identities, unselected/lookalike hosts, and
  alerts with a marked scrape host but an unselected `node_fqdn` subject.
- Selected email contains only chosen addresses, and optional SMS belongs only
  to those users. Shared receivers are absent from selected paths.
- Inspect generated SMS routes and nested frequency routes for exact critical
  daytime policies and no fatal restriction. Offline route tests do not exercise
  real daytime activation, timers, inhibition or delivery; state those limits.
- Existing monitoring checks retain default route/timing and label invariants.
- Run Nix syntax/format, shell syntax and focused evaluation/receiver checks in
  the pinned environment. Install and run mandatory Overcommit hooks; no bypass.
- Commit the complete deliverable and inventory the whole branch before final
  independent review. No migration or repeated input stream is expected.

## Longer checks after final review

Use a fresh Luna/low watcher to run focused flake checks and
`confctl build 'cz.vpsfree/containers/prg/int.alerts[12]'` in the pinned shell.
Use the repository's real selector syntax, confirmed from `confctl` help.
Compare monitor/aitherdev generated configuration with the base if the shared
helper or metadata causes unexpected differences. Cancel only an unexpected
owned local kernel build and investigate its cache provenance. Publish the
feature branch and handle any branch CI, retaining it awaiting explicit merge
direction. No production deployment in this implementation turn.
