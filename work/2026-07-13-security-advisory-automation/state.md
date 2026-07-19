# 2026-07-13-security-advisory-automation

## Current status

### Resumable per-Node history backfill (2026-07-19)

- The verified development session and existing vpsAdmin feature worktree are
  being reused. The worktree is clean at published feature head `96c622c13`.
- The requested refactor is confined to the existing unpublished kernel and
  system-state migrations, models, reconstruction operations/tasks/specs, and
  the configuration deployment runbook. No production operation is
  authorized.
- The current implementation materializes full historical `NodeStatus` rows
  and holds the Node lock throughout each scan. It has a kernel checkpoint but
  no system-state completion marker, no per-Node/task selection, no combined
  resume/status command, and no periodic progress reporting. These are the
  implementation gaps being addressed.
- The vpsAdmin implementation now has an unpublished private system-history
  checkpoint in the existing system-state migration, unlocked ID/scalar batch
  scans, three bounded retries, short savepoint-backed Node-lock writes,
  component resume/force behavior, combined and status tasks, and a reusable
  progress reporter.
- The configuration deployment runbook now requires a combined backfill and
  `complete` status immediately before each gradual Node deployment. It keeps
  inactive historical Nodes as separate off-peak work.
- Focused operation/model/task specs pass: 37 examples, 0 failures. They cover
  batch-boundary transitions/gaps, exact/live cutoffs, current ownership,
  idempotency, force, partial failure, atomic rollback, concurrent unlocked
  scans, bounded retry, scalar-only SQL, task selection/status, and rate/ETA
  formatting.
- Focused migration specs pass: 4 examples, 0 failures, including checkpoint
  uniqueness and rollback.
- Targeted RuboCop passes for all changed API Ruby/spec files: 13 files, no
  offenses. `tests/ci-selection-test.rb` passes with 16 runs and 55 assertions.
- The four Rake task descriptions were verified against the isolated test
  database. Plain task listing without a database and starting the database
  helper outside the Nix API shell both failed during application/tool loading;
  the working setup is recorded in
  `notes/vpsadmin/2026-07-19-rake-task-list-test-db.md`.
- The complete non-migration API RSpec suite passed in eight isolated local
  shards: 3,969 examples, no failures, and nine expected plugin-mode pending
  examples. Full API RuboCop inspected 1,442 files without offenses. The
  repository Overcommit gate passes migration specs, WebUI/API i18n, Nixfmt,
  RuboCop, and PHP CS Fixer.
- The initial broad vpsAdmin implementation commit was `a72e23de5`; the
  mandatory review required it to be split and folded into the unpublished
  owning commits. The configuration rollout runbook is committed separately
  as `71c78b5c`; its hooks passed. Upstream vpsAdmin `master` remains
  `81f7460c5`, so no upstream rebase was required before review.
- Long supervisor/dev-cluster integration and downstream exact pin updates
  remain gated on the mandatory standalone review. No production migration,
  backfill, deployment, or KB write has been performed.
- The mandatory standalone review blocked integration with two findings. A
  forced system rerun after an empty completion checkpoint could classify all
  later live states as reconstructed and delete them. The review also requires
  the broad vpsAdmin follow-up to be folded into the unpublished owning kernel,
  system-schema, and system-reconstruction commits, retaining only the combined
  task/progress interface as a focused new commit.
- Important review findings require terminal retry exhaustion to be reported as
  failure instead of a nonexistent next retry, and reconstruction output to
  expose the selected Node's component timestamps and processed boundaries.
  The original request says to retry up to three times; the plan will clarify
  that this means one initial scan plus at most three retries. Integration and
  downstream pins remain paused until remediation passes the same review gate.
- The blocking live-state issue is fixed. When an empty completed backfill is
  followed by live states, a forced rerun now treats the first existing state
  as the live boundary and preserves every live transition and row identity.
  A regression covers empty completion, two later live runs, and force.
- The final unpublished history now folds the checkpoint migration into
  `369c0032d`, its generated table into the owning schema refresh
  `5915750a3`, unlocked kernel reconstruction into `87880e2e4`, and unlocked
  system reconstruction into `e69af7d20`. The focused combined task and
  progress interface is `c7e4b8785`, which is also the current vpsAdmin head.
  Owning commit messages describe the final short-lock design. A recovery ref
  retains the pre-remediation `a72e23de5` tree.
- Exhaustion after one initial scan plus three retries now emits a terminal
  `failed` progress record rather than claiming another retry. Reconstruction
  prints each selected Node's overall/component state, completion timestamps,
  source-status IDs, and observation bounds, including on partial failure.
- Post-remediation focused RSpec passes 40 examples with no failures (seed
  62122), targeted RuboCop passes 12 files without offenses, migration and all
  commit-time Overcommit hooks pass, and every final commit message is within
  80 columns. The same standalone reviewer is performing the required focused
  remediation pass before integration can start.
- The focused re-review cleared the live-state, retry, history-split, and
  processed/partial output findings, then found that a fully complete no-op run
  returned before printing the selected Node's checkpoint details. The no-op
  path now prints the same final status line before returning. Its focused task
  spec passes 11 examples (seed 25282), focused RuboCop passes two files, and
  all amend-time hooks pass. Integration remains paused for the same reviewer's
  final confirmation.
- The same standalone reviewer confirmed the no-op correction at final head
  `c7e4b87854fe27619dd5450f93a1e5c4d4f8e4d1` with no Blocking, Important, or
  Advisory findings. It independently passed the 11-example task spec and
  opened the supervisor/dev-cluster integration gate. Accepted residual risks
  are production-scale scan/short-lock performance, the explicit immutable
  `NodeStatus` assumption, and real concurrent supervisor ingestion, which the
  next integration step targets.
- `nix develop -c rake vpsadmin:gems` completed before the cluster rebuild but
  also refreshed the unrelated unconstrained `concurrent-ruby` dependency from
  1.3.7 to 1.3.8 in three package bundles. That dependency-only drift was not
  accepted into this feature; the six generated files were restored to their
  committed content and the worktree is clean. The reusable caveat is recorded
  in `notes/vpsadmin/2026-07-19-vpsadmin-gems-unrelated-updates.md`.
- The dedicated single-Node bridge cluster was reset because the unpublished
  system-state migration changed. Graceful shutdown reached the tool's known
  timeout fallback, then only this initiative's state was removed. A clean
  `--topology single --network bridge` start rebuilt and deployed exact
  vpsAdmin head `c7e4b87854fe27619dd5450f93a1e5c4d4f8e4d1`; API, supervisor,
  nodectld, DNS, WebUI, and seeded pool setup reached ready state.
- The repository's long `supervisor/runtime-ingestion` scenario passed all 10
  examples and the complete test in 682.78 seconds. It covered legacy Node
  status, VPS status, storage, expansion, network monitor/accounting, mounts,
  VPS events, and oomd incident ingestion.
- The development database then received 20,000 synthetic immutable legacy
  statuses before the live/exact boundary. The combined per-Node task ran with
  `NODE_ID=101 BATCH_SIZE=1`. During its unlocked kernel scan, nodectld was
  restarted after making the current status eligible for logging; the real
  supervisor appended status ID `32776`. The first 20,000-row scan detected the
  changed watermark and retried once, then completed in 23.6 seconds at 846.7
  rows/second. System reconstruction completed its 20,000-row scan in 34.9
  seconds at 573.5 rows/second.
- Both durable checkpoints are complete with source IDs `9..20008` and
  observations `2026-07-01T00:00:01Z..2026-07-01T05:33:20Z`. Kernel history
  has three public events, exactly one current event, and that current event is
  exact `node_report`. System history collapsed to two states and exactly one
  current state; the original live row retained identity/current ownership and
  absorbed the equal reconstructed run. The supervisor status table contains
  20,003 rows with the concurrent row as its maximum.
- A repeated `NODE_ID=101 reconstruct_history` run invoked no component,
  reported `No pending combined history backfills`, printed both completion
  timestamps/source/observation boundaries, and kept before/after totals at one
  complete Node. This also confirms later legacy samples do not revert durable
  completion.
- The reviewed vpsAdmin branch was force-pushed with an explicit lease from
  expected remote head `96c622c13356c31db275e2050e5b724cbcb9739f` to final
  head `c7e4b87854fe27619dd5450f93a1e5c4d4f8e4d1`. The superseded self-hosted
  workflow was cancelled. All nine non-integration current-head workflows pass,
  including all 26 API topic-parallel jobs. The migration path intentionally
  makes the CI selector choose the full `tag=ci` integration set; its original
  self-hosted attempt remains in progress as run `29698931645` with no failed
  step or rerun. It was not cancelled; recent successful full sweeps take
  multiple hours.
- vpsfree-cz-configuration keeps the runbook in `71c78b5c`, then uses separate
  unedited confctl-generated commits `570832d8` and `898b8632` to pin
  `vpsadminStaging` and `vpsadminServices` to exact final vpsAdmin head
  `c7e4b878`. `nix flake check --no-build` passes. The branch is pushed at
  `898b863292f196b8e7c6998eb4c865f6dac45393`; pre-existing untracked `.bin/`
  and `.bundle/` development caches remain untouched.
- vpsadmin-kb-captures commit `0a3f92f` pins exact vpsAdmin revision
  `c7e4b878` in `flake.nix`, its generated lock, the capture inventory, and the
  navigation contract. `nix develop -c bin/check` passes 8/50 and 7/17 test
  groups and validates 38 controls, 29 paths, 32 capture concepts, 65
  bindings, 59 concepts, 118 variants, and all 118 PNGs. No semantic selector,
  capture, screenshot, KB candidate, staging content, or production page
  changed. The branch is pushed at
  `0a3f92f8dd4058186d51a9271d9debafd6f1c418`.

### Deployment runbook and configuration provenance (2026-07-18)

The user clarified that deployment is documentation-only. No production
deployment, migration, backfill, channel update, Node reboot, or KB write is
authorized by this follow-up.

A confctl feature worktree was created at
`worktrees/2026-07-13-security-advisory-automation/confctl` on branch
`2026-07-13-security-advisory-automation`, based on current
`origin/master` `8ccb94d`. The implementation in progress adds optional
per-closure vpsFree.cz configuration source metadata, canonical sysctl values,
the corresponding vpsAdmin/API/WebUI/advisory identity, and an operator
runbook under vpsfree-cz-configuration documentation.

The feature has seven core vpsAdmin migrations and no feature-specific plugin
migrations. The existing reconstruction tasks are
`vpsadmin:node:reconstruct_kernel_history` and
`vpsadmin:node:reconstruct_system_states`; they will be documented but not
executed against production.

### 2026-07-15 final implementation checkpoint

- The source histories have been rewritten into their owning functional
  commits. Current clean heads are vpsAdmin
  `fb11991d42f4f0cb18298137c8ceed8278dbb9ae`, vpsAdminOS
  `dbc03d00508b89093ecafc5e5abdcfc6bb5bdfbb`, and
  security-advisories `ce0aca81789c7dec31a939ddd5c88ebeafdc7281`.
  The vpsAdminOS feature branch is published at that head; downstream pins and
  the other rewritten branch updates remain pending final verification.
- vpsAdmin's vpsAdminOS input is an isolated generated lock commit and resolves
  the exact final vpsAdminOS head. The earlier intermediate lock revision was
  folded out of history.
- vpsAdmin verification before mandatory review was green: the schema-4
  reporter had 4 examples with no failures; status and record-operation
  coverage has 31 examples with no
  failures; normalized model/resource coverage has 19 examples with no
  failures; migration coverage has 2 examples with no failures; WebUI evidence
  coverage has 5 tests and 17 assertions; and the complete Overcommit gate
  passes migration mapping, WebUI/API i18n, Nixfmt, RuboCop, and PHP CS Fixer.
- security-advisories passes its full 67-example RSpec suite after review
  remediation, RuboCop reports no offenses, and its installed pre-commit hook
  passes.
- vpsAdminOS passes its Overcommit gate and targeted flake evaluation. Its
  repository-wide `nix flake check --no-build` still stops at the existing
  invalid `overlays.all` flake-output type; this is unrelated to the changed
  metadata module and is not treated as validation of this feature.
- A default vpsAdmin development-shell reporter invocation could not load the
  native libosctl extension. Re-running the same spec in the declared
  `.#libnodectld` component shell passed all 4 examples. Migration specs are
  also kept in their own process because their connection switching invalidates
  the ordinary shared test database when combined with model/resource specs.
- Mandatory review found that legacy report schemas could still produce a
  confident assessment, missing native dirty metadata was treated as clean,
  and configured kernel parameters remained in intermediate unmerged commits.
  The evaluator and historical attestations now require schema 4, nodectld
  falls back to closure confctl metadata when native dirty state is unknown,
  and all configured-parameter behavior was folded out of the feature history.
  Commit messages now describe the schema-4 contract and rolling behavior.
- The top-level dev-cluster source-identity plumbing is formatted,
  shell-checked, and committed as `069bd60`. Only this initiative's argument
  and Node metadata hunks were staged; unrelated notification work in the
  shared checkout remains untouched.

### 2026-07-15 exact closure metadata implementation

- Work resumed from heads vpsAdmin `c5803845c`, vpsAdminOS `6a8f1d355`,
  security-advisories `7e3979b`, KB contract `1adabf7`, and configuration
  `e8e60e4d`. All are still unmerged feature branches.
- vpsAdminOS evidence schema 4 removes configured kernel parameters, records
  native revision dirty state, and no longer emits the false `staging`
  fallback. vpsAdmin's native metadata likewise no longer emits `dev`.
- nodectld reports only the ordered `/proc/cmdline` parameters and all six
  booted/current vpsAdminOS/vpsAdmin/nixpkgs identities. It uses closure-native
  metadata first and the matching closure's confctl inputs file only as an
  exact-revision fallback. `/proc/config.gz` remains the no-reboot kernel-config
  fallback for an older booted closure. `/etc/os-release` is not used.
- The normalized database/API stores revision provenance and dirty state for
  current identities and history changes. WebUI links only full Git hashes,
  labels invalid or absent identities unavailable, and marks dirty native
  revisions as modified. Kernel parameter pages now show only the actual boot
  sequence.
- The security-advisories collector/evaluator is being updated to the same
  booted-only and exact-provenance contract. Its focused evaluator tests pass;
  the complete suite and RuboCop remain pending.
- Targeted vpsAdmin verification completed so far: libnodectld 4 examples,
  migration 2 examples, and normalized model/resource 19 examples all pass.
  Status/record-operation focused tests also completed without failures.
- The workspace dev-cluster launcher now derives exact worktree HEAD/dirty
  metadata and injects it into Node closures. These top-level edits overlap a
  shared dirty checkout only in `nix/test.nix`; the unrelated notification
  changes remain untouched and must not be staged in this initiative.
- `nix develop .#webui --command webui/lang/scripts/locales-update` failed
  because the shell changes into `webui`, duplicating the path. The correct
  invocation is `nix develop .#webui --command lang/scripts/locales-update`.


- The requested Node evidence presentation correction is implemented and
  pushed at vpsAdmin head
  `c5803845cc841d0c415b9009fe5878dcea23589c`. Parameter comparison rows follow
  booted positions, raw command lines render as wrapping code, passive
  explanations use a neutral content component, and current/history sysctl
  tables use compact fixed-width layouts.
- Full WebUI PHPUnit passes with 72 tests and 267 assertions. PHP syntax,
  JavaScript syntax, gettext health, PHP CS Fixer, `git diff --check`, and all
  vpsAdmin pre-commit hooks pass. The focused `webui#admin-cluster` integration
  passes end to end, including exact ordering, code markup, table structure,
  and browser width/overflow assertions.
- The first browser integration attempt found a shared fixture still calling
  revision-checked advisory publication without `expected_content_revision`.
  Focused tip commit `c5803845c` passes the fixture's current revision; the
  preserved test log established this as a setup failure before Chromium, and
  the cached rerun completed successfully.
- vpsfree-cz-configuration was rebuilt from feature base `e1cc165c` with
  exactly three generated commits: `751bb183` for `vpsadminosStaging`,
  `81dea6ca` for `vpsadminStaging`, and `e8e60e4d` for `vpsadminServices`.
  The final head is `e8e60e4d`, with vpsAdmin channels pinned to `c5803845c`
  and vpsAdminOS staging pinned to `6a8f1d355`.
- The KB contract is repinned and pushed at `1adabf7`; its complete check
  passes with 37 controls, 65 bindings, 9 exceptions, and 118 PNG variants.
  These administrator-only pages have no current end-user KB page or capture
  binding, so no KB candidate, staging, or production write is required.
- The mandatory fresh-context review initially blocked on repeated same-input
  pins and advised exact row assertions. After those fixes it cleared the
  presentation gate. The same reviewer examined the integration-discovered
  fixture commit and final repins and again found no Blocking, Important, or
  Advisory findings; no residual browser test gap remains.
- The bridge-network development cluster is running and ready with the updated
  services generation; WebUI and API both return HTTP 200 using the development
  CA. No production deployment or write was performed.
- No API/database/protocol compatibility changes are introduced. Deployment
  can update the vpsAdmin services independently; older Nodes continue to
  report the same evidence and rollback reads the unchanged schema.

- The approved relational evidence normalization is complete. Current and
  immutable event snapshots, kernel parameters/modules, security settings,
  livepatch/eBPF state, errors, and parsed kernel options use normalized
  tables. Top-level typed HaveAPI resources expose filterable rows, while the
  superseded opaque route and evidence blobs never appear in feature history.
- The final feedback implementation is committed on top of current
  `origin/master`/`origin/staging`. It replaces CVE-specific reporter fields
  with complete kernel configuration plus generic deployment/runtime inputs,
  excludes service-only Nodes, adds a digest-keyed configuration catalog and
  per-Node readiness preflight, generalizes repository instructions, and
  rewrites all five public texts for standalone clarity.
- The earlier requested implementation and mandatory-review fixes remain the
  base of this work. The final heads and exact downstream pins are recorded in
  the final feedback checkpoint below. The dev cluster has been rebuilt and
  freshly booted from those final vpsAdmin/vpsAdminOS worktrees.
- Exact feature revisions are pinned for vpsAdminOS/vpsAdmin staging and for
  the vpsAdmin services channel used by a later coordinated production service
  rollout. The production vpsAdminOS Node input is unchanged. No production
  deployment, vpsAdmin API write, KB staging, or KB publication has occurred.
- The required fresh standalone review of the final-feedback changes is
  complete. All blocking and important findings were resolved before
  integration: schema-v2 evidence is fail-closed, reconstruction and exact
  reporting share a Node row lock, and the new repository history is clean.
  confctl remains absent from the evidence contract: nodectld reports booted
  and activated system closures directly in every environment.
- The initiative development cluster was cleanly reset after the final history
  rewrite and is running and ready with the `single` topology on the bridge
  network. Its kernel-host Node reports complete normalized schema-v2 evidence;
  service-only Nodes retain no kernel evidence.
- Live per-Node conclusions are intentionally not fabricated from repository
  pins. Until the feature is deployed and exact evidence is collected, the five
  dossiers produce `unknown` rows that may be reviewed in a draft but cannot be
  published.

## 2026-07-14 final feedback verification

- `security-advisories`: all test files pass, all five dossiers validate, Ruby
  syntax and `git diff --check` pass.
- `libnodectld`: generic evidence, publish acknowledgement, and service-role
  suppression specs pass (5 examples).
- vpsAdmin migration/rollback specs pass (2 examples). A newly added Node API
  example initially omitted required `NodeCurrentStatus` fixture fields;
  adding the real non-null fields fixed the fixture and the focused example
  passes. This was a test-data issue, not an implementation failure.
- vpsAdminOS `nixfmt --check` and full system evaluation pass.
- The combined vpsAdmin API/evidence suite passes (57 examples), as do all
  repository pre-commit hooks: migration specs, API/WebUI i18n, Nixfmt,
  RuboCop, and PHP CS Fixer.
- The refreshed KB contract passes `nix develop -c bin/check`: 34 controls,
  29 paths, 32 capture concepts, 3 selectors, 65 bindings, 9 exceptions, and
  all 118 PNG variants.

## 2026-07-14 final feedback commit checkpoint

- `vpsadmin` head `70d4f4e5e8020113405c08b3ffba7d5cacc26c74`
  is pushed. Its seven feature commits are based on `origin/master`
  `1a4fa3031`; the final separate flake commit pins vpsAdminOS
  `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`.
- `vpsadminos` head `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`
  is pushed and based on `origin/staging` `ff9e49b20`.
- `vpsfree-cz-configuration` head
  `7d946a167b69068499ad0ca3474253d67de244b2` has three generated input
  commits: staging vpsAdminOS at `d47ba226...`, staging vpsAdmin at
  `70d4f4e5...`, and the vpsAdmin services channel at `70d4f4e5...`. It is
  pushed.
- `vpsadmin-kb-captures` head
  `f1b91c197e908e16b7b3c26bce2556338459fef5` pins vpsAdmin
  `70d4f4e5e8020113405c08b3ffba7d5cacc26c74`. It is pushed.
