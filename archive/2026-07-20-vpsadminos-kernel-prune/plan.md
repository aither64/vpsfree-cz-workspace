# 2026-07-20-vpsadminos-kernel-prune

## Goal

Prune the vpsAdminOS kernel registry to Linux 6.12.95 and 6.12.48, and make
the eBPF livepatch registry's `untilKernel` bound exclusive while preserving
the effective lifetime of existing mitigations.

## Affected repositories

- `vpsadminos`: kernel definitions, proactive-swap QEMU default, eBPF
  livepatch registry semantics, module documentation, and tests.

## Approach

1. Remove kernel definitions for 6.12.93, 6.12.91, 6.12.89, 6.12.87,
   6.12.81, 6.12.79, 6.12.70, 6.12.59, and 6.12.58. Keep stable and unstable
   defaults on 6.12.95 and retain 6.12.48 for running systems.
2. Move the proactive-swap QEMU default from removed 6.12.81 to 6.12.95.
3. Change eBPF `untilKernel` matching from `<=` to `<`, update user-facing
   descriptions and tests, and change `ptrace_mm_guard.untilKernel` from
   6.12.88 to 6.12.89 so its effective coverage remains unchanged.
4. Keep all examples. Keep the cumulative kernel livepatch,
   `ptrace_mm_guard`, and `cifs_spnego_guard`, because each real mitigation
   remains applicable to retained kernel 6.12.48.
5. Keep kernel pruning and eBPF bound semantics in separate commits.

## Compatibility and deployment

Running kernels and already-built closures are unchanged. After pruning, new
configuration evaluation for a removed runtime kernel will fail. Before a
downstream configuration advances to this vpsAdminOS revision, generated fleet
kernel inventory must contain only 6.12.48 and 6.12.95, or affected machines
must reboot to 6.12.95 first.

The `untilKernel` field name and monitoring/evidence shape remain stable, but
the upper bound becomes exclusive. Old nodes report 6.12.88 and new nodes
report 6.12.89 for `ptrace_mm_guard`; both describe the same effective coverage
through 6.12.88. There are no schema, persistent-state, or protocol changes,
and rollback to the previous vpsAdminOS revision restores the old registry.

## Testing plan

- Evaluate `flake.lib.kernelVersions`, defaults, both retained kernel
  toplevels, and the proactive-swap QEMU configuration.
- Evaluate kernel livepatch and eBPF selections for 6.12.48 and 6.12.95.
- Run the eBPF livepatch test suite with exclusive-boundary coverage.
- Run nixfmt and all Overcommit hooks.
- After the intended commits and quick checks, run the mandatory standalone
  change review before longer builds or integration tests.
- Push the feature branch, monitor GitHub Actions, and investigate failures.
