# Shared incident escalation backend delivery

## Current published receipt (2026-10-31)

Final feature head **f60d41a453b1703e42de4341285bdc6ba339aff0** is published over
SSH on `2026-10-30-oomd-abuse-policy`. Independent ls-remote confirms this head
and unchanged remote default **ac10a62f1cb0fc890378ae83cdf18dd0e29f049a**.
Tree **f6656bd2c1d49f308c6cc1697ad3fb1c44d2be5c** exactly equals the focused
tested and hook-checked R1 fix head 3cde6709. The original independent e9 review
is complete across all four lanes, with only Important R1; its accepted narrow
fix passed direct verification under mandatory-review step 9. See
[shared-review.md](shared-review.md) and
[shared-timestamp-remediation.md](shared-timestamp-remediation.md).

Final cleaned series:

1. `89a303e6396882ea7981a8077dba05a4ce9861ac`: backend plus accepted R1.
2. `f3e58cd3e5bf19e588ca40ef44b3b1da696137c7`: unchanged legacy patch.
3. `f60d41a453b1703e42de4341285bdc6ba339aff0`: unchanged isolated testDB patch.

Only the four accepted R1 paths differ from the original e9 review. Schema,
migration and flake inputs are unchanged; stable patch IDs prove legacy/testenv
equivalence. Original e9 and tested 3cde refs remain preserved. Normal Nix rebase
exited 0 with hooks enabled; no successful checks were repeated for history.
The tree is tracked-clean with only the prior PHPUnit cache untracked.

Receipts: `shared-r1-final-history.json`, `shared-reviewed-final-range-diff.txt`,
`shared-r1-consolidation-range-diff.txt`, `shared-r1-consolidation.log`,
`shared-r1-push.log`, `shared-r1-publication-{before,after}.txt` and
`shared-r1-legacy-equivalence.txt`. Capture-comparison exited 0 for ac10..f60d.
The lead and owner3 received authoritative publication proof directly.

Automatic exact-head workflows: API topic specs 41185457084, migrations
41185457125, integration CI 41185457135, PHPUnit 41185457117, RuboCop
41185457100, libnodectld 41185457104 and i18n 41185457388. Initial and fresh
nonterminal run queries are retained as shared-r1-ci-*.json; no superseded
same-branch nonterminal run remained to cancel. The actual push-diff selector
chooses full `tag=ci` due to the additive migration
(`shared-r1-push-selection.txt`). Five smaller workflows have succeeded; API
topics and hosted integration are being observed by one fresh catalog Luna/low
watcher. No scenario pass is inferred from the overall Run tests step.

Read-only local fallback planning is complete in
[shared-f60-capacity-plan.md](shared-f60-capacity-plan.md). No final images or
guests were realized; the source-copy-only evaluation allocation is accounted
there. Local heavy work remains held while hosted equivalent scenarios can
produce proof. No merge, deployment or lifecycle operation is authorized.

The earlier receipts below preserve the original e9 review and pre-remediation
history; this section supersedes their then-current publication/hold status.

Current contract: [implementation-contract.md](implementation-contract.md).
The backend, API, migration, real rendering and adjacent behavior are complete.
All intended source is committed and quick checks/hooks pass. Source is stable
for the lead-assigned retained independent reviewer; this is not review clearance.
No merge, push, deployment, guest/browser run or heavy image allocation is
authorized at this checkpoint.

## Final committed source and history

