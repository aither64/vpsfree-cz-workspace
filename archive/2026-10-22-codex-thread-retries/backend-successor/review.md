# Backend successor: independent FINAL review

Retained reviewer0 to lead, 2026-10-24. Complete report for backend-successor/review.md; lead saves it. Reviewer remained read-only.

## Findings and disposition

Blocking: none. Important: I-B1. Advisory: none. All four assigned lanes are complete on the exact frozen sources. Lead accepted I-B1 for remediation in review-finding-I-B1.md; corrected source has not been reviewed and no waiver is inferred. Complete the bounded correction and focused step-9 verification before proceeding. Retain this reviewer if the remedy changes the assessed contract.

### I-B1 — stale activity checkpoints falsely claim exact confirmed counts

Important; general and risk/compatibility. B commit85eb687a597df116690d6481ca2ec5d4ea94f0cd.

Primary reference: portal/internal/web/turn_retry_activity.go:67. Related: portal/internal/turnretry/controller.go:306 and :310; portal/internal/web/turn_retry_activity.go:164 and :176; portal/internal/turnretry/summary.go:43. Contract: docs/turn-retry-recovery.md:201 and accepted design's summary-isolation section.

retryActivityView copies ConfirmedStarts/CountQuality from the optional checkpoint without validating PendingID/LastConfirmed continuity against the authoritative ledger. Its later overlay corrects phase/actions and missing terminal timing, but leaves count quality untouched.

Concrete supported failure: scheduled UUID P has a saved summary with confirmedStarts=0, countQuality=exact, PendingID=P, no LastConfirmed. Native accepts P and the retry ledger durably saves Pending.ResultTurn. The optional summary write then fails or the process crashes before it. The existing summary persistence-fault test constructs this state. GET can still read the previous sidecar and accepted ledger; it returns running, confirmedStarts=0, countQuality=exact, unconfirmed=0. A known incomplete count is represented as exact. Stop after receipt recovery has the same exposure if its optional checkpoint fails. A checkpoint whose unconfirmed Pending has since disappeared or changed also has a detectable continuity gap before worker repair.

Conservatively mark presentation partial/unavailable when current ledger/checkpoint identities disprove completeness, or otherwise account for independently proved receipt continuity. Keep GET read-only. Do not infer counts from Attempt/quota, write metadata during polling, or require summary success for acceptance, durable Stop, manual input or exact receipt recovery. Cover accepted-result checkpoint failure and detectable retirement gaps through the view/actual HTTP boundary, including action responses. Existing persistence tests do not assert this stale HTTP response.

Source-derived; reviewer executed no reproduction. Sent promptly in message0269bc2a-d22a-47dc-845b-e1582d4015eb. Lead accepted bounded remediation while preserving frozen85eb.

## Identity and exact scope

dev-session current printed2026-10-22-codex-thread-retries. Both environment markers were absent; trusted binding matched /home/aither/workspace/ai/vpsfree.cz. Fresh roster revision22 verified reviewer0 ready/review-purpose, gpt-6.1-sol/xhigh/read_only, thread01a162d6-4bf1-7142-bb04-7b871eb2d1af. No overrides, fallback, authored implementation or nested agents.

Read authoritative review-release.md in full and completed review-supplement.md, accepted design/plan/state and relevant prior dispositions, mandatory-change-review skill/all four full references, applicable workspace routes and both repo AGENTS. Inspected immutable production code, actual callers/provider/HTTP integration, tests, documentation, complete series/final diff inventories and provenance. Unchanged prior conclusions were retained only at their verified exact-content boundary; they do not certify this backend.

| Repo | Base | Final | Tree |
| --- | --- | --- | --- |
| A codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 | 5743f94c2fbd01b65438847d2e2bab0f01df32ae | 481e7fa06bd98f2006e6d76758bce6b7134b52bb |
| B dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 | 85eb687a597df116690d6481ca2ec5d4ea94f0cd | be3753a029d646d170c93cf1aba6cfafa6db4925 |

Local heads/trees match. Independently compared B full.diff/delta.diff byte-for-byte with Git, verified first ten commits exactly equal accepted59c history, and checked all58 hashes referenced by final.json with zero mismatches. Source metadata's complete graph equals committed flake.lock. Final/tested-tree and SSH/source/NAR receipts bind the final source. Reviewer did not rematerialize source or recompute its NAR; those are inspected owner/lead evidence, not reviewer package execution.

No file writes/tests/native/browser/builds/CI query or wait/live ledger/history/state inspection, source/ref mutations, claims, deployment/integration/release/lifecycle actions.

## General lane

Apart from I-B1, no additional correctness or verification-design finding.

The store validates schema/scope/revision, explicit choices/enrollment, duplicate/unknown/trailing data,1MiB/128-entry bounds, private ownership/modes, summary qualities and safe numbers. Reads use limit+1. Writes reload under a bounded sibling flock and atomically replace/sync a complete candidate. Identity mismatch/corrupt/full state is preserved and holds automation.

