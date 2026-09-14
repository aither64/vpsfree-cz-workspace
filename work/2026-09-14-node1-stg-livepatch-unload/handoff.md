# vpsAdmin kernel-history bounds: implementation handoff

## Ownership and delivery

Use the new session created by the user through dev-portal. Verify its ownership
with `dev-session current` and matching `DEV_SESSION_SLUG`. Use that new slug for
tracking, branches, and worktrees. Do not reuse, revive, modify, or close
`2026-09-14-node1-stg-livepatch-unload`; its files are references only.

Implement, commit, review, test, and push feature branches in `vpsadmin` and
`vpsfree-cz-configuration`. Include the historical repair tool and exact
`vpsadmin` channel pin. Prepare deployment and repair instructions. Do not deploy,
run production repairs, merge default branches, or archive sessions.

Follow the current workspace/repository AGENTS.md and required skills. This
handoff records decisions, not an exception to those instructions.

## Confirmed cause

The user observed this interval for a recent node1.stg transition, in CEST:
`(2026-08-22 17:33:29, 2026-09-13 20:00:36]`.

At inspected vpsAdmin revision `791ab3aa89e2f613979da6090b89785c78245db5`,
`RecordKernelEvidence` selects:

```ruby
stable_observed_at = stable_event&.observed_before || previous_observed_at
```

The historical event time stays unchanged while current evidence receives newer
confirmations. Removals and release changes reuse that stale time. Applications
have a special case using a complete previous report. WebUI renders the stored
bounds. Existing tests do not cover repeated unchanged observations between
events. The regression originated in
`988ce4a0d1c0bbbe495963c5e8e3ed2190eaba1d`.

Read [the full diagnosis](vpsadmin-kernel-history-diagnosis.md) and
[the executable reproduction](reproduce-kernel-bound.rb). The reproduction runs
actual pinned selection logic with mocked persistence; it is not a production
database replay. Fetch current upstream before implementation.

## Recorder fix

- Add nullable `node_kernel_events.last_confirmed_at` without a default or
  automatic historical rewrite; cover the migration and regenerate core schema.
- Advance it on complete, non-transitioning observations confirming the same
  boot, release, and effective livepatch IDs. Reuse existing completeness and
  boot identity rules, ignore volatile verification metadata, and preserve
  safeguards against legacy reporters hiding an active patch.
- Consider the supplied previous report too, retaining a recent confirmation
  already in current evidence when the upgraded recorder first runs.
- Preserve the timestamp through transitions, incomplete reports, unrelated
  inventory changes, and supervisor restarts. Advance monotonically under the
  existing node lock and transaction.
- Routine confirmation updates must not touch event `updated_at`, original
  event bounds, or immutable snapshots. Public event revision hashes use
  `updated_at` and must remain stable during these internal updates.
- Use the last confirmed old-state time for removal/release `observed_after`.
  Fall back conservatively when no newer confirmation is provable.
- Preserve the application-specific use of a complete preceding non-effective
  report. A global substitution of the previous report time is unsafe because
  a transitioning report may already contain the new release.
- Initialize confirmation metadata only from complete stable event evidence.
  Preserve conservative behavior for unreadable initial boot evidence.
- No public API field, node protocol, WebUI wording, or layout changes are planned.

## Historical repair tool

Add these Rake invocations:

```sh
NODE_ID=400 bundle exec rake vpsadmin:node:repair_kernel_history_bounds
NODE_ID=400 APPLY=1 bundle exec rake vpsadmin:node:repair_kernel_history_bounds
```

Require one eligible node ID. Default to dry-run; accept unset/0 or 1 for APPLY.
Support positive BATCH_SIZE with the existing history batch-size default.

Handle inferred node-reported release changes and explicitly classified
livepatch applications/removals. Skip boots, reconstructed/exact events, missing
lower bounds, and ambiguous classifications. Identify the preceding public
baseline and the latest immutable event snapshot positively confirming its
stable state within the interval and same boot. Include internal event snapshots
and share the recorder's comparison helper.

Exclude mutable current snapshots, raw log imports, and uname-only status
samples as proof of module lifecycle. Tighten only when
`old observed_after < proven confirmation < observed_before`. Preserve upper
bound, classification, confidence, effective time, and evidence. Applied repairs
update `updated_at` normally to invalidate the public evidence revision.

Print event ID, old/proposed bounds, supporting evidence ID, skip reasons, and
totals. Scan a fixed candidate set in batches. Before each write, acquire the
node lock and revalidate target, predecessor, and supporting evidence; skip and
report concurrent changes. Reruns must be idempotent. Insufficient evidence
leaves the old interval unchanged. No production repairs are authorized here.

## Verification

- Database-backed recorder tests: unchanged observations over days, direct
  removal, multiple transition reports, release changing during transition,
  incomplete evidence, legacy ambiguity, reboots, and application behavior.
- Supervisor tests: persistence across a new supervisor instance, invalid and
  stale/out-of-order reports, stable original timestamps/snapshots/revisions.
- Repair tests: dry-run, apply, idempotence, evidence selection, insufficient
  evidence, cross-boot rejection, concurrent changes, revision invalidation.
- Extend supervisor runtime-ingestion integration coverage with synthetic
  evidence and a supervisor restart. Test repair on disposable data. Do not
  unload a real host patch for testing.
- Use repository Nix environments; run focused RSpec, migration checks, and
  lint. Register new specs in the relevant CI topic patterns.
- After commits and quick checks, run the mandatory general, architecture,
  scope, and compatibility review lanes using `gpt-5.6-sol` at `xhigh`.
  Resolve required findings before long integration tests, then monitor CI.
- Follow the canonical KB impact workflow for changed rendered timestamps.
  Apply the user-facing writing skill to command help and operator documentation.

## Configuration and prepared rollout

Fetch/rebase both branches before final validation. Push the tested vpsAdmin
commit over SSH and pin it from the new configuration worktree:

```sh
confctl inputs channel set --commit vpsadmin vpsadmin <tested-vpsadmin-revision>
```

Preserve the generated commit message. Verify the update targets
`vpsadminServices`; do not update staging, production, or vpsAdminOS channels.
Build `cz.vpsfree/vpsadmin/*` channel consumers and include the final pin and
build results in review.

Prepare instructions to pause both supervisor writers, activate the new API
package, run the additive migration, update the second API host, restart both
supervisors, and verify advancing confirmations. Prepare the node1 repair dry-run
separately. No node upgrade or reboot is required.

Older application code can ignore the nullable column on rollback, although
its old recording behavior returns. Never seed confirmation times with migration
time or automatically undo evidence-supported repairs.

Finish with pushed heads, review/CI/build results, rollout commands, repair
limitations, and the new session's portal URL. Leave that session open.
