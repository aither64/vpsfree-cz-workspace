# cgroup v1 device access after VPS soft deletion

## Goal

Determine why `osctl healthcheck -a` reports devices that are configured for a
container but missing from its cgroup v1 device allow-list after the
corresponding VPS is soft deleted in vpsAdmin. Establish whether the fault is
in vpsAdmin's soft-delete transaction, the vpsAdmin-to-node command path, or
vpsAdminOS/osctld's cgroup v1 device handling. Do not implement a fix unless the
user expands the request.

## Affected components

- `vpsadmin`: soft deletion of a VPS/container, device policy calculation, and
  node commands that change the VPS's state or configuration.
- `vpsadminos`: osctld container device configuration, cgroup v1 allow/deny
  application, persistence, and the `cgroup_device_list` health check.

Additional repositories will be added only if the command or deployment path
proves that they participate in the faulty transition.

## Approach

1. Inspect repository-local instructions and history in both candidate
   repositories.
2. Trace the vpsAdmin soft-delete transaction and all node commands it emits,
   with special attention to changes in user/group ownership and device
   inheritance.
3. Trace osctld's configured-device model, effective cgroup v1 policy, and
   health-check comparison.
4. Reconstruct the failing transition from code and existing tests. Run a
   focused reproduction or focused tests if the available development
   environment can do so without a kernel rebuild.
5. Report the root cause, occurrence conditions, immediate recovery mechanism,
   and likely repair boundary, clearly distinguishing proven facts from
   inference.

## Compatibility and deployment analysis

This investigation makes no runtime, API, schema, protocol, or persisted-state
change. A later fix must preserve mixed-version operation between vpsAdmin and
vpsAdminOS unless evidence shows that a coordinated deployment is unavoidable.
Any proposed repair must consider persisted osctld container configuration,
cgroup v1 versus v2 behavior, stopped and running containers, repeated soft
deletion, restore/recovery, and rollback to a version that reads state written
by the fix. No coordinated node update is expected from the investigation
itself.

## Testing plan

- Use focused unit/spec coverage around soft-delete state transitions and
  device policy updates where available.
- Compare configured and effective device lists before and after the relevant
  command sequence.
- If an integration reproduction is necessary, use the vpsAdminOS test runner
  in its documented Nix environment and the default bridge network; stop if an
  unexpected kernel build starts.

## Decisions

- Treat `vpsadmin` and `vpsadminos` as candidates until the cross-repository
  command trace identifies the actual faulty boundary.
- Keep this turn diagnostic-only, matching the user's request to find the root
  cause.
