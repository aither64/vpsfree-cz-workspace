# Committed R1 repair for affected final review

**Local committed repair complete; publication held.** Reviewer's Important R1
is implemented and quick/race-checked. The lead assigns the retained reviewer to
affected general, architecture and risk/compatibility lanes before publication.
No independent review, native/provider acceptance, consumer update, build,
activation, claim, integration or lifecycle action is claimed here.

## Exact source and history

Repository: `git@github.com:aither64/codex-web.git`.
Feature: `refs/heads/2026-10-24-workspace-session-ui`.
Worktree: `worktrees/2026-10-24-workspace-session-ui/codex-web`.

- Full review base `8b60554bc10c2a6bcbf9732a8b77ad959c317036`.
- Previously reviewed/published head `975746f40fe99c77689ede064197772e2cc25c18`.
- **Final local head `d0fe57bed9022db526fbe90836a8576dc4e92950`.**
- **Final tree `5e232c202077efd4c75d602abca28da12ac167d1`.**
- Four logical units, with no fixup or obsolete repair iteration in the series:
  `643898a4` source retry/proof import; `c1253607` prompted/shared runner and R1;
  `c1a17310` exact capacity classifier; `d0fe57be` disposable state-upgrade fixture.
- Source801099102ef9af4a82c1f3853c53d6b442ecd4dc -> import643898a4 remains exactly
  stable-patch equivalent (`3922626df4b8d48127ebd5889187ef56d44f0a7c`). Import643
  itself is unchanged. Source801 remains imported content, not a literal ancestor.
- Capacity/state-unit stable patch IDs equal their previously reviewed versions.
  R1 is folded into its owning second shared-runner unit, with its rationale in
  the normal temporary-file commit message. Normal Nix commit/rebase and hooks
  were used; no declared framework/active ordinary hooks and no bypass.
- Old975 is retained at
  `refs/heads/2026-10-24-workspace-session-ui-reviewed-975746f4`; old receipts,
  source/intake and reviewed ranges remain unchanged. The temporary repair
  commit6266aa8 is absent from final history. Its tree equals the final tree.

[Complete four-unit history](final-history.txt),
[whole-branch final diff](final-base-to-head.diff),
[narrow five-path diff versus975](repair-versus-reviewed975.diff),
[old/new range-diff](reviewed-to-final-range-diff.txt), and
[history/migration/preservation inventory](history-migration-preservation.json)
are the review inputs. The full branch changes15paths; the direct repair changes
only `codex/client.go`, `ephemeral.go`, `ephemeral_retry_test.go`, new
`ephemeral_teardown_test.go` and `docs/reference.md`.

## Correction and necessary internal boundary

One lock-held evidence validator now runs before both live and buffered
prior-error shortcuts. It validates exact identities, turn status/error/items
and async/question metadata even after failure. Contradiction, malformed or
interactive evidence permanently revokes the call's candidate. A bounded
semantic digest retains equivalent validated duplicate failed completions;
consumed status/error/item evidence matters, while JSON ordering, optional-null
equivalents and unrelated timestamps do not. Changed transient errors differ.
Consistent final-item duplicates remain valid; native non-agent items do not
become a new tool-isolation violation. Native preterminal willRetry stays on its
existing turn. No category exposes remote diagnostics.

The reviewed975 client.go was byte-identical to8b605. Its new
[intentional internal delta](client-boundary.diff) publishes one exact private
connection/generation/done record before reader launch, closes done on every
reader exit, and factors existing disconnect bookkeeping for reuse. The private
helper atomically detaches only the matching active generation; unexpected
pre-cutoff disconnect still fails the sink. CloseNow and reader joining occur
outside locks within the original cleanup context. Only after that reader exits
does the wrapper sample final failure/success/retry eligibility. Missing reader
after launch, mismatch, cleanup/shutdown failure or timeout supplies no proof;
the separate never-connected typed transient dial case remains supported.

The public Close body is byte-identical to baseline; ordinary reconnect policy
and disconnect/pending/settings behavior are retained. No new public API/option,
retry token, broad closing-error suppression, scheduler, reconnect, detached
cleanup task or timeout was introduced. This necessary reader-lifetime change
requires the affected independent review; it is not being closed under an
original-sink-only review assumption.

