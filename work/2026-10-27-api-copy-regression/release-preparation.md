# HaveAPI 0.31.1 release preparation

Owner: implementer2. Lead owns integration claims, final user-facing changelog,
independent review, tag and publication coordination.

Current status: final A/B/C backports followed by separate 0.31.1 metadata at
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42` passed independent complete final review
without findings and are published on the feature branch only. Corrected C's
ordinary server-bundle check passes (11 examples, 0 failures), as do release-check
and required commit hooks. The prior five optional-gem fixture failures were fixed
by the source owner without changing production code or dependencies. Exact-head
Feature CI passed all eleven workflows and retained artifacts passed parent
verification. Lead integrated maintenance, created `v0.31.1`, and approved the
exact tag candidate. Publication succeeded, and all public destinations including
Packagist are verified. The release execution/verification package is complete;
lead owns the final integration proofs and session handoff. Session remains open.

## Final publication receipt

[HaveAPI 0.31.1](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.1)
was published at 22:21:55 UTC on 2026-10-27. Exact source:
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`. Release run `40592240342` and publish
job `122502527148` both concluded success. Lead approved deployment `7371733214`
for the exact waiting `release` environment/candidate; implementer and watcher
performed only read-only observation and verification after that approval.

A new standalone Luna/low watcher used explicit `danger-full-access` / approval
`never`, with the retained utility catalog/identity and verified current selected
package policy. Its actual launch header is retained in
`release-publication-watcher.log` (thread `01a17f73-ca15-7c71-81c6-1579eb5a4e1a`).
It completed and owns no running operation. Utility slot is free.

Parent validated public destinations against the original approved tag artifacts:

- All twelve GitHub Release assets, including eleven release files and the
  manifest, are byte-identical to the approved candidate. Release is public,
  not a draft. Approved/public manifest SHA-256:
  `cfcdd41cba3984d07223db9261b1fae81b9ae919aeeddbb8873490321ca0473d`.
- RubyGems `haveapi`, `haveapi-client`, `haveapi-go-client`,
  `haveapi-rust-client` and `haveapi-typescript-client` 0.31.1 have matching
  identities, `ruby` platform and retained SHA-256 values.
- npm `haveapi-client` 0.31.1 has the retained tarball's SHA-512 integrity.
- PyPI `haveapi-client` 0.31.1 contains exactly the wheel and sdist, both with
  retained SHA-256 values.
- PHP mirror `master` and annotated `v0.31.1` peel to
  `29db964d90b69aa8a37518d5f16ca7e9743fa638` (tag object
  `bd7a54f14d22d868ea843961ae2a5e977f94a16a`). Commit provenance names exact
  HaveAPI source `d49cfa3f`. All 36 nonprotected snapshot files match approved
  archive contents and Git modes; mirror-owned `.github`/`AGENTS.md` are preserved.
- Packagist separately indexes actual version 0.31.1, with both source and
  distribution reference `29db964d90b69aa8a37518d5f16ca7e9743fa638`.

Raw public metadata, headers, final run/job status, job log, release assets and PHP
tree proof are under `release-publication-evidence/`. The compact accepted result
is `accepted-publication-receipt.json` there. No publication/index/cache uncertainty
remains. No retry, reupload, rebuild, manual workflow dispatch, cancellation or
additional external write was performed. The maintenance SQLite timing diagnostic
below remains accurately inconclusive; publication did not trigger a performance
retry or budget change. No cleanup or session lifecycle action was taken.

## Final maintenance/tag event checkpoint

Lead reported approved maintenance integration and annotated tag completion:
remote `haveapi-0.31` is exact `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`;
`v0.31.1` tag object `4d665d6bc1a2f6a62710219150afd2175c312347` peels to that
exact head. The atomic SSH push followed fresh old-target/source/tag-absence
checks and ordinary fast-forward hooks under lead's repository claim, explicitly
released at 22:07:01 UTC. No implementation-owned repository claim is held.

