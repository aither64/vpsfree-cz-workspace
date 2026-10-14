let
  source = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace?rev=0ff827df13e82dfab4b536ff29979280f264e8f5";
  pkgs = import source.inputs.nixpkgs { system = "x86_64-linux"; };
in pkgs.mkShell {
  packages = [ pkgs.ruby pkgs.bash pkgs.coreutils pkgs.diffutils pkgs.git pkgs.util-linux ];
  DEV_WORKSPACE_HOST_SOURCE = "/nix/store/y7r40b5h4hd44jfzan4kv1zar3rxmyyl-source";
  DEVCLUSTER_RUNTIME_CONTRACT = "/nix/store/y7r40b5h4hd44jfzan4kv1zar3rxmyyl-source/portal/internal/session/runtime-contract.json";
  VPSFREE_KB_ENGINE_METADATA = "/nix/store/8h3aayb16fhr7h36r6gvwx5a824rh80k-vpsfree-kb-runtime-source.json";
}
