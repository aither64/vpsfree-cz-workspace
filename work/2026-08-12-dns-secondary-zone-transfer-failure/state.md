# 2026-08-12 DNS secondary transfer monitoring

## Repositories and worktrees

- workspace coordination repository
  - branch: shared `master`
  - base before the concurrency follow-up:
    `d70e1a093b4848351f701ea44407487159a60dab`
  - dev-cluster harness commit:
    `1f3fb2d` (`devcluster: import managed notification templates conditionally`)
  - plan/state, two changed public KB candidate pages and final release
    manifests are recorded in the following tracking commit.

- `vpsadmin`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsadmin`
  - final rebase base: `8aa4ad30a` (`origin/master`)
  - head: `461a3c4bae767b2e3c6dcd91d9d501f76f410841`
  - eight focused commits; clean and pushed after the unmerged history rewrite.
- `vpsfree-cz-configuration`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-cz-configuration`
  - base: `f19c6a70d720383ccdac083731756d5ff1101d64`
  - head: `00edfbf6ddc76392822052229ccf2ecf1e832541`
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
  - base: `4189c7661c8dcefb2cb9f9610fe85515e87c9e6f`
  - head: `342e680c3f7790597e395f59fdc4677ebab0fc62`
  - exact final vpsAdmin pin and discovery inventory; clean and pushed.

The original `Transfer status: up to date` parser correction was already
merged, deployed and remains the production baseline. This follow-up branch is
not merged.

## Current design and implementation

- The durable plan is `plan.md`. The user approved the active-probe design,
  destructive transfer-history reset, WebUI separation and strict coordinated
  event-protocol cutover.
- The development cluster is disposable. It was reset and redeployed from the
  final exact revision instead of preserving the prototype database state.
- The custom BIND package and both 9.18/9.20 source patches have been removed.
  Production and tests use the one stock BIND package selected by pinned
  nixpkgs.
- The BIND parser remains as passive diagnostic evidence. It correlates real
  transfer attempts, treats completion as accounting, distinguishes peers,
  preserves invalid-zone/TSIG/ACL/network/protocol failures and avoids known
  lifecycle/fallback/local false positives.
- nodectld now actively checks every current managed-secondary × configured
  user-primary path. It binds the secondary's real source address, uses the
  configured TSIG when present, reads SOA, sends a TCP IXFR at the primary
  serial and escalates to bounded temporary AXFR validation only when needed.
- nodectld no longer fetches or validates user-controlled DNS data itself. It
  continuously schedules current paths and publishes results, while each check
  runs in a one-shot transient systemd service with `DynamicUser=yes`, no
  capabilities, a private temporary directory, protected/inaccessible BIND and
  nodectld paths, bounded memory/process/runtime/output and network access only
  to the selected primary. The worker receives no RabbitMQ/database credentials
  or trusted path identity and receives optional TSIG material only on stdin.
- New zones and primaries are scheduled with deterministic jitter of at most 60
  seconds. Removing a primary or zone drops pending work, stops its running
  transient unit and discards any obsolete result before publication. Existing
  API identity/generation/epoch admission remains defence in depth.
- Probe defaults are hourly healthy checks, five-minute access/network failure
  retries, and hourly invalid-zone/protocol/stale retries. Nodes run five probes
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
- Links in all globally styled `failed`/`error` table rows now use a dark,
  underlined normal/visited style and black hover/focus style on the retained
  red background; the rule is not specific to the DNS table.
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
- Unprivileged probe follow-up checks:
  - scheduler/runner/worker specs: 44 examples, 0 failures;
  - worker package builds with both `nodectld` and
    `vpsadmin-dns-transfer-probe` executables;
  - final DNS integration derivation evaluates as
    `/nix/store/3xd2r5wkpppi8k21iv7yz26fyma04lis-os-test-dns-secondary-transfer-errors.json.drv`;
  - Nix parse/format, targeted RuboCop, Ruby syntax and repository
    `git diff --check` pass;
  - WebUI stylesheet regression: 1 test, 2 assertions, 0 failures;
  - complete vpsAdmin pre-commit hooks pass for both follow-up commits.
- Runtime-churn coverage now removes/re-adds a primary and deletes the complete
  zone without restarting either nodectld. Unit coverage proves ≤60-second new
  path scheduling, pending deletion, running cancellation and post-delete
  result suppression; the expanded real-DNS scenario is pending review-gated
  execution.
