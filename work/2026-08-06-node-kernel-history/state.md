# 2026-08-06-node-kernel-history

## Repositories

- `vpsadminos`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadminos`
  - base for the two-stage cluster test: patch-2 revision
    `008aa4605ec263397bf46bd9fe915a01be1670a6`
  - head: patch-3 revision
    `8d5fe0058f5f4db3840c7d8043c7aba3b88ccca4`
  - no initiative-specific feature diff; the branch was fast-forwarded to the
    existing reviewed patch-3 revision after testing the patch-2 state
- `vpsadmin`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin`
  - base: `1657a32126a24a1a06f4e1fea3e9bdf3e40b335d`
  - head: `89f93ece94c8881706df37605cf3ed97bce55391`
- `security-advisories`
  - branch: `2026-08-06-node-kernel-history`
  - worktree:
    `worktrees/2026-08-06-node-kernel-history/security-advisories`
  - base: `5d4138ae01322904ae30cabfbe0c62dfa8eac344`
  - head: `9cd57ccfa25c21dcd9ff5ef67dc0b68735aa5222`
- `vpsadmin-kb-captures`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin-kb-captures`
  - base: `7248a8b`
  - head: `63c3618964576b2bf05f15ec2a27e89d1a600de8`
- `vpsfree-cz-configuration`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsfree-cz-configuration`
  - base: `338db498743c8e04fd6d9ed3d2a0f33f7bbc5ba5`
  - head: `380f756705b63f42dbeb2047a8df9a62af228017`

## Status

- The staging follow-up is implemented and committed in vpsAdmin and
  security-advisories. Configuration retains patch 3 and pins the rewritten
  vpsAdmin head; the KB contract pin is refreshed.
- The proposed vpsAdminOS livepatch completion service and reporter changes
  were removed. Its branch now points directly to existing patch-3 revision
  `8d5fe005` and has no initiative-specific feature diff.
- All repository branches are pushed. Exact configuration pins, strict runbook
  documentation, the KB contract, browser integration, and the bridge-network
  development-cluster scenario pass.
- The mandatory reviewer verified all four blocker fixes. No Blocking,
  Important, or Advisory findings remain, and the long-test gate is open.
- Final-head focused GitHub workflows pass. The vpsAdmin and vpsAdminOS
  aggregate integration workflows are still running.
- No production deployment or production KB write is authorized.

## Final commits

- `vpsadmin`
  - `197cbe351` — `api: record observed livepatch lifecycle`
  - `5456c7bfb` — `nodectld: report observed livepatch modules`
  - `03def1f37` — `webui: label effective livepatch lifecycle`
  - `b411950e6` — `webui: simplify inferred version timestamps`
  - `89f93ece9` — `tests: cover compact history tooltip in browser`
- `security-advisories`
  - `9cd57cc` — `security: evaluate observed livepatch state`
- `vpsfree-cz-configuration`
  - `17b4cd5e` — loaded-livepatch deployment runbook
  - `380f7567` — generated vpsAdmin role pins to `89f93ece`
- `vpsadmin-kb-captures`
  - `63c3618` — final vpsAdmin documentation-contract pin
- `vpsadminos`
  - no initiative-specific feature commit; branch and current channel revision
    are `8d5fe005`

## Staging patch-2/patch-3 follow-up

- Captured staging evidence showed patch 2 still active and reporting
  `6.12.95.2`, while the old reporter exposed only deployed, unavailable patch
  3 from the current system closure.
- libnodectld now enumerates `/sys/kernel/livepatch` and enriches loaded modules
  from both booted and current closure monitors. Patch 3 is omitted until it is
  loaded.
- Loaded modules without closure metadata remain valid nullable inventory.
  Unreadable enumeration, enabled, or transition state is recorded as an
  evidence gap and cannot create an applied or removed event.
- The recorder treats the old different-ID/same-release report as internal
  inventory, so API-first rolling deployment does not create a false removal.
- The undeployed migration no longer uses `verified_at` or repeated-run guards.
  It directly handles the master-produced inactive successor row and preserves
  same-ID removal candidates.
- security-advisories normalized evidence schema is 8, event attestations bind
  `livepatch_action`, accepted patches require exact kernel/vpsAdminOS identity,
  and livepatch mitigation timing uses the observation interval. An exact clean
  booted/current vpsAdminOS revision is required even when Linux source matches.
- The paused
  `worktrees/2026-08-07-security-advisories-6-12-95-2/security-advisories`
  worktree was read only and remains untouched for a later rebase.
- Quick verification:
  - libnodectld security-evidence spec: 10 examples, 0 failures;
  - API recorder spec: 26 examples, 0 failures;
  - corrective migration spec: 5 examples, 0 failures;
  - security-advisories RSpec: 122 examples, 0 failures;
  - security-advisories RuboCop: 28 files, no offenses;
  - vpsAdmin and security-advisories pre-commit hooks passed.

## Current verification

- vpsAdmin libnodectld security-evidence specs: 10 examples, 0 failures.
- vpsAdmin API recorder/parser specs: 26 examples, 0 failures.
- vpsAdmin corrective migration specs: 5 examples, 0 failures.
- vpsAdmin commit hooks passed Nixfmt, migration specs, RuboCop, WebUI i18n,
  and API i18n checks.
