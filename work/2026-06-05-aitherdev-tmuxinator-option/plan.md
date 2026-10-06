# Fix aitherdev tmuxinator option conflict

## Goal

Fix the `aitherdev` machine build in `vpsfree-cz-configuration`, which fails
because `home-manager.users.aither.programs.tmux.tmuxinator.projects` is
declared twice.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Create a fresh worktree and branch from current `origin/master`.
2. Read repository-local instructions.
3. Inspect the `aitherdev` machine config and the shared tmuxinator module.
4. Remove or convert the duplicate option declaration while preserving the
   configured tmuxinator projects.
5. Verify the targeted aitherdev build/evaluation.

## Compatibility and deployment

This is a configuration-only fix for one development machine. It does not
change persisted state, database schemas, API contracts, generated clients,
NixOS/vpsAdminOS protocol formats, or cluster-wide module options.

The only deployment effect should be that the `aitherdev` Home Manager
configuration can evaluate again. Old and new configurations do not need
coordinated rollout. Rollback should be safe because no state format is changed.

Home Manager 26.05 now declares
`programs.tmux.tmuxinator.projects` and generates tmuxinator project files
itself. The local `aitherdev` shim duplicated that declaration. Removing the
shim keeps the same project configuration surface and lets Home Manager own the
file generation.

## Testing plan

- Run the failing `nix build --json --no-link --impure --no-write-lock-file
  --no-update-lock-file` command or the closest local equivalent for
  `aitherdev` toplevel and autoRollback.
- Run repository hook/lint checks.
