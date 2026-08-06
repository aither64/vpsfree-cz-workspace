# 2026-08-06-node-kernel-history

## Repositories

- `vpsadminos`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadminos`
  - base: `origin/staging` at `008aa4605ec263397bf46bd9fe915a01be1670a6`
- `vpsadmin`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin`
  - base: `origin/master` at `92bba722b16d8f1e68e183f7041be1d44a17db7d`
- `vpsadmin-kb-captures`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsadmin-kb-captures`
  - base: `origin/master` at `7248a8b`
- `vpsfree-cz-configuration`
  - branch: `2026-08-06-node-kernel-history`
  - worktree: `worktrees/2026-08-06-node-kernel-history/vpsfree-cz-configuration`
  - base: `origin/master` at `d6f1c5d1`

## Status

- All intended changes are committed in four clean feature worktrees.
- All four feature branches are pushed to their SSH origins.
- Quick repository verification and the full WebUI browser integration test
  have passed. The mandatory fresh-context review is complete with no blocking
  or important findings. Both final advisory findings have been addressed.
- The single-node bridge-network development cluster
  `2026-08-06-node-kernel-history` is running and reports `ready: yes`.
- No production deployment or production KB write is authorized.

## Development cluster

- WebUI: `https://webui.aitherdev.int.vpsfree.cz/`
- Kernel history demonstration:
  `https://webui.aitherdev.int.vpsfree.cz/?page=node&action=kernel_history&id=101`
- API and WebUI both returned HTTP 200 after startup. The kernel-history API
  returned the real current boot event plus two dev-only demonstration rows:
  exact `applied` and inferred `removed`. The latter has distinct
  `observed_after` and `observed_before` values so the compact visible time and
  its hover/focus detail can be reviewed.
- The shared dev-cluster definition currently contains notification options
  from another unmerged vpsAdmin initiative, while this worktree is correctly
  based on `origin/master`. A task-local launcher snapshot from coordination
  commit `c1d70e281619b6a51c5d8f285bff2786f6c04cf9`, immediately before that
  notification integration, is retained at
  `dev-clusters/vpsadmin-node-kernel-history/` for cluster lifecycle commands.
  The shared tracked launcher and its unrelated working-tree changes were not
  modified.
- The cluster-specific config disables optional Mailpit capture and the fake
  SMS gateway. These services are unrelated to kernel history and their newer
  option definitions are absent from the vpsAdmin master base.
- Initial node activation encountered the documented late-osctld readiness
  race after the cluster had already reached `ready: yes`. Once `osctld` and
  `nodectld` were running, `devcluster update ... node1` completed cleanly.

## Commits

- `vpsadminos`
  - `a9baea19c0459538ac6191f426b80f3bdd64bfb6` —
    `livepatch: record verified application completion`
- `vpsadmin`
  - `ce6e984f2` — `nodectld: report verified livepatch completion`
  - `46de0b719` — `api: record effective livepatch lifecycle`
  - `e552642db` — `webui: label livepatch lifecycle events`
  - `8e9f8b230` — `webui: simplify inferred version timestamps`
  - `2726f6bd5` — `flake: vpsadminos 31b3dff43 -> a9baea19c`
  - `9529a92fe` — `tests: cover compact history tooltip in browser`
- `vpsfree-cz-configuration`
  - `970ea694` — generated os-staging vpsAdminOS pin
  - `93a72081` — generated staging/production vpsAdminOS pins
  - `5816cba3` — generated vpsAdmin service/staging/production pins
  - `97efd0ac` — `vpsadmin-config: document livepatch history rollout`
- `vpsadmin-kb-captures`
  - `bd4c589` — `contract: pin livepatch history presentation`

## Commands run

