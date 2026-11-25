# React merge preparation — structural fix milestone

Clean committed **32f29638855946e22a06a22f6853cffc321eaa87**, tree **0d5212cf3b2485cb947781f21f83884baea9a397**, frozen locally.
Publication is **held** for root's final SDK/adoption coordination. Public feature
remains bd7518; no remote mutation or new CI campaign ran. Same verified session,
roster44, implementer2 Sol/xhigh/workspace_write/full_access.

## Exact scope and module boundaries

The original run45447641643 at bd7518 failed only structural budgets in Required
nonbrowser checks / Run required quick checks: Views581 and router502 crossed500.
Original complete failed log is failed.stdout; run.stdout binds successful
Production build and Chromium script regression. Those passes retain bd7518 scope;
no blind rerun or new browser/build claim.

Six paths only:

- AdminIncidentViews.tsx:491physical lines (audit492), retaining all Overview,
  History, details/restrictions and paging; the existing Counts export is retained.
- New AdminIncidentFacts.tsx:94physical lines (audit95), only moved DateFact,
  AdminIncidentCounts, Fact, ChainLink and OutcomeSummary. Same context/router/
  formatting imports and exact bodies/signatures, no state or new abstraction.
- router.tsx:498physical lines (audit499); replace the five adjacent admin incident
  routes with a spread at the same position under identical parent guards.
- New adminIncidentRoutes.tsx:10physical lines (audit11), the same five route
  objects and SAME CoreRoutes component bindings. No new lazy/component wrappers.
- design-inventory.mjs: register the new existing-style route module.
- IMPLEMENTATION_INVENTORY.md: regenerate only five source links. All270route
  paths/elements/order/parent layers and79API module entries are unchanged.

module-equivalence.json proves all19function bodies/signatures unchanged after
normalizing export declarations/formatting. Expanding the route spread reconstructs
original router source byte-for-byte; inventory rows become byte-identical after
normalizing only the moved source path. Visible copy/styles/null/false/outcome/
permissions/filter/cutoff behavior stays unchanged. No budget/baseline/exception,
SDK/pin/hash/BFF/API, migration, catalog, screenshot or user prose change. Generated
inventory is the only necessary project documentation update; existing behavior
contracts and historical worklog remain unchanged. Technical rationale stays here.

## Actual quick verification

One sequential operation64bd5bf6-d7ee-4348-8ff5-de6a4b15b93c exited0 in185.555s:

- audit:structural0/0.654s:20raw/20preexistingaccepted,0unaccepted/0newexceptions.
- Changed-file strict typing with actual transitive imports0/52.102s.
- All four changed source files ESLint0/3.787s.
- Existing affected Views/PolicyPages/PageView/ParamKeyedRoute tests:37PASS,
  four files0/12.337s. No new test/relabelled unique coverage count.
- Exact CI required entry **npm run ci:quick0/116.654s**, including all audits,
  application/tooling/e2e/BFF typing. No latent failure surfaced.
- Diffcheck0; preparation formatter and generatedinventory succeeded.

quick-result.json and quick.stdout/stderr preserve exact commands/output. Fresh
installed g7wv/catalog7659519 Luna/low watcher19597 exited0 with INCOMPLETE before
ci:quick ended (and named unavailable log filenames). Active parent visibly
continued the SAME original native48971, joined its authoritative terminal0 and
read the final receipt. No command/watcher relaunch. Original watcher report remains.

## Commit, history and effects

One normal **git commit --amend -F** exited0, folding into the owning UI purpose.
No declared hook framework/active non-sample hook/core.hooksPath; no bypass.
Original UI author/date preserved. Checked committed hashes bind all six files.
Exact full4499..new remains TWO purposes: unchangedSDK5c291 then UI32f296.
Create-only refs/evidence/implementer2/nov24-merge-prep-reviewed-bd7518 preserves
bd7518; all prior reviewed/deployed refs remain. No migrations or repeated pin
stream. Source is now substantive module successor, not a literal new deployment
or whole-tree equality claim against deployed f7.

affected.diff/full.diff/series.txt and committed-source.json bind exact old/new
ranges, finaltree, path/hash checks. Root owns final affected review and necessary
exact-head checks after settled SDK adoption. Temporary development SDK still
remains selected; no registry prerequisite is claimed satisfied.

All native handles50616,19597,48971 joined; no unknown effects or active operation.
No browser/service/build/runtime/default/npm/release/lifecycle/cleanup action.
Source frozen, publication held as assigned; root coordinates next source window.
Implementer2 retains technical fixes. Existing deployment remains unchanged.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
