# Architecture and repetition review rerun

Reviewed the focused remediation described by `review-packet-v2.md`, together
with the original packet, reconciliation, initiative plan/state, repository
instructions, commit series, public interfaces, runtime consumer and tests. The
exact reviewed heads are:

- `codex-web` `39abf28707ac3417bfc1b1a26361d52f4f21e26d`
- `dev-workspace` `32760301b56dc490a12874edf854ae84d5bc89f5`
- `vpsfree-dev-workspace` `f0761fbbc75a44d6470b248df62bec4878cfbebc`
- `workspace` `f27c721bbd7ad5b3404d12112ae08b651e559827`
- `vpsfree-cz-configuration` `3f4375a33ef350ad008ec2e40b40ca332a32ab91`

The pin graph is consistent at those heads. The existing Codex schema-3
deletion intent remains the single durable coordinator, the upload catalog owns
application completion, and lifecycle validation now fails closed while an
intent remains. Catalog compaction also preserves queued and unresolved
submissions. I found one remaining interaction between queue recovery and the
started-message path.

## Important

### 1. Queue start does not join deletion-completion serialization, so a started attachment can be committed as cancelled

Commit: `codex-web` `39abf28707ac3417bfc1b1a26361d52f4f21e26d`;
consumer: `dev-workspace` `32760301b56dc490a12874edf854ae84d5bc89f5`.

`DeleteQueueEntryWithCompletion` and
`ReconcileQueueDeletionsWithCompletion` serialize through the per-thread
`queueUpdateLock` (`codex/client.go:3509-3518` and
`codex/client.go:3585-3603`), but `StartQueue` does not acquire that lock
(`codex/client.go:3677-3725`). Queue refresh can run concurrently with Start:
GET is classified as non-mutating and therefore does not take the application's
`MutationLock` (`conversation/handler.go:264-297`), even though the queue GET
now runs deletion completion (`conversation/handler.go:542-559`). This is a
real portal interleaving because refreshes are event driven while the Start
request is in flight.

A deletion request can durably record its intent, fail while the App Server
entry remains, and leave that entry available to Start. If Start removes the
entry while a concurrent refresh is reconciling, the refresh can observe the
queue entry as absent before `thread/items/list` exposes the started user
message. `finishAbsentQueueDeletion` makes one history observation and, when it
does not find the message, invokes the application completion callback and
clears the deletion intent (`codex/client.go:3629-3649`). Nothing in the public
contract or locking establishes the cross-endpoint visibility ordering on
which that decision relies; elsewhere the client explicitly polls for delayed
started-message visibility (`codex/client.go:3423-3443`).

The runtime callback then changes the upload submission to `cancelled`
(`portal/internal/uploads/store.go:861-872`). Cancelled submissions no longer
pin their files during collection (`portal/internal/uploads/store.go:875-901`).
For an input that has remained queued for more than seven days, the next
collector can therefore tombstone its bytes immediately, and compaction removes
the cancelled submission once those files are deleted
(`portal/internal/uploads/store.go:225-270`). A later transcript observation can
no longer restore the association, so Codex may receive a path whose contents
were reclaimed while its started turn is using it.

Serialize recovery with Start before it can invoke application completion. An
explicit mutation endpoint that takes the same application `MutationLock` as
Start would do this while keeping queue GET observational. Serializing the two
inside the client, or rejecting Start while deletion is pending, would also
close the ambiguity. Add a regression that begins with a retained deletion
intent and a present entry, holds Start's mutation lock while recovery is
requested, and proves that completion cannot run until Start releases the lock.
The current started case sets history visible before reconciliation
(`codex/client_test.go:4493-4509`), so it does not exercise this ordering.

## Residual validation

No additional Blocking or Advisory architecture findings were identified. The
planned live App Server and browser checks remain useful, but they will not
deterministically exercise this interleaving without the focused regression
above. The accepted rollback boundary remains retention-only and does not
change this finding.
