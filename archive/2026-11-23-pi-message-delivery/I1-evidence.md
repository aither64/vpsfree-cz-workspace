# I1: shared delivery and persistence inventory

Investigation only; implementer1. Verified session and matching environment identity.
Read session plan/state, workspace routing/procedures, both repository AGENTS,
README entry points and the delivery/backend/storage docs cited below. No source
edits, tests, native/runtime reads, merge, deployment or package changes.

Inspected clean registered worktrees at dev-workspace
`f3bd843f9858b87cef66d0949706f8af16ba9b13` and codex-web
`3209aa7bf93e2c7067b07494d1b254741812d714`.

## Existing browser and HTTP boundaries

- codex-web `conversation/assets/conversation.js`: `createConversationClient.message`
  accepts text, original ID, retry, attachment IDs and optional `delivery`.
  `createDurableSender` uses `createDurableAttemptStore`, verifies storage writes,
  binds retries to endpoint/namespace and retains one outstanding send or queue.
  It has no delivery-mode argument. It saves every successful message reply as a
  receipt; retirement requires transcript ID/digest plus server acknowledgement.
- Actual portal composer uses the shared storage helper, client and retry
  scheduler, but its own `createMessageDispatch` in `web/static/app.js:305`.
  Its schema-1 per-tab FIFO holds up to 20 entries. It persists `unknown` before
  HTTP, dispatches sequentially, and blocks on uncertainty. Browser receipt and
  dispatch state for Pi use scope-bound `sessionStorage`; closing the tab loses
  dispatch ownership. Codex queue-attempt records use `localStorage`; Pi's
  follow-up uses the message endpoint with delivery `followUp`, not that queue.
- Existing states include waiting/sending, accepted/observed, native pending,
  unknown and positively unsent/terminal failed. `savePiPending` only accepts an
  exact 409 `message_pending`, `pending:true`, matching ID and matching mode.
  Later steers can pass a natively queued follow-up. Background enquiries use
  the original POST with `retry:true` and mode; they do not generate a new ID.
- `acceptMessageReceipt` treats HTTP success as accepted. Explicit Pi modes also
  require the exact ID and nonempty native turn ID before that point. An
  unqualified 202 queue receipt would therefore either display Sent incorrectly
  or fail that guard. Portal durability needs an explicitly recognized state.
- Pi observation retires the browser card while retaining the native receipt;
  the portal deliberately skips Codex's server acknowledgement path for Pi
  (`app.js:5322`). Generic durable-sender acknowledgement cannot simply replace it.
- `conversation/backend/operations.go` owns `SendRequest` and outcomes
  Accepted/Pending/NotSubmitted/Unknown. `conversation/handler.go:495` validates
  mode before preparing attachments, then sends prepared text. Accepted returns
  202; Pending returns 409 only for explicit delivery; NotSubmitted returns 503
  with positive notSent/retryable proof; Unknown returns 409 without resend proof.
  Pending currently means same-process native enqueue, not portal persistence.
- The handler resolves and verifies before payload handling, then takes the
  mutation lock. Portal `resolvePiBackend`/`piAdmittedConversation.Verify` currently
  bind and verify Pi before Send; native-free durable admission cannot be achieved
  only by changing the final Send implementation. These are concrete integration
  points for the architect's brief, with current authorization retained.

## Persistence available and its limits

- Native Pi receipts: `piruntime/receipts.go` provides private bounded JSON,
  atomic rename, file fsync and parent-directory fsync; newly created ancestors
  are also synced. Helpers are internal to piruntime. `receiptEngine` has one
  supervisor writer and is not a portal work queue.
- `piquestions.StateFile` supplies strict bounded JSON, private directories/files,
  interruptible flock and atomic synced publication. Its public Path explicitly
  permits only question and Plan names/kinds, so it cannot host queue records
  unchanged. Question/Plan stores demonstrate durable pending/handoff ownership.
- SQLite is already supported/pinned (`modernc.org/sqlite v1.46.1`), including
  turnretry evidence. codex-web's submission database uses WAL/full sync and
  indexed exact-attempt transactions, but it is private to `codex.Client`, native
  Codex receipt/queue semantics and its JSON migration fences. No public generic
  backend-neutral queue store was found in the bounded files/imports.
- Adding queue files to the existing Pi member root is incompatible with the
  current retained inspector's explicit artifact whitelist. The native
  `submissions` directory is likewise schema-1 receipts only, not an extensible
  queue namespace (`retained_conversation_inspection.go`, `receipt_owner.go`).
