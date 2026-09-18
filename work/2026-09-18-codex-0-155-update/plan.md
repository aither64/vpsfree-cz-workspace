# Codex 0.155.0 rollout for aitherdev

## Goal

Update the development workspace, vpsFree extension and aitherdev configuration
to Codex 0.155.0. Deploy the configuration from its feature branch, switch the
shared workspace profile, and verify that its App Server uses the same version
after its clients are idle.

## Affected repositories

- `dev-workspace`: pin `llm-agents.nix` at
  `ddc89534b9a73cd99ff4d33656569ce3be6e6490` in its source and lock file.
- `vpsfree-dev-workspace`: pin the generic runtime feature revision.
- `vpsfree-cz-configuration`: pin both its independent `llm-agents` input and
  `devWorkspace` through `confctl`, then deploy `cz.vpsfree/machines/aitherdev`.
- `vpsfree-cz-workspace`: pin the extension feature revision and provide the
  source used by `workspace-host switch`.

## Approach

1. Create isolated worktrees from the fetched remote default branches.
2. Update the generic runtime and commit the exact Codex pin; propagate its
   feature head through the extension, configuration and consuming workspace.
3. Run quick version and diff checks, then one abbreviated General review using
   `gpt-5.6-terra` at `xhigh`, as directed by the user.
4. Build and dry-activate aitherdev, deploy the feature configuration, then
   switch the workspace user profile from the consuming workspace worktree.
5. Wait for all App Server clients to become idle and verify the active system,
   profile, portal and App Server versions are all `0.155.0`.

## Decisions

- The configuration must update its independent `llm-agents` input as well as
  its `devWorkspace` input. The former supplies system Codex, which the profile
  reconciliation adopts for the shared App Server.
- The current initiative uses no terminal Codex client, so it does not add an
  active native client while reconciliation waits for existing work to finish.
- Keep all feature branches unmerged and retain them after the rollout. The
  user authorized aitherdev deployment, not default-branch integration.

## Compatibility and deployment

No persisted schema, API, or configuration-module interface changes are
introduced. The selected profile bundles a compatible portal and App Server
pair; `workspace-host` validates the selected Codex protocol and model catalog
before activation. The system configuration is deployed before the profile
switch so system Codex and the adopted App Server converge on 0.155.0.

During the transition, the active 0.154.0 profile remains usable until idle
reconciliation can restart the shared service. The previous profile generation
is retained and can be selected with `workspace-host rollback`; the prior
configuration generation remains available through the normal deployment
rollback path.

## Documentation

The runtime README and session guide already document paired profile/App Server
activation, idle reconciliation and rollback. No lasting documentation change
is expected for this exact dependency pin. This plan and `state.md` own the
site-specific rollout, revisions, verification and recovery evidence.

## Testing plan

- Evaluate each selected package's Codex version and inspect generated lock
  changes with `git diff --check`.
- Run relevant Nix flake checks after review, plus aitherdev `confctl build`
  and dry activation before the live deployment.
- Verify system/profile versions, pending reconciliation state, user services
  and portal health after the profile switch.
