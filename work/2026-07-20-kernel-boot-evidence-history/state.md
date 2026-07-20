# Kernel Boot Evidence History State

## Scope and status

- Initiative: `2026-07-20-kernel-boot-evidence-history`.
- Status: implementation complete on pushed feature branches; mandatory review
  passed with no findings and the fresh development cluster is ready.
- Production premise: the preceding seven-migration release is deployed to the
  whole cluster and all eligible Node/storage history is backfilled. This
  release does not rerun or reset those completion checkpoints.
- Default branches remain untouched pending explicit user review and approval.

## Exact feature heads

- `vpsadmin`
  - base: `08ef574623c9d8ee8742c245036eae34c160cc0f`
  - head: `df4f02af3218172fd9871e079b6b4e2fb9a0f3d2`
  - commits:
    - `22e15a305` API reconciliation, migration, revision integrity and specs
    - `0b689d638` per-boot evidence WebUI
    - `b1ba46a47` generic system-configuration identity
    - `df4f02af3` migration-spec CI selection hardening
- `vpsfree-cz-configuration`
  - base: `2d2e1071cd1470de94b9eca6c6884919a68c8e8e`
  - head: `ab3f43f69b9d3871f75e57798c81a983da9e1881`
  - generated pins: `cdc12680` (`vpsadminStaging`) and `3307697c`
    (`vpsadminServices`), both resolving to `df4f02af...`
  - runbook/config commit: `ab3f43f6`
- `vpsadmin-kb-captures`
  - base: `8d0ff0913880373f69ff57fabdaa110d22e72ab0`
  - head: `f92c0783c8e886bf8764dcacd47ffbf9f97901e1`
  - the source and contract pin resolve to `df4f02af...`

All use branch `2026-07-20-kernel-boot-evidence-history` and SSH remotes.

## Implemented behavior

- Event `source` remains origin (`node_report` or reconstructed), while
  `confidence` now expresses boot-time precision (`exact`, `inferred`, or
  `incomplete`). Exactness comes from the immutable event evidence and its
  uptime-fallback error, never a later current report.
- Reported boot history uses the reported kernel boot time. The reversible
  `20260720120000 ReconcileReportedBootEvidence` migration corrects already
  deployed rows and adds a nullable supersession self-reference without
  deleting reconstructed events, evidence, parameters or source samples.
- A first evidence bootstrap may supersede one matching reconstructed boot.
  A real reboot written by an old rolling-window supervisor is repaired from
  its event evidence but remains a distinct reboot. Repeated reconciliation
  cannot consume more reconstructed rows.
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
- Deploy both backward-compatible WebUIs first, then quiesce api1 before the
  migration. The runbook captures the exact active `vpsadmin-api-*.timer` set,
  masks API, supervisor, scheduler, console router and those timers, drains and
  verifies all active rake services, switches api1 without health checks,
  migrates, then restores only the captured timers and long-running services.
- Deploy api2 after the schema is up. An explicit down migration mirrors the
  quiescence steps, rolls APIs back before WebUIs, and preserves the exact timer
  activation state.
- Old Nodes may report the legacy component indefinitely. New Nodes must not
  emit `system_configuration` until accepting supervisors are deployed. No
  vpsAdminOS change, Node reboot, Node deployment, protocol version change or
  history reconstruction is required for this release.
- `vpsadminosStaging` remains exactly
  `702155fb91effd7102a92b568f684c7b0d948b1f`.

## Verification

- Reconciliation operation spec: 17 examples, 0 failures.
- Isolated migration/rollback spec: 2 examples, 0 failures on the final tree;
  includes revision changes, untouched-event timestamps and repeated-up
  stability.
- Generic identity: reporter 7/0; focused supervisor/resource suite 45/0;
  WebUI regression 11 tests/58 assertions; unsafe non-HTTPS prefixes are not
  linked.
- Existing focused API/WebUI coverage includes exact/fallback/incomplete boot
  time, rolling-window repair, duplicate prevention, authorization, null legacy
  evidence, and pagination beyond 1,000 immutable rows.
- vpsAdmin syntax, targeted RuboCop, translations and all Overcommit hooks
  passed. Migration-spec mapping check selects only the final migration/spec.
- Configuration hooks, `nix flake check`, and
  `confctl ls cz.vpsfree/vpsadmin/int.webui1` passed at `ab3f43f6`.
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

- Final reviewed heads: vpsAdmin `df4f02af...`, configuration `ab3f43f6...`,
  captures `f92c0783...`.
- Disposition: no Blocking, Important or Advisory findings.
- Review confirmed immutable-evidence repair, actual effective times,
  terminal one-to-one reconciliation, row preservation, WebUI authorization
  and pagination, generic-component compatibility, revision invalidation,
  clean migration history, exact downstream pins and safe rollout/rollback.
- Residual production-scale migration locking and real mixed-supervisor timing
  are covered by integration and operator rollout checks.

## GitHub Actions

- Final head `df4f02af...`: API Migration Specs, RuboCop, WebUI PHPUnit, i18n
  health and libnodectld Specs passed.
- Topic-parallel API Specs and broad CI remain in progress without a reported
  failure. Per user direction, work proceeded without waiting for the long
  lanes.
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
- Fresh cluster `2026-07-20-kernel-boot-evidence-history` is running and ready
  with topology `single` and network `bridge` from the final feature worktree.
  WebUI is `https://webui.aitherdev.int.vpsfree.cz/` and API is
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
- Unmerged migration history was rewritten so only the final migration/spec is
  introduced. The timestamp/revision correction was folded into that backend
  commit. Tree identity was verified before each lease-protected force-push.
- One configuration push encountered transient GitHub SSH authentication before
  ref negotiation; the lease remained unchanged and the identical retry in the
  Nix shell succeeded. A durable workspace note records this.

## Remaining handoff

- Observe the current-head parallel API and broad CI runs; investigate original
  logs if either fails, without blind reruns.
- Present the three exact feature heads for user review. Do not merge default
  branches until explicit approval.
