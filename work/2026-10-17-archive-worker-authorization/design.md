# Archive worker authorization and acceptance brief

Lead owns design/implementation. Keep the production fix bounded: in run_archive,
validate the supplied operation ID, then authorize with resolved slug and ID.
Remove archive-specific authorization arguments from run_delete. Direct portal
children continue using portal service identity; workers require the exact saved
archive receipt and cgroup unit. Revive/delete cannot use archive receipts.

Add a CLI test exercising actual dispatch with worker cgroups, plus receipt
matcher coverage for wrong operation/session/workspace/attempt and terminal
receipts. No new authorization token, queue, schemas or compatibility reader.

Add one dedicated NixOS VM flake check using real user services, packaged CLI,
portal HTTP/browser entrypoint, native App Server and isolated local Git origins.
No paid/model turns or production credentials. Real archive execution cannot be
stubbed. Test explicit archive and revival with dirty index/files, portal restart
after admission, interrupted worker retry, and tracking Git failure independent
of local completion. Deterministic synchronization should use existing locks and
observable journal/progress phases rather than timing guesses. Archive/create
fixtures are scoped to the VM; cleanup retains compact failure evidence.

Export the check and add a required CI job on every push/PR/manual dispatch.
Preserve fast-check partitioning so the VM is not accidentally built twice.
Document test boundaries and release acceptance. Existing lower-level recovery
tests remain useful but cannot substitute for this check.

No public API, CLI or persistent-format changes; backward/forward journal and
snapshot readers unchanged. Old packages still contain the dispatch defect, so
deployment recovery is forward-only. Runtime pin changes stay mechanical, one
final update per stream. Build outside machine claims, activate through the
coordinator with matching runtime/host selection, retain reservation during
review. No host-fleet coordination or database migrations.

Acceptance: failing positive regression on old dispatch; focused Ruby/Go and
syntax checks; independent final review of committed complete series before long
VM/package checks; exact deployed package disposable archive/revive; normal
Retry of the reported receipt. Local archive success and pending Git status
remain distinct. Default-branch integration needs separate explicit direction.
