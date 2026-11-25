# Captured sites cache retention failure

Owner: implementer0, Package A. Tested/reviewed source remains
`efc5f8fe87f7b0ddc09b5946047e1c231d23db67`, run
[41714748110](https://github.com/vpsfreecz/vpsadminos/actions/runs/41714748110),
attempt 1. This note records the failed attempt and checked workflow
correction, consolidated locally as `06d373facd86003a6c2d27604d553939f7ef3577`
then equivalently rebased to `48f2983e3cf6b5b72a21c254f744ad8e7d62a123`
on fresh staging `742eb30cb1a8b6766c85e915d26b0400e38244b1`. The new head
subsequently passed affected independent review and was published under the
lead's explicit lease instruction. New run `41740116653`, attempt 1, is bound
to exact `48f2983...`; acceptance remains pending. The old attempt's scoped
cancellation request was accepted, with completion still pending in A's last
bounded check. No CI/runtime acceptance is claimed.

## Facts and boundary

- [Build job 126191705303](https://github.com/vpsfreecz/vpsadminos/actions/runs/41714748110/job/126191705303)
  built and captured sites output
  `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`.
  Raw build log lines 3460–3466 record successful construction and unchanged
  normal producer `qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
  module SHA256
  `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
- Build log lines 3518–3519 explicitly record copying both the normal toplevel
  and the exact sites path to `ssh://push@cache.int.vpsadminos.org`, sites at
  `2026-11-03T22:05:43Z`. Omission from SSH copy is ruled out. The subsequent
  profile call passes only `BRANCH` and `BUILD_OUT`.
- [Intel job 126236869931](https://github.com/vpsfreecz/vpsadminos/actions/runs/41714748110/job/126236869931),
  running on `gh-runner2`, passed source/lock/producer identity checks, then
  failed at the sites substitution boundary. Raw lines 234–237 at
  `2026-11-03T23:06:56Z` report no substituter for exact captured `aiqijl...`.
  No descriptor read, corrected/predecessor fixture setup, runner or VM was
  reached. Missing upload/test.log errors are secondary.
- Bounded public cache reads return sites narinfo HTTP 404, body
  `No such path.`, versus normal producer narinfo HTTP 200 with the existing
  cache signature. The saved sites response header is dated
  `Tue, 03 Nov 2026 23:11:05 GMT`.
- The separate test metadata output is outside the normal OS toplevel's
  dependency closure. The workflow publishes only that toplevel profile,
  leaving the copied sites path without a corresponding retention root.

Canonical cache-policy source was inspected read-only in
`vpsfreecz/vpsadminos-org-configuration`, revision
`f924aabd0a774d88d173419527215cf4b538168a`,
[`cluster/org.vpsadminos/int.cache/config.nix`](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/f924aabd0a774d88d173419527215cf4b538168a/cluster/org.vpsadminos/int.cache/config.nix).
Its `push-ci-generation` accepts exactly branch plus one store path, applies
`basename` to the branch, and uses `nix-env --set` at
`/nix/var/nix/profiles/ci-BRANCH-profile`. Daily `ci-gc` removes old recognized
profiles/generations and then collects unrooted store paths. Feature profiles
use 90-day retention. Nix-serve supplies the cache signature; the canonical
proxy forwards its responses.

The demonstrated defect is missing retention, rather than a failed copy or
changed captured identity. Garbage collection can remove this unrooted path
and is consistent with the observed loss. Actual deletion timing is **not
journal-proven**; no server journal or live-cache mutation was performed.

## Small correction and checks

Only `.github/workflows/ci.yml` changes: 11 insertions, 1 deletion.

1. `nix-build -A candidateSites` creates the ordinary local outlink
   `$RUNNER_TEMP/livepatch-sites-GITHUB_RUN_ID-GITHUB_RUN_ATTEMPT`, keeping the
   exact selected output rooted during the build job. It still captures the
   same returned store path once and performs all existing identity checks.
2. After the existing copy and toplevel-profile publication, a conditional
   second call publishes that exact `LIVEPATCH_SITES_OUT` via the existing
   helper with `BRANCH-livepatch-sites`. No server/API/configuration changes.

For this workflow branch the deterministic profiles are distinct:

```text
ci-2026-11-03-livepatch-fixture-failures-profile
ci-2026-11-03-livepatch-fixture-failures-livepatch-sites-profile
```

The existing helper/90-day policy handles the latter. Focused/ZTS jobs retain
the identical capture/matrix skip condition, and absent/empty sites output
continues to publish only the ordinary toplevel profile. Normal producer,
module digest, schema/descriptor semantics, predecessors, boot inputs, matrix
and recovery contracts are unchanged.

Passed bounded checks with no builds or guests:

- 19 actual-workflow identity/retention controls, including local output-link
  arguments and run/attempt separation, both exact remote profile arguments,
  absent/empty sites skips, nested-branch `basename` behavior, and all prior
  digest/source/input/producer/site-record rejection cases. Builds and SSH
  are stubbed; real Nix JSON/assertions and shell checksums run.
  [Control log](package-a-retention-check.log),
  [disposable harness](package-a-identity-check.py).
- Ruby stdlib YAML parse, equality of capture and lifecycle guards, retained
  nine-row matrix, Bash syntax of capture/copy/publication/row scripts, A Nix
  source parsing and repository whitespace checks.
- Non-stashing Overcommit Diff hooks passed in the exact cached declared
  Ruby 3.4.11/nixfmt 1.5.0/.gems environment, with no broad shell realization.
  [Hook log](package-a-retention-hooks.log).
- Bounded official release checks still select checkout v7.0.1 and
  upload-artifact v7.0.2 via the existing v7 refs; no action ref changes.

Source is frozen for affected independent committed review. Diagnosis and
controls performed no remote/cache/CI/VM mutation; later explicitly coordinated
Git slots preserved the tested `efc5f8fe...` and pre-rebase `06d373fa...` local
backup refs, amended only the workflow with mandatory hooks, then proved a
conflict-free equivalent rebase. All prior backup refs remain. The complete
proof is in [A's receipt](package-a-result.md). No push, CI retry/cancel/dispatch,
server/configuration, producer/pin, merge, deployment or lifecycle action was
performed during those preparation slots. Subsequent separately authorized
publication and obsolete-run cancellation are recorded in A's current receipt.
The new exact CI attempt must establish successful sites restoration and all
required runtime witnesses/nine rows. This failed attempt cannot satisfy merge
acceptance.

## Preserved raw evidence

The sole watcher supplied both completed-job logs; A did not refetch them:

| File | SHA256 |
| --- | --- |
| `ci-41714748110-build-job.log` | `84bab27b06c2e0ef63cb8558d6fe2ec39b7a246991f7e15858489260878098fb` |
| `ci-41714748110-intel-job.log` | `ca927242eda000fba4dfa6f6e2037f0494aca7145772858693796bdebc1ed263` |

Public receipts: `ci-sites-narinfo.headers`, `ci-sites.narinfo` (404),
`ci-producer-narinfo.headers`, `ci-producer.narinfo` (200).

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
