{
  description = "Local-input aitherdev deployment wrapper for agent teams";

  inputs = {
    workspace.url = "git+file:///home/aither/workspace/ai/vpsfree.cz?rev=0ccd1101f56499b69312c72de82f4171dde08762";
    vpsfree-dev-workspace.url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-dev-workspace.git?rev=583647dd998e5b4cb0e9fa6833e29bb5aec757b8";
    dev-workspace.url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=cf778e0559c39f88125d96e0e121b9470cad9ef5";
    codex-web = {
      url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/codex-web.git?rev=52b8ca6e9ddf2175d1a9163996fa9073f9c1882d";
      flake = false;
    };

    workspace.inputs.vpsfree-dev-workspace.follows = "vpsfree-dev-workspace";
    vpsfree-dev-workspace.inputs.dev-workspace.follows = "dev-workspace";
    dev-workspace.inputs.codex-web.follows = "codex-web";
  };

  outputs = { workspace, ... }: {
    packages.x86_64-linux.default = workspace.packages.x86_64-linux.default;
  };
}
