# 2026-08-12-dns-secondary-zone-transfer-failure

## Repositories

- `vpsadmin`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsadmin`
  - rebased base: `origin/master` at `02449a1e0`
    (`webui: identify the dataset edit action`)
  - merged feature head:
    `b3d63c005bef30be52165cd80ef4978bbf0e72b2`
  - pushed to `origin/2026-08-12-dns-secondary-zone-transfer-failure`
    and fast-forwarded into `origin/master`
- `vpsfree-cz-configuration`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-cz-configuration`
  - merge base: `origin/master` at
    `8dd3d1a42664ce0fed33fd6e985a2d95402bf2f0`
  - merged feature head:
    `a8d8b5fe84c8a9990f5ff245361819e4132e8826`
    (`inputs: set vpsadminServices to b3d63c00`)
  - pushed to `origin/2026-08-12-dns-secondary-zone-transfer-failure`
    and fast-forwarded into `origin/master`

## Status

- Root cause confirmed and implementation authorized.
- User selected cleanup of existing false rows.
- User selected unmerged feature-branch delivery and an exact
  `vpsadminServices` feature pin in `vpsfree-cz-configuration`.
- User subsequently chose to remove the supervisor compatibility filter and
  deploy nodectld to DNS nodes before the API cleanup.
- Both revised feature branches and default branches are committed and pushed.
  The standalone follow-up review is resolved, focused validation and all
  requested integration/configuration builds pass. No deployment or database
  migration was run.

## Commands run

- `bin/dev-session current`
  - confirmed the active slug and matching
    `VPSFREE_DEV_SESSION_SLUG=2026-08-12-dns-secondary-zone-transfer-failure`.
- Inspected the earlier `2026-07-07-secondary-dns-transfer-check` initiative,
  vpsAdmin history, parser, parser specs, API supervisor, supervisor specs, API
  resource, WebUI rendering, and DNS integration test.
- `bin/dev-session worktree add ... vpsadmin --base origin/master`
  - fetched current upstream and created the initiative worktree at
    `925a85878`.
- Inspected `vpsfree-cz-configuration`'s `vpsadminServices` lock.
  - production pin is `95f8d9ca7cb31e284d19ac7bc6d310a25a7071dc`.
  - both July DNS fixes, `62b838b1c` and `6761aa11b`, are ancestors of the
    pin.
- First `nix develop .#libnodectld --command ...` parser probe failed because
  the entered shell did not retain the caller's repository working directory.
  Retried with the absolute worktree path, following the already documented
  workspace workaround.
- Ran the exact observed `Transfer status` and `Transfer completed` messages
  through `NodeCtld::DnsTransferLog#parse_message` in the libnodectld Nix
  shell.
- Inspected upstream BIND 9.20.26 source at tag `v9.20.26`, including
  `lib/dns/xfrin.c`, `lib/isc/result.c`, and `lib/dns/zone.c`.
- Fetched both affected repositories before implementation.
  - vpsAdmin `origin/master` remains `925a85878`.
  - vpsfree-cz-configuration `origin/master` advanced to `a301114d`.
- Implemented parser suppression, cleanup migration, focused specs, and DNS
  integration coverage. The initially implemented supervisor rolling-upgrade
  filter was later removed at the user's request.
- Focused verification:
  - libnodectld parser: 7 examples, 0 failures;
  - API supervisor: 8 examples, 0 failures;
  - cleanup migration: 5 examples, 0 failures;
  - core schema smoke: 2 examples, 0 failures;
  - API and libnodectld RuboCop: no offenses;
  - Nix formatting and `git diff --check`: clean;
  - staged migration/spec pairing check: clean.
- The first commit invocation was attempted outside the Nix shell and was
  correctly blocked because hook executables were unavailable. It made no
  commit. Re-running inside `nix develop .#vpsadmin` passed every pre-commit
  and commit-message hook.
- Committed vpsAdmin as `c9b679847578bcbba9692f91bd3fb98b80add82e`
  (`dns: ignore up-to-date transfer statuses`) and pushed the feature branch.
- `bin/dev-session worktree add ... vpsfree-cz-configuration` created the
  requested branch and worktree at `a301114d`, but returned exit 78 because
  checkout-time Overcommit could not find its gems outside the dev shell. The
  worktree was verified intact; this is the known workflow documented in
  `notes/vpsfree-cz-configuration/2026-06-10-worktree-overcommit-gems.md`.
- Installed configuration hooks in `nix develop` and ran:
  `confctl inputs channel set --commit vpsadmin vpsadmin c9b679847578bcbba9692f91bd3fb98b80add82e`.
  It passed hooks and created `81cfa3d1`; only `flake.lock` changed.
- `confctl inputs channel ls vpsadmin` resolves `vpsadminServices` to
  `c9b67984`. Removed the transient `.bin/rubocop` and `.bundle/config` files
  created by the configuration dev shell; the worktree is clean.
