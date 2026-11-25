# Shared incident escalation React rework

Phase: reviewed shared source, bounded browser correction and accepted captures
published; exact-final-head CI complete/success. Ready, awaiting merge approval.
User
authorized the shared predefined-rule rework and the architect/lead released
the replacement implementation contract. No rework publication, build, browser,
capture or guest run has started. Original proof remains historical only.

Preserved original published source:

- Base: `40653dffed4561dd6086716fd506a7223d3631d7`.
- Final head: `b67c7917e8758e707e0b88512f055eab9fbd8529`.
- Full tree: `ce3b38c9ba4245e363dab48f8a8cc63882c90791`.
- Local preserved ref: `refs/heads/dev/oomd-abuse-policy-original-b67c7917`.
- Existing feature branch: `dev/oomd-abuse-policy`.
- PR: <https://github.com/vpsfreecz/vpsadmin-webui/pull/115>, open at the exact
  original head; SSH remote main/feature proof checked read-only.

Original review/check/capture ranges remain in [react-package.md](react-package.md),
with raw supporting receipts and compact failure traces under
`react-verification/`. The prior successful checks do not certify the replacement
API. Preserve these original refs/ranges while consolidating the final unmerged
series into the generic implementation; do not leave obsolete OOM plus generic
implementation history in that final series.

Saved implementer2 identity/access/settings verified: ready, workspace_write,
Sol/xhigh, retained catalog495ef662. Session current/env agree with trusted
binding; both environment variables absent. Required workspace Git/verification/
storage procedures and React AGENTS/localization/Nix/hook declarations reviewed.
No hook framework is declared. After authorized cleanup all package dependencies
and dist were absent; the later bounded frontend restoration is recorded below.
No shared or peer cache was touched.

## Scope and dependencies

React owns only its existing VPS adapters/components/tests/locales/docs and PR.
One shared per-type contract with a single registered trusted whole-VPS
memory-pressure rule, preserving5/7d warning,10/30d stop and24h new-incident
cooldown. No rule editor, additional navigation, arbitrary actions or BFF route.
Existing OOM-report screens are separate and remain outside this package.

The frozen contract is [implementation-contract.md](implementation-contract.md);
the lead owns accepted EN/CS wording in [mail-rework-copy.md](mail-rework-copy.md).
The implementation uses the selected registered key/localized label, per-type
counts/limits/warnings, VPS-wide permission/cooldown/action, explicit isolated
settings writes, selected readback and old-API capability fallback.

Current source map: `src/lib/api/vps.ts`; `VpsIncidentCard/SettingsForm/Filters/Indicator`,
`vpsIncidentEscalation.ts`, existing list helpers, focused adapter/rendered/browser
tests, incident locale chunk and REQ-051/API/workflow/work-log docs. Preserve immutable
save snapshot, narrow synchronous acknowledgement and unrelated async receipt
guard, nullable resets/readback, owner/admin gates, missing-field capability
fallback and latest-search ref regression for rapid/external navigation.

## Implemented package and current evidence

React source/helpers/catalogs/test IDs now use incident-escalation naming.
Existing process OOM screens remain unchanged. Synthetic `test_rule` tests prove
selected counts/limits/history/settings/readback and generic help, without adding
a production rule. The rapid-search ref fix, immutable submitted snapshot,
preflight/lock, nullable resets and unrelated async receipt guards are retained.
API/REQ-051/workflow/evidence docs and a replacement dated project work log
describe the common interface. Old4PNGs are preserved under the original ref and
`react-verification/historical-b67-captures/`, removed from the current feature
tree so they cannot be mistaken for new-label evidence.

The authorized root-only offline `npm ci` restored293,654,528 allocated bytes;
see `react-rework-verification/root-dependency-allocation.json`. This is a new
allocation after the completed cleanup, not a continuing net-recovery claim.
BFF dependencies and dist remain absent. No shared or peer cache was changed.

Quick verification, with exact source hashes and unchanged-input receipts in
`react-rework-verification/`:

- Initial wrapper failed before launch because `/usr/bin/time` is absent; no
  tests ran in that attempt. Python monotonic runner removed that assumption.
- First actual focused six-file batch:75passed/1failed. New API test mock
  returned both `vps` and `vpses` envelopes; strict adapter rejected ambiguity.
  Corrected only the mock to return distinct list/detail responses. The failed
  result/log remain unchanged.
- Corrected API file:18/18passed, inline pinned Vitest run. No product fix and
  no repeat of unaffected passing test files.
