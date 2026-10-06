# User Namespace Map Repair Plan

## Goal

Add a production maintenance script that finds VPS rows whose
`user_namespace_map_id` points to a map owned by another user, and repairs them
through vpsAdmin transaction chains rather than direct SQL.

## Affected Repositories

- `vpsfree-maintenance-tasks`: add an operator script.
- `vpsadmin`: read-only reference for model and transaction-chain behavior.

## Compatibility And Deployment

- No schema, API, protocol, or Nix module changes.
- Script is operational only and should be run manually on the vpsAdmin API
  host.
- Repair must queue the same node-side UID/GID map use, chown, and disuse
  transactions that `TransactionChains::Vps::Update` would queue, but through
  `TransactionChains::Maintenance::Custom` so the script can also send mail and
  wait for the VPS' configured maintenance window.
- Direct SQL updates are avoided because they would leave node runtime state
  inconsistent.

## Approach

- Preserve the existing `2023-09-22-fix-vps-userns-map` task, which fixes a
  narrower case where the current map row is missing.
- Add a new dated task for the current cross-owner mismatch, where the current
  map exists but belongs to another user.
- Scan VPSes where `vpses.user_namespace_map_id` points to a map whose
  `user_namespace.user_id` differs from `vpses.user_id`.
- For each VPS, show the current wrong map and candidate maps owned by the VPS
  owner.
- For each VPS, show whether mail will be sent, which language will be used,
  and whether the chain will wait for the configured maintenance window.
- Support interactive confirmation for all mismatched VPSes and `--vps ID` to
  handle only a selected VPS.
- Support `--map ID` when a selected VPS owner has multiple candidate maps.
- Send a short English/Czech inline notification by default, but allow
  `--no-mail`. Skip mail when the user has disabled mail delivery.
- Wait for the VPS' configured maintenance window by default, with
  `--no-maintenance-window` for immediate execution and `--reserve-minutes N`
  to set the remaining-window requirement.
- Support custom migration-style finish scheduling with `--finish-weekday DAY`
  and `--finish-time HH:MM` or `--finish-minutes N`. This uses
  `VpsMaintenanceWindow.make_for`, so the repair waits for temporary windows
  beginning at the selected finish day/time instead of the VPS' configured
  windows.
- Support `--dry-run` for review-only execution.

## Testing

- Ruby syntax check.
- `--help` smoke check if local environment can run the script without the
  production vpsAdmin wrapper.
- ERB render check for both inline mail languages.
- Option validation checks for incomplete finish config, out-of-range finish
  time, finish config with `--no-maintenance-window`, and duplicate finish time
  sources.
- Whitespace check for the new task file.