- `security-advisories` head
  `0d06b29d2af97699bc440d15d46c496e70ba3ef2` separates general assessment
  guidance, generic evidence evaluation, read-only readiness, and standalone
  public texts. Its GitHub repository still does not exist, so it remains
  local.
- All five project worktrees are clean. Final live-update, mixed-version, and
  fresh-boot integration checks pass.

## 2026-07-14 mandatory final-feedback review

- The standalone reviewer found that schema-v2 payload fields could be omitted
  and that an event configuration digest could be absent from the catalog when
  a dossier had no required kernel options. The receiver now requires every
  generic evidence component, the API emits explicit completeness gaps for
  older stored rows, and the evaluator requires every assessed configuration
  to resolve through the catalog or an explicit historical attestation.
- Reconstruction and exact Node reporting previously used independent event
  transactions. Both now serialize on the same Node row lock; regression
  coverage proves both operations use that lock and exact evidence remains the
  current record.
- Interactive-rebase status text was found in the first twelve
  `security-advisories` commit bodies. The complete orphan history was rewritten
  to retain only the intended subject and rationale.
- The two newly added Czech source labels now use invariant `node`, and the
  stale handoff revision was corrected. No additional functional bundles or
  unrelated changes were found by the reviewer.
- Focused post-fix verification passes: 33 vpsAdmin evidence/history examples,
  27 evaluator tests, the complete 50-test security-advisories suite, all five
  dossier validations, and the full vpsAdmin hook suite.

## 2026-07-14 final mixed-version hardening

- Live activation exposed one additional rolling-upgrade case: the running dev
  Node was still booted from an older closure whose metadata had no
  `schemaVersion` or generic kernel parameters, while its newly activated
  closure had schema 2. Defaulting the old fields to empty values could have
  made incomplete boot evidence appear complete.
- nodectld now validates both booted and current metadata as schema 2 before
  using them. A mixed-version Node reports an explicit `booted_metadata` or
  `current_metadata` error; the API preserves that gap and the evaluator must
  return `unknown`. A legacy-boot-metadata regression was folded into the
  original generic reporter commit.
- The dev cluster first verified the mixed state end to end: vpsAdmin stored
  schema 2 for `dev-node1` with `booted_metadata: schema version 2 metadata is
  unavailable`. A subsequent fresh boot used the final closure for both
  `/run/booted-system` and `/run/current-system` and replaced the gap with a
  complete error-free report.

## Repositories and revisions

### vpsadmin

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadmin`
- Base: `1a4fa3031` (current `origin/master` at final rebase)
- Head: `70d4f4e5e8020113405c08b3ffba7d5cacc26c74`, pushed to `origin`
- Commits:
  - `0b2cdc3c3 api: lock security advisory draft revisions`
  - `39d887ef8 api: reconstruct Node kernel history`
  - `09dcef90c api: store Node security evidence`
  - `6e78b2e80 libnodectld: report generic Node security evidence`
  - `ca210eac6 webui: show Node kernel history`
  - `17e691cba api: harden security advisory draft synchronization`
  - `70d4f4e5e flake: vpsadminos 849282e6b -> d47ba226a`

### vpsadminos

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadminos`
- Base: `ff9e49b20` (current `origin/staging` at final rebase)
- Head: `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, pushed to `origin`
- Commits:
  - `e6a5835f6 os: expose booted kernel build evidence`
  - `897580c12 os: record livepatch application time`
  - `d47ba226a os: expose eBPF live-patch link metadata`

### vpsfree-cz-configuration

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsfree-cz-configuration`
- Base: `e1cc165c` (`origin/master` when created)
- Head: `7d946a167b69068499ad0ca3474253d67de244b2`, pushed to `origin`
- Commits:
  - `5b558cca inputs: set vpsadminosStaging to d47ba226`
  - `a1b92bf9 inputs: set vpsadminStaging to 70d4f4e5`
  - `7d946a16 inputs: set vpsadminServices to 70d4f4e5`
- The input commits were generated with `confctl`. `vpsadminServices` feeds the
  production API/WebUI service channel, so its pin prepares a future
  coordinated deployment; it has not deployed anything. The production
  vpsAdminOS Node input remains unchanged. Configuration pins select the
  feature but are not part of the evidence contract.

### vpsadmin-kb-captures

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsadmin-kb-captures`
- Base: `470b759`
- Head: `f1b91c197e908e16b7b3c26bce2556338459fef5`, pushed to `origin`
- Commits:
  - `fa36dad contract: track the Node kernel history control`
  - `fa2f773 tools: ignore literal navigation tag examples`
  - `f1b91c1 contract: refresh production navigation inventory`

### security-advisories

- Orphan branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/security-advisories`
- Head: `0d06b29d2af97699bc440d15d46c496e70ba3ef2`
- Commits:
  - `d0d8816 Establish the advisory analysis repository`
  - `cba1e7b Add the narrow vpsAdmin API client`
  - `d15cbe4 Create least-privilege vpsAdmin tokens`
  - `735941b Evaluate exact deployed Node evidence`
  - `a31b291 Reconcile reviewed advisory drafts safely`
  - `03a0ef1 Add the review-gated advisory CLI`
  - `fc2ec47 Analyze CVE-2026-23111 nf_tables UAF`
  - `8cafa4a Analyze CVE-2026-46242 epoll flaw`
  - `a9ceb98 Analyze CVE-2026-53362 IPv6 flaw`
  - `6a37977 Analyze CVE-2026-53359 KVM flaw`
  - `2ca9acc Analyze CVE-2026-43499 GhostLock`
  - `0280f15 Test the complete advisory workflow`
  - `719f683 Use Node-reported system closure identities`
  - `338628a Generalize CVE platform assessment guidance`
  - `890fd60 Evaluate complete generic Node evidence`
  - `9c20448 Add a read-only publication readiness preflight`
  - `0d06b29 Clarify user impact in initial advisory texts`
- `origin` is the required SSH URL
  `git@github.com:vpsfreecz/security-advisories.git`, but the GitHub repository
  does not exist yet, so this branch is not pushed.

### vpsfree-sms-gateway (development-cluster input only)

- Branch/worktree: `2026-07-13-security-advisory-automation` at
  `worktrees/2026-07-13-security-advisory-automation/vpsfree-sms-gateway`
- Head: `af7b3fafb780c849ae03e31712128ecb0749ec0b`, matching
  `origin/2026-06-15-vpsadmin-events`; no files or commits were changed.
- This worktree is a supported local override for the dev cluster's private
  flake input. An unauthenticated Nix GitHub fetch returned 404 even though the
  SSH remote and branch are available.

## Implemented behavior

### vpsAdmin API, evidence, and history

- Ordinary advisory, advisory-CVE, and advisory-Node-status actions now expose
  and require a continuous `content_revision` precondition for mutations. They
  mutate drafts only. No `submit_draft` action was added.
- The automation scope includes the existing
  `security_advisory.node_status#index/create/update/delete` actions in addition
  to advisory/CVE actions; it excludes publish, mail, retract, generic Node/VPS,
  and `all` scopes.
- `NodeSecurityEvent` stores append-only exact or reconstructed kernel history.
  `vpsadmin:node:reconstruct_kernel_history` derives bounded boot/release events
  from historical `node_statuses`, records a per-Node reconstruction checkpoint,
  stops before the first exact Node report, is restartable/idempotent, and never
  supersedes an exact current event with an inferred row.
- Authenticated `node.kernel_history#index` is a sanitized projection available
  to all logged-in users, including inactive Nodes. It exposes boot/release
  intervals and confidence, not boot UUIDs or internal evidence. The WebUI links
  current kernel values to a per-Node history page.
- Czech follows `doc/i18n-cs.md`: the infrastructure term remains `Node` in
  Czech text, with `Nody` for the plural; neither `nod` nor `uzel` is used.
- Admin-only `node.security_evidence#index` returns, per active Node/storage
  Node: ID/name/role, separate Node observation/server receipt times, freshness
  based on receipt, reconstruction completeness and evidence revision; current
  immutable and reported kernel identity; complete internal event history with
  per-event evidence and coverage gaps; livepatch/eBPF state; selected loaded
  modules/runtime settings; deployment identity; and explicit missing-evidence
  gaps. It returns no users, VPSes, addresses, utilization, `untrusted_vps`, or
  KVM-device counts.
- The schema-versioned nodectld payload contains immutable boot ID/time/release,
  reported release, vpsAdminOS/kernel/config identity, livepatch/eBPF metadata,
  loaded modules, runtime settings, and exact booted/current system closure
  identities resolved from `/run/booted-system` and `/run/current-system`.
  Unsupported/malformed evidence becomes a gap without rejecting ordinary Node
  status.

### vpsAdminOS and configuration

- The booted system closure carries exact vpsAdminOS revision, boot kernel
  identity/source revision, and kernel configuration identity. The probe reads
  the immutable `/run/booted-system` metadata rather than a newly evaluated
  system closure and uses `/proc/stat` boot time with explicit inferred
  confidence.
- Livepatch services persist a first-application timestamp marker. eBPF
  livepatch metadata includes the link fields needed to verify every pinned
  attachment.
- nodectld resolves the booted and currently activated Nix system closures
  itself. This single mechanism works on production Nodes, the dev cluster, and
  other installations without confctl or a generated evidence file.

### security-advisories

- The dependency-free Ruby CLI provides `validate`, `collect`, `evaluate`,
  `adopt`, `ready`, and `sync`. Sync is dry-run by default and requires
  `--apply`; `ready` is a fresh read-only publication preflight, and there is
  no publish command.
- Before any remote mutation, sync validates the committed dossier/evaluation,
  recollects and re-evaluates evidence, compares the complete canonical per-Node
  results, verifies active-Node-set digests/freshness, checks the exact remote
  snapshot, and then maintains one revision chain. It atomically records
  recovery checkpoints in tracked `submission.yml` after every successful
  mutation, so partial create/update runs can be safely resumed.
- `unknown` is an honest draft conclusion for missing or stale evidence and is
  synchronized with its reason. Existing vpsAdmin publication validation still
  blocks `unknown` or `vulnerable` active Nodes.
- The evidence digest covers the complete canonical evidence snapshot. Per-event
  kernel/build/config identity, a real baseline event at or before the required
  history start, reconstruction/exact-history gaps, exact accepted build rules,
  runtime mitigations, tristate configuration reachability, and role-specific
  reachability are evaluated. A pin, synthetic current row, or mutable reported
  release alone cannot establish safety.
- `bin/create-token` interactively obtains password/TOTP credentials and writes
  a mode-`0600` token outside git. It requests exactly these 12 scopes:
  `node.security_evidence#index`; advisory `index/show/create/update`; CVE
  `index/create/delete`; and advisory Node status `index/create/update/delete`.
- All five CVE dossiers contain detailed source/platform analysis and concise
  Czech/English user text. Each separately discusses root in the VPS user
  namespace, host-Node root/escape, cross-VPS access, and Node availability.
  UAF initialization hardening and monitored NULL/general-protection faults are
  described as exploitation friction/detection, never as prevention.
- Exact accepted deployed-build lists are deliberately empty until live
  deployment evidence is reviewed. The configured 6.12.95 source contains all
  five fixes, but a configuration pin is not proof of a Node's booted build.

### Documentation contract

- The contract pins vpsAdmin `70d4f4e5e...` and records the bilingual
  `node.kernel-history` WebUI control/fingerprint.
- The canonical full production inventory was fetched (116 Czech and 70 English
  pages), checked, and used to build durable candidates. There are zero changed
  pages and zero annotation changes because current KB content does not document
  this admin-controlled Node detail view.
- Empty Czech/English release manifests were generated. With no changed pages,
  staging and production writes were neither useful nor performed.
- The annotation checker now ignores literal example tags inside DokuWiki code,
  file, nowiki, and `%%...%%` constructs; regression tests cover literal and
  real tags.

## Review findings already resolved

An initial independent design/change review found seven issues, all addressed
before the final review:

1. split oversized histories into framework, per-CVE, API/evidence/WebUI, and
   vpsAdminOS evidence commits;
2. bind boot evidence to the immutable booted closure and make timestamp
   confidence explicit;
3. require exact deployed-build identity, per-event evidence, history coverage,
   and role-specific evaluation;
4. bind sync to dossier/evidence/Node-set/freshness digests and recollect before
   writing;
5. use a continuous revision chain plus snapshot checks and partial-run recovery
   checkpoints;
6. make sync dry-run by default with explicit `--apply`;
7. state VPS-user-namespace versus host-Node impact in every public text.

Follow-up hardening also isolates malformed evidence, keeps TLS verification on
by default, hashes all evidence rather than selected labels, and allows
reviewable `unknown` draft rows while preserving the publication gate.

The mandatory final fresh-context reviewer then reported nine findings. All
were resolved before handoff:

1. apply now recollects and freshly evaluates evidence, then compares complete
   canonical node results instead of trusting editable cached rows;
2. reconstruction has a persisted completeness checkpoint, stops before exact
   reports, never promotes synthetic current evidence over exact current data,
   and the evaluator requires a real retained baseline event;
3. kernel configuration predicates use explicit enabled/disabled semantics, so
   both `y` and `m` satisfy enabled while only `n` proves disabled;
4. histories were rewritten into focused evaluator/API/token/reconciler/CLI,
   public-history/private-evidence/reporter, boot/livepatch/eBPF, and combined
   configuration-evidence commits;
5. submission checkpoint writes use fsync plus atomic rename and have an
   interruption regression test;
6. guest cluster status renders a plain kernel value, while only logged-in
   users receive the Node history link;
7. vpsAdmin stores server receipt time separately and uses it for freshness;
8. all five dossiers now link to and record the exact Linux 6.12 stable fix
   commit; and
9. mandatory publish revision preconditions remain intentional security
   hardening. The coordinated client/API deployment and rollback caveat are
   recorded below and in `plan.md`.

The review's final integration audit was also resolved: repeated repin/fixup
history was collapsed; every intermediate security-advisories commit now tests
without depending on later dossiers or classes; eBPF evidence is bound to a
revision/digest and attachment time; every draft mutation requires the expected
content revision; operator historical attestations are exact and digest-bound;
and an admin-only `external_id` plus atomic initial CVE creation recovers a
lost create response without duplicating drafts. The reporter does not depend
on confctl or any other deployment tool.

The mandatory direct-system-identity follow-up review confirmed that nodectld
is the sole source of booted/current closure identity and that missing links
fail explicitly. Its remaining findings were resolved before handoff:

1. repeated staging/services and KB pins were rewritten into one final commit
   per input stream;
2. a same-boot activation now has model/API regression coverage proving that a
   private `deployment_change` is recorded and exposed;
3. evaluator regressions prove that either changed closure, an old
   `deployment.inputs` payload, or a missing closure all invalidate the
   reviewed build and return `unknown`; and
4. these records now distinguish a prepared production services-channel pin
   from an actual deployment and from the unchanged production Node input.

At the user's request, the vpsAdmin history was then rewritten on current
`origin/master` so the direct closure mechanism is part of the original
libnodectld evidence commit. No commit in the final feature range adds or
removes `/etc/confctl/inputs-info.json` or `inputs_info`; the corrective commit
no longer exists. The exact vpsAdminOS feature revision is pinned separately by
the repository-prescribed flake update commit. Configuration and KB histories
were regenerated once more so they retain only the final vpsAdmin head.

## Verification

- vpsAdmin public history/reconstruction: 9 examples, no failures; private
  evidence/receiver/recording: 16 examples, no failures; split migration
  specs: 4 examples, no failures; libnodectld: 4 examples, no failures; WebUI
  visibility regression: 1 test/6 assertions, no failures.
- vpsAdmin RuboCop covered 20 changed non-generated Ruby files with no offenses.
  Every rewritten commit passed repository hooks: MigrationSpecs, WebUI/API
  i18n, Nixfmt, PhpCsFixer, and RuboCop.
- vpsAdminOS final-tree
  `nix eval .#packages.x86_64-linux.toplevel.drvPath --raw` passed; all three
  commits passed Nixfmt hooks.
- vpsfree-cz-configuration hooks passed. The staging Node build evaluated its
  configuration/modules/pinned vpsAdminOS and then stopped while forcing the
  closure because the local system lacks the external
  `/secrets/nodes/initrd/ssh_host_ed25519_key`. See
  `notes/vpsfree-cz-configuration/2026-07-13-confctl-node-build-initrd-secret.md`.
- A push attempted outside `nix develop` could not load the repository's removed
  local `.bundle`; retrying inside the declared Nix development shell ran the
  mandatory pre-push checks and pushed successfully.
- security-advisories: 50 tests, 286 assertions, no failures; all five dossiers
  validate; all Ruby files pass syntax checking; `git diff --check` passes.
- vpsadmin-kb-captures `nix develop -c bin/check` passes: 34 controls, 29 paths,
  32 concepts, 3 selectors; 65 bindings and 9 exceptions; 118 valid PNGs; test
  groups at 8/50 and 7/17 runs/assertions.
- The deployment-tool-independent follow-up passes its focused libnodectld spec
  (1 example), the focused evidence recording/API/receiver specs (19 examples),
  all vpsAdmin pre-commit hooks, 41
  security-advisories tests/143 assertions, and validation of all five
  dossiers.
- After the history rewrite and separate vpsAdminOS flake update, the same
  focused suites remained green and a complete `overcommit --run` passed
  MigrationSpecs, WebUI/API i18n, Nixfmt, RuboCop, and PhpCsFixer.
- The dev cluster was refreshed and all machines were updated from the final
  worktrees. Services and Node closures built and activated successfully; the
  WebUI/API both return HTTP 200 with the dev CA. Before reboot, Node1 had
  activated closure `gq2wq91k...` while retaining legacy booted closure
  `z2d206nn...`; nodectld reported the explicit booted-metadata gap described
  above.
- After a state-preserving cluster stop/start, the dev Node booted directly
  into `gq2wq91kc0h2d25m56gflrfnv6xy4yb2`, which is also its current closure.
  Its stored report has schema 2, an empty error list, booted/reported kernel
  6.12.95, source revision `a2384967...`, a catalogued config digest, complete
  configured and effective state, 341 loaded modules, 37 security settings,
  and a current exact boot report. The WebUI and API return HTTP 200.
- The mailer and both DNS service Nodes have null kernel and security-evidence
  fields after the fresh boot. The evidence collection and public kernel
  history resources filter them by role, so service-container host kernels are
  not exposed as managed Node kernels.
- Dev cluster `2026-07-13-security-advisory-automation` is `running`, `ready`,
  topology `single`, network `bridge`. WebUI and API are reachable at
  `https://webui.aitherdev.int.vpsfree.cz/` and
  `https://api.aitherdev.int.vpsfree.cz/`.
- The cluster was rebuilt after the final history rewrite. Both endpoints
  return HTTP 200, and the live API description exposes
  `node.kernel_history#index`, `node.security_evidence#index`, advisory
  `external_id`/`content_revision`, and expected-revision parameters on the
  advisory and nested Node-status mutation actions.
- Final vpsAdmin head `70d4f4e5e...` is green for API migrations, RuboCop,
  client specs, WebUI PHPUnit, i18n health, libnodectld specs, and the
  topic-parallel API suite. Selected integration run `29331995182` remains in
  progress. Its current reporter delta intentionally selects the broad
  `dns/network/node/storage/supervisor/vps` integration set; the run has no
  failure annotation or downloadable completed log yet.
- Final-head vpsAdminOS GitHub CI completed successfully, including the OS
  closure build and VM test suite.
- A superseded API-specs run failed because the two new endpoints were missing
  from the endpoint-coverage manifest. Logs were inspected, the manifest was
  fixed in the final evidence commit, and superseded runs were cancelled after
  the updated branch was pushed.
- After the history rewrite, the remaining superseded vpsAdmin CI run for old
  head `2cf07d4d...` was explicitly cancelled; new-head runs were left intact.
- After folding the direct-system-identity regressions into the implementation
  commit, the superseded selected integration run for `611d8a351...` was
  cancelled. Its completed API/libnodectld/RuboCop/i18n jobs were green; only
  runs for the then-current head were left active.
- After the final history rewrite, superseded selected-integration work for
  `039a6ecc0...` was cancelled; its API run had already completed before the
  cancellation request. Only current-head `a7781afee...` runs remain active.
- Final-head migration CI initially found that the new spec called the local
  two-argument `index_exists?` helper with an Active Record keyword. The logs
  were inspected, the spec was changed to inspect the exact index and unique
  flag, the focused suite passed locally, and final-head migration CI is green.
  Superseded long/API jobs for `67281212...` were cancelled.

### Typed evidence redesign (2026-07-14)

- Removed the unmerged nested `node.security_evidence#index` implementation
  and its `all/security_evidence` route. The replacement is twelve top-level
  HaveAPI object-list resources with concrete scalar fields; current Nodes,
  exact events, kernel options, parameters, modules, sysctls, livepatches,
  eBPF program details, and evidence gaps are independently filterable.
