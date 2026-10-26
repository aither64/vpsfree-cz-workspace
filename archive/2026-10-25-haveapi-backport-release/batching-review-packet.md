# Representative workload measurement — final review packet

User asked to backport all master fixes and release .2, then explicitly required
new tooling fixes master-first. Master1741 integrated and reviewed. Original
master push timing was inconclusive with high self noise; original evidence kept.
User clarified the goal: enough ordinary requests or complex API descriptions to
catch meaningful regression across request categories, not just documentation;
weekly can be broader/stricter. Rejected10x/1s coarse policy must be absent.

Current owning source master feature/worktree haveapi-master, base
1741a25e1df45f06f9966942d5c34a97967ebb3e. Intended one coherent successor source
commit, no metadata/runtime/pins/migrations. Existing canonical lineage/proof and
unchanged runtime conclusions reusable from master-final-review.md. Latest top
design acceptance/measured shape/weekly supplement authoritative, older sections
historical. Final head/complete series/diff/quick receipt appended before assignment.

Acceptance: baseline-driven common counts target1squick/2sweekly, cap20000,
one bounded adjustment ifbelow750ms/1.5s; both revisions same counts. Cheap
warmups2x100ms outside measurement, expensive baselinecount1/warmup0 symmetric.
Quick3self5pairs4agreement20%, weekly3self7pairs6agreement10%,50msaggregatefloor
normalizedbycount. Existing calibrated allocation bytes/reference unchanged.
Strict deterministic output/auth/work/SQL/allocation/source/input gates remain.
Noise/insufficient evidence labeled diagnostic, not claimed performance pass,
no repeated-workflow-untilgreen loop. Live/replay25-50% controls must detect,
including cheapcallsformerlyhiddenby0.20msfloor;15%quick/weeklythresholdcontrol.

All existing request categories retained. FullRustpages16quick/32weekly,
4actions2samples4parameters,bothadmin/member, fulloutput/auth/lastaction validated.
Measured16admin5.277s/member3.568s,32admin10.956s/member6.959s, substantialMBbody;
64probe23.6/15.2s retaineddiagnostic, no blindlyhuge128run. No repeated full warmup
for expensivecases. Actualhostedjobduration/adequacy/completeinventory required.
Quick+Rust expectedenv reuses existing weeklyexactRustclosure, includesactualRust
manifests/lock/gemspec/loadeddeps; no inventedquickcalibration or pairequality
weakening.30s request/batchworker safety supplementary, setupdistinct; meaningful
failure/source/workloaddiagnostic/ownedterminationreap, avoidperrequestIPC/timer
pollutionofcheaploops/allocations.

Source boundaries existing runner/comparator/focusedtests/workflowminimal/docs.
No new benchmark/calibration/equivalenceframework. Complete final history/stream/
no-migration conclusions required. Sameindependentreviewer0Sol/xhigh,allapplicable
lanes(general,architecture,scope,risk) atHigh; no nestedreview/sourceedits/longtests.
Reconcile docs to actual code/report/exit semantics and insufficientsignal cases.
Only quick checks before committed-source review, then hostedquick+weekly on
master alongside applicablecomponent/buildCI, masterintegration,exact-xbackport,
finalreleasequick+build/packageartifactchecks; no duplicatedbackportweekly.

## Final exact committed gate

Base 1741a25e1df45f06f9966942d5c34a97967ebb3e -> one commit 344351e70f78d8c0dff6ab5ca572e2498ca0906d: performance: measure representative request batches.
11 files,+550/-139; full-index binary diff batching-final-review.diff SHA256 d4cf21375b75b618ce0378d4828f052e590f1ca0dcd4881d59a2d8b98d60dda0.
Clean/index stable,no handles. No obsolete10x policy/fixups/repeated pins/migrations.
102focused pass65.33s; finalaffected24 pass32.7s afterguard/warmup refinement;8Ruby lintclean; normalhooks/messagepass,lines<=80.
Budgets/reference/flake/VERSION/changelog unchanged. Live256op0.829103s->1.217886s caught;cheap30% replay,15%weeklyvsquick.
Controls count1/warmup0symmetry,cheapcommoncounts/100mswarmup/singleadjustment,deadlineIO/reaping,quickRustinputcapture,runawayreplay,newRustallocation/auth.
Retained16/32 actualHTML revalidated193/128/385/256examples/private/Rustmarkers without rerender.
Logs batching-focused-checks.log/result.json,batching-final-affected-reconciled.log,batching-lint-accepted.log,batching-master-commit.log. No hosted push yet.

## Final timeout amendment

Final head 44c53bed31635a07d6ea859fe79047b1d07d35cc,one coherent commit atop 1741a25e1df45f06f9966942d5c34a97967ebb3e,11files+551/-140.
Only prior344351tree delta weeklytimeout30->45 +matchingdoclimit,2files+2/-2.
Full-index diff SHA256 2c4eca2f2d48050269035d2523d709891291121b921f42ea9ab62b584040a64c.
YAMLparses/45weekly10quick inspected,diffcheck/normalhooks/messagepass,clean/nohandles.
Unchangedcode102+24checks apply,no fullsuite rerunfortimeout. Designupdatedaccepted
measuredweeklycost,quickunchanged,no new runtime/dependency/migration change.

## Authoritative final committed head and preparation evidence

Final be520ed8ea8a82b4d1cb719a4066460f110bcf83, one coherent commit atop 1741a25e1df45f06f9966942d5c34a97967ebb3e;15files,+877/-173.
Full-index batching-final-review.diff SHA256 095a9c130f87fa6f8042b571a31f85d5b94327fa2e1c8b0fae90659692dc6db0.
Clean/index stable/no handles. Normalhooks+allmessagehooks pass;9Ruby lintclean.
ActualCampaign/normalizedReleasepreflights1741/fixedb85/published.1/retained.2
allpass,rawtamperreject.43affectedactivation/comparator/lineagepass39.54s;
9finalordinaryWorker.inputs/rawreceipt/missinglock/activationreplaypass2.09s.
Prior102+24batch/live/pagechecks stillvalidunchangedboundaries.
SharedJSON2.21.2bootstrapbeforefirstload,exactroot/server/Rustdevpins,
exactpreparationdelta3Gemfilesonly/raw+normalized+declarationreceipts/replay.
Productiongemspec/budget/flakeunchanged. Leadparagraphapplied/mainproseinspected.
Noobsolete10xpolicy/oldfixups/repeatedpins/migrations. SingledevelopmentJSON
preparationstreamconsolidatedinthiscommit,actualexpectedversionunchanged.
Logsjson-preparation-final-amend.log,preflightsummary/affectedfocusedreceipts.
No push/longCIyet; finalreviewmustbindthishead.
