{
  description = "Local-input aitherdev deployment wrapper for agent teams";

  inputs = {
    workspace.url = "path:../../../worktrees/2026-09-21-agent-teams-workflow/workspace";
    vpsfree-dev-workspace.url = "path:../../../worktrees/2026-09-21-agent-teams-workflow/vpsfree-dev-workspace";
    dev-workspace.url = "path:../../../worktrees/2026-09-21-agent-teams-workflow/dev-workspace";
    codex-web = {
      url = "path:../../../worktrees/2026-09-21-agent-teams-workflow/codex-web";
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