- Extended the original unmerged kernel-configuration migration with a
  relational `node_kernel_configuration_options` table. The canonical raw
  config remains private and digest-addressed; all `CONFIG_*` assignments are
  parsed atomically on first save, including `# CONFIG_* is not set` as `n`.
- Component resources use `node_active` for Node-state filtering so an eBPF
  program's own typed `active` field remains independently filterable. Service
  roles are excluded centrally; current evidence still uses its row-level
  `active` filter.
- security-advisories now reads and paginates the typed resources, requests
  only the union of exact kernel option names used by committed dossiers,
  reconstructs the evaluator's local snapshot, and re-reads revisioned current
  rows. It retries instead of combining data if evidence changes concurrently.
- Local advisory evidence is schema 4. The least-privilege scope list now names
  only the twelve evidence indexes and the existing advisory/CVE/nested
  Node-status actions; no generic Node inventory scope is required.
- Final quick checks: the normalized API/resource, model, supervisor, and
  migration specs pass; the full security-advisories suite passes 52 tests and
  300 assertions; all five dossiers validate; API catalog health, syntax,
  `git diff --check`, and RuboCop pass. vpsAdmin's complete Overcommit gate
  passed MigrationSpecs, Nixfmt, WebUI/API i18n, and repository-wide RuboCop.
  The KB contract passes its complete check with 118 valid PNGs and the WebUI
  tree is unchanged from the prior feature head.

### Final normalized-resource heads (2026-07-14)

- vpsadmin `0d07921edb969ee079e70b5430540de7d4cb7585`; pushed with rewritten
  history. The normalized implementation is folded into
  `0d04a9486 api: store Node security evidence`, while the vpsAdminOS flake
  input remains a separate final commit.
- security-advisories `6718325ff5e1dc00ea7a205330309edc6b5cc146`;
  local-only because the requested GitHub repository does not yet exist. The
  collector redesign is folded into `9ddbde0 Evaluate complete generic Node
  evidence`.
- vpsfree-cz-configuration `c1c17f27a073787dea2234ee6f8cc25d08b81e1c`;
  the clean feature range contains one generated staging pin and one generated
  services pin directly to vpsAdmin `0d07921e`, plus the independent
  vpsAdminOS staging pin.
- vpsadmin-kb-captures `27383188e6ee8cd896a69616688145ea09abd10a`;
  contract commit `06bb2f6` pins vpsAdmin `0d07921e`. No capture or annotation
  content changed because the normalized API rewrite does not change WebUI
  source.
- vpsadminOS remains `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`.

The configuration and KB branches are committed locally but not yet pushed.
The mandatory fresh-context change review is next, before rebuilding and
testing the dev cluster from the rewritten final inputs.

## Compatibility and deployment

- Database, evidence/history API, status-payload, metadata, and WebUI fields are
  additive. One deliberate contract change requires
  `expected_content_revision` for publication so a stale publisher cannot
  bypass the reviewed revision. Deploy the vpsAdmin API and WebUI together and
  update external administrative publishing clients before their next use; an
  old client then fails safely instead of publishing. Evidence readers ignore
  new response fields, and old nodectld payloads continue updating ordinary
  status while showing an evidence gap.
- Exact event storage and current evidence update atomically. History remains
  append-only; reconstructed events retain uncertainty rather than rewriting
  `node_statuses`.
- Deployment order: migrate and deploy the vpsAdmin receiver/API with its WebUI
  publication caller; update other administrative publishers; deploy node-side
  vpsAdmin; deploy vpsAdminOS/configuration evidence; run reconstruction; then
  collect/review evidence and draft results. Rolling Node upgrades work and no
  coordinated all-Node reboot is required.
- Rollback leaves additive tables/columns and metadata files that older versions
  ignore. An older API can read the revision column but loses publication
  enforcement, so operators must not use stale publishing clients during that
  rollback window. Unsupported evidence schemas do not prevent legacy status
  ingestion.
- The automation never needs root/SSH/log-host access. The unpublished central
  log work is useful only for an operator-controlled historical cross-check.

## Remaining handoff actions

1. Confirm final-head vpsAdmin selected integration run `29331995182`
   completes successfully and inspect its logs if it does not.
2. User creates the private `vpsfreecz/security-advisories` GitHub repository;
   then push `0d06b29d2af97699bc440d15d46c496e70ba3ef2` over its already
   configured SSH remote.
3. Deploy the feature in the recorded coordinated order and allow exact
   evidence to accumulate.
4. Create the scoped token, collect live evidence, populate each dossier's exact
   accepted build identities, evaluate, review the dry-run, and use `--apply`
   to prepare drafts. Resolve all `unknown` rows before human publication.

## Cleanup

- Worktrees remain active for review and deployment preparation.
- Dev cluster `2026-07-13-security-advisory-automation` remains running and
  ready on the bridge network. The previously running
  `2026-07-02-haveapi-i18n` cluster was stopped with the user's explicit
  authorization; graceful stop timed out and the devcluster tool terminated
  its runner and removed its GC root.
- No feature branch is merged or deployed.
- The vpsAdminOS, vpsAdmin, configuration, and KB contract branches are pushed.
  The security-advisories branch remains local only because its GitHub
  repository does not yet exist.
- No production vpsAdmin or KB write was made.

## Final review resolution and live smoke test (2026-07-14)

This section supersedes the older normalized-head and remaining-action
snapshots above.

The mandatory standalone change review completed and its significant findings
were addressed:

- the token generator verifies and grants the exact twelve typed evidence
  index actions plus existing advisory/CVE/nested Node-status draft actions;
- missing kernel configuration is represented by an explicit evidence gap and
  an `unknown` assessment, never a repository-derived assumption;
- eBPF mitigation evidence requires exact attached-link state;
- typed-resource collection is paginated, revision-checked, bounded, and
  retried instead of combining concurrent reports;
- vpsAdmin and security-advisories histories were rewritten so the superseded
  `all/security_evidence`/`node.security_evidence#index` implementation was
  never introduced; remaining string matches are negative regression tests;
- functional work, generated pins, and the vpsAdminOS flake input are split
  into reviewable commits.

Final heads:

- vpsadmin `1fa16a3cd0cb9c5c42904545f80aea210ccaeccf`, pushed;
- vpsadminOS `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, pushed;
- vpsfree-cz-configuration
  `795f459fa07bab1fe9cdf7f663b250b5723622aa`, pushed, with exact vpsadmin
  staging/services and vpsadminOS staging pins;
- vpsadmin-kb-captures
  `06c0f6cc488a07b83d1c56091848990edcf66639`, pushed;
- security-advisories
  `2737812d139facedd1250ccbefb9f5cd87889388`, local-only because the requested
  GitHub repository does not exist yet.

Final verification:

- security-advisories: 57 tests, 318 assertions, zero failures/errors; all five
  committed CVE dossiers validate;
- vpsAdmin ordinary focused suite: 102 examples, zero failures; libnodectld:
  five examples, zero failures;
- vpsAdmin complete Overcommit run: MigrationSpecs, WebUI/API i18n, Nixfmt,
  RuboCop, and PhpCsFixer pass;
- vpsadmin-kb-captures complete check: 34 controls, 29 paths, 32 concepts,
  65 bindings, nine exceptions, and 118 valid PNGs;
- vpsadminOS final-head CI and RSpec workflows pass;
- vpsAdmin final-head migration, API, client, libnodectld, RuboCop, WebUI, and
  i18n workflows pass. Long selected integration run `29355435328` remains in
  progress with its test step running; superseded run `29348186505` was
  cancelled after confirming its head is obsolete.

The dedicated dev cluster was reset after the history rewrite because its old
database had already recorded the same unmerged migration timestamp from the
discarded schema. A clean bridge/single initialization then applied the final
migration and demonstrated that relational kernel-option rows are created.
The cluster remains `running` and `ready`; WebUI and API both return HTTP 200.
The live API exposes all twelve typed evidence resources plus the public
newest-first `node.kernel_history#index`. Current evidence contains only
hosting Node 101; DNS and mailer service containers are excluded. Filtering
`node_kernel_configuration_option#index` by Node 101 and `CONFIG_IPV6` returns
the expected typed option row.

The real token smoke test initially exposed that vpsAdmin's token-management
endpoint is unversioned: authentication was incorrectly attempted below the
configured `/v7.0` resource URL. `TokenIssuer` now derives the API origin for
`/_auth/token/tokens` while retaining the versioned resource URL in the saved
configuration, with an exact-URI regression test. A newly generated token with
23 exact actions then ran `collect` end to end and produced schema-4 evidence
with the Node's booted/current closures, required kernel options, modules,
security settings, and no gaps. The temporary token file and ignored evidence
snapshot were removed; no credential was retained in the repository or notes.

Remaining handoff:

1. Monitor current-head selected integration run `29355435328`; inspect its
   logs if it fails.
2. Create the private `vpsfreecz/security-advisories` repository and push the
   existing SSH-configured local branch.
3. Deploy in the recorded coordinated order, collect production evidence, and
   resolve every per-Node `unknown` before preparing drafts for human review.

No production vpsAdmin, deployment, advisory, publication, notification, or KB
write was made.

## Relational evidence normalization (started 2026-07-14)

The user approved replacing the remaining current/event evidence JSON blobs
with relational storage. The implementation will retain only a canonical
SHA-256 snapshot revision, use a mutable current evidence row per reporting
Node, and create one immutable normalized snapshot shared by all events
detected from the same report. Typed component APIs will expose real evidence
foreign keys and database-backed ID pagination. vpsAdminOS schema 2 and the
existing action scopes remain unchanged.

Because all evidence migrations are unmerged, vpsAdmin and
security-advisories history will be rewritten so the blob-backed schema is
never introduced. Configuration and KB pins will then be refreshed to the new
vpsAdmin head. The dedicated dev cluster must be reset again after that rewrite
because its database has already applied the discarded migration timestamps.

## Relational evidence normalization (implemented 2026-07-14)

The approved normalization is implemented and committed.

- vpsAdmin base/head: `1a4fa3031` / `100e54ec20e3a185f357486d44ab7044c2cf1055`
  in `worktrees/2026-07-13-security-advisory-automation/vpsadmin`.
  The branch was autosquashed and force-pushed. Its history now introduces
  relational history gaps in `e511fd254`, normalized snapshots/components in
  `1f213c7fd`, and their typed top-level resources in `04dfaf658`; the discarded
  blob columns never appear in the rewritten series. The separate vpsAdminOS
  input commit remains the final commit `100e54ec2`.
- security-advisories head:
  `f98b88cf4e91b9108343c2b92c38c5b806973c5a` in
  `worktrees/2026-07-13-security-advisory-automation/security-advisories`.
  `46a93c6` collects stable component/evidence IDs, validates snapshot
  revisions, and uses ID pagination for stored rows. Its SSH remote still does
  not exist, so it is not pushed.
- vpsfree-cz-configuration base/head: `e1cc165c` /
  `6ef742eb333c727849f1521366f812481f9eefce`. Obsolete vpsAdmin pins were
  removed before `confctl inputs channel set --commit` generated the final
  staging and services pins to `100e54ec`; the vpsAdminOS staging pin remains
  `d47ba226`.
- vpsadmin-kb-captures base/head: `470b759` /
  `1e233c7daba10733d0e1a24c66fc2e1e79a3caa2`. The vpsAdmin flake,
  capture-manifest, and navigation-contract pins all select `100e54ec` and are
  squashed into the original Node history contract commit.
- vpsAdminOS remains `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`
  on base `ff9e49b20`; its report schema and deployed evidence mechanism did not
  change in this follow-up.

Storage now uses one mutable current snapshot per kernel-hosting Node and one
immutable snapshot shared by all events created from a single report. Scalar
versions/sysctl values are canonicalized before change comparison and digesting
so relational string columns cannot create false history events. Service-only
Node roles still neither retain nor expose kernel evidence.

Quick verification after the rewrite:

- vpsAdmin pre-commit hooks passed for every staged fixup in
  `nix develop .#vpsadmin` (Nixfmt, migration specs, WebUI/API i18n, RuboCop,
  and commit-message hooks). An ambient-shell attempt correctly failed because
  RuboCop/gettext/MariaDB were absent; commits were made only after rerunning in
  the declared shell.
- vpsAdmin migration specs: 4 examples, 0 failures.
- vpsAdmin normalized model/operation/supervisor specs after the final fixture
  correction: 30 examples, 0 failures.
- vpsAdmin combined API/supervisor/resource run before the final fixture-only
  correction: 29 examples, 0 failures. The larger rewritten run exposed only
  a direct test fixture missing mandatory `schema_version`; production reports
  were unaffected and the corrected affected suite is green.
- security-advisories: 57 runs, 319 assertions, 0 failures/errors.
- vpsadmin-kb-captures `bin/validate`: 59 concepts, 118 variants, 118 PNGs.
- `git diff --check` is clean in all changed feature worktrees.

Compatibility/deployment: all rewritten migrations are unmerged and absent
from production, so no blob data migration is needed. nodectld schema 2 and the
old/new reporter compatibility contract are unchanged. The dedicated dev
cluster must be reset before deployment because it used the discarded
migrations with identical timestamps. Long cluster integration is intentionally
deferred until the mandatory fresh-context change review.

## Mandatory normalization review resolution (2026-07-14)

The required standalone fresh-context review completed after the normalized
implementation and quick verification. It found six correctness issues; the
review was intentionally not repeated because the workspace review skill calls
for exactly one standalone reviewer. All blocking and important findings were
fixed and covered by focused tests before integration:

- status ingestion now reloads and updates evidence under the Node lock, uses
  the Node observation time as an ordering watermark, and ignores delayed
  reports; events and current evidence remain one transaction;
- event history selects one matching baseline per Node after applying all event
  filters, with cursor and limit handled by SQL rather than loading the fleet's
  history into Ruby;
- component collection expands back to the oldest exact baseline returned by
  the event API, and the collector recomputes every assembled snapshot digest,
  failing closed when a child row is absent;
- host-role filtering is applied to every component, nested component, kernel
  option, event, current, and gap path, including retained evidence after a Node
  changes to a service-only role;
- duplicate relational keys are rejected by the supervisor and normalized
  before direct model digesting, preventing the stored rows from disagreeing
  with the snapshot revision;
- collector convergence compares per-Node semantic evidence revisions, so a
  harmless observation/receipt timestamp refresh does not force repeated
  retries.

The review found no tenant authorization bypass and confirmed that the typed
resources remain admin-only, the token scopes are exact, the schema-2 Node
report is unchanged, and the flake input remains a separate commit.

Rewritten and refreshed heads:

- vpsAdmin `c83f8db49c5a905322615ba0bf6b55cdb2fab808`, force-pushed;
  normalized ingestion is `98af2959c`, typed resources are `e38063fad`, and the
  separate vpsAdminOS input is the final commit;
- security-advisories `f849a08`, local-only because the requested remote still
  does not exist; the review fixes are folded into `d98f46f`;
- vpsfree-cz-configuration `301ac693`, force-pushed, with generated staging and
  services pins to `c83f8db4` and the existing vpsAdminOS staging pin;
- vpsadmin-kb-captures `c8c592f`, force-pushed, with flake, capture inventory,
  and navigation contract pinned to `c83f8db4`;
- vpsAdminOS remains `d47ba226`.

Verification after the review fixes:

- vpsAdmin supervisor: 17 examples, zero failures, including stale worker,
  out-of-order report, and duplicate-key cases;
- vpsAdmin real MariaDB event checks: per-Node filtered baselines and 1,002-row
  two-page cursor traversal pass without omissions;
- both vpsAdmin fixup commits passed Nixfmt, migration specs, WebUI/API i18n,
  RuboCop, and commit-message hooks from `nix develop .#vpsadmin`;
- security-advisories: 60 runs, 326 assertions, zero failures/errors, including
  incomplete-baseline rejection and stable-revision timestamp convergence;
- vpsadmin-kb-captures validation: 59 concepts, 118 variants, 118 PNGs.

The current vpsAdmin GitHub Actions runs are on `c83f8db4`. Superseded
in-progress CI run `29363677398` for `100e54ec` was cancelled. The dedicated
dev cluster still requires a clean reset and redeployment because the migration
history was rewritten again.

## Final normalized integration checkpoint (2026-07-14)

This section supersedes older head, cluster, and remaining-action snapshots in
this file.

Final heads and pins:

- vpsAdmin `b7ec792464fb095961d9e84f49b4b86502ede694`, pushed. The
  normalized migrations are in `e4ddad399`, typed resources in `a5028934c`,
  generic reporting in `59c1100c7`, and the separate vpsAdminOS flake pin in
  `b7ec79246`.
- vpsAdminOS `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, pushed.
- vpsfree-cz-configuration
  `dda588941e901d49dfe5ae0de89ded0ba190e7ea`, pushed. Generated staging and
  services inputs select vpsAdmin `b7ec79246`; staging vpsAdminOS selects
  `d47ba226`.
- vpsadmin-kb-captures
  `64a1e37e925eed9bfc4b0ee79bb628cf160d9b89`, pushed. Its contract selects
  vpsAdmin `b7ec79246`.
- security-advisories
  `0f67a6047dac9dfc5b092edd3132ef2a7aa9e864`, local-only because the requested
  GitHub repository does not exist. The last commit corrects the documented
  current vpsAdmin resource URL from `/v2` to `/v7.0` after the live smoke test
  exposed the stale example.

The first clean-cluster ingestion exposed a real relational-schema issue. Linux
can simultaneously load case-distinct modules such as `xt_DSCP`/`xt_dscp` and
`xt_TCPMSS`/`xt_tcpmss`, but MariaDB's default Czech case-insensitive collation
treated each pair as a duplicate and rolled back the report transaction. All
machine-identity evidence tables and the kernel configuration catalog/options
now use `utf8mb3_bin`. Migration specs assert the collation and a model
regression preserves both pairs. This fix is folded into the original
normalized-ingestion commit, so the broken schema is absent from branch
history.

Final verification after that fix:

- normalized model and supervisor specs: 21 examples, zero failures;
- migration specs in their supported separate process: four examples, zero
  failures;
- focused RuboCop and the complete vpsAdmin pre-commit gate pass (Nixfmt,
  migration specs, WebUI/API i18n, RuboCop, and commit-message checks);
- security-advisories: 60 runs, 326 assertions, zero failures/errors; all five
  dossiers validate;
- vpsadmin-kb-captures complete validation/check passes with 59 concepts, 118
  variants/PNGs, and both test groups green;
- an attempted combined migration/model RSpec process produced false model
  failures after the migration harness intentionally switched to its stripped
  `vpsadmin_test_migration` database. The supported separate-process runs above
  are green; this was not an application failure.

The clean bridge/single cluster applied the rewritten migrations and is
`running`, `ready`, and serving the final worktrees. The live database contains
one current and one immutable event evidence snapshot, both for hosting Node
101. Service Nodes 100, 301, and 302 have null evidence references. The tested
normalized tables report `utf8mb3_bin`, and both snapshots contain all four
case-distinct `xt_*` module names. The supervisor journal has no ingestion
error. The WebUI returns HTTP 200 after final activation; authenticated typed
API collection succeeds.

The exact documented token workflow was tested with a fixed five-minute token.
It requested 23 actions (the twelve read-only evidence indexes and eleven
existing advisory/CVE/nested Node-status draft actions), saved the versioned
`/v7.0` API URL, and collected schema-4 evidence without overrides. The result
contains only `101:node`, one filtered kernel configuration, 341 loaded modules,
current and historical normalized snapshots, and a canonical evidence digest.
All five dossier evaluations completed and correctly returned `unknown` for the
dev Node because their accepted production build identities are deliberately
empty. The temporary token and command output were removed; no credential was
retained.

At this checkpoint, current-head vpsAdmin GitHub Actions are green for migration
specs, RuboCop, client specs, WebUI PHPUnit, i18n, and libnodectld. The long CI
run `29368532294` and topic-parallel API run `29368532293` are still in
progress. Superseded old-head runs were cancelled after the history rewrite.

Remaining handoff:

1. Monitor the two current-head vpsAdmin runs and inspect logs if either fails.
2. Create the private `vpsfreecz/security-advisories` repository, then push the
   already configured SSH branch.
3. Deploy in the recorded order, collect exact production evidence, and review
   per-Node conclusions. Do not publish until every active hosting Node is
   resolved and a human has reviewed the draft.

No production deployment, advisory mutation/publication, notification, KB
write, or root/log-host access occurred.

## Follow-up implementation started (2026-07-15)

The user approved a history rewrite that replaces the normalized
`node_security_*` family with `node_kernel_*` names and the clearer
`node_sysctl` resource/table. Kernel parameters will gain an explicit
zero-based position and separately stored name/value, preserving duplicates and
the distinctions between a flag, an empty value, and a value containing equals
signs. The observation-bound column names remain and will be documented as the
interval `(observed_after, observed_before]`.

The `security-advisories` repository will be converted from Minitest to RSpec
and receive the repository-standard RuboCop, Overcommit, locked bundle, and CI
setup. No source changes have been made for this follow-up yet. The existing
heads listed in the final normalized integration checkpoint are the rewrite
inputs. The dedicated dev cluster must be reset after rewritten migrations and
downstream pins are ready; no attempt will be made to migrate its old unmerged
schema in place.

## Kernel naming and ordered parameters implemented (2026-07-15)

This section supersedes the preceding follow-up-start snapshot.

Current heads and pins:

- vpsAdmin `dd07e0d26183db7462a92fc43f82443846a551f0`, force-pushed on
  `2026-07-13-security-advisory-automation`. Its rewritten history is four
  commits on `1a4fa3031`: the complete API/storage feature, generic
  libnodectld reporting, the WebUI, and the separately generated vpsAdminOS
  flake pin. The tree is identical to the pre-rewrite feature tree except for
  the approved kernel/sysctl names and ordered parameter representation.
- vpsAdminOS remains
  `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`; no report schema or source change
  was required.
- security-advisories
  `3486db8ebd9e1e898968220e8f3f03cc5ed67da5`, local-only. Its unpublished
  history is now one initial repository commit, so RSpec, RuboCop, Overcommit,
  and the kernel-focused API names exist from the first commit. The configured
  SSH remote still has no repository to accept a push.
- vpsfree-cz-configuration
  `4e827fbe4b6e7d8ee24b2ce207b9e732b1fe43c9`, local pending review. The three
  `confctl inputs channel set --commit` commits select vpsAdminOS `d47ba226`
  for staging and vpsAdmin `dd07e0d2` for both staging and vpsAdmin services.
- vpsadmin-kb-captures
  `b2e54855cdf4fe3e8925f566ac5863cb846434ec`, local pending review. Its rewritten
  single feature commit pins vpsAdmin `dd07e0d2` in the flake, capture
  inventory, and navigation contract.

Implementation details:

- normalized history/snapshot/error tables and resources use
  `node_kernel_*`; sysctls use `node_sysctls`/`NodeSysctl` and
  `node_sysctl#index`;