Discovered 21 exact-head push runs at 22:06:48 UTC, recorded in
`release-final-event-runs.json`: eleven on `haveapi-0.31` and ten on `v0.31.1`.
Distinct protected tag release run: `40592240342`; maintenance build-only release:
`40592241396`; maintenance performance: `40592241388`. Tag's nine other automatic
checks passed at the initial observation. A fresh retained Luna/low watcher owns
all discovered event observation, with current `full_access` policy verified
against selected package `pq2jwjcv4hbyiwzcam50x6j9fv008qiq`; parent does not poll
the same runs. Stop boundary: any concrete failure, or all required maintenance
checks passed and the tag's own successful candidate is retained and waiting for
protected approval. Pending deployment identity and exact tag artifacts must be
retained. Watcher and implementer must not approve publication, rerun workflows,
cancel runs, dispatch new work or change refs. Parent will verify the tag's own
candidate and actual maintenance 0.31.0 → 0.31.1 performance receipts.

The watcher reached that boundary and ended with all runs accounted for: eleven
maintenance workflows and nine automatic tag workflows succeeded. Protected tag
release `40592240342` remains **waiting**, with successful build job
`122499154029` and waiting publish job `122502527148`. This is twenty terminal
successes and one waiting protected run, not twenty-one completed workflows.
The `release` environment has ID `24722193856`; retained pending-deployment data
reports `current_user_can_approve: true`, reviewer `aither64`, wait timer zero.
No approval was submitted by implementer or watcher. Utility slot is free.

Parent verified the tag workflow's own candidate with the existing tools-only
Nix `ruby utils/release/cli.rb verify` command: passed for exact source
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, tag `v0.31.1`, version 0.31.1,
run `40592240342`, eleven files/checksums and ten retained locks. Its manifest
SHA-256 is
`cfcdd41cba3984d07223db9261b1fae81b9ae919aeeddbb8873490321ca0473d`.
No branch artifact was substituted for this tag candidate and no local rebuild
was run. Artifacts/logs/status snapshots are under `release-final-ci-artifacts/`;
compact validation is `validated-candidate-receipt.json` there.

Maintenance performance `40592241388` selected exact old target `c9124da1`, own
0.31.0, to exact candidate `d49cfa3f`, own 0.31.1. Parent matched all seven raw
source-version contents/hashes on each side against exact Git blobs, verified
equal normalized source hashes and unchanged remaining dependency graphs, and
matched the runtime/activated-gem and benchmark lock/normalized-manifest graph in
all nineteen observations. The all-client contract passed 108 examples with zero
failures. All fourteen correctness and allocation classifications passed, with
no regression, error or deterministic failure.

The timing result remains **inconclusive**, not a measured pass: thirteen cases
passed and `sqlite.includes` (32 rows, include depth 2) was inconclusive for both
wall and CPU, yielding 26 passing and two inconclusive timing classifications.
Both had adequate signal, three of five pass agreements and zero regression
agreements. Baseline batches were 0.956484208 seconds wall / 0.95639803 CPU;
noise was 0.000813387529 wall / 0.000813232623 CPU seconds per request. Existing
policy leaves this diagnostic and CI succeeded; lead accepted recording the
residual limit without retrying or changing budgets. Protected approval remains
the lead's next action after reviewing these facts.

## Feature publication and hosted verification

After final review acceptance, fresh fetch and SSH ref proof confirmed maintenance
target `c9124da141adc258fbbaf67d4ec19ee3f8580849` and published source feature
`2fc2b8f86c71a6062434bb60a24e174b20c1a520`. The release feature remained clean at
the reviewed final head; no rebase was needed. An ambient pre-push signature check
refused before a remote release feature existed. Unchanged config/custom hooks
and absent remote feature were verified, then the ordinary SSH push in the declared
tools-only top-level Nix shell passed with hooks enabled and no trust changes.
Remote proof confirms exact release feature
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, unchanged source feature and unchanged
maintenance target.

