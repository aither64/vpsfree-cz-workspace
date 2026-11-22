# Cgroup v2 parent device denial and container BPF programs

Initiative: `work/2026-09-05-cgroup-v1-shared-device-fix`.

The first expanded `./test-runner.sh test cgroups/devices-v2` run passed all
effective-access checks but failed an assertion that recursive parent-group
device deletion would reset each container's BPF program to its initial name.
The expected name was `946a3e34004`; the container retained `858012c51ba`, its
read-only TUN program. The parent program was replaced with the default policy,
and both read and write opens were denied in both containers with `EPERM`.

`Devices::V2::GroupManager#children` traverses child groups, while its v1
counterpart also traverses containers. Thus the v2 parent policy restricts
effective access without replacing container-local programs. BPF program names
are hashes of local device lists, not effective hierarchical policy.

Test effective access inside containers, assert the parent's restored policy,
and verify container attachment shape. Do not require each descendant program
name to match the parent's name after a group restriction. This observation is
limited to the immediate running-cgroup behavior; it is not evidence about
container restarts or later device reconfiguration.

Verification: after fresh general and risk reviews accepted the corrected
assertions, the complete v2 VM test passed on `5e31378ae` in 439.27 seconds,
including the final parent, attachment, and health checks.
