# Development-cluster packaging investigation

Both installed providers fail before VM startup. The immediate repairs belong
in `vpsfree-dev-workspace` (`vpsfreecz/dev-workspace`), which owns both cluster
helpers. Reverting password-reset application changes or rebuilding a kernel
would not resolve these failures.

## Scope and exact versions

- Installed generic runtime: `hv8p0qwk6qi04d6ac92y0x2p0x98faq7-dev-workspace-0.2.0`.
- Installed provider package: `824x3n05bh7zichkak2mp41j883cixxc-vpsfree-dev-workspace-tools-0.1.0`.
- Organization source: `0a9c974994746e2a6d9d74e83cde8abbf0e65f0a`, also the
  fetched upstream default on September 11. Its immutable source is
  `/nix/store/l9dm5nv24b7305w6cvxjk4kin3ssvid5-source`.
- vpsAdmin input: password-reset worktree at
  `2c1675980217c0a4c331543343054ee6bcd9b197`.
- vpsAdminOS input: retained staging revision
  `2166e5934fe1167ed4c5af67c744bdf3b12df0d5`, matching the original failure.
- The target session's logs, tracking and newly initialized cluster directory
  were inspected read-only. No target cluster command or reset was run.

## Confirmed causes

| Defect | vpsAdmin | vpsAdminOS |
| --- | --- | --- |
| Nix still reads removed `default-config.json` | Config evaluation fails | Config evaluation fails |
| Shared runner source uses `../lib` outside nested flake root | Runner evaluation fails | Same invalid reference, initially masked by overlay failure |
| Runner import does not call the current OS overlay function | Already correct | Runner evaluation fails: overlays must be a list |
| Runner bundle lacks `vpsadminosRubyGemConfig` | Already correct | After overlay repair: `attribute 'sha256' missing` |
| Lock callback disables shell failure propagation | Can continue after failed configuration build | Same shared implementation |

### Removed default files

Both `dev-clusters/<provider>/nix/test.nix` expressions unconditionally load
`../default-config.json` (vpsAdmin line 45, vpsAdminOS line 25). Even when the
per-cluster `CONFIG_FILE` is supplied, it is merged into those missing defaults.

The package correctly accepts host-owned defaults via `siteConfig.clusterDefaults`
and sets `VPSADMIN_DEVCLUSTER_DEFAULT_CONFIG` and
`VPSADMINOS_DEVCLUSTER_DEFAULT_CONFIG` in its shell wrappers. It neither installs
the expected default files nor passes that setting into the Nix expressions.
The wrapper successfully creates per-cluster `config.json`, then Nix fails.

Commit `1b037b0` on September 10 removed the in-tree defaults as part of moving
operational configuration to the consuming workspace. That ownership separation
is sound; the Nix configuration path was left incomplete.

### Shared library outside the nested flake

Both helpers invoke `nix ... path:$CLUSTER_DIR#...`, where `CLUSTER_DIR` is only
`dev-clusters/vpsadmin` or `dev-clusters/vpsadminos`. Nix snapshots that directory.
The sibling `dev-clusters/lib` is present in the outer package but is outside
the imported flake root. `builtins.path { path = ../lib; ...; }` consequently
resolves outside the copied source and fails with:

```text
error: 'lib' is too short to be a valid store path
```

Commit `62ea5a1` on September 10 replaced the previous workspace-based library
reference with `../lib`. Making a flake impure does not restore a missing sibling
inside its source snapshot; the original command already used `--impure`.

### vpsAdminOS runner has an older dependency interface

`dev-clusters/vpsadminos/flake.nix:41` imports `os/overlays` without calling it.
At the actual OS revision, that import is a function requiring `netlinkrb` and
`ruby-lxc`, not the list expected by nixpkgs. Match the working vpsAdmin expression:

```nix
overlays = import (vpsadminos.outPath + "/os/overlays") {
  inherit (vpsadminos.inputs) netlinkrb ruby-lxc;
};
```

Its `runnerDeps` also needs `gemConfig = pkgs.vpsadminosRubyGemConfig;`.
The current test-runner gemset intentionally omits download hashes for gems
built from the OS source. The source gem configuration supplies those builds;
falling back to the ordinary gem configuration produces the missing-hash error.
vpsAdmin already passes this configuration. These OS-only issues predate the
September packaging changes; the source-gem interface changed in OS commit
`b0c2ea255` on June 11.

### Failed builds can fall through to launcher startup

`dev-clusters/lib/runtime.sh:821` calls the locked callback as
`if "$callback" "$@"; then`. Bash consequently ignores `set -e` inside the
callback and its nested functions. The start functions do not explicitly return
on a failed `build_config_with_credentials` call, so they proceed to topology
metadata and `nix run` after `nix build` has failed.

