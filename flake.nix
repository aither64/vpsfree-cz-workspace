{
  description = "vpsFree.cz development workspace policy and records";

  inputs = {
    nixpkgs.follows = "vpsfree-dev-workspace/nixpkgs";
    vpsfree-dev-workspace.url = "github:vpsfreecz/dev-workspace/60649982d0f912d4ae398e7666f786b3921ec601";
  };

  outputs =
    {
      self,
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
    in
    {
      packages.${system} = {
        default = package;
        vpsfree-dev-workspace = package;
      };
      apps.${system}.workspace-host = {
        type = "app";
        program = "${package}/bin/workspace-host";
      };
      checks.${system}.deployment-contract =
        pkgs.runCommand "dev-workspace-deployment-contract-tests"
          {
            nativeBuildInputs = [ pkgs.ruby ];
          }
          ''
            cp -R ${self} source
            chmod -R u+w source
            patchShebangs source/bin
            ruby source/test/deployment_contract_test.rb
            touch "$out"
          '';
    };
}