Eleven actual push workflows were discovered at that exact release head.
`release-ci-runs.json` retains IDs, names, event, full SHA and URLs. Build-only
release run is `40590671173`; performance run is `40590671268`. Others cover Ruby
server/client, Go, Rust, JavaScript, PHP, Python, i18n and RuboCop. Initial states
were queued/in progress. Source owner0 retains the single watcher utility, so
this package visibly uses 30-second interruptible parent observation for release
runs only, without source-CI polling. When source owner0 freed the utility, a fresh
retained Luna/low watcher took only the two remaining exact release/performance
runs. Selected package `pq2jwjcv4hbyiwzcam50x6j9fv008qiq` execution policy was
verified `full_access`, with the retained catalog/model/effort/native identity
unchanged. Parent polling stopped until the watcher reported both terminal
success and downloaded artifacts. The watcher finished; utility ownership is
free and no commands remain running.

Final hosted evidence is verified:

- All eleven exact-head workflows are terminal success. IDs, full SHA, event,
  names and URLs are retained in `release-ci-runs.json`.
- Performance run `40590671268` is a measured pass: 14 cases, all 28 wall/CPU
  classifications pass, all 14 allocation classifications pass, zero inconclusive
  results. All-client contract: 108 examples, 0 failures.
- Actual selection: baseline `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`, own version
  **0.30.0**, to candidate `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, own version
  **0.31.1**. This new-branch push used the merge-base with captured default;
  it did not select maintenance version 0.31.0 as its baseline.
- Parent checked all seven retained source-version raw contents and hashes for
  each side against the exact Git blobs, equal normalized source hashes, and
  equal remaining config/gemspec graphs. The runtime/activated-gem graph and
  benchmark lock/normalized-manifest graph match in all 19 observations.
- Build-only release run `40590671173` retained source `d49cfa3f`, version 0.31.1,
  eleven release files and ten lock texts. Existing tools-only Nix
  `ruby utils/release/cli.rb verify` passed all retained package/checksum checks.
  Release-manifest SHA-256:
  `b3e92fca2275bef34449fe61a5bf98eef535cb86fd2e18de8b4f33cd9f113016`.

Raw artifacts and full logs are under `release-ci-artifacts/`; compact independent
parent conclusions are in `release-ci-artifacts/validated-receipt.json`.
Branch artifacts establish build verification only: the tag workflow must build
and retain its own exact candidate before publication approval. No redundant
local full build/suite or retry campaign was run.

## Corrected final release range for review

Lead accepted the narrow test-fixture correction from source C
`51f591ff75551a5b9679cd83b9c1fa23be0bd1eb` to
`2fc2b8f86c71a6062434bb60a24e174b20c1a520`. Only 14 test-fixture lines changed;
production behavior and reviewed design stayed the same. Source owner proved
the old and corrected examples against the same ordinary bundle. This package
waited for source publication's Git window, then replaced only C and kept
metadata last through ordinary rebases and a full-trailer `cherry-pick -x`
prepared commit using `git commit -F` with original author/date. All hooks passed.

Unchanged initial base: `c9124da141adc258fbbaf67d4ec19ee3f8580849`.

| Final commit | Purpose / source |
| --- | --- |
| `f47aacc1545fc768743055d35aa4582821d97427` | A, source `2ff8931bf266037d2d0cbca8655491043c105e35` |
| `baa736f2f3e3c2e7a50027f7abdc019dca672f5a` | B, source `8ea2c365a430c931afcde3e161178bf71cee928d` |
| `4dd137d6f354f312ea09bf41b6063cd5f7519067` | corrected C, source `2fc2b8f86c71a6062434bb60a24e174b20c1a520` |
| `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42` | exact final 0.31.1 metadata patch |

Ordered stable patch IDs match all three sources:
`650192e900b59adbefb62cc8c5161e7baaa80be7`,
`8182dbb7d01331862a0a4be91e711b5366737d12`,
`2c35cc290e95e7f822ec588ded016928e80580c6`. All original authors/dates and full
`-x` trailers were verified. Complete source base `4d36efcf`..`2fc2b8f8` and
release base `c9124da1`..`4dd137d6` binary diffs are byte-identical, SHA-256
`dff375984e4597e5ac09ff309912597441bd6a65f6845217bbdf6715c4e36c2f`.
The complete source-to-release delta before metadata remains exactly the
pre-existing release-only metadata/test-isolation delta, SHA-256
`ba25f8982a9b20557e40edbdb8c0b4f608b86388805bb4081c6cff3b641cfb44`.
Metadata is byte-identical to the prior `cc469984..852e5b83` metadata patch,
SHA-256 `864d6b93452daa15f04d61707e40806b90e36e58034fa28d7df30a0d057499fe`:
18 files, 34 insertions and 17 deletions, exact lead-owned changelog and shared
0.31.1 versions/constraints. Initial A/B commits are unchanged.

The old `c9124da1..852e5b83` range is preserved by local feature ref
`2026-10-27-api-copy-regression-release-before-c-fixture-fix`, in addition to
the earlier `...-release-before-c` ref at `d39a22e5` and the detailed evidence.
The final four-commit history has no superseded implementation, repeated pin
streams or migrations. No source code was independently edited in this package.

Final ordinary acceptance:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euc '
make release-check
cd servers/ruby
bundle exec rspec spec/performance/source_versions_spec.rb
'
```