- security-advisories RSpec: 122 examples, 0 failures.
- security-advisories RuboCop: 28 files, no offenses; its commit hook passed.
- Configuration exact-pin assertions passed: all three vpsAdmin roles use
  `89f93ece`; all three relevant vpsAdminOS roles use `8d5fe005`.
- `nix shell nixpkgs#mkdocs -c mkdocs build --strict` passed for the rollout
  runbook.
- KB `nix develop -c bin/check` passed: 39 controls, 29 paths, 32 capture
  concepts, 65 bindings, 9 exceptions, 15 tests, and 118 PNG variants.
- vpsAdmin browser integration `./test-runner.sh test
  'webui#admin-cluster'` passed. The Playwright example completed in 380.24
  seconds and the full test completed in 992.2 seconds.
- Configuration builds passed for `int.api1`, `int.api2`, `int.webui1`, and
  `int.webui2`. Evaluation of `node1.stg` stopped before compilation because
  this local machine does not have the deployment-only
  `/secrets/nodes/initrd/ssh_host_ed25519_key`; `node2.stg` was not attempted
  after the serial command stopped. No substitute secret was created.
- vpsAdminOS has no initiative-specific feature diff; its existing
  release-certification test `tests/suite/kernel/livepatch-6.12.95.nix`
  remains unchanged by this initiative.

## GitHub Actions

- vpsAdmin head `89f93ece`: migration specs, RuboCop, i18n health,
  libnodectld specs, WebUI PHPUnit, and topic-parallel API specs passed. The
  aggregate CI workflow `31207316731` is still running its selected integration
  tests.
- security-advisories head `9cd57cc`: RSpec and RuboCop passed.
- vpsAdminOS head `8d5fe005`: RSpec and the aggregate build job passed. The
  branch-specific aggregate CI workflow `31210461594` is still running its test
  suite. The same exact commit already passed full staging CI in workflow
  `31198648330`.
- Configuration and KB repositories have no workflows for this branch push.
- Superseded vpsAdmin aggregate runs `31186815892` and `31204583570` were
  cancelled after force-pushes; completed old-head runs are retained.
- Failed attempts from 2026-08-06 were inspected before rerunning and were
  attributed to the GitHub service outage and associated self-hosted-runner
  availability, not accepted merely because a later run became green.

## Development cluster

- The bridge-network cluster `2026-08-06-node-kernel-history` is running and
  ready. vpsAdmin services use final revision `89f93ece`; schema migrations
  `20260806120000` and `20260806120100` are applied.
- The cluster reproduced the staging transition without rebooting: the booted
  system remains vpsAdminOS `008aa460` with patch-2 metadata, while the current
  system is `8d5fe005` with patch-3 metadata. Kernel sysfs contains only
  `livepatch_2`, with `enabled=1` and `transition=0`.
- The current API snapshot contains only `livepatch_2` version 2 for kernel
  6.12.95. It contains no patch-3 row. Switching the current system created
  only an internal deployment-change event and no false applied or removed
  livepatch event.
- Current software evidence has concrete booted/current revisions for
  vpsAdminOS (`008aa460` / `8d5fe005`), vpsAdmin (`91b574ae` / `89f93ece`),
  and nixpkgs (`04607e11` / `445d861c`); the WebUI therefore has no reason to
  render those vpsAdmin/vpsAdminOS revisions as unavailable.
- The cluster is intentionally left running in this staging-like state at
  `https://webui.aitherdev.int.vpsfree.cz/`. Kernel history is at
  `?page=node&action=kernel_history&id=101` and software versions at
  `?page=node&action=software_versions&id=101`.
- The task-local launcher remains at
  `dev-clusters/vpsadmin-node-kernel-history/` because the shared launcher has
  unrelated concurrent changes.

## Compatibility and rollback

- Mixed node reporter versions are supported without a protocol bump.
- No coordinated vpsAdminOS rollout or reboot is required for history.
- The nullable action and appended internal event preserve old public enum and
  wire values.
- The data correction is one-way. If API rollback is unavoidable after it,
  old supervisors remain paused until the new recorder returns or an explicit
  semantic-regression plan is approved.

## Mandatory review

- The fresh-context review found four Blocking issues: nullable unmatched
  reporter metadata was rejected by the API; matching Linux source bypassed
  the reviewed vpsAdminOS revision; sysfs read gaps could appear as lifecycle
  transitions; and API/reporter rollout stages shared one commit.
- The API now accepts nullable livepatch metadata/state, records unknown
  metadata fail-closed, and suppresses lifecycle classification for incomplete
  livepatch observations. Reporter, parser, and recorder regressions cover
  metadata absence plus enumeration and flag-read failures.
- security-advisories now always requires the exact clean reviewed vpsAdminOS
  revision and separately verifies Linux source when available.
- The commit series is split into API/migration, reporter, WebUI labels,
  compact timestamps, and browser coverage. The runbook now verifies the
  supervisor runtime mask again after switching api1.
- The same reviewer verified the fixes and regenerated pins. No Blocking,
  Important, or Advisory findings remain, and the long-test gate is open. This
  is not merge or deployment approval.

## Cleanup

- Feature worktrees and the review cluster remain intentionally available.
- Generated MkDocs `site/` output was removed after validation. Configuration
  keeps untracked `.bin/` and `.bundle/` only for its installed hook/tooling
  environment.
- Top-level shared-workspace changes unrelated to this initiative were
  preserved and not staged.
