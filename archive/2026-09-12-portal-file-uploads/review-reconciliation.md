# Review reconciliation

Initial review: high risk, all four lanes, gpt-5.6-sol xhigh, standalone reviewers.
Exact original heads are in review-packet.md and each lane report.

- Catalog exhaustion (general/architecture Blocking; risk/scope Important): fixed
  with catalog-owned compaction. Expired empty scopes and obsolete unsent records
  are removed; sent history and fork tombstones persist while referenced. Explicit
  session deletion reclaims its associations. Completed files drop chunk hashes.
  Keep 1 MiB of the 16 MiB bound for recovery transitions. Restart tests cover
  the 10,000-scope cap and byte-cap recovery through session deletion.
- Runtime commit bundling (general Blocking): rewrote unmerged history into
  provider pin, private storage, portal input, and CLI lifecycle commits. The
  resulting final tree was checked against the pre-rewrite staged tree.
- Initial acceptance/deletion race (risk Blocking and parent finding): creation,
  draft deletion and expiry share a context-aware creation lock. Draft deletion
  reconciles accepted receipts first, including acceptance followed by failed
  catalog retention. Ordinary deletion only reclaims already obsolete blobs and
  cannot expire a different creation draft. Concurrency/partial-retention test
  proves accepted input remains available and deletion returns 409.
- Expired prepared replay (architecture Important): unaccepted/cancelled attempts
  revalidate ready records and actual files. Accepted retry wire text stays frozen.
- Terminal creation conflict (risk Important): conflict receipts cancel draft
  reservations and release slug binding; live receipts take precedence if an
  identical input is subsequently accepted under another slug. Tests prove that
  released drafts can be edited or removed and removed input cannot be replayed.
- Missing deletion thread (general Important): Go cleanup refuses an empty
  retired thread when ordinary scopes exist for that exact slug/epoch. Missing
  catalogs are a side-effect-free no-op. CLI tests create state through the
  real store and verify failed cleanup preserves bytes, then exact cleanup works.
- Duplicated state identity (architecture Important): Go workspace namespaces
  use internal/userstate; Ruby invokes the configured owning CLI without trying
  to discover its private catalog. CLI-only installations cannot create uploads.
  Ruby journal retry tests no longer fake a catalog path.
- Queue completion failure (all first three lanes Important): codex-web adds an
  optional completion-aware client contract using its existing durable deletion
  intent. Completion precedes ledger removal. Queue refresh only reconciles
  already absent entries; it never deletes a remaining entry. Lifecycle idle
  checks report pending deletion instead of silently completing it without the
  provider. Failure tests cover provider persistence, final ledger update,
  restart, refresh, and a submission proven to have started.

The last fix changes a public optional interface and lifecycle validation
behavior, so architecture and risk lanes will review the committed remediation.
The other direct fixes are verified with focused checks; no repeated general or
scope review is required merely to confirm their requested changes.

Accepted retention-only rollback boundary: resolve pending queue deletions
before rolling back. An older package can clear the unchanged Codex receipt
without updating the independent upload catalog. Rolling forward then retains
that file until explicit owner-session deletion; no bytes are lost or exposed.
A second provider-owned deletion journal was rejected because it would duplicate
Codex queue/history proof and expand the protocol for this exceptional rollback.

Quick verification after remediation:
- codex-web go test ./...; four Node browser contract tests: pass.
- dev-workspace portal go test -timeout 120s ./... at exact provider 39abf287:
  pass, including metadata caps, expiry/replay, conflict and deletion race tests.
- Ruby removal/fork tests: 69 tests, 622 assertions, pass.
- Go CLI checks exercise actual upload state ownership and missing thread proof.
- Nix vendor hash rebuilt with a temporary fake hash, then set to the measured
  sha256-9MB/8p3YsgyFl4ucyZ/S6W0rciro684hyKOiQT2gpzE=.
- No browser/live integration or deployment has started.


## Focused rerun outcome

Architecture and risk reruns completed at the exact v2 packet heads, using
fresh gpt-5.6-sol xhigh reviewers. Both reported the same Important issue:
GET-based queue completion bypassed mutation authority and could race queue start.
No other findings were reported. The direct remediation moves completion to
POST /queue/reconcile under the ordinary exact-origin, capability, transition,
runtime and application-mutex checks. GET no longer invokes completion. Client
queue start also shares its queue-update mutex with deletion/recovery.

The regression holds the application mutation lock, proves GET leaves the intent
untouched, proves POST resolves Mutation=true and waits for the lock, then verifies
completion and rejection without Origin. Full provider Go tests, four Node tests
and the targeted race check pass. Runtime observations additionally cannot move
cancelled or observed submissions back to queued when an earlier GET finishes
late; a focused regression covers that ordering.

This implements the exact requested narrow remediation. No additional reviewer
rerun is required by the skill. Integration may start after the direct fix is
committed, consumer pins updated, and focused consumer checks pass.


## Integration fixes

The real browser exposed two omitted pieces of the requested queue-recovery
wiring: the runtime session client did not forward reconcileQueue, and its
compatibility API did not forward POST queue/reconcile. Both now have contract
coverage using the shipped client against the actual HTTP route.

Real Codex fork/archive acceptance exposed copied initial submissions confusing
AdoptInitial. Adoption now considers only the submission scope that owns the
files; fork references remain references. A restart regression proves the source
can still adopt its original input and that a foreign session is refused.
The same fixture repeated its initial text after a native startup interruption.
Initial associations now keep their first observed item identity, preventing
repeated text from taking that association or leaving the actual send unresolved.
Tests prove arbitrary repeated text gains no attachment and confirmed deletion
works once an explicit repeated send is observed. These preserve the reviewed
ownership and receipt contracts; no state format or public API changes were added.
