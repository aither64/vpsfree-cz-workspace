let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=7b5acc05d3b005ebfb4f05c2cc58d636faaabd1e";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell { packages = [ pkgs.bash pkgs.coreutils pkgs.git pkgs.nix pkgs.python3 ]; }
