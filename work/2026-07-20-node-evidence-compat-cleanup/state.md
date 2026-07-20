# Node Evidence Compatibility Cleanup State

## Status

- Initiative: `2026-07-20-node-evidence-compat-cleanup`.
- Status: implementation, quick verification, mandatory review and fresh
  bridge integration complete. Feature branches are pushed for user review;
  default branches are untouched.
- Production premise: the compatible evidence release at vpsAdmin
  `1bca29dfac3dba6a82a857ffad24d42e46ae861e` is deployed throughout the
  cluster.

## Worktrees and bases

- `vpsadmin`
  - base: `1bca29dfac3dba6a82a857ffad24d42e46ae861e`
  - worktree: `worktrees/2026-07-20-node-evidence-compat-cleanup/vpsadmin`
- `vpsfree-cz-configuration`
  - base: `36c0e9ba2f5cdca43d4d3b0541c6b6fa809f699d`
  - worktree:
    `worktrees/2026-07-20-node-evidence-compat-cleanup/vpsfree-cz-configuration`
- `vpsadmin-kb-captures`
  - base: `8f5395f3890792bb9dc7ceb1c379cbef481e26f5`
  - worktree:
    `worktrees/2026-07-20-node-evidence-compat-cleanup/vpsadmin-kb-captures`

All branches are `2026-07-20-node-evidence-compat-cleanup`; remotes use SSH.

## Decisions

- Remove legacy component and old-supervisor runtime compatibility together.
- Keep enum value `3`, canonical `system_configuration`, first-report duplicate
  collapse and the deployed migration unchanged.
- Add no migration or protocol schema-version bump.
- Treat any remaining legacy producer as an unsupported deployment error.
- Expect no visible WebUI, screenshot or KB content change.

## Feature heads

- `vpsadmin`: `1bb84ae9bc792eef5650a030f850409c737b6a91`
  - `52aeb0019` removes legacy payload normalization and the WebUI component
    mapper;
  - `1bb84ae9b` independently removes old-supervisor boot-event reconciliation;
  - retains canonical `system_configuration`, enum value `3`, the corrective
    migration, and first-report reconstructed-boot collapse.
- `vpsfree-cz-configuration`:
  `cd86aa161e6b0e4ac5b58cb8932c6af139fe3c94`
  - replaces the old rollout with an application-only cleanup runbook and a
    read-only deployment safety gate;
  - pins vpsadmin services, staging and production channels to the exact
    vpsAdmin feature head in three generated `confctl` commits.
- `vpsadmin-kb-captures`:
  `3a42eb8a30e54f61fa9d0ede0f93a0dba3401f9a`
  - pins the exact vpsAdmin feature head; no contract or screenshot content
    changed.

## Verification log

- vpsAdmin focused API specs:
  - `spec/models/operations/node/record_kernel_evidence_spec.rb`
  - `spec/supervisor/node/status_spec.rb`
  - result: 45 examples, 0 failures.
- vpsAdmin focused RuboCop: 5 files, no offenses.
- WebUI `NodeEvidencePagesTest`: 11 tests, 57 assertions, green.
- vpsAdmin complete Overcommit pre-commit suite: migration specs, API and
  WebUI i18n health, Nixfmt, PHP-CS-Fixer and RuboCop all green.
- Source audit: no runtime occurrence of
  `LEGACY_SYSTEM_CONFIGURATION_COMPONENT`, `vpsfree_cz_configuration`,
  `node_software_component_key`, `reconcile_existing_reported_boot!`,
  `same_boot?`, or `BootTimeConfidence.from_evidence` remains. The retired
  component spelling remains intentionally in one negative regression.
- Configuration `nix flake check`: green. Channel inspection resolves
  `vpsadminServices`, `vpsadminStaging`, and `vpsadminProduction` to
  `1bb84ae9`.
- Runbook safety-gate Ruby and shell blocks: syntax checks green.
- KB `nix develop -c bin/check`: 39 controls, 29 paths, 32 capture concepts,
  65 bindings, 9 exceptions, 118 PNG variants; all checks green.
