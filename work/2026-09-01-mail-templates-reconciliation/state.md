# 2026-09-01-mail-templates-reconciliation

## Repositories

- `vpsadmin`
  - branch: `2026-09-01-mail-templates-reconciliation`
  - worktree: removed after default-branch integration
- `vpsfree-cz-configuration`
  - branch: `2026-09-01-mail-templates-reconciliation`
  - worktree: removed after default-branch integration
- `vpsfree-maintenance-tasks`
  - branch: `2026-09-01-mail-templates-reconciliation`
  - worktree: removed after default-branch integration

## Status

All intended implementation changes and mandatory-review fixes are committed,
fast-forwarded into the three upstream default branches, and pushed. Both
production-role configuration builds passed from the exact merge candidate.
Four default-branch vpsAdmin workflows passed; the API matrix is running
without failures and aggregate CI remains queued behind the shared-runner
backlog. The two other repositories did not trigger workflows for these
commits. All initiative worktrees have been removed while preserving the local
and remote feature branches.

## Commands run

- `bin/dev-session current`
- Inspected top-level status, initiative skeleton, canonical remotes, and
  feature-branch availability.
- Fetched current upstream `master` and created all three feature worktrees.
- Installed and verified Overcommit hooks in `vpsadmin` and
  `vpsfree-cz-configuration`; the maintenance repository declares no hook
  framework.
- `nix develop -c nixfmt ...` for touched vpsAdmin Nix files.
- `nix develop .#api -c bundle exec rspec` for the request update, request
  resolve, and registration API specs.
- `nix develop .#api -c bundle exec rubocop` for all touched API specs.
- `nix build --no-link` for the overlay and replacement notification-template
  checks.
- `ruby -c` for the maintenance task.
- Ran the maintenance task against an isolated temporary vpsAdmin database in
  dry-run, apply, already-absent, and referenced-template scenarios.
- Applied the `vpsfree-user-facing-writing` skill in embedded English mode to
  the new Nix option descriptions; no wording changes were needed after the
  technical text audit.
- Committed and pushed the vpsAdmin feature revision so configuration could pin
  it.
- `confctl inputs channel set --commit vpsadmin vpsadmin c962808b1`.
- Formatted and committed the API1 replacement-mode configuration.
- Ran the mandatory standalone review. It found two blocking cleanup-safety
  gaps and one missing module regression check: the already-absent path did not
  inspect orphan references, nonlocking reference checks allowed a live writer
  race, creation audit history was not exact, and replace-mode database seeding
  was not covered by a committed Nix check.
- Strengthened the maintenance task to reject orphan references, require an
  explicit all-writers-stopped maintenance window for apply, verify all target
  references again before commit, and require exactly one unchanged creation
  audit version per template and translation.
- Re-ran isolated-database cleanup scenarios for missing apply confirmation,
  dry-run, altered audit history, an existing mail-log reference, apply,
  already-absent idempotency, and an orphan mail-log reference.
- Added and built the vpsAdmin module check for replace-mode seeding defaults
  and the contradictory explicit setting.
- Amended and force-pushed the vpsAdmin feature commit, then cancelled the two
  queued or running workflows for the superseded commit.
- Regenerated the existing configuration input commit with `confctl` against
  the amended vpsAdmin revision and replayed the functional configuration
  commit, leaving one generated input-pin commit.
- The follow-up review found that the first contradictory-setting Nix check
  could pass because unrelated minimal-NixOS assertions also failed. Replaced
  the whole-system `tryEval` with direct checks of the uniquely identified
  vpsAdmin database-setup assertion in valid and contradictory configurations.
- The same standalone reviewer independently evaluated the corrected check and
  reported no remaining findings.
- Built `cz.vpsfree/vpsadmin/int.api1` and `int.api2` with `confctl`.
- Inspected the rendered generations: API1 reconciles an effective package of
  exactly 69 templates with all six targets absent; API2 has no notification
  template reconciliation unit.
- Pushed the maintenance and configuration feature branches. Maintenance and
  configuration have no GitHub Actions runs for this branch.
- Created detached integration worktrees from each exact `origin/master`,
  fast-forwarded them to the reviewed feature heads, and confirmed that no
  default branch had advanced before pushing.
- From the exact vpsAdmin merge candidate, reran 34 focused examples, RuboCop
  on the three touched specs, all three notification-template Nix checks, and
  `git diff --check`.
- From the exact configuration merge candidate, rebuilt
  `cz.vpsfree/vpsadmin/int.api1` and `int.api2` sequentially.
- Fast-forwarded and pushed `master` in dependency order: vpsAdmin, the
  maintenance task repository, then production configuration.
- Refetched all three remotes, verified each `origin/master` and preserved
  local/remote feature ref at the reviewed head, and removed all six clean
  initiative worktrees.

## Results

- Active initiative: `2026-09-01-mail-templates-reconciliation`.
- All three canonical remotes use SSH.
- No initiative branch or project worktree existed at start.
- The shared top-level checkout contains unrelated changes; only this
  initiative's `plan.md` and `state.md` will be staged for its tracking commit.
