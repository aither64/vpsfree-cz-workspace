# 2026-11-13-osctl-oomd-common-config

## Goal

Move the existing node25.prg osctl-oomd restart-hit and load-average settings to
the shared node configuration so every node uses the same tuning.

## Affected repositories

- Expected: `vpsfree-cz-configuration`; architect verifies exact ownership.

## Approach

Architect identifies the existing values, common imports and a bounded verification
brief in [design.md](design.md). One implementer moves the configuration, runs
quick checks, commits and publishes the feature branch. Independent final review
follows committed changes and quick checks.

## Decisions

- User clarification: "just change configuration, no deployment".
- Preserve the exact node25 tuning; avoid unrelated configuration or pin updates.
- No merge is authorized. Publish the feature branch and leave integration pending.

## Compatibility and deployment

Existing options and values move between configuration modules; no schema,
protocol, software or persistent-state changes are intended. Confirm that the
common module reaches all intended nodes without enabling oomd on other hosts.
Mixed deployed configurations remain supported; no coordinated update is needed.
No deployment, machine reservation, activation or runtime changes are in scope.
Reverting the configuration commit restores the previous per-node settings.

## Documentation

Readers are maintainers reviewing node policy. Keep this small move self-explanatory
in the existing configuration; preserve design rationale and check results in
session records. No new project documentation is expected unless investigation
finds a consequential invariant needing explanation.

## Testing plan

Use repository guidance for Nix syntax/format checks and inspect the complete diff.
Verify node25's overrides disappear and all nodes import the shared settings.
Prefer focused evaluations of the changed options over full system builds; any
uncertain or longer checks require the monitoring workflow after final review.