- The final visual-only CSS change affects no registered screenshot concept:
  the contract has no secondary-zone-status capture. The exact vpsAdmin pin was
  still regenerated in every contract declaration, and `nix develop -c
  bin/check` remains green with 44 controls, 34 paths, 33 captures, 83
  annotation bindings, 9 exceptions and all 118 existing PNGs valid.
- All four feature branches are clean, pushed and range `git diff --check`
  clean. No obsolete queued/in-progress GitHub Actions run remained to cancel;
  current-head CI was left running.
- The previous reviewed exact pins used the complete vpsAdmin object ID
  `38ad10fbdd00e7de07b5ac6b5261ec3d4f541d46` in configuration and every KB
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

1. Let current-head main CI finish and inspect any failure rather than blindly
   rerunning it.
2. Merge/deploy the coordinated feature set only with the queue and writer
   barriers below.
3. Promote the prepared KB manifests only after separate production approval.

## Unprivileged probe follow-up

- User review confirmed that probes currently run from root nodectld and asked
  for untrusted DNS transfer data to be processed in standalone unprivileged
  processes.
- Chosen design: nodectld retains scheduling, current `DnsConfig`, the durable
  AXFR latch and RabbitMQ publication; each path check runs as a one-shot,
  hardened transient systemd service with `DynamicUser=yes`. One immutable job
  is sent over stdin and one bounded result is accepted over stdout.
- Runtime contract: newly created paths are deterministically staggered within
  60 seconds; removed paths and zones cancel pending/running work; stale
  generation results are dropped locally and rejected again by the API.
- Log decision: keep probe transitions combined with real BIND diagnostics and
  retain both for 365 days. Identical probe retries and routine healthy probes
  remain nonpersistent; meaningful BIND outcomes remain fully retained.
- WebUI decision: apply accessible failed/error-row link colors globally while
  preserving the existing red status background.
- The first fresh-context review blocked long validation on a partially typed
  worker job, post-exit tempfile output caps, user values in child argv,
  AF_UNIX access and missing execution-level isolation coverage. The rewritten
  isolation commit now validates a closed bounded job/result schema and
  canonical reasons, streams/caps output while the unit runs, feeds dig through
  stdin and BIND validation through a private `named-checkconf -z` config,
  removes AF_UNIX, bounds cancellation state and adds real subprocess plus
  causal NixOS isolation/cancellation checks.
- The review follow-up found one remaining prelaunch lifecycle leak: a
  `ThreadError`, or path removal before `runner.run`, could retain a prepared
  runner registration and consume a concurrency slot until restart. The
  coordinator now explicitly releases prepared registrations from both paths,
  retries local thread-allocation failures, and covers both races. The focused
  suite passes 44 examples and targeted RuboCop reports no offenses; all
  repository hooks passed before the correction was folded into the isolation
  commit.
- The fresh reviewer verified the corrected committed ranges and independently
  reran the focused suite (44 examples, 0 failures). It reported no Blocking,
  Important or Advisory findings and authorized the long real-DNS, Playwright,
  exact-pinned configuration and dev-cluster validations. Current-head CI
  remains a residual gate before integration or merge acceptance.
- The selected primary address intentionally remains visible as the
  `IPAddressAllow` systemd property because this is how the root coordinator
  installs the destination filter. No zone name, source address, query or TSIG
  secret appears in root/child argv or unit names.
- The worker JSON is package-internal: scheduler, executable and NixOS
  hardening settings are deployed and rolled back as one nodectld revision.
  This follow-up changes neither the RabbitMQ event envelope nor the database
  schema or durable AXFR-latch format. Transient units are tied to
  `nodectld.service` and keep no durable worker state.
- Before the lifecycle cleanup, implementation was committed and pushed at
  vpsAdmin
  `38ad10fbdd00e7de07b5ac6b5261ec3d4f541d46`, configuration
  `6dde84e0da0e0614c5e049e7825c9bf5ac45cf83` and KB contracts
  `6e3935a4e12c383556109412b882a1bbda75c2b5`.
- The first post-isolation real-DNS run reached the complete readiness matrix.
  Three paths had the expected passive BIND evidence, while the path that
  depended solely on its active probe remained unknown. Extracted guest
  journal evidence showed every audit-wrapped transient unit exiting before
  the packaged worker because the test accepted only specific access-denial
  errno values. The isolation contract permits any failed syscall (or blocked
  connection timeout) and still fails if access succeeds, so the audit now
  rescues `SystemCallError`/`IO::TimeoutError` before running the real worker.
