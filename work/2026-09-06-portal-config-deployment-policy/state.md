---
lifecycle: active
---

# 2026-09-06-portal-config-deployment-policy

## Repositories

- Workspace branch: `2026-09-06-portal-config-deployment-policy`
- Planned worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-06-portal-config-deployment-policy/workspace`
- Registered workspace base:
  `c561cb9859b3217c0a8e5476af37c07a4332f060`; the reviewed branch was
  rebuilt as a linear series on current `master` at
  `214f94c466dd9356c7d984f79b60acc8257d35ab`.
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
- The hybrid implementation is committed on both feature branches and is ready
  for mandatory review. Neither default branch has been changed.
- An initial four-lane mandatory review of the earlier commit series found
  unsafe unpaired Codex switching and rollback, a volatile reopen journal, a
  finalization/cluster-release race, privileged password ownership assigned to
  the user, a per-request router keepalive leak, incomplete legacy migration,
  obsolete helpers, and non-reviewable intermediate commits. The implementation
  now addresses every blocking and important finding, and both unpublished
  feature branches have been rebuilt into coherent commits for review reruns.
- The general and architecture reruns found that the first hybrid draft would
  rotate the existing Basic Auth password, remove the legacy runtime before
  proving active turns idle, leave failed profile/Codex transitions partially
  applied, strand interrupted session migrations, miss offline system Codex
  changes, consult the current model catalog during materialized recovery, and
  omit directory fsyncs around archive moves. Remediation is in progress before
  the remaining review lanes and full tests.
- The user selected `gpt-6-astra` with `xhigh` reasoning as the new-session
  default. The live system Codex catalog advertises that exact model ID and
  effort.

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
- Built the workspace package in a clean Nix sandbox. Its Go, Ruby, JavaScript,
  PKI, password, and installed-wrapper checks passed.
- Validated the packaged App Server protocol contract and default `xhigh`
  support against system Codex `0.153.4`.
- Ran the configuration Overcommit hooks successfully in `nix develop` and
  built the aitherdev configuration generation with `confctl build`.
- Re-ran all Go package tests after adding the host transition gate and router;
  all packages passed. The final `workspace-host` suite passed 8 tests with 66
  assertions. The full `dev-session` suite reached 157 tests and exposed only a
  test-fixture value missing for the new transition flag; the corrected focused
  regression passed and a final full package run remains pending after review.

## Results

- No existing development session belongs to this process.
- Workspace code and rules now implement the hybrid runtime. Configuration
  contains only the privileged substrate and ordinary system Codex package;
  its obsolete workspace flake input and development pin have been removed.
- Workspace commits:
  - `333983c`: durable top-level deployment/integration rule;
  - `c61d691`: shared portal and CLI default changed to `xhigh`;
  - `18c6985`: exact merged-head completion proof, archive reopening, and
    portal finalization gating;
  - `124bc79`: mixed-version creation recovery preserves stored settings;
  - `c6d6f4b`: registry-backed user runtime, router, profile deployment, paired
    Codex adoption and rollback, and one-time migration.
- Configuration commits:
  - `e06c183e`: durable repository-local deployment/integration rule;
  - `66f73bc5`: privileged wildcard HTTPS, credentials, router socket, linger,
    and removal of the system-owned workspace application.
- Configuration `master` remains at `4d570e30`; the implementation is unmerged.
- All portal Go packages passed. Workspace and configuration flake evaluation
  passed. The resolver regression verifies `xhigh` for the default model, an
  explicit effort override, and fallback to an explicitly selected model's
  advertised default when it lacks `xhigh`.
- The obsolete workspace-side PKI and password helpers and their tests have
  been removed because NixOS is now the sole privileged substrate owner.
- The aitherdev build produced generation `2026-09-06--17-33-25` from the
  configuration feature worktree. It was built only, not deployed.
- Configuration worktree creation again completed in Git but returned exit 78
  because its post-checkout Overcommit hook could not load Nix-provided gems in
  the ambient shell. Both configuration commits ran their declared hooks
  successfully inside `nix develop`; its untracked `.bin/` and `.bundle/`
  development-shell caches are excluded from commits.

## Open questions

- None. The hybrid boundary, multi-workspace domain and CLI selection,
  system-Codex source, `xhigh` default, lifecycle rules, and exact recovery
  target are decision complete.

## Cleanup

- Remove the workspace worktree without force after integration.
- Remove the configuration worktree without force after deployment, retain its
  unmerged feature branch, and archive this initiative when complete.