- Upload `Backend.Prepare` already freezes original text, ordered file IDs and
  prepared wire text under scope/kind/attempt. Repetition recovers the same wire;
  changed text/files conflict. Pending records pin files against collection and
  deletion. Queue admission/recovery must preserve this ownership; browser draft
  metadata alone is insufficient. Terminal cleanup needs an explicit owner.

## Immediate consumers and retained compatibility

- dev-workspace pins codex-web 3209aa7b consistently in flake.nix/lock and
  portal/go.mod. Packaged assets and Go API must advance together if changed.
- Consumers of neutral sends include portal browser Pi admission,
  `teamruntime.PiDelivery` and initial assignment, web Pi team/publication,
  communication delivery, questions/Plan handoffs, and monitor utilities.
  Team delivery checks exact Pending/Accepted shapes; member publication requires
  native Accepted evidence. Utilities retain a separate schema-2 owner. A portal
  queue acknowledgement must not become Accepted for these direct consumers.
- codex-web also supports legacy `NewHandler`/Client integrations, `mountConversation`,
  custom clients/durable senders and its standalone example. Existing Queue means
  native Codex queued work, can execute when loaded, and has independent
  deletion/start/reconciliation semantics. It is not an alias for a Pi inbox.
- Pi `inputDelivery` stores schema-1 receipts with action context
  `pi-delivery-v1:steer` or `:followUp`. A missing receipt on retry:true remains
  Unknown. Existing same-ID receipt enquiries never enqueue, including terminal
  NotSubmitted. Prepared/dispatching without the exact live owner becomes Unknown
  after replacement; restart never replays saved native intent.
- Receipt identity binds stable conversation, original exact-spelling ID, immutable
  message/action/settings digest. Generation is evidence, not a dedup namespace.
  Both compact 32-hex and hyphenated lowercase IDs are supported and distinct.
  `SendRequest` carries no settings object; the adapter currently uses retained
  conversation settings. Durable selection and pre-dispatch recheck need an
  explicit settled contract to prevent a queued send silently adopting changes.
- CURRENT retained worker package controls `piInputDelivery:1` and native RPCs.
  Installing a portal does not upgrade workers. `SendRequest.Delivery` is omitted
  when empty to preserve exact legacy strict JSON envelopes; arbitrary new
  non-omitted fields break retained readers. Original init/snapshot/send replies,
  receipt schemas, native witness and forward-recovery fences remain supported.

## Minimal test boundaries for the eventual implementation

1. Shared HTTP/browser: explicit durable queue state never becomes Sent; original
   ID/mode/files survive response loss and reload; distinct targets stay isolated;
   native Pending and Unknown semantics and legacy successful sends stay unchanged.
   Keep legacy external embedding and exact send-wire tests.
2. Portal browser: actual hydrated composer saves/clears drafts truthfully, displays
   queued/sent/actionable terminal failure, preserves edited drafts and scoped late
   replies, and hands ownership to the server before tab closure. Existing
   composer_handoff, message_delivery and submission_notice contracts are relevant.
3. Persistence/recovery: repeat same ID produces one admission; changed payload,
   settings or mode conflicts; fsync/write failures never acknowledge durability;
   restart before dispatch resumes safe work, while restart around/after dispatch
   only reconciles native evidence and never replays ambiguity. Retained strict
   worker and native receipt crash-boundary fixtures must remain green.
4. Admission/effects: local authorization/incarnation/target/files/mode checks before
   queue receipt; current host/lifecycle/roster/access/settings/worker proof before
   effect; changed scope fails without dispatch or retargeting. Exercise upload
   retention and settings changes while waiting, same-ID recovery and background
   fairness with disposable state. Performance measurement belongs to the broader
   verification brief; no timing claim is made by this inventory.

Existing focused anchors: codex-web `test/conversation_browser_contract_test.cjs`,
`test/delivery_retry_browser_contract_test.cjs`, `conversation/backend_external_test.go`,
`legacy_external_test.go`, `queue_compat_test.go`, `send_delivery_test.go`;
dev-workspace `piruntime/input_delivery_test.go` (including strict 283 wire),
`receipts_test.go`, `receipt_lineage_test.go`, web `pi_message_verify_test.go`,
`submission_loss_test.go`, `composer_handoff_contract_test.cjs` and
`message_delivery_browser_test.cjs`.

Owning references: codex-web docs/reference.md (browser and backend adapters),
docs/submission-storage.md; dev-workspace docs/pi-runtime.md (input acceptance,
native modes and recovery), docs/workspace-portal.md (composer), and
portal/internal/agentbackend/README.md. No permanent docs need changing for this
read-only inventory. Architect owns design and lead owns package acceptance.
