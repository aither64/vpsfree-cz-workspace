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

- Keep this turn diagnostic-only, matching the user's request to find the root
  cause.
- The faulty boundary is vpsAdminOS's cgroup v1 container device
  configurator. It mutates the per-user ancestor cgroup as if that cgroup were
  private to one container, although multiple containers can share it.
- Normal vpsAdmin soft deletion is not the device-policy writer. It stops the
  VPS, clears routes, and disables resource accounting; it does not run the
  features command or remove devices. Treat the observed timing as a
  correlation until the transaction history identifies the device-removal
  operation that preceded the health-check failure.
- A later fix should be local to vpsAdminOS unless operational evidence reveals
  a separate vpsAdmin trigger. It must keep the shared ancestor permissive for
  every device required by any container below it and reapply affected child
  cgroups where necessary.

## Result

The failure was reproduced in the cgroup v1 test VM with two containers under
the same osctl user. Removing promoted TUN access from one container wrote a
deny rule to their shared `<group>/<user>` devices cgroup. The kernel therefore
removed access from the sibling's descendant cgroup while the sibling's osctld
configuration still contained TUN. `osctl healthcheck -a` then reported the
same `device "c 10:200 rwm" not allowed` error shape as production.

Stopping the container once or twice did not alter its device lists and left
the health check clean. Re-allowing the device at the ancestor was insufficient
to update an already-restricted descendant; starting the affected sibling
reapplied its configured devices and restored a clean health check.
