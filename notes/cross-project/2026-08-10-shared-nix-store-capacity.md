# Shared development host Nix store capacity

## Symptom

Small writes failed with `No space left on device` even after removing local
worktree caches. `df -h /` showed zero space available to the non-root user,
while an unrelated concurrent `nix build` continued adding store paths.

## Cause

The shared root filesystem crossed its reserved-space threshold during a large
KVM initrd build. The active build held temporary Nix GC roots, so an initial
garbage collection could not reclaim its closure.

## Workaround

Do not remove another session's worktree or interrupt its build. Remove only
caches owned by the current initiative, wait for the active Nix build to exit,
then run the standard collector:

```sh
nix-store --gc
```

Active builds and permanent roots are protected; the collector removes only
unreferenced, rebuildable store paths.

## Verification

For `work/2026-08-09-test-vm-kernel-oops`, garbage collection after the
concurrent build exited restored 261 GiB of available space. Repository data
and active worktrees were unchanged.
