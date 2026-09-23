{
  description = "aitherdev site package with team lead delegation";

  inputs = {
    workspace.url = "git+file:///home/aither/workspace/ai/vpsfree.cz?rev=8fe84327f656f1112b860a26b1e1ebd42bccc8ff";
    vpsfree-dev-workspace.url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-dev-workspace.git?rev=ad13e7fc2a1874a54921bb91d743e4a4851d3c4a";
    dev-workspace.url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=1b836baf85e8486e0455ce2a70f9c4423328ac22";
    codex-web = {
      url = "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/codex-web.git?rev=01e75798654b5c56535646dea687468a358408fb";
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