Fresh SSH fetch exited 0. The remote default and final merge-base are unchanged:
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`. Feature publication remains held;
the remote feature branch still points at the preserved old source
`4d72e3e754fd47b598de1e54e05b3c5d26c62200`.

Final local head: **e9a6530b0e18f2f58b013b3a470f3d6991d79876**.

1. `ffbe4cc5234a294cd2ca9ffc49f492183c08ce8d`: complete backend/API/schema,
   fallbacks, shared source selectors and verification scenarios/docs.
2. `8a6309553d0de3ee2535ffce7af5e3960eb9caaf`: owner1's legacy UI package,
   unchanged exact handoff bytes and rename deletions.
3. `e9a6530b0e18f2f58b013b3a470f3d6991d79876`: isolated testDB compatibility
   and its documentation, unchanged patch from the previously reviewed commit.

Tree **931bbd2c80c51c2c5db3e2eaa7bdc393e6005728** is exactly equal to the
hook-checked preconsolidation tree at
`857b6147829261bf44f02f6efb51b684a7a687d3`, retained under
`refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-shared-before-consolidation`.
Consolidation resolved only the browser file's historical ownership: its generic
replacement is in the backend commit, and the obsolete old filename introduced
by the original legacy child is absent. All rebase/amend operations exited;
the feature branch is restored and only `webui/.phpunit.cache/` is untracked.

Normal hooks passed for both source packages and the necessary consolidation
amend. Logs: `shared-backend-hooks.log`, `shared-legacy-hooks.log`,
`shared-consolidation-resolved.log`. The initial pre-rebase signature refusal
occurred before mutation; unchanged hook configuration was signed in the declared
Nix environment, without bypass. The temporarily isolated owned legacy form was
trap-restored before staging; source manifests verify exact bytes after hooks.

Receipts:

- `shared-final-history.json`: complete final series, source/input lock graph,
  tree identity, status and testenv patch identity.
- `shared-old-new-range-diff.txt`: preserved old published three-commit range
  versus final shared feature. This is a substantive approved rework, not claimed
  patch equivalence to the old narrow feature.
- `shared-consolidation-range-diff.txt`: five hook-checked development commits
  versus the cleaned three-commit series; final tree equality is independently
  asserted.
- `shared-final-diffstat.txt`, `shared-final-migrations.txt`,
  `shared-final-remote-before-review.txt`.
- `shared-{backend,legacy}-source-{sha256,equivalence}.txt`: exact checked source
  scope and successful post-consolidation verification, including legacy handoff.

The testenv stable patch ID remains
`a298c7e6db36ff22c400a04735a9f4b4228b6663`. There are no dependency/input pin
changes or repeated pin streams in this branch. Superseded OOM-only feature
iterations and their draft migration names were folded, not retained as separate
commits. The preserved review refs retain provenance outside the final series.

## Verification

| Check | Authoritative result | Evidence |
| --- | --- | --- |
| New affected app batch | 48 examples, 0 failures, exit 0 | shared-affected-specs.log/json/exit |
| Separate migration | 2 examples, 0 failures, exit 0 | shared-migration-specs.log/json/exit |
| Six adjacent files | 49 examples, 0 failures/pending, seed 50834, 258.779s RSpec / 280s shell, exit 0 | shared-adjacent-corrected.log/json/exit |
| Actual site rendering | 9 examples, 0 failures, seed 6895, 23.69s / 44s shell, exit 0 | shared-site-renders.log/json/exit; shared-site-render-spec.rb |
| API locale | Full-mode update and health exit 0 | shared-locales-normalized.log |
| Scoped Ruby lint | 26 files, no offenses; migration/spec correspondence passes | shared-lint-final.log |
| API topics | 13 identical full/core topics; 421 eligible files exactly once | shared-topic-coverage.log |
| CI selector | 16 tests / 55 assertions, 0 failures/errors | shared-selector-parse.log |
| Nix/Node parse | Scoped Nix format/parse and browser Node syntax exit 0 | shared-selector-parse.log; shared-browser-parse.log |
| Runtime selection | Existing tagged listing includes alerts/incident-escalation and webui#incident-escalation | shared-runtime-selection.log |
| Legacy owner package | PHP 120/832 full, 13/92 focused; locale/lint/formatter pass | legacy-incident-rework.md |

The actual site rendering uses exact template source
bf32762126f21fb7fc825fac25b5b45d075a2681 and calls the current backend mail chain
for specific/generic warning/stopped pairs in EN and CS, then requested-CS to
actual-EN fallback. It proves selection, real body rendering, type label,
recipient timezone, source-specific guidance and generic separation. It does
not prove SMTP delivery or a physical stop. The repository specs separately
prove disabled preference/suppression, specific render/translation failures
without generic fallback and current limits/permission after manual start.

Both app batches and migration ran in separate disposable MariaDB processes.
Actual local settings: MariaDB 11.4.12, REPEATABLE-READ,
innodb_snapshot_isolation=OFF. The isolated test helper compatibility change is
retained as its separate focused commit; production DB configuration is untouched.
Root hook dependencies restored only 37,791,909 bytes. No image/guest/browser
build was launched.

The initial adjacent command accidentally included a trailing `.` and expanded
beyond the assigned six files, including migrations. That run is invalid evidence:
677 seconds, native 143 after exact owned process reconciliation, empty JSON,
owned processes gone and disposable DB port 39699 closed. Its log/exit remain
shared-adjacent-specs.*. The corrected command has exactly six file operands;
there was no overlapping duplicate run. Runtime success is attributed only to
shared-adjacent-corrected.*.

## Contracts and privacy

Only production rule oomd is registered. Its source adapter preserves the daemon
protocol and supplies backend-only provenance. Generic ingest! is the deliberate
registered-type arrival boundary; registration alone enrolls no existing API,
nodectl or mail route. A synthetic manual-qualified rule without source_key
exercises actual arrival through durable warning preparation, selected-type
counts/limits/mail and isolation. Registry-union scheduler discovery includes
outstanding action/transfer recovery without replaying historical decisions.

Per-type policy rows own overrides/warning state. Physical stop permission,
ownership epoch, cooldown and outstanding stop exclusion are shared per VPS.
API selected-type summaries and filters use registry qualification. Qualified
member history also uses registry qualification/current owner epoch; unqualified
manual history retains existing visibility. Synthetic manual privacy tests cover
both Index and Show and administrator audit.

The existing IncidentReport New/Create intentional-empty synchronous receipt and
savepoint-isolated ordinary-mail preparation remain. Writes require a registered
selector plus a setting, synchronously validate/audit final values, and reject
mixed VPS properties before effects. Existing independent OomReport and daemon
codenames remain unchanged. Four templates and their registered variables are
implemented; specific definition absence alone permits generic fallback.

## Schema and pending long checks

Migration 20261030180000 was never merged, released, deployed or externally
persisted. Only disposable local/hosted spec databases used its drafts. The old
published head is preserved at
refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-before-shared-incident-rework.
The final series contains one additive AddIncidentEscalation migration and its
core-only schema dump, no transitional draft or existence guards.

The old exact-head hosted foundation failures were diagnosed as committed quota,
status/resource and session contamination from the new concurrency fixture.
Original order/IDs/assertions reproduced the problem, and minimal fixture/session
cleanup passed the same selected core 3/0 and full 7/0 controls; receipts are
ci-contamination-{negative,positive}-{core,full}.*. This is not final full-suite
acceptance. The final source still needs exact-head hosted full/core CI after
review/publication, plus real stop/mail retry/manual-start/chown/data-retention
alerts/incident-escalation and legacy webui#incident-escalation scenarios.
Physical evidence from old schema/source is not reused. No induced resource
abuse is needed; the authored scenario uses the established daemon-event source.

The durable project behavior/settings/ownership/failure/upgrade explanation is
[docs/incident-escalation.md](../../worktrees/2026-10-30-oomd-abuse-policy/vpsadmin/docs/incident-escalation.md), linked from the owning docs index.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Post-review bounded runtime plan

After independent review and capacity release, the bounded native commands are
`./test-runner.sh test alerts/incident-escalation` and
`./test-runner.sh test 'webui#incident-escalation'`. Prefer equivalent successful
exact-source hosted execution over duplicate local runtime. Preserve the first
failure's native logs/effects and diagnose before any rerun; no blind retry.
The alert scenario asserts real stop completion/autostart effect, independent
mail failure/retry with one stop identity, manual start/new events within cooldown,
confirmed ownership epoch reset with retained cooldown/member-history privacy,
and data sentinel integrity before/after start and transfer. It has not run on
the revised schema. Fresh supported capacity admission, coordinated with owner3,
must precede images/guests; the 20 GiB reserve and unexpected-kernel escalation
rules remain. No physical deployment, default integration or lifecycle action is
authorized.

## Exact quick-check scope

All API commands enter the declared `.#api` shell. App commands used
`VPSADMIN_PLUGINS=none`; locale generation used the default full plugin mode.
Native JSON/log/exit names above bind these commands to their actual result.

