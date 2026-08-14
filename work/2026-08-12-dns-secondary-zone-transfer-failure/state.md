# 2026-08-12 DNS secondary transfer monitoring

## Repositories and worktrees

- workspace coordination repository
  - branch: shared `master`
  - base before this follow-up: `ca6ebc3b49ec9ab562de8672b77b44beeef8f10d`
  - dev-cluster harness commit:
    `1f3fb2d` (`devcluster: import managed notification templates conditionally`)
  - plan/state, two changed public KB candidate pages and final release
    manifests are recorded in the following tracking commit.

- `vpsadmin`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsadmin`
  - follow-up base: `5724cf262e858409e9142502dcb2a84a2940065f`
  - head: `f54494a084382ecb20e414c35800655f33ee5fc4`
  - six focused commits; clean and pushed after the unmerged history rewrite.
- `vpsfree-cz-configuration`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-cz-configuration`
  - base: `a8d8b5fe84c8a9990f5ff245361819e4132e8826`
  - head: `a00de5876f1b6b9e66854626311d572d63f73476`
  - monitor policy plus generated exact vpsAdmin pin; clean and pushed.
- `vpsfree-mail-templates`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-mail-templates`
  - base: `04921d75ab5321962b207bb380deff90906bd662`
  - head: `40b0de6eda8180a46d7bd06eec41424a92669e11`
  - bilingual readiness/recovery templates; clean and pushed.
- `vpsfree-kb-contracts`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-kb-contracts`
  - base: `5bf06beccdd29c333f04bb044a7610cee5ccda3d`
  - head: `1afc364a3c78ca747cf62fb18022284592f0eb8e`
  - exact final vpsAdmin pin and discovery inventory; clean and pushed.

The original `Transfer status: up to date` parser correction was already
merged, deployed and remains the production baseline. This follow-up branch is
not merged.

## Current design and implementation

- The durable plan is `plan.md`. The user approved the active-probe design,
  destructive transfer-history reset, WebUI separation and strict coordinated
  event-protocol cutover.
- The development cluster is disposable. It will be reset for deployment
  instead of preserving the prototype database state.
- The custom BIND package and both 9.18/9.20 source patches have been removed.
  Production and tests use the one stock BIND package selected by pinned
  nixpkgs.
- The BIND parser remains as passive diagnostic evidence. It correlates real
  transfer attempts, treats completion as accounting, distinguishes peers,
  preserves invalid-zone/TSIG/ACL/network/protocol failures and avoids known
  lifecycle/fallback/local false positives.
- nodectld now actively checks every current managed-secondary × configured
  user-primary path. It binds the secondary's real source address, uses the
  configured TSIG, reads SOA, sends signed TCP IXFR at the primary serial and
  escalates to bounded temporary AXFR validation only when needed.
- Probe defaults are hourly healthy checks, five-minute access/network failure
  retries, and hourly invalid-zone/protocol/stale retries. Nodes run two probes
  concurrently, with a 30-second cheap timeout, ten-minute AXFR timeout and a
  256 MiB AXFR output cap. Secrets and transferred contents are not published.
- Zone configuration and every event carry stable server-zone/transfer IDs and
  a UUID generation. The supervisor accepts only the current enabled external
  path. There is no runtime branch for old nodectld or supervisor envelopes.
- The rewritten core migration creates the path-state schema, assigns fresh
  generations and deletes every existing transfer log/cache pointer. Rollback
  cannot restore that history. A guarded operational task can repeat the same
  destructive reset and queue complete server-zone configuration refreshes.
- Per-path state records probe/BIND evidence, serials, continuity, precedence
  and ordering watermarks. Explicit primary failures become alertable after
  continuous 30-minute evidence; network failures need repeated observations
  spanning 24 hours. The continuity margin is 15 minutes for five-minute
  retries and 75 minutes for hourly content/protocol/stale retries.
- A cheap successful IXFR check clears access, TSIG, network, stale and similar
  readiness failures. Invalid content/protocol failures require a real accepted
  transfer or a fully validated probe AXFR.
- Routine successful probes update the durable ordering/state watermark but do
  not create permanent log rows. Failure/reason/eligibility transitions,
  recovery and meaningful BIND outcomes are retained.
- The API exposes transfer readiness per primary and per path. Name-server
  rows expose only the resulting BIND serving state (`serving`, `expired`,
  `not_loaded`, `unknown`) with serial/load/refresh/expiry timestamps.
- The WebUI now shows serving state under **Name servers** and a two-column,
  vertically expanded primary/server-check presentation under **Primary
  servers**. TSIG no longer forces a wide table. Logs identify BIND transfers,
  IXFR readiness probes and AXFR validation.
