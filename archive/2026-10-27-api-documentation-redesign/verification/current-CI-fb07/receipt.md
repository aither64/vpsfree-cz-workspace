# Exact-final fb07 CI and artifact assessment

ONE fresh observation 2026-10-29T02:24:35.524453+00:00 through
2026-10-29T02:24:39.364934+00:00, of the 11 exact publication-record attempt1 runs.
All completed successfully at `fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`;
native source tree `0e72671b95ef3d0893eb83271c4ef2b78993d57a`.
Each executed checkout and run/jobs record identifies that exact head. Recovery
511 runs were not queried. No pending branches, CI wait/poll/retry/rerun/dispatch
or cancellation. Completed logs/API records and original artifact ZIPs retained;
all known-small read-only downloads completed inline, no utility was launched.

| Workflow/run | Actual completed commands and coverage | Scope/result |
| --- | --- | --- |
| Release40803800711 | release-test236/0 + six Python tooling cases; make release; full make test; npm/Python install smokes; upload/verify | PASS; fresh final artifacts retained and inspected |
| Server40803800814 | make doc/declarations; bundle exec rspec on Ruby3.2/3.3/3.4 each908/0; three Node assets | PASS |
| Rust40803800779 | units161/0/lint25; fmt; runtime default/blocking locked tests; all-target/all-feature Clippy; prepared fixture2/0 then protocol runner | PASS; corrected stage executed after server preparation |
| Performance40803800783 | actualfb07 all-client214/0; selected511→fb07 quick14PASS | Incremental pair only, not directf6 |
| JS40803800768 | npm test build/compatibility/async/resources/strict callback+async tsc/Mocha50/0 | PASS |
| Python40803800694 | check.sh362/0 each3.11–3.15; wheel/sdist installations each; integration61/0 + five skips | PASS at explicit scope |
| PHP40803800666 | PHP8.3/8.4 each52tests146assertions | PASS;8.4 one deprecation |
| Go40803800774 | Ruby3.2/3.3/3.4 each100/0 | PASS; no expanded native wire inference |
| Ruby client40803800834 | Ruby3.2/3.3/3.4 each67/0 | PASS |
| RuboCop40803800687 | parallel force-exclusion,420files/nooffenses | PASS |
| i18n40803800827 | bundle exec rake i18n:health | PASS |

single-observation.json binds exact job/step times; log-coverage.json points to
actual command/result lines; downloads.json hashes original raw log ZIPs and
retains artifact listings. No CI failure or missing retained artifact observed.

## Full release and corrected encoder acceptance

The completed 377s build/test step runs, fail-fast, make release-deps,
i18n:health, make release-test, make release, make test, smoke-npm dist and
Python uv --locked package_smoke.py. This is a fresh build, not artifact restore.
make test retains server908/0, Ruby67/0, Go100/0, TypeScript units62/0, generated
profile HTML19/0, JS50/0, PHP52/146, Python362/0 + integration61/0/five skips,
Rust161/0 + locked runtime default/blocking + fixture2/0 + root/mounted protocol,
and all three assets. The supplemental actual command is:

`cd servers/ruby && bundle exec rspec test_support/dynamic_protocol_spec.rb test_support/dynamic_python_login_spec.rb`

It passes7/0, seed49200,3.73s +0.56149s load: both native Python login mappings
and all five request-encoder contracts. The later npm smoke installs the retained
npm archive, validates callback/async exports/version and package-name strict
TypeScript consumer declarations. The later Python package_smoke builds fresh
temporary wheel/sdist from this same head, rebuilds a wheel from the standalone
sdist, and installs/checks both wheels outside the checkout. It does not consume
the original retained dist wheel/sdist; their content/hash proof is independent.
Extracted Rust generator/runtime and TypeScript generator/shared-schema/published
runtime smokes passed during make release. Raw completed step logs are retained.

Release artifact12868045261/release-40803800711 is12files, original ZIP SHA256
`9a101043273d9d844345b9d5c502e0cc7dce34261dcec80e2b9c2b096b83affd`;
API digest, upload log and downloaded bytes agree. Build checkout,
release-manifest.source and retained verify identify actualfb07. Manifest SHA256:
`00400290ff006d2bcace0adc1fe38e14d5daa50494772d7ea8cfd715be2f301d`.
All11 declared file hashes verify independently; release-manifest is the12th
file. Manifest tool versions and all ten resolved dependency-lock texts are
retained. The verify step explicitly reports v0.31.0 at exactfb07.

| Gem | Payload files | SHA256 |
| --- | --- | --- |
| haveapi | 268 | d28be5c5cca087a850c0f9013d003eb5001c27b30cdbe408b14c452eaccadc2c |
| haveapi-client | 74 | 513e0ecde4c7afa289e970503e9a588507f70de051354c2fa95e0f5f3fd9254a |
| haveapi-go-client | 57 | 2e814385452d27f59a8529e5b2a8f51c490bacd6b8409a4e1b0856334af1ad0a |
| haveapi-rust-client | 30 | 8c018728906e292c44822a556c413fb4f6bb935d2a425d21391bf21d03da88da |
| haveapi-typescript-client | 22 | 180aece3dc03ac6731713e593589d3f3dc1a73f00a6a17e98b14892e886a1a5b |

All five names/0.31.0 versions/Ruby floors/executables/dependency metadata and
metadata-declared payload sets were inspected without loading Ruby packages.
Inner SHA256 checksums verify. Server268, client74, Go57 and TypeScript22 payload
files equal the exact native source/export. Rust29source files equal source;
its30th file, Gemfile.lock, equals the retained component lock text. Server11
shared generated docs equal validated final outputs. Ruby client includes all
four current shared schema files; Rust includes eight embedded runtime files.
The PHP archive's36payload files also equal the exact source. Detailed per-file
and metadata digests are in release-payload-binding.json.

