let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime?rev=a50f8c1a11ea642edf823f04521f9eaa97132fd2";
  pkgs = import source.inputs.toolsNixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell {
  packages = [ (pkgs.ruby.withPackages (gems: [ gems.minitest ]))
    pkgs.nodejs pkgs.bash pkgs.git pkgs.coreutils pkgs.util-linux pkgs.shellcheck pkgs.nix ];
  NODE_PATH = "${pkgs.playwright-test}/lib/node_modules";
  VPSADMIN_KB_OSVM_SOURCE = source.inputs.vpsadminos.outPath;
}
