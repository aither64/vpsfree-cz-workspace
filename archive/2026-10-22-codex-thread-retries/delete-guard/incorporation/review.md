# Combined deletion guard: independent affected FINAL review

Retained reviewer0 to lead, 2026-10-24. Complete report for lead to save. Reviewer remained read-only.

## Findings and disposition

Blocking: none. Important: D1 below. Advisory: none. All four assigned lanes are complete on Bef773d223e946f1b5ca453f217a600b7e463e8b7/treef900fd6de795cfb1b3380fa61d0aa23c2b6646fd. Resolve D1 or record an explicit Important disposition before further verification. No corrected source is approved by this report.

### D1 — new deletion preflight rejects existing removed threadless members

Important; general and risk/compatibility. Commit ef773d223e946f1b5ca453f217a600b7e463e8b7. Primary: portal/internal/teamruntime/deletion.go:87. Call site: libexec/dev-session:2406. Existing producers: runtime.go:1531, :1594 and :2405.

deletionCandidates applies the new unknown-creation eligibility checks before its state switch. Every threadless member must satisfy unstarted, nonfork, canonical project, CreateAttempted=true and unbootstrapped constraints even when it is already removed.

Concrete supported cases:
- Ordinary Remove accepts a reservation whose native start was never attempted, then saves removed/RemovedAt with empty Thread and CreateAttempted=false.
- Fork copies an already-removed member, preserving its removed state/time but clearing Thread, ProjectID and attempt flags.
- A normally ready/completed session has unstarted=false.

Before this change RequireIdleAll/archive/retire skipped these terminal removed records. New mandatory prepare-delete rejects them, including force deletion. An unrelated already-removed reservation can therefore prevent deleting an otherwise valid ready or forked session.

Recognize an existing valid removed tombstone as a no-op before applying special eligibility to a creating unknown candidate. Preserve its removal time/identity; do not infer native absence or erase unknown evidence. Keep strict validation for new creating candidates. Cover ordinary unattempted-Remove and fork-inherited removed records in noncreating/ready deletion contexts, for force and nonforce, plus exact new-tombstone replay. This is a compatibility correction within the assessed deletion contract, not permission to broaden ordinary Remove/archive.

Sent promptly in message849c9d9b-9d2a-4b84-8b22-3014139e8180, confirmed same-ID retry. Source-derived; no reviewer execution.

## Identity and exact scope

dev-session current matched2026-10-22-codex-thread-retries. Both environment markers absent; trusted exact workspace/session binding matched. Roster34 verified reviewer0 ready/review-purpose, gpt-6.1-sol/xhigh/read_only, thread01a162d6-4bf1-7142-bb04-7b871eb2d1af. No overrides/fallback/nested agents.

Read authoritative delete-guard/incorporation/review-release.md, minimal/scope/quick/tested-tree/preservation/handoff/publication evidence, actual complete source delta/callers/tests/docs and accepted deletion brief in design.md. Mandatory skill/all four full lane references remain read in current context; reread lifecycle procedure/repo guidance. Retained completed5870 and prior product/I-B1/TB/service conclusions only at exact-content boundaries.

Base bf6d4b0c49600c15e17fe71248807ef43424e932 -> ef773d223e946f1b5ca453f217a600b7e463e8b7. Parent5870fcbec755f10396b7892b9f08e50335a77fe9 is exact reviewed content. Independently verified head/tree, first16 exact, complete17-series, full.diff and deletion.delta.diff byte equality with Git, exact eight changed paths, unchanged lock graph and sole A stream. Accepted patch hash matches e6ffd5fb48a27d8cb4cce596e360da6138393f0a1e543daada95fbfee1aad8b5; docs hash matches direct lead prose pass.

No source/file writes, tests/build/browser/native/CI/live-state/history inspection, claims/deployment/integration/deletion/lifecycle actions or nested agents. No optional NAR wait.

## General lane

Apart from D1, no additional finding.

The helper binds an exact operation ID/root to the live private deletion journal, expected phase/force/state/workspace/slug and retained manifest/roster. It uses full manifest validation plus presence-aware flags: missing/null initial-request flags cannot authorize the exception. It hashes/rechecks journal and manifest, then checks current roster/context again inside the atomic publication. All candidates are inventoried before mutation.

New eligibility is bounded to unstarted, nonfork direct-team creating reservations with canonical project, attempted native start, no thread, no bootstrap and no retirement intent. Published change only sets removed/RemovedAt, retaining project, attempts, identity and settings. Unknown outcome remains unknown; no native project deletion, adoption, fresh start, resume/bootstrap/send or generic cleanup is added.