Exit 0: release metadata and prepared inputs valid at 0.31.1; 11 examples,
0 failures in 7.51 seconds (seed 7495). Log:
`release-final-ordinary-c-check.log`. Broader prior quick evidence remains valid:
16 TypeScript examples and 72 maintenance/event examples passed; the unchanged
99 passing examples from the prior mixed batch are retained in
`release-final-quick-checks.log`. Strict external dependency graph evidence
remains in `release-inputs-version-comparison.txt`; no dependency or prepared-lock
changes occurred in replacing C. Final tracked tree is clean and diff-check
passes. Long release build/tests remain deferred to the reviewed final tag
workflow, and lead owns integration and publication.

## Final three-source history preparation

Lead authorized reversible preparation in parallel with C review, then confirmed
accepted C review without findings. Source C
`51f591ff75551a5b9679cd83b9c1fa23be0bd1eb` was backported with its full `-x`
trailer and original author/date. An ordinary two-commit interactive rebase moved
C before metadata. Metadata was amended through `git commit --amend -F` to use
the updated exact lead-owned changelog text; all hooks passed. A/B commits remain
unchanged. No reset, stash or clean was used.

Final range starts at the unchanged initial base
`c9124da141adc258fbbaf67d4ec19ee3f8580849`:

1. `f47aacc1545fc768743055d35aa4582821d97427` — A source `2ff8931b`.
2. `baa736f2f3e3c2e7a50027f7abdc019dca672f5a` — B source `8ea2c365`.
3. `cc4699843f5e24ee1f42cfd0827d9d061c914f23` — C source `51f591ff`.
4. `852e5b838b7aa969d513da57c7b67b1f3e7e4688` — final 0.31.1 metadata.

C's ordered stable patch ID matches source:
`60a4b9ff76bcd2977ae8ce956530baa25a75bb85`. Combined three-source and three-backport
binary diffs are byte-identical, SHA-256
`e511d104ac45bc7eb2090487e65ed43a660e280c52a6009cb76a868dff2d15a5`.
The pre-metadata source-to-release delta remains exactly the original
release-only delta, SHA-256
`ba25f8982a9b20557e40edbdb8c0b4f608b86388805bb4081c6cff3b641cfb44`.
Appended final range and metadata evidence to the existing range-diff/metadata
files. The original `c9124da1..d39a22e5` range remains preserved at local feature
ref `2026-10-27-api-copy-regression-release-before-c` and in the evidence below.

Final metadata changes 18 files, 34 insertions/17 deletions, including the added
lead-owned C release-note bullet. No migrations or dependency pins were added;
there are no repeated dependency streams or obsolete implementation commits on
the final four-commit branch. Input graph comparison from the initial package
remains unchanged: C and reordering do not modify prepared locks.

`release-final-quick-checks.log` retains the failed focused batch: release-check
passed, then 104 examples completed in 39.17 seconds with five failures, all
`Benchmark dependencies do not satisfy fiddle ~> 1.1, >= 1.1.8` in the new
source-version preparation/worker examples. No test was blindly rerun and no
source change was made in this release checkout. Source owner owns the diagnosis
and any fix before a follow-up backport.

## Executed initial release package

Lead started this package after accepted mandatory source review of
`4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`..
`8ea2c365a430c931afcde3e161178bf71cee928d`. Git mutations were serialized with the
source publication owner. The clean release base remains
`c9124da141adc258fbbaf67d4ec19ee3f8580849`.

