# CI impermanence failure diagnosis

Read-only investigation of exact source
`7e79afd4690ff5abac2554fd2a02ba8e8c97c0b1`. No product edits, Nix evaluations,
CI downloads or runtime reruns were performed. The lead retains the active local
runtime operation and all implementation/scope decisions.

The three CI failures share the same trigger: the adversarial account's UID
changes after restart. Both switch operations completed, rebuild-stage identity
and payload checks passed, restart completed, and post-restart network, DNS,
flake presence and machine-id checks passed before the UID assertion failed.
The GID and payload assertions after that failure did not execute, so their
post-restart preservation is not established by these logs.

| Image | Failed fixture | machine-shell first failure |
| --- | --- | --- |
| nixos-26.05-impermanence | test-f02218b3 | line 3187 |
| nixos-unstable-impermanence | test-350415e3 | line 2016 |
| nixos-25.11-impermanence | test-82678da5 | line 3177 |

Logs are in `ci-image-failure-artifacts/os-test-image-scripts__test__<image>-<id>/`.
The failed message is `fixture UID changed after restart`. Logs do not include
pre/post numeric IDs or map contents, and osctl-image cleaned up each failed
container. The ordinary variants passed.

The expectation is valid: the pinned NixOS `update-users-groups.pl` reads
`/var/lib/nixos/uid-map` and `gid-map` before allocation. For an existing recorded
system UID in range, allocUid revives it independently of the order of newly
declared users. Adding the earlier-sorting account after recording the first
account deliberately exposes missing persisted allocation state. Removing that
adversarial step or assigning explicit IDs would hide the regression.

Classification: evidence indicates a pre-existing compatibility boot-ordering
defect exposed by the new test, rather than a selector regression or invalid
test expectation. The unchanged stable raw latest and versioned 26.05 files are
identical blob `ca56009b6e9bc86646b37218884dd5e3f9ffcf40`. The unstable raw module
is unchanged blob `66383b30a719b935ac75e2614a091a72b05ee593`. Both blobs match
initial base `1150e37b`. The stable selector reaches the identical raw behavior,
while the unstable template/module does not use that selector at all.

Concrete source mechanism: raw modules put critical persistence binds into
`boot.specialFileSystems`. NixOS builds earlyMountScript from that set, but its
`stage-2-init.sh` only sources that script inside `if [ ! -e /proc/1 ]` (lines
37–54). It later runs the ordinary activation script at line 137, before
starting systemd. The shipped LXC common configuration uses
`lxc.mount.auto = cgroup:mixed proc:mixed sys:mixed`, so `/proc/1` is already
present in these guests. The early mount block is skipped. Having an evaluated
`boot.specialFileSystems."/var/lib/nixos".device` is therefore insufficient
proof that it was mounted before users activation. The CI boot trace proceeds
directly to activation on restart, with no allocator revival messages.

The next diagnostic should retain the failed fixture (`osctl-image test
--keep-failed ... <image> nixos_rebuild`, which is supported by the current CLI)
and print before/after numeric UID/GID values, persistent and visible uid-map /
gid-map contents, findmnt for `/var/lib/nixos` and `/persistent`, and the relevant
activation/early mount scripts. Capture all assertions independently so the UID
failure does not conceal post-restart GID/payload results. This remains a proposal;
no live guest inspection or diagnostic run was launched here.

A minimal product correction, subject to lead/architect scope approval, must
make the critical persistence bind available before user activation in container
boot even when proc is already mounted. Derive the required binds from the
existing compatibility mount selection, preserve self-contained raw files,
creation/order/ownership and idempotent switch behavior, and avoid blindly
running the complete earlyMountScript during a live switch. A concrete patch
requires the architect to settle those invariants and target the affected raw
stable/versioned/unstable modules; no daemon or host-kernel change is indicated.

Meaningful verification: retain the adversarial dynamic IDs, payload ownership
and machine-id assertions; reproduce the failure using baseline raw behavior;
then show unchanged recorded UID/GID and payload ownership across switch and
restart after the proposed fix. Evaluate the early-mount/activation ordering
with stable and unstable inputs and rerun their two impermanence image cases
on the final reviewed head. The nominal 25.11 image uses the shared stable
builder and is not independent historical nixpkgs runtime evidence.