- Initial vpsAdmin GitHub Actions at the superseded feature head `c9b67984`:
  - API Migration Specs, RuboCop, i18n health, and libnodectld Specs passed;
  - API Specs was cancelled automatically after the follow-up push;
  - the superseded full CI run was cancelled after confirming the remote branch
    had advanced to `6248f607`.
- Mandatory standalone review result:
  - no blocking findings;
  - one important deployment/concurrency finding: the initial cleanup could
    race active supervisor consumers and overwrite a newer cached state;
  - one advisory tracking finding: label the parser diagnosis as pre-change.
- Addressed the advisory wording in this state file and the important finding
  in code and deployment planning:
  - supervisor persistence now holds the DNS-server-zone row lock;
  - cleanup acquires the same lock, reloads/rechecks the latest pointer, and
    deletes candidates per zone;
  - the initial plan required all API supervisors to run the guarded/locking
    revision before migration, then ns3/ns4 to roll out after cleanup.
- Follow-up verification passed:
  - cleanup migration: 6 examples, 0 failures, including stale-state recheck;
  - API supervisor: 8 examples, 0 failures, including row-lock use;
  - API RuboCop: 4 files, no offenses;
  - repository hooks all passed.
- Committed and pushed vpsAdmin follow-up
  `6248f607e850b347ed39d43822540ab61260aad4`
  (`dns: serialize transfer state cleanup`).
- Updated the exact configuration pin through confctl. The initial follow-up
  left two consecutive generated pin commits; on the reviewer's advisory, the
  branch was regenerated from `origin/master` in a detached temporary worktree.
  Final generated commit `52aaabcc4e98adb5e3e48a55aabeb12ea86b76eb`
  directly pins `vpsadminServices` from production `95f8d9ca` to `6248f607`.
  It passed hooks, only changes `flake.lock`, and the temporary worktree and
  transient dev-shell files were removed.
- Reviewer follow-up confirmed the shared locking contract and deployment
  order resolve the Important finding, found no new Blocking or Important
  issues, and authorized long integration/build validation.
- Long validation passed:
  - `./test-runner.sh test dns/secondary-transfer-errors`: both examples and
    the 1-test scenario passed in 601.24 seconds;
  - `confctl build -y 'cz.vpsfree/vpsadmin/*'`: all 11 machines built;
  - `confctl build -y cz.vpsfree/containers/ns3`: built;
  - `confctl build -y cz.vpsfree/containers/ns4`: built.
- Refetched configuration `origin/master` before push; it remained at
  `a301114d` and is an ancestor of the feature head.
- The first configuration push attempt outside the dev shell was blocked by
  the installed Overcommit pre-push hook because ambient gems were missing; no
  remote ref changed. Re-running in `nix develop` succeeded and pushed
  `origin/2026-08-12-dns-secondary-zone-transfer-failure` at `52aaabcc`.
- GitHub Actions at superseded head `6248f607`:
  - API Migration Specs, RuboCop, i18n health, and every core/full API Specs
    topic shard passed;
  - API Specs run 31621832621 completed successfully;
  - full integration run 31621832711 was cancelled after the branch was
    rewritten to remove the supervisor compatibility filter;
  - the configuration repository has no push workflow applicable to this
    lock-only branch (its workflows are scheduled or event-specific).
- User changed the rollout strategy after this validation: remove the
  supervisor compatibility filter, deploy nodectld on every DNS node first,
  drain older queued events, then deploy the locking supervisor and run the
  cleanup migration.
- Removed the compatibility predicate and its two dedicated supervisor specs.
  The resulting supervisor spec has 6 examples and passes; RuboCop reports no
  offenses on the two touched API files.
- Folded the removal into the original unmerged vpsAdmin commit. The revised
  two-commit branch is `764dcaaec` followed by `28c01ee11`, and was force-pushed
  with lease.
- Regenerated the configuration pin from `origin/master` in a detached
  worktree. Commit `b1bfe70f` is a single generated commit directly changing
  `vpsadminServices` from production `95f8d9ca` to `28c01ee1`;
  `confctl inputs channel ls vpsadmin` resolves the expected revision.
- Mandatory standalone follow-up review of the revised design found no
  blocking code findings. It found one Important commit-message issue: the
  first commit body still claimed the removed supervisor compatibility filter.
- Amended the first commit body to require DNS-node nodectld deployment and
  queue draining before cleanup. This changed only commit hashes, not the
  reviewed tree. Final vpsAdmin commits are `0c9b3844d` and `7162ebac9`.
- Regenerated the exact configuration pin once more from `origin/master`.
  Final generated commit `60cc79d3` directly pins production `95f8d9ca` to
  final vpsAdmin head `7162ebac`; only `flake.lock` changes.