| Source | Backport |
| --- | --- |
| `2ff8931bf266037d2d0cbca8655491043c105e35` | `f47aacc1545fc768743055d35aa4582821d97427` |
| `8ea2c365a430c931afcde3e161178bf71cee928d` | `baa736f2f3e3c2e7a50027f7abdc019dca672f5a` |

Each backport used `cherry-pick -x --no-commit`, then an ordinary `git commit -F`
with original author/date and Git's prepared message. Exact full source trailers
are present. Declared pre-commit and commit-message hooks passed. Ordered stable
patch IDs are `650192e900b59adbefb62cc8c5161e7baaa80be7` and
`8182dbb7d01331862a0a4be91e711b5366737d12` on both ranges. Combined binary diffs
are byte-identical, SHA-256
`0bcf0688eb343c304a8aa3a1783e413011b9dbc3f91fd6eceff78d3ecc70556d`.
The source-to-release tree difference before versioning exactly preserves the
original 19 release-only metadata/test-isolation files; both binary delta hashes
are `ba25f8982a9b20557e40edbdb8c0b4f608b86388805bb4081c6cff3b641cfb44`.
See `release-backport-range-diff.txt` and `release-backport-patch-ids.txt`.

`make version VERSION=0.31.1` ran in the prepared tools-only top-level Nix shell.
The lead's exact `release-changelog.md` was prepended unchanged. Metadata commit
`d39a22e51b2a69bdcb79f0e4e493305df38e825a` changes 18 files, 32 insertions and
17 deletions: coordinated package versions, client constraints and release notes.
It contains no dependency pins or runtime changes. All HaveapiI18n, PythonChecks,
PhpCsFixer and RuboCop hooks passed. Existing TextWidth warns on message lines
above 72 characters; all remain within the required 80-character limit.
`release-metadata.diff` retains the exact initial metadata change.

Quick checks passed:

- `make release-check`: metadata and prepared inputs valid at 0.31.1, before and
  after the metadata commit.
- TypeScript documentation and performance specs: 16 examples, 0 failures.
- Server maintenance release-lineage and event-baseline specs: 72 examples,
  0 failures. Shared docs prepared with `make doc`.
- `git diff --check` and clean final tracked checkout.

`release-quick-checks.log` holds focused test results. Against the pre-version
snapshot, all ten locks retain byte-identical external records after narrowly
normalizing coordinated local HaveAPI versions. Only server, Rust, TypeScript,
npm and Python local own-version lock entries changed; no lock was staged.
`release-inputs-version-comparison.txt` contains normalized per-file hashes.
No migrations, obsolete implementations or repeated dependency-update streams
were introduced. A third source backport and final independent review remain.

Staging note: plain `git add` reports ignored parent `clients/js/dist` even for
its tracked bundle; it had already staged the owned metadata. Verified index
contents and used path-scoped `git add -u` to finish, without forcing ignored
locks or bypassing hooks.

## Prepared branch and authority

- Exact verified session: `2026-10-27-api-copy-regression`; both environment
  identity values match the thread binding and `dev-session current`.
- Retained roster: implementer2 is ready, `workspace_write`, Sol/xhigh.
- Repository: `git@github.com:vpsfreecz/haveapi.git`.
- Release worktree:
  `worktrees/2026-10-27-api-copy-regression/haveapi-release`.
- Feature branch: `2026-10-27-api-copy-regression-release`.
- Initial base: `c9124da141adc258fbbaf67d4ec19ee3f8580849`, from
  `origin/haveapi-0.31`. Intended integration target: `haveapi-0.31`.
- `v0.31.0` is annotated: tag object
  `d300dfa8715cca35c29bce312333ece886b5e74e`, peeled source
  `c9124da141adc258fbbaf67d4ec19ee3f8580849`.
- Compared with current master `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`,
  maintenance has release metadata `3bbb98e7` and test-version isolation
  `c9124da1`. There were no master-only commits at this preflight.

