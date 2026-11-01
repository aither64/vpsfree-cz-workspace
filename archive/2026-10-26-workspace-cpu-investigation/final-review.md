# Independent final runtime review

Reviewer0 report received2026-10-26;persisted by lead because reviewer read-only.
Reviewer verified exact dev-session current;both shellmarkers absent and trusted
threadbinding exact. Retained reviewer0,purpose review,read_only,
**gpt-6.1-sol/xhigh**,unchanged;no fallback/nestedreviewer.

Exact repository repos/dev-workspace.git;worktree worktrees/2026-10-26-workspace-cpu-investigation/dev-workspace.
Base **7e6d7c9cdb3388ab7abc720c034c15c21afbd686**,head
**74df2ed3868d953bea2eeea9d2af0f717d29622d**. Base confirmedmerge-base,
headmatched,tree/indexclean at reviewstart/end. Fullhistory/finaldiff,changed
source/tests/docs+adjacentauthorities inspected. No edits,tests,builds,deploys,
Gitmutations,lifecycleactions. Suppliedquickevidence notreviewerreruns.

Risk **High**:scheduler/retryadmission/host+lifecycle behavior. All4lanes applied
from fullyread mandatory-change-review/general/architecture/scope/riskrefs plus
workspace/projectguidance. Compare actualusergoal/scope/time/diff beforedetails.

## Findings

1. **Important — benchmark warm-up/active workload outruns real scheduler.**
   Commit69c45ad5b71a0eecb06bd782d5260a910b26a838,
   portal/internal/web/cpu_benchmark_test.go:391 (also98-107,371-387,421-423;
   turn_retry.go90-105,174-185). Default120conversations,real2workers/2buffer,
   traversalstopsfirstfullqueue/1stick.10swarmupdoesnotproveallsettled.
   Same-rootversions every5s cancoalescebeforeObserve;expectedreactionperversion
   canfailcorrectbaseline/candidate,andcandidateidleincludesfirstsettlement.
   Fix observedcompletecoveragewarmup andpaceoneoutstandingreaction(or equally
   smallsupportedworkload),sameinputsbothrevisions,honestdurations. Leadaccepted
   androutedimplementer3. Latereditsnotreviewed. Verifydirectfix+representative
   fixturebehaviorbeforetimedcampaign. No newbenchmarksubsystemneeded.
2. **Advisory — deadline test changes state rather than time-only invalidation.**
   Commit74df2ed3868d953bea2eeea9d2af0f717d29622d,
   turn_retry_idle_test.go252-259.SavingDeadlineMS1changesstatedigest,sofull
   admissionoccurs eveniftimeguardremoved. Productionguardturn_retry_idle.go69-71
   correctbyinspection. Addmatchingfuturedeadlinetoken,keepstate/policy/observation
   bytesunchanged,advanceonlyprobetimeandassertfulladmissionresumes. Existing
   controllertestsownactualdispatch. Coveragegap,notproductiondefect.

**No Blocking findings. No further Important production,authority,security,
architecture or scope findings identified in this reviewed range.**

## Scope/history/migration conclusions

ThreeboundedCPUoptimizations+meaningfultests+controlledexperimentmatchaccepted
scope.18files+2677/-42,mostlytests/fixture. No generalizedscheduler/monitor,
persistentindex,broadrecovery/catalogrefactor,unrelateddependencychanges.
Benchmarkcorrectionnecessarycredibleevidence,notoptionalhardening.

Completeindependentlyreviewedseries:
- f5ebb144330c30ea535d4e09a045db6db07fc65b:displaycache,owntests/docs.
- 24f8870a0f9b2dcb871c8bc717424ec1906da817:coordinatorselection,owntests/docs.
- 69c45ad5b71a0eecb06bd782d5260a910b26a838:separatefixture/methodology.
- 74df2ed3868d953bea2eeea9d2af0f717d29622d:settledretryhint,owntests/docs.

