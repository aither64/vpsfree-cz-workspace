# 2026-11-13-osctl-oomd-common-config

## Goal

Move the existing node25.prg osctl-oomd restart-hit and load-average settings to
the shared node configuration so every node uses the same tuning.

2026-11-23 addition: merge that reviewed change, then update the vpsadminos and
vpsadmin roles in production, staging and os-staging through confctl channels.

## Affected repositories

- `vpsfree-cz-configuration` only: shared `cluster/cz.vpsfree/nodes/common/all.nix`
  and `cluster/cz.vpsfree/nodes/prg/node25/config.nix`.
- New input-update milestone: same repository's channel-owned generated lock
  inputs; architect verifies mappings and compatibility before implementation.

## Approach

Architect identifies the existing values, common imports and a bounded verification
brief in [design.md](design.md). One implementer moves the configuration, runs
quick checks, commits and publishes the feature branch. Independent final review
follows committed changes and quick checks.

## Decisions

- User clarification: "just change configuration, no deployment".
- Preserve the exact node25 tuning; keep the newly requested pin updates separate.
- Accepted design: `restart_hits = 4`, `load_multiplier = 1.5`; use the existing
  shared settings block reaching 13 nodes, including staging and prg/backuper2.
- 2026-11-23 user: "merge this. I'd also like you to update channels vpsadminos
  and vpsadmin in all channels (production, staging, os-staging)." This authorizes
  the reviewed oomd move into vpsfree-cz-configuration/master after the disclosed
  missing-secret build gap. Refresh/check its exact patch before the short claim.
  The subsequent channel updates are a separate milestone; their integration
  approval is not inferred from the preceding "merge this".
- Subsequent explicit user "merge" approves the reviewed channel updates into
  the same repository/master. Both milestones are now merged; exact receipts
  are in state.md. Full-system build evidence remains limited by the disclosed
  missing external initrd host key; no successful realization is claimed.
- No deployment remains in force. Do not broaden input selection beyond requested
  channel roles and their necessary transitive lock changes.

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
The repository's AGENTS.md requires `confctl build` for changed nodes. After final
review use a fresh watcher for `confctl build 'cz.vpsfree/nodes/*'` (all 13), with
an initial ten-minute reassessment and a stop on unexpected kernel builds. Builds
do not authorize deployment. Do not run any deploy or dry-activation command.
