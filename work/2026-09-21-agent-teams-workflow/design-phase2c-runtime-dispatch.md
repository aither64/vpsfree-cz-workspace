# Phase 2C runtime dispatch and retained teams

## Decision

Phase 2C is four generic `dev-workspace` commits. It may use coherent local
commit slices during implementation, but is consolidated at its completed
numbered boundary. It has no offline migration, state-root schema bump, daemon,
or normally a `codex-web` change. Schema-1 sessions remain legacy indefinitely.
The user's explicit low-cost decision also keeps an unmanaged-source fork on
the legacy continuation path; this Phase does not convert its source or
destination.

## 2C.0: durable provenance dispatcher

Create one strict reader/classifier for the creation journal, managed state and
pinned catalog. Classify each session as `legacy_unmanaged`, `managed`,
`managed_recovery`, or corrupt. Schema-2 evidence with missing or mismatched
state, catalog or binding, a state without matching schema-2 provenance, or a
malformed current identity is corruption and every mutation fails closed. The
only intentional `creating` recovery windows, in write order, are:

1. Before managed-state publication, when a valid journal binding validates
   against its pinned catalog.
2. After state publication but before its per-slug runtime-authority record is
   persisted, when the state, binding, catalog, unarchived manifest/root thread
   and removal epoch agree, the configured authority directory exists, and only
   that per-slug record is absent.
3. During finalization, after the manifest is `ready` and before the
   runtime-authority `ready` write: journal `creating`, manifest `ready`, and
   runtime authority `creating`, with exact state, binding, tmux and runtime
   identity agreement.
4. The next finalization prefix, after the runtime authority is durably
   `ready` but before the schema-2 journal becomes ready: exact journal
   `creating` plus manifest and runtime-authority `ready`, with the same full
   identity agreement.

Arbitrary mixed phases and all-creating phases remain corrupt. A missing
authority directory is corrupt. A ready schema-2 journal without state is
always corrupt. Only an absent or valid schema-1 journal without state is
legacy.

The dispatcher owns routing: legacy uses existing conversation and lifecycle;
managed uses team/member/managed-send paths; recovery/corruption admits no
ordinary mutation. Managed lifecycle remains refused until its later owning
slice. Runtime authority, removal epoch, creation identity and root thread bind
live managed operations; state self-consistency is not sufficient.

## 2C.1: retained members

Retained member state is bookkeeping around native tools, never a portal-side
scheduler. A member plan can reuse, create or close with a blocker. Prepared,
submitting, accepted and unknown writes use CAS. An uncertain native spawn or
follow-up cannot be replaced until exact root-tree observation proves it absent.
Luna is rejected as a member and remains a fresh operation-scoped utility.

Add immutable requested task names, replacement linkage and per-selection
provenance so a completed historical assignment may remain valid after a team
transition. Active work/write ownership must bind the current selection.

### 2C.1 implementation contract

- A retained member is only a `designer`, `implementer`, or `reviewer`.
  The root/lead is never a member; Luna is rejected and remains a fresh,
  operation-scoped utility.
- Persist the immutable requested task name, selection/catalog provenance and
  replacement predecessor for every assignment. A completed assignment keeps
  its historical provenance after a selection changes. An unfinished assignment
  has authority only while its exact selection is current; historical records
  are evidence, never authority for active work or writes.
- Strict CAS `prepare` and `record` helpers own member-operation changes.
  `prepare` records `prepared`; `record` CASes it to `submitting` before a
  native call, then to `accepted` or `unknown`. `unknown` is blocking:
  neither replacement nor retry is allowed until authoritative observation of
  the exact root tree resolves it. Absence, completion and reuse are likewise
  established only by that authoritative observation, never by local inference.
- Capacity is one assignment per eligible current role. Reuse is permitted only
  for the same eligible role with matching current-selection provenance and an
  authoritative reusable native identity; otherwise the plan creates a new
  assignment, or closes with a blocker when the prior outcome is unresolved.
- Member reconciliation and any close/reuse decision require transition
  quiescence: the exact root and all retained members are idle, with no
  `submitting` or `unknown` operation. It does not apply a team transition.
- The portal is read-only for this slice. It reports the current selection and
  per-member role, requested task name, provenance, replacement link, native
  identity and observed display state: absent, prepared, submitting,
  accepted-awaiting-observation, active, completed, unknown, blocked, or
  historical. It neither schedules nor spawns members.

Non-goals: no portal scheduler or spawn path, no 2C.2 team-transition
implementation, and no 2C.3 managed dispatch or controls.

## 2C.2: CAS team transitions

This slice depends on 2C.0's managed-session dispatcher and runtime-authority
checks, and on 2C.1's authoritative member observation, unknown-operation
blockers and reconciliation rules. It adds no scheduler, native spawn, follow-up
or portal-side member action.

### 2C.2 implementation contract

- `selection_revision` is the public selection CAS version. It changes only
  when a transition is applied. `state_revision` is the private document CAS
  version and advances for every retained-state write, including observations
  and publication/resolution of a pending transition. Do not substitute one for
  the other or require consecutive state revisions in transition history.
