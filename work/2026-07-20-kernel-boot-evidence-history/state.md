# Kernel Boot Evidence History State

## Scope and status

- Initiative: `2026-07-20-kernel-boot-evidence-history`.
- Status: the final label and three-channel follow-up is committed, verified,
  reviewed, fast-forwarded to all affected default branches and pushed. A fresh
  development cluster is running the merged vpsAdmin head.
- Production premise: the preceding seven-migration release is deployed to the
  whole cluster and all eligible Node/storage history is backfilled. This
  release does not rerun or reset those completion checkpoints.
- The user approved integration after reviewing the commit series. All affected
  default branches were fast-forwarded from fresh integration worktrees.

## Exact merged heads

- `vpsadmin`
  - base: `9773ac2bdf931a052ba1d7394f5e57aa4ca99f74`
  - head: `1bca29dfac3dba6a82a857ffad24d42e46ae861e`
  - commits:
    - `6da090d6a` API reconciliation, monotonic data migration and specs
    - `5f7c7430c` per-boot evidence WebUI, concise origin label and coverage
    - `36f8f69e7` generic system-configuration identity
    - `1bca29dfa` migration-spec CI selection hardening
- `vpsfree-cz-configuration`
  - base: `1931c5d4c0676cba1214546ec98bcf7a0c288b74`
  - head: `36c0e9ba2f5cdca43d4d3b0541c6b6fa809f699d`
  - generated pins: `b8774fb3` (`vpsadminServices`), `b7610ed8`
    (`vpsadminStaging`) and `21c5d330` (`vpsadminProduction`), all resolving
    to `1bca29df...`
  - runbook/config commit: `36c0e9ba`
- `vpsadmin-kb-captures`
  - base: `b9eb59ebc81b78deaac1242fe6ce2e55c3f84efe`
  - head: `8f5395f3890792bb9dc7ceb1c379cbef481e26f5`
  - the source and contract pin resolve to `1bca29df...`

All use SSH remotes. The retained feature branches and the corresponding
`master` branches point to these same heads.

## Implemented behavior

- Event `source` remains origin (`node_report` or reconstructed), while
  `confidence` now expresses boot-time precision (`exact`, `inferred`, or
  `incomplete`). Exactness comes from the immutable event evidence and its
  uptime-fallback error, never a later current report.
- Reported boot history uses the reported kernel boot time. The data-only
  `20260720120000 ReconcileReportedBootEvidence` migration corrects already
  deployed rows and deletes only the one derived reconstructed bootstrap
  matched to an authoritative report. Raw `node_statuses`, evidence and kernel
  parameters remain stored; no supersession column is added.
- A real reboot written by an old rolling-window supervisor is repaired from
  its event evidence but remains a distinct reboot. Repeated reconciliation
  cannot consume more reconstructed rows, and a forced history backfill does
  not recreate the deleted derived bootstrap.
- The migration captures and row-locks the exact incorrect reported-event ID
  set. Runtime repair locking-reads the same event, so migration and supervisor
  cannot act on stale attributes. Uncaptured old-supervisor writes remain
  uncorrected for atomic runtime repair. Corrected effective time is also the
  fallback when a legacy event has no stored `booted_at`.
- Every migration data update advances `updated_at` monotonically with
  microsecond precision, even when the stored timestamp is at or ahead of the
  database clock. This invalidates exact event and collection revisions without
  allowing a same-second update to truncate or regress the timestamp. Repeated
  `up` runs do not churn timestamps or revisions.
- Kernel history separates Origin and Time precision. Administrators can open
  Node-scoped immutable boot evidence with observation metadata, raw command
  line and all ordered parameters. Reconstructed history explains that no
  detailed snapshot exists; members and cross-Node requests are denied.
- The WebUI renders directly reported origin as the concise label `node`
  (`Node` in Czech) without changing source or confidence semantics.
- Software identity is now the generic `system_configuration`. Enum value `3`
  is preserved. Supervisors accept and normalize legacy
  `vpsfree_cz_configuration`; reporters emit only the generic name. The WebUI
  accepts both and obtains an optional HTTPS commit-link prefix from NixOS
  configuration. vpsFree.cz config links it to the configuration repository.
- Legacy component normalization and `reconcile_existing_reported_boot!` are
  intentionally retained together for this rollout to avoid mixed-version
  disruption. Remove both only in a later cleanup after all reporters and
  supervisors have been upgraded.

