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
  - follow-up base: `origin/master` at `5724cf262e858409e9142502dcb2a84a2940065f`
  - follow-up feature head: `be0fa305f7d1d84c6dc3d7dca6abeee04906c983`
    - `ba76f23ad nodectld: correlate BIND transfer attempts`
    - `9c489d937 bind: log successful SOA refreshes`
    - `86efcf695 dns: track direct primary transfer paths`
    - `b64318eab monitoring: reset DNS transfer incident history`
    - `bb960396b webui: show direct DNS transfer status`
    - `be0fa305f tests: cover DNS primary path recovery`
  - follow-up branch pushed; not merged
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
  - follow-up feature head: `21f799aa015c82d661c9bb59e81a088f888ae56e`
    - `7639285f vpsadmin: monitor DNS primary transfer paths`
    - `bc8d48b1 dns: use vpsAdmin BIND telemetry package`
    - `21f799aa inputs: set vpsadminServices to be0fa305`
  - follow-up branch pushed; not merged
- `vpsfree-mail-templates`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-mail-templates`
  - base: `origin/master` at `04921d7`
  - feature head: `c4288b56a426385bb41ec66ed9aa57d14cf8d590`
    (`dns: report failed direct primary paths`)
  - branch pushed; not merged
- `vpsfree-kb-contracts`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-kb-contracts`
  - base: `origin/master` at `5bf06be`
  - feature head: `768ab2941e42c1033f1c295543f747bf17d2e6ee`
    - `66e1799 Pin DNS primary transfer status revision`
    - `768ab29 Track DNS documentation paragraph shifts`
  - branch pushed; not merged

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
- The vpsAdmin feature worktree was recreated at the merged feature head for a
  source-level audit of all BIND transfer messages. The audit is complete and
  shows that the parser is not yet a reliable user-health signal. No parser or
  API code was changed during this investigation.
- The user approved the follow-up implementation plan. It separates served-zone
  health from per-user-primary path health, keeps one alert incident per zone,
  delays network alerts for 24 hours, and preserves the July rolling-reboot fix
  by allowing same-primary up-to-date NOTIFY to clear network failures only.
- The retained vpsAdmin branch was fast-forwarded to current `origin/master` at
  `5724cf262`. Worktrees for mail templates and KB contracts were created; the
  existing configuration worktree was restored after its known checkout-hook
  exit 78.
- The final follow-up implementation is committed and pushed in all four
  affected project repositories. Quick verification and repository hooks pass.
  The mandatory standalone review reports no remaining Blocking or Important
  findings, and all authorized long validation passes on the final heads.
- Review findings were folded into the logical commits. The final deployment
  contract uses an all-at-once BIND/nodectld/consumer protocol boundary, a
  fresh tracking epoch, repeatable legacy-log and monitor-history cleanup, and
  explicit queue and journal-cursor barriers for rollback and re-upgrade.
- Final guarded Czech and English KB candidates are in
  `kb-candidates-final/`, with release manifests `kb-release-cs.yml` and
  `kb-release-en.yml`. Their code contract
  pins exact vpsAdmin head `be0fa305`. Production KB was not changed.
- The mandatory standalone review of the final clean, pushed commit ranges
  reports no remaining Blocking or Important findings. After the long tests,
  the reviewer re-audited the test-only vpsAdmin delta and the regenerated
  configuration and KB pins, found no new significant issues, and closed the
  review. Its residual Advisory is the operational NTP/clock-synchronization
  dependency already recorded in `plan.md`.

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
- Post-merge GitHub Actions at vpsAdmin `b3d63c005` pass for API Migration
  Specs, RuboCop, i18n health, libnodectld Specs, and the complete 27-job API
  Specs matrix (run 31675738739). At the user's direction, stopped waiting for
  the separate full CI workflow, which remained in progress; previous full
  validation at the pre-rebase equivalent source tree passed.
- Recreated the retained vpsAdmin feature branch worktree at
  `b3d63c005bef30be52165cd80ef4978bbf0e72b2` for the requested follow-up.
- Audited the exact deployed BIND 9.20.26 source from Nix source archive
  `/nix/store/jgibfp4pxrnlck46l7rbyd0j3yhan9vp-bind-9.20.26.tar.xz` and its
  upstream system tests. Compared the relevant behavior with BIND 9.18.50.
