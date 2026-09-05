# Prevent cgroup v1 container device changes from affecting siblings

## Goal

Fix vpsAdminOS cgroup v1 device handling so removing or narrowing a promoted
device on one container never revokes that device from sibling containers that
share the same osctl user. Preserve group-level restriction semantics, keep
cgroup v2 unchanged, and pin the tested staging-based fix to the production
vpsAdminOS input without merging or deploying it.

## Affected repositories

- `vpsadminos`: correct the cgroup v1 container configurator and add focused
  unit and VM regression coverage.
- `vpsfree-cz-configuration`: pin the exact pushed vpsAdminOS feature revision
  to the `production` channel using `confctl`.

No vpsAdmin change is required; its feature command is only a consumer of the
general osctld device API.

## Approach

1. In the cgroup v1 container configurator, distinguish the shared
   `<group>/<user>` intermediate from container-private descendant cgroups.
2. Keep widening operations safe and functional: additions, reconfiguration,
   and the allow portion of mode changes can update both shared and private
   paths after the parent group provides the requested mode.
3. Apply destructive operations only to the selected container's private
   paths: device removal and the deny portion of mode changes must never write
   `devices.deny` to `<group>/<user>`.
4. Leave group configurator behavior authoritative. Recursive group removal
   continues to update descendants and deny the device at the group cgroup,
   which is the security boundary above every per-user intermediate.
5. Do not add initialization reconciliation or a new osctl repair command.
   Existing mismatches heal on the container's next normal start/restart.
6. Base the vpsAdminOS feature branch on current upstream `staging`. After its
   exact head is pushed and CI passes, pin only the configuration repository's
   `production` channel to that revision. The user explicitly accepts the
   intervening staging changes already ahead of the current production pin.

## Compatibility and deployment

- No API, protocol, database, osctld configuration, or persisted-state format
  changes are required.
- Fixed and old nodes can operate concurrently. Rollback is mechanically safe
  but restores the faulty cgroup v1 behavior.
- cgroup v2 uses the separate BPF configurator and must remain behaviorally and
  structurally unchanged.
- A retained allow entry at `<group>/<user>` cannot exceed the effective
  parent group policy, and each container-private cgroup remains the final
  per-container restriction boundary.
- Existing corrupted running cgroups are deliberately not reconciled on
  osctld restart. Running containers require a controlled restart; stopped
  containers heal when next started.
- The production input pin will be committed and pushed on a feature branch,
  but neither repository will be merged and no `dry-activate`, deploy, or
  equivalent activation will run.

## Testing plan

- Add focused RSpec coverage proving that container removal never denies at
  the shared user path and mixed chmod changes send only allows there.
- Extend `cgroups/devices-v1` with two containers under one osctl user and
  verify independent delete and chmod behavior, clean health checks, and
  correct recursive group removal.
- Run focused specs, Nix parsing, and hook-managed formatting/linting before the
  first project commit.
- Run the mandatory high-risk change review at `xhigh` with general,
  architecture, scope, and risk lanes before VM integration tests.
- Run both `cgroups/devices-v1` and `cgroups/devices-v2` VM tests using the
  default bridge network. Stop and investigate any unexpected kernel build.
- Push vpsAdminOS over SSH and monitor all triggered GitHub Actions through a
  clean result, investigating logs and artifacts for any failure.
- Generate the production pin with
  `confctl inputs channel set --commit production vpsadminos <revision>`, keep
  its generated commit unchanged, and build all production-channel vpsAdminOS
  nodes without activating them.
