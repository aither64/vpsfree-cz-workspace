# Committed native version-probe fixture correction

**Quick-checked and committed; independent affected review pending. Publication held.**
Implementer0 changed only the two assigned tagged test files. No native Codex,
provider, final build, consumer refresh, publication, default integration, live
claim/activation, cleanup or lifecycle operation was performed.

## Exact source and history

- Repository `git@github.com:aither64/codex-web.git`.
- Feature `refs/heads/2026-10-24-workspace-session-ui`.
- Worktree `worktrees/2026-10-24-workspace-session-ui/codex-web`.
- Complete feature base `8b60554bc10c2a6bcbf9732a8b77ad959c317036`.
- Reviewed/published predecessor `d0fe57bed9022db526fbe90836a8576dc4e92950`.
- **Final local head `8e36734a5a5157e21f5719b2e52d6ba4686ec8d5`; tree `459962e198d4ecdab9fd75b299c8850ff3ce2e48`.**
- Clean worktree and index. Fresh ordinary SSH fetch/remote check before
  consolidation confirmed master8b605 and published featured0 unchanged.
  No push occurred; the remote still selects the reviewed predecessor.
- Preserved old ref `refs/heads/2026-10-24-workspace-session-ui-reviewed-d0fe57be`.

The final full series contains exactly four logical units:

1. `643898a4e010269ce8ea3f6b730eb0a7288f9e93`: exact source801 retry/proof import.
2. `ccd2ce581b5bccb0ced7f38141d9db254704662c`: prompted/shared runner and retained R1;
   shared test-only version probe and deterministic cases folded into this unit.
3. `ab60a81b90cb26b1d9e617d1f93573f5ada3d4b9`: unchanged exact capacity-classifier patch.
4. `8e36734a5a5157e21f5719b2e52d6ba4686ec8d5`: state-upgrade fixture, using that probe for both native versions.

Source801->643 stable patch ID remains
`3922626df4b8d48127ebd5889187ef56d44f0a7c`;643 is literally unchanged.
Source801 is imported content, not a literal ancestor. Capacity stable patch ID
remains `836c5d597bdc22859087814c5f7e1c5744dbb601`. Only the two fixture-owning
units change content. No fixup, obsolete repair iteration or superseded pin is in
the final four-unit series. Normal temporary-file messages and declared Nix Git
were used, without hook bypass. No hook framework or active ordinary hook exists.
The recorded initial consolidation launch path error occurred before any Git
mutation; the corrected absolute script then completed successfully, without
source changes or repeated tests.

[Full history](final-history.txt), [whole-branch diff](final-base-to-head.diff),
[narrow diff versusd0](repair-versus-d0.diff), [old/new range-diff](old-new-range-diff.txt),
[consolidation receipt](consolidation-receipt.json) and
[complete history/migration/preservation inventory](history-migration-preservation.json)
are the review inputs. The whole branch still changes15paths; this correction
changes exactly `codex/ephemeral_integration_test.go` and
`codex/native_upgrade_integration_test.go` (142 insertions,8 deletions).

## Bounded correction

The old version checks merged successful native stdout with startup-warning
stderr. One shared **test-only** probe now drains and captures the streams
separately. It requires successful exit and the exact expected stdout under the
existing `strings.TrimSpace` convention. Stdout retains at most1024bytes and any
overflow fails; it never searches for a version within other output. Stderr
retains the existing8KiB tail and explicitly reports truncation. Each real call
logs expected version, stdout, overflow, exit status, stderr tail and truncation,
including warnings on success. Nonzero exit, deadline failure, wrong/empty/extra
stdout and stdout overflow remain failures.

The two original commands keep exact binary/hash checks, arguments, context,
working directory and child environment. Native home/TMPDIR/helper aliases,
namespace/network/control, provider/tool observations, state and persistence
assertions are untouched. Stage05 has no version probe and is unchanged. No
other CombinedOutput call is altered. Separating the streams establishes only
version preconditions; it does not establish that native warnings are helper-neutral
or waive a later control failure. No new project prose is needed for this
fixture parsing correction; existing compatibility/native guides remain unchanged.