- Resolve the requested team, effective lead and role eligibility from the
  session's retained catalog, never the currently installed catalog. Before
  writing, verify the exact managed root/session identity and current immutable
  registration evidence for its retained catalog/native variants. Missing,
  changed, ambiguous or unregistered evidence is a controlled blocker, not a
  reason to remap a team or regenerate a variant.
- A request supplies a caller request ID, expected `selection_revision`, target,
  tri-state lead-override action, actor and non-empty reason. Validate target
  and runtime support before mutation. A request for the already-effective
  selection is a no-op. An exact replay of a retained pending or completed
  request returns the original transition/outcome; a reuse of that ID with any
  materially different request is a hard conflict. A distinct request at a
  stale expected selection revision conflicts. With one pending request, only
  its exact replay is accepted; a different request conflicts until it is
  resolved or cancelled. Deduplication is bounded by retained history: after
  pruning, do not promise session-lifetime replay protection.
- Apply directly only after authoritative reconciliation finds the root idle,
  all retained members idle or completed, no writer/check/lifecycle operation,
  no pending native approval/input and no `submitting`/`unknown` member or
  dispatch operation. Commit the new selection, incremented
  `selection_revision`, member eligibility/reuse-or-inactivation plan and
  history outcome in one state CAS. The plan changes assignment eligibility
  only; it never creates, closes, retasks or wakes a member.
- The sole deferrable boundary is the exact active managed root turn, requested
  by that root through its authenticated runtime path, after every other
  prerequisite is clear. Persist one `pending_boundary` record with its original
  public and private bases, root/turn observation and any trusted same-root
  continuation provenance, then return promptly. An external/browser/CLI
  request while that root is active returns controlled busy; active members,
  writers, unresolved work or a lifecycle boundary also return a blocker and do
  not silently arm a future transition. Never interrupt, poll, cancel or wait
  for a boundary.
- Provide `ApplyPendingBeforeSend` for 2C.3's managed start path. Under the
  same state and turn-submission fencing used for dispatch, it first reloads and
  revalidates authority, root identity, pinned catalog/registration, expected
  selection and the now-idle boundary. If no pending transition exists, it
  returns the current selection. If one exists, it atomically applies it before
  preparing the send: increment the public selection revision, retain the
  original request/base in bounded history with its completion state revision,
  set eligible members/reuse intent, clear pending, and return the exact new
  effective lead/settings. It does not create a synthetic turn, inject a user
  message, spawn/follow up/close a member, or submit dispatch itself. A failed
  revalidation leaves the transition pending with a reported blocker; an
  uncertain subsequent send is handled by 2C.3's dispatch ledger and cannot
  roll the applied selection back or fall back to old settings.
- Retain compact applied/cancelled outcomes with exact before, requested and
  actual-after selections, actor/reason, original base and completion
  `state_revision`. Preserve selection chaining: completion revisions strictly
  increase and each later base is at least the preceding completion; a pending
  record's original base may be below the current `state_revision`. Prune only
  oldest terminal entries to the existing bounded limit, never the active
  pending record, and preserve the current selection as the post-prune anchor.
- Schema-1/legacy and unmanaged-source sessions remain on their existing path:
  `team set`, pending application and managed send refuse rather than fabricating
  state. `managed_recovery` and corrupt classifications admit no transition.
  After a crash or lost response, read authoritative state and native/root
  evidence: an exact committed/pending record is replayed, any divergent record
  is conflict, and an unestablished native boundary blocks until reconciliation.

2C.3 exposes these results without conflating them: active selection,
`selection_revision`, pending target/reason/boundary, pinned catalog digest,
next-turn effective lead and last observed native settings are separate
user-visible values. Its Change-team, cancellation and send controls use the
same CAS/request IDs and `ApplyPendingBeforeSend`; they must label a pending
request as pending rather than as an applied switch.

## 2C.3: managed dispatch and controls

Persist dispatch preparation and option/context digests before
`PrepareSendWithOptions`, mark submitting before sending, then record accepted
or unknown. Unknown blocks resend and transitions until both ledgers reconcile.
Steering is only allowed under the same selection; queued starts and independent
model/effort settings are initially refused because they cannot bind a selection
revision safely. Portal controls expose active/pending team, pinned digest,
next-turn lead and observed members as distinct values.

## Verification and rollout

After Phase 2C is consolidated, its final head gets quick verification, one
mandatory Sol/xhigh review, and one proportionate verification batch. Full Go,
Ruby, Chromium and Nix checks are fresh Luna/low-owned waits. Only Blocking or
Important review changes that materially alter the phase require a focused
rerun; reviewer-fix amendments do not restart review or verification on their
own. Aitherdev deployment is a forward, quiesced user-profile switch and one
portal/App Server restart; no configuration, migration or rollback work is
added. Durable behavior belongs in `docs/workspace-portal.md`; command behavior
belongs in `docs/dev-sessions.md`.
