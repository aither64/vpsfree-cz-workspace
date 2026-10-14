let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=73a686c274205ee2cfa92a91c8da4e1625ecc027";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell { packages = [ pkgs.bash pkgs.coreutils pkgs.git pkgs.nix pkgs.python3 ]; }