Eachcoherentindependentpurpose. **No obsoleteunmergedapproaches,fixuphistory,
abandonedcompatibilitypaths ortransitionalbehavior inexactrange. No migrations**:
no schema/persistentformats;no migrationmerge/release/deploy/externaluselineage.
**No repeated dependency/channel/input/generatedartifactstreams**;nopins/locks.
Foldlaterdirectfixesintoowningunmergedcommits;leadinspectfinalseries/equivalence
under narrowfixrule. Consumerpins outside thisreport;lateraffectedrange/history
assessmentrequired,samereviewer.

## Technical conclusions

- Coordinator validatedinventoryafteruncertaintyreconcile;ownerorder,candidate
  claims/notices/allnonterminaljobs/nojobbackground/dueevents/completedreminders
  covered. Freshgeneration/retainedowner/fence/sessionadmission remain;claimedjobs
  freshlyreadinsideadmission,newnoticesfreshchecked,blockedownersisolated,wake+5s
  fallback retained. Candidate/dispatcherpredicate duplicationboundedandtested;
  noextraframework/extractionrequired.
- RetryfreshReadTurnState(nonactivitycache),exactstate/policy/session/runtime/
  roster/incarnation/socketbinding. Missingproof=>fullpath,malformed=>error;
  uncertaintyreceipt-onlyreconciliationbeforeexecutionholds. Admissionunchanged.
  In-stepcheckpointcapturecannotcertifylaterunlockedmanualstate,discardson
  failure/dispatch,livepruning/restartloseshints. Time-onlycoveragegapabove.
- Displayidenticalscopeonly,entry/bytes/flightbounds,2scompletionTTL,freshprofile/
  sessionproof,invalidatedflightfences,503refreshfailure,independentwaiters,
  processgroupcancel/joins. Successfulordinary/supervisedlifecycleinvalidates.
  Cachebytesneverauthorizeactions.
- Genericproviderdev-workspace;workspace/configconsumercontextinspected,noAPI/
  nativeprotocol/Nixoption/persistentrecord/extensioncontractchanges. Consumer
  mechanicalpinsnotreviewedyet. Restartdiscardsoptimizationssafely,existing
  forwardrecoverycontractsretained,nocoordinatednodeupdate,nodoDeployment.
- Owningdocsproperlastinglocations;benchmarkdisclosessyntheticnative/admission
  seams,excludeddaemon/activity/browserwork,wholecgrouphelperaccounting. Those
  limitsmustaccompanyperformanceclaims.

## Verification evidence and limits

Reviewerinspectedmeaningfulrealstores/controller/admission/status/coordinator
coverage:1/10/100idleownersvalid>3MiBledger,candidates/completed/bootstrap/nojob,
freshgeneration/incarnation/fence/suspension,notices/fairness/malformed;120threads
60faketicks7200observations/zeroadditionalidleauthority;bootstrap/policy/checkpoint/
manual/socket/retirement/acceptedcounts/disabledcancelleduncertainty;cachefanout/
TTL/identity/errors/invalidation/cancelchildren/capacity/supervisedcases.

PacketreportsfocusedRuby18tests133assertions,retry/web/cache/nav/lifecycle,
syntax/format/diffpass,and1root/1memberfixturevalidate. Thatquickfixturedoesnot
exerciserepresentativescaletimedworkload;hencefinding1. Longpackage/integration,
representativebaseline/candidateanddeployedhealth/continuity/CPUremainunrun.
No measuredspeedup/deploymentreadinessestablishedbyreview.

Disposition:finalindependentreviewcompleteforexactoriginalrange;Important1
awaitsacceptedfix/verification,Advisory2recorded+routed. No fullrerunrequired
forrequestednarrowcorrections;newmechanisms/contractsrequireaffectedlanereview.
Reviewgrantsnomerge/deploy/lifecyclepermission.

Session:https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/

## Independent final consolidated-history conclusion — PASS

