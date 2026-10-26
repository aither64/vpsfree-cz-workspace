# CI fixes — simplified final review packet

All intended changes committed and quick checks passed; ready for fresh independent final review at the exact range below.

## User scope and superseding decision

User requested root-cause fixes for Ruff/performance CI and authorized HaveAPI/master merge when finished. User then rejected the large utils/performance-env subsystem and accepted reassessment/progress with a conventional smaller solution. Push tests must compare the branch HEAD before push with HEAD being pushed. The rejected08355a22 attempt is retained separately for history, never merged, and its green/failing results do not validate this replacement.

Active contract: top superseding section of design-ci-fixes.md; historical Phase2 below is rejected. Current worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-client-readme-improvements/haveapi-ci-fixes, branch2026-10-26-client-ci-fixes, basecb43ae2367b12e22e602d69312bfd1f7331b4995. Original docs already integrated. Integration approval retained, but no claim until final accepted checks.

## Intended final deliverable

Preserve Ruff exact65a9082ed68cd2546b9a12c69bd9b0ac0b9859b8: devpin0.17.2 aligned nativeNix, exact TOML/package/executable parity check prevents updater drift; existing runtime guard preserved. Rootflake.lock/updater unchanged.

Conventional benchmark setup37520c4d2712df0947f59391903f55736868c25c: only Gemfile30lines, standardlock296lines, smallshell21lines and1applicationlockexception. Third-party dependencies only; no copied HaveAPI/source skeleton, snapshots, native inventories, Nixclosure receipts or proof framework. Actualnewlock5bcd8d2fec2f1a66b5a4981554be90165eb7e739b87a732405bbf64b5147fe66, ordinary frozen install, not claimed identical to historic locks. Small shell pins known oldNix for exact calibratedRuby. Clears inherited Bundler/Ruby injection including RUBYGEMS_GEMDEPS, isolated ownedgems+Rubydefaults.

Minimal existing runner/workflow consumer fca837b7be8913d9f79bc79c2437d25a0f5750ba: same prepared Ruby/gems for both exported sources; existing sourcearchives/manifests/sourceidentity/loadedfile checks. Retain benchmark3files/contenthashes/lock as consumed inputs, contributorflakes as raw sourceprovenance only. Other supported declarations/requirements/JSON and maintenance normalization stay strict. Actual calibratedRuby/full87 loadedgraph required; entirebudget/reference/classifier unchanged. Old replay absent-benchmark path preserved; new evidence uses direct fields in existing structures, no new standalone validation system.

Existing quick pushes use exact eventbefore/after on all branches. Nonancestor force pushes carry a narrow event-bound exception through existing ancestry guards. Newbranchzero-before uses mergebase ofafter and captureddefault. Reject deleted/equal/malformed/noncommit/missingobject pairs, no guessed beforefallback. PR/manual/weekly and provenmaintenance rules otherwise retained. Fixed reference b85ec364057f536940d689b09e612512ffffaf82; budgetSHA57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050 unchanged. Relative and historical absoluteallocation gates remain.

## Review selection and boundaries

Fresh final independent reviewer0, retained gpt-6.1-sol/xhigh/read_only. Verify roster/current identity before assignment. High risk for evidence/replay compatibility and CI source-pair contract: GENERAL, ARCHITECTURE, SCOPE, RISK/COMPATIBILITY; full skill/all4references. Prior rejected-attempt review is historical, not reusable approval of this rewrite. No nestedreviewers, sourceedits/builds/tests/timings/liveCI/refmutations during review.

Assess proportionality expressly: reject recreation of discarded framework; only conventional files/bounded runner changes needed. Whole branch series/finaldiff/repeated-input-stream/history/migration conclusions mandatory. Separate Ruff, shared toolbundle, runnerconsumer logical purposes. No DB/schema migrations; additive evidence fields and changed push-pair semantics need compatibility assessment. Legacy replay stays supported; no application API/state/runtime/deployment change. No benchmarkcalibration/budget/reference change or auto retry/recalibration. No new actionsuses refs.

