# Documentation CI evidence at a06b0cfa

Exact observed candidate: `a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9`, tree
`ed2764be21718b64e8f9f1bf9e2480798beaa18d`. These results belong to this
revision. The separately planned CSS overflow correction is not covered by
relabeling this CI; future reuse needs its actual unchanged contract/input proof
and affected checks. `committed-source-blobs.json` retains all 905 source blob
IDs for that later comparison.

## Actual executed scope

All four observations are push runs, attempt **1**, completed success:

| Run | Proven execution |
| --- | --- |
| Server `40745814328` | Ruby 3.2.11 / 3.3.12 / 3.4.11 each ran unrestricted `bundle exec rspec`: **867 examples, 0 failures**. Seeds 55722 / 20423 / 34637. Each generated shared docs and built current JS 0.31.0 public declarations before specs. Assets job executed highlighter check plus all three Node scripts successfully. |
| Branch release `40745814145` | Restore-original-artifacts skipped; Test-and-build-maintained-packages executed successfully. Build, release tests, full `make test`, npm smoke and Python package smoke all completed. Publish job skipped. Unrestricted server **867/0**, generated-profile **18/0**, exact supplemental dynamic protocol/login encoder target **7/0**; all three asset scripts passed. Installed npm callback/async exports and public declarations reported 0.31.0. Wheel and standalone sdist install smoke passed. |
| JS `40745814300` | Actual npm test built 0.31.0 then ran compatibility, async, resources, strict callback/async types and Mocha checks successfully. |
| Python `40745814262` | Python 3.11–3.15 each passed format/lint/type checks, **362 unit tests** and wheel/standalone-sdist smoke. Real fixture integration passed **61 tests** with **5 opt-in live-vpsAdmin skips**; no provider/private/live acceptance claim. |

The older-Ruby validator portability correction genuinely passed in the full
3.2/3.3 matrix. This is fresh successful execution, not a retry or reinterpretation
of the failed 35c run; those old failed logs remain intact.

Unrestricted server default discovery contains all **83** tracked spec files,
including all **11** ordinary performance spec files and `spec/packaging_spec.rb`.
`.rspec` only requires spec_helper; spec_helper does not exclude/filter this scope.
Packaging therefore exercised the actual gem build, extraction, isolated loaded
framework path and shared README/technical route assertions, not only file
presence. CI logs show the gem build during specs. See `ordinary-discovery-proof.json`;
this satisfies ordinary deterministic performance discovery for this CI graph,
without repeating a local server suite or claiming frozen benchmark equivalence.

The release's exact supplemental command was:
`cd servers/ruby && bundle exec rspec test_support/dynamic_protocol_spec.rb test_support/dynamic_python_login_spec.rb`.
Its distinct generated-profile command ran the three existing profile specs via
explicit Ruby/TypeScript load paths. Neither these nor npm/Python install smokes
invoke `dynamic_acceptance.rb`. The six-variant **thorough** installed npm+wheel
and npm+sdist snippet/wire runs remain **UNEXECUTED**, pending main's final-source
run grant. No installed simple-program equivalence is claimed.

## Input and package proof limits

Run/head/jobs/step statuses, full logs and artifact API responses are retained
as `ci-*`, `jobs-*`, `log-*`, `artifacts-*`. `coverage-excerpts.json` preserves
line-numbered relevant execution evidence.

Actual complete server Ruby lock text was printed in each matrix log and is
retained separately as `server-ruby3.x-Gemfile.lock` with SHA256 in
`server-input-summary.json`: source PATH packages have version0.31.0 and
server JSON2.21.2. These jobs used Node24.22.1/npm11.19.1 and their current
source declaration build; they are not asserted equal to prepared local graphs.
The branch-release log records repository-pinned Nix inputs, Bundler4.0.23,
Python3.11.17, actual package build and source-bound release verification.
Full release tools/resolved locks and per-package manifest hashes remain inside
the archive; they have not been read/extracted in this grant. No Nix cached
result or full local/frozen graph equivalence is inferred from green status.

Available source-bound artifact:

- Run40745814145, artifact **12842017816**, `release-40745814145`.
- Downloaded immutable ZIP: `release-40745814145.zip`, **1,200,257 bytes**.
- Actual ZIP SHA256 matches API: `86c49d97e29e628bf87a6ba6f74892216c9b31a5514bc93b218a60175810b2e4`.
- Central-directory metadata lists `release-manifest.json`,
  `haveapi-client-0.31.0.tgz`, `haveapi_client-0.31.0-py3-none-any.whl`,
  `haveapi_client-0.31.0.tar.gz`, source-matched gems and other release files.
- No ZIP member was decompressed, read or extracted; manifest source/version/
  tool/lock/per-package-hash content inspection awaits the later grant.
  CI itself reported `Verified retained artifacts: v0.31.0 at a06b0cfa...`.
  See `release-archive-identity.json`.

The release is ordinary branch **build-only**. No tag, registry publication,
workflow dispatch, retry, rerun or network mutation was performed here.

## Operation boundary

One metadata observation per run; no wait/poll loop. Twelve known-quick
job/log/artifact metadata downloads exited0 in **20.04 seconds**; ZIP download
and digest/central-directory check took **1.97 seconds**. No utility was started
or capacity taken; browser owner's utility remained available. All downloads
are complete, no active owned command/watcher remains. Source/Git/check quiet.

Only session evidence and downloaded CI files were written. No tests, builds,
installs, artifact extraction, app/source edits, Git mutations/hooks, preview,
HTTP/browser probes, OAuth/private/provider/TLS, peer or lifecycle action ran.
Prior35c evidence is unchanged. Remaining uncovered installed dynamic verification
waits for corrected final source and main's explicit run package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
