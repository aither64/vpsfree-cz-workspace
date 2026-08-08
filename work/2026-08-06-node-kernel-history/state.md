# 2026-08-06-node-kernel-history

## Repositories

- `vpsadminos`
  - branch: `2026-08-06-node-kernel-history`
  - worktree removed after merge completion; former path:
    `worktrees/2026-08-06-node-kernel-history/vpsadminos`
  - base for the two-stage cluster test: patch-2 revision
    `008aa4605ec263397bf46bd9fe915a01be1670a6`
  - head: patch-3 revision
    `8d5fe0058f5f4db3840c7d8043c7aba3b88ccca4`
  - no initiative-specific feature diff; the branch was fast-forwarded to the
    existing reviewed patch-3 revision after testing the patch-2 state
- `vpsadmin`
  - branch: `2026-08-06-node-kernel-history`
  - worktree removed after merge; former path:
    `worktrees/2026-08-06-node-kernel-history/vpsadmin`
  - base: `1657a32126a24a1a06f4e1fea3e9bdf3e40b335d`
  - head: `c0d87bebf36c6d29b7861990890e8c650fa1afca`
- `security-advisories`
  - branch: `2026-08-06-node-kernel-history`
  - worktree removed after merge; former path:
    `worktrees/2026-08-06-node-kernel-history/security-advisories`
  - base: `5d4138ae01322904ae30cabfbe0c62dfa8eac344`
  - head: `7cb4fb19253c853f720520dee37698c71def2189`
- `vpsadmin-kb-captures`
  - branch: `2026-08-06-node-kernel-history`
  - worktree removed after merge; former path:
    `worktrees/2026-08-06-node-kernel-history/vpsadmin-kb-captures`
  - base: `7248a8b`
  - head: `3d394b377db1e57375bd1af0f8d19f9b72a1a8b3`
- `vpsfree-cz-configuration`
  - branch: `2026-08-06-node-kernel-history`
  - worktree removed after merge; former path:
    `worktrees/2026-08-06-node-kernel-history/vpsfree-cz-configuration`
  - base: `338db498743c8e04fd6d9ed3d2a0f33f7bbc5ba5`
  - head: `2051708717b170afd34820817945bf858f93bb19`

## Status

- The migration readability and node-rollback follow-up is implemented and
  folded into the original undeployed vpsAdmin and security-advisories commits.
  Configuration retains patch 3 and pins the rewritten vpsAdmin head; the KB
  contract pin is refreshed.
- The proposed vpsAdminOS livepatch completion service and reporter changes
  were removed. Its branch now points directly to existing patch-3 revision
  `8d5fe005` and has no initiative-specific feature diff.
- vpsAdmin, security-advisories, configuration, and the KB contract were
  fast-forwarded into their GitHub-confirmed default branches on 2026-08-08.
  Exact configuration pins, strict runbook documentation, browser integration,
  and the bridge-network development-cluster scenario pass.
- The fresh mandatory review confirmed the migration and rollback semantics.
  Its one Blocking finding, a stale vpsAdmin revision in the rollout runbook,
  was corrected and verified by the same reviewer; no Blocking or Important
  findings remain.
- Final feature-head security-advisories and all vpsAdmin workflows pass,
  including aggregate integration workflow `31218686721`.
- No production deployment or production KB write is authorized.

## Final commits

- `vpsadmin`
  - `988ce4a0d` — `api: record observed livepatch lifecycle`
  - `0945bd749` — `nodectld: report observed livepatch modules`
  - `c6bd3796c` — `webui: label effective livepatch lifecycle`
  - `97db3a06f` — `webui: simplify inferred version timestamps`
  - `c0d87bebf` — `tests: cover compact history tooltip in browser`
- `security-advisories`
  - `7cb4fb1` — `security: evaluate observed livepatch state`
- `vpsfree-cz-configuration`
  - `af7962dae` — loaded-livepatch deployment runbook
  - `20517087` — generated vpsAdmin role pins to `c0d87beb`
- `vpsadmin-kb-captures`
  - `3d394b3` — final vpsAdmin documentation-contract pin
- `vpsadminos`
  - no initiative-specific feature commit; branch and current channel revision
    are `8d5fe005`

## Default branch integration

- `vpsadmin` `master` was fast-forwarded from `1657a321` to `c0d87beb`.
- `security-advisories` uses
  `2026-07-13-security-advisory-automation` as its GitHub default branch; it was
  fast-forwarded from `5d4138ae` to `7cb4fb1`.
