# Creation lock contention: reproduced causes and fixes

Both failures are now reproduced before the fixes with an identified application
holder. `holdCreationConversation` invokes the portal's ordinary conversation
resolver for an in-flight queue reconciliation; that real admission retains the
shared runtime lock. It proves that EX on the same inode is blocked. For plan
creation, the Ruby subprocess reports the device/inode of its exclusive source
attempt and the test matches it to that portal-held lock. No synthetic mutex or
unrelated test path stands in for runtime locking.

The original CI guests were already destroyed, so their exact historical holder
PIDs cannot be recovered. This reproduction establishes an actual supported
interleaving that produces each exact CI error and its causal code path, without
claiming retrospective PID attribution.

## Occupied automatic name

`reservePreparationLocked` acquired the candidate's creation lock and requested
runtime EX before calling `destinationOccupiedLocked`. A normal portal operation
on the already occupied fallback session retained SH. The exclusive attempt
therefore returned `session is changing: resource temporarily unavailable`
instead of discovering the collision and selecting `-2`. Custom names had the
same premature failure, losing their normal collision error.

The fix rejects/skips known occupied candidates before requesting exclusive
runtime access. For unused candidates, the original lock order and final
occupied/ownership checks remain. Busy unproved names still refuse; a lock file
alone is never ownership or permission to choose another target. Request ID,
receipt, attempt and accepted prompt remain stable through collision/replay.

## Accepted plan source

`Runner.start` called `verify_creation_source!` with its default nonblocking EX
from inside `with_creation_lock`, which includes provider creation admission.
The portal queue reconciliation's legitimate source SH made that EX fail with
`another dev-session command is changing source`, before native effects.

The fix waits for source EX before destination/provider creation admission,
matching the already supported accepted-fork ordering. It retains the exclusive
proof and validates the same source after the wait. The deterministic tests prove
that destination creation/runtime locks remain available during the source wait,
replacement source is rejected before native effects, cancellation terminates the
waiting worker, and the original accepted receipt/attempt survives a healthy
wait. A separate real CLI recovery test interrupts after native root creation,
removes the source tracking, and completes the journal-bound original plan on
retry without reconsulting that source or sending its initial goal twice.

## Evidence

- `contention-reproduction.log`: both failures, known portal SH holder and
  matching Ruby contender lock identity, before source changes.
- `contention-quick.log`: new collision/plan/cancellation/replacement/recovery
  cases pass, web 2.937s.
- `contention-related.log`: related preparation, fork, plan and creation checks
  pass, web 12.803s.
- `contention-ruby.log`: 9 source/binding/recovery tests, 117 assertions, pass.

The changes preserve receipt/journal formats, native APIs, public request shapes,
custom-name identity, package-generation rules and ordinary direct-CLI policy.
The two fixes are independently reviewable commits above the archive work.
