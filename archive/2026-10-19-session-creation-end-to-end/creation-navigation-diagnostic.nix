# Driver diagnosis; final exact source/package acceptance remains required.
let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-session-creation-end-to-end/dev-workspace?rev=28618437ecbd615ef4f2dd8090629cf8c9248730";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in
import (source.outPath + "/nix/tests/session-creation.nix") {
  inherit pkgs;
  self = source;
  mkPackage = _: builtins.storePath "/nix/store/bgkj0y921xi3q91a0rmjil6ww44hs2jh-dev-workspace-0.2.0";
}
