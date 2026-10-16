# The native runner's public helper and original parameters, with host pinning.
let
  source = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos;
  testJson = import (source + "/test-runner/nix/evaluate-tests.nix") {
    repoRoot = source;
    system = "x86_64-linux";
    testConfigPath = ../../image-test-config.nix;
    mode = "testJson";
    testPath = "dist-config/nixos-persistence-upgrade";
    testArgsJson = "{}";
    configuration = import ./config.nix;
  };
in
testJson.text
