# Exact e5ea CI/artifact assessment

One fresh observation of the11publication-record run IDs at
2026-10-29T00:01:37.369883+00:00 through2026-10-29T00:01:41.058822+00:00. All were completed attempt1,
all metadata/downloaded logs bind exact
`e5ea07028e48a6936b947c172fa89eca15e3a416`, tree
`543cd44c4a1863489ae2289d2a8769a60e7c1b85`. No pending branch, CIwait,
repeated status query, watcher, retry, dispatch or cancellation. Existing24ec
and older errors/proofs remain untouched. downloads.json hashes every raw logZIP;
run/jobs JSON, completed step logs and available artifacts are retained here.

| Workflow/run | Actual completed coverage | Result/usable scope |
| --- | --- | --- |
| Performance40789710177 | All-client214/0;24ec→e5ea quick14cases PASS | Actuale5ea all-client; incremental pair only |
| Server40789710167 | Ruby3.2/3.3/3.4 each908/2;3assets pass | Full matrix blocked by2tests; assets reusable |
| Release40789710021 | Metadata/tooling236/0,Python tooling6/0;make-test908/2 | Full package/build not completed; no release artifact |
| Rust40789709969 | Generator units162/1,seed13132 | Fixture subprocess fails; later compile/protocol skipped |
| JS40789710313 | build/compatibility/async/resources/types +Mocha50/0 | Actual JS workflow coverage |
| Python40789709988 |362/0 each3.11–3.15;realserver61/0+5skipped | Actual unit/integration scope, skips retained |
| PHP40789709975 |8.3/8.4 each52tests146assertions | Pass;8.4reports1deprecation |
| Go40789710016 | Ruby3.2/3.3/3.4 each100/0 | Actual adapter Ruby units; no wire inference |
| Ruby40789709855 | Ruby3.2/3.3/3.4 each67/0 | Actual client units |
| i18n40789710081 | bundle exec rake i18n:health | Pass |
| RuboCop40789710221 |420files,0offenses | Pass |

## Performance artifact and scope

Artifact id12860514417, performance-40789710177-1, ZIP digest matches API:
`32cdf3e3d9c6453977ee5984d30e39518144fc4126dc10852e5c7b7691ce6866`.
selection/event/runner-command explicitly choose push before24ec424c9592951da38584379b43379b0c39f115
aftere5ea07028e48a6936b947c172fa89eca15e3a416, quick, --push-event.
The immutable7b77Ruby executes endpoints.rb run outside Bundler with separate
baseline/candidate exports. runner.exit0, report.status pass,14cases all pass;
3self+5alternatingpairs each, pilot/calibration evidence retained. No failure or
inconclusive phase. This is NOT required directf6→final; that remains unstarted.
Do not compose24ec/d67/f6timings. Fixed reference remainsb85ec364057f536940d689b09e612512ffffaf82.

Both908blob native manifests, modes/blob hashes/archive members and recorded
file digests verified. Reconstructed Git tree IDs from those native records
match actual reported288376a727deb3905d2c368150543a6d7cfc0971 baseline and
543cd44c4a1863489ae2289d2a8769a60e7c1b85 candidate, without invoking Git.
Baseline equals retained24ecnative export; candidate hashes/modes equal all908
publication source records. Archive SHA256 baseline
8d76bba204178c3580a27a3cf6175314a3cab6614378453e5505ea2a7b29f352;
candidatea610c187ad514efe6a93bef83b4beaefa098316e44bfabe3b6d7693e56c079c1.
No local candidate export/archive campaign was started; these are downloaded
original CI artifacts.

All19process environments equal frozen weekly87-gem calibration, including
JSON2.21.2/io-console0.9.4 and exact Ruby
/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby.
CI dedicated gemroot is /home/runner/work/_temp/haveapi-benchmark-gems plus that
Ruby's defaults. It is not the local/root/Go/Rust bundle. Every recorded loaded
source digest belongs to its selected source, and all6neutral fixture hashes
match published final. Embedded benchmark Gemfile/lock/shell and9raw input hashes
match publication. Budget57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050;
canonical fixture-map/harness digeste77c9353fc486d8f54f3fd7fe7d8515b7e52a3a7dcb767d013ce751ca634f831.
Report consumed-samples digest verifies
83e03b9966f09d5c4a3fed4946a03c1e0c2640ee6af7bee2d67b1bbee8f05e67.
HTML observations retain overview shape/actual admin/member authorization:
Rust16resources4actions2samples4parameters,65admin/64member authorized actions,
65authorizations/request and no action execution. Existing real-cookie identity
and crypto/provider work stay in original neutral code and per-process proof.

