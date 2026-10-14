let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=d2079f605ae87871037ae73c5e5daf20a3e0d03d";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell {
  packages = [ pkgs.bash pkgs.coreutils pkgs.diffutils pkgs.git pkgs.nix pkgs.python3 ];
}
