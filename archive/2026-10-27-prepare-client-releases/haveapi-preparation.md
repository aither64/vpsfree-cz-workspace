# HaveAPI 0.31.0 preparation

Owner: implementer0. Fixture repair, focused checks, affected final review and
the broader performance specs pass. **HaveAPI 0.31.0 is published and verified
at every required destination**, including Packagist and the public GitHub
Release. PHP mirror integration is complete; see [PHP receipt](php-preparation.md).
HaveAPI source/default integration remains outside this release authorization.

## Source and scope

- Repository: `git@github.com:vpsfreecz/haveapi.git`.
- Worktree: `worktrees/2026-10-27-prepare-client-releases/haveapi`.
- Branch: `haveapi-0.31`.
- Fresh `origin/master` base: `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`.
- Current head: `c9124da141adc258fbbaf67d4ec19ee3f8580849`.
- Complete base-to-head series: `3bbb98e7 release: prepare HaveAPI 0.31.0`,
  then `c9124da1 servers/ruby: isolate maintenance lineage test versions`.
- Diff: 19 files, 141 insertions and 35 deletions. All maintained components
  advance together: Ruby server/client/Go/Rust/TypeScript gems, npm/browser,
  PHP/Composer and Python. Elixir remains excluded by the release procedure.
- No migrations, persisted-state changes, protocol changes, deployment,
  superseded approaches, repeated dependency/pin streams or externally consumed
  revisions in this release-preparation range.

The new changelog uses the lead's final editorial pass. Actual new changes were
identified by comparing released `v0.30.2` and development trees: commit-list
comparison overcounts backported fixes. Exact published 0.30.1 and 0.30.2
entries are retained byte-for-byte. The existing release/development guides
already document the operation, so no lasting procedure edit was needed.

## Preparation and quick evidence

- `dev-session current` and both identity environment values matched this exact
  session and `/home/aither/workspace/ai/vpsfree.cz`.
- `git --git-dir=repos/haveapi.git fetch origin`: current remote base above;
  stale bare local `master` was not used.
- `dev-session worktree add ... haveapi --as-is --branch haveapi-0.31 --base
  origin/master --no-fetch`: initial checkout completed but the unsigned
  Overcommit configuration caused exit 1. Inspected `.overcommit.yml` and both
  custom hooks, installed and signed through the top-level Nix shell, then
  repeated the registration successfully. No bypass.
- `nix develop -c make release-deps`: passed, exit 0, 177 seconds in a fresh
  catalog-selected Luna/low watcher; log `haveapi-release-deps.log`, status
  `haveapi-release-deps.status`. No process remains running.
- `nix develop -c bash -euo pipefail -c 'bundle exec overcommit --install &&
  bundle exec overcommit --sign'`: passed.
- `nix develop -c make version VERSION=0.31.0`: passed.
- `nix develop -c make release-check`: both metadata and prepared input checks
  passed at 0.31.0.
- `nix develop -c make release-test`: passed, exit 0, 24 seconds in a fresh
  Luna/low watcher at the final committed head: 213 Ruby examples, zero failures;
  six Python artifact tests, OK. Log `haveapi-release-test.log`, status
  `haveapi-release-test.status`. Existing Rust VERSION constant redefinition
  and gemspec advisory warnings did not fail the check.
- Mandatory commit hooks: HaveapiI18n, PythonChecks, PhpCsFixer and RuboCop all
  passed. Commit-message hooks passed, with only the framework's optional
  72-column warning on body lines that satisfy the repository's 80-column rule.
- `git diff --check origin/master..HEAD`: passed. Worktree clean after commit.

All ten prepared dependency locks were copied to
`haveapi-locks-before-version/` before versioning. Comparison confirms only
coordinated identity/version changes in the ignored npm, uv, Rust and TypeScript
locks; all external dependency records and the other six locks are unchanged.
An initial inspection assertion incorrectly expected unchanged locks to advance;
the corrected comparison explicitly accepts byte-identical locks. No lockfiles
were staged. `make version`'s prescribed tracked JavaScript bundle change is
exactly one version line; no rebuilt declaration, documentation or package
artifact was staged.

