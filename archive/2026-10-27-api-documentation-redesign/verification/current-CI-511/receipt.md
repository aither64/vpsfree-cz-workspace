# Exact 511 CI and artifact assessment

One observation of the 11 publication-record runs, 2026-10-29T01:11:37.422753+00:00
through 2026-10-29T01:11:41.188339+00:00. All completed attempt 1: ten success, release failed.
Run/jobs metadata and every executed checkout bind
`5114746f3a9f87e91c704147c0d99dd4f0d32f02`; native tree is
`5b9c52d0f0d81957bbca227d254e2e5b09b53373`. No pending branch, CI wait,
repeated status query, retry, rerun, dispatch or cancellation. Sole utility was
unavailable; the monitor skill's visible parent fallback owned only read-only
API/download handles, all now completed. No local test/runtime/benchmark launch.

| Run/workflow | Actual commands and coverage | Result and usable scope |
| --- | --- | --- |
| 40796243261 server | make doc; declarations; bundle exec rspec on Ruby 3.2.11/3.3.12/3.4.11, each 908/0; three Node assets | PASS; both prior server CI cases now execute successfully |
| 40796243240 Rust | generator units 161/0; lint 25 files; fmt; locked runtime tests default/blocking; Clippy all-targets/all-features; prepared fixture 2/0, then existing protocol runner | PASS; corrected stage executed, not skipped |
| 40796243284 performance | make test-performance-clients 214/0; original endpoints.rb e5ea→511 quick 14 cases | PASS at this exact pair only; direct f6 remains uncovered |
| 40796243237 release | release tooling 236/0 + six Python tooling tests; five gems/npm/wheel/sdist build; maintained make test reaches supplemental Python 7/2 | FAILURE exit 2; artifact retention/verification and subsequent install smokes skipped |
| 40796243252 JS | npm test: build, compatibility, async/resources, strict callback/async tsc and Mocha 50/0 | PASS; actual workflow source/test scope |
| 40796243386 Python | check.sh + 362/0 each Python 3.11–3.15; wheel/sdist installation each; real-server integration 61/0, five skips | PASS with explicit skips; package payload hashes not retained |
| 40796243298 PHP | vendor/bin/phpunit on 8.3/8.4, each 52 tests/146 assertions | PASS; PHP 8.4 reports one deprecation |
| 40796243251 Go | bundle exec rspec on Ruby 3.2/3.3/3.4, each 100/0 | PASS; no expanded wire/MSRV inference |
| 40796243270 Ruby client | bundle exec rspec on Ruby 3.2/3.3/3.4, each 67/0 | PASS |
| 40796243382 RuboCop | bundle exec rubocop --parallel --force-exclusion, 420 files | PASS, no offenses |
| 40796243684 i18n | bundle exec rake i18n:health | PASS |

`single-observation.json` retains exact jobs/steps/times. `downloads.json` hashes
every original log ZIP and records artifact listings. `log-coverage.json` points
to actual command/result lines; full completed step logs remain under logs/.
Ordinary matrix bundles resolve their own dependencies; they do not attest the
calibrated benchmark graph or prove equality to local component closures.

## Release failure and package provenance gap

Raw failure: logs/40796243237/Validate, test and build/
8_Test and build maintained packages.txt, SHA256
`2b69dd91e4942f4402acb8719324cc653cd83c2b0ea61ace09337ee5e6571890`.
make test-documentation-python runs the existing dynamic_protocol_spec.rb plus
dynamic_python_login_spec.rb: seven examples/two failures, seed 2782. Both
sync/async fail at dynamic_python_login_spec.rb:69: expected user=fixture-user,
password=fixture-password, scope=all, lifetime=fixed; actual native/rendered map
is user=user, password=secret, scope=scope, lifetime=fixed. The test still builds
HAVEAPI_AUTH_* environment values while the accepted M8 renderer emits public
literals. No authentication success or later URL/body/error assertion is inferred
from this failed comparison. The five native request-encoder contract cases pass;
the two token-login mapping cases block full supplemental coverage. No source
repair or rerun occurred; the exact failure was reported to the lead.

Earlier release work is usable at its actual scope: make release-test 236/0 and
six Python artifact-tool tests; make release builds haveapi-client, haveapi,
haveapi-go-client, haveapi-rust-client and haveapi-typescript-client 0.31.0, with
shared-doc copy, npm pack, Python wheel/sdist and extracted Rust/TypeScript
validation. make test then passes server 908/0, Ruby client 67/0, Go 100/0,
TypeScript units 62/0, generated profile HTML 19/0, JS 50/0, PHP 52/146, Python
362/0 + integration 61/0/five skips, Rust units 161/0, runtime default/blocking,
prepared fixture 2/0, root/mounted generated protocol and all three assets.
Only then does the supplemental 7/2 failure occur. The negative ContractError
messages inside passing server specs are expected contract tests, not run errors.

