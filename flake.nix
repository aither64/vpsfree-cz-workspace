{
  description = "vpsFree.cz development workspace policy and records";

  inputs = {
    nixpkgs.follows = "vpsfree-dev-workspace/nixpkgs";
    vpsfree-dev-workspace.url = "github:vpsfreecz/dev-workspace/3e3f0ff7c2d23f08f19887822efa12f969bbb56f";
  };

  outputs =
    {
      nixpkgs,
      vpsfree-dev-workspace,
      ...
    }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      siteConfig = {
        kb = {
          cz = {
            url = "https://kb.vpsfree.cz";
            tokenPath = "/home/aither/.codex/codex-kb-vpsfree-cz-aither-key";
            stagingUrl = "http://kb-cs.aitherdev.int.vpsfree.cz";
            stagingPasswordPath = "/home/aither/.codex/codex-kb-staging-cz-aither-password";
          };
          org = {
            url = "https://kb.vpsfree.org";
            tokenPath = "/home/aither/.codex/codex-kb-vpsfree-org-aither-key";
            stagingUrl = "http://kb-en.aitherdev.int.vpsfree.cz";
            stagingPasswordPath = "/home/aither/.codex/codex-kb-staging-org-aither-password";
          };
          stagingUsername = "aither";
          stageContainerctl = "/run/current-system/sw/bin/kb-staging-containerctl";
        };
        clusterDefaults = {
          vpsadmin = ./config/vpsadmin-devcluster.json;
          vpsadminos = ./config/vpsadminos-devcluster.json;
        };
      };
      package = vpsfree-dev-workspace.lib.mkPackage {
        inherit pkgs siteConfig;
      };
      migrationBridge = vpsfree-dev-workspace.lib.mkPackage {
        activationEnvironmentAliases = [ "VPSFREE_WORKSPACE_ACTIVATION" ];
        inherit pkgs siteConfig;
        routerSocket = "/run/vpsfree-workspace-router/router.sock";
        userNamespace = "vpsfree-workspaces";
      };
    in
    {
      packages.${system} = {
        default = migrationBridge;
        migration-bridge = migrationBridge;
        vpsfree-dev-workspace = migrationBridge;
        workspace-host = migrationBridge;
        workspace-portal = migrationBridge;
      };
      apps.${system}.workspace-host = {
        type = "app";
        program = "${migrationBridge}/bin/workspace-host";
      };
    };
}
