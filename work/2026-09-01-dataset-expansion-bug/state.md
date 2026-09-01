# 2026-09-01-dataset-expansion-bug

## Repositories

- `vpsadmin`
  - branch: `2026-09-01-dataset-expansion-bug`
  - worktree:
    `worktrees/2026-09-01-dataset-expansion-bug/vpsadmin`
  - stacked base: `origin/2026-08-31-vpsadmin-notifications` at
    `f2f7c6a9a10437892929fdf99b968e1010aa19b0`
  - head: `9fc0648accd414246d6422e67106ae7217486020`
  - clean and pushed
- `vpsfree-mail-templates` (upstream repository
  `vpsfree-notification-templates`)
  - branch: `2026-09-01-dataset-expansion-bug`
  - worktree:
    `worktrees/2026-09-01-dataset-expansion-bug/vpsfree-mail-templates`
  - stacked base: `origin/2026-08-31-vpsadmin-notifications` at
    `c38e56c945d1fb0df41a26b6c9127368eb592373`
  - head: `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`
  - clean and pushed
- `vpsfree-cz-configuration`
  - branch: `2026-09-01-dataset-expansion-bug`
  - worktree:
    `worktrees/2026-09-01-dataset-expansion-bug/vpsfree-cz-configuration`
  - stacked base: `origin/2026-08-31-vpsadmin-notifications` at
    `5aeb332c7841ec0f277b0062697805743b4cae24`
  - head: `3d09a0f1e50184e65f2547a0913f4aa76399f66b`
  - clean and pushed
- Top-level workspace: this plan, state, and one reusable API-suite note only;
  unrelated shared changes are being left untouched.

## Status

Implementation is committed and pushed in all three repositories. Focused and
broad tests, lint, hooks, template checks, flake checks, and both API-service
configuration builds pass. Mandatory fresh-context review reported no blocking
or important findings. The two selected vpsAdminOS node builds cannot evaluate
on this machine because its required initrd SSH secret is absent; both stop
before any derivation, including a kernel, is built. Nothing has been deployed
or activated.

## Implementation commits

- `vpsadmin`, pushed to `origin/2026-09-01-dataset-expansion-bug`:
  - `3385d7eeb`: update the post-expansion in-memory refquota and cover success,
    failure, pool accounting, and the published storage-status payload.
  - `9fc0648accd414246d6422e67106ae7217486020`: require explicit expansion-mail
    values; carry automatic targets from events and manual targets from their
    computed operations; cover all callers and the mail contract.
- `vpsfree-notification-templates`, pushed to the same branch name:
  - `5605118`: render Czech and English expansion sizes from explicit values,
    with no visible prose changes.
  - `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`: pin vpsAdmin at the producer
    revision for template checks and evaluation.
- `vpsfree-cz-configuration`, pushed to the same branch name:
  - `9388de2c`: pin `vpsadminServices` to `9fc0648a`.
  - `48497234`: pin `vpsadminStaging` to `9fc0648a`.
  - `c39e59e5`: pin `vpsadminProduction` to `9fc0648a`.
  - `3d09a0f1`: pin `vpsfreeNotificationTemplates` to `9e1ddbd9`.

## Quick verification

- `libnodectld` focused RSpec: 3 examples, 0 failures, seed 46495.
- API expansion mail, supervisor, task, and manual-chain focused RSpec: 24
  examples, 0 failures, seed 932 before the final event-target tightening;
  the affected task spec then passed 14 examples, 0 failures, seed 7939.
- Focused RuboCop passed for all changed vpsAdmin Ruby files under the API and
  root hook versions.
- Built-in notification template checker passed: 52 templates and 160 files.
- Both vpsAdmin commits passed all declared Overcommit pre-commit hooks,
  including Nixfmt, RuboCop, API/WebUI i18n, and migration specs.
- Representative standalone Czech and English rendering produced 290 GiB old,
  319 GiB new, 29 GiB added, and 288.9 GiB used. The template diff changes
  only ERB expressions, preserving all visible wording and layout.
- Notification repository `nix flake check --print-build-logs` and
  `nix run .#check` passed, checking 69 templates and 337 files.
- Every generated configuration pin passed its Nixfmt pre-commit hook, and
  `confctl inputs channel ls` reports the exact four revisions listed above.

## Broad verification

- Full libnodectld RSpec passed: 462 examples, 0 failures, seed 46077. It was
  run with an isolated task-specific gem cache because the repository's shared
  `/tmp/dev-ruby-gems` cache contained incomplete Bundler and
  `prometheus-client` trees, matching a previously documented workspace issue.
  The temporary cache was removed afterward.
- The final combined run of all five changed API spec files passed: 24
  examples, 0 failures, seed 51171. This closes the reviewer's request to run
  the final event-target behavior together with every affected mail caller.
- A serial ordinary-API run, explicitly excluding migration specs, completed
  236 examples with 0 failures before it was intentionally interrupted after
  11 minutes 57 seconds once the complete topic-parallel GitHub Actions matrix
  had passed. The remote matrix is the repository's exhaustive, isolated API
  suite and includes coverage aggregation for every selected spec file.
