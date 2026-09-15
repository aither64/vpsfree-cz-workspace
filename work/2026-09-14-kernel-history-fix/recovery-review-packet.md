# Kernel-history recovery and maintenance repair review

## Requested result and review boundary

Session: 2026-09-14-kernel-history-fix. Read the accepted follow-up in plan.md
and current state.md in this directory. The original single-node Rake command
was explicitly superseded by the user: repair belongs entirely in the dated
vpsfree-maintenance-tasks directory, previews all eligible nodes by default,
and offers --apply and repeatable --node filters. Include the demonstrated
invalid-evidence recovery defect across component histories.

The user explicitly corrected reviewer selection to gpt-6-astra at xhigh.
Use all four mandatory lanes with that model/effort; this overrides the older
model named in the skill. Do not edit persistent model instructions: the user
owns that update in a different session. Review directly without subagents.

This review covers the committed VpsAdmin and maintenance implementation before
any new long integration run or VpsAdmin push. Exact downstream configuration
and KB pins will follow the reviewed/pushed VpsAdmin head and receive their own
final-pin review and builds. Their previous pins are not validation of this
follow-up.

## Repositories and commits

All project paths are beneath:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-kernel-history-fix/

- vpsadmin base 014fbc78422f3660b295add7a50f35cc7acdf0c8;
  head 268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff.
  Commit cccf59c060be4c85a7a0809203e6fe24447e16a4 owns semantic stable kernel
  confirmation, nullable last_confirmed_at, recorder/comparator regression
  tests and synthetic restart coverage.
  Commit 268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff owns valid-evidence recovery,
  its empty private checkpoint table, application fallback correction and
  API/supervisor/integration regressions. Schema and tests travel with their
  respective behavior. The unreleased Rake repair never appears in this final
  series; it lives solely in the maintenance repository.
- vpsfree-maintenance-tasks base 6eea682ede8d8e2634b2d41e5b11cf0f02231bc6;
  head c77ff3742f623afd23c0be26c0f6ddbc026f1ba4.
  One dated task directory owns its executable, local node-repair helper,
  documentation and disposable DB/CLI tests. No generic repair framework.
- vpsfree-cz-configuration currently at upstream
  3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d pending final exact confctl pin.
- vpsfree-kb-contracts currently retains previous delivery head
  61aaf95d3dc0968728131a2cf4d4740dae6e9250, pending final VpsAdmin metadata pin
  and canonical impact validation.
- Registered vpsfree-dev-workspace is untouched at a08a40e; instruction work
  was taken into another session. It is not part of this implementation.

## Contracts, behavior and non-goals

VpsAdmin owns KernelEvidence::StableState and normalized Report state. Its
permanent recorder and the maintenance task import the same comparator.
SnapshotReader.comparison supplies supervisor ingestion from persisted current,
checkpoint or immutable fallback evidence. The private checkpoint serializes
normalized Report JSON and the original observation time, one row per node.
Rejected current evidence stays visible; no snapshot enum or public API fields
are added. Node protocol and WebUI wording/layout are unchanged.

Keep all original completeness/boot protections, including legacy reporters
that hide active livepatches. Confirm semantic boot/release/effective IDs,
excluding verification metadata. Routine confirmations preserve event bounds,
updated_at, public revisions and immutable snapshots. Applications retain the
complete preceding non-effective report rule without replacing a newer proven
confirmation with an older fallback. The checkpoint survives rejected reports,
missing reports and restart, and is cleared atomically on successful recovery.
Already-discarded observations cannot be reconstructed at upgrade time.

The repair handles only eligible inferred public release/livepatch events. It
requires strict lower < immutable confirmation < upper and the preceding stable
state in the same boot. Mutable snapshots, checkpoints, raw logs and uname-only
samples never prove historical repair. Candidate node/event IDs are fixed
before batching; target/predecessor/evidence are revalidated under the node lock.
Insufficient evidence and concurrent changes are skips; other errors are
nonzero and earlier applied writes remain committed. Reruns are idempotent.

Default node selection includes inactive node/storage hosts. Explicit unknown
or ineligible IDs reject the invocation before writes. Each output line identifies
the node/event, old/proposed bounds, supporting snapshot or skip reason, with
per-node/global totals. --batch-size defaults to the existing 1000 history batch
size. A preview is not an apply manifest; README/rollout explain keeping writers
paused if approval must cover identical output.

## Quick validation already completed

From VpsAdmin Nix shells:
- 130 DB-backed focused examples passed: recorder, StableState, supervisor,
  relocated repair and all-node CLI tests.
- 23 API-resource and standalone CLI examples passed, including public checkpoint
  invisibility, subset/all-node apply and rerun (420 seconds).
- Focused immutable-repair exclusion of private checkpoints passed (1 example).
- Both additive migration specs passed (2 examples, up/down/default/uniqueness/FK).
- Full core schema generated from exact upstream plus both migrations matches
  schema.rb byte-for-byte. This caught and corrected a lost upstream time index
  after rebase; no schema-content difference besides additive changes remains.
- CI selector 16 runs/55 assertions passed. Exact topic expansion covers all
  403 tracked non-migration specs once; migration specs use the existing workflow
  glob. No one-time maintenance tests remain in vpsAdmin.
- Touched API Ruby lint and maintenance Ruby lint with explicit VpsAdmin config
  passed. All commit hooks (Nixfmt, migration, RuboCop, i18n, messages) passed.
- No long integration test on this new head has started yet. The changed
  supervisor/runtime-ingestion scenario uses synthetic evidence and restart;
  it never unloads a real host patch. Historical repair CLI was exercised only
  against disposable MariaDB data.

## Risk, compatibility and deployment

High risk: persistent history, new schema, historical writes and mixed writers.
Review all four lanes at xhigh. Read task README and prepared rollout.md.
Migrations 20260914180000 (nullable confirmation) and 20260914190000 (empty
checkpoint table) are additive, no defaults/backfill/history repair. The first
was renumbered because current upstream claimed our earlier unmerged timestamp.

Prepared rollout pauses and runtime-masks both supervisors, activates API1,
runs migrations from its package using the database account, activates API2,
then restarts both supervisors and verifies confirmations advance. Both API
hosts have autoSetup=false. No node upgrade/reboot or reporter update.
Older application code can ignore both schema additions on rollback; its old
recording behavior returns. Keep schema additions and evidence-supported repairs.

Delivery permits feature commits, SSH pushes, reviews, tests and builds only.
No production deploy/repair, default-branch merge or session lifecycle action.
Leave this session and all retained branches/worktrees open. Do not touch the
old investigation session beyond read-only reference artifacts.
