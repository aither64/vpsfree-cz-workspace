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

Resolve against the session-pinned catalog and current registration evidence.
The public CAS key is `selection_revision`; internal state writes use
`state_revision`. Apply immediately only when root and members are idle. A
pending next-turn boundary is allowed only from the exact active root runtime;
browser requests during an active turn return controlled busy. Applying a
pending change is atomic before the next real idle send: it updates selection,
member eligibility and bounded history but never opens a blank turn or spawns
members.

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