- kernel parameter rows store zero-based `position`, `name`, and nullable
  `value`; reconstruction preserves order, duplicate names, flags, empty
  values, and values containing additional equals signs;
- set-like evidence remains canonicalized independently of report ordering;
- `observed_after`/`observed_before` are documented as the interval
  `(observed_after, observed_before]`, with a null lower bound for the first
  known state and `effective_at` reserved for exact times;
- public `node.kernel_history#index`, the nodectld `security_evidence` wire
  key, and vpsAdminOS schema 2 remain unchanged.

Quick verification:

- every rewritten vpsAdmin commit passed the declared Overcommit gate from
  `nix develop .#vpsadmin` (Nixfmt, migration mapping, WebUI/API i18n,
  RuboCop, PHP formatting where applicable, and commit-message checks);
- vpsAdmin application/API/model/supervisor specs: 89 examples, 0 failures;
- vpsAdmin migration specs in their separate process: 10 examples,
  0 failures;
- libnodectld component-shell specs: 5 examples, 0 failures;
- security-advisories: RuboCop inspected 18 files with no offenses; RSpec ran
  61 examples with 0 failures; its real staged pre-commit RuboCop hook passed;
- vpsadmin-kb-captures `bin/validate && bin/check`: 59 concepts,
  118 variants/PNGs, both test groups green, documentation contract and KB
  annotation inventory valid;
- rewritten worktrees are clean and downstream lock metadata resolves the
  exact revisions above.

Two invalid combined test attempts did not change source. Parallel vpsAdmin
development shells raced over the shared `.gems` cache, and mixing migration
and ordinary specs in one randomized RSpec process sent application examples
to the deliberately partial migration database. The successful sequential,
separate runs above supersede those results. The reusable migration-isolation
lesson is in `notes/vpsadmin/2026-07-15-migration-rspec-db-isolation.md`.
One `confctl` attempt used a mistyped nonexistent full revision and failed with
HTTP 404 before changing the lock; the exact pushed revision then succeeded.

Compatibility remains additive because none of these migrations or API names
has merged or reached production. A mixed deployment still accepts the
unchanged schema-2 Node report, while old vpsAdmin simply ignores its existing
extra report key. The dev database cannot be upgraded in place because the
unmerged migration timestamps were rewritten; the next integration step is a
clean bridge-network cluster reset after the mandatory fresh-context review.

## Focused review history and refreshed pins (2026-07-15)

The mandatory review preparation found that the first follow-up rewrite had
collapsed independent changes too aggressively. Before launching the reviewer,
the histories were made reviewable without changing the validated trees.

- vpsAdmin is now `bd6614122a03c1a2874c898b4872687dc318a506` on the current
  upstream base `8028e5032dcc2b778ae0e6d9cf21944b1c9fe6cf`. The branch was
  force-pushed. It restores the original focused advisory, history,
  normalization, typed-API, reporter, and WebUI commits; the kernel-specific
  naming/ordered-parameter change is `6343bdfdc`; the independent vpsAdminOS
  input update is the final commit. Upstream advanced only through generated
  Ruby and WebUI dependency locks, and the feature rebased without conflict.
- security-advisories is
  `2636f3ba5c0de895939c9c1c836ddb78bdd79091`, still local-only because its
  remote repository does not exist. Its unpublished history now has focused
  project/tooling, token client, collector, evaluator, reconciler, and one
  commit for each of the five CVE dossiers. Its tree is byte-for-byte equal to
  the previously validated single-root history.
- vpsfree-cz-configuration is
  `6e763101859448d9dcedbf470e59cc287f0d452f`, local pending review. Generated
  confctl commits pin staging vpsAdminOS to `d47ba226` and both staging and
  services vpsAdmin to `bd661412`. Lock metadata resolves those exact full
  revisions.
- vpsadmin-kb-captures is
  `2630ac8db3778c9734fad35581219c1c5b01186a`, local pending review. Its single
  contract commit pins `bd661412` in the flake, capture inventory, and
  navigation contract.
- vpsAdminOS remains
  `d47ba226ab759f6d71f0f8dbae5152dd1826e86c` on its staging-line base
  `ff9e49b20`; its evidence contract did not change in this follow-up.

Final quick verification on the review heads:

- vpsAdmin affected application/API/model/supervisor suite: 114 examples,
  0 failures, against a fresh MariaDB schema;
- vpsAdmin migration suite in its isolated process: 10 examples, 0 failures;
- libnodectld component-shell suite: 5 examples, 0 failures;
- security-advisories: RuboCop inspected 18 files without offenses and RSpec
  ran 61 examples with 0 failures;
- vpsadmin-kb-captures complete `bin/validate && bin/check`: 59 concepts,
  118 variants/PNGs, 34 controls, 29 paths, 32 capture concepts, 3 semantic
  selectors, and both test groups green;
- all five affected worktrees are clean.

Two confctl invocations failed without changing the lock: one used a guessed
nonexistent full vpsAdmin revision and GitHub returned 404; another used
`services` as a channel name, while the declared channel is `vpsadmin`. The
successful commands used the exact revision read from Git and the repository's
declared `staging` and `vpsadmin` channels.

The required standalone mandatory change review is the next step. The dev
cluster remains intentionally untouched until that review is resolved; it must
then be reset rather than upgraded in place.

Review-gate operations after freezing the packet:

- the superseded bridge/single dev cluster for this verified session was found
  running and was stopped successfully; its status is now `stopped` and its GC
  root was removed;
- superseded in-progress vpsAdmin CI runs `29403821237` (`dd9801251`) and
  `29402627560` (`dd07e0d26`) were cancelled after the final branch push;
- on final head `bd661412`, RuboCop, API migration specs, WebUI PHPUnit,
  client specs, i18n health, and libnodectld specs are green; the aggregate CI
  and topic-parallel API run were still in progress when recorded.

## Mandatory kernel naming review (2026-07-15)

The one required standalone fresh-context review completed. Long integration
remains paused while four Blocking findings are resolved; the review will not
be repeated because the mandatory review workflow calls for exactly one fresh
reviewer.

1. Collector-shaped reconstructed events always contain a partial
   `security_evidence.kernel` hash, so the evaluator returns that incomplete
   evidence before consulting a historical operator attestation. Advisory
   validation also accepts fewer attestation fields than evaluation needs.
   Fix the exact/reconstructed distinction, align validation, and cover the
   collector-to-evaluator path.
2. vpsAdmin normalization commit `6343bdfdc` combines the mechanical
   `node_security_*` rename with independently reviewable ordered-parameter
   semantics. Fold final names into their introductory commits and retain the
   parameter change as a focused commit.
3. security-advisories still combines tooling/CI with its domain model in
   `44b32f1`, and reconciler behavior with CLI/operator documentation in
   `c0261ae`. Split those layers.
4. KB commit `2630ac8d` combines annotation parser/test behavior with the
   generated contract pin/inventory update. Restore separate commits.

The reviewer found no other significant issue in the requested areas. It
confirmed final-name completeness, ordered command-line/digest semantics,
relational constraints and binary collations, `(observed_after,
observed_before]` meaning, authentication and service-role exclusion, exact
least-privilege scopes including `security_advisory.node_status`, draft
locking/revision checks, and the VPS-root versus Node-compromise wording.

Residual review notes: configuration and KB remotes must be fetched/reconciled
before push; regenerated pins must follow any rewritten head; the clean reset
and live collector/evaluator exercise remain required.

## Mandatory review resolution and final heads (2026-07-15)

All four Blocking findings from the single mandatory review were resolved;
the review was not repeated, as required by the review workflow.

- `security-advisories` no longer treats the collector's partial reconstructed
  event shape as exact evidence. Reconstructed events without an immutable
  snapshot require a complete operator attestation, and dossier validation now
  requires every field consumed by evaluation. The collector-to-evaluator
  regression is covered. Tooling/domain, collector/evaluator,
  reconciler/CLI, and individual dossier commits are separated.
- vpsAdmin introduces the final `node_kernel_*` and `node_sysctl` names in the
  original ingestion and typed-resource commits. Ordered kernel parameters
  and `(observed_after, observed_before]` documentation are independent
  commits; the vpsAdminOS input update remains last. The final tree is
  byte-for-byte identical to the previously reviewed implementation.
- The KB annotation parser/test change and generated navigation-contract pin
  are separate commits.

Final repository heads:

- vpsAdmin: `0e9c345f6c50b4c880382b237cc251a4eee9ed47`, force-pushed;
- vpsAdminOS: `d47ba226ab759f6d71f0f8dbae5152dd1826e86c`, unchanged;
- security-advisories: `334ae8d1e8ff7f426f075146ee1e3235cf73877c`, pushed
  to the newly created private remote;
- vpsfree-cz-configuration: `97220d423a3b49cce83ba36f2ec6b89d2e03f792`,
  force-pushed with generated `confctl` commits;
- vpsadmin-kb-captures: `c1c0fb2`, force-pushed.

The configuration lock resolves `vpsadminosStaging` to `d47ba226` and both
`vpsadminStaging` and `vpsadminServices` to `0e9c345f6`. The KB flake,
capture inventory, and navigation contract pin the same vpsAdmin revision.

Final quick verification after the history rewrite:

- vpsAdmin affected API/model/supervisor suite: 101 examples, 0 failures;
- isolated vpsAdmin migration suite: 10 examples, 0 failures;
- libnodectld component-shell suite: 5 examples, 0 failures;
- security-advisories: after the self-revocation follow-up, RuboCop inspected
  21 files without offenses and RSpec ran 64 examples with 0 failures;
- vpsadmin-kb-captures complete `bin/validate && bin/check`: 59 concepts,
  118 variants/PNGs, 34 controls, 29 paths, 32 capture concepts, 3 semantic
  selectors, and both test groups green.

The old session cluster was stopped, then its persisted state was reset. A
clean single-Node bridge-network cluster is running and ready from the exact
vpsAdmin and vpsAdminOS worktrees above. The prior migration timestamps could
not be upgraded in place because the unmerged history was intentionally
rewritten.

An ambient `vpsfree-cz-configuration` push failed locally before contacting
GitHub because its pre-push hook could not load bundled gems. The identical
lease-protected push passed inside `nix develop`; the reusable note is
`notes/vpsfree-cz-configuration/2026-07-15-push-hooks-require-nix-shell.md`.

Clean-cluster live verification:

- WebUI and API return HTTP 200 through the bridge-network endpoints.
- The schema-4 collector returned exactly active hosting Node 101. DNS and
  mailer/service Nodes were excluded. It collected Linux 6.12.95, the exact
  booted/current system closures, all six required `CONFIG_*` options, generic
  loaded-module/sysctl state, and no evidence gaps.
- `node_kernel_parameter#index` returned separate event/current relational
  rows with contiguous positions 0 through 4 and explicit `name`/nullable
  `value` fields. Their tokens reconstruct the configured parameter array
  exactly.
- All five dossiers evaluated the one authoritative Node and remained
  `unknown`, correctly fail-closing because the fresh cluster has no retained
  history back to `2026-01-01`. A dry-run sync for CVE-2026-23111 proposed one
  Node status and no writes; no advisory or draft was created.
- The real narrow token could read the typed evidence resources and received
  HTTP 403 for generic `node#index`.

The live cleanup exposed that HaveAPI describes self-revocation as the exact
`token#revoke` provider action. The repository now grants that one additional
non-domain action and provides `bin/revoke-token`; it still has no generic
inventory, VPS, publication, mail, or unrelated-resource authority. A new
24-scope token revoked itself successfully and removed its saved file. The
earlier 23-scope development token was closed and its token row deleted from
the disposable dev database. Generated `.state` evidence/evaluations and both
temporary credential files were removed.

Final GitHub Actions status:

- security-advisories RuboCop and RSpec are green on `334ae8d1`;
- all completed vpsAdmin workflows on `0e9c345f6` are green except the full
  platform shard of the topic-parallel API workflow, which GitHub cancelled at
  its 30-minute job limit while examples were still passing. Its complete log
  shows no failure before cancellation; the topic-coverage job and every other
  shard passed. The focused local platform tests covering this change passed;
- the vpsAdmin aggregate vpsAdminOS integration workflow remains in progress.

## 2026-07-15 software/sysctl evidence follow-up start

- The verified active session remains
  `2026-07-13-security-advisory-automation`; all five affected feature
  worktrees started clean and matched their remote feature branches.
- Starting heads are vpsAdmin `0e9c345f6`, vpsAdminOS `d47ba226a`,
  security-advisories `334ae8d1`, vpsfree-cz-configuration `97220d42`, and
  vpsadmin-kb-captures `c1c0fb25`.
- vpsAdmin `origin/master` remains `8028e5032`. vpsAdminOS `origin/staging`
  advanced from the feature base `ff9e49b20` to `c21989035` through a nixpkgs
  input update and packaged-gem update. Its unmerged feature branch will be
  rebased before the new implementation.
- Approved decisions are recorded in `plan.md`: booted/current identities for
  vpsAdminOS, vpsAdmin, and nixpkgs; grouped Nix deployment history; ordered
  configured and booted parameters; a versioned merit-based sysctl policy with
  availability and per-name history; and three admin-only Node detail pages.
- Receiver/API deployment precedes Node activation. Legacy schema-2 reports
  remain accepted, the new reporter emits schema 3, and exact legacy software
  history is not fabricated. The rewritten migrations require a clean dev
  cluster reset after mandatory review.

## 2026-07-15 software/sysctl evidence review checkpoint

All intended follow-up changes are committed and the review packet is frozen.
The final histories contain one vpsAdminOS input update and one generated pin
per configuration channel; superseded intermediate pins were removed before
review without changing the implementation trees.

Repository heads and commit shape:

- vpsAdmin is `f578c8adb77db7d64690524ecafa5c124aed1e19`, force-pushed.
  The follow-up is split into `5abee06af` for normalized API/database history,
  `b33f58c8e` for the schema-3 reporter, `b7855d72f` for the administrator
  WebUI, and `f578c8adb` for the separate final vpsAdminOS input pin.
- vpsAdminOS is `a42a9fc95997122769a1012ac208214b56c6dfae`,
  force-pushed after rebasing on current `origin/staging`. Its follow-up is the
  focused `os: expose exact nixpkgs build identity` commit on top of the
  existing boot/livepatch/eBPF evidence series.
- security-advisories is
  `829fa15aaa79ded43fef62ec33adff1e8ca9d2a4`. The follow-up adds typed exact
  software collection, schema-3 completeness/digests, and matching minimal
  token scope in one evidence-contract commit. It is committed locally and
  pending the review gate before push.
- vpsadmin-kb-captures is
  `2f86e434526c815427d68231c3bdaf37841e0dc2` locally. Its final contract commit
  pins vpsAdmin `f578c8adb`, refreshes the production navigation inventory,
  and registers kernel history, ordered parameters, sysctls, and software
  versions. The three new administrator pages have no current end-user KB page
  or screenshot bindings.
- vpsfree-cz-configuration is
  `1e340b498de25370c635d7cae34d78a0b4ee7d08` locally. Three clean generated
  confctl commits pin staging vpsAdminOS to `a42a9fc9` and staging/services
  vpsAdmin to `f578c8ad`; production vpsAdminOS remains unchanged.

Quick verification before review:

- vpsAdmin focused model/operation/supervisor/API-resource and advisory specs
  passed in their ordinary database; the isolated migration suite passed.
- libnodectld's schema-3 reporter specs passed. The vpsAdmin build-info module
  evaluated to schema 1 with the exact injected revision and version.
- vpsAdmin WebUI regression specs passed with 3 tests and 13 assertions. API
  and WebUI catalogs regenerated successfully, Czech uses `Node`, and all
  affected RuboCop/PHP CS Fixer/Nixfmt/migration/i18n hooks passed.
- vpsAdminOS system evaluation succeeded and its metadata evaluation returned
  the exact nixpkgs revision/version with evidence schema 3. `nix flake check
  --no-build` still reaches the repository's pre-existing invalid
  `overlays.all` list output; the targeted system check used by this change is
  green.
- security-advisories RSpec passed 65 examples with no failures, RuboCop
  inspected 21 files without offenses, and its staged Overcommit hook passed.
- vpsadmin-kb-captures `nix develop -c bin/check` passed: 37 controls, 29
  paths, 32 capture concepts, 3 selectors, 65 bindings, 9 exceptions, both
  test groups green, and all 118 PNG variants valid. The final rewritten pin
  was rechecked against the byte-identical vpsAdmin source tree.
- All generated confctl commits ran the active Nixfmt hook successfully. One
  attempted pin used a mistyped nonexistent vpsAdmin revision and failed with
  HTTP 404 before changing `flake.lock`; the exact revision read from Git then
  succeeded.

Compatibility remains additive. vpsAdmin accepts evidence schemas 2 and 3;
the reporter emits schema 3 only after the tolerant receiver/API is deployed.
The six exact software identities, booted parameters, and policy availability
are never synthesized for schema-2 history. A rollback ignores the new rows,
but cannot reconstruct identities that were not reported. Since the unmerged
migration was rewritten in place, the next integration step is a clean
bridge-network dev-cluster reset after the standalone review.

## 2026-07-15 mandatory software/sysctl review resolution

The one required fresh-context standalone review completed and was not
repeated. It found one Blocking schema-contract issue, two Important findings,
and two Advisory hardening opportunities. Every finding was resolved before
the clean integration test:

1. Schema 3 now supports one explicit policy version whose exact 35-control
   inventory is shared consistently by reporter, receiver/API, and advisory
   evaluator. Empty/partial maps and unknown policy versions fail closed.
   Software version and revision fields must be nonempty at receiver,
   API-completeness, evaluator, and historical-attestation boundaries.
2. vpsAdminOS records a nixpkgs revision only when the actual `pkgs.path`
   matches the flake input source. Caller-supplied package sets with unproven
   provenance record no revision, and dirty input metadata is never stripped
   into a clean-looking commit.
3. The WebUI labels an available but unread sysctl as an effective-value read
   failure, not as effective. Czech translates this as
   `efektivní hodnotu se nepodařilo načíst`.
4. A sysctl policy-version-only transition now creates an immutable internal
   history event even when serialized values are unchanged.
5. nodectld validates that parsed metadata is a JSON object; arrays, scalars,
   and null become explicit evidence gaps instead of aborting Node status
   construction.

Post-fix focused verification:

- security-advisories RuboCop: 21 files, no offenses; RSpec: 67 examples,
  0 failures, including receiver-equivalent empty/partial/unknown-policy and
  historical-attestation cases;
- vpsAdmin API/model/supervisor/operation resources: 48 examples, 0 failures;
- libnodectld probe: 3 examples, 0 failures;
- WebUI evidence regression: 4 tests, 15 assertions; all repository hooks for
  the API, reporter, and WebUI fix folds passed;
- vpsAdminOS Nix formatting and targeted system evaluation passed; a matching
  package set evaluates the exact nixpkgs revision
  `8eeec934ae0dbeca3d7868c059568a65c08b2fc3`;
- the three policy inventories were compared mechanically and are identical,
  sorted, and contain 35 controls.

