# F1: raw migration-default expectations

Owner: implementer3. Lead integrated exact final head into remote `master` and
reported SSH push/exact remote proof plus claim release verified at 15:07:04.
Implementation, review/reuse, full 84-example acceptance and target preparation
are complete. Lead reports all required fresh-hosted acceptance complete.
Five feature workflows passed; auxiliary CI `43447714261` was still running at
handoff. The owned local observer has exited; lead owns optional later remote
inspection, with no live member observer or remaining local effects.
Lead accepted the sufficient F1 brief after accepting [F0](evidence-vpsadmin-migrations.md).

## Source and scope

- Repository: `git@github.com:vpsfreecz/vpsadmin.git`; target `master`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsadmin`.
- Branch: `2026-11-13-scheduled-workflow-fixes`.
- Reviewed base/head: `6f71da9777edfc902f6483edcdd84a2ef7d464ab` /
  `81d754f47a58e92fddb2a84c67b1aec98b740ae3`.
- Current base: `74e3ab79118fb4a0a013d6c4ace20352e6d62e5f`.
- Final head: `2d0946c4e699aa61092228d8a7cb275477ee46d0`.
- Complete final base-to-head series: one commit, `2d0946c4e699aa61092228d8a7cb275477ee46d0`
  (`api: correct raw migration default expectations`). No superseded approach,
  transitional migration, dependency update or pin stream remains.
- Diff: exactly the nine paths in F0's expectation table, eleven insertions and
  eleven deletions. Each change replaces an incorrectly typed default expectation
  with the raw MySQL string `'0'` or `'1'`; no helper/comment change.
- Initial diff SHA256:
  `8a29c5ac65d032a95954626cd7347b95640f3a15eb1bfc09a4be0a5bf1b7513b`.

No migration was added, rewritten or removed. No dependency/pin stream, schema,
runtime, API/client contract, helper behavior, data or rollback assertion changes.
`git diff --exit-code <base> -- api/db/migrate plugins api/spec/migration_helper.rb
api/db/schema.rb flake.nix flake.lock` passed before checks. The tracked core/plugin
migration index listing has SHA256
`c4309c564d577c905ddb9dcd6b32ac9f81783af4eb85b32f14fc1792606e617d`.
No generated-client synchronization or machine deployment is needed for the
expectation-only diff; the architect's sufficient brief explicitly confirms this.
Revert the test commit to recover source. Persistent state and runtime rollback
behavior are unchanged.

## Verification and environment

`git diff --check` passed. Source was frozen during the bootstrap/narrow batch.
The exact selected paths and narrow invocation are in F0; the command
uses `VPSADMIN_PLUGINS=none nix develop .#api` and the repository's automatic
isolated MariaDB, never a real database. The batch also runs `ruby -c` and
`bundle exec rubocop` on all nine paths, followed by the root development shell
and ordinary Overcommit installation/signing. Profiles retain these exact
environments for later ordinary commit hooks.

