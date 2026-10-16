# Session-only export of the registered suite's actual scripts; no VM build.
let
  source = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos;
  flake = builtins.getFlake ("git+file://" + toString source);
  suite = import (source + "/tests/suite/dist-config/nixos-persistence-upgrade.nix") {
    system = "x86_64-linux";
    pkgs = flake.inputs.nixpkgs.outPath;
    testFramework = flake.lib.testFramework;
  };
in
builtins.mapAttrs (_: script: script.script) suite.config.testScripts
