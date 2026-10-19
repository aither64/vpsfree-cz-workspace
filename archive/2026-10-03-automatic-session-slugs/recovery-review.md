# Related independent review

Reported 2026-10-03T20:51:57.781Z

Team assignment from reviewer0 to lead:

Important — general + risk/compatibility — return the snapshot whose admission and persistence were checked.
Repository/commit: dev-workspace 473e045567f0ce090d6a81928865fc4f0c8aec75.
Primary location: portal/internal/web/preparation.go:128-132.
Related: preparation.go:60-83,144-154; static/preparation.js:10-14,96-104,154-165.

confirmPreparationStatus checks confirmation and rejects accepting intents under the transition/upload/operation locks, but releases all locks before preparationRoute calls preparationStatus to read a new snapshot. The second read can therefore acknowledge a record never covered by that check.

Concrete supported interleaving:
1. A recovery GET reaches confirmPreparationStatus while its request is absent; the function returns nil.
2. Before GET takes the second snapshot, a delayed or duplicate identical POST acquires the released locks, publishes an accepting intent, fails the post-rename directory sync, and returns the bound503 without claiming uploads or dispatching a worker.
3. GET now reads that accepting/unconfirmed record and returns HTTP200 with a valid requestId/receiptId/attempt/URL.
4. The shipped browser accepts that shape, deletes the frozen draft/body and upload selection pointers, and navigates to the preparation URL. Further GETs correctly return the bound503 for accepting, including after the sync is healthy, but the browser has discarded the exact body needed to finish admission. The preparation page cannot perform its repair. Collection or restart intervention may eventually recover it; the promised immediate same-process recovery is lost.

This is a source-established concurrency failure, not a claim of an executed server race or observed disk data loss. I separately ran the shipped browser helper with pure in-memory storage/fetch to confirm the consumer consequence: a200 accepting record was accepted, clearAccepted returned its preparation URL, and frozenBodyRetained was false. No actual browser/server/VM/Codex launch occurred.

Required bounded correction: capture existence, the immutable record and its work projection under the same locks as confirmation and acceptance classification, then derive the response from that checked snapshot. Do not re-read newer preparation state after releasing the gate. Preserve the current bound503, exact replay and dispatch contracts; no new journal or cancellation framework is needed. Add a deterministic GET-versus-admission regression with real post-rename failure. It must produce only404 for the checked absence, bound503 for an unaccepted/unconfirmed intent, or acceptance from a confirmed snapshot, and must retain the browser body needed to repair the intent. Returning a coherent older confirmed status during a concurrent update is sufficient.

No additional Blocking or Advisory findings identified. No further architecture/repetition or scope/proportionality findings supported by a concrete scenario.

R1/R2 disposition:
- R1's original single-process published-running/no-worker failure is repaired for the sequential and concurrent replay paths covered by the new tests. Private bookkeeping preserves one pending dispatch per request/attempt, does not redispatch a stopped worker on confirmation, exposes explicit retry using the saved base/reservation, and recovers a published retry attempt without another increment. Catalog claim confirmation and collector retention address the adjacent durability boundary; mapping confirmation now gates receipt retirement. R1 is not fully closed because the GET snapshot race above bypasses its acceptance gate.
- R2 is resolved in source by the accepted separate-request alternative. Recovery remains primary; the original immutable body/settings/scope/selection are retained, the link uses target=_blank with noopener/noreferrer and no prompt URL, and the user deliberately copies text and reattaches files. A fresh tab creates its own ID/scope/current settings without submitting or adopting old uploads; a restored attempted draft is preserved. The pure tests and prepared browser cases distinguish stale rejection from ambiguous old acceptance. Actual Chromium evidence remains pending.

Related review scope:
Retained independent reviewer0, saved read_only/gpt-6.1-sol/xhigh, unchanged, no fallback or nested reviewers. Session identity and live retained purpose/settings match the thread binding. Reviewed all four assigned lanes directly at high overall risk for the recovery changes and exact consumers. Read recovery-review-packet.md fully, applicable workspace/repository instructions/procedures, mandatory skill and all four references, documentation placement rules, accepted remediation design, changed source/tests/docs and relevant adjacent code.
Providerca0f3bc9 and its original helper boundary are unchanged; I carried forward pass1 conclusions without repeating unaffected provider lanes. No source/records/refs/pins written; no deployment, merge or lifecycle operations.

Independent exact-source checks:
- All current final.diff and incoming.diff artifacts are byte-identical to actual git diff. recovery-final.diff is exactly edcfc18-to0ed3237.
- Final runtime tree is e38e2be96608c43dedc76fbd4e8cecdfe57d9903, matching the packet's checked tree.
- End-of-review worktrees/indexes are clean and heads match:
  codex-web ca0f3bc980ca99454d000761aeee37b4b9bbafc3;
  dev-workspace 0ed3237557d1cac494b39234c1a0ae455fb6cee6;
  vpsfree-dev-workspace d297d8c3b39c973c194e40e1a91fff40a1b4b1d0;
  workspace fe9b2ccb0178f15ecbe05dfb0a33fd7ada53597a.
