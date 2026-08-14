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
  - head: `1c7d398ea8ca1a4e1172f19894d9c061ef866175`
  - six focused commits; clean and pushed after the unmerged history rewrite.
- `vpsfree-cz-configuration`
  - branch: `2026-08-12-dns-secondary-zone-transfer-failure`
  - worktree:
    `worktrees/2026-08-12-dns-secondary-zone-transfer-failure/vpsfree-cz-configuration`
  - base: `a8d8b5fe84c8a9990f5ff245361819e4132e8826`
  - head: `6a03e89343300d8c744c0689714c411a08a657fa`
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
  - head: `67f2b5dba510631d228e3a5cf6a6d589e420ee26`
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
  `1c7d398ea8ca1a4e1172f19894d9c061ef866175` in configuration and every KB
  contract declaration. An earlier local `confctl` attempt used an incorrect
  expansion of the abbreviated hash; GitHub rejected it before any lock or
  commit was changed.
- The standalone mandatory reviewer has completed the substantive parser,
  probe, state/API, security, monitoring, UI, mail, KB, migration and
  deployment review. All Blocking/Important findings have been resolved in
  the six focused vpsAdmin commits. Final long-test authorization is waiting
  only for this workspace record and exact downstream heads to be committed
  and handed back to the reviewer.

## Remaining work

1. Obtain the reviewer's final authorization for the committed exact ranges.
2. Run the long two-primary/two-secondary real-BIND test, Playwright WebUI test,
   exact-pinned configuration builds and final mail/KB validation.
3. Reset and deploy the dedicated development cluster over its default bridge
   network, seed a review zone, and hand the user the WebUI review details.

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
