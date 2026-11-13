# 2026-11-13-oomd-restart-thresholds

## Goal

i'd like to decrease osctl-oomd restart hits on node25.prg to 4 (instead of 8) and to trigger on a bit lower loadavg, not sure what the threshold is now.

## Affected repositories

- `vpsfree-cz-configuration`: expected node25.prg-specific oomd settings.
- `vpsadminos`: read-only reference for pinned option/daemon semantics; no
  application changes planned.

## Approach

Architect investigates the current configured and, where accessible, running
settings and writes a bounded design brief. One implementer prepares the minimal
node-local configuration change, passes quick checks, commits and publishes its
feature branch. Independent final review precedes longer evaluation/build checks.
Prepare a concrete deployment candidate; repository integration requires explicit
approval for its target. Keep this session open.

## Decisions

- Restart hits: 8 to 4, as requested.
- Lower load-average threshold: select a modest reduction after identifying the
  current value and whether it is absolute or CPU-scaled.
- Avoid changing global defaults, daemon behavior, or unrelated nodes.

## Compatibility and deployment

Use existing configuration options with the existing pinned daemon. Assess mixed
versions, service restart effects and rollback in the design brief. No database,
API, protocol, client or persisted-format changes are intended. Deploy only the
named node under its machine reservation; configuration deployment does not
authorize master integration. Record exact input graph, system paths and rollback
baseline before any activation.

## Documentation

Readers are the node operator and future maintainers. Keep current choices and
execution evidence in this session; add project documentation only if existing
behavior needs clarification. Architect owns [design.md](design.md); lead owns
plan/state and manifest.

## Testing plan

Inspect option semantics, parse/format the changed Nix configuration, verify
evaluated node25 thresholds and unchanged relevant defaults, and run declared
hooks. Bound full-node builds by the configuration's normal procedure; stop an
unexpected kernel build. Review the complete committed base-to-head branch and
migration inventory before longer integration checks. Verify the installed
configuration and oomd health after any deployment.