Bootstrap/preferences take separate runtime EX rather than upgrading SH. Current package/provider/lifecycle/root/runtime/tmux authority, stable roster operation, all nonremoved retained members, sorted thread order, two matching cold observations and post-inventory authority/roster checks precede one policy commit. Same-valued authorized POST preserves state/revision despite stale expected revision after a lost reply. GET does not bootstrap. Missing legacy records inherit default-on; any matching legacy opt-out disables both classes.

Explicit Decision governs scheduling, Begin and positive-never-submitted restart/reservation without rewriting legacy Enabled. Lazy new-member entries use exact managed enrollment, retaining their first eligible failure. Off/on suppression preserves chain/Pending/result identities. Disabled/unsupported result observations retain the owning tuple rather than inventing absence. Exact unknown reconciliation remains first and sidecar-independent.

Stop saves authoritative cancellation/Handled with Pending retained. Retry now only accelerates the same scheduled deadline. Tokens bind incarnation/thread/chain/revision/operation, plus Pending.ID for Retry now. Actual root aliases/member routes use A's provider. The narrow resolver reaches exact-token receipt recovery/Stop before ordinary activity-known admission, without Continue or cold activation. Normal origin/auth/authority checks remain.

Production manual capture/send/queue/plan/team and exact receipt settlement have no sidecar dependency. Actual HTTP tests exercise missing/malformed/full/unwritable metadata. Prepared-plan original-ID recovery, settings epoch/binding, generic unknown and protected retention contracts remain.

## Architecture and repetition lane

No additional finding. B owns policy/persistence/scheduling/action authority; A owns optional generic DTO/provider/validation/browser rendering. Checked actual A5743 interface and B Target/capability/provider/routes, embedded assets and Go/Nix/vendor selection. No duplicate generic receipt ledger or speculative consumer registry was added.

Sidecar RMW is a short inner checkpoint without native RPC or outer-lock acquisition. Existing order remains transition -> runtime -> roster -> conversation -> per-thread admission -> generic/native operations. Explicit class authority replaces temporary Enabled mutation.

LockRuntimeExclusiveContext delegates the existing lockRuntimeContext loop with EX and the same filename. Existing fail-fast APIs/callers stay unchanged. Real-flock tests cover SH/EX contention/release, pre-cancel, queued cancel/deadline and lock release.

Ruby's payload-agnostic presence guard composes with the legacy retry guard. Committed .json presence requires exact integer capability even for malformed/empty/oversized payloads; inspection errors refuse. Selected preparation, activation recheck and candidate self-activation use the existing guard chain. Go remains payload owner.

## Scope and proportionality lane

No additional finding. Bounded sidecar/class policy/exact actions/summary/guard/helper have accepted current consumers and concrete recovery requirements. No native CAS/protocol upgrade, generic lifecycle-lock redesign, new manual authority or global style change was introduced.

The four additive commits separate guard, lock helper and disposable evidence. The owning Go store/controller/HTTP/docs unit shares one incarnation/revision/action contract; bundling is coherent. The independent two-file accepted-fork fixture is separately reviewable/revertible. Direct inspection of the seven retained fixture diffs found only required Decision arguments/formatting, with no assertion removal or weakened count/replay/identity condition.

## Risk and compatibility lane

I-B1 is the count-honesty defect; no other new security, dispatch-authority or state-loss finding identified.

Retry ledger acceptance precedes optional summary. Summary failure cannot undo acceptance or durable Stop; before replacing accepted Pending, the controller checkpoints or holds progression. Exact settlement needs no policy. Unknown UUID/options/charge identity stays protected. Positive absence still requires explicit policy/current admission/settings proof and renewed quota reservation before dispatch.

Runtime EX serializes preferences with managed portal/team/worker participation. Two-read enable observation is the accepted boundary, not atomic native completion/file commit. Native unmanaged writers remain outside the fence; no CAS guarantee is inferred. Same-value no-op still requires current authority. Stale tokens/revisions do not grant new dispatch. Legacy boolean/tokenless POSTs require reload rather than being converted to session policy.

Guard support must ship before first production sidecar. Once any committed policy .json exists, old incapable packages must refuse selection even when state is unreadable/invalid. Preserve it and recover forward; deletion/reset is not supported downgrade.

## Actual accepted-fork evidence source

Inspected complete portal/internal/web/creation_source_lock_test.go and test/support/accepted_fork_runner.rb in b1d9e9a7. They drive actual Handler acceptance, Go initializer/command and ordinary Ruby CLI/Runner source checks, real flock, request binding, journal, completion and recovery. Synthetic adapters replace external native/provider/tmux effects; they do not fabricate Go success or replace lock/source/receipt/journal/completion logic.

Separate holder/initializer processes verify exact device/inode. Bounded socket/pipe handshakes distinguish first source EX before binding from second source EX after binding; second stage checks destination locks are released. Assertions retain202 acceptance, real EX|NB refusal, zero native effects while refused, original receipt/request/binding identity, replacement-source refusal, exactly one fork/destination after original-receipt retry, journal-bound recovery without source, duplicate/stale/wrong/restart readback. Owned processes are released/drained. Existing preacceptance409/200ms test is unchanged.