## Remaining work

No release-delivery work remains. Lead owns session tracking and any separately
authorized source/default integration. Keep feature refs and the original
failed-tag recovery ref; no session lifecycle action is authorized.

## Published refs and validation

After lead-reported final review cleared the exact range without findings,
the lead authorized branch and annotated tag publication. Fresh remote master
remained the recorded base; the branch and tag were absent. Both SSH pushes
succeeded in the top-level Nix shell with normal hooks.

- `refs/heads/haveapi-0.31`:
  `3bbb98e76e286d64707c368fe1c2cc4d03f35eed`.
- Annotated `refs/tags/v0.31.0` object:
  `73eb7726a245804b8aa3abdff9181772f827d2d9`.
- Peeled tag: `3bbb98e76e286d64707c368fe1c2cc4d03f35eed`.
- Branch release workflow:
  https://github.com/vpsfreecz/haveapi/actions/runs/40551776399 .
- Tag release workflow:
  https://github.com/vpsfreecz/haveapi/actions/runs/40551850652 .

A fresh catalog-selected Luna/low watcher monitors those exact runs, stopping
when the branch completes and the tag build completes at its protected gate,
or reporting failure evidence. No protected-environment approval is delegated.

## Tagged build failure

Run `40551850652`, job `122357410158`, failed at 2026-10-27T17:36:45Z in
`Test and build maintained packages`: server specs had 637 examples and seven
failures, all in `spec/performance/release_lineage_spec.rb`. Full failed log:
`haveapi-ci-tag-40551850652-failed.log`; status JSON:
`haveapi-ci-tag-40551850652.json`. Branch run `40551776399`, job
`122357147410`, completed with the same 637 examples and seven failures.
Its failed log/status are retained under the corresponding
`haveapi-ci-branch-40551776399` prefix. The watcher finished; no operation
remains running. The tag artifact API reports `total_count: 0`.

`HaveAPI::Performance::Release.version` deliberately accepts only `0.30.x`
for the proven maintenance-lineage normalizer. The test helper reads the live
checkout version and calls that normalizer before substituting a synthetic
0.30 version; at 0.31.0, constructing those fixtures fails. Worker receipt and
HTML examples also invoke the intentionally narrow release path on the live
0.31 checkout. This is reproducible source/test coupling, not a transient
registry failure. Keep the production maintenance restriction intact; route
the bounded fixture repair through the lead and architect before source edits.

The failed tag and original run remain unchanged. No blind retry or retag has
run. No retained tagged artifact is available for PHP preparation; the feature
and detached target mirror worktrees remain clean at
`a02dd2506209f54ea782fbd949243207bf9f93bc`. Source correction and release-version
recovery direction remain with the lead before this dependent package resumes.

## Fixture repair and recurrence prevention

Latest user direction keeps **0.31.0** and explicitly authorizes replacing only
the failed, unaccepted tag after repair, verification and final review. It
supersedes the brief earlier 0.31.1 selection. No 0.31.1 metadata or history
reconstruction ran. The original tagged source remains the first commit of
the final series; the existing changelog and version metadata are unchanged.

The bounded test-only commit is `c9124da141adc258fbbaf67d4ec19ee3f8580849`:

- `contents` reads the template's own version before substituting synthetic
  values, without first applying the production 0.30 validation to the template.
- One owned temporary 0.30.2 source supplies real worker input and HTML paths;
  loaded local component versions are scoped to the receipt example. Ordinary
  input validation, 0.30.99 loaded-version rejection, actual measurement,
  retained raw-body assertions and served-HTML/replay coverage remain.
- Synchronized 0.31.0 rejection proves the production guard remains narrow.
- A new regression constructs a synchronized 0.32.0 template, scopes only that
  example's root helper to it, successfully captures synthesized 0.30.2 data,
  and explicitly rejects synchronized 0.32.0 normalization.

