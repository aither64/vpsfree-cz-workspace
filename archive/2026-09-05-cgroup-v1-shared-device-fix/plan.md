# Prevent cgroup v1 container device changes from affecting siblings

## Goal

Fix vpsAdminOS cgroup v1 device handling so removing or narrowing a promoted
device on one container never revokes that device from sibling containers that
share the same osctl user. Preserve group-level restriction semantics, keep
cgroup v2 runtime behavior unchanged, and pin the tested staging-based fix to
the staging and production vpsAdminOS inputs. The user has now authorized
integration into both default branches and cleanup; deployment remains outside
this initiative's scope.

## Affected repositories

- `vpsadminos`: correct the cgroup v1 container configurator and add focused
  unit and VM regression coverage.
- `vpsfree-cz-configuration`: pin the exact pushed vpsAdminOS feature revision
  to the `staging` and `production` channels using `confctl`.

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
   exact head is pushed and CI passes, pin the configuration repository's
   `staging` and `production` channels to that revision. The user accepts the
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
- Both input pins will be generated on the retained configuration branch.
  Integrate vpsAdminOS into `staging` before configuration into `master`.
  No `dry-activate`, deploy, or equivalent activation will run.

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

## Approved cgroup v2 follow-up (2026-09-07)

- Keep this active initiative and both retained, unmerged feature branches.
  Add a focused vpsAdminOS test commit after the original v1 fix.
- Extend `cgroups/devices-v2` with ordered RSpec examples for two containers
  under one osctl user: local device deletion, local chmod from `rwm` to `r`,
  and recursive deletion from `/default`.
- Use promoted TUN device `char 10:200` and persistent test device nodes in
  both containers. Verify read-only and write-only opens without transferring
  data, including successful baseline opens and explicit permission-denial
  messages. Check BPF attachments and health after every mutation.
- Preserve sibling and parent BPF programs for local operations; recursive
  removal must restore `/default` to its default program and deny effective
  access in both containers. On v2 the parent BPF program enforces that denial
  without replacing the container programs; do not require their names to
  return to the original defaults (confirmed by the first VM run).
- Run quick Nix/Ruby checks and active hooks, commit, complete mandatory review,
  then run both v1 and v2 VM tests and monitor pushed-head GitHub Actions.
- Update the production pin to the exact validated new head with `confctl` on
  the retained configuration branch. Consolidate its unmerged input update
  into one generated commit, preserving the generated message.
- Verify the lockfile and run `nix flake check --no-build
  --no-update-lock-file`. Retain the established full-node-build limitation
  from the missing deployment-only initrd key; do not repeat the known failure.
- No runtime, API, CLI, protocol, schema, state-format, or Nix module contract
  changes are planned. No coordinated node update is required. Mixed-version
  operation and rollback have the original fix's compatibility properties.
- Push both retained branches; do not merge, deploy, activate, or archive.

## Staging pin correction (2026-09-07)

- The original plan and first v2 follow-up selected only `production`. The
  user clarified that `vpsadminosStaging` must also select the tested revision.
- Use `confctl inputs channel set --commit staging vpsadminos
  5e31378ae42f253b4878940e3462f6e40b214fb4` on the retained configuration branch,
  preserving the generated commit and changelog. Keep the existing production
  pin commit and add a focused commit for the newly requested staging input.
- Verify both requested inputs select the same source and that the separate
  `os-staging` channel and all other lock nodes remain unchanged. Run active
  hooks and `nix flake check --no-build --no-update-lock-file` before pushing.
- This selects the already reviewed and locally/CI-tested provider revision;
  no new runtime code or deployment contract is introduced. The staging
  channel's vpsAdmin inputs follow its vpsAdminOS input as already declared.
  No coordinated update, merge, or activation is required or authorized.

## Authorized integration and cleanup (2026-09-07)

- The user's merge-and-cleanup instruction supersedes the earlier pre-merge
  hold and active-retention requirement. Continue using the same initiative and
  retained feature branches until their integration is verified.
- Fetch defaults and rebase vpsAdminOS onto current `origin/staging`. Compare
  the rebased patch series with the reviewed series and run quick checks.
  Repeat affected review lanes only if the integration changes reviewed logic.
- Push the rebased feature branch with an explicit lease and require successful
  CI for its exact head. Do not accept an unexplained rerun or build kernels
  locally to work around unavailable cache outputs.
- Rebase configuration onto current `origin/master`, regenerating its two
  unmerged input commits with `confctl` for the final tested vpsAdminOS SHA.
  Keep upstream input changes and the generated changelogs; evaluate the flake.
- Create fresh temporary worktrees on the actual default branches, fast-forward
  them to the retained features, verify, and push over SSH. Monitor resulting
  default-branch workflows and preserve concurrent upstream changes.
- Remove temporary build artifacts and all initiative worktrees after checks
  finish. Keep local and remote branches, mark the lifecycle complete, run
  `dev-session finalize`, commit the curated archive on shared workspace
  `master`, then run `dev-session stop`.

## Integration result

- Integrated and pushed vpsAdminOS `staging` at `2166e5934` and configuration
  `master` at `e26f0a33`, both by fast-forward from fresh temporary worktrees.
- Both staging and production select the same integrated vpsAdminOS revision.
  Local checks, all 13 unit suites, and both feature/default CI runs passed.
- Temporary integration worktrees and generated artifacts are removed.
  Retained feature worktrees passed final cleanliness checks; normal guarded
  finalization removes them, retains all branch refs, archives the curated
  record, and stops the managed session after the archive commit.
- The helper requires the exact Codex thread to be idle. An independently
  tested finishing service executes this last sequence after the closing reply;
  it verifies prepared-file hashes and preserves unrelated shared workspace
  changes. No deployment is included.
