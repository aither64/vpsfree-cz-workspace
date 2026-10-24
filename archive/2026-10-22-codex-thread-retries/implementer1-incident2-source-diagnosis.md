# Delivery incident2 — prepared plan action and managed provenance

Owner implementer1, read-only diagnosis at deployed B
ed2a75b98a75f9b37b7a359e9091a94e9846644e; A c1f unchanged.
Session identity verified; deployed B bundle, full series and diff retained.
No live records, prompts or history inspected; no application edits or tests.

## Confirmed legitimate ordering

Server.implementPlan (portal/internal/web/server.go2527–2660) uses fixed text
Implement the plan., the original browser UUID, action plan:<turn>:<sha256>,
and zero generic TurnOptions. The conversation message lock covers:

1. Exact ReconcileSend before proposal freshness checks.
2. Validate exact completed current plan, digest, turn, idle status and mode.
3. In Plan mode, generic PrepareSend(false) reserves that immutable tuple.
4. Managed UpdateThreadSettings(Default) advances the provenance epoch before
   settings; an idle turn cannot inherit the I3 active witness.
5. Managed Send enters reconcileRetrySend. Generic Reconcile returns notfound
   for prepared; SendAttempted returns true for any durable exact attempt;
   second Reconcile still returns notfound. No retry admission exists because
   the generic preparation preceded it. ed2 then returns earlier submission
   has no managed admission proof before native delivery.

Already-Default retry uses SendAttempted(true) to authorize repeating the same
plan decision, so it encounters the same rejection. Generic options are zero,
not rederived model/effort. Root capture fills its separate proof from current
authorized settings only after that explicit mode change; generic immutable
identity must remain unchanged. Existing plan tests use browserContractCodex
and miss this composition.

## Additional outer resolver boundary

Actual Server.Handler sessionAPIForSummary takes the normal runtime fence and
calls requireOrdinaryRetainedMutation before implementPlan. For a retained
creation-less root, ObserveRetained/ObserveThreadIdentity require every generic
submission to be known. A prepared plan identity left by the refused request
is counted unresolved, so actual HTTP recovery can stop before the handler's
exact-ID receipt/prepared logic. A direct implementPlan-only test would miss
this. New regression must use the production HTTP path with the real managed
client and synthetic private wire. Ordinary-send incident ownership is separate;
this source finding does not establish the live cause.

## Source-derived preparation consumer inventory

Non-test production PrepareSend call sites in B:

- server.go2618: this plan decision; generic Prepare before managed Settings
  and managed Send. This is the demonstrated regression.
- workspacecodex/recovery.go72: cold assignment recovery prepares only after
  managed capture/admission and generic exact reconciliation, then delegates
  the same identity to native queue and explicit activation. Its existing
  snapshot and queue hold must stay protected.

Other production send consumers do not call PrepareSend first themselves:

- teamruntime/runtime.go2332: managed SendWithOptions after exact retained
  assignment identity; accepted options compaction retains their digests.
- web/member_conversation.go99: managed SendWithOptions after original option
  lookup and unchanged authorized member policy.
- cmd/workspace-portal/coordination.go105–110: exact generic reconciliation
  followed by managed SendWithOptions using durable outbox options; prepare
  action reads/saves options only, without reserving generic send.
- native generic SendWithOptions itself reserves before marking submitting;
  automatic ContinueFailedTurn remains exact proof/reconcile-only and must
  not gain a fallback through this fix.

## Unchanged A recovery primitives and pitfalls

OriginalSendOptions binds text/action and retrieves immutable options, but does
not prove prepared state. Reconcile notfound alone also does not prove absence.
DiscardPreparedSendWithOptions validates exact text/action/options digest under
the native ledger lock, returns true for absent or removes only an exact
prepared nonqueued identity, and returns false for submitting/accepted/queued.
It is not a general permit to recreate provenance from current defaults.

Generic SendWithOptions checks its saved Steered flag against actual active
state before native delivery. Deleting/recreating a prepared identity must not
lose that guard. Any approved exact positive-unsubmitted admission route must
preserve UUID/text/action/original options and ordinary loaded/policy/fence
holds; submitting/accepted remains reconciliation-only with no replacement ID.
A new Prepare override capturing before Plan→Default would instead create stale
epoch evidence; that is not valid execution provenance after settings intent.

Await architect-owned saved scope before any substantive edit. B successor must
be additive after deployed ed2; no A/schema/UI/native-version/pin change or
live record repair/reset/resend is authorized.
