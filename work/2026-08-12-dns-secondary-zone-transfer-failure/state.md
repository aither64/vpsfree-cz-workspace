# 2026-08-12-dns-secondary-zone-transfer-failure

## Repositories

- `vpsadmin`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsadmin`
  - base/head: `origin/master` at `925a85878`
    (`webui: update dependencies`)
  - feature head: `6248f607e850b347ed39d43822540ab61260aad4`
  - pushed to `origin/2026-08-12-dns-secondary-zone-transfer-failure`
- `vpsfree-cz-configuration`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-cz-configuration`
  - base: `origin/master` at
    `a301114d3e34412f201352a7f3e59d1556d2f561`
  - feature head: `52aaabcc4e98adb5e3e48a55aabeb12ea86b76eb`
    (`inputs: set vpsadminServices to 6248f607`)
  - pushed to `origin/2026-08-12-dns-secondary-zone-transfer-failure`

## Status

- Root cause confirmed and implementation authorized.
- User selected cleanup of existing false rows.
- User selected unmerged feature-branch delivery and an exact
  `vpsadminServices` feature pin in `vpsfree-cz-configuration`.
- User requires the supervisor compatibility code to include a removal TODO
  tied to full DNS-node rollout and draining older queued events.
- Both repository feature branches are committed and pushed. Local integration,
  configuration builds, and all completed current-head GitHub checks pass. The
  branches are ready for review; migration-triggered full integration run
  31621832711 remains in progress and is the only pending check.

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
- Implemented parser suppression, the marked supervisor rolling-upgrade guard,
  cleanup migration, focused specs, and DNS integration coverage.
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
  - the plan requires all API supervisors to run the guarded/locking revision
    before migration, then ns3/ns4 roll out after cleanup.
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
- Current-head GitHub Actions at `6248f607`:
  - API Migration Specs, RuboCop, i18n health, and every core/full API Specs
    topic shard passed;
  - API Specs run 31621832621 completed successfully;
  - full integration run 31621832711 remains in progress because the database
    migration intentionally selects the complete `tag=ci` suite;
  - the configuration repository has no push workflow applicable to this
    lock-only branch (its workflows are scheduled or event-specific).

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

- Both initiative worktrees are retained for review.
- No merge, deployment, or production write was made.
- The detached temporary configuration worktree used to regenerate the exact
  one-commit pin was removed; feature branch refs were retained.
- The upstream BIND source inspection used a temporary clone under `/tmp`,
  outside the workspace.
