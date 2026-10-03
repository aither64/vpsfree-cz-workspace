# Architect result

Design is ready for implementer0 in [design.md](design.md), based on
`b66c929bb7c202ad31bd8994a691ade14c40ebf0`. No deviation from accepted scope.

Recommended assignment: implement the typed machine metadata, three explicit
VM classifications, four authoritative host label constructors, exact terminal
SMS exception, and four CPU rule edits listed in the design. Add the focused
Nix/promtool/amtool fixtures and a short owning-project monitoring explanation.
Use the pinned shell, verify declared hooks, run quick verification, and commit
only the owned configuration changes. Application work has not begun here.

Important details for implementation:

- `monitorings` is the Nix target group; its actual job is `mon`. Include its
  local Prometheus/node-exporter pair and peer monitor targets.
- Append `machine_type` after `monitoring.labels`. Keep `type=node`; shared
  node labels also cover both ZFS jobs and IPMI.
- Reuse `blackhole` after email/Telegram and before both SMS routes. All four
  exact matchers are required; keep hourly notification subroutes unchanged.
- Only relaxed CPU aggregates retain `location`; remove their hardcoded stg
  labels. Do not touch raw load-average or I/O-wait rules.
- With 20-second rule samples, the first `irate` is at 20s, so hold-boundary
  fixtures fire at 10m20s/50m20s for already-old hosts, not t=10m/50m.
- Offline amtool routing tests verify receiver selection, not real delivery,
  repeat timers, inhibition or active-time behavior. Preserve those structures
  and verify their diff separately.

Proposed check commands are in the brief:
`nix build --no-write-lock-file --no-link .#checks.x86_64-linux.infra-monitoring-config .#checks.x86_64-linux.infra-monitoring-rules`,
then adjacent process-count/autostart regressions and declared Overcommit hooks.
The flake exposes `confctl.machines` for metadata, but not complete system
configuration objects; use a small module fixture for generated labels/routes.

After commits and quick checks, the lead owns mandatory whole-branch review,
including a no-migrations conclusion. Only then run both central configuration
builds through a fresh verification watcher:
`confctl build 'cz.vpsfree/containers/prg/int.mon[12]'` and
`confctl build 'cz.vpsfree/containers/prg/int.alerts[12]'`.
Confirm the selectors first; explicit single-machine builds are equivalent.

Execution path is available: the lead confirmed the authorized fresh watcher
entered the pinned shell and installed all 40 gems with the frozen bundle.
Use that watcher for functional Nix checks and the lead's captured pinned-shell
environment for implementer quick commands; verify hook installation/activation.
This member's failed daemon access during an offline source-path evaluation
does not block implementation. No build/test ran here. Fixture/package
feasibility was checked from source, not executed. Existing checks already use
`pkgs.prometheus.cli`; local nixpkgs source provides amtool via
`pkgs.prometheus-alertmanager`, whose pinned resolution remains to be checked.

Only design.md and this report were created. No application edits, commits,
deployment, integration, input changes or cleanup. Lead should link these
documents and record design completion in state/portal under normal cadence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/.
Session remains open.