Fixes were folded into their owning commits. Final pre-integration heads are
vpsAdmin `a757f6918123bd445ad71a47e45290857f216a85`, vpsAdminOS
`2b86a03952cc322bf43b506908bcf05e370d18d8`, security-advisories
`7e3979bf1c07a10442c6eebfdfab4f96a8359bb8`, vpsadmin-kb-captures
`0a551088637562c288261db206593df83b499cdd`, and
vpsfree-cz-configuration `814f02621b4719c33a4d59d0137c484513511c8c`.
The final contract and generated configuration pins resolve those exact
vpsAdmin/vpsAdminOS revisions.

## Final clean integration and live workflow (2026-07-15)

The clean bridge-network cluster exposed one additional integration gap after
the mandatory review: vpsAdminOS' raw test-framework evaluation did not carry
the locked nixpkgs revision into the generated closure. The receiver correctly
rejected that first schema-3 report instead of accepting a partial software
identity. Production flake systems already received the identity module; the
test framework now carries the same locked revision only when the evaluated
`pkgs.path` is the matching nixpkgs source. An unrelated caller-supplied
package set still records no revision. The active Node was updated and the
cluster was stopped and started so both booted and current closures contain
nixpkgs `8eeec934ae0dbeca3d7868c059568a65c08b2fc3`.

The resulting final heads are:

- vpsAdmin `d57c6f0fc66927bf5cea16dd10cbe519b31a3c86`, pushed;
- vpsAdminOS `6a8f1d35539f9aade7a0535a535587f025aa96d2`, force-pushed;
- security-advisories `7e3979bf1c07a10442c6eebfdfab4f96a8359bb8`, pushed;
- vpsfree-cz-configuration
  `fa01112c44afa31f53d21cc3e278ba3fef2cf6a0`, force-pushed with generated
  confctl commits for the corrected staging/services pins;
- vpsadmin-kb-captures
  `e060503b2de25c963ded49a1567de43d1b847452`, force-pushed and pinned to the
  exact final vpsAdmin/vpsAdminOS revisions.

Final live verification on the running, ready, single-Node bridge cluster:

- WebUI and API return HTTP 200. The normalized database contains one hosting
  Node and excludes the mailer and two DNS service Nodes from kernel evidence.
- Node 101 reports evidence schema 3 with no gaps. The canonical kernel
  configuration contains 8,047 parsed relational options; the advisory
  collector requested the six dossier-relevant options and received all six.
- Both current and event snapshots contain the exact 35-control sysctl policy:
  34 controls are available and one is explicitly unavailable. The initial
  event contains typed before/after sysctl rows and all six booted/current
  software identities.
- Configured kernel parameters reconstruct at positions 0 through 4 and the
  actual boot command line at positions 0 through 8, preserving order and
  values independently. The first boot event correctly has no
  `observed_after` lower bound and has its first `observed_before` upper bound.
- A real token created by `bin/create-token` had mode 0600 and exactly 25
  scopes: the typed evidence indexes, draft advisory/CVE/Node-status actions,
  and self-revocation. Collection returned evidence schema 5 for Node 101 only.
- All five CVEs evaluated that Node as `unknown`, fail-closing because the
  clean cluster has no history back to 2026-01-01. Dry-run sync for
  CVE-2026-23111 proposed one unknown Node status and no write; no advisory or
  draft was created.
- The automation token received HTTP 403 for generic `node#index` and
  `security_advisory#publish`. A normal member token received HTTP 200 for the
  nested public `node.kernel_history#index` and HTTP 403 for admin-only
  sysctls. All temporary tokens were revoked or removed from the disposable
  database, token files and generated `.state` files were removed, and no
  credential remains.
- The complete KB check remains green: 37 controls, 29 paths, 32 capture
  concepts, 3 semantic selectors, 65 bindings, 9 exceptions, both test groups,
  and all 118 PNGs.

Current-head GitHub checks are green for security-advisories RuboCop/RSpec and
the completed vpsAdmin and vpsAdminOS jobs. The long selected vpsAdmin
integration run `29432504910` and vpsAdminOS test-suite run `29432240364` are
still in progress at this checkpoint. Superseded vpsAdmin run `29429676226`
was cancelled after confirming that its head was obsolete.

The cluster remains running for review. No production deployment, vpsAdmin
advisory mutation/publication, user notification, or KB write was performed.

## Node evidence WebUI presentation completion (2026-07-15)

- vpsAdmin head `c5803845cc841d0c415b9009fe5878dcea23589c` is
  pushed. The functional WebUI commit is `b27406af2`; focused tip commit
  `c5803845c` updates the shared advisory browser fixture for the existing
  optimistic-concurrency publication contract.
- vpsfree-cz-configuration head
  `e8e60e4d4a999188b4b1e72e6abc86adf566e270` is force-pushed with exactly
  three generated pin commits from `e1cc165c`: `751bb183`, `81dea6ca`, and
  `e8e60e4d`. vpsadmin-kb-captures head
  `1adabf736d5bde9dd6b65d916b65b48d2b5efc6a` is force-pushed and pins the
  exact final vpsAdmin revision.
- WebUI PHPUnit passes 72 tests and 267 assertions. The complete KB contract
  check passes. `webui#admin-cluster` passes its Playwright scenario, including
  boot-position order, raw-command-line code markup, neutral descriptions,
  compact table columns, and horizontal-overflow checks.
- The first integration attempt failed during fixture creation before
  Playwright because `SecurityAdvisory#publish!` now requires
  `expected_content_revision`. The preserved log identified the exact call;
  passing `advisory.content_revision` fixed it, and the cached rerun passed.
- The same mandatory standalone reviewer checked this post-gate delta and the
  regenerated downstream pins. The result contains no Blocking, Important, or
  Advisory findings, and no residual test gap.
- The bridge development cluster remains `running` and `ready` on the default
  network, with WebUI and API returning HTTP 200 through the development CA.
  Its active services generation contains the final runtime WebUI changes;
  `c5803845c` changes test fixtures only.
- Current-head vpsAdmin CI run `29441379490` is still executing the full
  `tag=ci` set because the fixture lives in shared `tests/suite/webui.nix`.
  Setup, selection, and preview are green and the check has no annotations at
  this checkpoint. Superseded in-progress runs `29439429583`, `29438336356`,
  and `29432504910` were cancelled only after their heads became obsolete.
- All three affected project worktrees are clean and synchronized with their
  SSH remotes. No production deployment, API mutation, advisory publication,
  notification, KB staging, or KB publication was performed.

## 2026-07-16 exact closure final rollout

The exact-closure refinement is complete and all five project worktrees are
clean and synchronized with their SSH feature branches:

- vpsAdmin `9de28b8fb92c383f50e5ca3605642d7a78b46cf1`;
- vpsAdminOS `dbc03d00508b89093ecafc5e5abdcfc6bb5bdfbb`;
- security-advisories `ce0aca81789c7dec31a939ddd5c88ebeafdc7281`;
- vpsadmin-kb-captures `3fb8b0cfe7b53cfd83724766cb333553b96d3c46`;
- vpsfree-cz-configuration
  `9a7db1519ebea5bdc003c7232a5a167c50af18c9`.

The configuration branch consists of three generated confctl commits that pin
staging vpsAdminOS and staging/services vpsAdmin to the exact final revisions.
The KB contract pins the same vpsAdmin head and its complete contract check is
green. The top-level exact source-injection implementation is published on
workspace master as `cf437a53809cbc9b25d78bd7585325763ff26e86`.

The previous cluster was stopped and its state was reset before integration.
The final single-Node cluster is running and ready on the bridge network. A
clean temporary checkout was required so unrelated shared-workspace
notification edits could not enter the build. Nix rejected symlinked path
inputs, so project inputs were real detached worktrees. Workspace master also
contains an unmerged notification-stack harness whose NixOS options do not yet
exist on vpsAdmin master. The final build therefore used compatible committed
harness baseline `a98bdb9` plus only the 47-line source revision/dirty-state
plumbing from `cf437a5`; product inputs remained the exact clean final commits.
Both issues have durable troubleshooting notes.

Live evidence verification through the real narrow API token established:

- Node 101 is the only active kernel-hosting Node; DNS and other service roles
  are excluded from the evidence set;
- report schema 4 has no evidence gaps and identifies kernel `6.12.95`;
- booted and current vpsAdminOS are `dbc03d005`, vpsAdmin is `9de28b8fb`, and
  nixpkgs is `8eeec934ae0dbeca3d7868c059568a65c08b2fc3`; all six identities have
  native provenance and `revision_dirty=false`;
- booted/current system paths are identical in this fresh cluster, while the
  API still stores the two generations separately;
- `/proc/cmdline` reconstructed exactly as nine typed rows at positions 0
  through 8, including the valueless `quiet` token. There is no configured
  parameter origin or configured-parameter data;
- the typed sysctl resource contains the exact 35-control merit-based policy;
  the six dossier-required kernel options were retrieved by exact-name filters
  from the digest-addressed relational configuration;
- the first boot event correctly has `observed_after=null` and a populated
  `observed_before`, because no earlier observation can bound its lower side.

`bin/create-token` wrote a mode-0600 token with exactly 25 scopes. The complete
collector returned schema-5 evidence for Node 101 and all five CVEs fail-closed
to `unknown`: the fresh development database cannot prove history back to
2026-01-01. The real apply workflow created development draft 1, its CVE row,
and Node 101's unknown status. `ready` refused the draft because the Node is
unknown and resolution is incomplete. Generic `node#index` and
`security_advisory#publish` both returned HTTP 403. The token was then revoked
and its file removed; ignored development evidence/evaluation files were also
removed. The development draft remains for WebUI review, but no advisory was
published and no mail or user notification was sent.

Final current-head CI status at this checkpoint:

- security-advisories RuboCop and RSpec are green;
- vpsAdmin migration, RuboCop, WebUI, client, libnodectld, and i18n workflows
  are green. The topic-parallel full platform shard was cancelled exactly at
  its configured 30-minute timeout while examples were still passing; its log
  reached the new evidence resource specs without a test failure, and every
  other shard plus topic coverage passed. The long integration CI remains in
  progress;
- vpsAdminOS RSpec and the closure-build job are green; its long test-suite job
  remains in progress.

The bridge cluster is intentionally left running for review. Its state and
source mounts depend on
`/tmp/vpsfree-security-advisory-devcluster-compat-20260715` until it is stopped.

## 2026-07-16 integration follow-up

The completed long suites exposed four test assumptions rather than product
regressions. The fixes are committed and pushed on the feature branches:

- vpsAdmin `f6caefd79` makes `supervisor/runtime-ingestion` an explicit rolling
  compatibility test. It stops the real nodectld reporter, publishes a current
  legacy Node status with no `security_evidence`, verifies the ordinary status
  fields, and restarts nodectld. Follow-up `100c93fc3` permits the test to run
  before nodectld has created an initial current-status row, while still
  choosing an observation newer than the stored watermark when one exists.
  The existing stale-observation rejection is unchanged and remains covered by
  the supervisor unit specs.
- vpsAdmin splits the WebUI fixes into focused commits: `00ad4ab3b` links Node
  names in both cluster views and kernels in the overview, `b1e70f9ea` removes
  the displayed parameter position while retaining boot-order sorting and
  gives the raw command line value 85 percent of its row, `0e1ed2649` moves the
  selected sysctl into the history title, and `e44132ad3` edits advisory
  content while it is still a draft. `7f90ef35b` changes the raw-command-line
  table to automatic layout because fixed table layout ignored widths assigned
  after XTemplate's empty first row. The final head is
  `7f90ef35b269fec7cef6e61357b0a7162cc0cdb0`.
- vpsAdminOS `8f598f2d6` replaces an exact console-login prompt wait with the
  test driver's shell-readiness wait, avoiding console output interleaving from
  cron during stage-2 boot.

Quick verification is green: vpsAdmin WebUI PHPUnit passes 72 tests and 277
assertions; both changed Playwright files pass Node syntax checks; all three
vpsAdmin integration targets and the vpsAdminOS stage-2 target evaluate and
list successfully; `git diff --check` is clean. Overcommit hooks passed in both
repositories, including nixfmt, migration specs, WebUI/API localization, PHP
CS Fixer, and commit-message checks. The first vpsAdminOS commit attempt from
the ambient shell failed because nixfmt was absent; it was rerun normally from
the repository Nix shell without bypassing hooks. The removed `Position`
gettext entry and Czech catalog were regenerated with
`webui/lang/scripts/locales-update`.

The independent KB contract final commit is
`2f4742934d9f5b20d85a6858685157c57f977913`; it pins the exact final vpsAdmin
head. Its complete check is green with 37 controls, 29 paths, 32 capture
concepts, 3 semantic selectors, 65 bindings, 9 exceptions, 15 tests/67
assertions, and 118 PNGs. The changed administrator controls have no bound
Czech/English KB pages or capture concepts, so no KB candidate or PNG update
is required.

The mandatory standalone reviewer reported one Blocking commit-structure
finding: the original Node-evidence WebUI commit grouped cluster navigation,
kernel-parameter presentation, and the sysctl-history title. It was split into
the three focused commits above. The review's Advisory test gap was also fixed
by asserting the Node-details link in the alternate cluster VPS view. There
were no Important findings and no product-code, compatibility, authorization,
or escaping defect. No second reviewer was launched because the skill requires
exactly one standalone reviewer; the final trees preserve the reviewed behavior
and only improve the requested commit split and direct coverage.

Final focused integration verification is green:

- `supervisor/runtime-ingestion`: all 10 examples pass. The legacy `statuses`
  message omits `security_evidence`, is accepted by the real supervisor, and
  persists process, memory, swap, ARC, and pool fields; nodectld is restored
  before the remaining nine examples run.
- `webui#admin-cluster`: all 9 Playwright scenarios pass. The first isolated
  run measured equal 402-pixel command-line cells and exposed the fixed-layout
  behavior described above; the automatic-layout rerun passes the width,
  markup, order, link, and overflow assertions.
- `webui#security-advisories`: all 10 Playwright scenarios pass, including
  draft editing with the current content revision.
- vpsAdminOS `system/boot/stage-2`: all 4 examples pass using shell readiness.

Two initially simultaneous WebUI invocations collided over the same
`/tmp/os-test-runner/os-test-webui-fd1a3b33` runtime and virtiofsd PID file.
They were discarded as non-authoritative infrastructure collisions and rerun
in isolation. The final WebUI PHPUnit run also passes 72 tests and 277
assertions. vpsAdminOS GitHub CI at `8f598f2d6` is fully green. At the final
checkpoint, vpsAdmin WebUI PHPUnit and i18n are green at `7f90ef35b`; the full
selected integration workflow `29489765787` is still running its test step.
The obsolete `e44132ad3` integration run was cancelled only after the new head
was pushed.

The production configuration branch now ends at
`bde2ea9bd8495a675ef32294550fb63bc171cff8`. Its two generated confctl commits
pin both `vpsadminStaging` and `vpsadminServices` to `7f90ef35b`; the latter is
role `vpsadmin` in channel `vpsadmin`. The KB contract is pushed at `2f4742934`
and its complete check remains green.

The preserved bridge-network development cluster was restarted without a
reset and then switched in place with `devcluster update ... all`; no guest
reboot was requested. It is running and ready, and WebUI/API both return HTTP
200. The live normalized evidence contains two schema-4 observations for Node
101. Both booted and current software rows report exact clean revisions:
vpsAdminOS `dbc03d005`, vpsAdmin `7f90ef35b`, and nixpkgs `8eeec934a`. This
also verifies that the final revision metadata reaches nodectld after an
in-place update even though the booted kernel and system path are unchanged.

No production deployment, API mutation, advisory publication, notification,
KB staging, or KB publication was performed.

## 2026-07-16 authoritative system-state implementation

The user approved implementing authoritative runtime CPU, Linux-visible
memory, swap, and cgroup state for hosting/storage Nodes. The durable plan now
records the normalized change-only history, public authenticated read access,
narrow security-advisories cgroup projection, compatibility cache, backfill,
and rolling deployment design. Implementation begins from clean, pushed heads:
vpsAdmin `7f90ef35b`, security-advisories `ce0aca817`, configuration
`bde2ea9bd`, and KB contract `2f4742934`. The shared top-level checkout has
unrelated changes which will be preserved and staged selectively.

### Implemented and committed

- vpsAdmin now ends at `304d741e5` with three focused commits:
  - `c418e93e1` adds `node_system_states`, authoritative current-report reads,
    transactional rollback-cache updates, reconstruction, typed
    `node_system_state`/`node_cgroup_state` resources, raw-status cgroup
    output, and fail-closed swap checks;
  - `7ca044842` refreshes CPU count and cgroup version on every nodectld status
    cycle;
  - `304d741e5` adds the authenticated System history page, removes bootstrap
    capacity fields from the Node WebUI form, and adds member/admin browser
    coverage.
- security-advisories now ends at `07a4ecf`. Evidence schema 6 includes the
  narrow per-Node cgroup timeline, validates one current non-overlapping
  history for every active hosting Node, retries raced transitions, and adds
  only `node_cgroup_state#index` to the token. The digest includes cgroup
  transitions but excludes only the moving `last_observed_at` of an unchanged
  current row.
- Reconstructed rows can be inserted after a live current row, so database IDs
  do not necessarily follow observation time. The API now uses a composite
  `(first_observed_at, id)` cursor; a regression spec proves that pagination
  does not skip a backfilled row with a newer ID.
- Impossible zero CPU/memory reports are normalized to unknown. The non-null
  rollback cache is set to zero in that case, avoiding stale capacity after a
  rollback, while zero swap remains a valid observed value.

### Quick verification

- vpsAdmin application specs: 115 examples passed in 7m48s across the new
  resource/reconstruction suites and affected Node, supervisor, status, and
  VPS write specs. The focused composite-cursor resource rerun passed 12
  examples; the final capacity-normalization/atomicity rerun passed 3 examples.
- The migration ran separately and passed 2 up/down examples. An attempted
  mixed migration/application RSpec process was discarded because migration
  specs intentionally switch to a partial isolated database; the existing
  durable migration-spec note documents this constraint.
- libnodectld passed 5 examples. Its component bundle does not contain RuboCop,
  so the repository-level RuboCop run was used as CI does.
- Repository RuboCop inspected 2024 Ruby files without offenses. WebUI PHPUnit
  passed 75 tests/287 assertions, WebUI locale health passed, both changed
  Playwright files passed Node syntax checks through `nix shell
  nixpkgs#nodejs`, and CI selection passed 16 tests/55 assertions.
- security-advisories passed 71 RSpec examples and RuboCop inspected 21 files
  without offenses. Its installed Overcommit hook passed.
- All three vpsAdmin commits passed the installed Nixfmt, migration mapping,
  API/WebUI i18n, RuboCop, and applicable PHP CS Fixer hooks. The first commit
  attempt from the ambient shell failed because it lacked RuboCop, gettext,
  and MariaDB; it was rerun from `nix develop .#vpsadmin` without bypassing
  hooks. No product file changed during the failed attempt.

The vpsAdmin and security-advisories worktrees are clean. Configuration and KB
pins still point at the previous reviewed vpsAdmin head; they will be updated
after the mandatory fresh-context review establishes the final functional
revision. No long integration suite, dev-cluster update, production write,
advisory mutation, token creation, or KB staging has been started for this
follow-up yet.

### Mandatory review and remediation

The required standalone fresh-context review examined vpsAdmin
`7f90ef35b..304d741e5` and security-advisories
`ce0aca817..07a4ecf`. It reported one product-code Blocking finding: the
narrow `node_cgroup_state` resource projected every `node_system_states` row,
so a CPU, memory, or swap-only change produced a duplicate cgroup row, exposed
irrelevant transition timing, and changed the advisory evidence digest. It
also required the broad API and WebUI commits to be split into independently
reviewable history/policy and history/form commits. There were no Important
findings. Focused nodectld and security-advisories commit structure was
accepted.

The cgroup finding is fixed by coalescing consecutive equal cgroup versions in
the API's derived relation while returning null capacity placeholders to
ActiveRecord and omitting those fields from the typed resource. A vpsAdmin API
regression proves that a capacity-only change remains visible in full system
history but produces one cgroup period. The collector now also rejects an
uncoalesced narrow timeline fail-closed. Focused verification passes: the new
vpsAdmin regression passes against MariaDB, and security-advisories passes 13
collector examples plus RuboCop on both affected files. The first attempted
vpsAdmin focused command used the aggregate development shell and did not
provide the API bundle; it was rerun with the repository's `.#api` shell. The
initial derived relation omitted model-only placeholder columns and was
corrected after a failing API test identified ActiveRecord eager-load column
selection. No check was bypassed.

The remaining review remediation is an unmerged history rewrite into focused
commits. Exact configuration and KB pins remain intentionally unchanged until
the rewritten vpsAdmin head is final.

### Final system-state checkpoint and canonical Node authorization

The review remediation and requested follow-up are complete. The pushed
vpsAdmin branch ends at `a64c796fa3b05d0f8166ea5a33cf03bbdf56dc9a` with the
functional history split into `c32bb3004` (normalized system history),
`7bf62140a` (reported capacities), `ac8f8a517` (live probe refresh),
`d21da33a0` (history WebUI), and `b3f3bca61` (bootstrap form removal), followed
by the focused test/endpoint-inventory commit `889ab525f` and CI timeout commit
`a64c796fa`. The earlier
`api: expose Node IDs in system histories` workaround was removed completely
from the rewritten branch; the cgroup history resource has no duplicate
`node_id` field.

