---
lifecycle: complete
---

# Current state

## Initiative

- Slug: `2026-09-04-cgroup-v1-soft-delete-devices`.
- Requested outcome: root-cause diagnosis only; no fix was authorized or made.
- A separately owned initiative named `2026-09-04-cgv1-devices-bug` existed
  without a matching process environment and was not touched.

## Worktrees and branches

- `vpsadmin`
  - Branch: `2026-09-04-cgroup-v1-soft-delete-devices`
  - Worktree: `worktrees/2026-09-04-cgroup-v1-soft-delete-devices/vpsadmin`
  - Head: `3a64784708faef5e9f4f093255954b14e396904c`
- `vpsadminos`
  - Branch: `2026-09-04-cgroup-v1-soft-delete-devices`
  - Worktree: `worktrees/2026-09-04-cgroup-v1-soft-delete-devices/vpsadminos`
  - Head: `ec7dc42da33cd963fe63d8dde281b0e88fe790c2`
- `vpsfree-cz-configuration` was added for read-only inspection of production
  input pins. It is not an affected component.
  - Branch: `2026-09-04-cgroup-v1-soft-delete-devices`
  - Worktree:
    `worktrees/2026-09-04-cgroup-v1-soft-delete-devices/vpsfree-cz-configuration`
  - Head: `248e2fc614bb3bc29c0a9c9f910330ade0b3cb80`

All branches remained at their upstream starting commits. There are no project
commits or project source changes.

## Root cause

`OsCtld::Devices::V1::ContainerConfigurator` includes the per-user
`<group>/<user>` devices cgroup in every container's `abs_all_cgroup_paths`.
Its `remove_device` method writes a deny rule to that path as well as to the
container-specific paths. The per-user path is shared by all containers using
the same osctl user. Under cgroup v1, denying a device at that ancestor removes
it from every descendant and a child cannot override the denied ancestor.

osctld changes only the initiating container's configured-device model. Its
siblings still have devices such as TUN (`c 10:200`), FUSE (`c 10:229`), or KVM
(`c 10:232`) configured, but those rules disappear from their effective
`devices.list`. `Assets::CgroupDeviceList` compares those two views and reports
the missing configured devices.

The occurrence condition is therefore at least two containers sharing an
osctl user, with a promoted device removed or restricted on one while another
still requires it. The initiating container need not appear in health-check
output because its osctld configuration no longer requests the removed device;
the sibling victims do appear.

## Soft-delete trace

- `TransactionChains::Vps::SoftDelete` invokes `Vps::Stop`, clears network
  routes, and disables `ClusterResourceUse` rows.
- `NodeCtld::Commands::Vps::Stop` invokes only `osctl ct stop` and
  `osctl ct unset autostart` through `NodeCtld::Vps#stop`.
- Route deletion modifies network configuration and does not touch devices.
- Only `NodeCtld::Commands::Vps::Features` maps TUN, FUSE, PPP, and KVM to
  `osctl ct devices add -p` or `osctl ct devices del`.
- The current production configuration pins vpsAdminOS
  `3bf14ec679229ab6c19387593e3a34db2da20220` and vpsAdmin
  `9fc0648accd414246d6422e67106ae7217486020`; the inspected files at those exact
  revisions have the same relevant behavior.

Normal soft deletion is therefore not the operation that removes devices.
The reported timing is real but the direct causal link is incomplete: a
features/device-removal transaction on a container sharing the osctl user must
be identified in transaction logs around the event. Live transaction history
could not be queried with the credentials available in this environment.

## Reproduction and tests

Ran `./test-runner.sh debug cgroups/devices-v1` in the vpsAdminOS worktree. The
test used the cached vpsAdminOS kernel; no unexpected local kernel build ran.

1. Created `testct`, enabled TUN with parent promotion, and verified a clean
   health check.
2. Ran `osctl ct stop testct` once and then a second time to mirror the
   suspended-to-soft-delete double-stop path. The health check remained clean,
   and TUN remained present in the shared user and container cgroups.
3. Created `testct2` under the same osctl user, enabled TUN on both containers,
   and verified a clean health check.
4. Removed TUN only from `testct`. `osctl healthcheck -a` reported:

       container tank testct2
           cgroup_device_list /sys/fs/cgroup/devices/osctl/pool.tank/group.default/user.testct/ct.testct2: device "c 10:200 rwm" not allowed

5. Read `devices.list` from the shared user cgroup and `testct2` cgroup; both
   lacked TUN although `testct2` still had it configured.
6. Re-added TUN with parent promotion to the first container. The existing
   sibling cgroup remained unhealthy. Starting `testct2` reapplied its device
   configuration and restored `No errors detected.`

This reproduces the production error structure and isolates the cgroup v1
ancestor mutation as the cause. Source inspection shows the cgroup v2 path uses
a different BPF-based configurator and does not contain this cgroup v1
ancestor-list operation.

## Other investigation results

- Searched both repositories' GitHub issues and pull requests for matching
  soft-delete/device reports; none were found.
- Direct read-only SSH to the reported node reached the host but authentication
  was not authorized. A vpsAdmin API query also returned HTTP 401, so no live
  state was changed or collected.
- Creating the configuration worktree initially populated Bundler/Overcommit
  cache files before dependencies were available. The helper subsequently
  completed; the transient `.bin`, `.bundle`, and `.gems` directories were
  removed during cleanup.
- An exploratory vpsAdmin test-runner listing process was stopped after it was
  no longer needed.

## Review and compatibility

- Mandatory change review was not applicable because the investigation made
  no project code, schema, API, protocol, configuration, or documentation
  changes.
- No persisted state or deployment compatibility is changed by this
  investigation. A later fix should be confined to the cgroup v1 device-policy
  application path and must account for all sibling requirements before
  restricting a shared ancestor. Reapplying the ancestor alone does not update
  already-restricted descendant cgroups.

## Cleanup

- The debug VM exited normally and no initiative test-runner or QEMU process
  remains.
- All three worktrees are clean and ready for non-force removal.
- Feature branches are retained as required; no remote branch was pushed.
- Durable lesson recorded in
  `notes/vpsadminos/2026-09-04-cgroup-v1-shared-user-device-revocation.md`.
