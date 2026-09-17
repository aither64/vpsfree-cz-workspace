# Nix derivation JSON includes an explicit schema wrapper

In this environment, nix derivation show returns a top-level version and
an object named derivations. Derivation keys are basenames, and output paths
are store-relative names. Scripts expecting the older direct mapping keyed
by absolute drv path fail with KeyError.

Inspect the installed command's output before consuming it. Read the entry
under payload["derivations"][drv_basename], and restore /nix/store/ when using
an output path with filesystem commands. Provider dependencies are under
inputs.drvs and source dependencies under inputs.srcs. Avoid dumping full env
or compiler commands when only output paths are needed.

Verified with corrected6.12.109 normal/debug derivations. Related initiative:
work/2026-09-12-nfs-cancellation.