Member-owned native watcher: `/root/f1_quick_watch`, fresh GPT-6 Luna/low,
installed package
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`, utility
`dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`. Its installed TOML and
execution policy specify full access / approval never. One operation owns:

```text
bash /tmp/f1-scheduled-workflow-fixes/bootstrap-and-quick.sh
```

Bootstrap script SHA256:
`88571f551dc555b962caf251fcff0effa6164e77c65b2ff466926acf6ef7ec0c`.
API script SHA256:
`4ebdbfcaa94fa50675238022d8ecd57073e674ce725fc77b2fda4e089af7d1e6`.
Selected-path manifest SHA256:
`4904ae78e210c850b2d47a28a43eab1383b13d92d1f4596d13331bcd00747c5a`.
Logs/status: `/tmp/f1-scheduled-workflow-fixes/bootstrap-and-quick.{log,exit}`.
The first operation finished with exit 1 after 103 seconds, before syntax/specs
or RuboCop: its unbundled version probe could not load `active_record`. The API
bundle had installed successfully (33 dependencies, 118 gems). The requested
first-operation log/status files were absent; the watcher retained the terminal
exec result (session 77854) and bounded exception evidence. No operation remained
running. This was an invocation error, not a failing migration example.

The corrected probe uses `bundle exec ruby -ractive_record`. A fresh Luna/low
watcher `/root/f1_quick_v2_watch`, using the same installed utility policy, owns
`bash /tmp/f1-scheduled-workflow-fixes/quick-v2.sh`. This script records its own
log and exact exit status in `/tmp/f1-scheduled-workflow-fixes/quick-v2.{log,exit}`
and reuses the already realized API profile. Its SHA256 is
`1d33da7eedec1ad14119a0f8f117cd5b48772c1cf62b2f85783a54350adbf780`;
corrected API script SHA256 is
`3df978c00d503dd6aa27930f8617dd45eea452384d10884eebb99d40ec1a5ea3`.
No source change or check was duplicated; the first attempt had not reached them.
Corrected quick batch passed in approximately 64 seconds, exit 0 (watcher tool
session 21944 completed, no surviving owned operations):

- Ruby 3.4.9; ActiveRecord 8.1.4.1; local MariaDB 11.4.12. Automatic isolated
  database startup reported REPEATABLE-READ and `innodb_snapshot_isolation=0`.
- Nine `ruby -c` checks passed; the exact nine-file RSpec batch ran 18 examples,
  zero failures; RuboCop inspected nine files with no offenses.
- Root Overcommit 0.76.0 installed hooks and verified configuration/plugin
  signatures. No hook was disabled or changed.
- API profile: `/nix/store/6xasqclpph7jj3vls5zr9a3ffrxdg191-vpsadmin-api-env`.
  Root profile: `/nix/store/5m7xf80v9h6wrscc0r6jiznhnb1b221d-vpsadmin-env`.
- Effective core API lock SHA256:
  `bb4bccb319f98631d7c7c10a6560c517a475d7ee96c0252fd06923622c755e61`;
  root lock SHA256:
  `74c966464d3f0e21d4cffa8a9bfc87719ade909799d5ccf480c4cee91a838a20`.

Local narrow coverage uses MariaDB 11.4.12 rather than the failed CI runner's
11.8.6. Exact-head CI remains the check of that runner environment.

The first ordinary commit did not create a commit: its API i18n hook selected
all plugins, while only core-mode API dependencies were prepared (`fio_api`
missing). A direct `git hook run pre-commit` in the root shell confirmed that
failure; Nixfmt, migration coverage, WebUI i18n and RuboCop hooks passed. Log:
`/tmp/f1-scheduled-workflow-fixes/pre-commit.log`, exit 65. A core-mode commit
attempt then ran API i18n but failed normalization/missing/unused checks against
the full-plugin tracked catalog; log `commit.log`, exit 1, no commit created.
These failures are not a reason to change locale source or bypass hooks.

A fresh `/root/f1_hook_env_watch` runs only full-plugin API dependency preparation
and unchanged `rake vpsadmin:i18n:health`, using the same utility policy. Command
`bash /tmp/f1-scheduled-workflow-fixes/full-hook-environment.sh`, script SHA256
`45d72dcd17afb07be0f2a16ef1c1110901ca0fd84f4a53b06e096c7cc02b2414`, log/status
`/tmp/f1-scheduled-workflow-fixes/full-hook-environment.{log,exit}`. No full
migration suite or duplicate passing narrow batch was run. Full-plugin dependency
preparation and unchanged API i18n health passed, exit 0 in 74.1 seconds; 34 API
dependencies / 122 gems installed. Watcher session 19854 completed with no
remaining owned work. The failed core-mode catalog check was an environment
mismatch; no locale defect or source remediation was established. Normal
full-plugin commit hooks then ran with the prepared dependencies.

The original hook-enabled commit passed all five pre-commit hooks (Nixfmt, migration
spec coverage, WebUI i18n, RuboCop and API i18n) and all commit-message hooks.
The message-width hook issued a nonblocking 72-column warning; the longest line
is 73 characters, within the workspace's mandatory 80-character limit. No hook
was bypassed. Exact command:

```bash
VPSADMIN_PLUGINS=all nix develop /tmp/f1-scheduled-workflow-fixes/root-shell \
  -c git commit -F /tmp/f1-scheduled-workflow-fixes/commit-message.txt
