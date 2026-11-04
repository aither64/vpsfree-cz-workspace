# Final affected review: request return paths at babe5142

**No new findings: 0 Blocking, 0 Important, 0 Advisory.** The assigned committed change has no unresolved review finding preventing parent disposition and subsequent verification. This is not browser, Nix, CI, integration or deployment acceptance.

## Identity and reviewed boundary

I verified dev-session current as 2026-11-01-typescript-client-migration and both environment markers matching that slug and /home/aither/workspace/ai/vpsfree.cz before reading session files. Live roster61 identifies reviewer0 as ready, review-purpose, gpt-6-astra/xhigh/read_only, thread01a19801-c630-7971-b7b9-cc178b6ced88. Settings were retained; no override, fallback or nested reviewer was used.

I read mandatory-change-review and all four references directly, current workspace/repository AGENTS, applicable guidance and the bounded design brief. Unchanged workspace Git/verification/documentation procedures were also matched to their previously read complete contents. All four lanes were performed directly. Overall branch risk remains HIGH; the new local navigation change is medium risk.

Repository: vpsfreecz/vpsadmin-webui, canonical session worktree.
- Affected range: 79980b6a6607d08cccd252439ced328a250bd5b0..babe51421bd1df61a548e7b2f047053df14ff3eb.
- Complete readiness range: 670cf286daf9bddb65594035507ca112a9e6d397..babe51421bd1df61a548e7b2f047053df14ff3eb.
- Tree: 95f01c23a06e2c385756daa61305413af24403d9.
- Ninth commit: exactly five paths, +226/-160, including normal formatting; complete range: nine ordinary commits,31 paths,+1480/-643.
- Independently observed clean worktree/index, no untracked files or operation markers.

Packet SHA256 matches861e96bd0b6f6e92ee9d9968a22738f96cda68c2ae0636ff842bc62ef67c5aad; commit-receipt SHA256 matches6043dd0a5ef5d8957c730f9c2f085e800f7783d535a07d61b2a51ae6512eb8bb. Referenced receipt/quick artifact hashes matched. Prior full/affected reviews and parent step9 dispositions remain applicable to unchanged source; this new behavior was independently reviewed.

## General: correctness and negative paths

Owning commit: babe51421bd1df61a548e7b2f047053df14ff3eb.

RequestsModel.ts:15–20 copies URLSearchParams, removes every literal q occurrence and serializes the copy with the existing path convention. It preserves other parameter values, duplicates and ordering, leaves the caller object untouched, and avoids a trailing question mark for an empty result.

RequestsPage.tsx:505 uses this helper with the existing [basePath,sp] dependencies. The resulting value continues through:
- requestDetailHref at:507–513, including the off-page asynchronous typed Show path at:555–603;
- requestReviewState and sequential review at:524–553;
- ordinary/expanded list links at:773,795.

Thus a callback that captured parameters before the URL-normalization effect still receives a return path without q. The change does not require a later browser URL effect to repair its captured value. The existing effect at:130–162, async endpoint/identity discrimination, error handling, applicant selection, queue snapshots and pagination are unchanged. The broad page diff changes formatting around those functions, not their decisions or dependency arrays.

The new regressions in RequestsModel.test.ts:25–46 cover duplicate/captured q, nonmutation, retained filter and pagination fields including duplicate user values/order, canonical queries, empty queries and q-only queries. The existing browser leaf is byte-identical. Its canonical-URL poll, no-API-q assertions, two typed Show responses, correct change777 route, state=all retention and q-absence assertion remain at e2e/specs/admin/requests_operations_smoke.spec.ts:1027–1040. Later visible-request/applicant paths at:1042–1051 and adjacent outage negatives remain intact. No assertion, wait, timeout or retry was weakened.

I independently read the original target trace/context from the retained archive in memory, without extraction/download. Archive/member hashes and selected event/frame/network facts match evidencee673c154 and closurea213a6d2. The q-absent poll completes before input; the fill/Enter frames show /admin/requests?state=all; both Show calls return canonical200 frames; the subsequent change777 URL contains returnTo=/admin/requests?q=legacy&state=all. This supports correcting return-path construction. It does not identify the exact internal React scheduling event, and no successful-retry DOM behavior is inferred.

## Architecture and repetition

The finite helper belongs in the existing requests model and is used at the existing common return-path construction point. It covers row/detail/queue consumers without a shared router, hook, adapter or framework. The existing browser normalization effect and this captured-path boundary serve different purposes; the small repeated deletion does not justify a generalized normalization layer.

The detail-side security boundary remains unchanged: RequestDetailPage.tsx:198–199 uses safeRequestsReturnTo, whose RequestDetailModel.ts:137–149 restricts origin and path to the request overview. The new helper constructs an internal route from the existing application basePath and query serialization; it does not replace that validator or introduce an external redirect target.

No new cross-project/provider ownership or duplicated mutation policy was introduced.

## Scope and proportionality

This is a demonstrated production navigation defect exposed by the authorized broad verification, rather than a fixture workaround or an unrelated routing project. The functional patch is56 insertions/4 deletions including tests and documentation; the larger committed diff is mostly normal formatting of the three owned TS files. I inspected the actual formatted diff as well as the minimal patch; the owner also retained formatting/debug evidence. No optional subsystem or unrelated hook cleanup is needed to satisfy this boundary.