- `vpsfree-cz-configuration` `master` was fast-forwarded from `338db498` to
  `20517087`, after vpsAdmin `master` made the pinned revision reachable.
- `vpsadmin-kb-captures` `master` was fast-forwarded from `7248a8b` to
  `3d394b3`, after vpsAdmin `master` made the contract pin reachable.
- The KB bare clone's cached `origin/HEAD` still named the old
  `2026-07-10-kb-czech-fixes` default. GitHub's REST API identified `master` as
  current; the cached symbolic ref was refreshed before integration. The
  reusable lesson is in
  `notes/vpsadmin-kb-captures/2026-08-08-stale-origin-head.md`.
- Fresh detached target worktrees were used for all four fast-forward merges.
  Target-tree verification passed: vpsAdmin migration 6 examples,
  security-advisories 123 examples plus RuboCop, four vpsAdmin service builds,
  and the complete KB contract/inventory check.
- Feature branches remain locally and on origin at their final heads. All
  temporary target and feature worktrees were removed after the pushes.
- vpsAdminOS had no initiative-specific change and therefore required no
  default-branch merge.

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
- Quick verification before the migration readability follow-up:
  - libnodectld security-evidence spec: 10 examples, 0 failures;
  - API recorder spec: 26 examples, 0 failures;
  - corrective migration spec: 5 examples, 0 failures;
  - security-advisories RSpec: 122 examples, 0 failures;
  - security-advisories RuboCop: 28 files, no offenses;
  - vpsAdmin and security-advisories pre-commit hooks passed.

## Migration readability and rollback follow-up

- Replaced the corrective migration's deeply nested predecessor query with
  three named data-loading stages and small predicates. Its comment now states
  the old-reporter defect, the exact recognition rules, and why empty evidence
  and same-ID inactive evidence are preserved as possible removals.
- The migration orders events only by `observed_before` and event ID. It never
  compares kernel releases or Git revisions for recency, and it does not update
  `node_software_versions`.
- A MariaDB migration regression covers a stable patch application, an inactive
  next-patch availability row, and then a later reboot into the unpatched base
  kernel with an older software revision. The later boot remains the sole
  current public event; the older revision rows are byte-for-byte unchanged.
- The existing same-ID possible-removal regression also uses descending
  software revisions and verifies they remain unchanged.
- A security-advisories evaluator regression covers the same semantic rollback:
  after accepted livepatch mitigation, a later unpatched boot with an older
  vpsAdminOS revision evaluates as vulnerable and has no `mitigated_since`.
- Focused verification after the refactor:
  - vpsAdmin corrective migration: 6 examples, 0 failures;
  - security-advisories evaluator: 49 examples, 0 failures;
  - vpsAdmin and security-advisories RuboCop passed for changed files;
  - both repository pre-commit hooks passed;
  - KB contract check passed: 39 controls, 29 paths, 32 capture concepts,
    65 bindings, 9 exceptions, 15 tests, and 118 PNG variants;
  - exact configuration pins resolve all three vpsAdmin roles to `c0d87beb`.
- vpsAdmin, security-advisories, configuration, and KB branches were
  force-pushed with leases after folding/regenerating their undeployed commits.
- The paused `2026-08-07-security-advisories-6-12-95-2` initiative remains
  untouched. With this work now merged, it can be resumed and rebased in its
  own development session.

## Verification

- vpsAdmin libnodectld security-evidence specs: 10 examples, 0 failures.
- vpsAdmin API recorder/parser specs: 26 examples, 0 failures.
- vpsAdmin corrective migration specs: 6 examples, 0 failures.
- vpsAdmin commit hooks passed Nixfmt, migration specs, RuboCop, WebUI i18n,
  and API i18n checks.
- security-advisories RSpec: 123 examples, 0 failures.
- security-advisories RuboCop: 28 files, no offenses; its commit hook passed.
- Configuration exact-pin assertions passed: all three vpsAdmin roles use
  `c0d87beb`; all three relevant vpsAdminOS roles use `8d5fe005`.
- `nix shell nixpkgs#mkdocs -c mkdocs build --strict` passed for the rollout
  runbook.
- KB `nix develop -c bin/check` passed: 39 controls, 29 paths, 32 capture
  concepts, 65 bindings, 9 exceptions, 15 tests, and 118 PNG variants.