- Post-review long validation passed at the final source/configuration state:
  - `./test-runner.sh test dns/secondary-transfer-errors`: both examples and
    the 1-test scenario passed in 562.74 seconds;
  - `confctl build -y 'cz.vpsfree/vpsadmin/*'`: all 11 machines built;
  - `confctl build -y cz.vpsfree/containers/ns3`: built;
  - `confctl build -y cz.vpsfree/containers/ns4`: built.
- Force-pushed both unmerged feature branches with lease. Superseded active
  workflows were cancelled when their head no longer matched the branch.
- Current-head GitHub Actions at `7162ebac`:
  - API Migration Specs, RuboCop, i18n health, libnodectld Specs, API Specs,
    and full integration all completed successfully;
  - API Specs run 31634674759 and full integration run 31634674690 passed.
- Refetched vpsAdmin before integration. Upstream `master` had advanced by the
  unrelated `02449a1e0 webui: identify the dataset edit action` commit.
  Rebased the two feature commits conflict-free, producing final commits
  `35a7a9bf6` and `b3d63c005`.
- Re-ran all repository hooks after the rebase; Migration Specs, i18n,
  Nixfmt, PHP CS fixer, and RuboCop passed. A combined API RSpec invocation
  demonstrated the existing migration-spec connection isolation issue, so the
  affected groups were rerun in independent processes and passed:
  - libnodectld parser: 7 examples, 0 failures;
  - API supervisor: 6 examples, 0 failures;
  - cleanup migration: 6 examples, 0 failures.
- Force-pushed the rebased vpsAdmin feature branch with lease. Created a fresh
  detached worktree at current `origin/master`, fast-forwarded it to
  `b3d63c005`, and repeated the three focused spec groups there. An initial
  parallel API-spec attempt raced per-worktree gem-cache initialization; the
  parser passed and both API groups passed when rerun sequentially.
- Refetched vpsAdmin once more, confirmed upstream had not advanced, and
  fast-forwarded `origin/master` from `02449a1e0` to `b3d63c005`.
- Refetched vpsfree-cz-configuration. Upstream `master` had advanced to
  `8dd3d1a4`. From a fresh detached worktree, ran
  `confctl inputs channel set --commit vpsadmin vpsadmin b3d63c005bef30be52165cd80ef4978bbf0e72b2`.
  Generated commit `a8d8b5fe` changes only `flake.lock` and resolves
  `vpsadminServices` to `b3d63c00`.
- Force-pushed the regenerated configuration feature branch with lease. From
  the same fresh merge worktree, final configuration validation passed:
  - `confctl build -y 'cz.vpsfree/vpsadmin/*'`: all 11 machines built;
  - `confctl build -y cz.vpsfree/containers/ns3`: built;
  - `confctl build -y cz.vpsfree/containers/ns4`: built.
- Refetched configuration once more, confirmed upstream had not advanced, and
  fast-forwarded `origin/master` from `8dd3d1a4` to `a8d8b5fe`.
- Post-merge GitHub Actions at vpsAdmin `b3d63c005` already pass for API
  Migration Specs, RuboCop, i18n health, and libnodectld Specs. The API Specs
  and full CI workflows remain active on the same merged head and are being
  monitored; previous full validation at the pre-rebase equivalent source tree
  passed.

## Results

- Before the feature change, `parse_transfer_status` ignored only the literal
  status `success`; every other status was passed to `failed_event`.
- `up to date` does not match a known failure reason, producing exactly:
  - status: `failed`
  - reason code: `unknown`
  - reason: `The transfer failed`
  - message: `up to date`
- The direct parser reproduction produced:
  - a false failed/unknown event for
    `Transfer status: up to date`;
  - a successful event with serial `2026080601` for the following
    `Transfer completed: 0 messages, 1 records, 0 bytes, ...` line.
- BIND 9.20.26 returns `DNS_R_UPTODATE` when the primary serial is not newer
  than the secondary's requested serial. Its result text is `up to date`, and
  the zone refresh callback handles `DNS_R_UPTODATE` alongside successful
  refresh results. BIND then logs both the transfer status and completion
  summary seen in the excerpt.
- The API supervisor persists each normalized event as an independent history
  row. A later success can update the zone's latest transfer state, but it does
  not delete the earlier false failure row.
- The quoted `Reason code` / `Reason` / `Message` layout comes from the WebUI
  transfer-log row details, so it is displaying the false history event rather
  than interpreting BIND's completion line itself.
- The adjacent `SERVFAIL` refresh messages concern other zones and do not
  produce the quoted `message: up to date` values.

## Open questions

- None. The implementation and delivery choices are fixed in `plan.md`.

## Cleanup

- Both default branches are merged. No deployment, database migration, or
  other production write was made.
- Removed both initiative worktrees and both detached merge worktrees,
  including their local transient gem and configuration build caches. Feature
  branch refs are retained locally and remotely at the merged heads.
- The upstream BIND source inspection used a temporary clone under `/tmp`,
  outside the workspace.