Meaningful prepared evidence, not execution proof: actual21-leaf integration remains unrun. It neither fixes product source-lock waiting nor identifies historical CI holders.

## Whole histories, update streams and lineage

A complete seven-series:
df00fa36,6c828759,c1f415ad,ac62eeeb,f8629067,55e0300b,5743f94c.

B complete fourteen-series:
7262c24e,b3c7187c,aafaf419,9ccb4b11,100108b0,9311c15a,c8c31ab5,9ce6b291,4b4da049,59c0eb55,4b98ceb2,6817bb6f,b1d9e9a7,85eb687a.

Full IDs/messages remain in lead-a-complete-series.txt/lead-complete-series.txt and owner series.txt. First ten B commits are exact accepted59c ancestors; four backend/evidence commits are additive. Complete final histories/diff scope assessed, with unchanged prior conclusions retained at that exact boundary. No obsolete unconsumed iteration, fixup stream, abandoned schema bridge or transitional migration remains. Legacy input/interface supports deployed behavior rather than a branch-only abandoned schema.

Exactly one B codex-web update remains:9ccb4b11, consistently selecting A5743 through Go module/sums, flake source/lock and vendor digest. No repeated A pin or redundant dependency/channel/generated update stream remains. Backend introduces no asset/cache/dependency churn. Complete input graph/pins are unchanged from accepted59c and metadata matches the final lock.

Independently recomputed old/new stable patch equality:

- deployed retention/ed2 ->100108b0:4850f62fbfc3bb6569f25a5a4f946bcebce73a7f;
- deployed Incident2 prepared plan ->9311c15a:cbc1224fe9709472c635142d9ac1f772583697a9;
- deployed bounded runtime wait ->c8c31ab5:4bd691213eac0f4b2b9c561c41600cbe5490520c.

Preserved deployed7b8c is a nonancestor of final85eb, independently confirmed. Identical retained patches plus exact refs/bundles/rollout receipts establish supported lineage; they do not make7b8c literally merged or this substantive backend deployed-equivalent. This successor needs verification/deployment. W/C selection/composition/default integration are outside review.

## Migrations and persisted-state provenance

No database migrations, intermediate policy migrations, conversion/reset or old-format rewrites. Deployed retry schema1, generic submission schema3 and MaxSnapshots64 validation remain. Native/protocol/roster/browser-attempt/dismissal identities are unchanged.

Policy introduces final dedicated schema1 directly:1MiB/128 entries, exact canonical workspace/slug/root/retained ObservationIdentity. Sharing schema number1 does not make it a migration of the retry record. Per packet this backend is not deployed/released and no production sidecar/external state has been created. Disposable records do not establish supported intermediate schemas. Guard-before-creation and forward-only recovery remain required; deployed retry/submission and original receipt recovery remain supported.

## Documentation, evidence and residual gates

Lasting semantics/reasons/locks/compatibility/forward recovery belong in B docs/turn-retry-recovery.md and docs/workspace-portal.md, discoverable from README. Rollout hashes/failures/watcher preparation stay in session records. Docs state the intended count-honesty contract correctly; I-B1 is the implementation discrepancy. No unrelated documentation expansion needed.

Inspected final core normal2.186s/race9.757s; focused web14.722s/race11.231s; session contract/fail-fast0.017s and compile-only package/cmd receipts. Ruby9cases/164assertions and EX normal/race receipts bind frozen source. Compile output explicitly says no tests to run. Seven fixture reconstruction claims are owner source evidence, supported by direct diff inspection, not execution passes.

Required residuals:

1. Full final workspacecodex ^TestRetry pressure/retention/replay remains incomplete. Original45s overall timeout exit1/wall49.745s and fsync stack are retained. One stack snapshot establishes neither deadlock nor harmlessness/sidecar causation. Earlier narrow10.096s pass predates final terminal-tuple correction.
2. Corrected pressure-manifest inventories19 top-level names, including TestRetryPreparedFirstExecutionRetainsOptionsAndOldEpoch, plus14 pressure leaves. Prepared pressure-command.py guards exact85eb/clean source, unique absent output,180s Go budget, required cases/zero skips. It is unrun and must be rebound if remediation changes final head.
3. Actual accepted-fork21-leaf Handler/Ruby integration remains held for a fresh watcher.
4. Distinct creation CI9f/207/e7 failures/unobserved competing holders remain unresolved. Controlled evidence cannot explain or waive them.
5. Backend real-template interaction, applicable packaged/native checks, composed W/C graph/builds, deployment and renewed use acceptance are not certified. Prior visual/native evidence retains original scope. Actual five-second server receipt latency remains unmeasured/unattributed.

Disposition: completed source review with one Important finding accepted for remediation. Exact85eb is not unconditional no-findings approval. After saving this report, lead can release the assessed narrow correction and verify directly under step9 unless it expands the contract. Longer verification and operations remain separate. No integration/deploy/claim/release/lifecycle permission follows.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