The small existing work-log/index update accurately records cause, behavior and pending acceptance. Existing workflow/requirements treatment of review queues, return-to-list behavior and error preservation remains applicable. The new owning model regression documents the precise normalization invariant. No new UI copy, layout, locale, screenshot or KB mapping is introduced, and no new KB/live-image currency claim is made.

## Risk, compatibility and inherited lint boundary

The helper is a local read-only navigation transformation. It does not perform writes, alter roles, change async request identity, clear review state, weaken receipt/uncertainty handling or change the accepted bulk-note behavior. It removes only the unsupported legacy request q key; valid filters and pagination remain. No API/backend/SDK/runtime/dependency or deployment-order change follows.

I independently inspected the three direct whole-page ESLint diagnostics and their baseline/current source:
- unstable fallback identities for reg and ch around RequestsPage.tsx:285–289;
- the existing shareUrl memo's unnecessary sp dependency at:697.

They are identical inherited diagnostics, with source changes limited to formatting around those sites. The changed listReturnTo memo itself keeps its original dependencies. The project lint command runs the existing scoped-quality selection, whose eligible roots exclude pages; it was not narrowed by this patch. The helper/test direct lint and declared project lint passed. Parent dispositiona25be05e is therefore a reasonable bounded treatment; no directly relevant new defect was found. **Whole-page lint remains three errors, not lint0.** No rule suppression or mandatory-hook bypass was introduced.

## Evidence binding and verification limits

I independently matched all2595 final committed blob SHA256 values, object IDs, modes and live files to the final manifest and successful frozen working snapshotdf375f7c. All1370 installed hashes match that snapshot. Exactly five paths differ from published79980; the other2590 records are unchanged.

Retained logs/hashes support:
- focused model Vitest:1file/9tests passed, including3new cases, command exit0/3.759s;
- helper/test lint, formatting/debug, docs audit and whitespace exit0;
- declared project lint exit0/5.652s;
- actual app strict native exit0/59.777s, PID941812/start35202483, matching native exit/log and parent acceptance.

The original stopped quick batch and its page-lint failure remain honestly recorded. These checks ran against the later-committed working inputs, not literalbabe5142 commands.

The recorded E2E1159/tooling380 dependency enumerations exclude the changed TS files. Their recorded hashes match current bytes; all relevant tracked configuration and installed inputs are unchanged. E2E membership remains153/130; the complete metadata, baseline and deferrals are byte-identical. This retains earlier successful evidence for its exact input scope, not a new compiler execution. The prior31 advisory tests/captures similarly retain only their unchanged-input scope.

I ran no tests, lint, compiler, browser, Nix evaluation/build, install or network operation.

## Complete history, update streams and migration conclusion

I independently compared the complete nine raw commit objects, parents, authors/messages and pathsets with w-request-returnto-nine-series.json and matched both complete and narrow binary diffs to actual Git. All eight published79980 ancestors remain literal.

1. 9fd6d575 — compatible broad-workflow action dependency refresh.
2. e615538c — PR/all-branch triggers and owning documentation.
3. 96b02de8 — storage/VPS/DNS/export/focus fixtures.
4. d077da52 — infrastructure/outage/action-state fixtures with accepted role-shaped remedy.
5. 3e2d77ed — request-review/WebAuthn fixtures with accepted ordering remedy.
6. 5985f173 — nine whole-leaf strict adoptions.
7. 91ca5ab4 — explicit bulk-note intent, tests/catalogs/contracts.
8. 79980b6a — node-issues fixture and its strict adoption.
9. babe5142 — inherited request return-path correction, model regressions and owning log.

The new production bugfix addresses pre-existing baseline construction outside the earlier fixture patches. It does not replace or remove an earlier follow-up implementation. The ninth ordinary descendant is coherent and respects published-history protection; no rewrite authorization is inferred. No obsolete alternative implementation, fixup chain, abandoned compatibility path or superseded branch migration remains.

There is one workflow action-ref refresh, with triggers separated. There is **no application SDK/npm/lock/flake/hash/backend/channel update stream** in670..babe and no repeated dependency update to consolidate. The two earlier coverage stages are additive adoption for distinct repaired leaves under the retained published-prefix boundary; this ninth commit does not change that metadata.

**No migrations:** the ninth commit and complete670..babe range contain no DB/schema/persisted-format migration, seed or conversion. There is no intermediate migration release/deployment/external-consumption lineage to preserve or consolidate. Merged670's earlier client adoption and recovery provenance are unchanged. Reverting this ninth commit would restore the navigation defect, not require data conversion.

## Remaining gates and disposition

No review finding blocks parent disposition, but the corrected retries0 browser case, exact-final rooted Nix5 and current required/full broad CI remain pending. Static/list-only preparation is enumeration, not runtime evidence. Green79980 checks containing the diagnosed built-in retry do not certify this correction.

Remote publication is supported by retained authoritative79980/PR133 receipts, not a fresh reviewer network observation. The local origin feature tracking ref is stale atd3d5; it was not treated as authoritative remote state. Parent must perform normal fresh target/feature verification before any later integration.

Earlier live-backend, preview and A040 limits remain unchanged. This report grants no merge, configuration integration, deployment, cluster or session lifecycle acceptance. Parent owns the remaining checks and separately authorized later actions. Source/HEAD remained frozen and the session remains open.

Parent persistence target: work/2026-11-01-typescript-client-migration/webui-request-returnto-babe5142-final-review-result.md. Full report delivered through team reporting because reviewer access is read_only.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
