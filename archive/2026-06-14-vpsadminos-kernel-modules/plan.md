# 2026-06-14-vpsadminos-kernel-modules

## Goal

Make the vpsAdminOS `kernel-modules` runit service safer by default. The
service should keep loading configured kernel modules unless an operator opts
out, but it should no longer unload modules merely because they were removed
from `boot.kernelModules` unless an operator explicitly opts in.

## Affected repositories

- `vpsadminos`
  - Worktree:
    `worktrees/2026-06-14-vpsadminos-kernel-modules/vpsadminos`
  - Branch: `2026-06-14-vpsadminos-kernel-modules`
  - Base: `origin/staging` at `71b06c976`

## Approach

1. Commit 1: move the `kernel-modules` runit service into its own module file.
   - Add `os/modules/config/kernel-modules.nix`.
   - Register it in `os/modules/os-modules.nix`, near
     `./config/kernel.nix`.
   - Move the current service-only pieces out of
     `os/modules/config/kernel.nix`:
     - `kernelModuleList`
     - `kernelModuleServiceShell`
     - `environment.etc."kernel-modules".source`
     - `runit.services.kernel-modules`
   - Preserve the current behavior exactly in this commit: load configured
     modules, unload removed modules, update `/run/kernel-modules/modules`,
     and keep the same service check, logging, runlevels, and reload behavior.
   - Commit this as a focused mechanical extraction before adding behavior
     options.

2. Commit 2: reload `kernel-modules` through the active control script.
   - Keep the service `onChange` action as `reload`.
   - Add a runit `control.hangup` script that reloads modules using the
     activated generation's generated service shell. This handles normal
     `sv reload kernel-modules` without depending on the old long-running
     shell process.
   - Keep the HUP handler as a fallback for rollback or manual signalling: it
     stops the sleep child and re-execs
     `/etc/runit/services/kernel-modules/run`.
   - Reload `kernel-modules` before other reload-only services so services such
     as firewall see the module-list state after the activated generation has
     processed it.
   - Add focused switch-to-configuration coverage that:
     - proves `kernel-modules` is reloaded, not stopped/started, when its run
       script changes;
     - proves combined firewall and kernel module changes keep
       `kernel-modules` available while firewall reloads.

3. Commit 3: add two vpsAdminOS options in
   `os/modules/config/kernel-modules.nix`:
   - `boot.kernel.loadNewModules`
     - Type: boolean
     - Default: `true`
     - Purpose: control whether `kernel-modules` runs `modprobe` for modules
       listed in `boot.kernelModules` when the service starts or reloads.
   - `boot.kernel.unloadRemovedModules`
     - Type: boolean
     - Default: `false`
     - Purpose: control whether `kernel-modules` runs `modprobe -r` for modules
       that were present in the previously processed module list and are no
       longer present in the current one.

4. Thread those options into `kernelModuleServiceShell`.
   - Keep the current load behavior when `loadNewModules = true`.
   - Log a clear skip message when loading is disabled.
   - Only call `unload_removed_modules` when
       `unloadRemovedModules = true`.
   - Log a clear skip message when unloading is disabled.
   - Continue updating `/run/kernel-modules/modules` after a reload so the
     service check reflects the configuration that has been processed.

5. Update `tests/suite/system/switch-to-configuration.nix`.
   - Change the existing module transition test to expect the new default:
     added modules are loaded, removed modules remain loaded, and no unload log
     is emitted.
   - Add or extend a transition that sets
     `boot.kernel.unloadRemovedModules = true` and verifies that a removed
     module is unloaded only in the opt-in case.
   - Add coverage for `loadNewModules = false`, verifying that a module newly
     added to `boot.kernelModules` is not loaded and the service logs that
     loading is disabled.

6. Keep the change focused to vpsAdminOS. No generated client, API, schema, or
   configuration repository changes are expected.

## Compatibility and deployment

- Backward compatibility:
  - Existing configurations that do not set the new options continue to load
    configured modules, but no longer unload modules removed from
    `boot.kernelModules`. This is an intentional safer default.
  - Modules that remain loaded after removal from configuration will stay loaded
    until reboot, manual `modprobe -r`, or a later service reload where
    unloading is explicitly enabled for a subsequent removal.
- Forward compatibility:
  - Configurations using the new options require a vpsAdminOS revision that
    defines them. Pinning these options while evaluating an older vpsAdminOS
    module set will fail at Nix evaluation time.
- Commit ordering:
  - The first commit is a no-behavior-change module extraction and should be
    safe to deploy independently.
  - The second commit changes only the reload mechanism so generated service
    changes run through the active generation's control script immediately
    after activation while `kernel-modules` remains reload-based.
  - The third commit changes the default unload behavior and introduces the new
    options.
- Persisted state:
  - The service state lives under `/run/kernel-modules`, so it is runtime-only
    and does not introduce rollback-persistent on-disk formats.
- Deployment ordering:
  - This is a single-repository vpsAdminOS module change. It does not require
    coordinated updates of all running machines or nodes.
  - Operators can deploy incrementally. During mixed-version operation, only
    nodes running the new revision get the safer unload default and the new
    options.
  - Deploying this change keeps `kernel-modules` reload-based during
    `switch-to-configuration`, so reload-only services that wait for it do not
    observe a planned stop/start window.
- Rollback:
  - Rolling back to an older vpsAdminOS revision removes the new control script
    from the target service directory. In that case runsv sends HUP to the
    still-running new shell, whose fallback handler re-execs
    `/etc/runit/services/kernel-modules/run` after activation. The rollback
    generation's run script and unload semantics therefore take effect without
    requiring a reboot.

## Testing plan

1. Run formatting/hooks through Overcommit before committing:
   `nix develop --command overcommit --run`.
2. Run the focused VM test:
   `./test-runner.sh test system/switch-to-configuration`.
3. If the focused test or implementation touches shared boot/module behavior
   more broadly than expected, also run:
   `./test-runner.sh test kernel/module-autoload system/boot/stage-2`.
4. After intended changes are committed and quick verification passes, run the
   mandatory change review with a fresh standalone agent before longer
   integration testing.
