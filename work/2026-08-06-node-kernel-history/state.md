# 2026-08-06-node-kernel-history

## Repositories

- `vpsadminos`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadminos`
  - final/base revision: `008aa4605ec263397bf46bd9fe915a01be1670a6`
- `vpsadmin`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin`
  - base: `92bba722b16d8f1e68e183f7041be1d44a17db7d`
  - head: `bc6eb8e20f9cc4fa7b9c9f22650bc2cd235fc33d`
- `vpsadmin-kb-captures`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin-kb-captures`
  - base: `7248a8b`
  - head: `c3c1eb5c0d544149432417d3d92a64b653b75411`
- `vpsfree-cz-configuration`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsfree-cz-configuration`
  - base: `d6f1c5d1`
  - head: `157eea17eb8249d22fff214016723cdf324cb92f`

## Status

- The approved redesign is implemented and committed in vpsAdmin,
  vpsfree-cz-configuration, and vpsadmin-kb-captures.
- The proposed vpsAdminOS livepatch completion service and reporter changes
  were removed. Its branch now points directly to the existing `008aa460`
  livepatch release and has no feature diff.
- All four rewritten feature branches are pushed to their SSH origins.
- Quick checks pass. Mandatory fresh-context review, long integration testing,
  final CI confirmation, and development-cluster refresh remain.
- No production deployment or production KB write is authorized.

## Final commits

- `vpsadmin`
  - `5c3e59a95` — `api: record observed livepatch lifecycle`
  - `01af411e3` — `webui: label effective livepatch lifecycle`
  - `32035b72c` — `webui: simplify inferred version timestamps`
  - `bc6eb8e20` — `tests: cover compact history tooltip in browser`
- `vpsfree-cz-configuration`
  - `40242970` — generated production vpsAdminOS pin to `008aa460`
  - `53e0664a` — generated vpsAdmin role pins to `bc6eb8e2`
  - `157eea17` — observed-livepatch deployment runbook
- `vpsadmin-kb-captures`
  - `c3c1eb5` — final vpsAdmin documentation-contract pin
- `vpsadminos`
  - no feature commit; final revision is `008aa460`

## Implementation results

- Public history now compares effective patch sets. The first stable
  loaded/enabled observation creates inferred `applied`; disappearance creates
  inferred `removed`; inventory and metadata changes remain internal.
- Stable patches present at boot do not create a redundant lifecycle row.
- Legacy application and verification marker timestamps are ignored for new
  lifecycle timing. The optional verification field remains accepted for
  compatibility.
- The migration reclassifies safe availability-only rows, converts only exact
  old marker/event matches to inferred applications, repairs current markers,
  and leaves ambiguous history generic.
- WebUI and API expose only `applied`, `removed`, and the null/generic fallback.
- Bounded inferred timestamps visibly show the lower bound and retain the full
  interval in mouse-hover and keyboard-focus detail across version tables. The
  Czech catalog contains complete, non-fuzzy translations for these strings.
- Configuration keeps all vpsAdminOS channels at `008aa460` and points all
  vpsAdmin roles at `bc6eb8e2` using generated `confctl --commit` updates.
- The runbook removes the coordinated reporter rollout and exact-timestamp
  claims, and documents the one-way migration and supervisor quiescence.
- The KB contract found no owned administrator Node-history screenshots, so no
  PNG regeneration or production KB candidate is required.

## Quick verification

- vpsAdmin API recorder/resource specs: 41 examples, 0 failures.
- vpsAdmin migration specs: 5 examples, 0 failures. They must run separately
  from ordinary API specs because the migration helper switches to an isolated
  schema; mixing the suites caused later ordinary specs to see missing tables.
- libnodectld security-evidence specs: 7 examples, 0 failures.
- WebUI PHPUnit regression: 13 tests, 73 assertions.
- API i18n generation and WebUI locale generation passed.
- WebUI translation health passed after adding the missing Czech compact-time
  translations and removing two incorrect fuzzy matches.
- All rewritten vpsAdmin commits passed declared Overcommit checks, including
  Nixfmt, migration specs, RuboCop, PHP CS Fixer, and i18n validation.
- `git diff --check` passes in the affected worktrees.
- vpsAdminOS has no diff from `008aa460`; the existing
  `tests/suite/kernel/livepatch-6.12.95.nix` is unchanged.
- Configuration Overcommit/Nixfmt passed for all commits. Exact pin assertions
  passed for all six channel inputs.
- The configuration dev shell does not include MkDocs. The first documented
  shell attempt failed with `mkdocs: not found`; using
  `nix shell nixpkgs#mkdocs -c mkdocs build --strict` passed.
- KB `nix develop -c bin/check` passed: 39 controls, 29 paths, 32 capture
  concepts, 65 bindings, 9 exceptions, 15 tests, and 118 PNG variants.

## GitHub Actions

- The prior implementation's reruns were affected by the 2026-08-06 GitHub
  outage and self-hosted-runner availability. Those results do not validate the
  rewritten head.
- The first rewritten head's i18n workflow `31183328857` found three empty
  Czech translations and two incorrect fuzzy matches that the generation
  command alone did not reject. The exact log was inspected, the translations
  were completed, and local `locales-health` now passes. A follow-up workflow
  on `d34b9a3d` passed before that correction was folded into its owning
  timestamp commit.
- Superseded aggregate/API runs `31118349379`, `31183328520`, `31183328344`,
  and `31184331945` were cancelled after their heads were replaced. Fresh
  workflows for final head `bc6eb8e20` are pending/running and will be evaluated
  after review.
- The vpsAdminOS branch was force-updated from the discarded feature commit to
  existing revision `008aa460`; no new vpsAdminOS commit requires validation.

## Development cluster

- The existing bridge-network cluster
  `2026-08-06-node-kernel-history` is still running from the superseded
  implementation and must be refreshed after review/integration.
- WebUI: `https://webui.aitherdev.int.vpsfree.cz/`
- Kernel history page:
  `https://webui.aitherdev.int.vpsfree.cz/?page=node&action=kernel_history&id=101`
- A task-local launcher snapshot is retained at
  `dev-clusters/vpsadmin-node-kernel-history/` because the shared launcher has
  unrelated concurrent changes. Those shared changes remain untouched.

## Compatibility and rollback

- Mixed node reporter versions are supported without a protocol bump.
- No coordinated vpsAdminOS rollout or reboot is required for history.
- The nullable action and appended internal event preserve old public enum and
  wire values.
- The data correction is one-way. If API rollback is unavoidable after it,
  old supervisors remain paused until the new recorder returns or an explicit
  semantic-regression plan is approved.

## Mandatory review

- Pending. Provide the standalone reviewer with this plan/state, all four
  worktrees, base/head revisions, exact configuration pins, quick-test results,
  compatibility assumptions, and the unchanged release-specific vpsAdminOS
  test decision.

## Cleanup

- Feature worktrees and the review cluster remain intentionally available.
- Temporary build output was written only below `/tmp`.
- Top-level shared-workspace changes unrelated to this initiative were
  preserved and not staged.