All-client log contains210unique15×7×simple/thorough records, plus4registry/
profile/panel/role/scaling contracts,214examples0failures. All recorded direct
allocation increments<=32 (observed max1), call increments<=32(max0).
Resource2/4/8allocations179223/191266/215338; action2/4/8allocations
103248/184774/348498; both2.5increment-ratio bounds verified. Exact candidate
spec/fixture bytes exercise realGo/Rust/typedTSprofiles, declared groups/panels,
admin/member/admin isolation, unrelated-resource and selected-action growth.
Actual all-client command is make test-performance-clients under the frozen
benchmark shell, including doccopy. It has no separate activated-gem receipt;
do not call the pair's19graph records the standalone all-client process proof.
It completed24.25s+.72051sload (CI step26s); pair step5m35s.
This actuale5eapass avoids a local duplicate for exact unchanged affected inputs.
Later source changes require scoped comparison, not blanket final-head reuse.

## Failures: exact facts for original owners

Server3matrix lanes and release all fail the same2cases:

1. documentation/reference_headings_spec.rb:146: Rubyid0 page capability still
   expected['simple']; actual acceptedM8 declaration is['simple','thorough'].
   The surrounding group/panel/page-union checks are real; preserve them when
   updating this stale specific expectation.
2. client_examples/dynamic_mounted_paths_spec.rb:19/27: its mounted real-descriptor
   test still sends fixture-user/fixture-password, code123456 and fixture-token.
   The M8fixture accepts user/secret, code and example-token. The fatal401 is
   the protected action atline27; preceding token/challenge responses can still
   be HTTP200 with failed envelopes, which the helper does not inspect. Preserve challenge/discovery,
   nested typed path/body and callback/async assertions in any fixture update;
   no production auth fallback is suggested.

Rust documentation_harness_spec.rb:55/92 fails before a fixture request:
Bundler::ProductionError, “Your bundle only supports platforms [] but your local
platform is x86_64-linux.” Its newly real fixture unit subprocess selects
SERVER_GEMFILE/frozen server bundle during generator units; workflow's Prepare
fixture server dependencies step is later and skipped after failure. Repeated
Gem::Platform warnings precede this actual fatal error. This is a concrete test/
setup-order boundary for original owner diagnosis, not license to update locks
or bypass provider behavior. Remaining Rust runtime formatting/features/lint and
generated protocol steps are skipped, not passes. Old24ec13+2Rust wording and
Go-capture failures no longer appear; final full-suite success still absent.
Release stops at server make-test and retains no completed package artifacts;
publication job remains skipped, with no release approval/registry write.

JS actual npmtest builds and runs compatibility/async/resources, strict callback/
async TypeScript tsc targets and Mocha. Python uv--locked pytest integration is
real server transport;5skips remain. Assets execute all3highlighter/tabs/docsNode
targets and pass. No standalone generatedGo/typedTSwire, installed36program batch,
Rustcompile/MSRV/root/mounted/both-mode or supplementalPython documentation
encoder coverage is inferred from these job names or unrelated passes. The
release abort occurs before its remaining maintained-package stages.

Next needed: original-owner narrow test/setup fixes and affected checks; complete
final package/build and skipped explicit compiler/wire/encoder gates, with
independently running installed/browser packages remaining separately owned.
Required SINGLE directf6→actualfinal quick remains unrun; current all-client
success is reusable for its proven source/input scope. Main grants later work.

All2148protected current hashes and72frozen records rechecked unchanged. The
published908source snapshot was used as immutable artifact authority. At this
assessment end, current source differences versus that publication snapshot:
none observed by SHA256 read.
These are observations only; no source/index/ref/hook operation or source repair
was made here. No local tests/builds/versions/toolsetup/Nix/deps, listener,
CIwait/retry/dispatch/cancel, watcher/utility, preview/service/provider/TLS/peer/
lifecycle action. All owned read-only handles completed; no active effect.
Static performance preparation remains preparation, with no local export or
measurement. Old proofs preserved; no final overall readiness claim.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