```sh
VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec \
  spec/api/resources/incident_escalation_spec.rb \
  spec/models/incident_escalation_spec.rb \
  spec/models/incident_escalation_registry_spec.rb \
  spec/models/transaction_chains/vps/incident_escalation_mail_spec.rb \
  spec/models/incident_escalation_concurrency_spec.rb \
  spec/models/cluster_resource_package_spec.rb

VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec \
  --options /dev/null --require ./spec/migration_helper.rb \
  spec/migrations/20261030180000_add_incident_escalation_spec.rb

VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec \
  spec/api/resources/incident_report_spec.rb \
  spec/models/transaction_chains/incident_report/new_spec.rb \
  spec/models/transaction_chains/incident_report/send_spec.rb \
  spec/supervisor/node/vps_events_spec.rb \
  spec/models/tasks/incident_report_spec.rb \
  spec/models/incident_escalation_registry_spec.rb
```

Each app/migration command additionally used the documentation and JSON
formatters with explicit output paths, without a trailing directory operand.
The earlier shared-core-specs batch had 42 examples/4 failures; its seven
VpsIncidentSummary examples passed, including batch/filter parity and every
pending/failed/fatal/resolved transfer state plus confirmed Chown virtual epoch.
Their summary implementation inputs were unchanged by the affected corrections;
this successful scope is reused without claiming that original batch passed.

