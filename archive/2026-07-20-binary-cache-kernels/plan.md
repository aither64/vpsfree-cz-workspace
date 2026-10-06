# 2026-07-20-binary-cache-kernels

## Goal

Determine why deploying `backuper2.prg` from the current
`vpsfree-cz-configuration` wants to build
`/nix/store/z2f05q0gvrgnnxgym0ikrr3dwnil75lr-linux-6.12.48.drv` instead of
substituting it from `cache.vpsadminos.org`. Check whether recent vpsAdminOS
changes, especially commit `680f26f9800781e4321558001492a0b0d620dd27`, changed
the kernel derivation and whether the daily kernel workflow built and published
the exact required closure.

## Affected repositories

- `vpsfree-cz-configuration`: production channel pin, backuper2 kernel
  selection, and deployment cache configuration.
- `vpsadminos`: kernel definitions and daily kernel-cache workflow.

## Approach

1. Resolve the exact vpsAdminOS revision and kernel configuration used by
   `backuper2.prg`.
2. Inspect the cited commit and derivation inputs to determine whether it can
   alter the kernel output hash.
3. Query `cache.vpsadminos.org` for the exact derivation/output paths.
4. Inspect recent daily kernel workflow runs, their evaluated revisions and
   matrix, build/upload results, and timing relative to the configuration pin.
5. Report the root cause and the smallest operational or code-level remedy;
   do not change deployment inputs or production state during this
   investigation.

## Compatibility and deployment

This is a read-only investigation. No persisted state, API, protocol, schema,
or deployed configuration will be changed. If a follow-up fix is needed, its
deployment and mixed-version implications will be planned separately. Merely
building or publishing an existing Nix closure is compatible with current
nodes; changing the production vpsAdminOS pin or kernel must be treated as a
separate deployment decision.

## Testing plan

- Evaluate the exact backuper2 derivation and compare its kernel `.drv` and
  output paths to the cache narinfo records.
- Reproduce substitution-only resolution where practical.
- Correlate the current vpsAdminOS flake outputs with GitHub Actions run logs
  and cache publication.