Owning interfaces/consumers: standard benchmark Gemfile/lock/shell consumed by workflow/localcommands, endpoints runner actual runtime; performance_ci prepares selected exported source roots; comparator owns existing sample replay/classification. No external consumer/pin changes. Techdocs doc/performance.md and PythonCONTRIBUTING; lead prose passes complete. No service rollout or database migration required; reverting restores known explicit environment refusal.

## Quick evidence (finalize on freeze)

Ruff positive isolatedparity build; declared/distribution/native0.17.2;41filesformat/lint; same-helper missing/duplicate/range/malformed/bare/mismatch/badTOML/fakeexe negatives passed; updatercheckorder verified. Exact Ruff unchanged, reuse scope valid.

Conventional environment standardlockprep/frozeninstall<2min;70gems/25directdeps; unchanged lockbeforeafter; Gemfile syntax/Nixparse/RuboCop pass. Ownedhashes/commands/logs artifacts/benchmark-bundle/checks.json. Hooks HaveapiI18n/RuboCop/commitmsg pass. No historical gemspec warning because no copiedgemspecs.

Eventselection owner0:52examples0failures1.05s; syntax/RuboCop/diffpass. Exactbeforeafter,nonancestor,newbranchfallback,invalidpair,unchangedotherselection contracts and Campaign push-event forwarding. artifacts/event-baseline-spec/.

Owner1 final report artifacts/minimal-runner-checks/final-report.md and frozen-inputs.json: one untimed normal-request smoke per14quickworkloads BOTH b85ec364057f536940d689b09e612512ffffaf82/37520c4d2712df0947f59391903f55736868c25c,87actualgems/116sourcefiles/sourcebyteguards pass. Focused48examples47pass+1controlledfixture failure corrected and affected2/0; declarationguard unloadedRake bug fixed to RubyGems installedspec lookup, newrequirement1/0+bothactualsourcepreparation pass; maintenanceinput1/0. Full6fileRuby lint/all7syntax/diff/YAML+10shblocks pass. Initialfailed/zerofilter attempts retained in finalreport, not countedpass. Lead prose accepted. No active checks. No new timed campaign yet. Finalreview after all intendedcommits/quickpasses. Then ONE finalhead hostedquickperformancecampaign+releasebuild, initial15minwatch/reassess, no redundantlocaltiming/automaticweekly/blindretry. Preserve report pass/inconclusive/error distinctions. Any failure diagnosed by owner before further action.

## Final exact history inventory

Exact base/current fresh origin/master cb43ae2367b12e22e602d69312bfd1f7331b4995; exact final head fca837b7be8913d9f79bc79c2437d25a0f5750ba. Ordered complete series:
1.65a9082ed68cd2546b9a12c69bd9b0ac0b9859b8 clients/python: enforce Ruff parity with the Nix environment.
2.37520c4d2712df0947f59391903f55736868c25c conventional benchmark environment.
3.fca837b7be8913d9f79bc79c2437d25a0f5750ba runner/push pairs.

Whole diff17files881insertions/128deletions; project/indexclean; fullrange --check0. Normal required HaveapiI18n/RuboCop/commitmsg hooks passed; Ruff earlier PythonChecks pass. Mandatory80messagewidth respected, advisory72bodywidth only. All intended owner files/inputhashes matched before staging. SSHfetch target unchanged; no rebase. No activecommands/watchers.

Final path inventory: .github/workflows/servers-ruby-performance.yml; .gitignore; clients/python/CONTRIBUTING.md; clients/python/pyproject.toml; doc/performance.md; flake.nix; servers/ruby/benchmarks/{Gemfile,Gemfile.lock,endpoints.rb,performance_compare.rb,shell.nix}; servers/ruby/spec/performance/{comparator_spec.rb,event_baseline_spec.rb,release_lineage_spec.rb,runner_spec.rb}; utils/check-ruff.nix; utils/performance_ci.rb.

