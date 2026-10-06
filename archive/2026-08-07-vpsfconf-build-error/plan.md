# 2026-08-07-vpsfconf-build-error

## Goal

Fix the vpsAdminOS NixOS container-image repository module so it applies the
source-aware `osctl` overlay correctly, add regression coverage, update all
three vpsAdminOS channels in `vpsfree-cz-configuration`, and integrate both
repositories without deploying the build host.

## Affected repositories

- `vpsadminos`: fix the path-imported NixOS module and add a focused evaluation
  regression check to CI.
- `vpsfree-cz-configuration`: pin `os-staging`, `staging`, and `production`
  vpsAdminOS roles to the exact fixed revision using `confctl`.

## Approach

1. Change the vpsAdminOS NixOS helper module to consume the canonical,
   already-applied `osctl` and `ruby` overlays exported by its source flake.
2. Add a focused impure Nix evaluation that imports the actual helper module
   and forces `pkgs.osvm`, then execute it early in vpsAdminOS CI.
3. Run hooks and quick checks, commit and publish the vpsAdminOS feature
   revision, and generate one exact three-channel `confctl` pin commit.
4. Run the mandatory standalone change review before long CI/integration work.
5. Validate the feature branches, fast-forward vpsAdminOS `staging` first and
   configuration `master` second, monitor CI, and clean up without deployment.

## Compatibility and deployment

There are no persisted-state, database, API, protocol, or message-format
changes. The affected module is used while evaluating the NixOS build machine;
vpsAdminOS nodes do not import it, so mixed old/new nodes remain compatible and
no coordinated all-node update is required. Updating all three channel pins is
an intentional alignment choice; it does not deploy any system.

The refreshed vpsAdminOS base also includes `d1d73edcd`, which publishes the
6.12.95 cumulative livepatch v3. Its update path supports mixed v2/v3 nodes and
atomic v2-to-v3 replacement, so it does not require a coordinated fleet update.
After v3 has been activated on a running node, however, rolling its generation
back to v2 requires first unloading v3 or rebooting into the rolled-back
generation; v2 cannot load while v3 remains active. Rolling back only the
configuration pin also restores the evaluation bug, but it cannot make new
persistent state unreadable. The user will perform any later deployment and
must account for this livepatch rollback ordering on affected running nodes.

## Testing plan

- Run the focused vpsAdminOS module evaluation and repository Overcommit hooks.
- Verify all three configuration channel roles resolve to the fixed revision
  and run configuration Overcommit hooks.
- Evaluate/build a representative `os-staging` NixOS consumer.
- Run `confctl build -y -t build --show-trace`; in this development environment
  the documented missing SystemRescue ISO may remain the terminal error, but
  infinite recursion must not recur.
- After mandatory review, run and monitor vpsAdminOS GitHub Actions; inspect any
  failed attempt before rerunning it.
