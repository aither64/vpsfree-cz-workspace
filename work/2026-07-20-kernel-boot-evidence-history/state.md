# Kernel Boot Evidence History State

## Scope and status

- Initiative: `2026-07-20-kernel-boot-evidence-history`.
- Status: the final label and three-channel follow-up is committed, verified,
  reviewed and pushed. A fresh development cluster is running the final head.
- Production premise: the preceding seven-migration release is deployed to the
  whole cluster and all eligible Node/storage history is backfilled. This
  release does not rerun or reset those completion checkpoints.
- Default branches remain untouched pending explicit user review and approval.

## Exact feature heads

- `vpsadmin`
  - base: `9773ac2bdf931a052ba1d7394f5e57aa4ca99f74`
  - head: `f74b9da44878e053c7b76fc1bcc0cf60a90cd120`
  - commits:
    - `6da090d6a` API reconciliation, monotonic data migration and specs
    - `1938b9cd9` per-boot evidence WebUI
    - `76833158c` generic system-configuration identity
    - `3dd7e6a08` migration-spec CI selection hardening
    - `f74b9da44` concise WebUI Node-origin label and browser coverage
- `vpsfree-cz-configuration`
  - base: `1931c5d4c0676cba1214546ec98bcf7a0c288b74`
  - head: `06ba5f52304c6a4adea27791482beb453f7e227f`
  - generated pins: `bd8913af` (`vpsadminServices`), `f39c5ef3`
    (`vpsadminStaging`) and `ce3730f2` (`vpsadminProduction`), all resolving
    to `f74b9da4...`
  - runbook/config commit: `06ba5f52`
- `vpsadmin-kb-captures`
  - base: `b9eb59ebc81b78deaac1242fe6ce2e55c3f84efe`
  - head: `6e0fa98c4d092fd50391e1a1d57b988f9762fba0`
  - the source and contract pin resolve to `f74b9da4...`

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
  to exact vpsAdmin revision `f74b9da44878e053c7b76fc1bcc0cf60a90cd120`.

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
  passed at `06ba5f52`; the latter reports `f74b9da4` for all three channels.
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
- The final exact-head review of vpsAdmin `f74b9da4...`, configuration
  `06ba5f52...` and captures `6e0fa98c...` found no remaining blocking,
  important or advisory findings. It caught stale Playwright label assertions
  and non-monotonic bare `CURRENT_TIMESTAMP` migration writes; both were fixed,
  tested, and folded into the appropriate logical commits before downstream
  pins were regenerated. It also confirmed the intended five/four/one commit
  split and clean worktrees matching the pushed feature refs.

## GitHub Actions

- Current head `f74b9da4...`: API Migration Specs, topic-parallel API Specs,
  RuboCop, WebUI PHPUnit, i18n health and libnodectld Specs passed. Broad CI is
  queued and was left to run without blocking the reviewed integration checks.
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
  `f74b9da44878e053c7b76fc1bcc0cf60a90cd120`.
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
- Unmerged migration history was rewritten again so only the final data-only
  migration/spec is introduced. There is no supersession schema in any feature
  commit. Tree identity was verified before the lease-protected force-push.
- One configuration push encountered transient GitHub SSH authentication before
  ref negotiation; the lease remained unchanged and the identical retry in the
  Nix shell succeeded. A durable workspace note records this.

## Remaining handoff

- Present the three exact feature heads and deployment runbook for user review.
- Leave the broad current-head GitHub Actions run to finish naturally and
  investigate its logs if it fails.
- Do not merge default branches until explicit user approval.