The pushed security-advisories branch ends at
`10a1f7ace2c1e509e823be94dcd76f950ceec83b`. Its token now requests normal
`node#index` and `node#show` permissions, plus `node_cgroup_state#index` and
`node_cgroup_state#show`. The cgroup `show` scope is required by HaveAPI when
authorizing the typed Node association: with only the first three scopes a
direct Node show succeeds, but a cgroup row returns an unresolved,
unauthorized Node relationship. With all four, the row resolves to the
canonical Node object. A real mode-0600, 29-scope development token collected
schema-6 evidence for Node 101 through this relationship, including its cgroup
history. The token was then revoked with the repository command and its file
was deleted. No advisory draft was mutated.

Final vpsAdmin focused verification is green. The swap-policy specs pass four
examples after fixtures gained authoritative current reports, and endpoint
coverage passes after adding index/show coverage for both new typed resources.
The complete targeted integrations pass: `supervisor/runtime-ingestion` has 10
green examples (including an older status payload without evidence),
`webui#navigation-readonly` passes, and `webui#admin-cluster` passes. The
runtime integrations exercised the same functional head; `889ab525f` changes
only specs and the endpoint coverage manifest. security-advisories passes 72
RSpec examples and RuboCop over 21 files; GitHub RSpec and RuboCop are green at
`10a1f7a`. vpsAdmin GitHub RuboCop and i18n are green at `889ab525f`. Earlier
API failures were investigated: the first exposed swap fixtures that lacked
authoritative reports, and the second exposed missing endpoint coverage
entries. Both causes are fixed in `889ab525f`. The next full-platform shard
was cancelled exactly at the workflow's 30-minute timeout without an RSpec
failure; core platform was green but also needed 26m43s. Commit `a64c796fa`
raises both equivalent API matrix job limits to 45 minutes. The corrected
current-head workflow `29526678528` is fully green: all 26 topic shards and
aggregation passed. Full platform completed successfully in 31m43s, directly
proving that the former 30-minute limit, rather than an RSpec failure, caused
the cancelled run. The superseded selected-integration run was cancelled after
the follow-up push as required; the same functional tree had already passed
the three targeted integration suites locally.

The configuration branch ends at
`ceb856c3ea1f06e0cd7a51b85e231495731197be`; generated confctl commits pin both
`vpsadminStaging` and `vpsadminServices` to `a64c796fa`. The production input
was not changed. A production-configuration staging build resolved the feature
inputs but could not continue locally because the production initrd SSH host
key is intentionally unavailable at `/secrets/nodes/initrd/ssh_host_ed25519_key`.
The independent KB contract remains clean and pushed at `5e2221177`, pinning
the final functional WebUI revision; the later vpsAdmin commit has no product
or documentation change.

The bridge development cluster remains running. API/services and node1 were
updated in place to the exact final heads. Node 101 retained boot ID
`bca00320-cc4f-4381-a5a8-665cad7977c4`, so no reboot occurred. Its build-info
reports clean vpsAdmin revision `a64c796fa`, and the API database records the
same revision as the current vpsAdmin generation while preserving
`7f90ef35b` as the booted generation. This proves the normalized history
records an in-place closure change. No production deployment, API mutation,
advisory publication, notification, KB staging, or KB publication occurred.

### Evidence-page presentation and dev-cluster header follow-up

The user requested removing the description blocks from System history,
Software versions, Sysctls, Kernel parameters, and Kernel history, and showing
cgroup generations as `v1`/`v2`. vpsAdmin commit `61596d6b7` implements the
presentation changes, updates generated gettext artifacts, changes browser
expectations, and adds regression coverage for the compact value and absence
of descriptions.

The development header showed static `4.1.0` because the services machine had
both an empty packaged `.git-revision` and `revision: null` in
`/etc/vpsadmin/build-info.json`. The dev-cluster passed the selected worktree
revision only to Node-machine module arguments. Workspace commit `a95b2ba`
passes the same revision and dirty flag to the services host. vpsAdmin commit
`bf103480d` forwards them into the separately evaluated WebUI container,
removes cross-deployment session caching, and compares the rendered header link
with the exact packaged revision. Production flake inputs already provide
exact revisions and need no metadata fallback.

Quick verification is green: WebUI PHPUnit passes 76 tests/289 assertions,
both changed Playwright files pass Node syntax checks, locale generation and
health pass, all vpsAdmin pre-commit hooks pass, and the complete current API
matrix remains green. The workspace Nix file passes `nixfmt --check`.

The required standalone reviewer reported two Blocking findings: the
services-host module arguments did not cross the nested WebUI container's
`specialArgs`, and the presentation commit bundled independent header
coverage. It also reported two Important findings: sessions cached empty/stale
revisions across deployments, and the browser assertion accepted any valid
hash instead of the selected source revision. One Advisory finding asked that
the description regression not prohibit unrelated future Node descriptions.
All findings are remediated in the two focused vpsAdmin commits above: the
broad unit assertion was removed in favor of page-scoped browser checks, and
the expected revision is read from the packaged source used by the test. Per
the skill, exactly one standalone reviewer performed this follow-up review; no
second reviewer is launched. Long browser and live dev-cluster verification
can now proceed.

### Final presentation/header verification

The final pushed vpsAdmin head is
`ae76ea3c01148986acd34d43b0d0dd6f6f140ea4`. The focused commits are
`61596d6b7` for the concise evidence-page presentation and `ae76ea3c0` for
deployed WebUI source identity. The latter keeps an exact commit-link assertion
when metadata exists and verifies the intended static `4.1.0` fallback in an
isolated local-worktree evaluation, whose generated `.git-revision` is empty.
This preserves a strict deployed-revision check without inventing a revision
for unpinned local source.

Two integration attempts exposed test-only assumptions before the final green
run. The first referenced a package attribute unavailable at suite scope. The
second required an exact revision even though the isolated flake path has no
`rev` or `dirtyRev`; its package `.git-revision` contains only a newline. The
final test reads the services build metadata, validates an exact link when that
metadata is exact, and otherwise validates the static fallback. The durable
lesson is recorded in
`notes/vpsadmin/2026-07-16-webui-local-revision-fallback.md`.

Final integration verification is green and was run sequentially to avoid the
test runner's shared temporary VM-state collision:

- `webui#navigation-readonly`: 1/1 script successful in 715.22 seconds; its
  Playwright example passed in 155.17 seconds. It verifies no System history
  description and the compact `v2` value.
- `webui#admin-cluster`: 1/1 script successful in 701.77 seconds; its
  Playwright example passed in 332.34 seconds. It verifies the removed Kernel
  history, Kernel parameters, Sysctls, and Software versions descriptions.
- The KB contract at `2aa73ba1b` pins the final vpsAdmin revision and passes
  `nix develop -c bin/check`: 38 controls, 29 paths, 32 capture concepts, 3
  selectors, 65 bindings, 9 exceptions, 15 tests/67 assertions, and all 118
  PNGs. No KB pages or captures are bound to the changed controls.

Generated confctl commits `2168be37` and `6b92adea` pin both staging vpsAdmin
and the vpsAdmin services channel to `ae76ea3c0`; production remains unchanged.
Workspace commits `a95b2ba` and `7ed215d` propagate the services revision and
copy `.git-revision` into the live development WebUI root.

The persistent single-topology bridge cluster was switched in place and remains
running and ready. The public WebUI header renders `ae76ea3c` linked to the
exact GitHub commit. Services-host, nested-container, live-WebUI, and node1
metadata all report the full clean `ae76ea3c...` revision. Node1 retained boot
ID `bca00320-cc4f-4381-a5a8-665cad7977c4`; only nodectld restarted, so no node
reboot occurred. Normalized software evidence preserves booted vpsAdmin
`7f90ef35b...` and reports current vpsAdmin `ae76ea3c...`.

GitHub WebUI PHPUnit and i18n are green at the final head. The final selected
CI workflow is still running its integration step at this checkpoint. The
superseded `39c350a7` CI run was cancelled only after the final head was
pushed. No production deployment, advisory/API mutation, token creation, KB
staging, or KB publication was performed.

## 2026-07-17 kernel evidence simplification start

The user approved a history rewrite that removes the generic derived gap API,
splits every initiative top-level HaveAPI resource into its own file, and moves
report normalization/serialization/reconciliation out of ActiveRecord models.
The database schema and nodectld wire contract remain unchanged. vpsAdmin will
expose relational evidence errors, reconstruction state, and sampling gaps;
security-advisories will interpret those facts and advance its ignored evidence
document to schema 7.

Starting clean pushed heads are vpsAdmin `ae76ea3c0`, security-advisories
`10a1f7ace`, configuration `6b92adea`, and KB contract `2aa73ba1b`. The prior
vpsAdmin selected integration workflow `29534366590` completed successfully.
The persistent single-topology bridge cluster is still running and ready. No
source, database, deployment, API, advisory, token, or KB mutation for this
follow-up has occurred yet.

### Framework authorization dependency

The refactored advisory synchronization deliberately restored the canonical
HaveAPI `resource node` input instead of retaining a duplicate scalar
`node_id`. Its scoped-token regression exposed a framework defect: resource
input authorization constructed the referenced Show action's child context
without its resource path, so the global authorization hook saw `#show`
instead of `node#show` and denied a token that correctly held
`node#index`/`node#show`.

HaveAPI is now an affected repository. Its feature worktree is
`worktrees/2026-07-13-security-advisory-automation/haveapi`, branch
`2026-07-13-security-advisory-automation`, based on `origin/master`
`1d55e85`. The local fix passes the referenced resource path to the child
context. A nested-resource regression proves that the pre-authorization hook
receives the full scope and never the empty `#show` scope. The focused
ActiveRecord adapter suite passes 27 examples and focused RuboCop reports no
offenses. No HaveAPI release or package publication has been performed; that
will require explicit user approval after the code is committed and reviewed.

### Simplification implementation and final history rewrite

The kernel-evidence simplification is implemented and committed on top of the
current upstream bases. The final clean heads prepared for mandatory review
are:

- vpsAdmin `241312d3da55565609df3919912d70e8106e0d39`, based on
  `origin/master` `25611d8ff`;
- security-advisories `899cef950d52535b26c85813fa8890342a22f7ad`;
- HaveAPI `f9064b680affc1bf3e0d7b5e529d2fa698c64b06`, based on
  `origin/master` `1d55e85`.

vpsAdmin now introduces the feature in nine focused commits:

- `22b3ca278 api: add Node evidence and advisory schema`;
- `eb886017e api: ingest normalized Node evidence`;
- `8d01810e0 api: expose typed Node evidence resources`;
- `be49cb161 api: synchronize reviewed security advisory drafts`;
- `19c213690 libnodectld: report generic Node evidence`;
- `10b12c22d webui: show Node evidence and advisory review`;
- `803b2487e tests: cover Node evidence deployment and WebUI`;
- `e06a91a32 ci: allow complete API topic matrices`;
- `241312d3d flake: vpsadminos 849282e6b -> dbc03d005`.

The earlier broad but functionally equivalent series is retained at
`backup/2026-07-17-focused-series-pre-split`. A direct tree comparison between
that branch and the final head has no differences. Every rewritten commit
passed the installed vpsAdmin hooks, including migration mapping, API/WebUI
localization, Nix formatting, RuboCop, and PHP CS Fixer. The final branch is
clean and `git diff --check` passes.

security-advisories was rewritten from `ff28f95` into one core evidence
commit, one review-workflow commit, and five dossier commits. Its final tree is
identical to preserved commit `816c1a2`; the full suite passes 74 examples and
RuboCop reports no offenses over 21 files. The installed hook passes.

HaveAPI commit `f9064b6` preserves the referenced resource path during
resource-input authorization. Its complete Ruby server suite passes 348
examples and RuboCop reports no offenses over 235 files. The installed hook
passes. A vpsAdmin scoped-token regression also passes with this one-line
framework fix applied to the ignored local gem cache. The source dependency is
not published, and production vpsAdmin deployment therefore remains gated on
an explicitly approved HaveAPI release.

The vpsAdmin focused application verification passes 62 examples, including
normalized resources and snapshots, supervisor ingestion and reconstruction,
canonical advisory Node inputs, and an exact action-scoped-token workflow.
API RuboCop reports no offenses over 1,428 files. A previous 87-example run
found one timezone-formatting assertion that compared strings; the test now
compares timestamps within one second and the exact rerun passes.

Compatibility remains additive. vpsAdmin accepts legacy Node status reports
and evidence schemas 1 through 4, service-only Nodes remain excluded, and no
Node reboot is required. Evidence schema 7 invalidates only ignored local
security-advisories snapshots, which must be recollected. Rollback can ignore
the additive normalized tables. Configuration and KB contract pins still
point to the previous reviewed vpsAdmin head and will be regenerated only
after mandatory review and any remediation establish the final head.

### Mandatory simplification review

The required single fresh-context reviewer examined vpsAdmin
`25611d8ff..241312d3d`, security-advisories `ff28f95..899cef9`, and HaveAPI
`1d55e85..f9064b6`. Long integration remained paused. The review reported four
Blocking groups:

- malformed schema-4 software identity can raise `NoMethodError` in the
  evaluator instead of producing a fail-closed `unknown` result;
- a time-filtered event collection can omit the reconstruction's first boot,
  while client completeness logic still requires that boot in the returned
  window;
- kernel-configuration parsing, boot-parameter serialization, and system-state
  reconciliation remain in ActiveRecord models despite the requested service
  boundary;
- the rewritten schema, ingestion, WebUI, core security-advisories, and final
  dossier commits still bundle independently reviewable changes.

The reviewer also reported three Important findings: public kernel history
includes inactive hosting/storage Nodes, recovery from a malformed evidence
snapshot can synthesize a false reboot, and sysctl/eBPF scalar fields are not
fully shape-validated at the report boundary. The focused HaveAPI fix had no
finding.

All findings are accepted for remediation. Configuration and KB pins remain
unchanged, the persistent development cluster is not updated, and no long
integration, production write, release, advisory mutation, notification, or
publication will begin until product fixes and the corrected commit split are
reviewed by the same standalone reviewer.

### Mandatory review remediation

All Blocking and Important findings are remediated and committed. Final clean
heads awaiting follow-up review are vpsAdmin
`db634e949bc2a930c84f10b2789bf034bbe97500`, security-advisories
`5b2bc3ee78b1211707a4701e1e52007d0e3ca856`, and unchanged HaveAPI
`f9064b680affc1bf3e0d7b5e529d2fa698c64b06`.

Product fixes are:

- schema-four assessment verifies that every software identity is an object
  before reading its fields, so malformed snapshots produce `unknown` instead
  of `NoMethodError`;
- reconstruction completeness uses the stored completed checkpoint and
  coherent first/through status IDs, independent of which pre-window baseline
  event a time-filtered query returns;
- kernel configuration parsing and writing, boot-parameter serialization, and
  system-state normalization/reconciliation now live in dedicated services;
- public kernel history returns only active hosting/storage Nodes;
- supervisor comparison falls back to the newest valid exact event after a
  malformed current snapshot, preventing a false same-boot reboot event;
- sysctl scalar fields and optional eBPF text fields are validated at the
  payload boundary and malformed shapes remain explicit stored errors.

The vpsAdmin history is now 24 focused commits. Advisory synchronization,
kernel evidence, and system-state migrations are separate, followed by one
generated schema commit. Kernel report modeling, change recording, history
reconstruction, system-state recording/reconstruction, capacity policy, kernel
resources, system resources, advisory synchronization, endpoint inventory,
nodectld reporting, three WebUI behaviors, four integration-test concerns, CI,
and the vpsAdminOS pin each have independent commits. The only deliberate
cross-domain commit is `54ed3bc19 api: ingest Node runtime reports atomically`:
one accepted status must update ordinary status, normalized system state,
rollback capacity cache, kernel events, and current evidence under one Node
lock and database transaction; splitting that adapter would permit one report
to describe conflicting persisted Node states.

security-advisories is split into collector, evaluator, reconciler, token
permissions/self-revocation, operator workflow, five individual CVE dossiers,
and a final cross-dossier validation commit. General token and historical
attestation regressions no longer appear in the GhostLock dossier commit.

Post-remediation verification is green:

- security-advisories passes all 76 RSpec examples and RuboCop over 24 files;
- the affected vpsAdmin API/resource/supervisor suite passes 68 examples and
  focused RuboCop passes over 20 files;
- vpsAdmin WebUI PHPUnit passes 75 tests and 288 assertions after removing the
  now-unused page-description abstraction;
- every final vpsAdmin commit passed installed Nixfmt, migration mapping,
  API/WebUI i18n, RuboCop, and applicable PHP CS Fixer hooks;
- both final source trees exactly match their preserved, verified remediation
  snapshots and all feature commit-message lines are at most 80 characters.

During the isolated hook workflow, a successful `git stash pop` automatically
dropped the initiative stash before a following unconditional drop targeted
the older shared stash. The older stash object was immediately restored under
its original message from Git's reported object ID and remains present. The
reusable precaution is recorded in a dedicated cross-project note. No user
work was lost.

### Mandatory follow-up review passed

The same standalone reviewer rechecked the full final series and reported no
Blocking, Important, or Advisory findings at vpsAdmin `db634e949`,
security-advisories `5b2bc3e`, and HaveAPI `f9064b6`. All seven original
findings are resolved. The reviewer explicitly accepted the supervisor adapter
commit as transactionally indivisible and found the remaining functional,
generated, integration-test, CI, dependency, and dossier splits cohesive.

Residual gates are long supervisor/WebUI/collector/dev-cluster verification,
the generated configuration and KB pins, and the explicit approval required
before any HaveAPI release. The concurrent kernel-configuration
`RecordNotUnique` recovery was not stress-tested directly; its post-conflict
reread is compatible with the configured `READ-COMMITTED` database isolation.
No production write or release is authorized.

### Single evidence schema and HaveAPI associations

The latest review feedback is implemented in clean, unpublished histories.
Current heads prepared for mandatory review are vpsAdmin
`d3d28744a5d8c0f14aa10c51ee207016326702ca`, security-advisories
`8920cb7c0c08fd945e5fb9a97aa819e321dc8181`, HaveAPI
`3bd0f946e0e2a8517faeff7be5a20ff967e7657b`, and vpsAdminOS
`d1df07f89e0cc55d74d388902c59fe3284467248`.

vpsAdmin and nodectld introduce exactly one complete evidence payload schema,
version 1. The original model, ingestion, and reporter commits were rewritten
so schemas 2 through 4 are never introduced and then removed. Pre-feature
nodectld remains compatible by omitting `security_evidence`; unsupported
non-1 evidence is rejected and recorded as incomplete. vpsAdminOS metadata is
also schema 1 in every feature commit, and its exact-nixpkgs commit message no
longer describes unpublished schema transitions. The security-advisories
collector/evaluator history likewise introduces schema 1 and typed API reads
directly rather than carrying follow-up correction commits.

All normalized evidence resources are now model-backed and return real
HaveAPI associations. Node, evidence, event, history-state, livepatch, and eBPF
relationships are resource objects; duplicated `node_id`, `node_name`, role,
active-state, and relationship-ID outputs are removed. In particular,
`NodeKernelHistoryGap` returns `node_kernel_history_state` instead of
`node_kernel_history_state_id`, and `SecurityAdvisory::NodeStatus` returns
`node`. The only raw relation-like output values are `source_status_id`,
`from_status_id`, and `through_status_id`: opaque provenance into internal
Node status samples, which deliberately have no API resource.

The collector reads the canonical active Node inventory with `node#index`,
joins actual evidence through typed associations, and creates an explicit
unresolved local input for a hosting Node whose upgraded reporter has not yet
sent evidence. Its token therefore grants read-only `node#index`/`node#show`
and the Show actions needed for association targets, but no Node mutation.
HaveAPI now preserves the related resource path for authorization of both
resource inputs and ActiveRecord-backed resource outputs. The fixes remain
unreleased; publishing a HaveAPI release and updating vpsAdmin's packaged gem
still require explicit user approval.

At the preceding review checkpoint, the vpsAdmin association conversion was
one API-wide commit followed by one WebUI consumer commit. An initial split
showed that the repository's global i18n contract is invalid while only part
of the association graph has changed. That checkpoint is superseded by the
hook-clean history fold recorded below.

Verification at that checkpoint was green. The vpsAdmin tree passed 85 focused
resource, advisory, supervisor, and model examples with no failures in 10
minutes 17 seconds; every history-rewrite commit ran the installed Nixfmt,
migration, API/WebUI i18n, RuboCop, and applicable PHP hooks.
security-advisories passed its then-current 76 examples and RuboCop, HaveAPI
passed all 349 Ruby server examples and RuboCop over 116 files, and vpsAdminOS
passed its Nixfmt/Overcommit gate.

