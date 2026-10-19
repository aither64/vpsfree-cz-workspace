# Optional questions: design and verification brief

The lead owns this design and application edits. Scope and accepted interaction
are in plan.md. Substantive design uses xhigh effort.

## Interfaces and invariants

codex-web owns additive transcript fields for agent questions/delivery and parsed
native user replies. A question identity is JSON.stringify of
[request_user_input_async, native item ID, original question index]. Preserve
raw wire text and its digest; display answers as quoted question plus answer.
Encode replies in the pinned CLI's send_user_message_question_reply JSON array
envelope. Use normal authorized durable sends, never fake pending RPC requests.

Shared browser controller owns ordered transcript reconciliation, pin eligibility,
drafts, dismissal, in-flight identity and answer state. Separate controls render
inline and in a bounded pinned region outside transcript scroll. Every question
supports suggestions and free text. A submission disables both views until
accepted/reconciled. Do not remove uncertain attempts or regenerate their IDs.
Maintain composer and attachments independently. Arrival never steals focus.

Pin questions only from an active live turn, stop pinning after accepted normal
follow-up or turn finalization. Preserve drafts on unpinning. Inline unanswered
questions remain answerable after unpinning; answered questions show the answer.
Answering one question does not clear peers. Dismiss sends no model message.
No countdown/autosend. Replay and paged refresh cannot repin handled questions.
Canonical user reply envelopes resolve browser and terminal answers; matching
the old whole-item identity resolves all that item's questions.

Remote clients remain untrusted; all sends retain existing origin, authorization,
payload, retry and trusted-target checks. No browser-provided sockets/cwd/thread
authority. Local operator trust is unchanged.

## Compatibility, deployment and recovery

No native upgrade or state migration. Additive JSON, optional types and separate
browser keys preserve old readers. Maintain existing send digests and ledgers.
No database/API client/CLI/Terraform/Nix module/protocol format changes beyond
exposing already-supported native question metadata. Mixed browser/server
versions degrade to text; version assets together. Runtime composes published
codex-web; workspace/configuration select identical reviewed runtime revisions.
Use coordinated system then user-profile activation with aitherdev reservation;
forward-only application recovery. Feature deployment is not merge permission.

## Acceptance and checks

Go normalization and reply-envelope tests, shared browser state tests, rendered
controls and durable-send tests, portal Playwright flow with real templates,
mobile/keyboard/focus checks, legacy mandatory request regressions. Test live
turn completion, follow-ups, dismiss, replay, pagination, reload, thread/member
switching, identical titles, cross-client answers, late inline reply, read-only
capabilities and transport uncertainty. Quick checks precede final committed
independent review; longer native/browser/package checks follow it. Record
commands and evidence in state, use fresh utility watcher for long operations.
