# Kernel Boot Evidence History State

## Scope and status

- Initiative: `2026-07-20-kernel-boot-evidence-history`.
- Status: simplified data-only implementation is complete, pushed, independently
  reviewed and smoke-tested on a freshly reset development cluster.
- Production premise: the preceding seven-migration release is deployed to the
  whole cluster and all eligible Node/storage history is backfilled. This
  release does not rerun or reset those completion checkpoints.
- Default branches remain untouched pending explicit user review and approval.

## Exact feature heads

- `vpsadmin`
  - base: `08ef574623c9d8ee8742c245036eae34c160cc0f`
  - head: `1eb428ede8603fea88850e5da08620e249dba83e`
  - commits:
    - `cdfa72fde` API reconciliation, serialized data migration and specs
    - `fad28bb25` per-boot evidence WebUI
    - `c12034169` generic system-configuration identity
    - `1eb428ede` migration-spec CI selection hardening
- `vpsfree-cz-configuration`
  - base: `2d2e1071cd1470de94b9eca6c6884919a68c8e8e`
  - head: `cec56806cdc395bf28d3edfd4ed408dfbbf2fcb3`
  - generated pins: `3fe973c8` (`vpsadminStaging`) and `6a30f45c`
    (`vpsadminServices`), both resolving to `1eb428ed...`
  - runbook/config commit: `cec56806`
- `vpsadmin-kb-captures`
  - base: `8d0ff0913880373f69ff57fabdaa110d22e72ab0`
  - head: `d19358eb695692700d692d9383e1593a51449ecf`
  - the source and contract pin resolve to `1eb428ed...`

All use branch `2026-07-20-kernel-boot-evidence-history` and SSH remotes.

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
- Every migration data update advances `updated_at`, which invalidates exact
  event and collection evidence revisions. Repeated `up` runs do not churn
  timestamps or revisions.
- Kernel history separates Origin and Time precision. Administrators can open
  Node-scoped immutable boot evidence with observation metadata, raw command
  line and all ordered parameters. Reconstructed history explains that no
  detailed snapshot exists; members and cross-Node requests are denied.
- Software identity is now the generic `system_configuration`. Enum value `3`
  is preserved. Supervisors accept and normalize legacy
  `vpsfree_cz_configuration`; reporters emit only the generic name. The WebUI
  accepts both and obtains an optional HTTPS commit-link prefix from NixOS
  configuration. vpsFree.cz config links it to the configuration repository.

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

## Verification

- Reconciliation/backfill operation specs: 30 examples, 0 failures. They cover
  exact, inferred and incomplete times, one-duplicate deletion, actual reboot
  preservation, locking old-supervisor repair, null-time fallback, forced rerun
  non-recreation and concurrent exact-history cutoffs.
- Isolated migration/no-op rollback spec: 3 examples, 0 failures on the final
  tree; includes raw-status preservation, current-marker transfer, exact
  captured-ID isolation, one-candidate deletion, actual reboot correction,
  revision changes and repeated-up stability.
- Affected API resource specs: 20 examples, 0 failures.
- Generic identity: reporter 7/0; focused supervisor/resource suite 45/0;
  WebUI regression 11 tests/58 assertions; unsafe non-HTTPS prefixes are not
  linked.
- Existing focused API/WebUI coverage includes exact/fallback/incomplete boot
  time, rolling-window repair, duplicate prevention, authorization, null legacy
  evidence, and pagination beyond 1,000 immutable rows.
- vpsAdmin syntax, targeted RuboCop, translations and all Overcommit hooks
  passed. Migration-spec mapping selects only the final migration/spec. The
  rewritten final tree exactly matches the tested tree.
- Configuration hooks, `nix flake check`, and
  `confctl ls cz.vpsfree/vpsadmin/int.webui1` passed at `cec56806`.
- Capture `bin/check` passed: contract suites 8 runs/50 assertions and
  7 runs/17 assertions, 39 controls, 29 paths, 59 concepts, 118 variants and
  118 PNGs valid. Capture `nix flake check` passed.
- Capture changes are limited to `flake.nix`, `flake.lock`, `captures.json` and
  `contract/navigation.yml`; no PNG or KB page content changed.
- Fresh-cluster smoke check: API and supervisor are active, node1 nodectld is
  running, migration `20260720120000` is up, and supervisor ingestion produced
  two evidence snapshots plus one boot event. That event is a directly reported
  exact boot with evidence attached and `effective_at = booted_at`.

## Mandatory fresh-context review

- Fresh review found and blocked two migration/runtime serialization races and
  a FORCE null-time mismatch. The exact-ID capture, migration/runtime row locks,
  and effective-time fallback resolve them; independent focused verification
  is green.
- The final exact-head review of vpsAdmin `1eb428ed...`, configuration
  `cec56806...` and captures `d19358eb...` found no blocking, important or
  advisory findings. It independently reran the 30 operation examples and
  three migration examples successfully.
- Residual rollout checks are production-scale row-lock duration and genuine
  supervisor concurrency. Do not run `FORCE=1` reconstruction from a rolled-back
  pre-feature application because that old code does not contain the duplicate
  recreation guard.

## GitHub Actions

- Final head `1eb428ed...`: API Migration Specs, RuboCop, WebUI PHPUnit, i18n
  health and libnodectld Specs passed. Topic-parallel API Specs and broad CI
  remain in progress; work continues without waiting for those long lanes.
- Superseded queued/in-progress workflow runs for old feature SHAs were
  cancelled after the final force-push. Runs on the current SHA were retained.
- Failed migration run `29752208265` was investigated from its retained failed
  logs before any further validation. The workflow had selected the deleted
  pre-rename migration-spec path, so RSpec failed before examples. Commit
  `df4f02af3` adds `--diff-filter=ACMRTUXB`; final migration CI is green.
- Workflow edit verified current upstream action refs: `actions/checkout@v7`
  (v7.0.1) and current `ruby/setup-ruby@v1` (v1.319.0).

## Development cluster

- Previous cluster `2026-07-13-security-advisory-automation` was confirmed
  running, ready, single-node and bridge-networked before shutdown.
- `devcluster stop` exhausted its graceful timeout and then terminated the old
  runner as designed; final status is stopped.
- The dedicated cluster was reset, rebuilt and left running and ready with
  topology `single` and network `bridge`. Both services and node1 report exact,
  clean vpsAdmin revision `1eb428ede8603fea88850e5da08620e249dba83e`.
- API and supervisor are active; node1 `osctld` and `nodectld` are running; API
  and WebUI return HTTP 200. Migration `20260720120000` is present in
  `schema_migrations`, and `node_kernel_events.superseded_by_event_id` does not
  exist.
- Supervisor ingestion produced two evidence snapshots with no evidence errors
  and one current boot event. Its integer enum values map to `node_report` and
  `exact`; it has evidence attached and `effective_at = booted_at`, with no
  duplicate current row.
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
- Unmerged migration history was rewritten again so only the final data-only
  migration/spec is introduced. There is no supersession schema in any feature
  commit. Tree identity was verified before the lease-protected force-push.
- One configuration push encountered transient GitHub SSH authentication before
  ref negotiation; the lease remained unchanged and the identical retry in the
  Nix shell succeeded. A durable workspace note records this.

## Remaining handoff

- Present the three exact feature heads and deployment runbook for user review.
  Do not merge default branches until explicit approval.
- The topic-parallel API and broad CI workflows are still running on the exact
  current vpsAdmin head without failures; inspect original logs before any
  rerun if either later fails.