Final quick batch on actual source VERSION 0.31.0, in top-level `nix develop`:
`make doc`, then server `bundle exec rspec
spec/performance/release_lineage_spec.rb` and root `bundle exec rubocop
servers/ruby/spec/performance/release_lineage_spec.rb`: passed, 18 examples,
zero failures (seed 63695, specs 8.55 seconds), no RuboCop offenses. The initial
17-example batch passed through a fresh watcher; its log/status are
`haveapi-fixture-focus.{log,status}`. The final known-quick batch ran inline
after adding the later-minor regression.

Required i18n and RuboCop commit hooks passed; commit-message hooks passed with
only optional 72-column warnings inside the 80-column rule. Full-range
`git diff --check` passes. Only this spec differs from the reviewed metadata
head; production benchmarks, runtime, budgets, reference, workflows and all
version/changelog files remain byte-identical. No migrations or repeated
update streams were added.

No post-fix branch push or tag replacement has run. The old tag object
`73eb7726a245804b8aa3abdff9181772f827d2d9`, old source
`3bbb98e76e286d64707c368fe1c2cc4d03f35eed` and failed-run receipts remain
recorded. The lead gates operational execution after affected final review;
replacement requires the exact-old-object lease in the accepted brief.

Before any replacement, the original annotated object was also preserved using
create-only `git update-ref` under normal local recovery ref
`refs/recovery/2026-10-27-prepare-client-releases/v0.31.0-failed`. Readback proves
the exact old tag object and peeled source above. This ref is outside
`refs/tags/v*`; it was not pushed and triggered no workflow. The actual release
tag remains unchanged pending review and the lead's execution instruction.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/

## Reviewed failed-tag recovery execution

Affected final review cleared exact `c9124da141adc258fbbaf67d4ec19ee3f8580849`
without findings; see `fixture-review.md`. The lead then authorized the complete
recovery package under the user's explicit keep-0.31.0/fix/retry override.

- Required broader `nix develop -c make test-performance`: fresh Luna/low
  watcher, exit 0, 84 seconds, 160 examples and zero failures. Source stayed
  fixed and tracked-clean at the reviewed head. Log/status:
  `haveapi-performance-recovery.{log,status}`.
- Fresh preflight near 2026-10-27T17:49:49Z: old remote tag object/source and
  branch were unchanged; failed tagged run still had zero retained artifacts.
  Exact 0.31.0 endpoints returned 404 for all five gems, npm, PyPI and GitHub
  Release. PHP mirror still had no 0.31.0 tag and master stayed at its 0.30.2
  source. These reads establish no observed accepted version; they do not claim
  registry name ownership.
- Branch SSH push fast-forwarded `3bbb98e7` to `c9124da1`. Recreated the
  annotated `v0.31.0` locally at the reviewed head and pushed only that tag with
  `--force-with-lease=refs/tags/v0.31.0:73eb7726a245804b8aa3abdff9181772f827d2d9`.
  Both commands ran in the top-level Nix shell with normal hooks.
- New tag object: `d300dfa8715cca35c29bce312333ece886b5e74e`; peeled source:
  `c9124da141adc258fbbaf67d4ec19ee3f8580849`. Fresh `git ls-remote` proved the
  branch/new tag/source exactly and unchanged master
  `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`. The old annotated object remains
  under the local recovery ref; no other tag changed.
- Comparison recaptured for base `4d36efcf` and head `c9124da1`. No superseded
  queued/running branch workflows remained to cancel.
- Corrected tagged release workflow:
  https://github.com/vpsfreecz/haveapi/actions/runs/40554625752 . Exact current
  head native run inventory is `haveapi-recovery-runs.json`. The spec-only
  branch push does not match release.yml's path filter, so only its tag event
  starts the coordinated release batch; native component checks still run.

Fresh-agent delegation became unavailable in the current tool set after the
performance watcher finished. Reported that once to the lead and used the
monitoring skill's bounded parent fallback for these exact native runs. No
local full release build or protected approval ran.

The corrected tag build subsequently passed and retained original artifact
`12756023295` (`release-40554625752`). Exact-source tools-only artifact
verification passed. All other 19 current-head native workflows completed
successfully. The protected `release` environment is waiting, with reviewer
`aither64`; it has not been approved. The original manifest, payload identities
and verified PHP snapshot candidate are recorded in `php-preparation.md`.

## Final publication receipt

