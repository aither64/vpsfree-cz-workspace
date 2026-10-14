let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell {
  packages = [ (pkgs.ruby.withPackages (gems: [ gems.minitest ]))
    pkgs.bash pkgs.git pkgs.tmux pkgs.coreutils pkgs.util-linux ];
}