The isolated vpsAdmin flake commit still points to the pre-rewrite vpsAdminOS
metadata commit. After mandatory review clears the source histories, publish
the reviewed vpsAdminOS feature branch and regenerate that one flake commit to
the exact `730b144ac` metadata revision. Configuration and KB pins remain at
the previous reviewed vpsAdmin revision until the final vpsAdmin head is known.
No long integration test, development-cluster refresh, production write,
advisory mutation, notification, package release, or KB write has begun for
this follow-up.

### Review remediation and association-history fold (2026-07-17)

The mandatory reviewer found that the internal report reader still accepted
legacy shapes, explicit unsupported evidence could preserve stale current
data, two API relationships still used raw IDs, token-scope coverage was
incomplete, API projections had moved into ActiveRecord models, and migration
rollback intent was unclear. These findings are remediated in the rewritten
source histories:

- the report reader now requires the one complete internal shape and the
  payload parser records explicitly unsupported schemas as an invalid current
  snapshot without deriving events;
- omission of `security_evidence` remains the sole rolling-upgrade fallback,
  while an explicit unsupported report replaces stale evidence;
- API presentation is isolated in immutable resource projections rather than
  model methods;
- all available association targets are exercised under the exact read scopes,
  and security-advisories rejects scalar relationship IDs;
- the remaining kernel-history and advisory Node relationships use HaveAPI
  resources, and the token documentation is checked against the configured
  scope list;
- reversible migrations use `change`, while the two MySQL migrations that
  require foreign-key/index rollback ordering retain explicit `down` methods
  with the reason documented.

Before the final history fold, the vpsAdmin head was saved as local branch
`2026-07-13-security-advisory-automation-before-association-fold` at
`51281fa144e82d8c23ea984bd183338681e07041`. The standalone commits
`api: expose Node evidence through associations` and
`webui: consume typed Node evidence associations` were then removed. Their
changes now appear directly in the earlier model, typed evidence,
system-state, advisory synchronization, endpoint inventory, Node WebUI, and
advisory WebUI commits. Each amended boundary passed the installed repository
hooks. The rewritten vpsAdmin tree is byte-for-byte identical to the backup
tree.

Current review heads are vpsAdmin
`40527f781e827a6201fb05c5856af1a495344f9c`, security-advisories
`6ce87ffe2d4addceb5e30b70f23274100d176874`, HaveAPI
`3bd0f946e0e2a8517faeff7be5a20ff967e7657b`, and vpsAdminOS
`d1df07f89e0cc55d74d388902c59fe3284467248`.

Verification on the preserved final trees is green: the focused vpsAdmin
resource, advisory, supervisor, and model suite passes 93 examples; the
resource-only association suite passes 20 examples; the model/supervisor set
passes 34 examples; migration coverage passes 8 examples; security-advisories
passes all 77 examples and RuboCop over 24 files; HaveAPI passes all 349
examples and RuboCop over 116 files. Long integration suites remain paused
until the mandatory reviewer rechecks these final heads.

The first follow-up review found one remaining commit-boundary issue and no
other findings: the pre-existing advisory `node_id`/`node_name` transition,
its public Node authorization guards, and generated locale cleanup had been
folded into the kernel-evidence resource commit. Those changes now remain in
their merged-compatible scalar form through the evidence commit and transition
atomically in `api: synchronize reviewed security advisory drafts`, alongside
the advisory and scoped-token regressions. Both amended boundaries passed the
full hook gate, locale catalogs were regenerated at each boundary, and the
final tree remains byte-for-byte identical to the preserved backup. A final
review of head `40527f781e827a6201fb05c5856af1a495344f9c` passed with no
Blocking, Important, or Advisory findings. The reviewer authorized long
integration testing while retaining the separate HaveAPI release and
production-action approval gates.

### Reporter-owned sysctls and cached boot evidence (2026-07-17)

The final unpublished evidence protocol no longer carries
`sysctl_policy_version` or `security_settings`. `libnodectld` owns the only
tracked-sysctl list, omits the unavailable
`kernel.unprivileged_userns_clone`, and emits `sysctls`. The API structurally
validates and relationally stores exactly the reported map; it has no copied
inventory or completeness policy. security-advisories accepts arbitrary
structurally valid maps and instructs each CVE analysis to discover and require
only the controls relevant to that vulnerability.

The reporter now derives reused paths from shared filesystem roots. It caches
boot identity, kernel, command line and ordered parameters, booted closure
metadata, and kernel configuration on first collection. Current closure
metadata, loaded modules, sysctls, livepatches, and eBPF state remain dynamic.
The cached configuration text is still sent initially and at the existing
six-hour recovery interval, without rereading or rehashing `/proc/config.gz`.

Backup refs created before history rewriting are:

- vpsAdmin `backup/2026-07-17-security-evidence-refactor-vpsadmin` at
  `d650b7fd8b6794a9a5b7e81e8328461831b1bd29`;
- security-advisories
  `backup/2026-07-17-security-evidence-refactor-security-advisories` at
  `6ce87ffe2d4addceb5e30b70f23274100d176874`;
- vpsfree-cz-configuration
  `backup/2026-07-17-security-evidence-refactor-vpsfree-cz-configuration` at
  `77ec4722010edc9cccaa7354577ef149cd721574`;
- vpsadmin-kb-captures
  `backup/2026-07-17-security-evidence-refactor-vpsadmin-kb-captures` at
  `9ee2f48a23870fcf4b5ee8f11b8d265a30d7bd86`.

Current committed heads are vpsAdmin
`1fc8d245845cca1c39ffc451096f4495d4810361`, security-advisories
`0b0b69d75cfd67cc740521b81dbd6926e62a8b1f`,
vpsfree-cz-configuration
`d86fd3ee252b8ee3f1b22a6136860e212fffbba9`, and
vpsadmin-kb-captures
`c4bb0afb9eaf89b4cd4117bb6cfd150a9797f623`. The two source branches are
force-pushed. Configuration and KB pins are committed locally and await the
mandatory review before their force-push.

Quick verification is green:

- libnodectld evidence/status specs: 10 examples, no failures;
- affected API operation/reconstruction specs: 17 examples, no failures;
- evidence migration specs: 2 examples, no failures;
- security-advisories: 77 examples, no failures, and RuboCop clean over all
  24 files;
- touched vpsAdmin API and libnodectld Ruby files: RuboCop clean;
- the KB contract check: valid 38-control/29-path contract, 15 test runs with
  67 assertions, and a valid 118-image capture inventory.

Every rewritten vpsAdmin commit passed the installed Nixfmt, migration,
WebUI/API i18n, RuboCop, and commit-message hooks. security-advisories commits
passed their installed RuboCop and commit-message hooks. The source histories
contain none of `sysctl_policy_version`, `SYSCTL_POLICIES`, or
`security_settings`; a negative reporter spec is the sole intentional history
reference to the omitted sysctl.

Rolling compatibility is unchanged: deploy the API/services first, continue
accepting old status updates that omit evidence, then deploy nodectld to staging
and the fleet without rebooting Nodes. Only intermediate unpublished payloads
from this feature branch are unsupported. Long supervisor, WebUI, scoped-client,
and dev-cluster checks remain paused for the mandatory standalone review.

### Mandatory reporter/sysctl review remediation

The standalone reviewer confirmed the vpsAdmin reporter, storage, history,
commit split, exact downstream pins, and rolling deployment design. It found
one Blocking omission in security-advisories: the workflow told analysts to
identify relevant sysctls, but the dossier could not declare them, so an empty
map or unavailable relevant control did not fail closed. It also found that the
advisory-side name validator did not mirror vpsAdmin's dotted-name/255-byte
contract and that `docs/evidence.md` still described the superseded versioned
policy.

All findings are remediated in the rewritten 14-commit security-advisories
history at `41d19eeb4bec50f0c63d20867d2dc1e442a5bf4e`:

- `platform.required_sysctls` maps each relevant sysctl to a nonempty unique
  list of exact effective string values reviewed for the conclusion;
- current and historical snapshots remain `unknown` when a required sysctl is
  missing, unavailable, unreadable, or outside the reviewed value set;
- one `SysctlEvidence` module owns the vpsAdmin-compatible generic name/value
  validation used by the collector, evaluator, and historical attestations;
- the collector rejects malformed typed sysctl rows before accepting the
  reconstructed snapshot;
- the schema, operator instructions, evidence contract, fixture, and all five
  initial dossiers express the final contract directly; the five current
  dossiers explicitly declare `{}` because their analyses do not depend on a
  sysctl value.

Post-rewrite verification passes 82 RSpec examples and RuboCop over 25 files;
`git diff --check` is clean. Added regressions cover malformed dossier
requirements, malformed collected/evaluated names, missing/unavailable/missing
effective values, unreviewed values, and accepted values. The same reviewer is
performing the required follow-up check; long integration remains paused until
that gate is cleared.

### Runtime evidence integration follow-up (2026-07-17)

The reporter/sysctl reviewer cleared all findings at security-advisories
`41d19eeb4bec50f0c63d20867d2dc1e442a5bf4e`. The supervisor
`runtime-ingestion` integration suite then passed all 10 examples, including
the rolling-deployment case where an older nodectld omits evidence.

The admin-cluster WebUI integration reached seven passing browser examples but
failed the kernel-parameter page because the API had stored the current report
as an invalid evidence gap. Test artifacts showed nodectld reporting normally
after startup, and source comparison identified the contract mismatch:
vpsAdminOS uses valid Nix booleans for configured sysctls such as
`kernel.dmesg_restrict = true`, while schema-1 validation accepted only string
and numeric scalars. The unrelated initial nodectld restarts were caused by a
pre-existing CPU-sampling `NaN` serialization error and recovered before the
browser checks.

vpsAdmin now accepts boolean configured sysctl scalars and normalizes them to
their string representation in relational evidence. The regression uses
`false` and asserts the stored report value is `"false"`. Two full-matrix CI
failures were also traced to shared seed Nodes whose role/activity had been
changed by other examples; the kernel-evidence and advisory resource specs now
restore their required active host roles in setup.

The combined supervisor, Node-kernel-resource, and security-advisory resource
run passes 69 examples with no failures. Every fixup passed the installed
Nixfmt, migration, WebUI/API i18n, and RuboCop hooks. The changes were folded
into their original model, ingestion, resource, and advisory commits. The
pre-follow-up head is preserved as
`backup/2026-07-17-security-evidence-runtime-fixes` at
`1fc8d245845cca1c39ffc451096f4495d4810361`; the rewritten vpsAdmin head is
`b1551d3da688e4bce3914734753d8d79bff51c8f`.

A fresh mandatory reviewer is checking this final follow-up before the failed
WebUI suite is rerun. Downstream configuration and KB pins still point to the
previous vpsAdmin head and must be regenerated after that review.

### Final integration, pins, and release blocker (2026-07-18)

The fresh mandatory review of vpsAdmin
`b1551d3da688e4bce3914734753d8d79bff51c8f` found no Blocking, Important, or
Advisory issues and cleared the integration gate. The final branch has 24
feature commits, is pushed, and differs from the pre-follow-up backup only by
the reviewed four-file semantic correction folded into its owning commits.

Long integration is green on that exact head:

- `webui#admin-cluster` passed its complete three-VM Playwright flow in 870.31
  seconds, including the previously failing kernel-parameter evidence page;
- `supervisor/runtime-ingestion` passed all 10 examples in 554.04 seconds,
  including acceptance of the pre-feature Node status without evidence.

Generated downstream pins are pushed. vpsfree-cz-configuration
`feb859be6d5a675ce985dca5755a332ffc690e76` contains separate confctl-generated
commits for `vpsadminStaging` and `vpsadminServices`, both at `b1551d3da`, after
the isolated `vpsadminosStaging` pin at `730b144ac`. vpsadmin-kb-captures
`89ea2ea1e9aeb7e518cf170d97ea35c87b8423b5` pins the same vpsAdmin revision and
its followed vpsAdminOS revision. `nix flake check` passed, and `bin/check`
validated the 38-control/29-path contract, 15 tests with 67 assertions, and all
118 PNGs.

The verified session's old bridge cluster was the only running dev cluster. It
did not exit before the normal stop timeout, so `devcluster` killed the runner,
removed its state, and built a fresh single-node bridge cluster. It is ready at
the standard aitherdev URLs. Services and the nested WebUI container both
report exact vpsAdmin revision `b1551d3da`; the public header links to that full
commit. Node 101 reports schema 1 for kernel `6.12.95`, 9 ordered boot
parameters, 34 relational sysctls, and zero evidence errors. The original Nix
boolean values are accepted and stored as configured `true` while their
effective values are `1`.

The least-privilege token was created successfully with 34 scopes and mode
0600. Collection then failed read-only before writing `.state` or any advisory:
released HaveAPI 0.29.3 serialized `node_cgroup_state.node` as
`{"_meta":{"resolved":false,"authorized":false}}`, without an ID, even though
the token has `node#show`. The existing HaveAPI feature branch at
`3bd0f946e0e2a8517faeff7be5a20ff967e7657b` fixes output association resource
paths; vpsAdmin still packages 0.29.3. Granting `node_cgroup_state#show` would be
an unrelated-permission workaround and is intentionally rejected. The
temporary token was revoked and its file removed.

Completing the scoped collector requires explicit approval to release the
reviewed HaveAPI changes and bump vpsAdmin's packaged gem, followed by another
vpsAdmin/configuration/KB pin and bridge-cluster refresh. No draft advisory,
publication, notification, package release, production deployment, or KB write
was performed. GitHub RSpec and RuboCop are green for security-advisories
`41d19eeb`; current vpsAdmin CI is green for RuboCop, libnodectld, WebUI,
client, and i18n, with the final API matrix still in progress. A superseded CI
run for the old vpsAdmin head was cancelled.

### HaveAPI release approval (2026-07-18)

The user approved merging the reviewed HaveAPI fixes into master, backporting
them to the supported 0.29 line, publishing 0.29.4, and updating every HaveAPI
consumer in vpsAdmin.

Current exact refs before release work are HaveAPI master
`1d55e85b57569ff00b4bcd12b158ea77fba24ed6`, feature head
`3bd0f946e0e2a8517faeff7be5a20ff967e7657b`, and `haveapi-0.29`/`v0.29.3`
`268fd6c8a2eef3635d8a518bc1a35467959334a0`. The feature branch contains two
commits and fast-forwards master. The supported patch branch will receive both
with `cherry-pick -x` before the version commit.

The release also requires the standalone `haveapi-client-php` master/tag
because HaveAPI's shared version task updates the PHP client marker and vpsAdmin
WebUI resolves that package from its independent repository. Temporary master,
release, and PHP integration worktrees will be recorded here when created.

### HaveAPI 0.29.4 release preparation (2026-07-18)

HaveAPI master was fast-forwarded and pushed at
`3bd0f946e0e2a8517faeff7be5a20ff967e7657b`. The supported patch worktree is
`worktrees/2026-07-13-security-advisory-automation/haveapi-0.29.4` on branch
`2026-07-13-security-advisory-automation-0.29.4`. It contains the two
`cherry-pick -x` association backports, the release-order backport, and the
separate version commit `6a8ca97fc8c0f3db4ef33fd9d9f62703d807572f` on top of
v0.29.3.

The Ruby server suite passes 349 examples, RuboCop passes all 116 files, the
JavaScript suite passes 39 examples, and the PHP suite passes 49 tests with 136
assertions. `make release` succeeded inside the top-level Nix shell after
installing the declared JavaScript development dependencies; the repository
does not carry a lockfile or provision `node_modules` in its shell. Built gem
metadata reports 0.29.4 and the expected `~> 0.29.4` internal dependencies.

The standalone PHP worktree is
`worktrees/2026-07-13-security-advisory-automation/haveapi-client-php` on branch
`2026-07-13-security-advisory-automation-0.29.4`, with synchronized version
commit `44bb8d1e4f786f3a84794c5ffe845d9afd2d50e5`. Composer validation succeeds
with only its existing warning about the explicit package version. Neither the
HaveAPI nor standalone PHP release branch has been pushed, tagged, or
published. Both now await the mandatory standalone release review.

The mandatory reviewer found no Blocking or Advisory issues and one Important
release-integrity issue: the shared publish target uploaded the server before
the matching Ruby client required by both the server and Go generator. Master
now fixes this in `555fd7e20d520409fb19ed72c46600b00f14d57b`; its
`cherry-pick -x` backport is
`ee27701d46ce6458360ef5c9f9a2417401d3f45d`, placed before the rewritten
version commit. `make -n publish` now orders the Ruby client, server, Go
generator, and JavaScript package. The pre-remediation release head is retained
at `backup/2026-07-18-haveapi-0.29.4-pre-publish-order`. Artifact contents and
checksums are unchanged. The same reviewer is performing focused follow-up.

The focused follow-up found no remaining Blocking, Important, or Advisory
issues. It confirmed the master and release patches are identical, the version
commit rewrite is patch-identical, artifacts are unchanged, and the publication
gate is clear. The remaining risk is the unavoidable non-atomic sequence across
RubyGems, npm, GitHub, and Composer; every published component will therefore
be verified before vpsAdmin is updated.

HaveAPI `master` is pushed at
`555fd7e20d520409fb19ed72c46600b00f14d57b`; `haveapi-0.29` and annotated tag
`v0.29.4` are pushed at `6a8ca97fc8c0f3db4ef33fd9d9f62703d807572f`.
All seven branch workflows and all seven tag workflows passed. The approved
publish target successfully registered `haveapi-client`, `haveapi`, and
`haveapi-go-client` 0.29.4 on RubyGems and `haveapi-client@0.29.4` on npm.
Independent registry queries list all four versions; npm reports tarball SHA-1
`3e5a4c7bb2271e78130259cdde72d9ad3dce2d69`.

The standalone PHP feature branch, master, and annotated `v0.29.4` tag are
pushed at `44bb8d1e4f786f3a84794c5ffe845d9afd2d50e5`. Packagist resolves
`haveapi/client` 0.29.4 to that exact commit. Temporary master/release
integration worktrees were removed; the initiative feature worktrees and
branches remain. vpsAdmin dependency regeneration can now use only public
0.29.4 artifacts.

### vpsAdmin HaveAPI 0.29.4 adoption (2026-07-18)

Every tracked HaveAPI consumer now resolves 0.29.4: API, vpsAdmin client,
download mounter, mail templates, outage-report utility, WebUI PHP client, and
both bundled JavaScript clients. The API/client/download-mounter package locks
and Nix gemsets were regenerated from RubyGems. The WebUI Composer lock and
Composer-to-Nix source resolve `haveapi/client` to exact standalone revision
`44bb8d1e4f786f3a84794c5ffe845d9afd2d50e5`; no unrelated Composer package was
changed. Both bundled JavaScript files have release artifact SHA-256
`d848de52fa3999e75bcba8d9764012a190bf6a8c495b5e4066a4c605c6a171d6`.

The initial repository package task hit the known Bundix gem-environment
mismatch after deleting `packages/api/Gemfile.lock`. A first clean-environment
retry also ran from the wrong directory because the root development shell
returns to the repository root. The documented clean Bundix command was rerun
with `cd packages/<name>` inside the shell; all three generated package sets
then contain only 0.29.4. The working-directory lesson is recorded in
`notes/vpsadmin/2026-07-18-vpsadmin-shell-package-working-directory.md`.

The exact scoped-token advisory workflow now creates a cgroup state, reads
`node_cgroup_state#index` with `node#show` but without
`node_cgroup_state#show`, and asserts that the returned typed Node contains its
ID. Its first run exposed the missing spec fixture rather than a product error;
after adding the explicit state, the exact example passes.

Quick validation is green: the scoped example passes, the touched API spec is
RuboCop-clean, API i18n health passes, WebUI passes 75 tests with 288
assertions, Composer validates and reports exact 0.29.4/`44bb8d1`, and Nix
builds pass for API, client, download mounter, console router, and WebUI. The
complete installed vpsAdmin pre-commit suite passes migration specs, API/WebUI
i18n, Nixfmt, PHP-CS-Fixer, and RuboCop.

The complete dependency update and scoped-token regression are committed as
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc` (`deps: update HaveAPI to
0.29.4`) on top of rebased, previously reviewed vpsAdmin head
`f963e542f3ebeda9e727f49ac7e0e97453023fc8`. The worktree is clean. The commit
awaits the mandatory standalone dependency-integration review before push,
downstream repins, and dev-cluster refresh.

Upstream master advanced to `400a20fad29e27d3256a3345e6c6c21354e51672`
with a generated WebUI Guzzle 7.15 update before the feature push. The complete
25-commit feature series was rebased onto it after preserving pre-rebase head
`f287fc3c347c933241a76812a3dbfec5b4b8153f` at
`backup/2026-07-18-pre-haveapi-0.29.4-rebase`. Range-diff reports all 25 feature
patches unchanged. The final WebUI lock/Nix files contain both master’s Guzzle
7.15 revision and HaveAPI 0.29.4; compared with the backup feature tree, those
two generated files are the only changes. The combined WebUI again passes 75
tests with 288 assertions and its Nix package builds successfully.

The fresh mandatory reviewer cleared rebased head
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc` with no Blocking, Important, or
Advisory findings. It confirmed the stable dependency patch, all tracked
consumer versions, exact PHP/JS artifacts, non-vacuous least-privilege
regression, upstream Guzzle retention, and unchanged compatibility contract.
The push/integration gate is clear; remaining assurance is the current-head CI
and bridge-cluster scoped-token workflow.

