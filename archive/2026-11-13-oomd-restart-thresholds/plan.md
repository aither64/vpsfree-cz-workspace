# 2026-11-13-oomd-restart-thresholds

## Goal

i'd like to decrease osctl-oomd restart hits on node25.prg to 4 (instead of 8) and to trigger on a bit lower loadavg, not sure what the threshold is now.

Delivered: node25-only restart hits 4 and load multiplier 1.5, as explicitly
selected by the user, merged to remote configuration master at 08d68a85. No
deployment in scope. Review/quick checks/focused canonical JSON validation passed;
full-node build was attempted but lacks its external initrd key. See [state](state.md).

## Affected repositories

- `vpsfree-cz-configuration`: expected node25.prg-specific oomd settings.
- `vpsadminos`: read-only reference for pinned option/daemon semantics; no
  application changes planned.

## Approach

Architect investigates the current configured and, where accessible, running
settings and writes a bounded design brief. One implementer prepares the minimal
node-local configuration change, passes quick checks, commits and publishes its
feature branch. Independent final review precedes longer evaluation/build checks.
User clarified this is configuration-only work; deployment belongs to the user.
Repository integration requires explicit approval for its target. Keep this
session open.

## Decisions

- Restart hits: 8 to 4, as requested.
- Lower load-average threshold: node-local multiplier 2.0 to 1.5, a 25%
  reduction for the same rolling median. Activation compares 1-minute host load
  with the median of up to 24 hours of 15-second samples; it is not absolute or
  CPU-scaled. User explicitly selected 1.5x median, superseding the initial 1.8
  proposal. Existing memory and CPU guards remain.
- Avoid changing global defaults, daemon behavior, or unrelated nodes.

## Compatibility and deployment

Use existing configuration options with the existing pinned daemon. Assess mixed
versions, service restart effects and rollback in the design brief. No database,
API, protocol, client or persisted-format changes are intended. No deployment,
live verification or machine reservation is in scope. Existing deployment and
recovery guidance is operator context only.

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
configuration locally. Deployment/live checks belong to the operator.