The exact-head fresh build is proven by checkout and completed build logs, but
release API lists zero retained artifacts: upload, retained-artifact verification
and summary are skipped. Consequently the five final gem contents/docs/runtime/
metadata and wheel/sdist/npm SHA256 or payload equality cannot be independently
inspected here. The log's npm SHA1 is diagnostic only. The release's subsequent
smoke-npm and Python package_smoke commands do not execute after make test fails.
The separate Python workflow does prove fresh wheel/standalone-sdist installation
on all five versions; those packages also have no downloadable payload receipts.
Publish approved artifacts is skipped, branch build-only; no registry/tag/release
publication was requested or performed.

Retained a06b installed artifacts tested against e5ea renderers remain their
original evidence. They are not renamed as this 511 build or installation.
Fresh exact-source package payload identification/retention is still missing.

## Exact-head performance evidence

Artifact 12864680158, performance-40796243284-1, ZIP SHA256 equals the API digest:
`5093d73d263429a8cbda30a3617883cef4670a993191679b998e18cb4062a715`.
Event, selection and runner-command choose push before
`e5ea07028e48a6936b947c172fa89eca15e3a416` and after
`5114746f3a9f87e91c704147c0d99dd4f0d32f02`, quick, --push-event;
captured default f6 is not the selected timing baseline. Original runner exit 0,
report pass, 14 cases all pass with adequate wall/CPU/pilot signal, three self
and five alternating pairs each. All-client step 27s (RSpec 24.72s +0.74962s
load), pair step 333s. This incremental result cannot replace direct f6→511;
no timing composition or local measurement occurred.

Both 908-blob native manifests, modes, Git blob identities, tar members, recorded
full-file SHA256 maps and reconstructed Git trees verify. Candidate archive
`215b32ae9f7cb4f5dacb7806081cf736d6b66a81052245a7a41b6b54d532a2b2`
is byte-identical to the Phase A511 export; baseline archive equals original
e5ea CI candidate archive. `performance-source-input-binding.json` retains trees,
archive/manifest identities and detailed verification.

All 19 paired process graphs match unchanged weekly 87-gem calibration, JSON
2.21.2/io-console 0.9.4, immutable 7b77 Ruby; dedicated CI benchmark gemroot plus
Ruby defaults, outside Bundler. Each process's 127 loaded source digests match
its native source; six neutral fixture hashes, nine raw source input hashes,
embedded benchmark Gemfile/lock/shell, normalized input graph and raw metadata
receipts match retained e5ea policy. No graph/lock/version/normalization change.
Budget SHA256 `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`;
fixed reference `b85ec364057f536940d689b09e612512ffffaf82` unchanged.
Comparator-consumed samples SHA256:
`1f6e418e8eadc738d47dd79c7a54fdfbaf413c4ae7b4b5def06647b2874e7f69`.
All actual source/inputs/raw-normalized/process/sample/report evidence is retained;
this assessment reads and binds it without replaying measurements.

Actual 511 all-client log verifies 210 unique 15×7×both direct records plus four
registry/profile/panel/role/scaling cases, 214/0. Maximum unrelated-subtree
allocation increment 1, calls 0, both <=32. Resource 2/4/8 allocations
179218/191290/215365; action allocations 103256/184808/348489, both unchanged
2.5 increment-ratio bounds pass. Exact final spec/fixture bytes use real generated
profiles, every declared panel and admin/member/admin isolation. Standalone
all-client still has no independent activated-gem attestation; the 19 graphs
belong to paired processes. No local duplicate all-client is needed.

Rust CI explicitly runs the new two-spec fixture command after server dependency
preparation and before unchanged HAVEAPI_RUST_INTEGRATION=1 protocol. Runtime
results default 2+5+16 and blocking 2+11+16 pass; generated protocol returns
2+6+2 per root/mounted pass. The driver source confirms both mounts and async/
blocking tests. CI uses its declared component shell, not an explicitly selected
1.95 compiler: the crate's Rust 1.95 declaration/compatible dependency resolution
is not proof of the separately assigned MSRV/root/mounted documentation-program
batch. No 52-program installed/native acceptance is inferred here.

## Remaining work and preservation

Needed: original-owner supplemental two-expectation diagnosis/fix with preserved
body/URL/missing-field checks; full release completion and retained exact-source
package hashes/payloads; separately owned remaining native MSRV/mounted batch;
then the single direct f6→actual final pair only on the lead's execution relay.
No automatic retry, duplicate all-client or product change is authorized here.

All 908 current source paths/modes match publication; all 2148 protected inputs
and 72 frozen records rechecked unchanged. Existing e5ea/24ec/failed CI logs and
all prior performance exports/proofs were only read and remain intact. Phase A
and its commands are unchanged, paired-quick does not exist; Phase B stays held.
No source/Git/index/ref/hook, local test/compiler/runtime/version, Nix/setup/
install, listener, preview/service/provider/TLS/peer/lifecycle action. All owned
read-only handles completed; no active or uncertain operation. No final overall
performance/package readiness is claimed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