- The same run exposed a separate test-only race: the invalid-zone diagnostic
  remained retained as required, but an asynchronous probe could replace the
  current failed state before it was sampled. The scenario now asserts the
  durable diagnostic and eventual validated `axfr_probe` recovery, without
  requiring a routine deduplicated success log row. The healthy interval is
  60 seconds in this scenario to keep that state observable and reduce probe
  churn.
- Nix parse/format, CI selection (16 runs, 55 assertions), range diff-check and
  all mandatory vpsAdmin hooks pass after folding the two corrections into
  their logical integration/isolation commits. Configuration and KB pins were
  regenerated through their required workflows and all worktrees are clean.
- The fresh standalone review of the committed test-only delta reported no
  Blocking, Important or Advisory findings and authorized the long real-DNS,
  WebUI and exact-pinned configuration validations. It independently verified
  the isolation audit's causal active-only path, the validated-AXFR recovery
  assertion, the eight-commit split and every exact downstream pin. The long
  rerun remains the definitive systemd/kernel boundary proof; current-head CI
  is still a merge gate.
- An unrelated OOM kill interrupted a later heavy Nix evaluation while the old
  disposable review cluster was still consuming memory. No worktree changes
  were lost. The bridge cluster is now stopped, leaving approximately 88 GiB
  available before the long retry; it will be reset for the final deployment.
- The next real-DNS run proved the full four-path readiness matrix, the
  retained invalid-zone diagnostic followed by validated AXFR recovery, and
  the two-observation continuous-outage rule. The matrix's refused path used a
  valid initial `axfr_probe` because no local serial was available yet, so its
  assertion now accepts either active probe kind instead of incorrectly
  requiring IXFR.
- Runtime deletion exposed a product lifecycle bug: transaction confirmations
  raw-delete `DnsZoneTransfer` and `DnsServerZone`, bypassing their ActiveRecord
  dependent callbacks. Deleting a primary or whole zone therefore left
  `DnsServerZonePrimaryTransferState` rows behind. The destroy chains now
  register those rows as explicit `just_destroy` confirmations under the
  server-zone lock. Focused specs cover primary, managed-secondary and
  whole-zone deletion; successful confirmation removes the rows while generic
  confirmation behavior continues to preserve them on failure or rollback.
- Focused API specs for all three destroy chains pass (6 examples), targeted
  RuboCop and Nix parse/format checks pass, and the integration scenario now
  asserts that whole-zone removal leaves no path state. All vpsAdmin hooks and
  KB contract checks pass. The correction is folded into the original logical
  commits, the eight-commit series is clean and pushed, and configuration and
  KB contracts carry the exact new vpsAdmin revision. A fresh mandatory review
  remains required before another long run.
- Current-head migration, RuboCop, WebUI PHPUnit, i18n and libnodectld GitHub
  workflows are green; the main CI and topic-parallel API specs are still
  running. Superseded old-head CI run `31810932973` was cancelled without
  touching any current-head run.
- The fresh lifecycle review withheld long-test authorization on one race and
  one lock-order issue. A managed-secondary event could pass the initial lookup
  before `confirm_destroy`, wait for the server-zone lock, and recreate state
  after confirmation registration. Primary deletion also locked the transfer
  before server zones, inverse to event consumption.
- Event admission now scopes server zones to `existing`, repeats that check
  after taking the server-zone lock, and safely ignores a row deleted between
  lookup and locking. Primary deletion locks ordered server zones before
  marking the transfer for destruction. Deterministic supervisor regressions
  cover both the post-lookup `confirm_destroy` window and row disappearance;
  the focused supervisor/destroy suite passes 22 examples and targeted RuboCop
  reports no offenses. All mandatory hooks and KB contract checks pass. The
  fixes are folded into the path-state commit, the clean eight-commit vpsAdmin
  series is pushed, and configuration plus KB carry the exact new revision. A
  second fresh review is required; long validation remains paused.
- The second fresh lifecycle review accepted the destroy-time admission and
  lock-order corrections, but found a separate pending-create rollback race.
  `confirm_create` endpoints are intentionally visible to probes, while a later
  failed creation is removed by raw confirmation SQL. That SQL bypasses model
  dependencies, so probe state/history admitted before rollback could become
  orphaned.