The target's original logs show exactly this sequence: missing defaults, then
runner launch and the shared-library error. An isolated probe using the actual
lock function and a callback containing `false` followed by a marker printed
the marker and returned zero. This is independent of Nix.

Repair failure propagation at every build/start boundary, preserving lock and
environment semantics. At minimum, configuration/credential build failure must
prevent runner launch and use of an old `result-config` link. Test failure with
both absent and retained previous build results. Do not replace the lock logic
with a casual subshell: callbacks currently also export configuration for the
subsequent runner command.

## Recommended repair

Make each packaged provider flake contain the assets it needs:

1. During `nix/organization-tools.nix` installation, copy the corresponding
   validated `siteConfig.clusterDefaults` into each provider's
   `default-config.json`. Keep the operational JSON in the consuming workspace.
   Preserve the current merge of defaults and retained per-cluster overrides.
2. Copy the canonical shared runner source into each packaged provider, for
   example under `shared/`, and reference `./shared`. Keep one maintained source
   copy in the repository; generate the package copies. Copy actual contents
   so no sibling symlink recreates the flake-boundary problem.
3. Bring the vpsAdminOS overlay and gem configuration up to the interface already
   used by vpsAdmin.
4. Make configuration-build failure terminate startup and add regression coverage
   for both providers through the real lock wrapper.

An alternative is to pass the immutable defaults and shared runner source as
explicit Nix arguments/inputs, or move both outputs beneath one common flake
root. That makes dependencies explicit and avoids generated copies, but changes
more interfaces and input-override plumbing. The small packaging repair above
was exercised in temporary copies and is the shortest demonstrated path.

A global rollback is not the preferred workaround. The vpsAdminOS dependency
issues and callback behavior are older, and package switches must still satisfy
the current recorded socket/state contract. Restoring old scripts or editing
another session's state bypasses the supported deployment path.

## Verification performed

Using `nix eval --offline --impure --no-write-lock-file` with exact existing
source overrides and `.drvPath` outputs:

- Original vpsAdmin configuration: failed on missing defaults.
- Original vpsAdmin runner: failed on the external shared library.
- Original vpsAdminOS configuration: failed on missing defaults.
- Original vpsAdminOS runner: failed on the overlay type.
- vpsAdminOS with dependency fixes but its original shared-library reference:
  independently reproduced the same invalid-store-path error as vpsAdmin.
- Temporary copies with packaged defaults/shared source: both configuration
  derivations evaluate successfully; vpsAdmin runner evaluates successfully.
- vpsAdminOS with overlay repair: the independent missing gem configuration is
  exposed. Adding that configuration makes its runner evaluate successfully.
- Both repaired runner packages build successfully and execute their usage path
  with expected exit status 2, loading `devcluster_runner`, `osvm` and Ruby
  dependencies. This was a runner loading check, not VM startup.
- Existing `test/devcluster_status_test.rb`, run from an isolated source copy
  with pinned Nix Ruby and installed runtime contract: **46 tests, 516 assertions,
  zero failures/errors/skips**, 49.2 seconds, seed 26910.
- Shared lock failure-propagation probe: incorrectly returned success after the
  injected failure, confirming the separate startup-control defect.

No VM or kernel build was started. Config evaluation performed one small
`vpsadmin-source-unknown` source-preparation derivation; it did not build the
cluster. Runner builds required only wrappers, bundle links and executable stubs.

The current package install check validates JSON and `--help`; the Ruby tests
exercise state, locking, status and refusal cases. Neither forces the nested
Nix configuration or runner outputs, explaining why these defects pass CI.

## Required acceptance for an implemented fix

Add packaged-source checks for both `cluster-config` and `runner`, runner loading,
and failed-build propagation. Exercise host defaults and per-cluster overrides.
After implementation, commits, quick checks and mandatory review, run both
providers through the installed stable dispatcher on isolated bridge clusters:
start, ready/status, SSH health check, service/node update, stop, and restart with
retained VM state. Check API/database/nodectld/osctld for vpsAdmin and node
boot/osctld/container operation for vpsAdminOS. Allocate nonconflicting addresses
or run serially; inspect binary-cache coverage before building VM closures.

Only after those checks should the password-reset deployment be retried. Its
current failed-start state must be preserved and handled through the stable
helper. These package repairs need no database/schema/API change, no VM disk
migration, and no coordinated production node update. Preserve the current
package-generation, ownership and socket checks during deployment and rollback.

Full VM startup, update and retained-state restart remain unverified in this
investigation. No project fix or workspace package deployment was performed.
