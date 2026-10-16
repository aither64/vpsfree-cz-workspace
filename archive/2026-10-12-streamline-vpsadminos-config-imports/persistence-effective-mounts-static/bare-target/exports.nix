# Parent-owned evaluation only. This artifact is not a product test runner.
let
  source = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos;
  flake = builtins.getFlake ("git+file://" + toString source);
  check = flake.checks.x86_64-linux.nixos-container-persistence;
  suite = import (source + "/tests/suite/dist-config/nixos-persistence-upgrade.nix") {
    system = "x86_64-linux";
    pkgs = flake.inputs.nixpkgs.outPath;
    testFramework = flake.lib.testFramework;
  };
in
{
  inherit (check.evaluation) assertions;
  snippets = builtins.mapAttrs (_: fixture: {
    inherit (fixture) snippet;
    mounts = fixture.earlyMountScript.text;
  }) check.evaluation.shellFixtures;
  scripts = builtins.mapAttrs (_: value: value.script) suite.config.testScripts;
}