- Reviewed `lib/dns/xfrin.c`, `lib/dns/zone.c`, `lib/isc/result.c`, transfer
  system tests, the complete libnodectld parser, its specs, API persistence,
  BIND statistics ingestion, and the DNS integration test's injected logs.
- Ran representative BIND 9.20 messages through
  `NodeCtld::DnsTransferLog#parse_message` in the libnodectld Nix shell. The
  sequence `failed while receiving responses: FORMERR`, `Transfer status:
  FORMERR`, and a nonempty `Transfer completed` summary produced two failed
  events followed by a false successful event with the rejected serial.
- The same parser probe confirmed false failures for `Transfer status: IXFR
  failed`, `Transfer status: shutting down`, a secondary MX/SRV `has no address
  records` warning, and failure to load the secondary's local cached zone file.
- Implemented a bounded stateful libnodectld parser for BIND 9.18 and 9.20.
  It correlates pointer or zone/primary attempts, never treats completion
  accounting as success, accepts only `transferred serial` as transfer success,
  treats ambiguous xfrin `up to date` as refresh evidence, suppresses IXFR
  fallback, and classifies user-primary, network, local, lifecycle, and unknown
  failures.
- Added `dns_server_zone_primary_transfer_states` and event classification to
  the API. The supervisor tracks each current `(secondary, configured primary)`
  path, preserves explicit-failure precedence, resets grace time when network
  failure becomes explicit, and changes network failure to unknown on a
  same-primary current NOTIFY. Peer events never mutate direct-primary state.
- Added batched aggregate status to `DnsZoneTransfer`, user log authorization
  and filtering, alert-eligibility scopes, pruning preservation, aggressive
  legacy log cleanup, and a monitoring-plugin migration that removes old
  `DnsServerZone` incidents for the zone-level monitor.
- Updated the WebUI, generated Czech gettext catalogs, Playwright fixture, and
  DNS integration scenario. The Primary servers table now shows direct status,
  failed/participating server counts, last attempt, and a primary-filtered log
  link.
- Updated the production monitor to query one precomputed eligible-failure count
  per external DNS zone. It closes incidents for disabled zones and uses the
  model's 30-minute primary and 24-hour network thresholds.
- Updated and rendered both notification languages. Confirmed alerts group
  failures by primary and list every affected secondary; closed alerts now own
  a `DnsZone` object.
- Focused checks passed:
  - libnodectld: 16 examples, 0 failures; targeted RuboCop clean;
  - supervisor: 14 examples, 0 failures;
  - path model: 2 examples, 0 failures;
  - core cleanup migration: 5 examples, 0 failures;
  - monitoring cleanup migration: 2 examples, 0 failures;
  - aggregate/visibility/filter API examples: 4 examples, 0 failures;
  - DNS task specs: 6 examples, 0 failures;
  - API and WebUI i18n health, PHP syntax, JS syntax, Nix parse/format, full
    integration derivation evaluation, test discovery, and CI selection pass.
- Repository hooks passed for every vpsAdmin and configuration commit. The first
  vpsAdmin API commit attempt was correctly blocked by three migration-spec
  RuboCop offenses; the lines were fixed and the complete hook set passed.
  The first configuration functional commit attempt similarly caught two
  RuboCop offenses; both were fixed before commit.
- Pushed vpsAdmin follow-up head `9526f88db` and generated the exact production
  configuration pin with
  `confctl inputs channel set --commit vpsadmin vpsadmin 9526f88d...`.
  `confctl inputs channel ls vpsadmin` resolves `vpsadminServices` to
  `9526f88d`. A first push outside the dev shell was blocked by the mandatory
  pre-push hook's missing ambient gems; the dev-shell push succeeded.
- Pinned vpsfree-kb-contracts to `9526f88db` in the flake, capture, navigation,
  and article contracts. The first `bin/check` exposed the undocumented article
  provenance pin; it was updated and the canonical workflow was corrected.
  The complete contract then passed: 40 controls, 30 paths, 33 capture concepts,
  one article, all unit checks, and 118 PNG variants.
- `bin/kb-contract-fetch` fetched 116 Czech and 70 English production pages.
  `bin/kb-contract-build` prepared two local candidates documenting direct
  status and alert delays. The independent discovery inventory was updated for
  the shifted TSIG paragraphs, and `check-kb-annotations.rb` then passed with
  75 bindings and 9 exceptions. Guarded one-page Czech and English release
  manifests were generated. No staging or production write was made.

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
- BIND's `xfrin_destroy()` logs both `Transfer status` and `Transfer completed`
  for every terminal result. Completion is transfer accounting, not evidence
  of success; its counters and serial can be nonzero after malformed data or a
  rejected database.
