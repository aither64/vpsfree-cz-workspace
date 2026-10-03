# Functional quick checks requested

Implementer0 has staged all 15 owned application/fixture/documentation paths in
the configuration worktree. HEAD remains the assigned base
`b66c929bb7c202ad31bd8994a691ade14c40ebf0`; no application commit yet. Leave the
staged changes in place for Git flake visibility. No deployment, input update,
push, integration or long system build is requested.

Run through a fresh lead-owned verification watcher from
`worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration`:

```sh
nix eval --impure --no-write-lock-file --json .#confctl.machines \
  --apply 'ms: builtins.mapAttrs (_: m: { inherit (m.metaConfig) machineType; }) ms'
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.infra-monitoring-config \
  .#checks.x86_64-linux.infra-monitoring-rules
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.vps-autostart-prometheus-rules \
  .#checks.x86_64-linux.process-count-prometheus-rules
```

The config derivation evaluates real metadata, validates the enum, and directly
imports the production monitor/alerter modules. It checks both monitors' local
and peer labels, infra VPS/VM/physical hosts, shared node/ZFS/IPMI labels and
custom-label conflicts. Fixtures supply only inventory lookup and inert
receiver names; routes and intervals come from production. Amtool covers the
exact exception and all negative routing cases, and promtool covers filesystem
labels, mounts and five minute timing. The separate CPU derivation imports only
the four production CPU usage rules and checks full ALERTS labels at exact
10m/10m20s and 50m/50m20s boundaries, both relaxed locations, missing location,
threshold equality, non-vpsAdminOS hosts, two-core averages and boot boundaries.

Known quick static evidence: the pinned bundle is satisfied; Overcommit was
installed and signed without bypass; pinned Nixfmt formatted all changed Nix
files; Bash syntax and staged whitespace checks passed. Byte comparison proves
common.nix/infra.nix, flake.lock and Gemfile.lock unchanged, and nodes.nix has
exactly the four approved CPU rule edits. Full Overcommit run is next while the
watcher runs. Functional fixture mechanics remain unverified until these checks
pass; return concrete failures for implementer correction.

After the lead confirms the requested quick checks pass, implementer0 will
create the required two behavior commits, with corresponding tests/docs and
active hooks, then write implementation-result.md. No migration or obsolete
intermediate application history is introduced. The lead owns tracking and
whole-branch independent review before the longer central system builds.

## First watcher result and fixture correction

The first watcher passed metadata evaluation, then stopped focused evaluation
at `sv.monitor` in target filtering. The fixture had added synthetic ZFS/IPMI
service ports without the `monitor` field supplied by real metadata. Both
synthetic services now include `address`, `port` and `monitor = null`; the
fixture was formatted and staged again. No production source changed. The two
focused checks and adjacent regressions require a fresh watcher rerun.
The full declared Overcommit run passed before this fixture-only correction.