Ruby check-only occurs before root quiescence. Durable thread_retiring precedes mutating helper and normal team/root retirement. A failed/uncertain publication stops further retirement, leaving a non-discardable journal. Replay after publication preserves the original tombstone time/bytes under the same context. Existing preserve_removed_state! moves complete roster to private team.json alongside recovery/creation records.

## Architecture/repetition lane

No additional finding. The internal command/service owns deletion-specific preparation and does not enter public member Remove/archive/preset routes. Reused Store operation/update locks and existing schema publication; no new outer-lock acquisition/framework. The Ruby owner retains lifecycle/generation/creation/runtime exclusions across separate calls; stateless helper does not falsely claim cross-call comparison.

The extracted requireIdleMember reproduces existing RequireIdleAll behavior and is shared by deletion preflight. Nonforce confirmed members retain idle/submission checks; force follows existing verified interruption/retirement flow. Ordinary Remove/ArchiveAll/RetireAll still refuse the new creating unknown without preparation. D1 concerns terminal records, not relaxation of those creating checks.

## Scope/proportionality lane

No additional finding. Eight paths form one coherent deletion-only unit with owning tests/docs. No retry/browser/service/pin/native API or generic lifecycle redesign entered commit17. Bounded local journal reader is justified by authoritative force/phase/presence needs; Ruby remains inventory/operation owner. Unknown native orphan cleanup is explicitly outside the guarantee.

## Risk/compatibility lane

D1 is the compatibility regression. Otherwise the new exception preserves rather than fabricates native certainty. Confirmed-thread queue/submission/retry/history retirement remains with existing owners. Project identity is retained; a fresh root derives a distinct project key. Journal/manifest/root/force/phase changes refuse before publication. Validated phase alone cannot mutate, and a partial applied operation stays deletion-owned.

Tests inspect source-level invalid-context/ineligible candidates, force change during idle proof, atomic refusal, bounded-save failure, restart before/after publication, exact replay, no unknown native effects and unchanged ordinary retirement refusal. Cross-language test executes actual Ruby delete ordering and real Go helper/confirmed-member native idle proof; known/root retirement is explicitly synthetic there. It asserts private team.json preservation. Ruby fault tests retain same operation at thread_retiring after uncertain publication. These are meaningful disposable boundaries; they are not deployed deletion proof.

## Documentation, full history, update streams and migrations

docs/dev-sessions.md explains the exception, explicit initial flags, private tombstone fields, unknown native outcome, preserved project, no adoption/bootstrap and journal recovery. Placement is appropriate in existing deletion/recovery guidance, discoverable from session docs. It does not promise native object cleanup. Lead prose pass is preserved.

Complete17-series:
7262c24e,b3c7187c,aafaf419,9ccb4b11,100108b0,9311c15a,c8c31ab5,9ce6b291,4b4da049,59c0eb55,4b98ceb2,6817bb6f,91bd8535,66d8ef32,02d33648,5870fcbe,ef773d22.
Exact first16 remain reviewed5870. Deletion is a separate logical17th commit; no unconsumed intermediate/fixup/transitional migration remains. Earlier preserved nonancestor refs/bundles/failed evidence retain their historical scope.

Sole A update9ccb4b11 still selects A5743. No repeated dependency/channel/generated update stream remains; complete graph unchanged. Prior deployed7b8c lineage remains based on verified product patches/ref/bundle receipts, not literal merge ancestry. Current W/C selections are excluded/stale for this final head and need fresh matching evidence before composition/deployment.

No database/data migrations, new schema/ledger/journal phase, conversion or reset. This uses existing roster schema1 removed+RemovedAt, which existing readers can parse, while preserving the new deletion-context meaning of unknown reservation abandonment. Retry schema1/generic3/policy1/MaxSnapshots64/native/browser identities remain unchanged. No live state consumption/deletion occurred during this review. Keep prior policy guard-before-creation/forward-recovery and ordinary lifecycle recovery obligations.

## Verification limits

Inspected owner composition quick:39 Go tests/subtests across10 topnames/3 packages, zero skips/fails; package2.558s/1.531s/0.529s. Ruby25tests/158assertions, zero failures/errors/skips; syntax/format/Node/diff receipts present. Parsed raw Go/Ruby results; reviewer ran none.

Actual combined browser32 remains unrun. Prior fork21/pressure passes retain unchanged-source scope; no repeats or package/derivation reuse inferred. Package/native/composition/deployment and any exact authorized old-target deletion remain unproved and lead-owned. Source review supplies no operational/integration permission.

Disposition: complete affected final review with one Important finding D1. Correct the bounded terminal-tombstone handling and verify focused regressions under step9 unless remedy expands the assessed contract. Retain reviewer0 for material changes.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