The real-site check used the single absolute operand
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/shared-site-render-spec.rb`.
No cross-repository runtime dependency or permanent test framework was added.

Actual final-source automatic CI selection is recorded in
`shared-final-ci-selection.json`: full `tag=ci`, triggered by the additive
migration. The successful static tagged listing contains both renamed scenarios;
this proves selection intent, not an actual CI run or pass. Hosted final-head
full/core and integration acceptance remain pending review/publication.

## Retained R1 correction after the original review head

The original final-review head e9a6530b remains pinned unchanged. Its accepted
narrow timestamp correction is retained separately at
3cde6709ba57ea7e5809bcccbf10938494d2bc31, tree
f6656bd2c1d49f308c6cc1697ad3fb1c44d2be5c. See
[shared-timestamp-remediation.md](shared-timestamp-remediation.md) for the actual
API negative 2/2 to positive 9/0 proof, four-file lint, exact patch and successful
normal hooks. The migration/input graph and other source packages are unchanged.
The current working tree has only the prior PHPUnit cache untracked. All owned
local operations exited. Consolidation, publication and heavy runtime remain
held pending the lead's release of the original independent review report.

### Hosted foundation milestone

Exact f60d API run 41185457084 foundation jobs passed with native artifacts:
full 1,469 examples / 0 failures / 3 pending, 285.323 seconds; core 1,469 /
0 / 52 pending, 248.843 seconds. Results and actual Ruby/Bundler/RSpec/effective
lockfile hashes are retained in ci-41185457084-attempt1/. Both completed job logs
(shared-f60-foundation-{full,core}-job.log) show actual MariaDB 11.8.6,
innodb_snapshot_isolation OFF and REPEATABLE-READ. This closes the previously
failed foundation scope on the published source, not the still-running whole
API/topic aggregate or required physical/browser scenarios.

The initial CI utility returned before long-run completion. Parent briefly owned
read-only gh watchers, then reconciled only those local clients (both exit 143,
remote workflows untouched) and launched a fresh standalone catalog Luna/low
completion watcher with explicit full-access/never policy. Its operation brief,
event stream and final receipt are shared-f60-ci-completion-{brief.md,events.jsonl,result.md};
parent native handle 16318. It owns the two existing long run IDs and actual
scenario/artifact observation; parent does not poll in parallel. Full/core VPS
jobs also passed (18m51s/13m4s). Whole API aggregate and physical/browser scenario
acceptance remain pending; no local duplicate or further source work is admitted.

### API aggregate terminal milestone

Owned observer's terminal status receipt shared-f60-api-completion-status.json
reports exact f60d run 41185457084 completed success at 09:05:07 UTC: all 27 jobs
succeeded, including 26 full/core topic jobs and topic-coverage aggregate at
09:05:06. The local downloaded topic artifacts currently contain only 25 unique
result JSONs; rspec-results-core-dns.json is missing. Their verified sum is
9,217 examples / 0 failures / 412 pending. The watcher's prose total of 26 files /
9,456 examples is not accepted as complete native artifact proof until this gap
is resolved; no workflow rerun is needed or authorized by an artifact gap.

The same observer's integration snapshot at 09:30:34 UTC still shows run
41185457135 in Run tests, started 08:41:05 (49m29s elapsed). Neither required
alerts/browser scenario has a reported terminal result or artifact. Remaining
duration cannot be derived from GitHub step state. The next observable boundary
is native Run tests completion/evaluation/artifact publication. The existing
completion watcher remains owner; no parallel remote query, local duplicate or
cancellation accompanies this milestone.

### Completed API native artifact reconciliation

The missing completed core-DNS artifact was downloaded successfully without
rerunning a workflow. All 26 unique topic result JSONs and 26 environment JSONs
are now present and verified. Exact native totals: full 4,775 examples / 0
failures / 8 pending; core 4,775 / 0 / 404 pending; combined 9,550 / 0 / 412
pending, zero outside-example errors. This supersedes both the earlier partial
25-file total and the watcher's unsupported 9,456 total. Each mode has one
consistent effective generated Gemfile.lock hash across its 13 topics.
`shared-f60-api-native-summary.json` records the deduplicated totals, mode
boundaries and hashes. The 27/27 terminal job/aggregate success remains unchanged.

The integration observer's 09:47:44 UTC snapshot still reports Run tests on the
same exact-head run, 66m39s after its 08:41:05 start. Required physical/browser
outcomes and artifacts remain unavailable; duration alone proves no failure.
The existing watcher/native16318 remains active; no duplicate query/run,
source change or local heavy allocation accompanies this update.

### Progress visibility limit

One local read of the sole observer at 10:07:41 UTC exposes Run tests active
since 08:41:05 (86m36s). Its last concrete exposed workflow advancement is
selection/preview and Prepare test state success at 08:41:05. Job-status JSON
contains no current test/build, last per-test advancement, or dependency/resource
wait. Successful observer status commands establish only that provider access
works. They do not prove runner advancement or a hang.

The existing workflow tees per-test output to the runner test.log/job console.
Its full-log artifact upload follows failure/cancellation; evaluation and summary
follow Run tests exit. No corresponding scenario artifact is present in the
owned observer receipts yet. A provider-permitted live job-console/log read may
offer finer progress, but the current observer has not retrieved one. The parent
has not made a duplicate provider query or disrupted the observer merely for
status. Exact required scenario outcomes and remaining duration remain unknown;
Run tests exit/evaluation/artifact publication is the next exposed native boundary.
