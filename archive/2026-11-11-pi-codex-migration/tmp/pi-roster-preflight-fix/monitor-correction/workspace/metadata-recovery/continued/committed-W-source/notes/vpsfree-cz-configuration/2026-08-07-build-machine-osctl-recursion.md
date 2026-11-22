# Build machine evaluation blocked by osctl overlay recursion

## Symptom

`confctl build -y cz.vpsfree/machines/build` fails during NixOS evaluation with
an infinite recursion at `vpsadminos/os/overlays/osctl.nix`. The build does not
reach the machine's custom packages.

## Cause

The failure is present on `vpsfree-cz-configuration` `origin/master` at
`3c3de36a`, using nixpkgs `445d861c` and vpsadminos `c140a894`. An untouched
detached worktree at that commit fails with the same trace, so package-only
changes on top of that revision are not the cause. The underlying
vpsadminos/nixpkgs compatibility defect was not diagnosed further in this
initiative.

## Workaround

Validate an isolated package change by building the package derivation and
running its executable directly. Re-run the complete build-machine evaluation
after the vpsadminos input or overlay is fixed; do not change unrelated channel
pins merely to make a package update pass.

## Verification

For the exporter dependency update, `pkgs.ssh-exporter` built successfully and
Puma served both the root and metrics endpoints. The parallel `int.log` target,
which consumes syslog-exporter, completed a full confctl build.

Related initiative: `work/2026-08-07-exporters-gem-update/`.
