# Final replacement review packet: RELEASED for committed candidate

Lead releases final independent review now. Intended substantive source, tests,
package/build and technical documentation are complete and committed; quick gates
passed. Both source trees clean and complete diffs whitespacechecked by lead.
Do not start long verification; inspect the full candidate and flag real findings.

Requested outcome: user “well no trial, just replace the original solution in
vpsadmin-webui with the new client”. Replace all generic HaveAPI transport,
including authenticated requests, anonymous/public reads and description lookup,
using the real AsyncClient in ordinary production entry points. Preserve WebUI
BFF/OAuth/session change/impersonation rules, exactly one qualifying read retry,
no mutation replay, abort, language/header selection and rejection/uncertainty
semantics; keep domain helper signatures. Remove superseded pilot/duplicate wire
implementation. Use exact reproducible prerelease official npm archive as normal
dependency, with integrity/provenance and normal npm/Nix build. No release needed.

Session:2026-10-19-haveapi-async-client, worktrees group same slug. Owning
brief design.md17-136; current records plan.md/state.md, webui-replacement/README.md.
Repositories: HaveAPI feature at worktrees/.../haveapi; React WebUI feature at
worktrees/.../vpsadmin-webui-async branch dev/haveapi-async-client / PR74.

Overall risk HIGH: public cross-project protocol, auth/session/retry and mutation
certainty boundaries. Required lanes general, architecture/repetition, scope and
risk/compatibility. Reviewer0 retained Sol/xhigh/read_only independently reviewed
prior coherent feature; same reviewer eligible and current identity saved in roster.
No model/effort override. Reviewer reads skill references directly and reviews
without nested agents. No tests/builds beyond quick review-specific checks unless
explicitly assigned. No source changes or publication/operation/lifecycle action.

Package ownership: HaveAPI owns protocol encoding/envelope/error decoding and
recursive wire-error type. Local ValidationErrors remains flat; callback Envelope
error default unchanged. WebUI owns runtime configuration and live credentials,
BFF recovery policy and result projection; public clients remain anonymous.
Actual consumers discovered by imports include57domain modules, description
cache, public dashboard/admin helpers and ordinary app/browser fixtures.

Non-goals: legacy PHP, backend/BFF/OAuth implementation rewrite, runtime rollout
infrastructure, UI redesign/copy/catalog changes, npm publication/version/tag,
WebUI main integration or deployment. PR stays open. No parallel default legacy
transport, trial flag, source alias, custom installer or filtered Nix cache lock.

Compatibility/rollback: unchanged server protocol/session persistence, no schema
or data migration intended. Restore frontend with its matching package lock to
rollback. Generic provider nested-error change preserves legitimate custom server
Action#error! forwarded maps, retains invalid scalar/metadata failure class.
Stock parameter errors remain flat; no claim that stock VPS emits nested maps.

Validation: owner quick evidence in nested-errors operation logs; oldbundle fails
validnested200/422; corrected strictbuild/bothtypes/callback26/core13/async39 PASS. Corrected provider commitf94e65e35166a0bf8048a27c9d57c7d36957d65b
tree2f2879b95f4fba789d8a9d52ca914b8876438dae; exact13paths105+/31-,
normalhooks/Jakubidentities/sourceclean. Official51filearchive matchedallcommitted
blobs, normalNixNode24.21/npm11.19 npmci/gulp/pack; no release/versionbump.
Final exact hashes/commits/quickconsumer checks still required below before review.
Longer full app/Nix/frontend/browser checks deliberately await independent review.

REQUIRED FINAL APPENDIX BEFORE RELEASE:
- Exact current bases/heads/trees/status; complete base-to-head series/diff in both repos.
- Whole history dispositions, obsolete unpublished approaches and all migration
  provenance (including explicit NONE); generated/dependency/update streams and
  consolidation or evidenced retention. Respect published refs/author history.
- Exact archive sourceSHA/SHA256/lockintegrity/inventory and frontend hash; npm/Nix
  localarchive compatibility proof state. Rootlock unrelatedversions unchanged.
- Final quick checks including actual package consumer/domain/public/renewal and
  docs/hooks/identity, all finalchanges committed before review.
- Owning componentdocs/provenance/APIrequirements/worklog/inventory links and main
  prosepass. Distinguish prepared/code/fixture checks from release/live evidence.
- Complete final diff and any retained earlier pilot commits justified by real
  reviewed finalcontent/history; ask lead if packet incomplete.

## Architect history assessment pending final reviewer

Read-only architect assessment: published0d05a258 mixes still-useful request/
session factoring and adapter tests with roughly1,000lines supersededpilot
harness and unchanged-default rationale. Published5dd2333b is truthful dated
proof, not a deployment/support boundary requiring obsolete code retention.
Continue additive candidate without rewriting; final reviewer must distinguish
published-history protection from any claimed independent seam-only purpose.
Preferred eventual series if exactrewrite authorized: one final vendored package/
lock/hash/provenance commit, then complete default runtime/tests/docs commit.
Preserve old complete head under a named before-consolidationref and exact
0d05/5dd reachability; user authorization needed before published rewrite.
No such refs/rebase/forcepush have been performed or authorized yet.

