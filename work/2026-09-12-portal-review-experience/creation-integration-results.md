# Packaged creation acceptance

Creation, exact plan recovery, and old/new package compatibility passed with
exactly four isolated fixture threads. Passive observation of a real blocking
question passed; submitting its answer and retaining its closed waiting time
remain unverified because the browser harness lost its interactive connection.
The private fixture and all its processes have been removed. Exact package,
receipt, thread and cleanup identities are in
[creation-integration-results.json](creation-integration-results.json).

| Operation | HTTP response | Response time | Browser navigation | Shell GET |
| --- | --- | --- | --- | --- |
| New session | 303 | 14.8 ms | 300 ms | 2.1 ms |
| Fork | 202 | 42.7 ms | 255 ms | 2.8 ms |
| Plan into new session | 202 | 12.6 ms | 239 ms | 1.9 ms |

The real CLI remained behind the fixture delay gate during navigation and shell
checks. The new shell showed five status polls and an advancing elapsed counter.
Matching duplicates reused receipts; conflicting requests and mutations against
initializing sessions were rejected. The initial request appeared once. The fork
preserved source history without submitting another initial turn.

The source produced a completed plan, then a different plan after acceptance.
Graceful portal restart left the accepted destination paused until explicit
browser retry. Wrong receipt and stale-attempt retries failed. The exact earlier
plan text, turn, hash, model and effort survived.

This run found a goal-normalization defect: the frozen goal ended in a newline
that the CLI stripped, so the portal rejected otherwise valid completion
evidence. After the reviewed `d3bfd0f` fix, package
`prpvck3v35xbvyz60gfwprz9p3lsagal` reconciled the same deployed receipt and completed
thread. Its receipt ID, attempt 2, raw frozen request, binding and evidence stayed
unchanged. Reconciliation invoked no CLI, submitted no duplicate initial message,
and allocated no thread. The plan's single model turn completed in 2.922 seconds.

The previous package `aamx7bqmg406w3zrfnvpd60knhrgps4s` read all three completed
sessions and validated their manifests. Replaying the original source preserved
its thread and single initial request. While a fourth head request was paused
before CLI binding, the previous package independently created that destination
with a different goal. Rollforward retained the earlier receipt as `conflict`,
exposed the canonical conversation and composer, rejected retry, and created no
receipt completion proof. Existing manifests, receipts and thread identities
survived the package changes.

The first question request encountered stale Plan metadata after fixture client
reconnect and completed with a Plan-mode-required refusal. Ordinary
default-to-plan settings preceded the one authorized retry. Separate observer
resume probes produced no settings-change notification, which does not prove
that every in-memory setting remained unchanged. No production settings behavior
was changed for this test.

The retry produced the requested real blocking two-choice question. Before any
source navigation, two activity snapshots three seconds apart passed assertions
that waiting grew by at least 2.5 seconds and working time changed by at most one
second. Exact snapshot values were lost when Selenium retained a form replaced
after choosing Alpha and failed before Submit. The harness now resolves each
action in the current DOM and saves the snapshot checkpoint first. These artifact
fixes were syntax-checked but were not validated by another question turn.
After reconnect, the exact turn remained waiting but the portal had no pending
interactive request. The answer and closed-wait subchecks are unverified; the
separate controlled browser results remain in
[conversation-browser-verification.md](conversation-browser-verification.md).
The exact stranded fixture turn was interrupted through the ordinary portal API
before the independent rollback checks. No third question was sent.

Two environment limitations required bounded diagnosis. The shared authenticated
Codex home held 2,365 persisted threads; a missing-directory filtered lookup
exceeded the CLI's 60-second timeout before allocation. Exact read-only metadata
queries proved no fixture thread existed. The same receipt then used a clean
private metadata home and owned App Server; the identical filtered lookup took
3.9 ms. Authentication and configuration were private symlinks, with no credential
contents copied or printed. The source's first turn was interrupted after 141 ms
while its native client and App Server homes differed. After consistent fixture
home setup and native reconnect, one separate diagnostic completed and the
original model/effort were restored through ordinary settings. The first source
turn is not counted as a successful model response.

A preflight harness expectation also changed from 409 to the documented
canonical-route 404 before any thread allocation; the legacy fork route retained
its expected 409. Every uncertain allocation was inspected before the same
receipt resumed. The four-thread budget was preserved across all checkpoints.

Cleanup verified all four owned threads were inactive and the private metadata
database contained exactly those IDs. It stopped the four dedicated tmux sessions
and the exact owned App Server, verified no fixture process remained, then removed
the private metadata home, workspace, sockets, TLS, raw logs and screenshots.
Authentication symlink targets, shared services and registered sessions were
untouched.