Strict0.163 and prompted raw0.164 support, catalogs, fixed restrictions and the
user's no-custom-Codex-patch decision are unchanged. The lead completed the new
reference-paragraph writing pass; final reference SHA256
`7ea84d328f1c7a7298003efd5035bfe77611d30aa9f9ca262cf46a2dffdad3fc`.

## Verification and tested-tree identity

Fresh catalog-bound Luna/low/full_access watcher, parentouter9329,
thread01a1745c-7025-7941-a4ae-c68e30906505, settled exit0 with no operation left.
Declared Nix environment, Go1.26.7, GCC15.2 wrapper, CGO1 and owned short
`/tmp/cw.vQ3o9M` were retained. CODEX_WEB_TEST_BINARY was absent.

- Protocol request-corpus coverage passed.
- Full untagged `go test -mod=readonly ./...`: exit0,33s wall;
  983 executed passing leaf cases, six opt-in skips, no failure events.
- Tagged codex_integration **compile only**, run `^$`: exit0,7s wall;
  no tagged/native test executed.
- Focused `-race`: all ephemeral/prompted plus ordinary disconnect/generation/
  cancelled-write controls; exit0,89s wall including instrumented compilation,
  Go15.281s,287 passing leaf cases and no failure events.

[Stage summary](final-verification-summary.json), original final-* logs/exits,
and [original watcher result](final-watcher-result.md) remain intact. That watcher
report contains a runner-hash transcription typo. Canonical runner/launch guard
SHA256 is `02f134c896d11f83a567c04d41a3d3b9ae46666d467529c6ff4c09fff104ab27`;
the parent independently rechecked it and all successful stage receipts.
The exact passing137-file manifest is
`a4e0b900d9fcb83f225b08248db57c21052963e5110e1438ba4343b7dc3b2a43`,
verified before and after the batch.

[Committed tested-tree proof](committed-tested-tree.json) independently binds
all137paths, Git modes/blobs, reconstructed blob hashes, bytes, lengths and
SHA256 to that passing manifest and clean worktree, with complete exact inventory
and no extras. No source content changed during consolidation and no passed test
was repeated merely for the history fold. Final own-range whitespace passed.

Deterministic tests cover both APIs and direct/pre-bind replay, changed permanent
and transient errors, malformed status/error/items, late starts, standalone and
embedded async/questions, conflicting final evidence, equivalent duplicate
failures and consistent final-item duplicates. Every public call issues one
start, with no fresh call on revoked proof or foreign interrupt. Bound/settled
cases assert no redundant interrupt; an early failure without acknowledged start
retains only its original exact-owned interruption authority. Paused real-Read
fixtures use channel gates to prove already-read contradiction/question handling
finishes before final proof; timeout/mismatch/missing-reader/pre-cutoff disconnect
and unchanged public Close controls are covered. Late success evidence cannot
mint retry proof or preserve a revoked answer.

## Preservation and remaining gates

**No new migrations, schema rewrites or pin streams.** Existing deployed8b605/963
SQLite submission/admission, writers/readers and supported migration lineage are
preserved; protected module/flake/storage/turn-state/queue/send blobs and unchanged
public Close bytes are recorded in the preservation inventory. client.go's former
whole-file equality is explicitly historical, with only the new narrow internal
boundary changed. Native SQL/state acceptance remains a separate post-review
gate; no mixed-writer, downgrade or old-reader runtime guarantee is inferred.

[Updated complete source/input graph](final-source-input-graph.json) retains raw
native/source/stock patch/catalog provenance and original source/intake receipts.
No native/catalog/module/flake dependency changes occurred. Local derived future
Go pseudo-version is `v0.0.0-20261025184548-d0fe57bed902`; it is **unpublished** and
its module checksum is unresolved. The old975 checksum remains old-source
history; consumers must not select this head before review/publication release.

Other reviewed runtimeb241/config06351/workspace7c3 heads remain frozen. Parent
owns the same-reviewer affected final review and publication disposition, then
coherent consumer refresh. Original combined report and unaffected conclusions
remain authoritative in their own scope. No push, downstream source change,
default integration, native/provider campaign, final build, live capture,
claim/activation or lifecycle action was performed by this repair package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