The requested worktree creation materialized the clean branch and manifest entry,
then returned exit 1 because its post-checkout Overcommit configuration signature
was absent for this checkout. Configuration and both custom hooks were inspected;
they match the selected maintenance base. Reconcile through ordinary hook setup
and repeat registration with `--no-fetch`; retain this exact initial base.
The automatic manifest target initially said `master`; lead corrected it to
`haveapi-0.31` without changing the base.

## Release contract

Repository `AGENTS.md`, release/development procedures and the architect brief
were read. `haveapi-0.31` is the newest supported release branch. Backport every
new source/test commit with `git cherry-pick -x`, preserving the maintenance-only
commits and proving patch equivalence before metadata changes.

Use the top-level Nix shell. First prepare `make release-deps`, then run
`make version VERSION=0.31.1` only after release-package start. Keep local library
locks untracked and prove external dependency records unchanged during versioning.
Lead supplies the changelog text. Run `make release-check` and declared hooks,
with source/backport commits separate from release metadata. Do not run a full
local release campaign before independent review.

All maintained packages share the version: five Ruby gems, combined JavaScript
and TypeScript npm package/browser bundle, PHP mirror and Python package. No API,
database, persisted-format or deployment migration is introduced. Existing release
procedure owns partial publication recovery with original tagged source and
retained artifacts; never move an existing tag or replace an accepted package.

## Dependency preparation

Source implementer dependency preparation took priority. After its utility
finished, the lead reserved the single shared watcher slot for release prep.
A fresh native `prepare_release_dependencies` watcher uses the pinned catalog
`3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`,
`gpt-6-luna`/low, utility identity
`dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b`, with installed
`danger-full-access` and approval `never` policy. Command:
`nix develop -c make release-deps`, in this exact release worktree at the initial
base. No source, version, tag, publication or integration action was assigned.
Logs are `release-dependencies.log` and `release-dependencies.exit` beside this
record. Preparation passed, exit 0 in 161 seconds. The watcher has finished and
the shared slot was released to source-check preparation. Its first auxiliary
HEAD read used the shared workspace cwd; explicit release-worktree HEAD and
`/proc` cwd checks resolved that observation. The dependency command itself ran
in the correct release checkout.

After preparation, a quick tools-only top-level Nix shell confirmed the root
bundle, updated the Overcommit configuration signature, confirmed custom hook
signatures and an executable pre-commit hook, and ran post-checkout successfully.
Tracked checkout remains clean at the exact initial base. A `--no-fetch`
registration retry encountered the session writer lock before any change; the
next retry succeeded. Preparation is ready, pending reviewed source commits and
the lead's release-package start instruction.

Before versioning, captured all ten lockfiles listed by existing
`HaveAPI::Release::Artifacts::LOCK_PATHS` using `tar` and `sha256sum` only.
`release-inputs-before-version.tar.gz` retains the exact inputs for later diff;
archive SHA-256 is
`1e12e0488a4a0b447d8e8f10955a343c7ad56cca73f073db5665e891775ce22e`.
`release-inputs-before-version.sha256` records per-file hashes. These are local
disposable evidence, not project manifests or tracked library locks. The release
checkout remains clean at `c9124da1`; no broad tests were run.

## Prepared integration target

Lead assigned the detached, unregistered
`worktrees/2026-10-27-api-copy-regression/haveapi-release-target` checkout.
Creation was serialized with the source package owner and followed a successful
`git fetch origin`. It starts at fresh `origin/haveapi-0.31`, exact base
`c9124da141adc258fbbaf67d4ec19ee3f8580849`, with detached HEAD and a clean tracked
checkout. The usual initial post-checkout signature refusal was reconciled:
configuration and custom hooks match the prepared release checkout; the target
has an ignored `.gems` symlink to `../haveapi-release/.gems` and matching ignored
root `Gemfile.lock`. A tools-only Nix shell confirmed the root bundle, signed
configuration, confirmed custom hook signatures and executable pre-commit, and
ran post-checkout successfully. No package installation, test, build, claim,
merge or push was run in the target. Lead must recheck the exact remote target,
feature head and cleanliness inside the later short merge claim.

No project documentation edit is useful for preparation alone: the existing
release procedure already describes versioning, verification and recovery.
