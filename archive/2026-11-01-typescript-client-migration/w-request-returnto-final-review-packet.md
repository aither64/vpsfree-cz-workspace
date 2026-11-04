# Final request return-path review packet

Repository: vpsfreecz/vpsadmin-webui; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui`.
Session:2026-11-01-typescript-client-migration. Plan/state/design remain in this tracking directory; bounded owning brief is `w-request-returnto-design-brief.md`.

Base `670cf286daf9bddb65594035507ca112a9e6d397`; published parent `79980b6a6607d08cccd252439ced328a250bd5b0`; final head `babe51421bd1df61a548e7b2f047053df14ff3eb`; tree `95f01c23a06e2c385756daa61305413af24403d9`.

## Requested outcome and scope

Fix the actual first-attempt broad failure before main integration. The approved target trace proves that the visible list URL had already dropped legacy `q`, but typed Show lookup navigation restored it inside `returnTo`. No exact React scheduling event is claimed. `requestListReturnTo` copies parameters and deletes only `q` at the owning construction boundary; RequestsPage uses it without changing memo dependencies, router, async lookup, guards, review state or pagination. Three meaningful existing-model regressions cover captured/duplicate legacy parameters, preserved filters/pagination/order, nonmutation, canonical/empty paths.

Exactly five paths changed in the ninth ordinary commit: RequestsModel.ts, RequestsPage.tsx, RequestsModel.test.ts, approved dated work-log append and WORK_LOG index. No UI copy/layout/KB edit, shared control/hook/router/API/SDK/backend/pin/persisted-format change. The active E2E leaf remains byte-identical, including its original wait and assertions. Strict selection remains153/130 with all metadata/deferrals unchanged. Existing workflow/requirements request contracts were inspected; no additional contract gap required widening docs.

## History and migrations

All eight published commit objects remain literal; ninth is an ordinary child of79980. No rewrite/fold/amend/fixup was used. Complete raw commits/authors/messages/paths/stats and current diff are in `w-request-returnto-nine-series.json`; full and narrow patches plus old8/new9 range-diff accompany it.

1. `9fd6d575c37032727394a5352591ecc25f51d96b` — Refresh broad smoke action dependencies
2. `e615538c88d05a5b340dc811fed1bf5ff8437a14` — Run broad smoke on pull requests and every branch
3. `96b02de80528319d728b95ed060037b18a62c091` — Align broad storage and VPS fixtures with canonical API contracts
4. `d077da52e4364763999c8d4e5cada437e9a71065` — test(e2e): align broad smoke fixtures with generated API contracts
5. `3e2d77ede05077f51ce57f987bdd2e6c3f6087a1` — Correct request-review and WebAuthn broad smoke fixtures
6. `5985f173928973de24a425c2f26becd32143f17f` — Adopt repaired broad-smoke leaves into strict E2E coverage
7. `91ca5ab44d07d62a8226f5a2b774747a44ff2c0d` — Require explicit language selection for bulk advisory notes
8. `79980b6a6607d08cccd252439ced328a250bd5b0` — Correct the node issues-filter fixture and applied-state assertions
9. `babe51421bd1df61a548e7b2f047053df14ff3eb` — Remove legacy q from request return paths

The stages retain separate workflow action-ref update, automatic PR/all-branch routing, three independent fixture packages, central nine-leaf strict adoption, bulk-notes product policy/regressions, later node-issues fixture/strict adoption, and this local return-path fix. The new fix removes no preceding stage or supported flow. No obsolete alternative framework or compatibility path is introduced. No migrations or DB/persisted-format changes exist in the complete670..head range. No application dependency/lock/flake/API/npm hash update stream exists in these nine commits; workflow action refs were updated once in their focused stage, with triggers separate. Earlier0.4 adoption/recovery lineage is in merged670 and retained records, not rewritten here. Rollback of this correction restores a navigation race and needs no data conversion.

## Verification and exact input binding

All2595 committed/live file SHA/blob/modes equal the accepted frozen working snapshot `df375f7c24a5cae2bc68647fde37fd2a1156998d5444cdb911991ade4c75706f`. All1370 installed guards remain equal; other2590 paths/modes unchanged from published79980. Final full source manifest SHA256 `a01d8df7aa4220cc3b47ae9b92d2430ef2a38c1a327ca8158282ccff975ea534`. Fullclean/empty index/no untracked/no operation; only ordinary feature ref advanced.

Actual focused Vitest1file9tests PASS0/3.759s (three new regressions); helper/test lint, full touched formatting/AST check, docs audit and whitespace all0. Declared `npm run lint` PASS0/5.652s. Extra direct whole-page lint remains3 inherited diagnostics with zero new: literal79980/current comparisons and exact lead disposition `a25be05e69b111eaf09531460ca78d10d6e9cee112ec50486306fa6cb77c15d4` are explicit limits, **not** page lint0. No hooks/rules were suppressed and unrelated reg/ch/shareUrl hooks remain unchanged. Original stopped quick batch remains retained. First project-lint exec refused before process creation; its first actual command then passed with explicit Bash.

Affected application strict actually PASS0/59.777s, native PID941812/start35202483, parent watcherCLI65497 terminal0. It ran on the frozen working snapshot over79980, not literal79980 or a future-head command. Final committed/live equality binds that exact successful input to this head. See app-strict native log/state/exit/lead acceptance and `w-request-returnto-quick-bindings.json`. Current E2E/tooling dependency memberships1159/380 exclude all changed TS files; all tracked dependencies and1370 installed guards are unchanged, retaining prior accepted strict153/130/tooling evidence in their actual input scope. List-only enumeration is not a new compiler pass. Prior31 advisory tests/captures retain only unchanged production-input scope.

Normal Prettier reformatted pre-existing lines in the three owned TS files: full ninth diff226insertions/160deletions versus minimal functional patch56/4 including docs. `w-request-returnto-functional-only.patch` SHA256 `2cff5e7c7f141788c60a1142f8c549182a87eb74a29b396fdf6c78801c2d493a` and formatted/narrow patch preserve this distinction. No other paths/modes changed.

## Independent review request and remaining limits

Parent selects retained reviewer0 Astra/xhigh/read_only with saved settings. Inspect the complete nine-stage history and final diff, then all four affected lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. The local fix is medium-risk compatible navigation normalization; broader branch context includes mutation/no-replay policy and workflow verification. Explicitly conclude whole-series/history, no migrations, input-stream disposition and inherited lint boundary; do not treat earlier review as automatic new-change acceptance.

Existing eight-stage reviews/step9 acceptances and original33/99 failure evidence remain retained. Target causal closure SHAa213a6d2 and evidence SHAe673c154 are inputs, not a passing rerun waiver. Current79980 CI10jobs green includes the diagnosed built-in retry; no new-head browser/Nix/CI pass exists. Final affected native case retries0, exact-head rootedNix5 and current automatic required/both broad CI remain pending after committed review. No publication/main claim/configuration/preview/cluster/lifecycle action was done. Parent owns later integration and user cluster controls.

Commit receipt `w-request-returnto-commit-receipt.json` SHA256 `6043dd0a5ef5d8957c730f9c2f085e800f7783d535a07d61b2a51ae6512eb8bb`. Final manifest, nine-series/raw history, complete/narrow diffs, range-diff, exact quick receipts, manual-lint baseline/current/lead disposition, approved prose and source guard receipts are linked there or in `w-request-returnto-quick-bindings.json`.

Source/Git/index turn explicitly RETURNED to lead; source frozen at final head. No W-owned active operation/claim/reservation. Static native/Nix preparation may follow in tracking only.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