Reviewer0 reverified session and retained Sol/xhigh/read-only settings. Independently
inspected complete final7e6d7c9c..31157faf series,parents,per-commit paths,final
diffstat/path inventory,history receipt and fresh old/new range-diffs. Base is
merge-base,HEAD exact,checkout/index clean. Four coherent commits:unchanged
f5cache/24coordinator,a006benchmark with4201fix,31157retry withdd2test.

Independently confirmed4201 andd0a77c18 exacttree144380422aad17c46b0150a4e565bcd06bc0a4b6;
finaltree03e9f52e1c77442ce41ef1a240976b990a75cc3b differs only by explicit
one-off/ordinaryCI-skip/neverroutine opening paragraph. No standalonefixes left.
**No obsolete unmerged approaches,superseded behavior,fixup/tidy history or
transitional migrations. No migrations/persistent-format/schema changes. No
repeated dependency/channel/input/generated streams or pins. Appropriate commit
split;no further consolidation.** No new findings.
Preserve original code assessment+lead narrowfix acceptance;no unchanged-source
review/fixrerun,timed result,consumer review,deployment or integration permission
claimed by this limited gate. Ready for planned post-review checks.

## Independent refreshed final history/equivalence — PASS

Reviewer0Sol/xhigh/read-only independently checked d2099c62656bc2a36c306918a92832ba1e1a0cc0..0fd31c1fa8858ef15d516e58c883f8dea9aa727e.
Cleanexacthead/mergebase,SSHfeature/masterproof. Fourlogicalcommits
deec3201cache,627060cdcoordinator,090e6379benchmark,0fd31retry.
31157..217fixture-onlydelta;217==f813exacttree0ddf3cdf7750de53792947c46fa92c763b3e5d4e.
Repairfoldsintocoordinator,nofixcommitleft. Freshf813→0fd31range-diffall4'=';
orderedstablepatchIDs EXACT:
adccaaaa47763038517878ff76f8c302a180a293
14cacbbd788cb0396698b8554566e89178df1e61
4d8f0cea8decf820e14489bcfb79369484a2a086
71f332e3b10913bf0da0f1cb5d648ba24cf71eb3
Alreadymergedbaselineadvanceonlyattentiontitles,noinput/migrationchange.
**No obsolete/superseded/fixuphistory/transitionalmigrations;no migrations;
no repeateddependency/channel/input/generatedstreams,pins.** Appropriate4commits.
Originalsourceassessment+narrowfixacceptanceretained;changedfullbaselineneeds
exactfinalchecks,notoldverificationreuse. Consumerpinsseparateunreviewed.
No fullsource/tests/build/rerun/deploy/integrationpermissionbyhistorygate.


## Final refresh assessment (reviewer0)

PASS, no new findings. Retained reviewer0 gpt-6.1-sol/xhigh, read-only,
verified bound session; no tests/builds/source edits or unchanged CPU rereview.
Independent exact ranges:

- Runtime deed45f04fc0698b2f2f408b2816ac124913d582..f23e717c2fa33803d889414b243591c9a97846d6.
- Workspace83282a493a6961d352b8ad0e2dfa3b17624fd46c..4dbe8687964a51e8a9cb8171c60de2210e272bc9.
- Configurationcba1f93fcf2d0c2be35d4fb3dd868ba537c38656..7b3fa628622f193a0374564eb96079969741420c.

Reviewer independently inspected histories/parents/diff inventories, exact clean
HEADs/merge bases, receipts and fresh SSH defaults/feature refs. Four runtime
range-diff pairs equal d209..0fd31; ordered stable patch IDs independently match
adccaaaa47763038517878ff76f8c302a180a293 /
14cacbbd788cb0396698b8554566e89178df1e61 /
4d8f0cea8decf820e14489bcfb79369484a2a086 /
71f332e3b10913bf0da0f1cb5d648ba24cf71eb3. Flake lock byte-identical.
19-path CPU inventory remains +2772/-44. No new mechanism.