## Deployment and compatibility

- The updated runbook is
  `docs/operations/vpsadmin-security-evidence-deployment.md` in the
  configuration branch.
- Deploy both backward-compatible WebUIs first, deploy api1 normally, run the
  migration from its new application shell, then deploy api2. The corrective
  migration changes data only, so there is no schema compatibility window or
  service-quiescence procedure.
- Application rollback keeps the corrected authoritative event and raw status
  source. Migration `down` intentionally changes only migration bookkeeping;
  it does not recreate misleading derived history or reduce precision.
- Old Nodes may report the legacy component indefinitely. New Nodes must not
  emit `system_configuration` until accepting supervisors are deployed. No
  vpsAdminOS change, Node reboot, Node deployment, protocol version change or
  history reconstruction is required for this release.
- `vpsadminosStaging` remains exactly
  `702155fb91effd7102a92b568f684c7b0d948b1f`.
- `vpsadminServices`, `vpsadminStaging`, and `vpsadminProduction` all resolve
  to exact vpsAdmin revision `1bca29dfac3dba6a82a857ffad24d42e46ae861e`.

## Verification

- Current-head reconciliation, reconstruction and supervisor specs: 61
  examples, 0 failures. They retain legacy normalization and old-supervisor
  repair coverage alongside exact reporting and forced-rerun protection.
- Isolated migration/no-op rollback spec: 4 examples, 0 failures on the final
  tree; includes raw-status preservation, current-marker transfer, exact
  captured-ID isolation, one-candidate deletion, actual reboot correction,
  revision changes, same-tick monotonic timestamp advancement and repeated-up
  stability.
- Affected API resource specs: 20 examples, 0 failures.
- Generic identity: reporter 7/0; WebUI regression 11 tests/58 assertions;
  unsafe non-HTTPS prefixes are not linked. Gettext health and all vpsAdmin
  commit hooks pass on the current head.
- Existing focused API/WebUI coverage includes exact/fallback/incomplete boot
  time, rolling-window repair, duplicate prevention, authorization, null legacy
  evidence, and pagination beyond 1,000 immutable rows.
- vpsAdmin syntax, targeted RuboCop, translations and all Overcommit hooks
  passed. Migration-spec mapping selects only the final migration/spec. The
  rewritten final tree exactly matches the tested tree.
- Configuration hooks, `nix flake check`, and `confctl inputs channel ls`
  passed at `36c0e9ba`; the latter reports `1bca29df` for all three channels.
- Capture `bin/check` passed: contract suites 8 runs/50 assertions and
  7 runs/17 assertions, 39 controls, 29 paths, 65 bindings, 59 concepts, 118
  variants and 118 PNGs valid. Capture `nix flake check` passed.
- Capture changes are limited to `flake.nix`, `flake.lock`, `captures.json` and
  `contract/navigation.yml`; no PNG or KB page content changed.
- Fresh-cluster smoke check: API and supervisor are active, node1 osctld and
  nodectld are running, migration `20260720120000` is up, and supervisor
  ingestion produced two evidence snapshots plus one boot event. That event is
  a directly reported exact boot with evidence attached,
  `effective_at = booted_at`, one current marker and nine ordered parameters in
  each snapshot.

## Mandatory fresh-context review

- Fresh review found and blocked two migration/runtime serialization races and
  a FORCE null-time mismatch. The exact-ID capture, migration/runtime row locks,
  and effective-time fallback resolve them; independent focused verification
  is green.
- An earlier exact-head review of vpsAdmin `1eb428ed...`, configuration
  `cec56806...` and captures `d19358eb...` found no blocking, important or
  advisory findings. It independently reran the 30 operation examples and
  three migration examples successfully.
- Residual rollout checks are production-scale row-lock duration and genuine
  supervisor concurrency. Do not run `FORCE=1` reconstruction from a rolled-back
  pre-feature application because that old code does not contain the duplicate
  recreation guard.