- The unmerged schema now makes this integrity boundary explicit with foreign
  keys: deleting a server-zone endpoint cascades its path states and transfer
  logs; deleting a primary cascades its path states and nulls the primary link
  on retained logs; deleting a retained log nulls the state's optional latest-
  log link. Deterministic supervisor regressions cover both pending-create
  rollback shapes and prove clean recreation. The migration spec checks all
  five delete actions. The migration suite passes 3 examples, the combined
  supervisor/destroy suite passes 27 examples, and targeted RuboCop reports no
  offenses. CI selection passes 16 runs/55 assertions, Nix parsing and Nixfmt
  are clean, and all mandatory vpsAdmin hooks pass. The correction is folded
  into the core path-state commit and pushed; configuration and all five KB
  declarations carry the exact new object ID. Long validation remains paused
  pending a fresh committed-range review.
- That fresh review accepted the database cascade/nullification graph and all
  surrounding lifecycle, deployment, API, probe-isolation, WebUI, mail, KB and
  commit-boundary decisions. It found one independent parser blocker: BIND can
  reuse a pointer after a missed terminal journal line, and the stale attempt
  could attribute a new failure to the old zone, primary and generation.
- Correlation now drops a pointer-keyed attempt before processing any line when
  its normalized zone or address changes. Every `connected` line starts a new
  logical attempt even for the same path, so generation/transfer snapshots and
  failure flags cannot leak across reuse. Regressions cover both different-path
  and same-path/configuration-churn reuse. The focused parser suite passes 30
  examples and targeted RuboCop is clean. All mandatory hooks pass, the fix is
  folded into parser commit 1, the clean eight-commit branch is pushed, and the
  generated configuration pin plus all five KB declarations use the exact new
  object ID. A final confirmation review is required; long validation remains
  paused.
- The final pointer confirmation review reported no Blocking, Important or
  Advisory findings. It independently passed the 30-example parser suite and
  3-example migration suite and authorized the long real-BIND, Playwright and
  exact-pinned configuration validations at vpsAdmin
  `7496cdd69fa6e04044a6331453606f20a870ec87`.
- The authorized expanded real-BIND run completed all four examples in 939.58
  seconds. Invalid-zone evidence with validated AXFR recovery, the simulated
  continuous crashed-primary condition and runtime add/remove/delete without a
  nodectld restart all passed. The matrix reached its final assertion with all
  four path states correct and both secondaries serving. Its refused path was
  last updated by a legitimate passive BIND transfer after an active probe, so
  the test-only requirement that the latest attempt kind be a probe failed even
  though retained history contained the expected real `transfer`/`refused`
  diagnostic. The complete result is preserved at
  `/tmp/os-test-runner/os-test-dns__secondary-transfer-errors-3ad00b8f`.
- The matrix now checks that the retained diagnostic includes a real BIND
  transfer with reason `refused`, without imposing a race-dependent latest
  source. Runtime-churn coverage separately and causally waits for isolated
  active-probe units on both DNS nodes. Relative to the fully reviewed tree,
  the final vpsAdmin tree changes only those two assertions. Nix parsing,
  Nixfmt, CI selection (16 runs/55 assertions), range diff-check and all
  mandatory hooks pass. Configuration and all five KB declarations are pinned
  exactly to `8fa969886bba1a95efe9edf399bcc1d213129f4d`; a fresh focused review
  is required before the definitive rerun.
- The fresh focused review reported no Blocking, Important or Advisory
  findings and independently confirmed that the two-line matrix correction did
  not hide any product change. The definitive real-BIND rerun then passed all
  four examples and the complete script in 944.72 seconds: the M:N matrix in
  162.28 seconds, invalid-zone/validated-AXFR recovery in 22.28 seconds,
  continuous crashed-primary behavior in 72.05 seconds and runtime
  reconciliation/cancellation in 109.81 seconds.
- The targeted `webui#networking-dns` browser run completed three of four
  Playwright tests and exposed a test-only locator error in the changed DNS
  user-flow test. The fixture renders the failed summary row—with the zone link
  whose global contrast is under test—followed by a separate details row that
  contains `reason_code: refused` but intentionally has no link. The test tried
  to find a single failed row containing both. The page snapshot proves the
  failed IXFR-probe summary and refused detail were both rendered correctly;
  services stayed healthy. The result, screenshot, error context and trace are
  preserved under `/tmp/os-test-runner/os-test-webui-fd1a3b33`.
- The locator now selects the actual failed summary row by its `IXFR readiness
  probe` source; the table-level assertion still verifies the filtered
  `refused` reason independently. Relative to the previous reviewed head, this
  changes one Playwright line and no product code. JavaScript syntax,
  diff-check, CI selection (16 runs/55 assertions), all mandatory vpsAdmin
  hooks and the complete KB contract check pass. Configuration and every KB
  declaration now pin exact vpsAdmin
  `39e2753d8e4decc3a0961738741bdfaba4c44b65`. A fresh focused review is
  required before rerunning Playwright.