The only upstream runtime delta is the merged/live archive-permission repair,
14 paths with zero intersection with CPU files. It temporarily adjusts verified
lifecycle directory access, restores surviving modes and reconciles owner-write
against existing legacy snapshots. No scheduler/retry/native/cache/dependency or
schema/journal/recovery-format changes. Retaining deed preserves live behavior.
No additional source-review lane required; this is not a full audit of upstream.

Independent full consumer graph comparisons preserve 35/64 nodes and every
edge/follows/root/sibling/extension field except intended runtime identity and
workspace exact original rev. Both select f23e717c, NAR
sha256-ApfVPQlt0X9XfcjG20Tx31rcb5HOwLwKDlqGly/mxaM=,
lastModified1793050724. Full effective runtime graphs match (projection SHA256
4c0460ad58ff283d1863f0d6cb92795abf9e0edfcdf9ff2195672e077c3bc352).
Lock SHA256 workspace4d0bd26ad018c44532c938117e979dcad145dbcc3a7ef89f834feadd616e8c5c,
config921b557e235073cab5369f849a9793bb26326b8a7df34ea042aefc7fc50887e2.
One pin commit per consumer, correct generated four-commit changelog.

Explicit final conclusions: NO obsolete unmerged approaches, standalone fixes,
superseded pin commits or transitional behavior; NO migrations/schema/persistent
format changes; NO repeated update streams. Provenance refs retain earlier
never-deployed CPU heads; merged deployed deed is appropriately an ancestor.
Original review/narrow-fix acceptances remain. Benchmark d209..0fd31 measures
that exact source pair and unchanged CPU patches, not directly f23. No full matrix
rerun required solely for disjoint lifecycle refresh. Exact-final-head checks,
builds/deployment and integration remain separate. No lifecycle authorization.


## Final archive fixture correction review (reviewer0)

PASS, no findings. Saved gpt-6.1-sol/xhigh/read_only, exactboundidentity verified;
no unchangedCPUreview/tests/builds/sourceedits/nestedreviewers. Exact reviewed
f23e717c2fa33803d889414b243591c9a97846d6..fffbd0d59fffc09667cb39878d9f7da8bdcd3806,
cleanHEAD, onecommit/twofiles+54/-1. General andaffectedstorage/lifecyclerisk.
Reviewerinspectedactualdiff,adjacentstorage/command/helpercontracts,fixturestate
setup, fullCIcauseexcerpts/runidentity. Directrequire-idle nowselectsexisting
/home/developer/.local/state/dev-workspaces matching portalSQLite/socket hash.
Explicit emptyroot previouslyselectedlegacyJSON, notenvironmentfallback. Parser,
admission, timeout, productionlogic/interfaces/formatsunchanged.

Regressionusesrealclient/command/PrepareSend/DiscardPreparedSend withestablished
nativemetadatafixture. Unselectedhelperreproducesfenceerror; correctrootrefuses
currentunresolvedreceipt; exactdiscardthenprovesidle. Meaningfulwrongledger
falsesuccesscoverage,noframework/speculativecompatibility. FailedCI40406137477
provesprebrowserstorageidentityfault; notcauseofearlierlocalhydrationtimeout.

Full deed..fff fivecommitseriesindependentlyinspected. FourCPUcommitsunchanged
exactancestors; separatefifthtestfixrepairsbasefixtureandimprovesreviewability.
NOobsoletehistory/abandonedpaths/transitionalbehavior; NO migrations/schema/
persistentformatchanges; NO repeateddependency/channel/inputstreams. Existing
JSON→SQLite fenceisexercised,notintroduced. Consumerrefreshseparatepending.
Quickowner2tests/Nixparse/diffappropriate; targetedexactarchiveverification
remains. Retainoriginalreviews/benchmarksourcebounds. No deploy/merge/lifecycle
authorizationgrantedbyreview. Leadacceptsboundedfix/review; singleCIobservationnext.
