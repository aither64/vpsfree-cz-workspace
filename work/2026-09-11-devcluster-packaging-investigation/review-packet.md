# Review packet: both packaged development-cluster providers

## Request and accepted boundary

Implement the plan in plan.md: repair missing defaults, out-of-flake runner source,
vpsAdminOS overlay/gem dependencies, and start/update failure propagation. Deploy
the package and validate both providers. Retain all feature branches unmerged.
Do not mutate the password-reset session, merge defaults, archive, delete sessions,
or deploy system configuration. Do not build Linux kernels locally unless the
workspace's explicit cache exception is established.

## Repositories and revisions

Workspace: /home/aither/workspace/ai/vpsfree.cz
Initiative: work/2026-09-11-devcluster-packaging-investigation
Organization worktree: worktrees/2026-09-11-devcluster-packaging-investigation/vpsfree-dev-workspace
Branch: 2026-09-11-devcluster-packaging-investigation
Base: 0a9c974994746e2a6d9d74e83cde8abbf0e65f0a
Head: see exact SHA appended below.

Other registered worktrees under this initiative:
- workspace: f50473c base, currently unchanged; will receive only a generated pin
  of the reviewed/pushed extension after review. That mechanical pin update does
  not add a new design; check the existing consumer flake and deployment contract.
- vpsadmin: 8d0ccafd5b307115ddc4b1f24152ba30ed52e893, unmodified test input.
- vpsadminos: 3eaf7b7320754715b38fc629e7f0ce23d13402cd, unmodified test input.

## Commit series

1. 55830a7: install defaults and shared runner inside each packaged flake, install
   assertions and related stable-command/config documentation.
2. 30516d8: vpsAdminOS overlay arguments and source-gem configuration.
3. 35a7090: checked return paths for credentials/config/start/update/refresh;
   command tests with failed external tools, retained results and lock assertions;
   documentation of partial-update behavior.
4. Final test commit: locked test-only inputs, packaged Nix smoke app, CI invocation
   and associated documentation. Generated lock entries belong to this test app;
   the generic runtime and package nixpkgs inputs are unchanged.

## Ownership, interfaces, consumers

The organization extension owns both shell providers and nested flakes. The
common Ruby runner source stays under dev-clusters/lib and is copied into each
package subtree. Nix imports only the provider subtree at runtime. The consuming
workspace supplies validated siteConfig.clusterDefaults; each provider still
merges its defaults with retained per-cluster config.

The generic runtime is unchanged at bcbaf825d71285cbbd05b56e78bc386f2df480bd.
Its immutable extension catalog dispatches stable commands with workspace identity,
package-generation gates and lifecycle/socket contracts. See workspace/flake.nix,
the organization's mkPackage and installed generic source/worktree as needed.

The runtime provider uses the initiative's vpsAdmin source and OS worktree or bare
origin/staging input. CI uses locked test-only vpsAdmin 8d0ccafd5, OS 3eaf7b732 and
vpsf-status 587cd65b. Provider CLI/schema/socket/state/VM-disk formats are unchanged.
The new devcluster-check flake app is a test interface, not a cluster management
command. The actual dependency interface is visible in vpsAdminOS overlays and
runner gemset at its pinned source.

## Risk, compatibility, trust

High risk due to host-side start/update, persisted cluster state and deployment.
Use gpt-5.6-sol, xhigh, for all four lanes: general, architecture, scope, risk.
Run each review directly without nested agents. This packet records facts and
accepted constraints; form findings independently.

Maintain existing callback environment exports, lock release and nested lock
identity. Explicit return checks are chosen over a broad shell/lock redesign or
subshells that discard exports. Keep old build results for recovery but never
consume them following a failed build. Stop subsequent deployment steps on a copy,
activation or refresh failure; previously updated nodes retain their configuration.
No database/API/protocol migration or coordinated production node update is needed.
Rollback retains old state readability, but old package startup defects still exist.

The local operator is trusted to administer the development host for workspace
integration and migration. Ownership assigns operational responsibility and does
not contain that operator. Preserve ordinary path/ownership checks, serialization,
credential integrity, retry/rollback behavior. This does not weaken remote-client
or guest/host boundaries or KB publication approval.

## Quick verification and remaining acceptance

- Both changed shell helpers pass bash -n; changed Ruby files parse.
- New actual-command tests: 6 runs, 110 assertions, no failures/errors/skips.
- Existing status/lifecycle suite: 46 runs, 516 assertions, no failures/errors/skips.
- Package asset install checks pass and package builds; inherited Go and Ruby
  package checks passed (285/2737 + 73/438, declared sandbox-only skips).
- Nix formatting and git diff --check pass. Official action tags verified:
  checkout v7.0.1 and install-nix-action v31.11.1, unchanged.
- Packaged smoke app builds and is undergoing configuration/runner evaluation;
  record its final results before deployment. Full flake/CI and all live VM
  start/update/stop/restart/data-retention acceptance remain after review.

The investigation.md and evidence.txt document the original failures and temporary
proofs. State.md records ongoing work. Do not start VM integration tests or change
project files during review. Return findings with severity, code/commit references,
concrete failure scenarios and residual gaps.
5802fd67832a6e7490fa9d166ae9541cd4dff103

## Post-review remediation

The source helper is now shared as dev-clusters/lib/runner.nix and installed in
both provider shared/ directories. It imports vpsadminos.overlays.all, bundles
source gems once, preserves provider entry points/RUBYLIB and forces interface
validation during configuration evaluation. Both docs declare minimum 6f9b2c755;
older worktrees require rebase, without state conversion. The earlier smoke at
961dadf passed all eight configs and both runner loads. Read state.md reconciliation
for all findings and explicit residual credential decision. Updated commits follow.
44c3e4647e0834e971a5167d8019228f35f6f0b7 test: evaluate and load both packaged development clusters
3af634f6869a6a8e73389c4325abb152065581e6 devcluster: stop start and update after prerequisite failures
9cc72e1467d622423f054b4a92480814ed0b8f50 devcluster: use current vpsAdminOS runner dependency interfaces
55830a78c7bac70ea16ec234c2b0afce8a70c4d9 devcluster: include configuration and runner assets in packaged flakes
