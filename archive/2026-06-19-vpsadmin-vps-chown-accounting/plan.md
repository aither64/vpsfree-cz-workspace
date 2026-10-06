# 2026-06-19-vpsadmin-vps-chown-accounting

## Goal
Investigate and fix leaked IP address resource accounting when a VPS ownership
change fails during the chown transaction rollback. Provide an operator-safe way
to repair already leaked accounting for affected accounts.

## Affected repositories
- `vpsadmin`: API/resource accounting and VPS chown transaction logic.
- `vpsfree-maintenance-tasks`: one-off production repair script for already
  leaked IP resource accounting.
- `vpsfree-cz-configuration`: deploy vpsAdmin through the `vpsadmin` channel
  after the fix is merged.

## Approach
- Trace the VPS chown transaction, especially owner resource transfer and
  rollback ordering.
- Reproduce or unit-test the resource accounting failure path where chown
  succeeds far enough to move accounting but a later VPS start action fails.
- Fix the rollback/accounting logic and add focused coverage.
- Add a maintenance script for existing incorrect IP address accounting.
- Update the `vpsadmin` channel in `vpsfree-cz-configuration` using `confctl`
  once the vpsAdmin fix is on `master`.

## Compatibility and deployment
- API/database semantics must remain backward compatible. The repair script must
  default to dry-run output, require explicit execution, and must not require a
  coordinated vpsAdminOS update.
- No protocol or persistent on-disk vpsAdminOS format change is expected.
- Mixed-version deployment concern is limited to the API process running the
  corrected chown code; failed transactions before deployment may still need the
  repair path.
- The configuration update only moves the `vpsadminServices` flake input to a
  commit already merged to `vpsadmin` `master`; no schema, protocol, or
  vpsAdminOS coordinated rollout is required.

## Testing plan
- Run focused API specs covering VPS chown resource accounting success and
  rollback behavior.
- Run Ruby syntax checks for the maintenance script.
- Run relevant API lint/spec checks for touched files before committing.
- Run mandatory change review after intended code changes are committed and
  quick local verification passes.
- Verify the updated `vpsadmin` channel revision with `confctl inputs channel
  ls` before pushing the configuration commit.