### HaveAPI 0.29.4 rollout verification (2026-07-18)

The reviewed vpsAdmin branch is pushed at
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc`. The earlier API workflow failure
on superseded head `b1551d3da688e4bce3914734753d8d79bff51c8f` was investigated from its
logs: released HaveAPI 0.29.3 omitted authorized typed Node associations on
evidence output and rejected the advisory Node resource input. These are the
two association-context defects fixed by HaveAPI 0.29.4. The exact current
regression passes locally and exercises both the required `node#show` scope and
the absence of the unrelated `node_cgroup_state#show` scope.

Downstream pins were regenerated from their current upstream masters and
pushed. vpsfree-cz-configuration
`4e5922f145181fe6d7066c3005a1eb0426864bda` contains separate generated
confctl commits for vpsAdminOS staging
`730b144ac36b6bded25d84e47aa33020b8dae916`, vpsAdmin staging
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc`, and vpsAdmin services at the same
vpsAdmin revision. `nix flake check` passes. vpsadmin-kb-captures
`b5adc2fcb7b98eb899e233d5e4b486f6ea27a95a` pins exact vpsAdmin revision
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc`; `bin/check` validates all 38
controls, 29 paths, 32 concepts, 65 bindings, 15 test runs, and 118 capture
images. This dependency-only change does not alter the visible WebUI contract,
so no KB page or screenshot was changed.

The existing single-node bridge cluster was updated in place without a reboot.
The API, supervisor, WebUI container, and nodectld are active. Services and
node1 carry `/etc/vpsadmin/build-info.json` revision
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc`; the API identifies HaveAPI 0.29.4
and the public WebUI header links to the same exact vpsAdmin commit. Node 101
correctly reports booted vpsAdmin revision
`b1551d3da688e4bce3914734753d8d79bff51c8f` and current revision
`b216a5fcb5bc65b9e8472a512ac88e5aac68becc`, demonstrating an activated
closure change without falsely claiming that the new vpsAdmin revision was
booted.

The end-to-end least-privilege workflow now succeeds. A temporary permanent
development token was issued with exactly the documented 34 scopes and file
mode 0600. `collect` succeeded without `node_cgroup_state#show` and saved one
active hosting Node with schema 1, kernel 6.12.95, six requested configuration
options, nine ordered boot parameters, 34 sysctls, exact software revisions,
kernel/deployment history, cgroup v2 history, and no evidence errors. All five
dossiers validate and evaluate the complete active Node set. Each result is
deliberately `unknown` because the fresh development cluster has neither
kernel history back to the dossiers' required `2026-01-01` boundary nor a
completed reconstruction for that period. Dry-run synchronization for every
CVE produced a new-draft plan with the typed Node 101 status and performed no
mutation. No advisory draft, publication, notification, or KB production write
was made. The temporary token was revoked and its file removed.

Current-head GitHub validation is green wherever complete. API migration,
client, WebUI, console-router, RuboCop, download-mounter, i18n, and libnodectld
workflows all passed at `b216a5fcb5bc65b9e8472a512ac88e5aac68becc`. In API matrix run
`29639019554`, 25 of 26 shards have passed with no failures; only the full
platform shard remains in progress. Self-hosted integration run `29639019522`
is queued for its runner. These two externally running checks are the only
remaining validation; all intended implementation, review, publication,
repinning, cluster verification, and scoped dry-run work is complete.

### Deployment runbook and configuration provenance (2026-07-18)

This follow-up is documentation and implementation only. No production host
was activated, migrated, backfilled, rebooted, or otherwise changed. The
operator runbook is committed in vpsfree-cz-configuration as `92860594`
(`docs: add vpsAdmin evidence deployment runbook`). It documents the manual
api1 migration, api2 and WebUI rollout, the two idempotent reconstruction
tasks, no-reboot staging-node validation, gradual production rollout, and
rollback. The seven feature migrations are all core API migrations; there are
no feature plugin migrations.

confctl worktree
`worktrees/2026-07-13-security-advisory-automation/confctl` uses branch
`2026-07-13-security-advisory-automation` at
`e61385ef8a6eb9242ef39832bdc0eea1f68f28b3`. It embeds optional schema-1
configuration metadata containing the exact configuration-flake revision and
dirty flag in NixOS and vpsAdminOS closures. RSpec passes 35 examples,
RuboCop passes 120 files, Nixfmt and all Overcommit hooks pass. A full
`nix flake check --no-build` encounters the same invalid vpsAdminOS source-path
error on untouched upstream `8ccb94d317`; this is not caused by the feature.
The branch is pushed.

vpsAdmin history was backed up at
`backup/2026-07-18-configuration-provenance-vpsadmin` and rewritten so the
configuration identity, scalar sysctl conversion, and dirty-revision model fix
are folded into their owning commits. The clean 25-commit feature head is
`2e2f6dc496b5b99fdef097a958a5cf35046ae751`. Nix booleans are reported as
kernel-facing `1` and `0`; optional booted/current
`vpsfree_cz_configuration` revisions are stored, exposed, linked in the admin
WebUI, and rejected when present but malformed. Focused reporter, persistence,
API, WebUI, translation, and all pre-commit checks pass. The rewritten branch
is pushed and current-head GitHub workflows are running.

security-advisories history was backed up at
`backup/2026-07-18-configuration-provenance-security-advisories` and rewritten
so optional configuration provenance is part of the original collector,
evaluator, dossier validation, evidence digest, and general agent guidance.
The clean 14-commit feature head is
`55e26c3ad6bc548e7b40b0cc1dddd47c41e2da11`. All 84 RSpec examples and
RuboCop over 25 files pass. The rewritten branch is pushed and current-head
GitHub workflows are running.

vpsfree-cz-configuration pins the final vpsAdmin revision for staging and
service closures through generated commits `33e07297` and `2c3bc792`, contains
the runbook in `27311f57`, and pins confctl through generated commit
`e45eca0e`. Its current exact head is
`e45eca0e947626de9f64c86b80e8696a3b77bb9d`. The temporary replacement pins
were folded into their original generated commits; backup ref
`backup/2026-07-18-pre-provenance-pin-fold-config` retains the pre-fold head.
The final tree is byte-identical. `nix flake check --no-build` passes. Before
the history-only fold, a local
`confctl build -y cz.vpsfree/vpsadmin/int.api1` completed and the resulting
`/etc/confctl/configuration-info.json` contained its then-current exact
revision with `revisionDirty: false`; the generation was built but not
activated. A current-head build remains part of post-review integration. The
rewritten feature branch is pushed.

vpsadmin-kb-captures pins exact finalized vpsAdmin revision `2e2f6dc496...` in
commit `fdb788f`. The temporary replacement pin was folded into its owning pin
commit; backup ref `backup/2026-07-18-pre-provenance-pin-fold-kb` retains the
pre-fold head and the final tree is byte-identical. Current-head
`nix develop -c bin/check` passes with 38 controls, 29 paths, 32 capture
concepts, 65 bindings, 15 test runs, and 118 PNGs. The semantic contract did
not drift, so no screenshot or production KB page changed. The rewritten
feature branch is pushed.

The mandatory standalone review at task
`mandatory_configuration_provenance_review` completed with no Blocking,
Important, or Advisory findings and cleared the post-review integration gate.
It confirmed coherent commit boundaries, correctly folded provenance changes,
isolated generated pins, and byte-identical configuration/KB rewrite results.
Residual verification is the current configuration-head build, current-head
GitHub and bridge-cluster integration, and scoped no-reboot collection. The
review also notes that optional-identity removal and current-only to
booted-and-current transitions rely on the generic reconciliation coverage
rather than dedicated end-to-end cases. The deployment runbook was reviewed
statically and none of its operational commands were executed.

Post-review confctl integration exposed three test-harness assumptions. The
flake fixture carried a stale lock into its initial commit, the expected Git
revision was captured outside the example-sharing context, and vpsAdminOS
deployment replaces the bootstrap VM test shell. The final test prepares its
lock before the clean commit, captures the revision in `before(:context)`, and
reads deployed metadata through the same confctl SSH transport used by the
other post-switch checks. These corrections are folded into the original
confctl feature commit at final head
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`.

The first full `deploy/flakes` attempt was not accepted or blindly rerun: its
artifacts showed the clean metadata file was initially absent and later dirty
metadata was correct. Focused diagnostic runs then proved exact clean JSON and
identified the example-context and vpsAdminOS-shell assumptions. The final
fresh `deploy/flakes` run passes all 23 examples in 1017.94 seconds, including
clean NixOS/vpsAdminOS and dirty NixOS metadata.

The same standalone reviewer then found that the shared harness also serves
legacy swpins mode, where no configuration identity exists. The final test
gates value assertions to flake mode and explicitly verifies file absence in
swpins mode. `deploy/swpins` passes all 23 examples in 555.28 seconds. The
reviewer's focused remediation pass reports no remaining Blocking, Important,
or Advisory findings and clears the updated integration gate.

vpsfree-cz-configuration now pins final confctl head through the one generated
commit `10a5ae21` and has exact head
`10a5ae213c8ee63601b12579a698f89913bf3fc8`. The replacement pin was folded
into its owning generated commit; backup
`backup/2026-07-18-pre-swpins-confctl-repin` has the byte-identical pre-fold
tree. Final `nix flake check --no-build` and
`confctl build -y cz.vpsfree/vpsadmin/int.api1` pass, and the generated
configuration metadata contains exact revision `10a5ae21...`, clean state,
and schema 1. No generation was activated.

### Final-head integration and dev-cluster evidence (2026-07-18)

Post-review integration ran against final vpsAdmin head
`2e2f6dc496b5b99fdef097a958a5cf35046ae751`. The vpsAdminOS supervisor VM
scenario `supervisor/runtime-ingestion` passes all 10 examples in 734.61
seconds, including acceptance of a legacy Node status without security
evidence. The Playwright-backed `webui#admin-cluster` scenario passes its full
browser flow in 946.0 seconds. It covers the cluster and Node navigation plus
kernel, parameter, sysctl, system, and software history pages at the fixed
test viewport.

The existing bridge-network development cluster
`2026-07-13-security-advisory-automation` was updated in place without a
reboot. The API, supervisor, WebUI container, and nodectld are active. Services
report exact clean vpsAdmin revision `2e2f6dc496...`. Node 101 still truthfully
reports booted vpsAdmin revision `b1551d3da...` while its current activated
closure reports `2e2f6dc496...`; the booted and current nixpkgs and vpsAdminOS
identities are also exact native revisions. Optional vpsfree-cz-configuration
identity is absent in this confctl-less development closure, as designed.

A newly issued temporary development token used exactly the collector's 34
documented scopes and file mode 0600. At final heads, `collect` saved schema-7
evidence for the one active hosting Node: kernel 6.12.95, ordered boot
parameters and raw command line, selected parsed configuration options,
runtime modules and mitigations, cgroup history, software generations, and no
reporting errors. Current `kernel.dmesg_restrict` is correctly represented as
configured `1` and effective `1`. The older historical snapshot retains the
pre-normalization configured string `true`, rather than rewriting historical
evidence.

All five dossiers validate and evaluate with a typed result for Node 101. Each
result is conservatively `unknown` because this fresh cluster does not cover
the dossiers' required history boundary and has no completed reconstruction
for that period. Dry-run reconciliation succeeds for all five CVEs, proposes
one advisory and one Node status each, reports `dry_run: true`, and performs no
API writes. The temporary token was then revoked through its own scoped action
and its local file was removed.

Exact remote refs match every final feature/release head, all inspected
worktrees are clean, and all remotes use SSH. Current-head confctl RSpec,
RuboCop, and test workflows pass; security-advisories RSpec and RuboCop pass;
vpsAdmin's client, API, WebUI, libnodectld, i18n, RuboCop, console-router, and
download-mounter workflows pass. The vpsAdmin self-hosted integration workflow
`29651792649` remains in progress on its current head and is being monitored.
No superseded queued or in-progress workflow exists on any rewritten feature
branch. HaveAPI 0.29.4 release/backport workflows are green; repositories
without Actions on mechanical pin heads retain the local checks recorded
above.

### Interrupted RPC reliability follow-up recovery (2026-07-19)

The resumed session recovered two unfinished vpsAdmin paths:
`libnodectld/lib/nodectld/rpc_client.rb` and the new
`libnodectld/spec/nodectld/rpc_client_spec.rb`. The implementation retries the
complete RPC channel setup on a fresh channel after a timeout at any setup
boundary. It retains ten delayed retries, a final attempt, and the existing
ten-second delay. Six deterministic examples cover channel creation,
exchange declaration, reply-queue declaration, binding, subscription, and
retry exhaustion.

The partial change is not treated as the cause of the existing self-hosted CI
stalls. Run `29651792649` attempt 1 had one unrelated invalid Nix-store path
while evaluating `storage/vps-hard-delete` and stalled at the final queue
release in `storage/rollback-across-trees`. Attempt 2 stalled inside
`osctl ct send state` in `vps/swap-across-locations` after 116 other scenarios
passed. Earlier run `29639019522` stalled in swap and
`vps/migrate-with-subdataset-mounts`. The targeted scenarios will be rerun
after review to classify this evidence independently.

Initial focused RSpec passed 6 examples and focused RuboCop passed. The first
full libnodectld run reported 17 `LoadError` failures because the shared
`/tmp/dev-ruby-gems` cache contained truncated Bundler and RSpec gem trees.
No process was using that cache, so it was preserved as
`/tmp/dev-ruby-gems.incomplete-20260719133451` and rebuilt through the declared
Nix shell. The resulting full suite passed 419 examples. The reusable failure
mode is recorded in
`notes/vpsadmin/2026-07-19-libnodectld-incomplete-ruby-cache.md`.

All Overcommit checks passed and the follow-up was committed before rebasing
as `6cbbe5c0f`. A recovery ref named
`recovery/2026-07-13-security-advisory-automation-pre-20260719-rebase`
preserves that exact pre-rebase head. Upstream master had advanced from
`400a20fad` to `81f7460c5` through scheduled Ruby and WebUI dependency updates.
The complete 26-commit feature series rebased without conflicts. Range-diff is
identical except that upstream had already supplied the generated lockfile and
gemset portions of the HaveAPI dependency commit. The rebased RPC commit is
`d8d12e9d6`; current rebased head is the same commit.

Post-rebase verification passes: full libnodectld RSpec has 419 examples and
no failures with seed 55996, and focused RuboCop inspected the implementation
and spec without offenses. The complete post-rebase Overcommit run also
passes. The mandatory standalone review remains before integration. Existing
configuration and KB capture pins still refer to the pre-follow-up vpsAdmin head
`2e2f6dc496b5b99fdef097a958a5cf35046ae751` and must not be updated until the
reviewed final head is known.

The mandatory standalone review reported one Blocking finding and no
Important or Advisory findings. Bunny 2.24.0 routes every channel-open reply
through a connection-wide continuation queue without retaining the AMQP frame
channel number. A delayed `Channel::OpenOk` from a timed-out first channel can
therefore satisfy the next channel's open, even though it has a different
number. The original direct-timeout spec did not model this queue. Long
integration remained correctly gated.

The remediation moves channel-open timeout handling into `NodeBunny`. Channel
creation is serialized; on timeout it identifies the opening channel, closes
the transport immediately, removes that orphan through Bunny's pre-recovery
callback, waits for a new `recovery_completed` generation, and only then
propagates the original timeout to `RpcClient`. Bunny resets the
connection-wide continuation queue while starting the new transport and
recovers every remaining long-lived channel. The orphan is removed before
recovery and its allocator ID is released, avoiding one unreachable recovered
channel per retry. Later exchange and queue setup timeouts remain isolated by
using a fresh registered channel.

The regression uses Bunny's real session continuation queue: it reproduces a
timed-out open followed by a delayed `Channel::OpenOk`, verifies forced
transport recovery, verifies the stale continuation is discarded, verifies
the orphan registry entry is removed and its ID reusable, and verifies the
original timeout is re-raised. Focused RSpec passes 7 examples; focused
RuboCop passes all four implementation/spec paths; full libnodectld RSpec
passes 420 examples with seed 51908; and every Overcommit and commit-message
hook passes. The corrected focused commit and current head is
`c7dd83878a4c87dafa42c67907ec3c08db8163ea`. The same standalone reviewer must
clear this remediation before the long integration gate opens.

The same standalone reviewer completed the focused remediation pass with no
Blocking, Important, or Advisory findings. It independently reran the focused
suite with 7 passing examples and confirmed the continuation reset, orphan
cleanup, allocator reuse, recovery-generation predicate, and mutex/callback
ordering. It also confirmed the remaining 25 commits are unchanged and opened
the long integration gate. The accepted residual contracts are the intentionally
unbounded Bunny recovery wait, isolated use of Bunny 2.24.0 private-documented
internals with regression coverage, the ordinary forced-recovery window for
other NodeBunny consumers, and deliberate retention of channels that time out
after opening so their numbers cannot be reused unsafely.

All post-review long integration gates pass on
`c7dd83878a4c87dafa42c67907ec3c08db8163ea`. The
`supervisor/runtime-ingestion` scenario passed all 10 examples and the complete
test in 583.67 seconds, including the legacy status without security evidence.
`vps/swap-across-locations` passed its cross-location VPS/IP swap example in
696.91 seconds and the complete test in 1296.75 seconds.
`vps/migrate-with-subdataset-mounts` passed its mounted-subdataset remapping
example in 452.45 seconds and the complete test in 1081.22 seconds.
`storage/rollback-across-trees` passed both examples, including backup-head
switching and future incremental backups, and completed in 1127.89 seconds.
The previous container-send and final queue-release stalls did not reproduce;
these isolated results provide no basis to attribute them to the RPC recovery
change.

The reviewed vpsAdmin branch was force-pushed with an explicit lease from the
expected old remote head `2e2f6dc496...` to
`c7dd83878a4c87dafa42c67907ec3c08db8163ea`. Upstream master remained
`81f7460c5cc9b26cf3deffefa55044fd180d2c1c`. No superseded queued or running
workflow existed after the push. Current-head WebUI PHPUnit, API migrations,
RuboCop, client, i18n, libnodectld, download-mounter, and console-router
workflows pass. API topic-parallel specs and the self-hosted integration
workflow remain in progress and are being monitored.

Downstream pins were regenerated and pushed from clean worktrees whose master
refs had not advanced. vpsfree-cz-configuration has separate generated confctl
commits `ca68ee77` and `4aa97c28` for `vpsadminStaging` and
`vpsadminServices`, both at exact vpsAdmin head `c7dd83878`. Final configuration
head is `4aa97c28`; `nix flake check --no-build` passes. The Nix development
shell's generated `.bin/` and `.bundle/` caches were moved outside the worktree
after the pin and push commands, leaving it clean.

vpsadmin-kb-captures head `f0d9e6c6` pins exact vpsAdmin revision `c7dd83878`
in `flake.nix`, the lock, capture inventory, and navigation contract. Its full
`bin/check` validates 38 controls, 29 paths, 32 capture concepts, 65 bindings,
both test groups, and all 118 PNGs. The RPC recovery and upstream rebase do not
change the member-visible WebUI contract, so no semantic fingerprint,
screenshot, KB candidate, staging content, or production page changed.

The verified single-node bridge cluster was updated in place with
`devcluster update ... all`. It remains running and ready; API, supervisor,
WebUI, and nodectld are active. Services and node1 carry exact clean vpsAdmin
revision `c7dd83878a4c87dafa42c67907ec3c08db8163ea`. The update did not reset or
reboot the Node: evidence retains boot ID
`048f8a1d-2327-475e-9ac0-8d61bb8f47bc`, booted vpsAdmin revision
`b1551d3da688e4bce3914734753d8d79bff51c8f`, and current vpsAdmin revision
`c7dd83878a4c87dafa42c67907ec3c08db8163ea`.

A temporary permanent development token was issued through the repository
token issuer with exactly 34 documented scopes and mode 0600. All five dossiers
validate. Collection saved schema-7 evidence for the sole active hosting Node,
with kernel 6.12.95, six requested configuration options, ordered boot
parameters, runtime evidence, exact software generations, and no errors. All
five evaluations are conservatively `unknown` because the fresh cluster lacks
history back to 2026-01-01 and a completed reconstruction for that period. All
five default sync commands returned `dry_run: true`, proposed one new advisory
and one typed unknown Node status, and performed no write. A read-only API check
confirmed zero remote advisories. The token was revoked through its scoped
action, its file removed, and ignored evidence/evaluation state moved outside
the worktree. No production deployment, migration, backfill, reboot, advisory
mutation, publication, notification, KB staging, or KB write occurred.
