# Performance correction integrated — master CI snapshot

HaveAPI/master and retained feature are exact reviewed
`4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`. Normal fast-forward/SSH push and
remote proof passed; claim release was verified before this inventory.
[Integration receipt and exact-head runs](performance-response-integration-result.json).

One bounded master/push snapshot: seven successes, three active workflows:

- [Rust 40547615521](https://github.com/vpsfreecz/haveapi/actions/runs/40547615521)
- [Server RSpec 40547615785](https://github.com/vpsfreecz/haveapi/actions/runs/40547615785)
- [Performance 40547615707](https://github.com/vpsfreecz/haveapi/actions/runs/40547615707)

No failure observed, no waiting/rerun/dispatch/cancellation campaign. The completed
feature CI below remains separate evidence; no master timing result is inferred.
Older vpsAdmin master `40531100170` and feature `40529944536` broad CI were still
in progress at the latest read, with exact `08c3bd7e` push identity unchanged.

## Completed feature verification before integration

# Performance policy correction — final feature CI

All ten push workflows passed at exact feature head
`4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c` on the session branch. No manual
rerun, dispatch or cancellation occurred. The bounded monitor is finished.

Performance run
[40542087398](https://github.com/vpsfreecz/haveapi/actions/runs/40542087398)
returned COMPARED, measured pass for genuine `18b45aed..4d36efcf`: all 14 cases,
28 wall/CPU classifications, 14 allocation gates and 14 correctness checks pass.
No inconclusive/no-work result. The unchanged budget hash is `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`.
The report binds policy `per-revision-response-stability-v1`, comparator
`163e7bbec7725d784e72677456238ada5264adec8c2c8dda9caa83ccd7fd5267`, and exact
sample input `0c319019db2742554854ed301c2f4d01d63904ded5d10e4697a3db598d63bc8b`.
[Final result and run inventory](performance-response-feature-ci-result.json).

Separately, one postreview reanalysis of retained original master-run samples
passed all 14 cases with the same timing/allocation limits. Four HTML responses
changed by 12 bytes; OPTIONS serialization changed with equal canonical content
and zero byte delta. This was not a new measurement. Original run `40529570313`
and its failed report remain unchanged. [Replay evidence](performance-response-replay-result.json).

The new feature is ready, awaiting separate HaveAPI/master merge approval.

## Previous integration checkpoint

# Integrated default heads — 2026-10-27

Allfive remote defaults verified equal their final feature heads, all claims
released. HaveAPI/master18b45aed, vpsAdmin/master08c3bd7e, Go/master73f164dd,
Rust/main80be1c1a, TypeScript/main149c72f1. [Remote proof](integration-remote-verification.json).
VpsAdmin rebase over disjoint WebUI dependency update is independently certified
patch-equivalent; capture provenance and TS source pin unchanged.

- HaveAPI10workflowsSUCCESS; release40529570376 publishSKIPPED.
- HaveAPIperformance40529570313FAILED on actual029f79b->18b45aed integrationpair:
  ContractErrorexit3, fourHTMLidentities differonlyintentional12byteSDKprose.
  Other10identities/all14counters/environment/fixture/dependencycompat match.
  No timing classification/pass/regression conclusion. Artifact12745607977,
  reportSHA6db05c94dd2a9bee3ba708abbae987c80b4b513ddf67964a913483259159ece7.
  Actual logs/reports/ZIP/sample proof retained at master-performance-diagnosis
  prefix in/tmp. No rerun/ancestor/comparator/baseline/budget/ref manipulation.
- Rust/main40530562211SUCCESS all4jobs.
- TS/main40531930677SUCCESS build/publishSKIPPED.
- Go no configured workflows; bounded defaultpush inventory0.
- VpsAdmin/master40531100501lintSUCCESS,40531100170 broadselectedci-taggedtests
  stillIN_PROGRESS at exact08c3/master/push. Feature08c3broad40529944536alsoactive;
  its lint/i18n/WebUI passed. No duplicates manually triggered or cancelled.

All feature/source checks and final reviews retain their recorded exact scope;
new masterpair performance is honestly failed, no earlierpair substitution.
No package release/version/tag/registry/deployment/lifecycle action occurred.
Remaining follow-up is CI assessment; all requested merges are complete.

## Prior member-focused documentation checkpoint

# Member-focused README final CI

Finalfeatureheads published/clean/defaultsunchanged: Go73f164dd5eeebfc494705ae27981d30872fa88c3
(no workflows/onebounded inventory0), Rust80be1c1a90b7009f8ddecf6a7fe042b506de8b42,
TS149c72f11acef67224a47ed77711a3abb805fbd4.
[Rust40526005081](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/40526005081)
completedSUCCESS all4jobs.
[TS40526154339](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40526154339)
completedSUCCESS build/publishSKIPPED. Both exactownedbranch/push/head.
No failedchecks/reruns/dispatch/cancellations/default/release/deployment.
Proseonlycorrection: all45fences/38compiledexamples unchanged, no redundantlocaltest.
Independentfinalgeneralreview has nofindings; [review](vps-readme-member-focus-review.md).
Finalsnapshots `/tmp/2026-10-26-typescript-client-generation-member-focus-{rust,typescript}-ci.json`;
publicationreceipt under readme-editorial prefix. Disclosedboundedparentfallback
because nativeutilitylaunch unavailable. No API/VPSaction or actualrelease.

## Prior lifecycle checkpoint

# VPS lifecycle README final CI

Allthree featureheads are published/clean with unchanged default branches:
Go51b86a59dc378eab1d84249094e27c80bdaf4d08 (no workflows/inventory0),
Rust020f4ddb229d7892c76cf10e89ee7a792fddf9ad and
TSa8966789bd24914daebd9fc0e33a51f76480c4ba.
[Rust40523070025](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/40523070025)
completed SUCCESS (regeneration,async,blocking,MSRV allsuccessful).
[TS40523115572](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40523115572)
completed SUCCESS; protected publish skipped. Both exact ownedbranch/push/head.
No reruns/dispatches/cancellations or actualrelease/API/VPS action/defaultmerge.
All38 exact final fences compiled before independent final documentation/history
review, which passed without findings. [Review](vps-lifecycle-readme-review.md),
[packet](vps-lifecycle-readme-review-packet.md), [state](state.md).
Native watcher tools unavailable; disclosed bounded parent fallback collected
final snapshots `/tmp/2026-10-26-typescript-client-generation-lifecycle-{rust,ts}-ci.json`.
No new local campaign or changed runtime/generated/release inputs.

## Prior README alignment checkpoint

# Generated-client README final CI

All three README feature branches are published and clean. Go
`bb1bc9622fff5a95b9c922c5b419949235a0305f` has no configured workflows;
its one bounded branch inventory returned zero runs. Rust
`2aad8d47c68d53ce1cb7e8669e083f96dc868a8c` passed
[Rust client40516988544](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/40516988544).
TypeScript `e116b3e87ce73386b64d8291cffa1f24bb38b718` passed
[Package validation and release40516963287](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40516963287);
its publish job was skipped. Both are push events on the exact owned branch/head.
No release, workflow rerun/dispatch/cancellation, default integration or deployment.

Before final review all13 exact README code fences compiled without execution/API
calls. Independent general documentation/history review completed; its sole Go
wording Advisory is closed by narrow owning amend and unchanged-fence proof.
See [review](vps-client-readme-review.md), [closure](vps-client-readme-disposition.md)
and [state](state.md). Parent bounded CI fallback was disclosed after native
watcher tools became unavailable; no repeat local integration campaign.
Final raw snapshots retained under `/tmp/2026-10-26-typescript-client-generation-readme-rust-ci.json`
and `/tmp/2026-10-26-typescript-client-generation-readme-ts-final-ci.json`.

## Prior generator/release CI checkpoint

# Corrected final heads

HaveAPI18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875 and SDK2dab582881c4af8d8b3f932d9f2308e133d8d925 are published. Both exactleasedpushes/freshSSHdefaultandcleantrackingproofpassed; defaultsunchanged. No staleactivejobs/cancellations. OnefreshLuna/lowoperationowns:

| Repository | Workflow | Run |
| --- | --- | --- |
| HaveAPI | clients/python |40405397908 |
| HaveAPI | release |40405397909 |
| HaveAPI | servers/ruby RSpec |40405397984 |
| HaveAPI | servers/ruby performance |40405397920 |
| HaveAPI | i18n health |40405397936 |
| HaveAPI | RuboCop |40405397950 |
| SDK | Package validation and release |40405727027 |

All eventpush/ownedfeaturebranch, exactheadsabove. AllsevenfinalrunscompletedSUCCESS at exacthead/event. HaveAPIrelease40405397909 and SDK40405727027 protectedpublishjobsSKIPPED. Performance40405397920 completedCOMPARED/measuredPASS: genuinepairf02eca2->18b45aed,14caseclassificationspass/zeroinconclusiveorregression, runnerexit0, workflow6m55s/comparison6m46s. Artifact12691397431 SHA61982acd05af478b34a6db2796a67743edae5ba2ac95728314e0c53a1c1052ec; actualreportSHAf429687aa225f41ccf9249a0fc816638a5122faaef5d5fd82661b5154e115c76. Parentreadactualselection/report and confirmedexactSHAs/14pass classifications, relevanttrue, onlyMakefile+releasespecchanged. Harness33da812806d8a946a3681a8df6bb786d5be213aa637b1baa94248ca3ef34c42f/budget57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050, calibrationenvironmentweekly. NewrunsfollowdiagnosednarrowBundlerisolationfix/full213Ruby+6PythonPASS, notblindrerun. SDKsource differs onlyexactproducerrevision, initial/releaseexpectedtreesindependentlyreconstructed; allactualartifactinputsunchanged. The firstcorrectedCIutility stopped beforequeries because ambientghwasmissing; parentprovedpreparedrepositoryNixghworks and made oneboundedparallelstatusread. FreshLuna/lowutilitycompletedremainingperformance via explicitNixghprefix and bothprotectedpublishskipproofs; terminal/noactiveoperations. Evidence retained withoutdeletion. Logs/resultsprefix /tmp/2026-10-26-typescript-client-generation-corrected-performance; incompleteoriginalutilityresult retained at release-corrected-ci prefix. No test/workflowretry. No actualrelease/version/tag/registrysettings/upload/default/deploy/lifecycle.

## Prior release-preparation checkpoint

# Final release-preparation CI

Published exactHaveAPIf02eca2e96d9fa6db6e8cb22a4f1fca7092c5ade and SDK6fc0955fc078f3af3ef69adaaec30d5038eff70d. FreshSSHfeature/default/cleantrackingproof passed with exactleases; defaults unchanged. Complete5/2/1finalreview and R1/R2narrowclosure accepted; both newpostreviewartifactstages passed4.2s+10s, including positivefullarchiveconsumer. No version/tag/release/registrysettings/upload/deploy/lifecycle.

One fresh retained-policy Luna/low operation owns these fixed push-event runs on branch2026-10-26-typescript-client-generation:

| Repository | Workflow | Run |
| --- | --- | --- |
| HaveAPI | i18n health |40403389685 |
| HaveAPI | RuboCop |40403389687 |
| HaveAPI | clients/python |40403389461 |
| HaveAPI | servers/ruby RSpec |40403389778 |
| HaveAPI | release |40403389950 |
| HaveAPI | servers/ruby performance |40403389598 |
| SDK | Package validation and release |40403652603 |

SDK40403652603passed withpublishSKIPPED. HaveAPIi18n/RuboCop/Python/RubyRSpecpassed. Release40403389950failed in Test/build:1failure/213examples, version-lockdiff expectation mentions TS0.30.0 vs fixture999.0.0; owner0ownsdiagnosis/fixbeforeanyretry. ProtectedpublishSKIPPED/noartifactretained. Performance40403389598completedSUCCESS/COMPARED: genuinee6d4f797->f02eca2pair, quick/relevanttrue,7m33s, all14cases timing/correctness/allocationPASS, runnerexit0. Artifact12690925828 SHAe0b3795379fb591f2d1a8d4d4f79eb8f02a9a6247d5034ba4f69474f20176029; reportSHA5fdfac2e3fa544309610f35d898e3c525c6c875806552a01aedf95db905425d7. Originalartifact/compactresult retained in release-final-ci directory; utilityterminal/noactiveoperations. Performanceactualeventpair e6d4f797fc92090fff265585196970e6b017003f -> f02eca2e96d9fa6db6e8cb22a4f1fca7092c5ade; preserveactualCOMPARED/NO_WORK/inconclusive distinction. No supersededactivejobs/cancellation, no workflowsmanuallytriggered/rerun. Logs/status/result use /tmp/2026-10-26-typescript-client-generation-release-final-ci prefix. Prior intentional12byteHTMLidentityfailure below remainsfailed, never relabeledmeasurement.

## Prior unified-generator checkpoint

# Current unified-generator CI

HaveAPI `e6d4f797fc92090fff265585196970e6b017003f` and client `50a9602cbc30ca0c18ace092ad9750439e9cf82a` are published. Fresh SSH proofs show unchanged defaults, clean tracking and exact reviewed heads. Client has no configured workflows. All four postreview runtime/package checks passed; [acceptance](unified-postreview-results.md).

The 11 exact HaveAPI push runs, all created2026-10-26T20:28:23Z, are under one fresh Luna/low utility `unified_final_ci`:

| Workflow | Run |
| --- | --- |
| servers/ruby performance | 40395934496 |
| clients/go RSpec | 40395934955 |
| clients/ruby RSpec | 40395934730 |
| release | 40395934499 |
| RuboCop | 40395934556 |
| clients/rust | 40395934489 |
| clients/php PHPUnit | 40395934585 |
| clients/js tests | 40395934486 |
| servers/ruby RSpec | 40395934655 |
| i18n health | 40395934473 |
| clients/python | 40395934566 |

No superseded same-branch queued/in-progress runs existed, so no cancellation occurred. No manual workflow/retry/publication action. All 11 runs are terminal. Ten succeeded, including release validation/build/artifact retention; protected publishing was skipped. Performance40395934496 failed after7m13s: `HaveAPI::Performance::ContractError: Response identity differs between operations/revisions`, runner exit3. Exact quick push pair `fae5508aca9def6b1388d298aab898b0b9ce832c -> e6d4f797fc92090fff265585196970e6b017003f`; no measured pass/NO_WORK. Original artifact `performance-40395934496-1`, ID12686064128, retained with logs/status at `/tmp/2026-10-26-typescript-client-generation-unified-final-ci/`. Owner1 owns diagnosis before any retry. Fresh watcher terminal; no active operation/cancellation/retry. The unchanged vpsAdmin integration run40330622527 passed at7456c7eaae11cee0c76a984b1386a94656510f88; all its workflows passed.

Diagnosis: retained samples show only the12byte unconditional HTML introduction difference across all4HTML workloads and all5ABpairs; no TypeScript profile was enabled. API/OPTIONS response identities are unchanged. Architect/lead retained the already reviewed generic sentence because it describes supported SDKs, not enabled profiles. The proposed conditional-copy patch was reversed exactly before commit; sources equal e6d4HEAD and index untouched. The original failed run remains an intentional documentation identity change with no measured result. Next genuine e6d4->releaseworkflowcandidate push receives normal exactpairCI; no ancestor substitution, ref manipulation or benchmark/comparator/budget/reference change. No retry has been launched.

## Earlier checkpoints

# CI checkpoint before modular output follow-up

HaveAPI published head `dcbd537f325ce4b8a8d0afb1a398763260806c87` passed all 11 push workflows. Full release validation/build passed; protected publication was skipped. Client published head `33bc6f9e1daa08539f3f3aeec5a4b542e2c5f49d` pins that exact provider and has no configured workflows. Both remote feature refs/defaults were freshly verified after exact-leased pushes; defaults unchanged.

Performance run [40358420413](https://github.com/vpsfreecz/haveapi/actions/runs/40358420413), attempt1, completed success. Actual outcome COMPARED, measured pass:14 cases,28 wall/CPU classifications,14 correctness and14 allocation gates all pass; pilots adequate/uncapped and16 validated samples per case. Actual nonancestor event pair `73115aa5e66c5bebdc3150fff27e6054ff0c4271 -> dcbd537f325ce4b8a8d0afb1a398763260806c87`; captured master 029f79b, quick profile, relevant=true. No timing-inconclusive/no-work result or speedup claim.

Frozen benchmark Gemfile SHA256 `eaca394cd1b4b5d05dfc2b95d40bf3d75a42ca058a952cc51d0833b21c7534b4`; lock `5bcd8d2fec2f1a66b5a4981554be90165eb7e739b87a732405bbf64b5147fe66`; shell `fd42593a40e09298b73e31f848cc13d38a3447fbae2f09cd7279548dc4748cef`. Baseline/candidate representative workers used identical Ruby3.4.11 and87 activated gem identities, same frozen lock, calibrated environment. All 9 retained input hashes match the candidate; normalized dependency configs/gemspec declarations equal. Nix-shell warned that it could not resolve <nixpkgs> for bashInteractive and used environment bash; recorded benchmark Ruby/dependency/input graph and measured gates passed. No warning suppression/rerun.

Immutable artifact 12666822745, `performance-40358420413-1`, 11,465,616 bytes, API/downloadSHA256 `5f15d6aa95227c19346c99acbaa15acc04bf0af3c0d3cae3e5b2f1e7fec53c1a`. Bounded receipts under `/tmp/2026-10-26-typescript-client-generation-refreshed-performance/`; only <150 KB extracted, source/raw samples left unexpanded. selectionSHA256 `2d971ac2960667d09c722597b83e64228c2698c46844510731792de76535b59f`; report `868162577608ca5f6dd004934c7b78ca4fff3ea9a5962bcc08cc1567b4bebd32`; dependency `c320e7cd3c63125c485e619343a239e09f9a46625db621320754435bfebb4daa`.

vpsAdmin final 7456c7eaa API/lint/i18n/PHPUnit passed; broad integration run 40330622527 remains active under existing utility. Source unchanged. New user-requested resource/action module follow-up begins after this checkpoint; these results certify previous code/inputs and do not replace its required checks/review.

## Modular output final heads

Final HaveAPI `2f2daf625672b3d5c11067538a7250acd70d63d5` and client `ddfe79a1d0d0e5a8d6e77eb4ab4bf136052c9284` were independently reviewed with no findings and passed new postreview published-runtime wire/extracted-package checks in44.09seconds. Both feature refs were published with exact prior-head leases; defaults unchanged. All3selected HaveAPI workflows passed: performance40366764293, i18n40366764623 and RuboCop40366764318.

Performance40366764293 explicitly returned **NO_WORK**, not a measured pass: exactpushpair `dcbd537f325ce4b8a8d0afb1a398763260806c87 -> 2f2daf625672b3d5c11067538a7250acd70d63d5`, RELEVANT=false, reason “No relevant source changes; immutable event resolution passed.” Candidate/build/benchmark steps skipped and the explicit no-work gate succeeded. Compact receipt `/tmp/2026-10-26-typescript-client-generation-modules-ci-receipt/receipt.json`, boundedselectionlog~1.4KB. No benchmark rerun or artifact expansion.

Release failure diagnosis: the expected999.0.0 TypeScript lock transition is correct. The Makefile TS local-lock command overrides BUNDLE_GEMFILE while inheriting BUNDLE_LOCKFILE from outer Bundler4, so Bundler targets the rootlock. Existing Rust command already clears that variable. Owner0 owns the narrow equivalent TS isolation fix plus exactversionregression; no expectation weakening/CIretry.
