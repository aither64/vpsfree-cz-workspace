# 2026-09-14-kernel-history-fix

## Goal

Implement the vpsAdmin kernel-history timestamp fix described below, including
  a historical repair tool and updating channel `vpsadmin` in
  vpsfree-cz-configuration.

  Session ownership
  - Use this NEW dev-portal session and its slug for tracking, branches, and worktrees.
  - Verify ownership with `dev-session current` and matching DEV_SESSION_SLUG.
  - Do not reuse, revive, modify, or close session
    2026-09-14-node1-stg-livepatch-unload.
  - Its investigation artifacts may be read as reference only.
  - Follow workspace/repository AGENTS.md and required skills.

  Authorized delivery
  - Implement, commit, review, test, and push feature branches.
  - Include a dry-run-first historical repair tool.
  - Update the configuration channel to the exact tested vpsAdmin feature revision.
  - Prepare deployment and repair instructions.
  - Do NOT deploy, modify production history, merge default branches, or archive
    sessions. Those actions are outside the agreed delivery.

  Problem and confirmed diagnosis
  On node1.stg, the WebUI describes a recent transition as:
  “Change occurred after the last previous observation at 2026-08-22 17:33:29
  and no later than the first new observation at 2026-09-13 20:00:36:
  (2026-08-22 17:33:29, 2026-09-13 20:00:36].”

  The recorder confuses the first observation of the previous public kernel
  event with the latest observation confirming that state.

  At inspected vpsAdmin revision 791ab3aa89e2f613979da6090b89785c78245db5:
  - api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb:97 selects:
    stable_observed_at = stable_event&.observed_before || previous_observed_at
  - Removals use this stale value; reported-release changes do too.
  - Unchanged reports refresh current evidence but leave the historical event
    timestamp unchanged.
  - Applications have a special case using a complete previous report.
  - webui/forms/node.forms.php renders the supplied bounds; it does not calculate
    the bad lower bound.
  - The bug was introduced in commit
    988ce4a0d1c0bbbe495963c5e8e3ed2190eaba1d.
  - Existing tests miss repeated unchanged observations between public events.

  The actual recorder logic was reproduced with mocked persistence: a fresh
  September observation still produced the August lower bound for direct removal,
  removal through transition, and release-only change. Production database rows
  were not inspected. Fetch current upstream before implementing.

Recorder fix
  1. Add nullable node_kernel_events.last_confirmed_at with no default or automatic
     historical rewrite. Include migration coverage and regenerate the core schema.
  2. Advance this internal timestamp when a complete, non-transitioning observation
     confirms the baseline's boot, reported release, and effective livepatch IDs.
     Reuse existing completeness/boot-identity rules and preserve protections
     against legacy reporters hiding an active patch.
  3. Compare semantic runtime state, excluding volatile verification metadata.
     Consider the supplied previous report as well, so a recent confirmation
     already present at upgrade time is retained.
  4. Preserve confirmation time through transitions, incomplete reports, unrelated
     inventory changes, and supervisor restarts. Advance monotonically under the
     existing node lock and transaction.
  5. Routine confirmation updates must NOT touch event updated_at, original event
     bounds, or immutable evidence snapshots. Public event revision hashes depend
     on updated_at and must remain unchanged by these internal confirmations.
  6. Use the last confirmed old-state timestamp for removal/release observed_after.
     Fall back conservatively when no newer confirmation is provable.
  7. Preserve application-specific use of a complete preceding non-effective report.
     Do not globally substitute previous_observed_at: a transitioning report may
     already contain the new release.
  8. Initialize confirmation metadata for new events only when their evidence
     establishes a complete stable state. Preserve conservative bootstrap behavior
     for unreadable evidence.
  9. No new public API field, node-report protocol change, or WebUI wording/layout
     change is planned.

  Historical repair tool
  Add:
    NODE_ID=400 bundle exec rake vpsadmin:node:repair_kernel_history_bounds
    NODE_ID=400 APPLY=1 bundle exec rake vpsadmin:node:repair_kernel_history_bounds

  - Require one eligible node ID; default to dry-run. APPLY accepts unset/0 or 1.
    Support positive BATCH_SIZE, defaulting to the existing history batch size.
  - Handle inferred node-reported release changes and explicitly classified
    livepatch applications/removals. Skip boots, reconstructed/exact events,
    missing lower bounds, and ambiguous classifications.
  - Find the preceding public baseline and the latest retained immutable event
    snapshot that positively confirms its stable state within the interval and
    same boot. Include internal event snapshots.
  - Share the recorder's state-comparison helper.
  - Do not use mutable current snapshots, import raw logs, or infer module lifecycle
    from uname-only status samples.
  - Tighten only when:
    old observed_after < proven confirmation < observed_before.
  - Preserve upper bound, event classification, confidence, effective timestamp,
    and evidence. Applied repairs update updated_at normally so revisions change.
  - Print event ID, old/proposed bounds, supporting evidence ID, skip reasons,
    and totals. Insufficient evidence must leave the interval unchanged.
  - Process a fixed candidate set in batches. Revalidate target, predecessor, and
    evidence under the node lock before each write; skip/report concurrent changes.
  - Make reruns idempotent.
  - Build and test the tool; do not execute production repairs during this task.