- Loading ordinary and migration specs in one local RSpec process is invalid:
  `spec/migration_helper.rb` globally switches that process to
  `vpsadmin_test_migration`, after which ordinary examples cannot find the core
  schema. The initial monolithic run was stopped after confirming this common
  root cause. The suite boundary and workaround are recorded in
  `notes/vpsadmin/2026-09-01-api-migration-spec-suite-boundary.md`; migration
  specs separately passed through both vpsAdmin pre-commit hooks.
- Pushed-head GitHub Actions results:
  - vpsAdmin API Specs (topic parallel), including all full/core topics and
    coverage: success at `9fc0648a`;
  - vpsAdmin libnodectld Specs, RuboCop, and i18n health: success at
    `9fc0648a`;
  - notification-template Check: success at `9e1ddbd9`;
  - the independent generic vpsAdmin `CI` workflow remains queued for its
    self-hosted runner and has not failed.
- `confctl build -y cz.vpsfree/vpsadmin/int.api1` succeeded and produced
  generation `2026-09-01--13-03-29`.
- `confctl build -y cz.vpsfree/vpsadmin/int.api2` succeeded and produced
  generation `2026-09-01--13-05-02`.
- Both `cz.vpsfree/nodes/stg/node1` and `cz.vpsfree/nodes/prg/node19` stopped
  during evaluation because
  `/secrets/nodes/initrd/ssh_host_ed25519_key` is absent on this machine. The
  identical pre-build error on staging and production targets confirms a local
  deployment-secret prerequisite, not a target-specific regression. No kernel
  build started.
- The configuration shell's generated untracked `.bin/rubocop` and
  `.bundle/config` files were removed after validation; all three source
  worktrees remain clean.

## Mandatory change review

- One standalone fresh-context reviewer inspected all three committed series,
  their stacked bases, tests, pins, commit splits, and compatibility plan.
- Result: no blocking or important findings. Commit splitting, messages, SSH
  remotes, implementation behavior, security, and mixed-version assumptions
  passed review.
- The sole advisory identified stale diagnosis-era statements in this file.
  They were corrected before broader verification.
- The reviewer's residual verification requests were completed as recorded in
  `Broad verification`. The only incomplete external checks are the queued
  generic vpsAdmin CI runner and node builds that require a local deployment
  secret; neither has reported a code or configuration failure.

## Commands run

- Verified that `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG` both identify
  `2026-09-01-dataset-expansion-bug`.
- Inspected the shared workspace status and preserved unrelated changes.
- Read the vpsAdmin security-audit skill and repository-local `AGENTS.md`.
- Located prior workspace guidance for read-only access to central logs at
  `log.int.prg.vpsfree.cz`.
- Fetched both affected upstream repositories and created isolated initiative
  branches and worktrees at the commits listed above.
- After implementation was requested, fetched all three SSH origins, rebased
  the vpsAdmin and notification-template initiative branches onto the exact
  pushed stacked bases listed above, and created the configuration worktree on
  its pushed stacked base. The other initiative's worktrees were not changed.
- `bin/dev-session worktree add` created the configuration worktree but exited
  with status 78 because its checkout hook invoked Overcommit before the
  ambient shell had the bundle's gems. The worktree and branch are intact;
  hook installation and all commits will run from the repository's Nix
  environment.
- The first vpsAdmin commit attempt was blocked by Overcommit because Git ran
  outside `nix develop .#vpsadmin`, leaving RuboCop, gettext, and MariaDB out of
  the hook environment. Retrying from the documented shell passed every hook.
- API RuboCop 1.90 recommended `disable-next`, while the root hook's RuboCop
  1.85 rejected that newer directive syntax. The affected loop was expressed
  as a normal `next unless` guard, which passes both versions.
- The first configuration push attempt was similarly blocked because its
  pre-push hook ran outside `nix develop`. The push passed inside the
  repository shell. Generated `.bin/rubocop` and `.bundle/config` shims were
  removed afterward.
- An initial notification lock command used an incorrectly completed full
  commit hash and received GitHub 404 without changing the lock. It was rerun
  with the exact pushed vpsAdmin hash and succeeded.
- Searched the central logs read-only for the exact dataset-expander event,
  ZFS command, notification transaction, and backup activity for dataset
  `22316`.
- Traced the node event through
  `Operations::DatasetExpansion::ProcessEvent`, the expansion history, the
  storage-status publisher and consumer, the mail transaction chain, dynamic
  dataset property accessors, and the Czech and English notification
  templates.
- Searched all notification templates and the API expansion task for adjacent
  uses of logical-dataset `refquota` and `referenced` properties.
- Ran the focused reproduction with:

  ```sh
  VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec \
    ../vulnerabilities/DATASET-EXPANSION-MAIL/poc_spec.rb \
    --format documentation
  ```

  Result after correcting the production mechanism: 1 example, 0 failures,
  randomized seed 7550.