- Remaining batch: application types, adopted E2E coverage/types, design audit
  and all lint stages passed. It stopped at `format:check` on
  `tsconfig.e2e.json`; Prettier formatted that one file. Logical adopted entries
  are unchanged. Failed81.93s result/log remain unchanged.
- Fresh Luna/low watcher completed remaining format/locale/structural/component/
  page/active-doc/UI-string/mutation audits:exit0,20.6s. No new structural
  exception.8411matching EN/CS keys and225mutations/no warnings.
- Final rendered assertion now checks the current approved exemption help and
  localized API label:19/19passed,10.76s. Final changed-test typecheck and
  reconciled docs audit passed. No broad suite/build/browser run.

Final consolidated head `55a813b44edb915c7ed5ce68366d6d797a551606` is clean on
fresh SSH main40653dff. One generic application commit,30files1040+/23-; no
migrations, pins or obsolete API aliases/current old-label images. Preserved
preconsolidation2fb91af6 ref/tree equals final tree
`a9de950ca24ba002143a24744e6d8c1091e6a067`. Exact range-diffs, finaldiff,
source hashes and clean-source receipt retained in `react-rework-verification/`.
Normal Nix commits/rebase used; configured contributor identity verified;
no hook framework declared or bypassed.

## Postreview result, 2026-10-31

Retained reviewer0 completed all four lanes at55, no React finding; explicit
coherent-history/no-migrations conclusion in [shared-review.md](shared-review.md).
Lead released source gate after separate backend R1 direct verification.

Scoped browser run initially10passed/1failed/1notrun. Canonical-limit-only
correction had1passed/1failed; no old-API follow-up launched. Concrete traces
showed deferred router publication dropping a filter. Existing `flushSync`
navigation convention plus explicit current pagination limit corrected this;
latest-search ref, unrelatedparams/reset/externalBack behavior remain.
Negative guards and focused21/filter2/types/affected audits passed. Lead directly
accepted bounded fix. Final affected overview2and remainingoldAPI1passed with
retries0. Original failures remain separate. See
[browser correction](react-browser-correction.md).

Fix folded into owning app `4343a02cb13ba42ae50a3276715f1c8e5b7765ea`;
tree4bee7d1455f35cd422fc385fafda18486f6ee3ea exactlyequals testedstage and
preconsolidationd8d93a1. Retained55/d8d refs/rangediffs preserve review lineage.
Onlynewcomponent/listpaginationprops+supportingtests changed; no sharedrouter/
pagination/API change. Eight detail passes/captures retain55scope and unchanged
detail/adapter/catalog hashes. Accepted corrected lists come from4bee tree.

Lead visually accepted4actual syntheticPNGs, requested one capture-only desktop
scroll reset, then accepted replacement. One existing ENadmin desktop case and
affectedE2Etypespassed; fixture hashde357213..., productruntimeunchanged. Missing
unrelatedfixturedata and synthetic-vs-real limits remain explicit.

Complete final series on fresh SSH main40653dff:

1. `4343a02cb13ba42ae50a3276715f1c8e5b7765ea` application.
2. `9e7dd95d67a3b33b88674a3d436775e0bb820504` evidence/worklog/4PNGs and
   two capture-only fixture lines.

Finaltree47812c2ba7826c71cf6a014de1dd92592bb7dbea. Runtime/toolchainroots
equal4343; no migrations/dependency updates/obsolete intermediate history.
NormalNixidentity/hooks verified; noframework declared/no bypass. Clean source.
Single force-with-lease publication replaced actualremote b67 only; SSH/PR115
head exact9e7 confirmed. Comparison capture saved base40653/head9e7. Existing
PR title/body uses sharedcontract/REQ051/currentimages/honestsourcegraph.

Automatic runs, exact9e7:

- [CI41186801790](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41186801790).
- [Playwright41186801724](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41186801724).

Fresh Luna/low utility observes onlytheseIDs and saves full results/logs under
`react-rework-verification/hosted-final*`. No duplicate workflowdispatch/full local
ci:pr/BFFdependencyrestore. No supersedednonterminalwork existed tocancel.
Terminaloutcomes: bothaggregates/allsixcheckssuccess at9e7. CI226script/57BFF/
1954unit(309files), build9.48s,productionaudits0; smoke613desktop/555mobileChrome/
249WebKit=1417passed+2intentional skips, noflaky/retrysummary. Actualfull
devdependencyinstall19advisories(16moderate3high) inheritedunchangedlock;
recordedseparatelyfromcleanproductionaudits. No reruns/dispatch/sourcechurn.
PR115updatedactualresults; fullreceipt [react-shared-final.md](react-shared-final.md).
Watcherended,norunningoperation. No merge/deploy/lifecycle. Sessionactive/open.
