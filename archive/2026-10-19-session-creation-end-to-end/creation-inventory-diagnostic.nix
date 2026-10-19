# Driver diagnosis using a rooted package containing both reviewed product fixes.
# Final exact source/package acceptance remains a separate required check.
let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-session-creation-end-to-end/dev-workspace?rev=a0799a622610db0eadd0e94a31d0bcd06d75cfd3";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in
import (source.outPath + "/nix/tests/session-creation.nix") {
  inherit pkgs;
  self = source;
  mkPackage = _: builtins.storePath "/nix/store/bgkj0y921xi3q91a0rmjil6ww44hs2jh-dev-workspace-0.2.0";
}
