# Reliable message delivery

The lead owns this design and implementation in the threadless initiative.
Scope is dev-workspace; codex-web already has typed not-sent and uncertain-send
errors and the durable submission ledger required by this change.

## Delivery and authority

Explicit sends retain the existing package/runtime/conversation/per-thread locks,
authorization, exact submission IDs and generic receipt reconciliation. Automatic
continuation cancellation is saved before a new dispatch. A possibly submitted
automatic attempt must be reconciled before conflicting work; its receipt is never
discarded. Transcript prefix verification is removed from the synchronous manual
capture/receipt path. Its failure cannot refuse an otherwise valid explicit send.
An accepted send is acknowledged from the delivery ledger even if optional proof
advancement cannot run. Pre-send failures known to be unsubmitted use the existing
typed MessageNotSentError; ambiguous previous attempts retain unknown outcomes.

Automatic retry continues to require exact native history, settings, binding,
epoch, and receipt proof. Missing evidence holds automation and has a diagnostic
reason. No guessed binding, fabricated handled watermark, or deletion of uncertain
identities is used to admit messages.

## Evidence storage

Each existing per-thread JSON filename remains as a schema-3 identity/cutover
marker. A sibling SQLite database stores bounded state metadata, indexed snapshot
rows and deduplicated immutable settings. There is no total snapshot-count or
total evidence-byte admission limit. Individual request/settings and state-machine
metadata retain their meaningful bounds.

State reads load a bounded working set; exact admission IDs and turn proofs use
indexed lookup. Native verification retains its bounded page/time batches. Saves
atomically commit state and changes to loaded evidence, leaving other rows intact.
Copy-on-write cache metadata preserves rollback of unsuccessful proof batches.
Detached stale state cannot overwrite a newer database revision. Current APIs
retain the in-memory snapshot representation for state-machine fixtures and legacy
import, but production reads and mutation lookups do not materialize the history.

Migration holds the existing .json.lock. Save a private, fsynced original JSON
backup, atomically publish the incompatible marker, then construct and atomically
publish the complete SQLite database. A crash after the marker resumes import
from the backup under the same lock. A new empty marker can initialize its empty
database on retry. A final completion flag distinguishes interrupted conversion
from later database loss; completed stores never restore a stale JSON backup. Read-only calls never migrate. Older readers reject the marker;
new package-transition checks also refuse targets lacking the SQLite capability.
Preserve original epochs, pending automatic attempts, charges, bindings and proofs.
Source JSON backups remain recovery evidence, not an alternate writable authority.

## Interruption and diagnostics

Interruption saves cancellation before the RPC. After success, a fresh terminal
observation of the exact interrupted turn settles its handled state immediately.
If native stop has not completed, do not claim settlement; new explicit messages
still have no dependency on evidence compaction. Keep errors classified by whether
dispatch may have happened. Log bounded non-secret categories for proof failures
and show a recoverable automation hold, without publishing prompt/settings text.

## Compatibility, deployment and recovery

The runtime contract adds an exact SQLite-evidence capability while retaining the
older capability keys needed for the first supported forward upgrade. New state
requires the new reader. Existing schema-1 and schema-2 JSON remain importable;
mixed old/new writers are fenced by the cutover marker and package generation.
No Codex protocol, public send request shape or native submission ledger changes.
The feature remains on its branch pending explicit integration/deployment approval.
Rollback must use a forward-compatible package; do not delete receipts or restore
stale JSON over the database. All tests use disposable paths and sockets.

## Acceptance and verification

- Hundreds of active-turn sends and queued inputs remain admissible with native
  prefix verification unavailable, including restart and aggregate evidence >1 MiB.
- Shared settings are deduplicated; state reads and exact lookup remain bounded.
- Accepted and uncertain UUIDs preserve their original settings and dispatch count
  through retry, lost acknowledgement and restart. No replacement dispatch occurs.
- Automatic work waits for proof and resumes only with supported complete evidence.
- Confirmed interruption updates handled state without a scheduler pass.
- The HTTP/browser path distinguishes definite rejection from uncertain delivery.
- Legacy migration, interrupted migration, atomic saves, stale revisions, package
  capability refusal and lifecycle cancellation preserve unresolved work.

Run focused Go/storage/delivery and Ruby contract checks first; commit final work
and obtain mandatory independent review. Then run broad Go/Ruby/browser and relevant
native integration checks through a fresh Luna/low watcher. Diagnose failures
before rerunning. Publish the reviewed feature branch without integrating master.

## November 8 queue recovery and baseline refresh

The user explicitly requested resolving the queue and improving the process.
Coordinator logs identify MachineSource.local_revision refusing the 933490-byte
configuration packed-refs file against the 262144-byte command/request buffer limit. Of 4346 refs,
3422 are archive retention refs; do not delete legitimate retention metadata.
Replace aggregate loading with a streamed exact-ref lookup, bounding each chunk
to the required line length and ignoring unrelated oversized records. Preserve
loose-ref precedence and the existing exact revision recheck under admission.
No claim schema, logical identity, ownership, or recovery change is needed.
Regression: queued typed claim grants after an earlier owner releases while its
source ref is packed behind more than the former aggregate limit. Test oversized
unrelated lines and malformed/missing target refs without broad new machinery.

Cancel the stale unowned request normally, refresh the feature on current master,
retain upstream delivery diagnostics/discovery and maintenance interruption
suppression, and renew only after artifacts are ready. Refreshing the own config
branch naturally creates a loose ref readable by the installed predecessor.
No manual claim edits, reservation bypasses, retention deletion or service
interruptions. New source must preserve upstream monitor/maintenance capability
and codex-web selection. Re-review conflict integration and new queue reader;
run focused checks first and packaged verification after review.

Queue visibility: inspect existing status semantics before changing them. Do not
add a persisted diagnostic schema solely to expose this refusal. Document the
operator check for waiting-without-owner; decide a small existing-interface
improvement only if it does not add a new state machine.

## Creation fixture follow-up (November 9)

CI 42532231977 passed fast/package and archive but failed maintenance case setup
for startup-failure. Native logs prove the previous active goal's turn ended
between observation and turn/steer; same-ID replay correctly refused the changed
steer/start action. The fixture deliberately retained an active goal in the
previous case and reused its conversation without quiescing it. This is separate
from evidence admission and requires no delivery-contract change.

Bounded lead brief: after each successful maintenance case has proved active-goal
and queue preservation, pause that fixture-owned goal through its ordinary API
and await terminal native root/member turns. Keep all preservation and recovery
assertions before cleanup. Do not add retry loops, replace send IDs or change
product semantics. Failure before preservation must keep diagnostic state.
Quick checks: Nix parse, extracted Python compile, diff whitespace. Independent
review of the test-only follow-up before exact-head creation verification.
No state schema, migration, deployment contract or user-visible behavior changes.