```

Log/status: `/tmp/f1-scheduled-workflow-fixes/commit-full.{log,exit}`, exit 0.
Commit tool session 9682 finished with no unresolved command effects. At original
publication, a fresh fetch confirmed `origin/master` was still
`6f71da9777edfc902f6483edcdd84a2ef7d464ab` and an ancestor of reviewed head
`81d754f...`; no rebase was needed then. The later refresh is recorded below.

Feature publication passed using the same repository root Nix profile and hook
bundle with `VPSADMIN_PLUGINS=all` and ordinary `git push -u origin
2026-11-13-scheduled-workflow-fixes`. An initial ambient-shell push was refused
by its unsigned-config check and created no remote branch; using the correctly
signed repository environment resolved that without any hook bypass or source
change. Log/status: `/tmp/f1-scheduled-workflow-fixes/push.{log,exit}`, exit 0.
`git ls-remote --heads origin refs/heads/2026-11-13-scheduled-workflow-fixes`
confirmed original reviewed head `81d754f47a58e92fddb2a84c67b1aec98b740ae3` remotely.
The committed final diff SHA256 still equals the initial patch SHA256 above.

Original reviewed-head push CI (attempt 1), without dispatch/rerun:

- [API Migration Specs 43444434044](https://github.com/vpsfreecz/vpsadmin/actions/runs/43444434044)
- [RuboCop 43444433950](https://github.com/vpsfreecz/vpsadmin/actions/runs/43444433950)
- [i18n health 43444434005](https://github.com/vpsfreecz/vpsadmin/actions/runs/43444434005)
- [CI 43444434000](https://github.com/vpsfreecz/vpsadmin/actions/runs/43444434000)
- [API Specs 43444434070](https://github.com/vpsfreecz/vpsadmin/actions/runs/43444434070)

The single push-CI watcher `/root/f1_push_ci_watch` recorded the first four runs
completed/success at attempt 1 on the original reviewed head. API Specs completed
cancelled automatically when the refreshed branch superseded it. The watcher
returned aggregate exit 1 for that cancellation, not a source/test failure;
original session 5247 is finished with no remaining owned work. Watch script SHA256:
`d090bf1eb780e436acc15b99ed56891e179292fb6a39e376bcdc365367c8b17c`;
aggregate log/status `/tmp/f1-scheduled-workflow-fixes/push-ci.{log,exit}`, with
per-run final JSON and any failed logs in that same directory. No workflow was
dispatched, rerun or duplicated by the watcher.

API Migration Specs completed successfully: attempt 1, original reviewed head,
ActiveRecord 8.1.4.1 and MariaDB Ubuntu package `1:11.8.6-5ubuntu0.1`, 18 examples,
zero failures in 3.81 seconds. Its command was `xargs -a tmp/migration-specs.txt
bundle exec rspec --options /dev/null --format documentation`. Log retained at
`/tmp/f1-scheduled-workflow-fixes/api-migration-ci-success.log`.
This is the nine changed files selected by the push event, not the full
84-example migration suite selected by schedule/dispatch. It proves the repaired
expectations on hosted MariaDB 11.8.6; 66 other examples remain outside this run.
Lead was informed before deciding on a post-review local full batch or the
approved lead-owned post-integration workflow dispatch. Lead selected the local
full 84-example batch after final review, adding the missing 66 examples before
integration, followed by the separately requested master workflow dispatch.
The post-review full batch passed as recorded below. No check was rerun merely
to change its ordering relative to review.

The worktree registration/check-out succeeded, but its existing post-checkout
hook returned unsigned-configuration failure. Authoritative worktree/branch and
portal entries were checked before proceeding; the add was not repeated. Normal
Overcommit installation and trust signing are part of the authorized bootstrap.

## Post-review full suite and refreshed history

Lead reported reviewer0's final all-lane review complete with no F1 source
finding, then released one full migration batch. Exact command, in the feature
worktree:

```bash
VPSADMIN_PLUGINS=none nix develop /tmp/f1-scheduled-workflow-fixes/api-shell \
  -c bash -euo pipefail -c \
  'bundle exec rspec --options /dev/null --format documentation spec/migrations/*_spec.rb'
