let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=06eefd98d09d756a8791c494cd855ffcfa625548";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell { packages = [ pkgs.bash pkgs.coreutils pkgs.git pkgs.nix pkgs.python3 ]; }