- Monitoring opens one zone incident only after a path reaches its grace
  period, keeps it open while any current path remains failed, suppresses empty
  repeat mail for young overlapping failures and sends closure only after all
  paths recover.
- Confirmed/closed Czech and English mail templates and complete guarded KB
  candidates describe readiness checks, retained BIND diagnostics, the fact
  that peer distribution can keep the zone available, and the alert delays.
- The real-BIND scenario now has two user primaries and two managed
  secondaries. Both primaries intentionally deny the second secondary, which
  must serve through its managed peer while both direct readiness paths show
  `refused`.

## Documentation artifacts

- Guarded production snapshot:
  `work/2026-08-12-dns-secondary-zone-transfer-failure/kb-sources/`
- Replacement plan:
  `work/2026-08-12-dns-secondary-zone-transfer-failure/kb-replacement-plan.yml`
- Current complete candidates:
  `work/2026-08-12-dns-secondary-zone-transfer-failure/kb-candidates-final/`
- Current review manifests:
  - `kb-release-final-cs.yml`
  - `kb-release-final-en.yml`
- Candidate build currently reports two changed pages, no new pages, no media
  and six guarded replacements. Production wikis have not been changed.
- The immutable source snapshot and regenerated complete-page candidate tree
  remain local verification inputs because the fetch also contains unrelated
  private/internal wiki pages. Only the two changed public pages and their
  checksummed release manifests are committed with this workspace record. The
  superseded intermediate candidate directory is not retained.
- The already-pushed `d30f744` commit body overstated artifact retention by
  saying that the complete source snapshot and candidate tree were preserved.
  This linear follow-up records the actual privacy boundary without rewriting
  shared workspace history: only the two public changed-page candidates and
  manifests are durable; complete source/candidate snapshots remain local and
  untracked.
- The final Czech/English manifests were regenerated from those complete-page
  candidates after the final KB-contract commit. Their page hashes match the
  candidate index (`dd87efcd...` Czech and `fdbbd25c...` English).
- The existing capture concepts do not include the secondary-zone status
  tables. New semantic paths bind zone creation, adding a primary, selecting
  its TSIG key and creating a TSIG key to the revised bilingual instructions.

## Verification completed for the rework

- `nix develop .#libnodectld -c bundle exec rspec`
  - 481 examples, 0 failures.
- Targeted RuboCop over all 46 modified/untracked API and libnodectld Ruby
  files, excluding generated `api/db/schema.rb`
  - no offenses.
- Core migration spec in its required isolated RSpec process
  - 3 examples, 0 failures.
- Ordinary model/task/transaction/supervisor API specs, separately from the
  migration process
  - 35 examples, 0 failures.
- The first combined migration+ordinary invocation failed after the migration
  helper left later examples on the schema-only `vpsadmin_test_migration`
  database. This known repository harness constraint is documented in
  `notes/vpsadmin/2026-07-29-migration-spec-isolation.md`; separate reruns are
  green.
- Configuration monitor spec
  - 3 examples, 0 failures.
- Configuration RuboCop
  - 2 files, no offenses.
- Configuration Nix formatting and `git diff --check`
  - clean.
- Mail ERB compilation with trim mode, both meta.rb syntax checks and mail
  repository `git diff --check`
  - clean.
- vpsAdmin WebUI PHP syntax, generated gettext/API locale health, Playwright JS
  syntax, Nix parse/format checks, CI selection test and transfer-test inventory
  evaluation are green.
- API DNS server-zone and transfer resource specs:
  - 82 examples, 0 failures.
- Final combined API suite covering the rewritten migration, path-state,
  supervisor, resources, monitoring lifecycle, DNS-server source-address
  propagation and reset/verifier tasks:
  - 168 examples, 0 failures.
- The final source-address lifecycle regressions prove that updating a DNS
  server address, rotating every affected generation, selectively resetting
  only paths of that address family and queuing all configuration refreshes is
  atomic. The simulated second-enqueue failure rolls the complete transaction
  back.
- Final supervisor and DNS reset-task specs after the new-envelope correction:
  - 19 examples, 0 failures.
- Every vpsAdmin commit passed the complete repository pre-commit hook set from
  `nix develop .#vpsadmin`. The first ambient-shell attempts were rejected for
  missing RuboCop/gettext/MariaDB; no commit was made until the full Nix-shell
  hooks passed.
- Every configuration commit passed its Nixfmt/RuboCop hooks. Its generated
  exact input pin was created by `confctl inputs channel set --commit`.
- Mail templates compile and dummy-render in both languages for confirmed and
  closed incidents.