The user explicitly approved PHP master/tag synchronization, PHP-first order
and protected HaveAPI publication. Lead completed and remotely verified the
PHP integration, then released claim
`18deacb8-41f8-41c8-915f-d03ef92c8645` with authoritative released readback at
2026-10-27T18:07:40Z before approving protected environment `24722193856`.
Deployment `7366320231` and publish job `122371179918` belong to exact run
`40554625752` and source `c9124da141adc258fbbaf67d4ec19ee3f8580849`.

Both build and publish jobs completed **success**. Public GitHub Release
[v0.31.0](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.0), ID
`425817748`, is non-draft/non-prerelease, published 2026-10-27T18:13:31Z.
Fresh remote tag readback remains annotated object
`d300dfa8715cca35c29bce312333ece886b5e74e`, peeled source `c9124da1`.

Read-only checks through the existing exact-source `Publisher` passed at
2026-10-27T18:16:02Z. Every RubyGems response had the exact gem name, version
0.31.0, platform `ruby` and the original retained SHA256:

| Gem | SHA256 |
| --- | --- |
| haveapi-client | `513e0ecde4c7afa289e970503e9a588507f70de051354c2fa95e0f5f3fd9254a` |
| haveapi | `c4e535b8f760ddd4feeeb79f7a239fcffe3df6cde9bb7a41e06d9474ec6fe541` |
| haveapi-go-client | `fe1a0ac06ad643d11bbbea8d9d541156d4230517c21465c1f3f2a7103a0906ed` |
| haveapi-rust-client | `28f5411113f7780b6e3d76a22aa5191e18abe18ed3ae02e167b19be4bb452d2b` |
| haveapi-typescript-client | `34815ad52c59f59513f710fb123d290536ec9886ecd11634f53262964f69f6ff` |

npm `haveapi-client@0.31.0` name/version and tarball integrity match:
`sha512-KdEEu7jMFWFTHBVWtSSjZoB6WA68BDSE68IMW8LXUverfcg8V1tzptBcgu+IUOwOcqayq9OaPxJX676Cir+S0g==`.
Both PyPI files and their exact hashes match:

| File | SHA256 |
| --- | --- |
| haveapi_client-0.31.0-py3-none-any.whl | `016a08dfe2ca6c629034bb2308267c234a21cb00edda019bd56a206e8c1e1aca` |
| haveapi_client-0.31.0.tar.gz | `75c48e61e7cb87639f6b0e32f4beca4cd458a3a591a99b1afbb9e1f41d78f7cf` |

PHP remote master and peeled v0.31.0 remain
`eafc2a9b77990dd5c927f0d412d14801261223cc`, tag object
`fe2e2355933f334244e8bb80a31ce4bd6c02af4f`. Packagist initially lagged, then
both fresh p2 metadata and cache-distinct package JSON listed `haveapi/client`
0.31.0 (normalized 0.31.0.0), with source and distribution references exactly
equal to that PHP commit. No webhook/settings changes, redelivery or tag retry
were needed.

Downloaded all 12 public Release assets to
`haveapi-public-assets-40554625752/`. Their name set, GitHub SHA256 digests and
actual downloaded bytes match all 11 original payloads plus the original
manifest. The public manifest is byte-identical to the retained tag manifest,
SHA256 `6e31e4c59e4629adeff0fd8f00e86935b644b6018c3d53361450b07a1b102a49`;
tools-only `cli.rb verify` also passed against the public assets. It retains
the complete ten-lock input graph and exact source/tool identities.

The new TypeScript gem now exists at 0.31.0 with the expected hash. Public
RubyGems v1/v2 APIs return empty `metadata` and no trusted-publisher fields;
the public gem page exposes no publisher identity. Its first trusted upload
succeeded, but account-level conversion from pending to normal publisher was
not separately observable through these public sources.

Evidence: `haveapi-publication-run.json`, `haveapi-publication-job.log` and
`haveapi-public-release.json`. The workflow log confirms all five gems, npm,
the existing PHP tag and final Release completion. No duplicate publishing
command, repack, rebuild or retry ran. No operation remains running under this
verification package; no repository claim or machine reservation is held.
