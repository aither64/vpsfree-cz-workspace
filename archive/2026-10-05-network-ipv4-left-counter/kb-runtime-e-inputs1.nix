let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=0ff827df13e82dfab4b536ff29979280f264e8f5";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell {
  packages = [ pkgs.bash pkgs.coreutils pkgs.diffutils pkgs.git pkgs.nix pkgs.python3 ];
}
