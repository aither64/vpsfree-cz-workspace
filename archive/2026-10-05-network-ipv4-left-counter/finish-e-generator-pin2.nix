let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=94f9f8061b8ae6db3f98fbd8a2e1c73490869cd7";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell { packages = [ pkgs.bash pkgs.coreutils pkgs.git pkgs.nix pkgs.python3 ]; }
