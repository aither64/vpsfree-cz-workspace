# Runtime sysctl application: bounded source trace

**A declaration alone does not apply this value during a live switch.** It
generates a sysctl file; the existing explicit vpsAdminOS application command
runs during boot stage 1. No running host was accessed or changed.

Inspected OS worktree: `worktrees/2026-10-20-kernel-check/vpsadminos`, committed
head `b81c43ff6865a033268072f55cd94ad763d0630b`, one commit over staging base
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`. Directly reading `b81c43ff:flake.lock`
confirms `root.inputs.nixpkgs` → `nixpkgs_2` →
`cd4ea8d57de16f4810bc5f14207bac45fbf19f67`, and root unstable input
`02c087f3fe673c9e317f206a627cb6b910336dbe`. The separate lock node `nixpkgs`
is `e4bae1bd10c9c57b2cf517953ab70060a828ee6f`, referenced by
`impermanence.inputs.nixpkgs`; it is not the OS root Nixpkgs input.
During this read, implementer2's
uncommitted `crashdump.nix` added the hard-panic sysctl and comment; that file's
observed blob was `adcb99b2833a919586d423562b16382146dcc5ba`. The lifecycle files
below were unchanged. This report does not certify later implementation edits.

The retained site configuration is `37a338b25192d9271ee211110800c2dc6a094a57`:
production OS remains `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`, staging OS
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`; both node Nixpkgs channels select
`cd4ea8d57de16f4810bc5f14207bac45fbf19f67`. No pin was changed.

## Exact path

All OS references below are to committed `b81c43ff` unless marked working copy.

1. `os/modules/nixos-modules.nix:56` imports Nixpkgs `config/sysctl.nix`.
   At the root/site pin `cd4ea8d5`, that module's lines 94–104 render
   `environment.etc."sysctl.d/60-nixos.conf".text` and declare a restart trigger
   for **systemd** service `systemd-sysctl`. It has no activation snippet.
   Its additional ASLR file does not supply live application. The separately
   inspected nested `e4bae1bd` module has equivalent behavior at lines 64–73;
   that trace is corroboration, not root-input attribution. Both exact cached
   sources were read; the `cd4ea8d5` source's NAR hash matches the site lock.
2. `os/modules/nixos-compat.nix:84–109` provides inert systemd compatibility
   options. No runit sysctl service or systemd-to-runit translator exists in
   this module graph. `os/modules/system/activation/top-level.nix:13–20` exports
   only `config.runit.services` into the service manifest, so that systemd
   restart trigger is not consumed by the live runit switch logic.
3. Boot `os/modules/system/boot/stage-2-init.sh:65–81` invokes the generated
   activation program, then execs runit. `os/modules/config/runit.nix:19–26`
   loads kernel modules and runs `sysctl -w --system` in **stage 1**. The runit
   stage source is installed by `system/boot/runit/default.nix:615–619`.
4. Live `switch-to-configuration.rb:75–121` runs boot-loader handling for
   `switch`, then the `test` path: stop changed services, execute the new
   `activate`, switch runlevel, reload/restart changed runit services. The
   imported etc activation snippet updates `/etc`; it does not write sysctls.
   This path never calls runit stage 1 or `sysctl`. `boot` alone only prepares
   the bootloader; it is not runtime application either.
5. Restart decisions compare resolved service `run` paths and explicit trigger
   arrays (`switch-to-configuration.rb:186–203,293–318`). Trigger differences
   cause restart even with `onChange = "ignore"`. Current crashdump triggers
   cover kernel, crash initrd and boot-stage-2 paths (`crashdump.nix:424–429`
   before the working insertion); its run body loads kexec and has no sysctl
   command. A possible crashdump restart therefore does not apply the sysctl.
6. Crashdump uses `oneShot = true`. The generated run wrapper appends a `done`
   marker and `sv once`; its default check tests that marker
   (`system/boot/runit/default.nix:283–313`). There is no separate `runonce`
   sysctl facility. Neither starting this service nor observing its marker
   proves that the hard-panic sysctl was written.

## Bounded choices for the design owner

The smallest change is to keep the declaration and explicitly require a later,
separately authorized targeted `sysctl -w kernel.hardlockup_panic=<effective-value>`
plus readback on running hosts. Describe automatic application as boot-only.
Do not silently substitute `sysctl --system`, which would replay other policy.

If automatic application on ordinary live switches is required, an existing
`system.activationScripts` snippet is smaller than a new service/framework:
gate it with crashdump, order after `etc`/`specialfs`, target only the effective
hard-panic setting, honor explicit overrides/null, and keep dry activation
nonmutating. The existing `kernel.modprobe` activation in
`os/modules/config/kernel.nix:435–445` demonstrates a targeted live write.
This is a proposal for architect/lead acceptance, not implemented behavior.
Runtime readback remains necessary: `Configuration#activate` does not propagate
its child status as a checked failure (`switch-to-configuration.rb:117–121`).
Removing a declaration or disabling crashdump would not reset a live value.

Existing switch fixture `tests/suite/system/switch-to-configuration.nix:188`
checks restart-trigger selection; Ruby
`system/activation/switch_to_configuration_spec.rb` checks trigger precedence.
They do not prove sysctl live application. No fixture, evaluator, build or CI
observer was run here; only source and cached input metadata were read.
No source/Git mutation or production access occurred. Implementer2 and
architect0 received the conclusion before any proposed activation edit.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>