- `vpsfree-kb-contracts`: `nix develop -c bin/check`
  - contract validation and all 32 unit runs passed;
  - 44 controls, 34 paths, 33 capture concepts and 3 semantic selectors;
  - annotation inventory: 83 bindings and 9 exceptions;
  - 59 concepts, 118 variants and all 118 PNGs validated.
- All four feature branches are clean, pushed and range `git diff --check`
  clean. No obsolete queued/in-progress GitHub Actions run remained to cancel;
  current-head CI was left running.
- Final exact pins use the complete vpsAdmin object ID
  `f54494a084382ecb20e414c35800655f33ee5fc4` in configuration and every KB
  contract declaration. An earlier local `confctl` attempt used an incorrect
  expansion of the abbreviated hash; GitHub rejected it before any lock or
  commit was changed.
- The first authorized real-BIND run failed during suite setup before any DNS
  assertion. The preserved runner log showed the API helper received literal
  `DNS_NODE2_ID`, `DNS_NODE2_NAME`, `DNS_NODE2_ADDR` and `ZONE_NAME` constants
  in a separate Ruby process, which raised `NameError`. The integration test
  now interpolates all five concrete values before dispatch. Nix parse/format,
  test discovery and CI selection are green; the correction is folded into the
  existing test commit, and configuration/KB exact pins were regenerated.
- The second authorized real-BIND run also stopped during suite setup before
  any DNS example. The dynamically inserted node 302 started nodectld, but the
  daemon remained in `get_node_config` RPC retries and never created
  `/run/nodectl/nodectld.sock`. A preserved debug run showed that the
  supervisor had enumerated active nodes before node 302 was inserted, so its
  RabbitMQ RPC/status/DNS queues had no consumers. Restarting the supervisor
  after creating node 302 created all four consumers; the next RPC attempt
  completed and nodectld initialized normally. The fixture now performs that
  reload before starting either DNS node. Nix parse/format, test discovery,
  CI selection (16 runs, 55 assertions), `git diff --check` and the complete
  vpsAdmin pre-commit hook set are green for this correction.
- Inspection of the older failed `API Specs (topic parallel)` workflow exposed
  a real coverage-manifest omission rather than an unrelated runner failure:
  `dns_server_zone_primary_transfer_state#index` was tested by the resource
  suite but absent from `covered_endpoints.yml`. The scope is now listed; the
  current targeted endpoint inventory run passes with 1 example and 0
  failures. The one-line correction is folded into the core path-state commit,
  all vpsAdmin hooks passed, and the downstream exact pins were regenerated.
- Configuration history now contains only the monitor-policy commit followed
  by one generated `confctl` exact-pin commit. The two superseded consecutive
  pin commits were dropped before regenerating the final pin.
- The first full run to reach product assertions proved that the real M:N
  matrix was already exactly correct, but exposed two integration-test contract
  errors. The matrix poll now compares all four rows with `match_array` and
  returns explicit success. The invalid-zone example now distinguishes the
  retained BIND diagnostic history from a newer current network timeout while
  the primary is stopped; it then restarts the primary and still requires the
  durable full-validation latch to recover specifically through `axfr_probe`.
  The old form waited the runner's full 15-minute bound for `invalid_zone` to
  remain the current failure and therefore never reached recovery. The run was
  stopped before its third example because that example inherited the primary
  and AXFR latch left by the failed second example. Nix parse/format, discovery,
  CI selection (16 runs, 55 assertions), diff-check and all hooks pass for the
  correction. The continuous-outage poll now also returns its final state
  snapshot explicitly instead of relying on an RSpec expectation object as the
  polling predicate. Both corrections are folded into the existing test
  commit. Exact downstream pins were regenerated and a focused follow-up
  review is in progress before the rerun.
- The standalone mandatory reviewer completed the substantive parser, probe,
  state/API, security, monitoring, UI, mail, KB, migration and deployment
  review. Its final focused pass verified all clean/pushed exact ranges and the
  integration-only polling correction, found no Blocking, Important or new
  Advisory items, and authorized the real-BIND, Playwright and exact-pinned
  configuration validations. The previously recorded synchronized-clock/NTP
  assumption remains operational.
- The next authorized real-BIND run reached all three examples. The retained
  invalid-zone diagnostic and validated-AXFR recovery example passed. The
  complete matrix and continuous-outage examples both failed only when their
  final serving checks referenced the Nix evaluation variable
  `dnsNode1.ipAddr` from runtime Ruby. The preserved result at
  `/tmp/os-test-runner/os-test-dns__secondary-transfer-errors-3ad00b8f`
  reports the same `NameError` for both examples and no DNS assertion failure.
  The fixture now serializes that address as `DNS_NODE1_ADDR`, matching the
  existing runtime node-2 address constant. Product code is unchanged; quick
  checks/hooks pass, exact pins are regenerated, and the clean heads are with
  the reviewer for the narrow rerun authorization.