- BIND converts an incremental-transfer processing error to `IXFR failed` and
  immediately retries with AXFR. Its own tests deliberately avoid treating any
  transfer status as final because of this fallback.
- Shutdown, forced retransfer, and reconfiguration can emit `shutting down` or
  `operation canceled`; these are infrastructure lifecycle events, not failures
  caused by the zone owner or primary.
- Refresh messages are per-primary attempts. BIND may retry without EDNS, use
  TCP, start AXFR despite an SOA-query refusal, or try another primary. A later
  equal-serial response is successful but has no matching INFO-level success
  line, so a parsed first-primary failure can remain falsely current.
- Secondary MX/SRV `has no address records` messages are nonfatal consistency
  warnings in BIND. Failure to load a secondary's master file refers to its
  local cached copy and triggers automatic refresh. Both are currently
  mislabeled as a rejected customer zone.
- BIND can reject a received database with `transferred zone has <n> SOA
  records` or `transferred zone has no NS records`, yet the transfer context
  still reports status success and a completion summary. The parser ignores
  the rejection and emits success.
- `transferred serial <serial>` is the reliable accepted-transfer message: BIND
  emits it only after the received database passes SOA and NS checks. Existing
  BIND status ingestion separately provides loaded, serial, refresh, and expiry
  timestamps suitable for health/staleness gating.
- Minimum safe remediation is to stop using `Transfer completed` as success,
  use accepted `transferred serial` as transfer success, use equal/older-serial
  refresh evidence only to recover network reachability state, ignore IXFR
  fallback and lifecycle cancellation, and remove nonfatal/local cache patterns
  from user failures. Correct notification also requires correlating attempts,
  preserving each configured primary path independently, and delaying alerts.

## Current implementation and review

- The user accepted patching BIND to restore positive passive recovery
  evidence. Minimal version-specific patches add an INFO message to the
  successful equal-serial SOA refresh branch in BIND 9.18 and 9.20 without
  changing protocol or refresh behavior. The configuration selects
  `pkgs.bind-vpsadmin` for DNS servers. GNU patch dry runs with fuzz disabled
  pass against official BIND 9.18.50 and the exact deployed BIND 9.20.26 source.
  The exact deployed 9.20.26 derivation builds successfully at
  `/nix/store/3z3iy9r677xbfhl06rd8ljsi67rf8kjg-bind-9.20.26`; its companion
  `dnsutils` and `host` outputs are also present. The exact 9.18.50
  compatibility derivation builds at
  `/nix/store/vs7gkqc1c4h3yby17bp1pjrh482q5qli-bind-9.18.50`. The respective
  `libdns-9.18.50.so` and `libdns-9.20.26.so` outputs both contain the patched
  `confirmed current serial` message.
- Network failures become alertable only when failed observations span 24
  hours. A patched equal-serial refresh, the existing older-primary-serial
  response, or same-primary current NOTIFY clears only a network failure to
  unknown. Ambiguous xfrin `up to date` is refresh evidence and cannot clear an
  explicit error. Routine refresh/NOTIFY and peer-positive events do not create
  durable transfer-log rows, but associated direct-primary observations advance
  the per-path ordering watermark so out-of-order consumers cannot restore an
  older failure.
- The review also found and the working tree now addresses: BIND network-down
  and malformed-response result families, context-sensitive `unexpected error`,
  partial-transfer EOF, the 120-minute maximum transfer window, per-enable and
  per-path event boundaries, and queued events received while a zone is
  disabled. It additionally led to filtering stale/unassociated successes from
  the user API, resetting path state across enable/source epochs, closing
  monitor incidents after source changes, and a repeatable rollback/re-upgrade
  monitor-history cleanup task.
- Follow-up verification currently passed: libnodectld parser 27 examples and
  API supervisor/model/task 36 examples. The core migration passes 5 examples.
  An earlier accidental combined run
  included an isolated migration spec with normal API specs and switched the
  shared test connection to the migration database; the groups are therefore
  run separately, as required by the migration-spec harness.
