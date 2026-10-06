# 2026-08-23-vpsadmin-ci-failure

## Goal

Contain the recurring Linux 6.18 module-loader failure in vpsAdmin integration
tests by using Linux 6.12 for generated NixOS guests, remove the insufficient
udev-worker serialization parameters, and roll the change through vpsAdmin's
vpsAdminOS channel pin.

## Affected repositories

- `vpsadminos`: select `linuxPackages_6_12` in the generated NixOS guest base
  configuration and remove the test-only udev serialization parameters.
- `vpsadmin`: update the `vpsadminos` flake input after the vpsAdminOS change is
  merged to `staging`.
- Workspace coordination repository: update the durable kernel-failure note and
  record implementation, review, verification, merge, and cleanup state.

## Approach

1. Pin generated NixOS test VMs to `pkgs.linuxPackages_6_12` with a comment
   documenting the Linux 6.18 bug and the precise removal conditions.
2. Remove `rd.udev.children_max=1` and `udev.children_max=1`, which did not
   prevent the recurrence, while retaining the serial console parameter and
   kernel-failure detector.
3. Run formatting, evaluation, hook, and focused driver checks, then commit the
   vpsAdminOS and workspace changes.
4. Run the mandatory fresh-context change review and address significant
   findings before VM integration testing.
5. Run the focused vpsAdminOS VM test, push the feature branch, monitor its
   GitHub Actions, and fast-forward the verified commit into `staging`.
6. Create the vpsAdmin feature worktree from current `master`, update the
   `vpsadminos` input using `tools/update_vpsadminos_flake.sh`, and run focused
   integration tests against the exact new pin.
7. Push and monitor the vpsAdmin feature branch, fast-forward it into `master`,
   monitor target-branch CI, finalize workspace records, and remove worktrees.

## Compatibility and deployment

- The vpsAdminOS change applies only to generated NixOS test VMs. It does not
  change the kernel of vpsAdminOS machines or deployed VPSes.
- There are no schema, API, protocol, persisted-state, or on-disk format
  changes. Old and new vpsAdmin revisions remain compatible with either
  vpsAdminOS test input during rollout and rollback.
- Updating vpsAdmin's flake input changes test infrastructure only. Deployment
  ordering is vpsAdminOS `staging` first, then vpsAdmin's lock file, so the
  downstream pin always names a reachable merged commit.
- The containment temporarily gives up coverage of the NixOS default Linux
  6.18 kernel. Remove it only after upstream commit
  `1871d548fc4feb007644efb6d669c93a4e191254` is in `linux-6.18.y`, the pinned
  Nixpkgs packages that fixed release, and parallel boot/module-load stress no
  longer reproduces either the `__execmem_cache_free` fault or the earlier
  `__text_poke` static-call failure.
- Rollback is a flake-input or configuration revert and has no persisted-state
  implications. No coordinated update of running vpsAdminOS nodes is needed.

## Testing plan

- Format the changed Nix expression and run the vpsAdminOS hook suite.
- Evaluate/build `.#tests.x86_64-linux."driver/nixos"` and inspect the
  generated machine JSON: kernel is Linux 6.12, the serial console remains,
  and neither udev-worker parameter remains.
- Run `./test-runner.sh test -f --jobs 1 driver/nixos` in vpsAdminOS.
- Run vpsAdmin's `services-up` and
  `vps/deploy-public-key-and-user-data` tests against the updated lock file.
- Require green feature-branch and target-branch GitHub Actions for both
  repositories, investigating any failure before accepting a rerun.
- Stop and investigate if any validation unexpectedly starts compiling a Linux
  kernel instead of substituting it from the configured binary caches.