Tests and review
  - Database-backed recorder regressions: long unchanged periods, direct removal,
    multiple transition reports, release changing during transition, incomplete
    evidence, legacy inventory ambiguity, reboot boundaries, and application behavior.
  - Supervisor tests: persisted confirmation across a new supervisor instance,
    invalid reports, stale/out-of-order reports, unchanged original event timestamps,
    immutable snapshots, and stable public revisions during confirmation updates.
  - Repair tests: dry-run, apply, idempotence, evidence selection, insufficient
    evidence, cross-boot rejection, concurrent changes, and revision invalidation.
  - Extend the existing supervisor runtime-ingestion integration scenario with
    synthetic evidence and supervisor restart; exercise repair on disposable data.
    Do not unload a real host patch for testing.
  - Use repository Nix environments; run focused RSpec, migration checks, and lint.
    Register new specs in CI topic patterns.
  - After committing intended changes and passing quick checks, run the mandatory
    general, architecture, scope, and compatibility review lanes, using
    gpt-5.6-sol at xhigh. Resolve required findings before long integration tests.
  - Run selected integration tests and monitor GitHub Actions to completion.
  - Follow the canonical KB impact workflow for changed rendered timestamps.
    No documentation prose/capture changes are expected unless the check shows impact.
  - Apply the user-facing writing skill to command help and operator documentation.

  Configuration update
  - Fetch/rebase feature branches before final validation.
  - Push the tested vpsAdmin revision over SSH.
  - From the new session's vpsfree-cz-configuration worktree, run:
    confctl inputs channel set --commit vpsadmin vpsadmin <tested-vpsadmin-revision>
  - Keep the generated commit message exactly as produced.
  - Verify the update targets vpsadminServices. Do not update staging, production,
    or vpsAdminOS channels.
  - Build the cz.vpsfree/vpsadmin/* channel consumers and record results.
  - Include the exact final pin in review and the final handoff.

  Prepared rollout, not execution
  Document pausing both supervisor writers, activating the new API package,
  running the additive migration, updating the second API host, then restarting
  both supervisors and verifying confirmation timestamps advance. Prepare the
  node1 repair dry-run separately.

  No node upgrade or reboot is required. Older application code can ignore the
  new nullable column on rollback, although its old recording behavior returns.
  Never seed confirmation times with migration time or automatically reverse
  evidence-supported historical repairs.

  Finish with pushed feature heads, review/CI/build results, rollout commands,
  repair limitations, and this NEW session's stable portal URL. Leave it open.

  Read-only references: diagnosis (work/2026-09-14-node1-stg-livepatch-unload/vpsadmin-kernel-history-diagnosis.md), reproduction (work/2026-09-14-node1-stg-livepatch-unload/reproduce-kernel-bound.rb), original investigation portal
  (https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-node1-stg-livepatch-unload/).

## Affected repositories

- vpsadmin: recorder, internal state comparison, additive migration/core schema,
  repair task, regression specs, CI selection, synthetic ingestion integration,
  and operator documentation.
- vpsfree-cz-configuration: exact vpsadminServices pin for channel vpsadmin only.
- vpsfree-kb-contracts: exact feature pin and canonical documentation impact check;
  no prose or capture changes unless the check establishes impact.

## Approach

1. Fetch current upstream and create session-owned feature worktrees.
2. Add persisted stable confirmations and shared semantic comparison; retain
   existing boot/completeness rules and application-specific bounds.
3. Add a bounded dry-run-first repair from immutable retained snapshots only.
4. Add database-backed, supervisor, migration, repair, and synthetic integration
   regressions, register specs in CI, and document the operator procedure.
5. Commit and pass quick Nix checks, then run general, architecture, scope,
   and compatibility reviews with gpt-5.6-sol at xhigh.
6. Resolve findings, run selected integration tests, push and monitor CI. Fetch
   and rebase before final validation. Pin the exact tested feature revision via
   confctl, review it, and build all cz.vpsfree/vpsadmin/* consumers.
7. Record final feature heads and rollout/repair instructions; leave session open.

## Compatibility and deployment

The only schema change is a nullable timestamp without a default or backfill.
Old rows stay conservative until supported by actual evidence. No protocol,
public API, CLI response, Terraform, node configuration, or persisted evidence
format changes are planned. Internal confirmations do not invalidate public
revisions; explicit repairs do. Older code ignores the column on rollback but
resumes old recorder behavior. Keep evidence-supported repairs on rollback.

Prepared rollout pauses both supervisor writers, activates the first API package,
runs the additive migration, updates the second API host, and restarts both
supervisors. No node upgrade, reboot, or coordinated node update is required.
No deployment, production repair, default-branch integration, session archival,
or session cleanup is authorized by this task.

## Testing plan

Use repository Nix shells with disposable MariaDB for focused recorder,
supervisor, repair, and migration RSpec plus Ruby lint and CI topic coverage.
Validate monotonic confirmation, immutable historical timestamps/evidence,
legacy ambiguity, reboot/stale report boundaries, revision behavior, repair
idempotence, and concurrent revalidation. After mandatory review, run the
supervisor runtime-ingestion scenario with synthetic reports, restart, and
repair on disposable data. Run canonical KB contract impact checks, GitHub
Actions to completion, and confctl builds for channel consumers. Investigate
unexpected local kernel builds before continuing.

## Follow-up status-history audit

After CI completed, the user asked whether the same timestamp problem affects
software versions and other nodectld status histories, and why kernel history
uses different logic. A read-only code audit and 13 disposable-database examples
answer that question in status-timestamp-audit.md. They found a separate existing
invalid-evidence recovery gap, including the application-specific previous-report
branch. That finding is retained as an open follow-up; the audit changes no
project revision or configuration pin.

## Accepted follow-up implementation

The user approved preserving valid evidence through rejected reports and moving
the one-time historical repair into vpsfree-maintenance-tasks. This supersedes
the original single-node Rake interface and the audit's open-follow-up status.

- Add a private, one-row-per-node checkpoint holding the comparable normalized
  report and its actual observation time before an invalid report overwrites
  current evidence. Retain it through invalid reports and supervisor restarts;
  consume it atomically on valid recovery. Keep rejected current evidence visible
  and checkpoint data outside public evidence APIs. Prefer newer retained event
  evidence over a stale checkpoint after rollback/mixed-version writes.
- Preserve application bounds from newer proven kernel confirmations even when
  the preceding-report fallback is older. Keep completeness and boot rules.
- Add an empty checkpoint table through a schema-only migration, regenerate the
  core schema, and test old-schema upgrade and rollback. Do not reconstruct lost
  reports, backfill observation times, or change the node protocol.
- Add the session-owned vpsfree-maintenance-tasks worktree and dated task folder
  2026-09-14-repair-kernel-history-bounds. Move repair implementation, tests and
  operator documentation out of vpsAdmin. The command defaults to all eligible
  node/storage hosts, including inactive hosts; --apply writes and repeatable
  --node ID selects a subset. --batch-size is positive and defaults to 1000.
- Freeze node/event candidate IDs before processing. Keep immutable-snapshot
  proof, per-write node-lock revalidation, strict bounds, revision invalidation,
  idempotence, explicit skip reasons and per-node/global output. Checkpoints and
  mutable snapshots are never historical repair evidence. Historical repair
  remains limited to public kernel release/livepatch events.
- Extend real supervisor and database tests across software/deployment, sysctl,
  module, eBPF inventory and kernel histories. Test maintenance CLI against
  disposable data. Update CI topic patterns and synthetic runtime ingestion.
- Repeat quick checks, four mandatory review lanes, integration, CI, exact
  vpsadminServices pin/builds and KB impact validation before final handoff.
  The user corrected the review model to gpt-6-astra; use xhigh for all review
  lanes, overriding the older user request and skill's gpt-5.6-sol default.
- Keep deployment and all-node repair as prepared instructions. Both additive
  schema changes remain on application rollback; old recording behavior returns.
  Never reverse evidence-supported repairs automatically. Session stays open.

## Default-branch integration authorized on 2026-09-15

The user requested merging this work into the default branches. Integrate V/M/C/K
with fresh target worktrees, current upstream, fast-forward-only pushes and
retained feature branches. V rebases over the upstream DDNS check without changing
our two patches; verify the combined code and regenerate exact C/K pins. Keep
rollout and production repair as prepared instructions and leave this session
open. The unused extension worktree remains outside this integration.