- The fresh focused locator review reported no Blocking, Important or Advisory
  findings and authorized the browser rerun plus exact-pinned configuration
  builds. The definitive `webui#networking-dns` run then passed its changed
  browser scenario in 229.7 seconds and the complete 1/1 test in 808.67
  seconds.
- Exact-pinned configuration builds completed successfully for
  `cz.vpsfree/vpsadmin/int.api1` (generation
  `2026-08-14--20-56-07`), `cz.vpsfree/vpsadmin/int.webui1`
  (`2026-08-14--20-57-42`) and `cz.vpsfree/containers/ns3`
  (`2026-08-14--20-59-03`).
- Current-head WebUI PHPUnit and i18n GitHub workflows are green. Main CI is
  still running; the immediately preceding product-equivalent head is green
  for API specs, RuboCop, libnodectld, WebUI and i18n, and the final head
  changes only the reviewed Playwright locator.

## Development cluster review deployment

- The dedicated
  `2026-08-12-dns-secondary-zone-transfer-failure` development cluster using
  the default bridge network was reset and freshly deployed after all long
  validation. It is ready and running from exact vpsAdmin revision
  `39e2753d8e4decc3a0961738741bdfaba4c44b65`.
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
  failures. The successful path has current validated probe evidence. The
  secondary remains healthy despite the two failed readiness paths.
- The fixture populated using normal production probe timing; no runtime
  interval override was needed. Its retained history contains the real
  successful BIND transfer and the two failure transitions, while routine
  successful checks remain state watermarks rather than noisy permanent log
  rows. The primary's zone stanza is local to this disposable cluster and is
  not a repository or production configuration change.
- Review access is `https://webui.aitherdev.int.vpsfree.cz/`, user
  `test-user1`, password `testUser1Password`. The zone is
  `transfer-review.aitherdev.test.` (ID 3).
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

## 2026-08-17 probe-concurrency follow-up

- The user deferred transfer-count quotas for a later initiative and requested
  that the node-wide default probe concurrency increase from two to five.
- The vpsAdmin feature series was rebased onto current `origin/master` and the
  new value was folded into the original probe and DNS integration-test
  commits. The default, scheduler fixtures and real-DNS scenario all use five;
  explicit node configuration can still override it.
- Compatibility is unchanged: there is no schema, API, Rabbit envelope or
  persisted-state change. During a rolling deployment, old nodes run two
  probes and updated nodes run five until convergence. Rollback restores the
  old default without data work.
- Focused verification before review:
  - scheduler spec: 14 examples, 0 failures;
  - RuboCop: 4 files, no offenses;
  - Nix parse/format, CI selection (16 runs/55 assertions), test inventory and
    range `git diff --check`: green;
  - complete vpsAdmin pre-commit and commit-message hooks: green from the root
    Nix shell. The ambient-shell attempt was rejected for missing declared
    tools and made no commit.
- `vpsfree-cz-configuration` was rebased onto current `origin/master`. It has
  the monitor-policy commit plus one generated `confctl` commit pinning exact
  vpsAdmin `461a3c4bae767b2e3c6dcd91d9d501f76f410841`.
- All five KB-contract revision declarations pin that same exact vpsAdmin
  commit. `nix develop -c bin/check` passes: 46 controls, 38 paths, 35 capture
  concepts, 98 annotation bindings, 60 inventory concepts/120 variants/120
  PNGs and 47 unit runs with no failures. Public candidate content and release
  manifest hashes did not change, so the release manifests were not rewritten.
- The existing development-cluster review fixture still runs the previous
  exact application head. This follow-up has not redeployed it.
- The mandatory fresh standalone review found no Blocking, Important or
  Advisory issues and authorized the long real-DNS scenario and exact-pinned
  configuration builds. It independently reran the scheduler spec with 14
  examples and no failures.
- Residual capacity note: the integration matrix has only two paths per DNS
  node and does not saturate five workers. Five simultaneous production AXFR
  validations can reserve up to 3.75 GiB of cgroup memory, approximately
  2.5 GiB of transfer/temporary storage and 80 tasks. Production resource
  pressure should be monitored; transfer-count quotas remain deferred.
- Long validation for the five-probe default is authorized and pending.
