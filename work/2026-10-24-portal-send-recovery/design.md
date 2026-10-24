# Delivery and feedback design

## Dispatch safety

Keep schema-3 ledger states. Mutation admission must distinguish a request that
never entered WebSocket Write from any uncertain write/reply failure. Persist
`submitting` at admission, preserve `prepared` for proven pre-write refusal, and
never downgrade a previously uncertain attempt using absence from history.
Return additive structured delivery codes and `notSent` through the HTTP layer.
Preserve immutable message/options/context bindings and acceptance reconciliation.

An authorized portal send gets a bounded server-owned operation context after
validation and lock acquisition. Browser cancellation before admission refuses
safely; after admission it must not cancel dispatch or receipt recording.
Honor server shutdown and the existing request deadline. No persistent job
queue or native Codex protocol change is introduced.

## Recovery controls

Retry original keeps its existing identity. An unknown ordinary receipt also
offers Send another copy. Reconcile first; accepted original means no new send.
Otherwise require explicit acknowledgement that the original might arrive.
Persist one replacement ID before dispatch, retain the original record, and
reuse the replacement ID after failures/reloads. Preserve text/attachments and
the unrelated current draft. Older clients may ignore additive browser metadata.

## Composer feedback

Bind global feedback to the latest composer operation generation within the
selected conversation. A newer successful send/queue clears prior global send
feedback; old receipts remain independent. Late older failures cannot restore
stale feedback. Successful observation alone is not proof of message delivery.

## Verification

Exercise cancellation before admission and immediately at the write boundary,
lost accepted replies, restart before/after dispatch, same-ID concurrent retry,
legacy uncertain attempts, explicit replacement confirmation and stable IDs.
Browser checks cover original failure/reworded success/banner clearing,
late responses, reloads, attachments, storage errors and draft preservation.
Quick Go/JavaScript checks precede committed final review; packaged/browser and
native integration checks follow review. Use only disposable fixtures.

## Composition and operations

Keep native Codex and unrelated inputs fixed. Select the reviewed codex-web
feature revision in dev-workspace's Go and Nix inputs. Select matching runtime
revisions in the composed workspace and confctl-managed devWorkspace channel.
Build/copy outside claims, activate under ordinary shared aitherdev ownership,
then select the separate application profile. Preserve journals and forward-only
profile recovery. Verify portal/router health and existing conversations; do not
send the original affected message. Keep branches unmerged pending direction.