- Verified the active development session with `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Inspected top-level status and preserved unrelated shared-workspace changes.
- Fetched the four affected canonical bare repositories.
- Created per-initiative branches and worktrees with `bin/dev-session add`.
- Read the top-level and all affected repository `AGENTS.md` files, the
  mandatory change review skill, and the canonical WebUI/KB workflow.
- Inspected the live-patch loader, node evidence reporter, kernel event model,
  recorder, API projections, migrations, WebUI history pages, and tests.
- Installed and ran the declared Overcommit hooks in the vpsAdminOS, vpsAdmin,
  and configuration worktrees from their Nix development environments.
- Updated the vpsAdminOS flake input in vpsAdmin with the repository helper.
- Updated all configuration channel pins with `confctl inputs channel set
  --commit`; generated commit messages were left unchanged.
- Pinned the exact pushed vpsAdmin revision in the capture repository and ran
  `nix flake update vpsadmin` followed by `nix develop -c bin/check`.
- Ran the mandatory standalone review, rewrote the affected commit series after
  addressing its findings, force-pushed with leases, and cancelled the only
  still-running GitHub Actions run for a superseded head.

## Results

- Confirmed that existing `applied_at` is written immediately after enablement,
  before the kernel transition is known to have completed.
- Confirmed that the reporter/API already accept and persist optional
  `verified_at`; no node-evidence protocol version bump is required.
- Confirmed that public live-patch events currently compare complete inventory
  arrays, causing availability-only changes to appear in kernel history.
- Confirmed interval semantics: `observed_after` is the last old observation and
  `observed_before` is the first new observation, so the interval is
  `(observed_after, observed_before]`.
- The ambient post-checkout hook for `vpsfree-cz-configuration` reported missing
  Overcommit gems and exited 78 after the clean worktree was created. Installing
  and running hooks inside `nix develop` resolved it. A first push outside the
  Nix shell was similarly rejected; the push inside the shell succeeded.
- vpsAdminOS quick evaluation passed:
  `nix eval .#checks.x86_64-linux.os-eval.drvPath --raw`.
- vpsAdminOS Overcommit passed Nixfmt and RuboCop.
- vpsAdminOS loader failure-path coverage now includes verified-marker write
  failure and a stuck transition timeout, both with marker/module cleanup.
- vpsAdmin reporter specs passed: 8 examples, 0 failures.
- vpsAdmin API resource and recorder specs passed separately from migration
  specs: 39 examples, 0 failures. Migration specs passed: 5 examples,
  0 failures. They are intentionally separate because the migration helper
  switches to its minimal test schema.
- vpsAdmin WebUI localization generation/checks passed. The focused PHPUnit
  regression suite passed: 13 tests, 74 assertions.
- The final Playwright addition passes JavaScript syntax validation and the CI
  selection suite (16 tests, 55 assertions). It exercises the rendered compact
  interval's hidden, mouse-hover, mouse-away, and keyboard-focus states in the
  existing admin-cluster browser test; execution of that VM test awaits the
  mandatory long-test gate.
- All vpsAdmin commits passed Overcommit, including Nixfmt, migration specs,
  WebUI gettext validation, PHP CS Fixer where applicable, RuboCop, and API
  i18n validation.
- On the amended vpsAdmin head, the dedicated migration, WebUI, libnodectld,
  client, i18n, and RuboCop workflows passed. Aggregate CI run `31115552639`
  failed before checkout while the self-hosted runner tried to resolve action
  downloads: GitHub returned Bad Gateway, then Service Unavailable twice. No
  repository code or tests ran; a rerun is deferred until the long-test review
  gate opens.
- Final-head vpsAdmin CI run `31118349379` selected the intended
  `webui#admin-cluster` test, but GitHub cancelled it after no self-hosted runner
  acquired the job despite multiple attempts. The job has no runner, steps, or
  test logs, so it is infrastructure feedback rather than a test result.
- The selected local `./test-runner.sh test 'webui#admin-cluster'` integration
  test passed: its Playwright example succeeded in 428.75 seconds and the full
  test completed successfully in 1072.14 seconds. This executed the compact
  interval's hidden, hover, mouse-away, keyboard-focus, overflow, and greater
  than `0.99` intersection-ratio assertions in the real WebUI VM environment.
- vpsAdminOS CI run `31114615370` built the complete OS successfully, but its
  test-suite job was externally cancelled while tests were still running. The
  downloaded artifact showed four unexpected results, all caused at the exact
  cancellation second by closed QEMU/VM streams; 59 tests had succeeded and the
  run was incomplete. After inspecting the job log and all four affected test
  logs, workflow attempt 2 was started. GitHub then cancelled its build job
  before it produced any step log, so the test job was skipped and the rerun
  supplied no additional repository feedback.