Fresh final npm archive SHA256:
`1f01aea5cd29415013b21cbe763ae5823d6889d8b6a93567916801ac50705af3`.
Fresh final wheel SHA256:
`016a08dfe2ca6c629034bb2308267c234a21cb00edda019bd56a206e8c1e1aca`.
Fresh final sdist SHA256:
`75c48e61e7cb87639f6b0e32f4beca4cd458a3a591a99b1afbb9e1f41d78f7cf`.
Npm53payload files include46declarations; package manifest equals source and the
packed runtime equals the standalone bundle. Wheel RECORD hashes/sizes verify;
19Python payload files match wheel/sdist/source, and complete parsed pyproject
fields match source (pyproject.toml.orig also matches raw bytes).

Those three complete archive byte streams independently equal preserved a06b
artifacts. All67authored runtime source blobs and46declarations match, with the
full pyproject compared separately. The initial static inspector accidentally
counted that separate pyproject as a68th member of the retained67-source set;
correcting this inventory grouping found no payload drift and changed no input.
Original installed36×2 execution remains labeled with its actual old artifacts/
e5ea renderers. These newly identified fb07 artifacts/builds and successful CI
smokes are separate evidence; no installed full-program rerun is claimed.

Ordinary release locks/tools are their own resolved graph (including newer
compatible dependencies); they are not asserted equal to the frozen benchmark
87-gem graph or local root/server/Go/Rust bundles. Current local locks remain
unchanged. Manifest tag=v0.31.0 is conventional build metadata: this branch run
has empty RELEASE_TAG, publication setup skipped, Publish approved artifacts
skipped. No registry/tag/default-branch publication was requested or performed.

## Exact-final performance CI at its actual pair

Performance artifact12867721059, original ZIP SHA256
`dcb10d58928a1fd675e97e6796ac19c40c00291ecec9677162743f8f48ca3b34` verifies API digest.
Actual push selection is511→fb07 quick, relevant=true for the one supplemental
Python spec delta. Original endpoints.rb run --push-event executed, not skipped;
runner0/reportPASS/all14PASS, adequate wall/CPU signals,3self/5alternating pairs.
All-client step27s (RSpec25.39s +0.75287s load), paired step350s. This actual
incremental timing does not substitute for or reclassify the directf6 result.

Native908blob manifests/modes/Git blob identities/full-file hashes/tar members
and reconstructed trees verify for both endpoints. Candidate archive equals
original fb07 native export; baseline equals original511 native export. All19
paired process graphs match weekly87gems, JSON2.21.2/io-console0.9.4, immutable
7b77Ruby with dedicated CI benchmark gemroot. Each process's127loaded source
hashes belongs to its exact source. Raw source inputs, source-version/normalized
graph, benchmark Gemfile/lock/shell, fixtures, budgets/reference equal retained
511 policy. Comparator-consumed samples SHA256:
`2174427247219a21cf41d6e67a90f12cb885ef5358039a999a608cee81a3e825`.

Actual final all-client214/0 contains210unique15×7×both records, registry/profile/
panel/admin-member-admin checks, unrelated-subtree +32 object/call bounds and
both resource/action2/4/8 growth bounds at2.5. Standalone all-client still has no
separate activated-gem attestation; paired graphs do not fill that distinct gap.
No local duplicate all-client or measurement was launched.

Rust CI uses the declared component shell and tests the existing root/mounted
protocol in async/blocking modes. A Rust1.95 crate declaration and compatible
resolver selection do not prove an actual1.95 execution. The separately retained
native511Rust208 development/MSRV/root/mounted proof keeps its actual label;
no new native208 execution is inferred here.

## Preservation, remaining limits and resource release

At 2026-10-29T02:34:16.876259+00:00, raw ref-file readback is exactfb07;
all908current source hashes/modes,2148protected inputs,72frozen records,23roots,
9152prior performance files and all99current direct-run hash records are
unchanged. Original direct receipt/report/samples retain their accepted digests:
receipt `a0ed2ef9f8c4dea545eee5e809fb7214239dd0124fedaaff0185b40773f55e15`.
The existing index mtime predates this assessment; its SHA256 is recorded in
preservation.json. No Git/index/ref/configuration command or mutation occurred;
flags and locks were not changed. No tool setup/Nix/install/local test/compiler/
program execution, source write, preview/service/provider/TLS/peer/lifecycle action.
No watcher/utility was launched; all API/download handles and child processes
completed normally. No runtime/ownership/source/input blocker observed.

Directf6→fb07 remains its original correctly executed INCONCLUSIVE result:
eight pass/six inconclusive, all14deterministic pass, no classified regression;
no all14measuredpass/no-slowdown claim or required-check waiver. Main/architect
own its accepted disposition; no replay/retry/new performance work follows here.
Python integration's five skips and standalone activated-graph limit remain
explicit. This assessment reports coverage, not general readiness or publication
approval.

**Current assessment operation/sourcehold and utility capacity explicitly
RELEASED; no active or uncertain owned handle.** Main and owner4 receive the
actual receipt/outcome. This releases the resource, not CI acceptance. Owner4's
controlled refresh follows only its separate main grant6a98fdbc and its own
stable-head/input/capacity checks; no additional preview hold is inferred from
the historical inconclusive run. No preview action was taken here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