```

Result: **84 examples, zero failures**, command exit 0; 24.41 seconds of examples
and 1.34 seconds loading. This adds the 66 uncovered examples. Environment:
Ruby 3.4.9, ActiveRecord 8.1.4.1, automatic isolated MariaDB 11.4.12,
REPEATABLE-READ / snapshot isolation 0; logical database `vpsadmin_test_migration`.
The runner creates a fresh temp directory/free local port and removes its owned
instance at exit. The random port/directory are not exposed by its log; no real
database URL or database-name override was configured. Effective core lock
remained `bb4bccb319f98631d7c7c10a6560c517a475d7ee96c0252fd06923622c755e61`.
Script SHA256 `e2cf39f16483491b9f9d18046f1d262935c439c4494dddc472d392db79635f30`;
log/status `/tmp/f1-scheduled-workflow-fixes/full-migrations.{log,exit}`.
Tool session 36419 completed, with no surviving test runner/database.

A fresh fetch before target preparation found upstream dependency commits
`dd894e1e10d5b11c0ad42d9e74995d39f6029548` (packaged API/console-router) and
`74e3ab79118fb4a0a013d6c4ace20352e6d62e5f` (WebUI). An authorized clean rebase
changed the reviewed range
`6f71da9777edfc902f6483edcdd84a2ef7d464ab..81d754f47a58e92fddb2a84c67b1aec98b740ae3`
to final range
`74e3ab79118fb4a0a013d6c4ace20352e6d62e5f..2d0946c4e699aa61092228d8a7cb275477ee46d0`.
`git range-diff` reports the single patch equal; there was no conflict or edit.
The final leased force-push named the exact original remote head and remote
`ls-remote` verified final head `2d0946c4e699aa61092228d8a7cb275477ee46d0`.

Lead independently reconstructed the reviewed patch on the new base, proved
exact final tree and byte-identical binary patch, and accepted review/full-suite
reuse in [review-reuse-f1.md](review-reuse-f1.md). All value-bearing profile fields
and functions match fresh environment evidence; only six unknown/no-value shell
placeholders are omitted. API/root outputs remain the exact store paths above;
the current effective core lock equals the saved successful core lock. API tree
`ce5631c9d4139eb8a338dae79397d35f828f950e`, plugins tree
`449edce0cab21fb2a3c355f551c4a865655adb27` and tools tree
`87cd674523792d96b0a84ac31339743cce805e73` match at both feature heads. No
unchanged successful test was repeated after the equivalent rebase.

## Detached target and current CI

Clean detached integration target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/vpsadmin`,
HEAD `74e3ab79118fb4a0a013d6c4ace20352e6d62e5f`. Prepared outside claims using
only this session's ignored gem bundles and exact locks. From that target cwd:

```bash
VPSADMIN_PLUGINS=all nix develop /tmp/f1-scheduled-workflow-fixes/root-shell \
  -c bash /tmp/f1-scheduled-workflow-fixes/target-hooks.sh
VPSADMIN_PLUGINS=all nix develop /tmp/f1-scheduled-workflow-fixes/api-shell \
  -c bundle check
```