- Whole lock-node comparison: runtime changes only codex-web; extension changes only codex-web/dev-workspace; workspace changes only codex-web/dev-workspace/vpsfree-dev-workspace. All exact pins match these heads, all unrelated nodes equal incoming baselines.
- Full runtime-contract JSON is byte-identical to deployed4ef, not only its schema/policy numbers.
- Adapter range-diff differs only in the documentation hunk's surrounding context after consolidation; its implementation patch remains unchanged. Dependency patch is byte-identical. Extension/workspace each contain one exact consumer pin update.
- Read the parent's quick logs: Go25top-level passes,0skips/failures, including the new admission/retry/stopped-worker/mapping/generation/catalog/actual-file collector groups; Ruby16runs223assertions, extension2runs149assertions and workspace4runs19assertions all pass with0failures/errors/skips. These logs do not cover the new GET interleaving or prove actual browser/binary behavior.

Architecture/scope conclusion:
The confirmation and dispatch maps are bounded private state attached to the existing preparation owner; they add no independent scheduler or persisted version. The fixed request-bound503 has an actual browser consumer. The separate-tab continuation uses an ordinary link and the existing copy helper, preserving the chosen immutable-identity boundary. These mechanisms respond to concrete recovery failures and fit their component owners. Owning runtime documentation explains lasting semantics; individual source/results/rollout records remain in the session. No generalized rejection ledger, cancellation system, hostile-operator defense framework, or arbitrary-root relocation promise was added.

Explicit complete history conclusion:
Assessed the actual complete remote-default-to-head inventories (20commits including unchanged provider, preserved deployed ancestry and inherited workspace coordination history), with incoming feature diffs separated from those ancestors. Runtime's five incoming units are802b3db uploads,473e045 backend,abed217 adapter,2bf6d5e dependency and0ed3237 frontend. The remediations and their tests/docs are folded into their owning units; temporary50f1d0a/d5527ac/3e9fa3b recovery fixups and prior pass1 feature heads are absent from the final series. No obsolete unapplied approach, unused transitional shim or repeated consumer pin update remains. Commit splits are coherent and independently reviewable.
Runtime4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 and extension5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12/101d31264fb54cc39b2d0d9519a202d0705a7078/f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2/399c33023a568a8d7a21e4e4df52829628720a28 remain exact deployed/published externally consumed lineage. Workspace's seven inherited coordination commits through sharedmasterad539340 belong to their respective owners; only the final pin is this feature's incoming workspace change. Their preservation is appropriate.

Explicit migration/provenance conclusion:
No incoming database migrations or namespace/state-root conversions in any affected repository; no transitional unapplied migrations remain. Preparation schema1 is introduced directly, receipt1/2/3, catalog1, authority/journal/manifest formats stay supported, and recovery bookkeeping is in-memory only. The inherited policy2-to3 and extension storage/bootstrap/preserving-seed behavior remain already-consumed lineage, not migration steps from abandoned automatic-slug versions. Migration lineage is sound on reviewed source/provenance; no new deployed migration version was claimed.
The private confirmation changes alter neither namespace/host paths/rewrite inventory nor the unchanged authority contract. The source-based “no new host-migration VM trigger” conclusion remains valid. Normal host-path/migration checks still apply; no VM evidence or arbitrary-root relocation guarantee is inferred. Forward-only recovery via a newer user-profile package retaining required readers remains the supported deployment contract.

Remaining gates:
1. Fix or explicitly reconcile the Important GET snapshot finding and verify the targeted concurrency/body-retention regression. A narrow checked-snapshot correction can be directly verified under mandatory-review step9; another full review is not required merely to confirm that narrow correction. If its design/public contract expands, reuse this reviewer for affected lanes.
2. Parent owns complete packaged checks, race regressions, real Chromium no-opener/old-recovery acceptance, exact old-source compatibility fixture, assembled candidate validation and retained canaries.
3. Exact unchanged Codex0.160.0 binary/model action/question/clock isolation, active-provider response-loss cancellation and no persisted utility thread/goal/memory effects remain required before naming enablement. Mock/schema/compile/normalCI evidence is not that proof.
4. No full workspace package/VM or post-remediation deployment success is claimed. No default-branch integration or lifecycle authorization follows from this review.

Phase: related mandatory review complete with one Important finding. Completed: R1/R2 assessment, all affected lanes, cleaned complete history/provenance and exact consumer checks. Remaining: snapshot fix/reconciliation and release gates. Next action belongs to coordinator; I remain available and idle with the session open.

Stable URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