No obsolete approaches/fixups/repeated update streams in finalrange. Ruff one intentionalpin0.17.1->0.17.2; toolenvironment one ordinarybenchmarklock+independentoldNixshell, rootcontributorflake.lock unchanged. Three commits independently reviewable logical purposes; supportdocs/specs with owners. Rejected08355a22 is not an ancestor and never claimed merged; retained only separate localref2026-10-26-client-ci-fixes-rejected-performance-env and oldpublishedfeature/historicalCIevidence. utils/performance-env absent. No DB/schema migrations; additive direct toolinput evidence fields preserve oldschema2 replay; changedpushpair semantics intentional. No fix commits released/deployed/merged/externallyconsumed; database provenance inapplicable. Ordinarylibrarylocks remain ignored; sole trackedlock is toolapplicationbundle.

Current remote feature still rejected08355a22; publication held until finalreviewdisposition. Guardedlease publication then cancelonlyactualsupersededactive runs; oldbatchalreadycomplete. One finalhead hostedquickcampaign/release batch next. No claim during verification. Userapproved eventualHaveAPI/master integration after completion/acceptance, no furtherpermission needed. Session staysopen.

## Final-review reconciliation in progress

Reviewer0 reports Important GENERAL+RISK directrun preflight bypass at originalfca837b7: Makefile/doc direct endpointsrun does not call Campaign source Ruby/gemrequirement checks before firstworker. Lead accepted and assigned owner1 bounded sharedvalidation reuse plus no-child regression; no new proof/receipt/framework. Original committed range attribution preserved; fullreport pending. Publicationheld.

## Direct-run review correction accepted

Lead inspected final5file delta and authoritative artifacts/review-direct-preflight/specs.exit=0/specs.log7examples0failures5.27s. Shared existing Performance.gemspec policy owns source specification/subprocess/Ruby/runtime requirements; Campaign delegates with sameError contract; direct CLI checks all3gemspecs in BOTH verified roots before firstchild/pilot. Focused realgemspec tests valid/unsupportedRuby/incompatibledependency on either side+nochild; existingcomposition/push/weeklymaintenance checks pass. Final5filelint/syntax/diffpass; no dependency/runtime/budget/reference/schema/doc changes or repeatedsetup/smoke/timing. Owner report/frozenhashes artifacts/review-direct-preflight/.

Important originalfca837 finding resolved by narrow requested policyreuse; reviewsteps9-10 focusedleadacceptance, no automaticfullrereview. Original report remains fca837. Gitowner3 released owningrunnercommitconsolidation/exactrange-diff, guardedfeaturepublicationoldremote08355a22, then ONEactualexacthead hostedquick/releasebatch viafreshpinnedwatcher(initial15min). Actualforcepushbefore/after must be retained, no guessedmasterbaseline. Priorapprovalsactive, actualmasterclaimmerge helduntilhostedacceptance.

Finalnarrowfix consolidated: correctedhead029f79b31cec93167f07e43e571c36b5f42d5b80/basecb43ae2367b12e22e602d69312bfd1f7331b4995, orderedunchangedRuff65a9082ed68cd2546b9a12c69bd9b0ac0b9859b8/env37520c4d2712df0947f59391903f55736868c25c/runner029f79b31cec93167f07e43e571c36b5f42d5b80. Lead independently inspected artifacts/review-direct-preflight/final-range-diff.txt: only accepted5file sharedpreflight/tests, Ruff/env exact; no new contract or boundary beyond requestedfix.17files955+/135-,clean. Originalreviewfca837attribution preserved; narrowfix accepted persteps9-10. Noobsolete/repeatedstreams/DBmigrations introduced.

Guardedfeaturepush boundoldremote08355a22 succeeded withhooks, freshSSHfeature029f79b3/mastercb43ae23 unchanged. Portalcomparisoncaptured. ActualexactheadpushCI IDs/watch launch pending; noclaim. Firstrebaseattemptrefused becausecommitnotyetsettled, no mutation; ownerverifiedcleancommit/index/norebasestate thensequentialretry succeeded. All known effectsreconciled, no lostchanges.
