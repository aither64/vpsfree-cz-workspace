# Preserve observations across forced VM replacement

A retained-services fixture replaces its OSVM machine object between boots.
Two constraints need explicit handling at that boundary.

## Keep the pinned restart gap

Pinned OSVM `Machine#start` waits for a five-second gap after its own reaper
records a stop. Constructing a new machine loses that instance timestamp. A
fixture that replaces objects must retain a monotonic stop-completion time
after successful stop/kill, kernel check, finalize and cleanup, then wait only
the remaining gap before starting the replacement. Keep the new object in the
native evaluator's shared registry and recheck retained disks immediately
before start. A startup error must still fail the test.

The focused real-main probe covered initial, immediate, partial and expired
gaps plus error propagation without starting a guest. A later native run
completed the replacement boot. This does not prove that timing was the only
cause of an earlier virtiofs lock failure.

## Flush instrumentation before a deliberate power cut

A shell append followed by a visible marker establishes ordering, not durable
storage. The fixture observed its first new-seed marker, removed it, then
killed the guest. A later boot completed but the final counter contained only
one start. Buffered instrumentation loss is a plausible explanation, not a
proven exclusive cause.

While the new seed remains blocked, remove its entered marker and run
`sync -f` on the containing fixture directory before the forced cut. Propagate
removal or sync failures and retain the requirement to observe two starts.
Flushing the counter alone would leave marker deletion unprotected and could
let a stale marker satisfy the next boot's readiness check.

A focused real-main probe used a private temporary filesystem and the actual
shell tools. It verified successful removal/reopen, and that removal/sync
failures prevent the cut. That proves command behavior. The final native
forced-cut/reboot scenario passed with both starts and preserved SQL/payload
projections; it does not establish a general power-loss guarantee.

Related initiative: [storage redesign](../../work/2026-09-23-storage-redesign/state.md).