- The following authorized run eliminated both runtime-scope failures. The
  invalid-zone/validated-AXFR example and the continuous crashed-primary
  example passed completely. The matrix example reached the final probe-proof
  assertion with the exact expected four path states and both secondaries
  serving, but its snapshot showed `last_attempt_kind: ixfr_probe` alongside
  retained `attempts: [transfer, transfer]`. That is the intended bounded-log
  policy: an identical refused probe advances the durable state watermark but
  does not add another diagnostic row. The fixture now asserts the watermark
  rather than expecting deduplicated history to grow. Product code is again
  unchanged; quick checks and hooks pass, pins are regenerated, and this
  one-line contract correction is in focused review before the final rerun.
- The focused reviewer approved that one-line bounded-history assertion with no
  findings. The final real-BIND run then passed all three examples in 871.54
  seconds: the exact two-primary/two-secondary readiness matrix and peer-served
  availability, retained invalid-zone evidence with validated AXFR recovery,
  and the simulated continuous 24-hour crashed-primary condition with both
  secondaries still serving followed by IXFR-probe recovery.

## Remaining work

1. User review of the deployed WebUI and seeded readiness states.
2. Stop/reset the disposable cluster when the review is complete.

## Development cluster review deployment

- Reset and started the dedicated
  `2026-08-12-dns-secondary-zone-transfer-failure` development cluster using
  the default bridge network. It is running and ready at
  `https://webui.aitherdev.int.vpsfree.cz/`.
- The deployed API and WebUI report the exact vpsAdmin revision
  `f54494a084382ecb20e414c35800655f33ee5fc4` with a clean source tree.
- The disposable cluster needed a top-level harness compatibility correction:
  revisions without the optional notifications module cannot define the
  notification dispatcher, Telegram receiver/webhook or webhook test service.
  Those declarations are now guarded by the same module-existence check as the
  managed template import. The focused mandatory review found no Blocking or
  Important issue and independently evaluated the module-present branch as
  well. Nix formatting/checking and `git diff --check` pass; top-level commit
  `73e234d3` is pushed on `master`.
- Seeded user `test-user1` with external secondary zone
  `transfer-review.aitherdev.test.` (zone ID 3). Its assigned managed secondary
  is loaded and serving serial `2026081401`; an actual TSIG-authenticated
  transfer from the working primary completed successfully, and both the SOA
  and `www` record are answerable from the secondary.
- The primary table has three paths for WebUI review:
  `172.16.106.61` succeeds through the configured TSIG key, while deliberately
  unreachable `172.16.106.250` and `172.16.106.251` both show network timeout
  failures. The successful path's latest observation is an IXFR probe with
  matching primary/secondary serials. The secondary remains healthy despite
  the two failed readiness paths.
- Probe timing was shortened only in the running nodectld process to populate
  the disposable review state promptly; restarting nodectld restores normal
  production intervals. The primary's zone stanza is likewise local to this
  disposable cluster and is not a repository or production configuration
  change.
- The cluster can be inspected with
  `dev-clusters/vpsadmin/bin/devcluster status 2026-08-12-dns-secondary-zone-transfer-failure`
  and removed after review with the matching `reset` command.

## Deployment constraints

- Pause monitoring and drain alert/mail work, then stop DNS-zone/API
  configuration writers. Keep old nodectld running while every old DNS
  configuration transaction is drained; make the new schema-independent
  verifier available without starting new services and require
  `bundle exec rake vpsadmin:dns:verify_configuration_drained` to report zero.
- Only after that configuration boundary, stop old nodectld on every DNS node,
  drain `dns_transfer_logs` with old supervisors, and stop all old consumers
  and monitoring-event writers. Deploy/migrate the new API, configuration and
  templates, then run
  `CONFIRM=1 bundle exec rake vpsadmin:dns:reset_primary_transfer_tracking`
  while writers and consumers remain stopped.
- Start stock-BIND/new-nodectld producers, verify every queued full
  configuration refresh and persisted probe envelope, then start only new
  consumers. Resume API writes and monitoring after the new event queue is
  drained and inspected. No mixed old/new configuration or event envelope is
  supported.
- Rollback uses the same empty producer/queue/consumer boundary in reverse and
  the guarded state/monitor reset tasks. Deleted transfer/incident history is
  not recoverable.
- Event admission compares DNS-node journal time with API database epochs;
  synchronized clocks/NTP are an operational requirement.
