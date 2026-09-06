---
lifecycle: active
---

# 2026-09-06-portal-config-deployment-policy

## Repositories

- Workspace branch: `2026-09-06-portal-config-deployment-policy`
- Planned worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-06-portal-config-deployment-policy/workspace`
- Initial base: workspace `master` at `cf3e0809b30b0d144f10e2b81aa27ba4e431de87`
- Configuration branch: `2026-09-06-portal-config-deployment-policy`
- Planned configuration worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-06-portal-config-deployment-policy/vpsfree-cz-configuration`
- Configuration `master` baseline:
  `4d570e3053b114518ada59c2a45d5e9d8644347b`. It may advance only to the
  isolated repository-rule commit, never to the later portal pin.

## Status

- Session created without launching a duplicate Codex client. The current API
  agent owns implementation.
- Initial tracking prepared before the workspace feature worktree is created.
- The user corrected the new-session default to `xhigh`. The earlier deployed
  `max` default came from an explicit earlier instruction in the portal thread;
  the newer instruction supersedes it.
- The user expanded the initiative to replace the host-bound portal deployment
  with a hybrid privileged-system/user-service architecture, correct initiative
  completion semantics, add archive reopening, and recover a prematurely
  archived legacy initiative.
- The earlier `xhigh` and deployment-policy commits remain useful inputs, but
  the implementation and configuration feature branches now require a larger
  refactor. The generated configuration pin is obsolete under the chosen
  architecture and will be replaced before the branch is pushed.

## Commands run

- `dev-session current`
- `dev-session start portal-config-deployment-policy --no-codex --no-attach`
- Inspected the current workspace rules and the configuration repository's
  local instruction topics.
- Created both initiative worktrees with `dev-session worktree add`.
- Ran the focused and complete portal Go tests, Go vet, both flake evaluations,
  and focused diff checks.
- Updated the configuration input with
  `confctl inputs channel set --commit workspace-tools
  aither-vpsfree-workspace 9251c2be8c879fb40bcda995b72b0a1584e679f2`.
- Inspected the current package, NixOS services, CLI lifecycle implementation,
  manifest schema, archive workflow, user systemd state, ports, and Codex
  runtime coupling.
- Verified the retained local and remote branches for
  `2026-09-05-cgroup-v1-shared-device-fix`, its committed legacy archive, its
  lack of a portal manifest or live runtime conflicts, and its original merge
  bases.

## Results

- No existing development session belongs to this process.
- Workspace code and rules require changes. Configuration receives one durable
  policy-only commit eligible for integration, followed by an exact development
  pin that remains only on the initiative branch for deployment.
- Workspace commits:
  - `6c6ade3`: durable top-level deployment/integration rule;
  - `9251c2b`: shared portal and CLI default changed to `xhigh`, with tests and
    documentation.
- Configuration commits:
  - `a3e4276b`: durable repository-local deployment/integration rule;
  - `bf8a0b61`: generated development pin for workspace `9251c2be`.
- The configuration policy commit and branch were pushed before the generated
  pin. Configuration `master` remains at its baseline `4d570e30`; the generated
  pin is local and unmerged.
- All portal Go packages and Go vet passed. Workspace and configuration
  `nix flake check --no-build -L` both passed. The resolver regression verifies
  `xhigh` for the default model, an explicit effort override, and fallback to
  an explicitly selected model's advertised default when it lacks `xhigh`.
- Configuration worktree creation again completed in Git but returned exit 78
  because its post-checkout Overcommit hook could not load Nix-provided gems in
  the ambient shell. The worktree is registered and clean apart from generated
  `.bin` and `.bundle` development-shell caches. Both configuration commits ran
  their declared hooks successfully inside `nix develop`.

## Open questions

- None. The hybrid boundary, multi-workspace domain and CLI selection,
  system-Codex source, `xhigh` default, lifecycle rules, and exact recovery
  target are decision complete.

## Cleanup

- Remove the workspace worktree without force after integration.
- Remove the configuration worktree without force after deployment, retain its
  unmerged feature branch, and archive this initiative when complete.
