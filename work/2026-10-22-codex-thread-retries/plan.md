# Automatic retries for failed Codex turns

## Goal and authorization

User requested a no-Codex-patch solution, selected capacity retries until cancelled
and automatic retries enabled by default, increased cybersecurity retries to30 in
five minutes, then approved the implementation plan with “Implement the plan.”
The plan includes deployment to aitherdev using vpsfree-cz-configuration and the
workspace user profile. No default-branch integration, machine release, session
archive/delete/stop or reboot is authorized.

## Affected projects and baseline

- codex-web: terminal failure projection, idle-only ledger-backed continuation,
  optional capability/API/browser retry controls, tests and reference docs.
- dev-workspace: durable policy/scheduler, admission/recovery/lifecycle fences,
  settings provenance, runtime docs and client dependency pin.
- workspace: composed nested runtime selection and deployment-contract checks.
- vpsfree-cz-configuration: existing dev-workspace/devWorkspace channel pin and
  aitherdev system build/activation; application stays in its user profile.

Fresh remote planning baseline: dev-workspace483d4e7eafeda974dfe19de45687795562072d7d,
codex-webea64ef57fdd2ff5fd60715b62f2d1696bc0133e5. Installed runtime source
/nix/store/vq9x3djn7b5v42ywbyfwagr3cslk9wja-source matches all535 source paths of
runtime483d4e7e exactly. Recheck actual current defaults before feature work; do
not downgrade to the older shared workspace pins.

## Behaviour and invariants

- Capacity terminal code serverOverloaded: base delay15/30/60/120/240/300seconds,
  then300 indefinitely. Positive jitter0..min(3seconds,10%base), capped total300.
- Cybersecurity terminal code cyberPolicy: validate in pinned generated schema;
  immediate dispatch, max30 automatic submissions/thread in rolling(now-300s,now].
  Original/manual attempts excluded; exhaustion remains failed until manual input.
- Default-on managed lead and ready retained-team threads; durable per-thread
  optout. New failures only on initial enrollment, with persistent watermark.
  Native Codex child threads excluded. Existing pending retries survive restarts.
- Only authoritative terminal failures; no intermediate/native willRetry errors,
  unknown/quota/auth errors, ordinary refusal, broad text classifier or model change.
- Visible continuation message: “Continue the interrupted task from the saved
  conversation. Inspect the current state before repeating actions.” New idle turn,
  preserving history/results/effective settings; no original-input or tool replay.
- Shared native admission lock and submission ledger, stable ID and exact immutable
  input/options. Reconcile uncertain outcomes only; never retry with a fresh UUID.
- Fresh identity/package/lifecycle/recovery/provider checks before every dispatch.
  Newer turns/native queues/manual input/team assignment/settings changes supersede
  pending retry; do not delete/reorder native queue. Cancel future work without
  pretending an uncertain in-flight submission did not run.
- Atomic private versioned store and interprocess lock. One dispatch/thread,
  bounded workers. Persist schedule/jitter/enrollment/quota/identity before send.
- Optional authenticated opaque-conversation retry status/preference/cancel API.
  UI displays class/phase/attempt/countdown/quota/reason, server schedules work.
  Cancel leaves preference enabled; disabling preference cancels current chain.

## Ownership and dependencies

Architect0 owns design.md and material design deviations. Implementer0 owns the
codex-web package and generic browser capability; implementer1 owns dev-workspace
controller/state/admission/runtime. State/policy can proceed against fixed interface
fixtures while library API is implemented. Dispatch depends on library publication.
Lead owns brief scoping, acceptance inspection, user copy, coordination/tracking,
review and deployment approval boundaries. Shared repository edits/Git serialized.
Deployment configuration execution packages return to implementers after feature
code settles. No repository claim for development, tests, publication or review.

## Compatibility and recovery

No Codex fork/protocol version upgrade, database migration, history rewind or
roster schema change. New retry state stays separate from submission schema3.
Preserve old/new package and native queue contracts; generation dispatch fence,
owned-work checks and explicit record-version capability prevent an incompatible
package from ignoring pending work. Workspace selection is forward-only; use
supported compatible forward recovery and retain exact pending identities.
A failed turn may have performed actions; new model turns cannot promise
exactly-once external effects. Unproved native-origin settings remain manual.

## Verification and acceptance

Quick focused Go/browser/Ruby checks first. Meaningful tests cover exact classifier,
backoff/jitter/rolling-window boundaries, persistent optout/cancel, enrollment races,
missed events, duplicate/process concurrency, before/after-acceptance crash,
unknown outcome, restart identity, queue/manual/stop/settings/provider/lifecycle
races, child exclusion, UI and authorization. After intended commits and quick
checks: mandatory independent reviewer0 final general/architecture/scope/risk
review with full branch history, final diff, migration and pin-stream inventory.
Then pinned disposable App Server schema/continuation synthetic-failure checks,
full package/build/CI verification via fresh Luna/low utility watchers.

## Deployment and integration

Publish reviewed feature branches; preserve no-Codex-patch baseline. Match the
workspace nested runtime and configuration confctl channel selection; run
bin/check-dev-workspace-deployment. Build committed source and copy before a
machine-only vpsfree:aitherdev claim. Dry-activate and no-reboot system switch,
then workspace-host switch --source with exact session/claim identity. Verify
system/profile paths, graph, health, continuity, old-failure exclusion and restart.
Retain deployed machine until integrated lineage, user acceptance and explicit
release direction all exist. Integration requires separate explicit approval.

## Documentation destinations

Architect design and rollout/review/verification receipts stay in this session.
Library behaviour belongs in codex-web reference; supported controller/recovery
behaviour in dev-workspace portal/operations guides. User-facing UI copy receives
lead's direct vpsfree-user-facing-writing/humanizer-en pass before commits.