- The final content review of vpsAdmin `f74b9da4...`, configuration
  `06ba5f52...` and captures `6e0fa98c...` found no remaining blocking,
  important or advisory findings. It caught stale Playwright label assertions
  and non-monotonic bare `CURRENT_TIMESTAMP` migration writes; both were fixed,
  tested, and folded into the appropriate logical commits before downstream
  pins were regenerated. At the user's final history review, the label-only
  commit was folded into the earlier WebUI commit. The resulting
  `1bca29df...` tree is byte-for-byte identical to the reviewed vpsAdmin tree,
  and the KB flake retained the same NAR hash. Only commit identities and exact
  downstream pins changed, producing the final four/four/one commit split.

## GitHub Actions

- Feature head `1bca29df...`: broad CI, API Migration Specs, topic-parallel API
  Specs, RuboCop, WebUI PHPUnit, i18n health and libnodectld Specs all passed.
- Merged `master` at the same head: API Migration Specs, RuboCop, WebUI PHPUnit,
  i18n health and libnodectld Specs passed. Broad CI and topic-parallel API
  Specs are still running and were left to finish naturally.
- Superseded queued/in-progress workflow runs for old feature SHAs were
  cancelled after the final force-push. Runs on the current SHA were retained.
- Failed migration run `29752208265` was investigated from its retained failed
  logs before any further validation. The workflow had selected the deleted
  pre-rename migration-spec path, so RSpec failed before examples. Commit
  `df4f02af3` adds `--diff-filter=ACMRTUXB`; final migration CI is green.
- Workflow edit verified current upstream action refs: `actions/checkout@v7`
  (v7.0.1) and current `ruby/setup-ruby@v1` (v1.319.0).

## Development cluster

- The previous dedicated cluster state was stopped and reset after mandatory
  review. A new cluster with the same initiative name was built from scratch
  and is left running and ready with topology `single` and network `bridge`.
- Both services and node1 report exact, clean vpsAdmin revision
  `1bca29dfac3dba6a82a857ffad24d42e46ae861e`, which is also the merged
  vpsAdmin `master` head.
- API and supervisor are active; node1 `osctld` and `nodectld` are running; API
  and WebUI return HTTP 200. Migration `20260720120000` is present in
  `schema_migrations`, and `node_kernel_events.superseded_by_event_id` does not
  exist.
- Supervisor ingestion produced two evidence snapshots and one current boot
  event. Its integer enum values map to `node_report` and `exact`; it has
  evidence attached and `effective_at = booted_at`, with no duplicate current
  row. Each snapshot stores nine ordered kernel parameters.
- WebUI is `https://webui.aitherdev.int.vpsfree.cz/` and API is
  `https://api.aitherdev.int.vpsfree.cz/`; the standard Web CS/EN, Auth,
  Console, Mailpit, Status and Adminer endpoints were also published.
- Shared dev-cluster tooling detected its existing global Telegram token and
  performed the standard post-ready services update. It is unrelated to this
  vpsAdmin branch; the user explicitly requested that the ready cluster be left
  as-is.

## Investigation and workflow notes

- A literal all-files local RSpec run mixed ordinary and isolated migration
  databases, producing deterministic missing-table cascades. Migration specs
  are now run separately; ordinary validation uses focused local suites and
  parallel GitHub Actions. The later long serial ordinary suite was stopped at
  the user's request and was not treated as authoritative.
- Fresh rewrite worktrees initially lacked repository-local hook gems. Entering
  their declared Nix shells installed dependencies, after which every real
  commit hook passed; no hook was bypassed.
- The fresh vpsAdmin integration worktree's first explicit Overcommit run lacked
  `api/.gems`, so only `VpsadminApiI18n` failed before loading ActiveRecord.
  Entering `nix develop .#api` populated the declared API bundle; the complete
  root Overcommit suite was then rerun and all hooks passed before pushing
  `master`.
- Unmerged migration history was rewritten again so only the final data-only
  migration/spec is introduced. There is no supersession schema in any feature
  commit. Tree identity was verified before the lease-protected force-push.
- One configuration push encountered transient GitHub SSH authentication before
  ref negotiation; the lease remained unchanged and the identical retry in the
  Nix shell succeeded. A durable workspace note records this.

## Remaining handoff

- Leave the two long merged-`master` GitHub Actions runs to finish naturally and
  investigate their logs if either fails.
- The configuration, capture and temporary integration worktrees were removed
  after merge. Keep the ready development cluster running; its vpsAdmin source
  worktree is retained until the cluster is stopped, then remove that final
  worktree while preserving the feature branch.
- Production deployment and migration execution remain operator actions under
  the reviewed runbook.