The hook script installs Overcommit, signs config/pre-commit plugins, invokes
the normal pre-commit entry point, and verifies clean detached HEAD. It passed
in three seconds; this empty-index invocation does not claim to rerun the five
source checks. Full-plugin API bundle preparation/check also passed: 34
dependencies, 122 gems, all dependencies satisfied. Target root lock SHA256
`74c966464d3f0e21d4cffa8a9bfc87719ade909799d5ccf480c4cee91a838a20`;
API full-plugin lock SHA256
`95d433705be8d06260b5099d39a4f0735ba6441d4e59923be543b7a5668ca4ae`.
Hook log/status: `/tmp/f1-scheduled-workflow-fixes/prepare-target-hooks.{log,exit}`
(exit 0, watcher tool session 82713 complete). API preparation log:
`/tmp/f1-scheduled-workflow-fixes/target-api-bundle-check.log` (exit 0, session
82317 complete). `git status --porcelain=v1` is empty and `git symbolic-ref -q
HEAD` returns 1. Lead should enter the target with the full-plugin root-profile
prefix above for ordinary Git/hooks. No member merge/default push was performed.

Refreshed exact-head push runs, all attempt 1: migration specs `43447714222`,
RuboCop `43447714108`, i18n `43447714074`, WebUI PHPUnit `43447714353` and API
Specs `43447714245` passed. The final authoritative `gh run view` snapshot
reported CI `43447714261` still `in_progress`, no conclusion. Every run is bound
to final head `2d0946c4e699aa61092228d8a7cb275477ee46d0`.
The single watcher `/root/f1_refreshed_ci_watch` observed the six existing runs
without dispatch/rerun; script SHA256
`0259bc18b4a1786774035a0d33253cc1260db9f816e87072712689fa6ca2b701`, aggregate
`/tmp/f1-scheduled-workflow-fixes/refreshed-ci.{log,exit}`. CI-specific watch output
is `/tmp/f1-scheduled-workflow-fixes/ci-43447714261.watch.log`.

After approximately 58 minutes, lead explicitly authorized ending only the owned
local read-only observation command, retaining every remote run. The final
six-run status snapshot above was taken first. Original native session 27679
then exited 143 through scoped graceful local interruption. The script's EXIT
trap file contains 0 despite that signal; it is not a successful CI receipt.
The authoritative result is **incomplete remote feedback, no local effects**.
The watcher reconciled all owned cells/sessions and found no remaining observer
or script process. Parent also confirmed former observer PIDs 2745251 and
2747200 are absent. No remote CI cancellation/retry/dispatch or session/team/
utility lifecycle action occurred. The native utility remains retained normally.
Lead owns optional later inspection of remote CI `43447714261`; no replacement
live observer was started by this member.

## Delivery boundary

Lead reported approved fast-forward integration of exact final head
`2d0946c4e699aa61092228d8a7cb275477ee46d0` from fresh target
`74e3ab79118fb4a0a013d6c4ace20352e6d62e5f`, through the prepared normal hook
environment, followed by SSH push and exact remote proof. Repository claim was
released and its release verified at lead-reported 15:07:04. This member performed no
merge or default push. Feature branch is retained.

Lead dispatched full master API Migration Specs
[43449334492](https://github.com/vpsfreecz/vpsadmin/actions/runs/43449334492) at
the integrated exact head; it was initially queued. Root's
`watch_org_and_migrations` is its sole observer. This member does not dispatch or
observe that master run. Lead subsequently reported required F1 source/full-suite
local and fresh-hosted acceptance complete. Remaining broader feature CI is
auxiliary feedback, not an F1 acceptance gate: only remote CI `43447714261`
lacks a terminal conclusion in the final snapshot. Its optional later inspection
belongs to lead. No additional tests or cleanup requested; all local work and
observer effects are reconciled.
Migration provenance: none created, changed or removed; every existing migration
version remains byte-identical. No obsolete functional history, migration or pin
stream remains in the one-commit feature range. No runtime/API/client contract,
schema or machine deployment is part of F1. Session remains open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
