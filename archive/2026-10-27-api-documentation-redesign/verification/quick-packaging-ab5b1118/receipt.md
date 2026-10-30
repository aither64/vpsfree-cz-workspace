# Final 0.31 packaging and performance input preparation

Completed remaining preparation at final source
`ab5b11188941d1c8c918951cdee162e9aa9f68cf`, tree
`c3c3e04337bcf9669dbb79611d72a65c686af9e0`, based on
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
Exact head/tree and clean source/index were checked before and after each stage.
No operation remains running; watcher ownership is released.

## Actual checks and result scope

The original resumed operation's stage 05 ran the existing **three packaging
examples, zero failures**, at this exact final source. It built the actual
0.31.0 gem, extracted it and served the existing documentation/asset route
matrix from its packaged framework. The existing subprocess source-location
assertion proved that server code loaded from the extraction rather than the
checkout. RSpec took 2.85 seconds; the stage took 9.75 seconds.
See `05-packaging.log`. These examples were not repeated.

The following metadata-only stage initially failed because the original-owner
probe omitted `require 'fileutils'`. The lead accepted that diagnosis and the
one-line explicit require. `receipt.initial.md`, original driver/probe/logs,
exit and watcher evidence remain unchanged. The corrected operation reused the
same retained gem, without rebuild or new functional checks, and passed:

| Corrected stage | Exit | Wall time |
| --- | --- | --- |
| Retained gem metadata/extraction | 0 | 1.174 s |
| Baseline exported `make doc` | 0 | 0.242 s |
| Candidate exported `make doc` | 0 | 0.188 s |
| Frozen dependency availability | 0 | 7.022 s |

The complete corrected operation took 13.313 seconds and exited 0. Exact
commands/cwds/exits/timings are in `corrected-stages.json`; logs have the
`corrected-` prefix. `operation.corrected.log`, `.exit` and `.elapsed` retain
the driver result; watcher CLI result is separate.

Earlier successful results retain their recorded scope: `make doc`, source
metadata `check-clean --master`, sibling-source version/loaded-path probe, and
44 unchanged lineage/profile examples were run at the prior head. The changed
profile-mount file's seven focused examples passed separately after its route
assertion fix. The final head differs from that prior source only by the
accepted test-file patch. Neither those 44 examples nor the seven fixed cases
were rerun by this packaging/export operation. See
`../quick-packaging-a0c78d1c/receipt.md`,
`../profile-mount-route-fix-a0c78d1c/` and
`../../history-profile-mount-fold-20261028t132040z/receipt.md`.

## Retained gem and source identities

`haveapi-0.31.0.gem` SHA-256:
`a6bb22115c557b6733dd3d30efa52c9f3e7f0f15e03865f248c03cf675431820`.
`package-metadata.json` verifies package `haveapi` 0.31.0 and internal
`haveapi-client ~> 0.31.0`. The same bytes were retained before the correction
and extracted under `extracted-server-corrected/`; no rebuild occurred.
Existing packaging examples prove actual route/load behavior; the corrected
metadata stage only inspects/extracts that retained artifact.

## Exact performance exports: preparation only

Both roots under `../../performance-ab5b1118/` were created with ordinary
`git archive`, retained native NUL-separated `git ls-tree` manifests, and ran
`make doc`. Every tracked file was rehashed against its native Git blob after
doc generation. Full SHA-256 source manifests and separate generated-document
manifests remain beside each archive. Neither export is a measurement result.

| Input | Full source/tree | Archive SHA-256 | Verified tracked files |
| --- | --- | --- | --- |
| baseline | `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0` / `123020cb5dfe6490a1335c0f3ff041b93bcc9550` | `b0139d61d086abcb5fafc5d65d12581e3d7096514ea32d42b1bebe6bed8e88d2` | 860 |
| candidate | `ab5b11188941d1c8c918951cdee162e9aa9f68cf` / `c3c3e04337bcf9669dbb79611d72a65c686af9e0` | `141c8d60c81f9ee4c8300851b27c3d5dda4d45a6981d22dff8f295980359c646` | 898 |

`source-preparation.json` also binds each native ls-tree hash.
`neutral-harness.sha256` binds the one final-candidate harness. Baseline,
candidate, neutral checkout and historical prepared exports have identical
frozen benchmark Gemfile, lock, shell and budget bytes. Budget SHA-256 remains
`57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`;
fixed reference remains `b85ec364057f536940d689b09e612512ffffaf82`.
No policy, workload, count, ceiling or runtime was changed.

`frozen-availability.json` proves calibrated interpreter
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`,
Bundler 4.0.23, JSON 2.21.2 and the dedicated benchmark gem home. It records
71 resolved available specs (70 dependencies plus Bundler), with no HaveAPI
package. This is availability/identity preparation; future ordinary workers
must still prove their complete activated graph and loaded source paths.
The separate Go JSON 3.1.0, server/Rust JSON 2.21.2, preview, MSRV and published
TypeScript runtime inputs were preserved without resolution or mutation.

## Preservation and next step

All **2,148** protected input/evidence hashes remained unchanged, including
previous quick failure/probe/packaging evidence, old exports and refreshed
component locks. No unused standalone component lock appeared. One fresh
retained-catalog Luna/low utility ran each distinct operation, with explicit
danger-full-access/never from installed full-access policy and native binding
checks outside Nix. Parent did not poll the watcher's logs during execution.

No source, dependency, Git/hook, preview, OAuth/TLS, publication, default merge
or lifecycle action occurred. Only ignored docs/gem/extraction/export/evidence
artifacts were written. No all-client, scaling, paired pilot, measurement,
compiler, wire or other long gate was launched. Independent final review and a
separate run grant precede long acceptance; `commands.md` in the new export
directory retains exact future commands and stopping rules.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