- KB `nix flake check`: green. No PNG or KB candidate changed.
- GitHub Actions at initial inspection:
  - vpsAdmin RuboCop, WebUI PHPUnit and i18n health: green;
  - API topic specs: running;
  - integration CI: queued;
  - configuration and KB repositories have no branch runs.
- The initial combined vpsAdmin feature commit was split before mandatory
  review so the two independently reversible compatibility removals are
  separately reviewable. Exact configuration and KB pins were regenerated,
  all three feature branches were force-pushed with exact leases, and queued
  or running Actions for the superseded vpsAdmin head were cancelled.

## Mandatory review

- Standalone reviewer: `/root/node_evidence_compat_cleanup_review`.
- Initial result:
  - Blocking: the runbook checked reporter evidence but not the actual running
    supervisors, leaving a post-gate old-writer race.
  - Advisory: add an exact negative regression for the retired component name.
- Resolutions:
  - the runbook now uses an aborting `confctl ssh` check immediately before
    deployment to require active supervisor services and package revision
    `1bca29df` on both `int.api1` and `int.api2`;
  - the alias-removal commit now asserts the exact retired spelling creates an
    invalid current evidence snapshot, no derived event, and still advances
    ordinary status and system state.
- Final result at the feature heads above: no Blocking or Important findings;
  approved to proceed to the bridge integration scenario.
- Residual risks: current-head CI, the bridge mixed-version scenario, and the
  production gate/backfill premises cannot be proven by repository review.

## Non-obvious command findings

- `nix develop .#webui -c composer exec ...` from the repository root uses
  Composer's global working directory and cannot find project PHPUnit. Run the
  shell with `webui/` as the working directory. The corrected invocation passed.
- A plain `git commit` runs Overcommit outside the required tool environment
  and was rejected for missing RuboCop, gettext, PHP-CS-Fixer and MariaDB.
  Retrying `git commit` inside the root `nix develop` shell passed every hook.

## Bridge integration

- The preceding `2026-07-20-kernel-boot-evidence-history` cluster was stopped.
  Its graceful runner shutdown reached the known 120-second timeout, after
  which the helper killed the runner, released socket processes and removed
  its GC root successfully.
- Fresh cluster: `2026-07-20-node-evidence-compat-cleanup`.
  - topology: `single`;
  - network: `bridge`;
  - status: running and ready; leave it running for review.
- The built closure identified vpsAdmin
  `1bb84ae9bc792eef5650a030f850409c737b6a91` throughout. Running
  `vpsadmin-api` and `vpsadmin-supervisor` process working directories both
  contain that exact `.git-revision`.
- `vpsadmin-api`, `vpsadmin-supervisor`, and node1 nodectld are healthy.
- Migration `20260720120000` is up in the fresh database.
- Node1 current evidence is schema version 1. Both booted and current vpsAdmin
  software identities report exact revision `1bb84ae9`; there are no invalid
  current-evidence errors.
- This generic devcluster image has no confctl configuration metadata, so its
  live report legitimately omits the optional `system_configuration`
  identities. A deployed-runtime parser check built from node1's current
  evidence accepted an appended canonical `system_configuration` identity and
  rejected `vpsfree_cz_configuration` with the exact invalid-component reason.
- Kernel history contains one exact, directly reported current boot and no
  duplicate current row. Current evidence and the current system state
  continued advancing across ordinary status intervals.
- API and WebUI HTTPS endpoints returned HTTP 200 using the devcluster CA.
- Supervisor error journal for the integration window was empty.
- The first ad-hoc runtime script omitted `require 'vpsadmin'` and failed before
  any data access. The corrected read-only parser script loaded the application
  and passed; the temporary script was removed automatically.

## Remaining work

- Observe current-head GitHub Actions and investigate any failure from logs.
- Obtain user review before any default-branch integration. The fresh cluster
  remains running for that review.
