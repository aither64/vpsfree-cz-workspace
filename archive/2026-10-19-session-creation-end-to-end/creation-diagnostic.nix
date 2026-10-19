# Driver diagnosis only: actual already-built package, current test driver.
# This intentionally does not certify the final source/package derivation.
let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-session-creation-end-to-end/dev-workspace";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in
import (source.outPath + "/nix/tests/session-creation.nix") {
  inherit pkgs;
  self = source;
  mkPackage = _: builtins.storePath "/nix/store/xbwqqax8kgy7pw8jhcv1j2wsjhfv823c-dev-workspace-0.2.0";
}