## Concrete packaging finding

Normalnpm installfile archive passed; all482previous lockentries preserved and
clean npmci/import succeeded. Same pinned prefetch-npm-deps rejected
file:///vendor/...tgz invalidformat. Architect/owner0 read-only investigation
of locked Nixpkgs `importNpmLock` local-file/npmConfigHook may identify standard
route. No Nix source edits/probe/build or altered/filtered lock authorized by
that finding yet. Final packet must name actual chosen supported packaging seam
and checks; do not accept passing npmci as sufficient Nix proof.

Read-only pinned-tool diagnosis: existing helper converts file:vendor archive to
file:///vendor and rejects format. Same locked Nixpkgs5e2305 supports
`importNpmLock` with its own npmConfigHook under buildNpmPackage overrides.
One exact packageSourceOverrides entry for node_modules/haveapi-client can map
to committed archive; standard importer creates/restores private store metadata
without filtering committed lock. Architect assesses exactdeclared seam before
owner0 edit. Actualfrontendexpression is packages/frontend.nix (notflake);
BFF stays on existing npmDepsHash. All source/provenance/audit/install checks
must remain. Final build proof still pending independent finalreview.

WebUIactualinstalledpackage core4files/63tests7.34sPASS. Remaining35fixtures
from39totalchanged APItestfiles delegatedonefreshLuna/low watcher; nofullsuite
yet. Typeconsumer permits envelope.message null; minimalerrorMapping nullish
normalization preservesundefined/no-message UIsemantics; no UIcopy change.
MainprosepassreadAPI_CONTRACTS/ARCHITECTURE/DOMAIN_COVERAGE/README/REQUIREMENTS/
VERIFICATION/worklogs and providedmechanicalwording; finalverificationfactpass
and provenance/PACKAGING prose stillpending beforecommit.

FinalNixseam accepted andimplementedonlypackages/frontend.nix: standard
importNpmLock with onecommittedarchive sourceoverride +matchinghook, remove
onlyfrontaggregatehash; BFF/flake/filter/provenance/installauditunchanged.
Knownquicksourcechecker6/6, nixparse anddrvPathevalPASS. Untrackedarchive
precommiteval doesNOTprovefinaltrackedsourcebuild; actualexactcommitbuild
requiredafterfinalreview. Sourcecheckadds exactnormaldep/lock/provenance archive
SHA256/integrity agreement; no custominstaller/cache. Mainprosepasscomplete
readfullvendorREADME/manifest/51filehashes/HAVEAPI_CLIENT/PACKAGING; fixexportOUT
andremoveobsoleteWASI-prefetchwarningsfromcurrentguide. LicenseMITincluded.

Committeddependency checkpoint3b2eed453f385ee37d07c7339edcce8fc28ffd31
tree3e32a1871a217457fae11202e0da47e196b63a0e, parent5dd2333b, exact22paths
502+/1013-, normalNixgitcommit-F/Jakub andno declaredhookframework/activehooks.
Mainreadcommitstat/indexempty, source/dependencyseparation preserved. Current
HaveAPIf94 clean; WebUIowner1 source/test/docs stillpendingcommit. Final fullseries
is not yetreadinessreviewable. FullNixsource nowincludesregulararchive+provenance,
nofrontendbuildyet.

Owner0fullinventory nowavailable: webui-replacement/owner0/README.md,
haveapi-series.txt (six commits/fullmessages),haveapi-final.diff,
haveapi-correction.diff,dependency.diff,dependency-paths.txt,provider-receipt.json,
dependency-receipt.json,archive-provenance.json,lock-delta.json. Leadreadcomplete
README/receipts/series; preserveoriginalfrozenpremergereports. No migrations in
providerorconsumer, no consumed/deployed intermediatevendorpin. Existing callback/
async/generatedproducingcommitboundaries eachcoherent. Finalreviewmust independently
assessall6providercommits andcompleteWebUIrange; publishedpilotmixedscopeexplicit.

Owner1finalquicks: all39changedAPIfiles289cases9.52sPASS,app/toolingtsc,
E2Ecore61checked/202deferred (changedpublicoverviewjoinedstrictcoverage),
docsinventory257routes64modules/audit118docs75requirements,
Tailwind/patternlint/scopedESLint25/Prettier62+directnewfiles,
structuralaudit0unaccepted/invalid/aggregatefailures,diffcheckPASS. Mainread
finalproductionworklogandacceptedfact/proseparagraphunchanged. Initial35domain
220cases204pass16fail diagnosedfetchfixtureobservations; correcteddecodedquery/
MIMEcharset/XHRabortcontrolswithnounchangedrequestvaluesorreplayweakening.
Actualpackagecoreaddedprojection/null/custommetadataandcontradictorystatus:true
HTTP401write-no-renewalregression. Sourcecommitnowreleased, awaitsfinalSHA.

