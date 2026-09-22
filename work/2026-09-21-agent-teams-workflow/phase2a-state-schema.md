# Phase 2A dormant state schema

This records the retained designer's schema checkpoint before any managed state
is emitted. Root keys remain exactly:

```text
schema state_revision workspace slug removal_epoch creation_identity
root_thread_id catalog selection pending_transition dispatch members history
```

`removal_epoch` is the lowercase 64-hex digest returned by
`session.CompletedRemovalHistory`. Catalog names use the catalog identifier
grammar. Runtime, request and native identifiers are opaque valid UTF-8 strings
of 1–512 bytes without ASCII controls.

## Selection

`selection` contains `selection_revision`, `team`, `team_digest`, tri-state
`lead_overrides`, the exact `effective_lead`, and catalog/team/role provenance.

## Pending transition

A non-null pending transition contains:

- distinct transition and caller request IDs;
- state `pending_boundary`;
- base state and selection revisions;
- exact before and requested-after selections;
- actor, reason and request time;
- a root-turn blocker with root thread ID, optional turn ID and observation
  time; and
- an optional trusted `same_root` continuation with source turn ID, intent
  digest and capture time.

It is persisted only when the current root turn is the sole remaining boundary.

## Dispatch

A non-null dispatch binds request and client-message IDs, action
(`initial_message`, `user_message`, or `continuation`), delivery (`start` or
`steer`), message/options/context digests, exact selection revision/team/digest
and effective lead, state (`prepared`, `submitting`, `accepted`, or `unknown`),
nullable turn ID, and request/update timestamps. Accepted requires a turn ID;
prepared and submitting forbid one; unknown permits either. Policy-bearing
sends are start-only.

## Members

Each member records a bounded opaque ID, behavior, generation, independence,
desired lifecycle (`active`, `inactive`, or `shutdown`) and nullable observed
Codex status. Verification watchers are never members.

Creation records the caller request, delivery state, immutable catalog/team/
role/selection provenance, actual spawn model and effort, generated native role
name, fresh-context flag and request/acceptance times. Requested settings are a
separate current binding with their own allowed variant and reason. Observation
records nullable model/effort, verification level and evidence source.

Native provenance keeps the generated config name plus actual task name,
canonical agent path, optional thread ID and observation time. Generated config
names and task names may repeat across replacements; canonical agent paths and
nonnull native thread IDs are unique among retained members.
Assignment provenance includes distinct assignment/request/work-unit IDs, task
digest, selection/team/role, delivery/outcome state and lifecycle timestamps.
Write ownership is nullable structured provenance tied to an assignment and
scope digest.

Observed member states mirror the installed Codex `AgentStatus` values:
`pending_init`, `running`, `interrupted`, `completed`, `errored`, `shutdown`,
`not_found`, plus the single forward-compatible bucket `unknown`.

## History and static integrity

History records transition/request IDs, base and completed revisions, before,
requested and actual-after selections, outcome (`applied` or `cancelled`),
actor/reason and request/completion times. Applied transitions have
`after == requested`; cancelled transitions have `after == before` while still
preserving the requested target. The base revision is the caller's original CAS
base. Completion must advance beyond it, but need not be exactly the next
revision because publishing a pending transition and unrelated member or
dispatch observations can consume intervening revisions. In retained order,
each later base revision must be at least the preceding completion revision,
and completion revisions remain strictly increasing.

Publishing a pending transition advances the state document while preserving
that original base, so a pending record has `base_revision < state_revision`.
Resolution preserves the base and records the post-CAS state revision as the
completion revision.

`ValidateAgainst` validates current, pending and historical selections against
the pinned catalog; transition revision ordering and chaining; uniqueness of
request IDs within each operation domain (with pending transitions and retained
history sharing one transition domain); transition and native identities;
creation and requested role variants; member revision bounds; delivery/outcome
timestamp equations; and write-owner referential integrity. Live root/child
idleness, blocker liveness, current writer activity and observed App Server
settings remain later manager responsibilities.

Transition deduplication is bounded by retained history. Phase 2C must not claim
session-lifetime idempotency after history eviction unless it adds compact
request tombstones; expected-revision refusal is useful but is not an equivalent
deduplication guarantee.
