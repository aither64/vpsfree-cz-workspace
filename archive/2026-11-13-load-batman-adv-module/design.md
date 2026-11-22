# Load batman_adv by default

Package D owner: `architect0`. Design is sufficient for lead release of package I.
Inspected vpsAdminOS base: `eedc1254d309cac861cb0f7af080ee8de8296506`.
Feature worktree: `worktrees/2026-11-13-load-batman-adv-module/vpsadminos`.
Integration target: `vpsadminos/staging`; integration requires separate approval.

## Scope and settled interface

Add `"batman_adv"` alphabetically to `boot.kernelModules` in
`os/modules/config/kernel.nix`. Use the existing explicit `modprobe` path to
resolve compiled dependencies. Keep kernel autoload disabled by default. Do not
change kernel configuration, kernel pins, initrd loading, mesh configuration,
network interfaces, tools or production configuration.

Evidence at the inspected base:

- `os/modules/config/kernel.nix:187` defines the common default module list;
  `batman_adv` is absent and `crc16` is already present. The same file defaults
  `boot.kernel.moduleAutoload.enable` to false.
- `os/modules/config/runit.nix:20` explicitly runs `modprobe` for each configured
  module at boot. `os/modules/config/kernel-modules.nix` writes
  `/etc/kernel-modules` and runs explicit kmod `modprobe` on service start/reload.
  Thus adding the module uses both existing boot and configuration-switch paths.
- `os/modules/config/kernel-compatibility.nix` already loads `libcrc32c` and
  `crc32c_generic` before Linux 6.18, with version-appropriate replacements for
  newer kernels. Do not unconditionally add those old names to the common list.
- Stable kernel 6.12.117 uses Linux source
  `764acbb0ca8c4b60ee5b98f89406b152e992b1d6`. Its `net/batman-adv/Kconfig`
  selects `LIBCRC32C`; the default bridge-loop-avoidance feature selects `CRC16`.
  Its Makefile builds `batman-adv.o` from `CONFIG_BATMAN_ADV`. These are source
  facts, not proof of the final compiled configuration or all module dependencies.
- A no-build Nix evaluation of the default QEMU configuration passed with
  `--option allow-import-from-derivation false`: kernel version `6.12.117`,
  configuration `/nix/store/lr07axmngs2fgb2h610m6pm9myqshz1j-linux-config-6.12.117`,
  kernel output `/nix/store/8mixm0g0z8iabkgm0np6zyjmrhdndxyf-linux-6.12.117`,
  nixpkgs `/nix/store/7sa2x9c9566lfxkaxs36n3z4yayl5cy4-source`.
  The evaluated list confirms the absence of `batman_adv` and presence of the
  existing CRC dependencies. Evaluation alone does not prove these outputs exist.

## Package I

Owner: `implementer0`, after lead acceptance/release. Own the single source file
above, its quick checks, normal hooked commit, and compact completion evidence.
Routine technical clarification goes to `architect0`; scope or consequential
design changes go through the lead. No competing application edits are planned.
Dependencies: initial tracking/worktree/hooks owned by lead (reported ready),
this brief, and lead release. Remaining compiled evidence is verification work,
not a reason to defer this bounded source edit.

Acceptance: default configurations request `batman_adv`; explicit modprobe
resolves its actual compiled dependency chain; existing autoload policy and
version compatibility remain intact. Add only a proven missing dependency or
softdep if compiled/source evidence establishes that explicit modprobe cannot
satisfy a runtime request with autoload disabled. Escalate that finding before
expanding the settled one-line implementation.

Quick checks (one bounded batch, expected under a minute per command):

1. Run required Nix formatting/hooks and `git diff --check`.
2. Evaluate default `boot.kernelModules` through `flake.lib.vpsadminosSystem`
   with `os/configs/qemu.nix`; assert `batman_adv` is present and autoload remains
   disabled. Use `allow-import-from-derivation = false` to prohibit evaluation
   builds. Comparing before/after evaluated lists should show only this addition.
3. Inspect available cached kernel config/module metadata: `CONFIG_BATMAN_ADV`,
   the module's `modinfo` dependencies and a dry-run `modprobe --show-depends`
   against that kernel's module directory. Confirm the transitive modules are
   present and identify any dependency that performs runtime autoload. Never
   load modules into the development host for this check.

If the compiled outputs are unavailable, report the precise evidence gap and
cache/build requirement rather than starting a kernel build. An exhaustive
kernel matrix, full VM suite, new test harness or mesh functional test is not
required for this loading-list change. No new implementation-mirroring test is
needed. If runtime proof remains necessary after metadata inspection and final
review, the lead may select one focused disposable VM boot: verify
`/sys/module/batman_adv`, dependencies and absence of module-load errors under
the default disabled-autoload policy. Long/uncertain verification uses the
required watcher; stop an unexpected local kernel build. This is proposed
verification, not authorization for a production deployment.

Report exact base/head, changed files, commands/results, compiled evidence or
remaining gap, and whole-branch history with no migrations. Final independent
review follows the committed deliverable and quick checks before any long test.

## Compatibility, rollout and recovery

No persisted format, schema, API/client/CLI, inter-service protocol or Nix option
changes. Mixed old/new nodes remain compatible; no coordinated fleet update is
needed. Existing host update procedures can load the module during a switch
when the running kernel supplies it and `boot.kernel.loadNewModules` is true
(the default). A boot into the updated system also loads it. Actual switch
success must be checked in module state/logs because the loader logs individual
failures and continues. This initiative does not deploy or configure a mesh.

Rollback restores the old loading list without changing stored data. Because
`boot.kernel.unloadRemovedModules` defaults to false, rollback need not unload
an already loaded module. A reboot into the prior generation restores its boot
policy; explicit unload is an operator action only after checking active use.
Do not force-unload modules or disrupt interfaces as part of this change.

The source list is sufficient lasting documentation for this small default;
this brief retains investigation, acceptance and rollback rationale for the
lead/reviewer. No product manual or separate operational guide is needed.
