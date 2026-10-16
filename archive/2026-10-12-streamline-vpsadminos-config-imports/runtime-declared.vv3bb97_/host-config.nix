# Reuse the original host build; test source and guest inputs stay current.
{ lib, ... }:
let
  hostSource = /nix/store/hzblqf1z79akb3wrck2xqmfi791g0xk4-source;
  inputs = (builtins.getFlake ("path:" + toString hostSource)).lib.testFramework.sourceInputs;
in
{
  system.vpsadminos = {
    revision = "edb90d2fe2190d88d8b9d2d21bd0def79eedc898";
    revisionDirty = false;
    versionSuffix = ".git.edb90d2fe";
  };
  nixpkgs.overlays = lib.mkForce (
    import (hostSource + "/os/overlays") {
      inherit (inputs) netlinkrb ruby-lxc;
    }
  );
}
