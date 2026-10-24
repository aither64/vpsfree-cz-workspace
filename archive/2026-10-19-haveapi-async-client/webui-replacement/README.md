# Production WebUI HaveAPI replacement

User direction on2026-10-20: “well no trial, just replace the original solution
in vpsadmin-webui with the new client”. PR74 remains open.

| Package | Owner | Expected result and acceptance | Dependency/checks |
| --- | --- | --- | --- |
| Design (accepted; design.md17-136) | architect0 | Actual AsyncClient normal runtime; reproducible pre-release dependency; remove duplicate protocol implementation; retain WebUI BFF/session policy | Record near-top design addendum before source edits; combine peer findings |
| Package/dependency/contracts | implementer0 | Exact official package consumable by clean npm ci/Nix/CI without npm release; focused provider/consumer checks | Architect design and released disjoint paths; no frozen HaveAPI changes unless demonstrated defect |
| Application/docs | implementer1 | Authenticated, description and public paths use new client; superseded generic fetch/decoder removed; accurate owning docs | Architect design; independent files from owner0; focused regressions |
| Final review | reviewer0 | All applicable lanes, complete commit series and migration/update-stream conclusions | Intended changes committed and quick checks passed |
| Longer verification | one fresh retained Luna/low watcher | Actual app workflow/client package/build checks with exact identities and durable logs | Independent final review; one operation at a time |
| Publication/contact | lead | Concrete PR74 update, evidence and truthful limits | No merge/deploy/release or lifecycle action; user-facing prose pass |

All source edits and Git operations stay with implementers and are serialized
per repository. Earlier pilot/no-default-switch restriction is superseded by
user direction. HaveAPI merge authorization persists; its runtime adoption is
owned by the separate rollout session. This work does not resume infrastructure
investigation paused by the user.

## Provider acceptance checkpoint

Owner0 reports old emitted bundle fails valid nested HTTP200/422 rejection tests;
corrected strict build, both emitted TypeScript consumers, callback26 and core13
pass, including bad scalar/metadata controls. Lead inspected the focused source
and documentation diff and applied the main writing pass, accepted unchanged.
Normal HaveAPI commit is released after remaining known quick async checks.
This is quick-check acceptance, not independent final review or a new release.

Owner0 has the sole utility slot for one necessary uncertain-duration dependency
setup/prefetch/hash-generation operation. Full app/package/browser integration
checks remain behind committed-deliverable independent review. No source push
or WebUI Git commit slot has yet been released.

Owner0 additional quick results: all39async actual-bundle cases passed, including
receipt/resource and prior R2 regressions. Normal commit encountered stale
Overcommit signature before hook execution; owner verified config/hooks unchanged
from HEAD and is using ordinary `overcommit --sign` then normal commit. No hook
bypass authorized. Exact tracked generated files are included; ignored-parent
warning during staging did not change tracked content.

Exact final corrected package archive generated from clean committedf94e65e
with normal pinned HaveAPI Node24.21/npm11.19: npmci5s, gulp4s, pack, clean build
and all51files match committed source. Existing17development dependency audit
warnings retained, no automatic dependency updates. Vendor archive/provenance
and root dependency prepared; root lock baseline unchanged before watcher.
Owner0 launches sole fresh Luna/low batch for package-lock-only install, unrelated
version guard, npmci and pinned prefetch/hash. Stops first failure; no frontend
build/tests/browser or independent final-review claim.

## Source and history state

Owner1 reports actual production AsyncClient import/default, separate auth/public
instances and removed redundant wire modules.35fixture migration to real-package
controlled XHR remains in progress. No tests claimed green yet for replacement.

Architect whole-history readback:0d05pilot mixes reusable policy/seam with now
superseded runner (~1,000lines);5dd is truthful historical proof. Keep published
refs unchanged during implementation; no deployment/schema boundary requires
obsoletepilotimplementation. Final reviewer must assess fullseries and any
consolidation need. No rewrite/rebase/forcepush authorized so far.

Dependency operation first attempt: normal npm lock generation/unrelated-version
guard, clean npmci and real AsyncClient import PASSED. Pinned prefetch failed,
exit1 about32seconds; stopped first failure. Utility released and owner0
diagnoses actual stderr; no alternative/filtered lock/cache workaround applied.
Owner1 has sole utility slot if needed for bounded migrated-domain quick batch;
full app/build/browser integration still awaits finalreview.

