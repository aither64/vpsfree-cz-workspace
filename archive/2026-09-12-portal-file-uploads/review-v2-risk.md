# Risk and compatibility rerun

Reviewed the high-risk remediation at the exact packet heads:

- `codex-web` `39abf28707ac3417bfc1b1a26361d52f4f21e26d`
- `dev-workspace` `32760301b56dc490a12874edf854ae84d5bc89f5`
- `vpsfree-dev-workspace` `f0761fbbc75a44d6470b248df62bec4878cfbebc`
- workspace `f27c721bbd7ad5b3404d12112ae08b651e559827`
- `vpsfree-cz-configuration` `3f4375a33ef350ad008ec2e40b40ca332a32ab91`

I read the original packet and first-round reconciliation, the complete commit
series, applicable repository instructions, queue deletion and submission-ledger
code, upload catalog transitions and compaction, lifecycle authority and
retirement paths, rollback documentation, regression tests, and current consumer
pins. The development-host operator is treated as trusted as required; browser
requests, ordinary persistence failures, concurrent lifecycle operations and
package transitions remain inside the reviewed boundary.

## Blocking

No Blocking findings.

## Important

### Queue refresh performs durable completion without mutation authority or serialization

Commit: `codex-web` `39abf28707ac3417bfc1b1a26361d52f4f21e26d`.

`GET /queue` now calls `ReconcileQueueDeletionsWithCompletion` before returning
the queue (`conversation/handler.go:542-560`). For an absent recorded entry this
can call `AttachmentProvider.QueueDeleted`, which changes the application catalog,
and then clear the Codex deletion and submission attempts
(`codex/client.go:3582-3617,3629-3649`). This is a durable mutation that can
release an attachment submission from its unresolved `queued` state.

The handler still classifies every GET as non-mutating, passes `Mutation: false`
to the application resolver, does not require an exact-origin mutation request,
and does not acquire `Target.MutationLock` (`conversation/handler.go:255-297`).
That contradicts the public target contract that every operation mutating a
conversation shares the application mutation lock (`conversation/handler.go:84-105`;
`conversation/mutation_lock.go:5-18`). In the concrete runtime it also bypasses
the transition lock, current-package check, runtime shared lock and pending
lifecycle check that `resolveConversation` performs only for mutation requests
(`portal/internal/web/server.go:2282-2326`).

Consequently a queue refresh can finish catalog and ledger state while a queue
start, lifecycle command or package transition owns the mutation boundary. In
particular, it can race a queue start between the absent-queue observation and
the history check used to decide whether provider cancellation is safe. It also
lets a consumer that grants queue-read authority but withholds mutation authority
run completion callbacks. The callback-before-ledger ordering prevents the
original persistence leak, but it does not substitute for current mutation
authorization and serialization.

Move recovery to an explicitly mutating operation, such as a POST queue-reconcile
endpoint. It should use exact-origin validation, mutation capability resolution
and the application's shared mutation lock before invoking the completer. Queue
GET should remain observational. Cover that GET does not complete a pending
deletion, the mutation endpoint waits for `Target.MutationLock`, and a POST
without the allowed origin is rejected.

## Advisory

No Advisory findings.

## Compatibility and residual validation

Apart from the authority issue above, the new two-store completion ordering is
sound. The concrete client records the unchanged schema-3 deletion identity
before the App Server request, invokes the idempotent provider completion before
clearing that identity, and retains it when either provider persistence or the
final ledger write fails (`codex/client.go:3507-3579`). Absent-entry recovery
does not issue another App Server deletion and checks exact client-message text
in history before deciding whether the queued input started
(`codex/client.go:3582-3649`). Lifecycle validation now reports any retained
deletion identity rather than clearing it without the provider
(`codex/client.go:2245-2252`).

The runtime catalog transition is idempotent, keeps `pending` and `queued`
submissions pinned, and refuses ordinary file deletion while either state remains
(`portal/internal/uploads/store.go:861-901,645-726`). Catalog compaction preserves
live sent and fork references, while explicit exact-owner session removal removes
the owning submissions and tombstones bytes before reclamation
(`portal/internal/uploads/store.go:227-271,930-993`). I found no additional data
loss, authorization or mixed-version defect in those remediation paths.

All consumers select the reviewed pair: the runtime Go and Nix inputs pin
`codex-web` `39abf287`; the organization, workspace and aitherdev configuration
pins select runtime `32760301` through the recorded heads. The documented rollback
boundary is accurate: an older package can clear the unchanged Codex deletion
receipt without updating the independent upload catalog, but the stale `queued`
submission remains pinned. Rolling forward therefore retains bytes until exact
owner-session deletion; it does not expose or erase them. The operator must finish
pending queue deletions before rollback as documented in `dev-workspace/README.md:219-226`.

After the Important finding is remediated, focused tests should exercise the new
mutation route across provider-write failure, ledger-write failure and restart.
The planned real-browser/live App Server run, explicit rollback/roll-forward
exercise, 1 GiB bounded-memory transfer, package deployment and live lifecycle
checks remain necessary integration validation; they had not started at this
review checkpoint.
