# I-B1: stale checkpoint can overstate count quality

Status: Important finding accepted for remediation. Final review completed on
B85eb687a597df116690d6481ca2ec5d4ea94f0cd; full report in review.md.
Owner: implementer1. Lanes: general/risk. This file is the finding/remedy brief.

Reviewer0 source finding: portal/internal/web/turn_retry_activity.go:67 copies
ConfirmedStarts/CountQuality from an optional checkpoint without checking the
authoritative current Pending/ResultTurn or checkpoint PendingID/LastConfirmed
continuity. Controller.dispatch:306–310 saves acceptance first and deliberately
ignores optional checkpoint failure.

Concrete supported state: an exact-zero summary contains scheduled UUID P;
native accepts P; ledger saves Pending.ResultTurn; a write failure or crash
prevents summary update. GET activity still loads the readable old summary and
returns confirmedStarts=0, countQuality=exact, unconfirmed=0 although the ledger
proves P accepted. The existing summary-failure test establishes this persisted
state without checking HTTP presentation. Failed Stop checkpointing and later
manual retirement can also expose a known continuity gap.

Accepted contract requires partial/unavailable evidence after a checkpoint gap.
The lead checked the cited view/dispatch boundary and accepts the finding.
Prepare a narrow read-only view-quality reconciliation against current ledger
and checkpoint identity, or conservatively partial/unavailable output. Do not
write sidecar on GET, infer counts from Attempt/quota, or make summary success a
Stop/manual/receipt precondition. Add focused view and actual-HTTP coverage for
accepted-result checkpoint failure, Stop checkpoint failure and known retirement
gaps. Preserve exact chain/pending/action/recovery behavior.

Source correction is now RELEASED after the completed review and lead acceptance
of I-B1-remedy-plan.md. Only the activity view and owning test file may change;
preserve exact85eb ref/bundle/packet and fold correction into the owning commit.
Final disposition requires owning implementation, focused checks, committed
history and lead step9 inspection. A new design/contract expansion requires
affected-lane review under the normal policy. Longer verification stays held.