PinnedNix diagnosis confirms standard importNpmLock + matching npmConfigHook
can handle localpackage via exact packageSourceOverrides; architect finalseam
pending before edit. Frontend actualowner path packages/frontend.nix, preserve
its source/provenance/audit/install boundaries and BFF unchanged. No toolchain
update/customfetcher/filteredcommittedlock. Normal install locked xmlhttprequest
1.8.0 plus HaveAPI only, all482oldentries unchanged.

Owner1 core actualinstalledpackage checks4files/63tests/7.34s PASS. Typecheck
found fixture narrowing and legitimate envelope.message null; lead approved only
errorMapping nullish normalization to existing undefined semantics, no UIcopy.
Now sole fresh Luna/low watcher runs exact35changed domainfixtures (39total minus4core) excluding
alreadypassed corefiles; owner1 inline app typecheck proceeds independently.
No dependency/node_modules mutations; no fullsuite/browser/build.

Owner0complete inventory at owner0/README.md read by lead; all6HaveAPIcommit
messages/fullrange/correction diffs, exact22dependency paths/commit, archive
provenance andlockdelta bindactualchecks. Providerfinalf94clean; consumer
dependency3b2committed; bothnotpublishedyet. No migrations, no intermediate
vendorpin; oldmixedpilotpublishedhistoryretainedforfinalreviewdecision.

## Committed candidate in independent final review

HaveAPI f94e65e35166a0bf8048a27c9d57c7d36957d65b/tree2f2879b95f4fba789d8a9d52ca914b8876438dae.
WebUI8772bab21cd8739bf4672cdf4976aea2a6e59de3/tree3302fcf2bc01f1885426a69c7ddc364b8cdd35ad,
sourcecommit62paths940+/902- andcompletefinalrange72files1661+/617-. Bothclean.
Mainreadinventories/fullseries/status/tree/whitespace; owner1finalquick39files/
289cases9.52spassed plusapp/tooling/E2Etypes/docs/lint/structural.
Reviewer0retainedSol/xhigh/read_only all4lanes assignednewfinalturn, nooverrides.
Wholehistory/migrations/update-streamdisposition explicit, oldmixedpublished
pilotnotexcusedbypriorproof. No fulltests/builds/browser/pushyet.
Owner0preparespostreviewfullapp/Nixbatch; owner1prepares9ordinarybrowsercommand
withoutlaunch. PRtextpreparedlocally currentfinalscope/pendinggates, notpublished.

Lead independently reconciled vendortarSHA256 andall51regularpackedfiles
byte-for-byte against gitobjects of exactproviderf94 (read-only, noextraction
write), allmatch. Postreviewfullapp/Nixandordinary9specscripts prepared and
readby lead; no launch. Browser usesnormalVitedeventry, minifiedBFFbuildseparate,
no productionbrowser/OAuthclaim. Revieweractive, sourcefrozen.

ReviewerinterimImportantfindingaccepted: publishedmixedpilot/proof thenremoval
isobsoleteunappliedhistory; no supportedboundaryjustifiesit. RepoAGENTS73-74
requires explicitexactpublishedcommitrewritepermission. No permissionassumed,
no waiver/readinessclaim. Architectpreparesfinaltwo-commitpartition while
reviewcontinues. CorrectedfinalincomingoverlapSIXpaths inclnodefixture/E2E
coverage; current3docs-onlysummarywaspilot-only. Futurebasepreservesupstream
newnodehelpers+signaltest/adoptedstrictE2E. No source/ref/indexmutationyet.

## Final review result

Retainedreviewer0completedall4lanes atf94/8772: code/contractsACCEPTED; no
Blocking/additionalImportant/Advisorycodefindings. I1Importantobsoletepublished
pilothistoryremainsaccepted/notwaived. Finalreview.jsonrecordsidentity/ranges/
findings/proofs/limits. No longverificationyet. Architectrecommendswaitfullruns
untilb9reconciledfinalcommittedcandidate toavoidrepetitionofchangedbehavior/
coverage. Owner1preparesONLY reviewablecontentpreviewprivateindex/tmp, noowned
originalsource/index/ref/remotechanges, beforeexactpublishedrewritequestion.
Preparedfulltests/Nix/browser scriptsremainheldandnotexecuted.

Provider publication released independently after completedproviderfinalreview.
FreshnormalNixSSHfetch confirmsmasterc587, remotesource19c, localf94clean; no
rebase/basechange. Firstnormalpush refusedstaleOvercommitprepushsignature before
remotechange; ownerreviewedunchangedconfig/hooks andusesnormalovercommit--sign
thenauthorizednormalpush, nobypass/force. Actualreceipt/CIIDs pending, nowatcher.
