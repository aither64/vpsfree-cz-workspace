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
  - head: `91b574aefc49aabb9c3fdc867120a0946b40c324`
- `vpsadmin-kb-captures`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin-kb-captures`
  - base: `7248a8b`
  - head: `b3802820f8302cda11c0bdb174621df906c35407`
- `vpsfree-cz-configuration`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsfree-cz-configuration`
  - base: `d6f1c5d1`
  - head: `8818f1f98ce6c76cd1b0b00ca7af23daac436ab5`

## Status

- The approved redesign is implemented and committed in vpsAdmin,
  vpsfree-cz-configuration, and vpsadmin-kb-captures.
- The proposed vpsAdminOS livepatch completion service and reporter changes
  were removed. Its branch now points directly to the existing `008aa460`
  livepatch release and has no feature diff.
- All four rewritten feature branches are pushed to their SSH origins.
- Quick checks, mandatory fresh-context review, long local integration testing,
  application-host builds, and the development-cluster refresh pass. All
  final-head GitHub workflows except the still-running aggregate integration
  workflow have completed successfully.
- No production deployment or production KB write is authorized.

## Final commits

- `vpsadmin`
  - `b703e5948` — `api: record observed livepatch lifecycle`
  - `cb0c05c39` — `webui: label effective livepatch lifecycle`
  - `582e1ebc9` — `webui: simplify inferred version timestamps`
  - `91b574aef` — `tests: cover compact history tooltip in browser`
- `vpsfree-cz-configuration`
  - `eeefda7f` — generated production vpsAdminOS pin to `008aa460`
  - `6d4a6664` — generated vpsAdmin role pins to `91b574ae`
  - `8818f1f9` — observed-livepatch deployment runbook
- `vpsadmin-kb-captures`
  - `b380282` — final vpsAdmin documentation-contract pin
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
- The migration reclassifies an all-false availability row only when its
  immediate public predecessor has trustworthy evidence with no loaded,
  enabled, transitioning, or marked patch. It converts only exact old
  marker/event matches to inferred applications, repairs current markers, and
  leaves unload-shaped or otherwise ambiguous history generic.
- The private event API applies `livepatch_action` filters before time-window
  and baseline selection for both applied and removed values.
- WebUI and API expose only `applied`, `removed`, and the null/generic fallback.
- Bounded inferred timestamps visibly show the lower bound and retain the full
  interval in mouse-hover and keyboard-focus detail across version tables. The
  Czech catalog contains complete, non-fuzzy translations for these strings.
- Configuration keeps all vpsAdminOS channels at `008aa460` and points all
  vpsAdmin roles at `91b574ae` using generated `confctl --commit` updates.
- The runbook removes the coordinated reporter rollout and exact-timestamp
  claims, and documents the one-way migration and supervisor quiescence.
- The KB contract found no owned administrator Node-history screenshots, so no
  PNG regeneration or production KB candidate is required.

## Quick verification

- vpsAdmin API recorder/resource specs: 42 examples, 0 failures.
- vpsAdmin migration specs: 6 examples, 0 failures. They must run separately
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
- `./test-runner.sh test 'webui#admin-cluster'` passed on the final head. The
  Playwright example succeeded in 360.22 seconds and the complete scenario in
  689.61 seconds.
- Final configuration builds passed separately for
  `cz.vpsfree/vpsadmin/int.api1`, `int.api2`, `int.webui1`, and `int.webui2`.

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
  `31184331945`, and `31184769710` were cancelled after their heads were
  replaced. On final head `91b574aef`, migration specs, RuboCop, i18n health,
  libnodectld specs, WebUI PHPUnit, and the topic-parallel API specs have
  passed. Aggregate integration run `31186815892` is still running its selected
  tests; its live log is unavailable until the job completes. The selector
  intentionally chose the full `tag=ci` suite because the final force-push
  changed a database migration relative to the preceding remote head. Recent
  successful full runs take approximately 4.5--6 hours, so its current runtime
  is expected.
- The vpsAdminOS branch was force-updated from the discarded feature commit to
  existing revision `008aa460`; no new vpsAdminOS commit requires validation.

## Development cluster

- The single-node bridge-network cluster
  `2026-08-06-node-kernel-history` is running the reviewed vpsAdmin revision
  `91b574aef` and vpsAdminOS revision `008aa460`.
- WebUI: `https://webui.aitherdev.int.vpsfree.cz/`
- Kernel history page:
  `https://webui.aitherdev.int.vpsfree.cz/?page=node&action=kernel_history&id=101`
- Software versions page:
  `https://webui.aitherdev.int.vpsfree.cz/?page=node&action=software_versions&id=101`
- The rendered kernel table was verified with inferred applied and removed
  examples. It displays only the lower observation bound and exposes the full
  interval in the accessible tooltip.
- The rendered software-version table was verified with booted and current
  revision links for vpsAdminOS `008aa4605ec2`, vpsAdmin `91b574aefc49`, and
  nixpkgs `04607e1165ac`; no revision is shown as unavailable.
- The task-local launcher passes clean worktree HEAD and dirty-state metadata
  into the existing vpsAdmin and vpsAdminOS version options. This compensates
  only for Nix `path:` inputs dropping flake revision metadata and is unrelated
  to the removed livepatch service design. `bash -n` and `nixfmt --check`
  passed for the local launcher changes.
- An in-guest node reboot exposed that the retained older launcher does not
  respawn a QEMU VM started with `--no-reboot`. The whole runner was restarted
  without resetting persistent state, then node pool/nodectld refresh passed.
  The first automatic refresh raced `osctld` socket creation; retrying after
  `osctld` became ready succeeded.
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

- The standalone fresh-context review found one Blocking issue: the original
  migration could irreversibly classify an all-false unload report as internal
  inventory. It also found one Important issue: the declared
  `livepatch_action` API filter was not applied.
- The migration now requires trustworthy inactive predecessor evidence and has
  positive availability and negative same-release unload regressions. The
  resource scope now applies the action filter before window/baseline selection
  and tests both action values. The runbook describes the conservative rule.
- Both corrections were folded into the owning API commit and downstream pins
  were rebuilt with one clean update per input stream.
- The same reviewer inspected final heads `91b574aef`, `8818f1f9`, and
  `b380282` and confirmed that both findings are resolved, no new regression is
  apparent, the runbook is accurate, and the commit split remains clean. There
  are no Blocking, Important, or Advisory findings. The long-test gate is open.

## Cleanup

- Feature worktrees and the review cluster remain intentionally available.
- Temporary build output was written only below `/tmp`.
- Top-level shared-workspace changes unrelated to this initiative were
  preserved and not staged.
