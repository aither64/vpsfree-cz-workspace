# Design and verification brief

This records the implementation design after the user enabled tracking. Initial
implementation occurred under the explicit no-tracking request.

## Boundaries and invariants

The generic codex-web client owns delivery state, SQLite storage, schema-3 import,
thread-scoped export and the shared browser retry scheduler. The runtime owns
socket-derived persistent paths, package admission, plan authorization and its
browser receipt integration. Configuration and workspace pins select matching
host/application sources without changing the native protocol version.

Reserve digest, action context and turn options before dispatch. Claim under
writer admission and check cancellation again after durable admission. Failed
writer acquisition proves non-transmission. Once writing starts, retain
uncertainty until native acceptance is observed. SQLite claims prevent stale
recovery from resetting another admitted operation. Restoration failures remain
uncertain. Network I/O never occurs within a database transaction.

SQLite uses WAL, FULL synchronization and indexed scoped transactions. Atomic
schema bootstrap cannot silently recreate lost tables. Migration holds ordered
predecessor locks, records imported data and sources transactionally, preserves
private backups, publishes both predecessor fences, then marks ready. Interrupted
fence publication resumes against exact source identities. Archives export through
the client API and retain the existing held-prompt format.

Browser retries require `message_not_sent`, `notSent: true`, `retryable: true`.
Use 250 ms to five-second backoff, pause hidden/offline/busy, retain UUID/text/
attachments/options, preserve unrelated drafts, and stop on uncertainty. Admitted
plan dispatch detaches browser cancellation while retaining the operation deadline
and service shutdown cancellation. Authorization still precedes admission.

## Verification

Quick checks: full library Go suite, focused storage/deadline regressions, generic
browser contracts, portal shipped-browser harness, plan/disconnection tests,
archive export and Ruby predecessor-transition tests. Protocol coverage and Go
vet also passed during initial implementation.

Final review covers all four mandatory lanes and complete branch history across
all four repositories, including migration and repeated pin streams. Then run
packaged checks, applicable native App Server and lifecycle checks through fresh
verification utilities. Run final composed-lock validation and build the exact
profile/system candidates before deployment ownership.

After activation verify portal health, naming, conversation continuity, database
integrity and safe sending. Inspect the original attempt against current ledger
and complete native history. A targeted state repair needs the original writer
acquisition failure as pre-transmission proof; absence from history is insufficient.
Keep recovery forward-only after migration and preserve all unrelated receipts.

## Reboot recovery refinement before deployment

The runtime's legacy predecessor path is socket-adjacent under `/run`. A reboot
removes its fence and any source-adjacent backup. Keep checksum-named predecessor
backups beside the persistent SQLite database, including when only the volatile
fallback existed. After the import transaction commits, an absent source can be
reconstructed only when its retained backup matches the journal digest. Present
changed sources still fail closed.

Once the database is ready, its committed journal and records are authoritative.
Acquire the same ordered predecessor locks, validate every present fence and
the exact configured source identities, then recreate absent fences atomically.
Never overwrite an unexpected present file or reimport records after readiness.
Extract the existing ordered lock handling for initialization and validation;
avoid nested acquisition when initialization already holds those locks.

This refines the initial undeployed schema-1 implementation. It does not upgrade
an externally consumed branch schema. Add ready/imported restart tests with the
volatile directory removed, retained receipt assertions, durable backup
verification, and refusal of changed present sources or corrupted backups. Run
the affected independent review lanes before accepting the refined candidate.
