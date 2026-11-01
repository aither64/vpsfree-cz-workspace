# Final source review follow-up

**Three Important findings in the added shared-client admission boundary; no
Blocking findings.** All three original browser findings are corrected.
Fix or explicitly record acceptance of the new findings before long checks.

## Important F1 — Pre-write cancellation can still misclassify another client's dispatched message

`codex-web` `f66a8b2f`, `codex/client.go:5184`–`:5198`, with the pre-admission
context check at `:1213` and the earlier direct returns at `:5156`–`:5165`.

The new shared-state reconciliation only runs when the error is specifically
`errSendAdmissionChanged`. A waiting sender whose context is cancelled is
rejected before its admission callback runs, so that error is a transport
cancellation instead. The caller then receives `MessageNotSentError` even when
another client has already claimed and dispatched the very same saved attempt.

Concrete sequence, using the new shared-ledger test's own arrangement:

1. A observes/prepares the attempt and waits behind A's writer mutex.
2. B claims the shared prepared record, writes the native mutation, and holds
   its reply. The shared record is now `submitting`.
3. Cancel A's context, then release A's writer mutex.
4. `writeOfferAdmission` returns before invoking `admit`; A returns
   `MessageNotSentError`, although the original message is already dispatched
   and its delivery is uncertain.

The same stale initial-state assumption exists in the resume/turn-read failure
returns. Recheck the relevant shared attempt before declaring non-delivery on
these exits; an advanced or unreadable shared state must stay conservative.
Preserve the positive pre-write refusal for an attempt that really remains
unsubmitted. Extend the two-client fixture with the cancelled losing caller and
assert uncertain/accepted delivery, never `MessageNotSentError`.

This does not itself emit a second native mutation. It violates the public
delivery-evidence contract and feeds the portal a false `notSent: true`.
Lanes: general, risk/compatibility.

## Important F2 — Losing optioned sends reconcile with the zero-options identity

`codex-web` `f66a8b2f`, `codex/client.go:5186`.

The new losing-admission branch calls `c.sendAttempt`, whose implementation
always supplies `zeroTurnOptionsDigest()`. An attempt created through
`SendWithOptions` with a model, effort, policy or additional context therefore
fails this lookup with an identity-mismatch error. The branch ignores that
lookup error and returns unknown delivery, even if the shared record already
contains a valid accepted receipt.

Member sends and managed continuations are actual optioned consumers, as shown
by `dev-workspace/portal/internal/web/member_conversation.go:99` and
`portal/internal/workspacecodex/turn_retry_proof.go:233`. The default-options
two-client test cannot expose this bug.

Use the normalized options digest already owned by `SendWithOptions` for the
fresh lookup and retain meaningful lookup failures. Cover an optioned losing
sender whose winner's receipt is already accepted when admission is refused;
it should recover the same receipt without another mutation.

Lanes: general, architecture/consumers, risk/compatibility.

## Important F3 — History recovery still uses the now-exclusive mutation-admission helper

`codex-web` `f66a8b2f`, `codex/client.go:5374`–`:5383` and `:2813`.

`markSendSubmitting` used to accept an already-submitting record. It now
exclusively claims a prepared record, but `SendAttemptedWithOptions` still uses
it while reconstructing a receipt from positive native history.

Two independent recovery callers can both initially find no ledger record and
both obtain the same accepted native-history proof. Both can complete
`recordSendAttemptWithOptions`, which accepts an identical existing record.
One caller then advances it to `submitting`; the other caller's
`markSendSubmitting` now returns `errSendAdmissionChanged`, even though delivery
has already been positively established. That caller returns `false, err`
instead of recovering the accepted attempt. The conversation handler treats
this untyped error from `SendAttempted` as generic service unavailability.

Adapt this existing consumer to the new exclusive-claim semantics. Prefer
recording/adopting a positively proven history receipt atomically under the
ledger transaction, checking the immutable bindings and any existing receipt,
rather than representing observation as fresh mutation admission. Add a
two-client history-recovery test with both callers starting from an absent
record; both should recover the same acceptance without native mutations.

Lanes: general, architecture/ownership, risk/compatibility.

## Original findings

- **I1 resolved:** composer retries save `unknown` before HTTP and present
  `sending` in memory. The VM test checks both; the real-browser regression now
  reloads while the retried request's response is held and expects unknown.
- **I2 resolved:** failed retry persistence derives `notSent` from the original
  attempt's state. An unknown original retains uncertain guidance.
- **I3 resolved:** queue-start creates and passes its operation token on both
  completion paths. The new controlled completion tests preserve newer
  feedback against both old success and old failure.

These are narrow corrections within the original reviewed design. No remaining
browser issue was identified in the follow-up diff.

## Complete series, pins and migrations

Reviewed the full final ranges and their differences from the first reviewed
heads:

- `codex-web`: `11ec57d2203fc735696fe75a837d47da55a5c6af` to
  `f66a8b2f46a6d43115327f42edbdaf58581e3c25`; one functional commit.
- `dev-workspace`: `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` to
  `13308f030bd1e88c5cbb94cf1aa308cfc814f2c2`; functional commit
  `74dbf68d29b6694cddf0f0f2f5b865ea9c8b41ed`, then dependency commit
  `13308f030bd1e88c5cbb94cf1aa308cfc814f2c2`.

Worktrees are clean and `git diff --check` passes for both complete ranges.
Corrections are folded into their owning source commits. No obsolete branch
iterations or fixup commits remain in the final series. Behavior and dependency
selection remain separately reviewable.

**Pin consolidation:** no repeated update stream remains in either final
series. The single final Go/Nix dependency update consistently selects
`f66a8b2f46a6d43115327f42edbdaf58581e3c25`, with the corresponding module
pseudoversion and vendor hash. Earlier checksum entries do not select another
provider version. Workspace/configuration mechanical pins remain outside this
source review and must ultimately select the final accepted runtime.

**Migration lineage: no migrations.** Schema 3 and the native protocol remain
unchanged. There is no intermediate unpublished schema or migration retained
solely for an abandoned branch design.

## Remaining lane assessment and verification

The shared-ledger claim belongs in codex-web and directly addresses a real
concurrent-writer failure. The exclusive state transition is appropriately
bounded; no native deduplication framework or protocol expansion was added.
The default-options fixture correctly proves one mutation when two upgraded
clients reach admission. F1–F3 concern surrounding evidence classification and
existing consumers of that state transition, not the need for the transition.

The original authorization, origin, attachment, private-state and bounded HTTP
lifetime assessment remains applicable. Source/API and persisted formats remain
compatible. The stronger claim is enforced by upgraded clients; mixed old/new
clients still inherit the old client's non-exclusive admission behavior, so
rollout should avoid overlapping old and new same-ID mutation attempts. Native
Codex remains unchanged. Project documentation remains correctly placed and
discoverable, but its broad admission/reconciliation guarantee depends on the
corrections above.

Reviewer identity is the same independent `/root/final_review` under retained
`gpt-6.1-sol/xhigh` policy. I reread the mandatory review instructions, all four
lane references, packet, prior report and relevant project guidance. This
follow-up used source/history inspection and quick diff checks only; it made no
source edits and ran no long tests or deployment. Findings F1–F3 are supported
by the concrete control flow above; no new reproduction test was added by the
reviewer.

After remediation and focused verification, full packaged/native checks,
Chromium/Firefox execution, exact composition/deployment-contract checks and
live verification remain pending. No deployed result is certified here. The
packet's newly recorded user integration authorization is conditional on
successful deployment and verification first; this report does not satisfy
those operational conditions.
