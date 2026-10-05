# Prepared monitoring rollout

Status: prepared rollout; deployment is owned by the user. The reviewed revision
was merged into remote master by fast-forward after explicit approval:
`7e32833aca1cb65902b50f61eb76dd1022691591`. Both monitoring-host builds passed
at that head: mon1 generation
`2026-10-03--20-47-18` and mon2 generation `2026-10-03--20-51-51`. Neither was
activated. See [verification.md](verification.md) for results and evidence.

## Prerequisites

Use the integrated configuration revision from master in the operator's
configuration checkout and enter `nix develop`. Confirm the revision against
session state and inspect the completed independent review and both monitoring
host builds. Record current monitor generations before activation. The user
has retained responsibility for executing this deployment; no agent activation
has been performed.

## Activation and verification

1. Dry-activate and inspect both exact targets using confctl:
   `cz.vpsfree/containers/prg/int.mon1` and
   `cz.vpsfree/containers/prg/int.mon2`.
2. Activate the reviewed monitoring configuration on both targets using the
   normal confctl deployment workflow. Until both update, an old monitor can
   still emit the faulty regex failure and critical Newadmin alerts.
3. On each monitor, query its localhost blackbox exporter with module
   `newadmin_vpsfree_cz_http_2xx`, target
   `https://newadmin.vpsfree.cz/build-info.json`, and `debug=true`. Require
   `probe_success 1`, HTTP 200 and no regex failure. Repeat with module
   `newadmin_bff_vpsfree_cz_http_2xx` and target
   `https://newadmin.vpsfree.cz/healthz`. This is read-only verification.
4. Inspect each Prometheus server's loaded rules. Require all nine dedicated
   Newadmin alerts to have severity warning. The API, console and legacy WebUI
   ExporterDown/WebDown rules remain critical. Shared infrastructure severities
   remain as configured. Confirm both monitoring scrape results after their
   next 300-second interval and allow old critical alert instances to resolve.
5. Confirm Alertmanager sees the new severity labels through existing routing.
   Do not provoke production outages or send synthetic notifications.

These probes do not certify interactive login or full WebUI functionality.

## Recovery

If activation fails, retain the generation records and diagnose the failed
monitor. Restore its recorded previous generation through the normal confctl
workflow if directed. A whole-change rollback restores the compact-body false
failure and prior critical Newadmin labels. Prefer a targeted software
correction that preserves the user-approved warning-only policy. There are no
application, database, API or persisted-state changes to undo.
