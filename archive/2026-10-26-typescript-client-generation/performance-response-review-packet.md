# Final review: performance comparison across changed responses

User explicitly approved simplified plan: content differing BETWEEN revisions must never itself fail or skip performance comparison; userselectedKEEPexistingtiming+allocationlimits. Goal timingperformance, no newresponse-contract/approvalframework. AcceptedTOP design.md brief is authoritative and supersedesearlierhelper/schema3proposal.

Final committed HaveAPI-only range `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875..4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`; tree `1cab0cbb36d28270c16d3e115813b689186f95b8`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-typescript-client-generation/haveapi` clean. This is ONE NEW commit after previousfivecommitsalreadymerged; do not re-review/rewrite those historicaldefaultcommits.

```text
4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c servers/ruby: compare performance across changed responses
```

Fullfinaldiffstat:

```text
doc/agent-instructions/development.md              |   4 +-
 doc/performance.md                                 |  54 ++++++++---
 servers/ruby/benchmarks/endpoints.rb               |  19 +++-
 servers/ruby/benchmarks/performance_compare.rb     |  43 ++++++---
 servers/ruby/spec/performance/comparator_spec.rb   | 105 +++++++++++++++++++--
 .../ruby/spec/performance/event_baseline_spec.rb   |  30 ++++--
 servers/ruby/spec/performance/runner_spec.rb       |   5 +
 utils/performance_ci.rb                            |  21 +++++
 8 files changed, 238 insertions(+), 43 deletions(-)
```

## Accepted behavior and boundary

- Existingcanonicalresponse/occurrence-totalstability is keyedbyactualverifiedobservationSHA; bothAAself-paircolumns belongbaseline. No one-raw-body/newrawdeterminism rule.
- Crossrevisionraw+canonicalchanges andAB-onlyoccurrenceweightedbytes/request+signedbyte/percentdeltas arediagnostics. No bytechange alonefails/skipscomparison orwaivestiming/allocbudgets; no per-byteperformance discount.
- Existingfunctional/status/header/counters/provenance/rawcanonicalintegrityguards remain; sampleformat2 kept. No addedmedia-typeschema/semanticvalidator/fixtureexpansion/normalizer/allowlist/acknowledgement mechanisms.
- CLIreports originalmeasurementharness_sha256 plus comparison policy per-revision-response-stability-v1, actualloaded comparatorfileSHA and exactconsumedsamplebytesSHA. Loaded-inputerrors keep originalidentities; earlyunavailableidentities omitted, notsubstitutedcurrentfixture. Existinglegacydistinct_responses retained plusper-sourcecounts.
- Driver writesvalidatedGITHUB_STEP_SUMMARY with performanceoutcomes/responsechanges before returningordinaryexitstatus, includingregression/inconclusive. No YAML/action changes.
- All clocks/profiles/statistics/noise/adequacy/watchdogs/warmup/order/sourcepair/reference/budgets/frozenruntime/fixtures unchanged.

## Evidence before review

Focusedcomparator+eventdriver81/0(33.87s); selectedrunnercomposition/earlyerrors3/0(.30s); compatibilityfieldcase1/0(.51s). SixchangedRubypathslintclean,3productionfilesyntaxpass, whitespace/links/LFUTF8pass. Logs/tmp/2026-10-26-typescript-client-generation-performance-{focused,lint,final-source}.log. No newmeasurements/API/DB/install/regeneration/fullintegrationcampaign. Normalroottools-onlyNix/OvercommithooksHaveapiI18n+RuboCop+commit-msgpassed, no bypass; TextWidthwarningsonlyalllineswithin80. Testedcandidate/staged/committreeequal; all8filehashesmatch. Leadcompleted directprosepass; finalreflowonlymeaningunchanged.

Meaningfulnewregressions cover stablevalidchangedHTML/JSON passingnormalclassification, changedresponse+wallORCPU/allocregressionstillfailing, sameSHAvariation(includingAAsecondcolumn) failing, weighteddiagnosticarithmetic, exactcomparator/inputidentity andoldharnessattributiononerrors. Existing malformed/hash/count/counter/provenance refusals retained.

AllotherGitentriesbyteidenticaltobase, includingclients/VERSION(generatorf7d79703), fixtures,budget/reference/benchmarkGemfile+lock+shell/workflows/Makefile/flakes. No downstreamrepin, API/runtime/schema/persisted/deployment change.

## History and review assignment

Mediumrisk benchmarkpolicy/reportingonly. Requested lanes GENERAL + ARCHITECTURE/REPETITION + SCOPE/PROPORTIONALITY; read mandatory-change-review SKILL and all3references. Retainedindependentreviewer0savedSol/xhigh/read_only, preserve settings/nooverrides/fallback/nestedagents. Readcurrentworkspace/localAGENTS/procedures and finalbrief/plan/state. Fullnewrange1commit isindependentlyrevertible; no obsoleteapproach/fixup/repeateddependency/generatedstream; no migrations. Prior5mergedcommits are supportedhistory, unchanged. Explicitwholehistory/repeatedstream/nomigrationconclusionsneeded.

Reviewcommittedsource/tests/docsactualconsumers(APIhereisbenchmarkCLI/report consumedutils/performance_ci.rb/workflow+tests). No tests/builds/compilers/network/API/Gitmutations/source/recordsneeded forread-onlyreview. Findingsfirstwithseverity/evidence; leadpersistsfullreport. Do notrubberstamp; flagconcretefaultswithinchosenboundary, avoidrestoringrejectednewvalidatorframework.

## Postreview acceptance, not yet run

Retainedmasterfailure40529570313 remains originalfailedhistoricalevidence(pair029f79b->18b45aed,12byteHTMLaddition). ZIPe1fed6ccfe5902a691bf987b39d6bda3f332f6b336a1630003d6104b91c131d9 containscomplete115773806bytesresults/samples.json writtenbeforeoldcomparatorfailure. MatchingbudgetSHA57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050 unchanged. Preparedreplayscript/tmp/2026-10-26-typescript-client-generation-performance-replay.sh bindsnewcleanHEAD+comparatorSHA, extractsONLYsamplesandimmutable18bbudget intoNEWdir, thenCLIcompare. NOTYETRUN; requirescompletedreviewfirst. Newreportmustbindnewpolicy/comparator+exactinputbutoriginalmeasurementharness33da8128 andoriginalsourcepair. Neverrewriteoldreport orclaimnewmeasurement/greenoldCI. No newbenchmarkcampaignneeded.

Previous“mergeitall”approval precededthismaterialnewpolicy, so no defaultintegrationauthorized; sourcepublicationwaitsreview+replayacceptance. No release/version/tag/registry/deployment/sessionlifecycle action.
