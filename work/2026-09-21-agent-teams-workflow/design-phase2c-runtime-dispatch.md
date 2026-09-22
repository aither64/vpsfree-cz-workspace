# Phase 2C runtime dispatch and retained teams

## Decision

Phase 2C is four generic `dev-workspace` commits. It has no offline migration,
state-root schema bump, daemon, or normally a `codex-web` change. Schema-1
sessions remain legacy indefinitely. The user's explicit low-cost decision also
keeps an unmanaged-source fork on the legacy continuation path; this Phase does
not convert its source or destination.

## 2C.0: durable provenance dispatcher

Create one strict reader/classifier for the creation journal, managed state and
pinned catalog. Classify each session as `legacy_unmanaged`, `managed`,
`managed_recovery`, or corrupt. A valid schema-2 journal with mismatched or
missing state/catalog/binding, a state without matching schema-2 provenance,
or malformed current identity is corruption and every mutation fails closed.
Only an absent or valid schema-1 journal without state is legacy.

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

Each commit gets focused tests and mandatory Sol/xhigh review. Full Go, Ruby,
Chromium and Nix checks are fresh Luna/low-owned waits. Aitherdev deployment is
a forward, quiesced user-profile switch and one portal/App Server restart; no
configuration, migration or rollback work is added. Durable behavior belongs in
`docs/workspace-portal.md`; command behavior belongs in `docs/dev-sessions.md`.