- Ran a focused nodectld reproduction with:

  ```sh
  nix develop .#libnodectld -c bundle exec rspec \
    ../vulnerabilities/DATASET-EXPANSION-MAIL/node_snapshot_spec.rb \
    --format documentation
  ```

  Result: 1 example, 0 failures, randomized seed 42034.
- Initial reproduction setup needed three local corrections: loading
  `spec_helper` relative to the PoC, seeding pool dataset-property definitions,
  and passing the mail variables as a positional hash on Ruby 3. These were
  PoC construction issues, not product failures.
- The diagnostic PoCs were replaced by maintained libnodectld and API specs and
  removed before committing. `git diff --check` passed, and all three source
  worktrees are clean at their pushed feature heads.

## Results

- At `2026-09-01T10:54:10+02:00`, `node19` logged:

  ```text
  Expanding tank/ct/22316 290.4G -> 319.4G (+29.0G)
  zfs set refquota=342996088259 tank/ct/22316
  ```

  The exact target is 319.4400000004 GiB, matching the 319.44 GiB currently
  shown in vpsAdmin. The old quota was 290.4 GiB and the increment was about
  29.04 GiB. Integer-GiB mail formatting rounds these to 290 and 29.
- `int.vpsadmin1` logged mail transaction chain `12779553` / transaction
  `72540304` as saved, confirmed, and closed at `10:54:12`, two seconds after
  the node event. No expansion or mail failure was logged.
- Event processing explicitly updates the primary `DatasetInPool` property to
  the exact new quota and records an immutable `DatasetExpansionHistory` with
  the event's old, new, and added values.
- The backup-replica theory from the initial investigation was rejected.
  `refquota` is non-inheritable and defaults to zero, so a normal backup
  `DatasetInPool` does not explain an old nonzero quota of 290.4 GiB. The
  original PoC had incorrectly assigned the primary quota to the backup. It
  was replaced with the race reproductions described below.
- nodectld's storage-status reader reads `refquota`, `referenced`, and other
  ZFS properties into an in-memory snapshot, then calls the dataset expander.
  The expander changes ZFS and queues an expansion event, but updates only the
  in-memory pool space counters; it does not update the dataset snapshot's
  `refquota`.
- After expansion, the storage-status submitter publishes that same snapshot
  with the old 290.4 GiB refquota. Expansion events and storage statuses use
  separate publisher threads, RabbitMQ routing keys, queues, and supervisor
  consumers, so their database writes are not ordered together.
- If the expansion event is handled first, it writes 319.44 GiB. The in-flight
  storage status can then overwrite it with 290.4 GiB before the mail is
  rendered. A later storage-status cycle reads ZFS again and restores
  319.44 GiB, explaining the user's current vpsAdmin value.
- The node-level reproduction performs a successful ZFS expansion and proves
  that the immediately published storage-status payload still carries the old
  refquota.
- The API/template reproduction uses only one hypervisor dataset. It applies
  the expansion value, then the in-flight old storage status, renders the
  production Czech template, and finally applies the next fresh status. It
  reproduces the four quoted values exactly and ends at 319.44 GiB.
- The mail chain passes the logical `Dataset`, while the exact new quota is
  already available in `DatasetExpansionHistory`. The Czech and English
  templates render original size from the expansion record but new size from
  the transient current dataset property, exposing the race.
- This is a presentation/data-selection bug, not a failed or rolled-back ZFS
  expansion. The primary quota and accounting are consistent with 319.44 GiB.
- The same transient current-status properties are used by the over-quota
  warning and
  stopped-over-quota mail templates and the active-expansion supervisor's
  stop/suspend thresholds. They may briefly observe stale status, but this
  incident directly confirms only the expansion-mail manifestation.
- The primary fix should update the in-memory storage-status dataset's
  `refquota` after a successful expansion, before publishing the snapshot. The
  expansion mail should additionally render its new size from the exact
  expansion history/event value instead of transient current status. Merely
  changing rounding would not fix the defect.

## Decisions

- Automatic notification targets are carried directly from each successfully
  processed immutable event, rather than querying the newest history row after
  the operation. This removes a possible second race with a concurrent later
  expansion. Deferred batch processing keeps one notification per expansion
  and the target from the latest successfully processed event.
- Adjacent over-quota warning/stop mails and enforcement remain out of scope.
  Correcting the node snapshot removes their confirmed stale-refquota input;
  this incident did not establish a separate persistent defect in those paths.

## Cleanup

- All three worktrees and feature branches are retained for review and
  integration. Remove the worktrees after the initiative is merged or
  abandoned;
  retain branch refs per workspace policy.
- Mandatory change review completed with no blocking or important findings.
- The full libnodectld suite, final combined API regression suite, complete API
  topic-parallel CI matrix, notification CI, and both API configuration builds
  pass. Selected node builds are blocked only by the missing local initrd SSH
  secret and did not start a kernel build.
- No deployment or activation was performed.