- vpsAdmin browser integration `./test-runner.sh test
  'webui#admin-cluster'` passed. The Playwright example completed in 380.24
  seconds and the full test completed in 992.2 seconds. This was before the
  migration-only history rewrite; the browser-affecting tree is unchanged and
  final-head WebUI PHPUnit passes in CI.
- Final configuration builds passed for `int.api1`, `int.api2`, `int.webui1`,
  and `int.webui2`. Earlier evaluation of `node1.stg` stopped before
  compilation because this local machine does not have the deployment-only
  `/secrets/nodes/initrd/ssh_host_ed25519_key`; `node2.stg` was not attempted
  after the serial command stopped. No substitute secret was created.
- vpsAdminOS has no initiative-specific feature diff; its existing
  release-certification test `tests/suite/kernel/livepatch-6.12.95.nix`
  remains unchanged by this initiative.

## GitHub Actions

- vpsAdmin head `c0d87beb`: migration specs, RuboCop, i18n health,
  libnodectld specs, WebUI PHPUnit, and topic-parallel API workflow
  `31218686499` passed. Aggregate CI workflow `31218686721` also passed the
  full `tag=ci` integration suite selected because the branch changes a
  migration.
- security-advisories head `7cb4fb1`: RSpec and RuboCop passed.
- After the default-branch pushes, security-advisories RSpec and RuboCop passed
  again. vpsAdmin migration specs, RuboCop, i18n, libnodectld, and WebUI
  PHPUnit passed again; the redundant exact-head topic-parallel and aggregate
  workflows remain in progress. The same commit already passed both full
  feature-branch workflows before integration.
- vpsAdminOS head `8d5fe005`: RSpec passed and exact-head full CI workflow
  `31198648330` passed. Later branch workflow `31210461594` had 71 successful
  tests and four unrelated QEMUs terminated by runner memory pressure. Its
  downloaded artifacts show synchronized `qemu_exit` records with empty status,
  abrupt guest consoles without panic, and OSVM shell EOFs; this matches the
  documented 92-GiB scheduling-on-96-GiB swapless-runner failure.
- Configuration and KB repositories have no workflows for this branch push.
- Superseded vpsAdmin aggregate runs `31186815892`, `31204583570`, and
  `31207316731` were cancelled after force-pushes; completed old-head runs are
  retained.
- Failed attempts from 2026-08-06 were inspected before rerunning and were
  attributed to the GitHub service outage and associated self-hosted-runner
  availability, not accepted merely because a later run became green.

## Development cluster

- The bridge-network cluster `2026-08-06-node-kernel-history` completed its
  review purpose with vpsAdmin services at clean revision `c0d87beb`; schema
  migrations `20260806120000` and `20260806120100` were applied.
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
  render those vpsAdmin/vpsAdminOS revisions as unavailable. The node system
  intentionally remains at the pre-rewrite reporter closure; only services
  needed refresh because the folded follow-up changed migration/spec code, not
  reporter behavior.
- The cluster was stopped after the default-branch merges. Its runner did not
  exit on TERM within the launcher's built-in 120-second window, so the launcher
  used its documented forced-stop path. The cluster is stopped and its
  persistent task state was not reset.
- The task-local `dev-clusters/vpsadmin-node-kernel-history/` launcher was moved
  to trash after shutdown; the shared launcher's unrelated concurrent changes
  remain untouched.

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
- A new fresh-context review of the migration readability and rollback
  follow-up found no semantic, architectural, security, or commit-split issue.
  It found one Blocking operational mismatch: the runbook still named the
  superseded `89f93ece` revision while generated pins used `c0d87beb`.
- Both runbook constants now use `c0d87beb`; strict MkDocs, exact-pin
  assertions, configuration hooks, and a same-reviewer follow-up pass. No
  Blocking or Important findings remain. The only Advisory was to refresh this
  state file's pre-rewrite hashes, which this update resolves.

## Cleanup

- The review cluster is stopped. All initiative feature worktrees and fresh
  default-branch integration worktrees were removed. Feature branch refs were
  retained locally and remotely as required.
- Generated MkDocs output, downloaded CI diagnostics, configuration hook/gem
  caches, build logs, and the task-local cluster launcher were moved to trash.
  Tracked content remains recoverable from the retained commits and branches.
- Top-level shared-workspace changes unrelated to this initiative were
  preserved and not staged.
