# Final remediation verification

Retain your existing reviewer identity, model and effort. Read the previous two
reports. All source is committed and quick checks pass. Inspect the focused
remediations to F1-F3 and the final full-series/pin identities, without repeating
unaffected UI review or running long tests. The change stays in the already
reviewed delivery contract.

Final ranges:
- codex-web 11ec57d2203fc735696fe75a837d47da55a5c6af..57dd01b1d860181e12aa7ccb37ecdeae8b2c08c5
- dev-workspace b3a6eb2fc0b41cf0cb965bf4c39991815d9df734..fac4e6a3d2169dd81d0ae9bb891e7f8ca62114de

F1: all pre-dispatch failures after initial reconciliation now use one
unwrittenSendOutcome helper, including resume/turn-state failure and cancellation
before the admission callback. It reads send and queued state in one ledger
transaction; advanced, missing-after-prepare or unreadable state stays unknown.
An exact accepted receipt is returned directly; an actually prepared attempt
stays definitely unsent. Only an initial absent attempt before preparation may
remain absent and be classified unsent.

F2: that snapshot uses the original normalized options digest. The two-client
fixture now runs the cancelled/noncancelled losing caller matrix against both
uncertain and already-accepted winner outcomes with nonzero model/effort.
Accepted winners recover the exact receipt; uncertain winners never report
MessageNotSentError or emit another mutation.

F3: SendAttemptedWithOptions no longer invokes mutation admission. The existing
recording transaction accepts an optional positively proven receipt and records
it atomically as accepted, validating message/context/options/steering and any
existing accepted turn. There is no transient prepared state for history
adoption. Concurrent history callers both recover the same receipt without any
native mutation. This shares the existing attempt persistence implementation
rather than adding a parallel format or persistence framework.

Focused codex Go selectors (Send|SharedLedger|SharedHistory|CanceledWrite|
AlreadyCanceledWrite|OperationTimeout), protocol corpus coverage, portal Node
notice/composer contracts and focused portal Go checks pass. Browser corrections
I1-I3 remain unchanged from your accepted follow-up. Native Codex stays fixed;
no migrations or ledger schema changes. Provider source remains one consolidated
functional commit. Runtime remains functional plus one final dependency commit.
Go/Nix selections and vendor hash match the final provider. Intermediate source
and pin versions have not been deployed by this initiative.

Write review-remediation-report.md here. If resolved, explicitly release the
long-check gate and retain any actual residual verification limits. User's merge
authorization remains conditional on deployment and verification first.