## Exact quick evidence and committed tree

Parent-owned fresh Luna/low watcher outer66700 ran the guarded batch once and
settled CLI0/runner0. The earlier outer63514 ran no tests; its raw report and
[parent launch reconciliation](parent-watcher-launch-reconciliation.json) remain
preserved. Only actual stage receipts establish the following results:

- Tagged `go test -mod=readonly -tags=codex_integration ./codex -run '^$'
  -count=1 -timeout=30s -json`: exit0,7s, no executed cases.
- Same tagged package with
  `-run '^(TestEphemeralIntegrationVersionProbe|TestEphemeralIntegrationDiagnosticBounds)$'`:
  exit0,2s,24 passing test records/20 passing leaves/no failures.
- The version cases reexecute only the synthetic Go test child, for both0.163
  and0.164: exact/whitespace and successful-warning positives, wrong and empty
  stderr-only-version negatives, extra stdout, nonzero exit, stdout overflow,
  bounded/truncated stderr tail and context timeout. Existing diagnostic-bound
  controls also pass. No native Codex executable was launched.
- Before/after all137source files, inventory and flakes matched manifest
  `5bd5df9b46eefc71d961e33d23ca3ba9df59c785317b77da9c0aeaebc8180acc`.
  Runner SHA256 `e148d949ec7fa5f82ada0abc831e4e61e2e64d313b0feeab7b8f6bd8354e2858`.
- Declared Nix package environment, pinned Go1.26.7/GCC15.2/CGO1; short owned
  `/tmp/cw.vp.OE8eQe` retained with its owner receipt. No cleanup occurred.
- Gofmt and own-range whitespace pass. No passed test was repeated for folding.

[Parent canonical assessment](parent-quick-assessment.json), original quick stage
logs/exits and [frozen manifest](inputs-final.json) remain authoritative.
[Committed tested-tree proof](committed-tested-tree.json) SHA256
`cc1ae3f25ce480e0436fc13a10e425c53bb34ad61ef822ff8949cde56a760af6` reconstructs all137Git blob IDs from actual
bytes and records paths, modes, sizes, hashes and checkout/tested-byte equality.
Complete inventory matches without extras, and all137modes equald0.
[135 protected-source proof](committed-protected-source.json) establishes unchanged
modes/blobs for every other file, including all production/R1 reader/retry source,
module/flake/catalog/docs, SQLite/admission, ordinary conversation and stage05.

## Preservation and next gates

**No migrations, schema rewrites, dependency/module/catalog/native input changes
or pin streams.** Existing merged SQLite/submission and native-state lineage are
retained, without new downgrade or mixed-writer guarantees. Strict0.163 versus
prompted raw0.164 contracts and rawEA/d2af native identities remain unchanged.
The original R1 full nonnative/race receipts and independent affected-clear
report retain their original scope; the135unchanged files support their reuse.
The new test source receives its own narrow affected review.

[Full updated source/input graph](final-source-input-graph.json) SHA256
`8ce974cb6ba52145cec98a2485bd039b766f9abf9f569e09cf5229ad3deccc11` binds the new local head and retained old published-source/native/
patch/catalog/review graphs. New source is unpublished; no new module checksum,
immutable source NAR or consumer acceptance is claimed. Do not reuse thed0 module
checksum for this different source. Originald0 publication/ref/receipts and failed
native attempt01/roots remain unchanged; stages02-06 are unaccepted. Parent owns
independent review, publication and any new native attempt, without reusing the
failed attempt directory.

Workspace remains at reviewed7c3 with exactly its already prepared two pin-file
edits preserved ([proof](workspace-candidate-preserved.json)); runtime5eb and
configuration508 remain held preparation. No new downstream selection is made
until the lead resolves final native campaign/identity sequencing. The selected
new client must later propagate through coherent module/vendor/runtime and both
consumers under the parent's gates. Default integration is unapproved and the
session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