- `vpsadmin`
  - base: `ba1217fb2757cf8624ac0d1fd89d9466377b6289`
  - head: `cbd0fa164` (`nixos: support authoritative notification templates`)
  - pushed to `origin/2026-09-01-mail-templates-reconciliation`
  - fast-forwarded and pushed to `origin/master`
  - focused RSpec: 34 examples, 0 failures; post-edit chain rerun: 5 examples,
    0 failures
  - RuboCop: 3 files, no offenses
  - overlay, replacement, and replace-mode database-seeding Nix checks built
    successfully
  - all declared pre-commit hooks passed
  - mandatory review: all initial blocking/important findings resolved; final
    narrow follow-up reported no findings
  - current-head GitHub Actions passed: API Specs (topic parallel), RuboCop,
    WebUI PHPUnit, Client Specs, and i18n health
  - aggregate CI run `33525532270` is queued without a runner; older master and
    feature-branch aggregate CI runs are also queued or running ahead of it
- `vpsfree-maintenance-tasks`
  - base: `4f48c0ef6b3e1d948e94452d83a06a126694d4b0`
  - head: `9965859` (`2026-09-01-remove-unintended-notification-templates: add cleanup`)
  - Ruby syntax valid; file mode is executable
  - isolated database dry-run preserved all rows; apply with explicit writer
    shutdown confirmation removed six templates and six translations; rerun
    succeeded as already absent
  - altered creation audit history, an existing mail log, and an orphan mail
    log after deletion each caused refusal; apply without the writer-shutdown
    confirmation was also refused
  - pushed to `origin/2026-09-01-mail-templates-reconciliation`
  - fast-forwarded and pushed to `origin/master`
- `vpsfree-cz-configuration`
  - base: `94125328acb7a6f5b28cfe4d58e49ed4788d23a1`
  - head: `28a39a52`
  - generated pin commit: `9a4df408`, unchanged `confctl` message
  - functional commit: `28a39a52` (`vpsadmin-config: use authoritative notification templates`)
  - vpsAdmin services input pins `cbd0fa16`
  - all declared pre-commit hooks passed
  - feature API1 generation `2026-09-01--17-28-32` and exact-merge generation
    `2026-09-01--19-08-39` built successfully
  - feature API2 generation `2026-09-01--17-30-20` and exact-merge generation
    `2026-09-01--19-09-31` built successfully
  - API1 effective package contains 69 templates and omits IDs/names 71--76;
    API2 has no `vpsadmin-notification-templates.service`
  - pushed to `origin/2026-09-01-mail-templates-reconciliation`
  - fast-forwarded and pushed to `origin/master`
- A first manual database command failed because separate short-lived
  `nix develop -c` invocations do not preserve the test database process. The
  existing durable note `notes/vpsadmin/2026-07-22-test-db-single-nix-shell.md`
  documents the cause and working single-shell procedure used successfully.
- The first API spec command included an unnecessary `cd api`; the API dev
  shell already changes into that directory. The corrected command ran the
  suite successfully.
- An initial post-review amend and configuration rebase were invoked outside
  their Nix shells and correctly refused by repository hooks because declared
  tools were unavailable. Both operations were rerun in their repository Nix
  shells; the complete hook suites passed.
- Superseded vpsAdmin workflow runs `33521432634` and `33521432404` were
  cancelled after force-pushing `e98080819`. Current-head workflows were left
  running.
- Superseded vpsAdmin workflow runs `33524398574` and `33524398557` were
  cancelled after the final force-push to `cbd0fa164`.
- A first `confctl build` omitted `--yes` and exited at its confirmation prompt;
  both builds were rerun noninteractively with `--yes` and passed.
- A mistyped full vpsAdmin revision produced a GitHub 404 before changing the
  configuration lock. Repeating `confctl inputs channel set` with the exact
  `git rev-parse HEAD` result succeeded.
- The first configuration push was correctly refused by its pre-push hook in
  the ambient shell due to unavailable bundled gems. The Nix-shell push passed.
- Current-head vpsAdmin API Specs run `33525532305` completed successfully.
  RuboCop, WebUI PHPUnit, Client Specs, and i18n health also completed
  successfully. Aggregate CI run `33525532270` remains externally queued; at
  handoff, older runs including master `33511838961` were still ahead of it.
- The first merge-worktree RSpec invocation used stale `spec/api/...` paths and
  therefore loaded no examples. The corrected repository paths ran 34 examples
  successfully before any default-branch push.
- Default-branch integration heads are vpsAdmin `cbd0fa164`, maintenance
  `9965859`, and configuration `28a39a52`. Local and remote feature branches
  remain at the same heads.
- Default-branch vpsAdmin RuboCop, WebUI PHPUnit, Client Specs, and i18n health
  runs passed. API Specs run `33536221934` had 14 of 26 jobs complete and 12
  running without a failure at the last check; aggregate CI run `33536221911`
  remained queued behind the shared-runner backlog.
- The operator reported that a production maintenance-task run intentionally
  refused removal after finding one `mail_logs` reference to the target IDs.
  The guard ran before deletion, so no target template was removed by that
  attempt. This proves that one fallback generated a logged email, although a
  mail log alone does not prove final delivery. The operator subsequently
  reported removing the inspected log and completing the cleanup. Those
  production changes were not performed or independently verified by this
  development session. The operator then confirmed that a follow-up dry-run
  reported all targets absent; that path also validates that no table with a
  `mail_template_id` column still references target IDs 71--76.

## Open questions

None. Decisions confirmed with the user: explicit replace mode, guarded
maintenance task, default-branch integration, and worktree cleanup. The
maintenance task must not be run on production as part of this initiative.

## Cleanup

Complete. Removed the three feature worktrees, the three detached integration
worktrees, and the now-empty initiative worktree directories. Preserved all
three feature branches locally and remotely, plus this plan and state record.
