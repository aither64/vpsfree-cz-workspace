# Session-only evaluation of existing suite inputs. No alternate test runner.
let
  source = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos;
  flake = builtins.getFlake ("git+file://" + toString source);
  suite = import (source + "/tests/suite/dist-config/nixos-persistence-upgrade.nix") {
    system = "x86_64-linux";
    pkgs = flake.inputs.nixpkgs.outPath;
    testFramework = flake.lib.testFramework;
    # Intentionally reuse the already-tested host. Its source code and inputs
    # are unchanged by this test-script-only correction; compare exact outputs.
    configuration = import ../runtime-effective.yf2uje2x/host-metadata.nix;
  };
in
{
  config = suite.config;
  persistenceCheck = flake.checks.x86_64-linux.nixos-container-persistence.drvPath;
}
