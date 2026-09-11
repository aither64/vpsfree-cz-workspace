# Repair daily dependency updates and refresh Codex

## Goal

Diagnose and fix vpsfree-cz-configuration daily-update, run the repaired
workflow to publish current llm-agents for the newest stable Codex, and refresh
any independent pin used by development sessions.

## Affected components

- vpsfree-cz-configuration: daily-update workflow and generated input/dependency
  updates. Feature branch/worktree: 2026-09-11-daily-update-llm-agents.
- dev-workspace and/or this workspace: inspect ownership of the separate
  llm-agents input used by the user-profile runtime; update the owning pin in
  an isolated feature worktree if needed.

## Approach

1. Inspect failed job logs, updater, hook configuration, and pin consumers.
2. Reproduce the failure and make the smallest supported repair, keeping
   functional changes separate from generated dependency updates.
3. Run quick verification and mandatory adaptive review on committed changes.
4. Publish the workflow fix through fast-forward integration and dispatch the
   workflow; investigate failures and verify published llm-agents/Codex.
5. Refresh the separate development-session dependency pin, verify its package,
   and integrate reviewed changes where authorized. Keep this session open.

## Compatibility and deployment

The workflow already updates and pushes default-branch dependencies; the user's
request to repair and run it authorizes that existing behavior. No deployment
or service restart is requested. Do not alter active conversations or other
sessions. The user-profile workspace is independent from system configuration.
Keep Numtide's Codex package and its nixpkgs identity intact for cache reuse.
No database/schema, persisted format, API, protocol, client, or node changes are
intended. Dependency updates remain revertible in Git; runtime activation, if
needed, must respect existing active-session ownership and package contracts.
No coordinated node upgrade is needed.

## Testing plan

Use the configuration Nix development shell and mandatory hooks. Reproduce and
check the hook-signature failure after bundle updates. Check workflow syntax
and actual GitHub Actions execution, including generated commits and final
push. Evaluate old/new Codex versions and llm-agents revisions for configuration
and development-session consumers. Realize the package from its configured
cache and verify --version when feasible. Run applicable workspace/package
checks for any independent pin update.
