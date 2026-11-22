# Container repository module must apply osctl overlay inputs

## Symptom

Evaluating the vpsFree.cz NixOS build machine fails with infinite recursion at
`os/overlays/osctl.nix:1:1`. A full trace first mentions a `pkgs` argument in
the nixpkgs Bluetooth module, which is only an incidental place where `pkgs` is
forced.

## Cause

vpsAdminOS commit `b0c2ea255` changed `os/overlays/osctl.nix` from a normal
two-argument nixpkgs overlay to a function that must first receive the source
inputs `netlinkrb` and `ruby-lxc`. Most callers were updated, but
`os/modules/services/misc/build-vpsadminos-container-image-repository/nixos.nix`
continued to put an unapplied `(import ../../../../overlays/osctl.nix)` in
`nixpkgs.overlays`.

Nixpkgs therefore passes its recursive final package set as the source-input
argument. Inspecting that set while it is still being constructed closes the
cycle and reports infinite recursion.

## Verification

With the current vpsFree.cz configuration, overriding only
`vpsadminosOsStaging` to `b0c2ea255` reproduces the recursion. Overriding it to
the parent `13d07aa36` or the last pre-update pin `14843dbb` evaluates beyond
this failure and reaches the unrelated, expected missing local ISO error.

The first vpsFree.cz configuration revision to contain the bug is `a10a50a7`,
which updated `vpsadminosOsStaging` from `14843dbb` to `0236bcd3` on
2026-06-13.

## Fix direction

The container-image repository module must install an already-applied osctl
overlay with the matching `netlinkrb` and `ruby-lxc` flake source inputs. Keep
path-based consumers of this NixOS module in the compatibility design.

Related initiative: `work/2026-08-07-vpsfconf-build-error/`.
