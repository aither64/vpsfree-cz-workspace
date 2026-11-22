# Preserve Git identity when evaluating vpsAdminOS systems

A system evaluation using `builtins.getFlake (toString root)` loads a path flake without `rev`/`dirtyRev`. QEMU channel registration then fails with `cannot coerce null to a string` when forcing the toplevel derivation: the existing channel recipe interpolates `system.vpsadminos.revision`.

Use `builtins.getFlake ("git+file://" + toString root)` for local Git-worktree evaluation, matching normal flake invocation and retaining real clean/dirty Git metadata. Do not work around this by changing product configuration. This was reproduced through metadata inspection during [proactive-swap removal](../../work/2026-10-16-proactive-swap-patch-removal/state.md); corrected evaluation is recorded there.
