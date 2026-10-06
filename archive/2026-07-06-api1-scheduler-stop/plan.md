# 2026-07-06-api1-scheduler-stop

## Goal

Run a one-off command on `api1.int.vpsfree.cz` during the night:

```sh
systemctl stop vpsadmin-scheduler
```

The intended time is `2026-07-07 01:10` in the node's local timezone.

## Affected repositories

- `vpsfree-cz-configuration`
  - Worktree:
    `worktrees/2026-07-06-api1-scheduler-stop/vpsfree-cz-configuration`
  - Branch: `2026-07-06-api1-scheduler-stop`

## Approach

- Add an `api1`-local systemd one-shot service that runs
  `systemctl stop vpsadmin-scheduler.service`.
- Add a matching systemd timer with an absolute `OnCalendar` timestamp:
  `2026-07-07 01:10:00`.
- Keep the timer non-persistent, so a missed deployment does not stop the
  scheduler later at an unexpected time.

## Compatibility and deployment

- No persisted state, database schema, API contract, generated client,
  protocol, or on-disk format changes are involved.
- The change affects only `api1.int.vpsfree.cz`, adding one transient timer
  unit and one one-shot service unit.
- The existing health check still expects `vpsadmin-scheduler.service` to be
  active. Stopping the service may therefore alert unless operators silence or
  otherwise handle that separately.
- `api1` imports `environments/base.nix`, where `time.timeZone` is
  `Europe/Amsterdam`; on `2026-07-07` this is CEST and matches the intended
  night maintenance time.
- Mixed-version operation is unaffected. The configuration must be deployed to
  `api1` before `2026-07-07 01:10:00`.
- After the maintenance window, remove the timer/service from configuration to
  avoid stale operational intent.

## Testing plan

- Run `nixfmt` on the touched Nix file.
- Run `confctl build "cz.vpsfree/vpsadmin/int.api1"`.
- Install/verify Overcommit hooks before committing, then commit with
  `git commit -F`.
- Run mandatory change review after the commit and quick local verification.