- KB replacement text, generated candidates, manifests, hashes, and exact code
  pins were rebuilt for the final policy. `nix develop -c bin/check` passes at
  vpsAdmin pin `be0fa305`; the final two-page candidate build reports two
  replacements with no annotations or media changes, and annotation checking
  passes with 75 bindings and 9 exceptions.
- The first post-review long-validation pass built all 11 exact-pinned
  vpsAdmin machines plus `ns3` and `ns4` successfully. It also exposed two
  integration-test defects and one ambiguous selector rather than product
  failures:
  - after the first refused refresh, BIND's process-local unreachable cache
    suppressed the test's immediate second `rndc refresh`, so the simulated
    24-hour outage never received its required second observation;
  - synthetic assertions still expected routine peer/refresh successes to add
    durable log rows, contrary to the finalized state-watermark design;
  - the Playwright primary-row selector matched the DNS-server status row first
    because both rows contained the same primary IP address.
  The DNS scenario now restarts BIND to clear only its local unreachable cache
  before the real repeated outage attempt, backdates the tracking/path epoch
  consistently with the simulated 25-hour failure, disables automatic test
  NOTIFY so equal-serial refresh telemetry is proven directly, and uses
  persisted local-event barriers when asserting that routine positive events
  add no rows. The Playwright assertion is scoped through the primary-specific
  transfer-log link.
- Final long validation on the committed and exactly pinned heads passes:
  - `./test-runner.sh test dns/secondary-transfer-errors`: all six examples and
    the one real-BIND scenario passed in 764.74 seconds;
  - `./test-runner.sh test 'webui#networking-dns'`: all four Playwright cases
    and the focused browser scenario passed in 1,130.76 seconds;
  - `confctl build -y 'cz.vpsfree/vpsadmin/*'`: all 11 machines built from
    exact vpsAdmin revision `be0fa305`;
  - `confctl build -y cz.vpsfree/containers/ns3` and the corresponding `ns4`
    command both built with the patched BIND package;
  - final KB contract checks pass with 40 controls, 75 annotation bindings,
    118 screenshot variants, and all 32 executable/unit test runs green.
- The prepared KB candidates can be staged for review after code review. Any
  production KB promotion requires separate direct user approval.

## Cleanup

- The earlier minimal fix is merged in both original default branches. The new
  four-repository follow-up remains on pushed feature branches. No deployment,
  database migration, staging KB write, or production write was made.
- Removed both original initiative worktrees and both detached merge worktrees,
  including their local transient gem and configuration build caches. Feature
  branch refs are retained locally and remotely at the merged heads. The
  vpsAdmin feature worktree was later recreated for the requested BIND audit
  and remains available for follow-up implementation.
- The upstream BIND source inspection used a temporary clone under `/tmp`,
  outside the workspace.

## Dev cluster WebUI review

- On 2026-08-13, deployed exact vpsAdmin revision `be0fa305` to the bridge-mode
  dev cluster `2026-08-12-dns-secondary-zone-transfer-failure`. The running
  review topology contains the services VM plus the primary and secondary DNS
  VMs; no compute node is needed for the DNS WebUI review.
- The shared dev-cluster harness currently contains unrelated notification-test
  integration that requires API options from another unmerged vpsAdmin branch.
  To avoid changing that concurrent work, this deployment uses an isolated
  compatibility copy of the harness from workspace revision `39750da` at
  `dev-clusters/.vpsadmin-dns-transfer-compat`. Mail capture is disabled in
  this review cluster; the DNS API, WebUI, and both DNS VMs are healthy.
- Created user-owned external zone `secondary-transfer-review.example.` for
  `test-user1` on `ns-public.aitherdev.int.vpsfree.cz`, with four configured
  primary paths for visual review:
  - `198.51.100.210`: successful, 0 / 1 failed servers;
  - `198.51.100.211`: explicit `REFUSED`, 1 / 1 failed servers;
  - `198.51.100.212`: continuous network failure older than 24 hours,
    1 / 1 failed servers;
  - `198.51.100.213`: unknown, 0 / 1 failed servers.
- Verified an OAuth login as `test-user1`, fetched the exact zone detail page,
  and found all four expected status rows, counts, timestamps, and filtered
  transfer-log links. The WebUI endpoint returned HTTP 200 at
  `https://webui.aitherdev.int.vpsfree.cz/`. The cluster remains running for
  user review; no production service or data was changed.