- The gated `kernel-livepatch-6.12.95` VM examples could not be evaluated
  because two exact external fixture modules are unavailable on this host. The
  corrected module rebuilt with the required `88e7aede...` hash, but the
  released-v1 and predecessor derivations produced `5dfb6bda...` and
  `154cd274...` instead of required `a3f79b22...` and `70f22f6f...`. The
  released-v1 derivation is identical at the pre-feature and feature commits,
  while its signed historical cache artifact has a third hash,
  `0d7c7722...`; this confirms that derivation identity does not reproduce the
  pinned kpatch artifact. The test's hash guards were not changed or bypassed.
  The durable fixture workflow is recorded in
  `notes/vpsadminos/2026-08-06-livepatch-fixture-artifacts.md`.
- Plain `bundle exec rake db:migrate` in the development checkout had no
  configured database connection. The committed schema matches the migration,
  and isolated migration specs validate both migrations against MariaDB.
- Configuration exact-pin assertions passed for all six channel inputs.
- Full configuration builds passed for `int.api1`, `int.api2`, `int.webui1`,
  and `int.webui2`, resolving vpsAdmin `9529a92f` and vpsAdminOS `a9baea19`.
  The `stg/node1` build then reached the final vpsAdminOS closure but could not
  evaluate its initrd because this workstation has no
  `/secrets/nodes/initrd/ssh_host_ed25519_key`. The repository provides no
  documented dummy-secret override; `stg/node2` uses the same common netboot
  module, so it was not redundantly attempted. No host key was synthesized or
  copied into the operator secret path.
- The configuration development shell does not contain MkDocs. Running
  `nix shell nixpkgs#python3Packages.mkdocs -c mkdocs build --strict` passed.
- Capture contract verification passed: 39 controls, 29 paths, 32 capture
  concepts, 65 KB bindings, 9 exceptions, 15 contract tests, and all 118 PNG
  variants. No owned screenshot concept covers the changed administrator-only
  Node history tables, so no PNG regeneration is required.
- The configuration runbook records supervisor quiescence around the one-way
  migration, exact pin checks, rolling-node compatibility, verification, and
  rollback limitations. Committing these pins did not deploy any machine.

## Mandatory review

The first standalone review found these blocking issues:

- the data migration could promote later verified metadata snapshots to
  duplicate applied events;
- removal inference used a transient transition observation instead of the
  latest stable effective-state observation;
- the livepatch loader could wait indefinitely and did not treat marker-write
  failures as load failures;
- reporter/API and lifecycle/timestamp WebUI changes were combined too broadly;
- keyboard focus exposed only native title/ARIA text instead of a visible
  tooltip; and
- rollback guidance did not keep old supervisors paused or fully describe the
  old enum serialization failure mode.

The amended series limits applied backfill to exact matching evidence, uses the
latest stable event as the removal lower bound, adds bounded loader transitions
and cleanup, splits the vpsAdmin work into focused commits, renders a real
hover/focus tooltip, and strengthens rollback guidance. API lifecycle fields
also now have explicit labels/descriptions.

Re-review then found two related edge cases: a release-only change deferred by
a transition still used the transient observation as its lower bound, and the
absolute tooltip was clipped by the table cell even though Playwright reported
it CSS-visible. The API now uses the stable event for deferred release bounds;
the timestamp cell permits tooltip overflow, and Playwright checks both the
computed overflow and actual intersection (ratio `1` in the review probe). The
corrections were autosquashed into their original unmerged feature commits, and
the final tree is byte-identical to the reviewed corrected tree.

The final standalone review reported no blocking or important findings. It
advised narrowing one runbook statement about historical migration and making
the browser geometry assertion stricter. The runbook now explicitly says that
only exact event/evidence timestamp matches become historical `applied` rows;
ambiguous or later metadata rows remain generic. The browser test now requires
an intersection ratio greater than `0.99` for both hover and keyboard focus.
Both advisory changes are committed and pushed.

## Open questions

- None. Decisions recorded in `plan.md` were confirmed with the user.

## Cleanup

- The temporary detached vpsAdminOS history worktree used to compare fixture
  derivations was removed.
- Top-level tracking updates are committed and pushed.
- The development cluster, its state, and its task-local compatibility launcher
  are intentionally retained while the user reviews the feature. Feature
  worktrees remain pending integration/merge.