Ordinarypostreviewbrowserplan9specs Chromiumworkers2,retries0,maxfailures1:
public/overview,public/news_compact,app/authenticated_home_smoke,
app/session_expiry_redirect,app/header_session_limit,app/vps_create_failures,
app/vps_create_admin_flow,app/blocking_action_progress_modal,
app/action_state_detail_page. RepoordinaryappE2Eentry/server nativeXHRasserted;
existingbootstrapversionedenvelopes/OPTIONS, noliveOAuth/APIcertification.
FullproductionminifiedBFFmodebuild/Nixfrontendsource/packagechecks separately.

## FINAL EXACT CANDIDATE — controlling appendix

HaveAPIbasec58704a08451a231fdf6c6123437133422af46dc..head
f94e65e35166a0bf8048a27c9d57c7d36957d65b,
tree2f2879b95f4fba789d8a9d52ca914b8876438dae, sixcommits.
WebUIbase7860521f30826c3886c89c35e8ab6f4e082e0a4b..head
8772bab21cd8739bf4672cdf4976aea2a6e59de3,
tree3302fcf2bc01f1885426a69c7ddc364b8cdd35ad, fourcommits:
0d05a2584bf30ee4acfa1d64bf00325cdda62934 (publishedpilot),
5dd2333b9af230d4a81c8f772cbbb08d39b14913 (publishedproof),
3b2eed453f385ee37d07c7339edcce8fc28ffd31 (normaldep/Nix/provenance),
8772bab21cd8739bf4672cdf4976aea2a6e59de3 (production/test/docs).
Lastfetchedmainb9f47f06e0877eb4a160053c413c4b87dd4a3d55,20upstreamcommits
beyondbase; source mainoverlapthreeadditivedocs only. No rebase/forcepush.
Current commits notyetpublished (originalpilothead5dd isremote).

Owner1fullinventory: webui-replacement/owner1/{inventory.md,full-series.txt,
full-final.diff,final-paths.txt,commit-receipt.json}. Completeconsumerfinaldiff
72files1661+/617-; sourcecommit62paths940+/902- (newhelper106lines included).
BothJakubidentitiesnormalNixcommit-F,no declaredhookframework/activehooks.
Allintendedchangescommitted andclean; mainindependentlyreadlog/stat/status/tree,
completewhitespacecheckpassed. No migrations, onefinaldependencyarchive/lock/
Nixstream, no intermediatevendorpins. Priorpublishedmixedpilotstillvisiblein
history thoughobsoleteimplementationabsentfinaltree. Independentwholehistory
judgment REQUIRED; noleadinstructiontoexcuseobsoletehistory. Ifconsolidation
isrequiredidentifyconcretecommits/dispositions, preservepublishedrefs andnote
repoexactrewriteapprovalgate. No historyrewrite/branchreadyclaimauthorizedyet.

Mandatoryreviewallfourlanes, savedreviewer0Sol/xhigh/read_only
thread01a154af-cc09-7422-bff8-fcc87e300be1 verifiedready/purpose/settings.
Readmandatory-change-reviewSKILL andallfourreferences; reviewsourcetest/docs
build/providerpubliccontract andactualconsumer, no nestedagents.
Priorreportretainedoriginalheads; thisnewreviewmustassess changedboundary and
wholebranchhistory/migrations ratherthanrubberstamp. ReportBlocking/Important/
Advisory findings andspecificresidualtestlimits; noauthoritygrant.

Additionalleadacceptance evidence while sourcefrozen: independent read-only
archiveSHA256plusall51regularfilebytes comparedto exactproviderf94Gitblobs,
allmatch. No sourceedit/test/build/repack. Prepared post-review scripts inspected
by lead; no launch until finalreviewaccepted.

INTERIMREVIEWCORRECTION controllingoverearlieroverlapstatements:
finalproductionrangevsfetchedmainb9overlapSIXpaths:WORK_LOG,API_CONTRACTS,
REQUIREMENTS,e2e-type-coverage.json,nodes.test.ts,tsconfig.e2e.json.3-doconly
claim appliedoldpilotrange, notfinalcandidate. Upstreamnodeshelpers/newfetch
fixture/E2Eadoptionsmustbepreserved onanyfutureauthorizedbaseintegration.
ReviewerImportantobsoletepublishedpilotseriesfindingrecorded
review-interim-history.md; nohistoryrewriteauthorized,no readinessclaim.

FINALREVIEWRESULT recordedfinal-review.json: code/contractsacceptedall4lanes,
noBlocking/additionalImportant/Advisorycodefindings; I1Importantwholehistory
outstanding. No sourcefreezechangesduringreview. Owner1subsequentlyreleased
onlyprivateindex/tmpcontentpreview for b9sixoverlapreconciliation; nooriginal
worktree/index/ref/remotechange. Finalhistoryrewriteawaitexactuserpermission
aftermaininspectspreview. Fullverificationhelduntilfinalcandidate.
