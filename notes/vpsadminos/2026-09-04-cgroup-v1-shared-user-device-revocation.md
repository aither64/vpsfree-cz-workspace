# cgroup v1 container device removal affects siblings

Related initiative:
`archive/2026-09-04-cgroup-v1-soft-delete-devices/`

## Symptom

`osctl healthcheck -a` reports a configured device such as
`c 10:200 rwm` as not allowed for one or more containers. The affected
containers share an osctl user with a container whose promoted device was
removed.

## Cause

The cgroup v1 container configurator applies add, remove, and change operations
to both container-specific cgroups and `<group>/<user>`. The latter is a shared
ancestor for every container assigned to that osctl user. Removing a device
from one container writes to the shared ancestor's `devices.deny`, so cgroup v1
revokes the device from all descendants. The sibling container configurations
are unchanged, which makes the health check detect a mismatch between their
configured devices and effective `devices.list`.

Normal vpsAdmin soft deletion does not remove feature devices. It stops the
container, removes routes, and disables resource accounting. Check transaction
history for a nearby VPS-features/device-removal operation instead of assuming
the soft-delete transition itself wrote the deny rule.

## Reproduction and verification

In the vpsAdminOS `cgroups/devices-v1` debug VM:

1. Create two containers with the same osctl user.
2. Add TUN to both using `osctl ct devices add -p ... char 10 200 rwm
   /dev/net/tun`.
3. Verify `osctl healthcheck -a` is clean.
4. Run `osctl ct devices del` for TUN on only one container.

The shared user cgroup and the sibling's container cgroup both lose TUN. The
health check reports the sibling with `device "c 10:200 rwm" not allowed`.
One and two consecutive `osctl ct stop` calls do not reproduce the problem.

Re-allowing the device at the ancestor does not automatically restore an
existing descendant's allow-list. Reapplying that sibling's device
configuration is also required; starting the stopped sibling did so in the
test and restored a clean health check.
