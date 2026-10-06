# 2026-08-04-nodectld-crash

## Goal

Prevent `nodectld` from crashing when export-mount collection encounters a
running container for which osctld has no cached init PID. Preserve the current
behavior of skipping publication until the mount namespace is available.

## Affected repositories

- `vpsadmin`: owns `libnodectld`, the export-mount API/supervisor code, and the
  node daemon deployment package. This is the only repository to change.
- `vpsadminos`: read-only source reference used to confirm how osctld caches and
  refreshes container init PIDs.
- `vpsfree-cz-configuration`: read-only reference used during the incident
  investigation; no configuration change or deployment is planned.

## Approach

1. Make `read_vps_mounts` consistently return an array by returning an empty
   array when `ct.init_pid` is nil.
2. Add focused regression coverage proving the reader does not access `/proc`
   and the update path neither publishes nor raises in this state.
3. Commit the implementation and regression spec together with mandatory hooks
   enabled.
4. Run the required standalone change review after quick verification, then run
   the full libnodectld spec suite.

## Compatibility and deployment

The fix is internal to libnodectld and does not change the RabbitMQ payload,
API, schema, persisted state, or configuration. Older and newer nodectld
instances can run concurrently against the same supervisor. Deployment can be
rolling, and rollback requires no state conversion; it only restores the crash
behavior for a missing init PID.

## Testing plan

- Run a focused spec for `NodeCtld::ExportMounts` with a nil init PID.
- Run RuboCop on the changed implementation and spec and run `git diff --check`.
- Run mandatory Overcommit hooks during the commit.
- Run the required standalone change review.
- Run the full libnodectld RSpec suite after review. A VM integration test is
  unnecessary because the change only restores an internal return contract.
