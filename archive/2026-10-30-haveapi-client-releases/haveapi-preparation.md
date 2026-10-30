# HaveAPI 0.32.0 preparation

Owner: implementer0. This record covers feature preparation only. Integration,
release branch/tag creation, registry publication and PHP mirror writes remain
with the lead and require their separate approvals.

## Source and history

- Canonical origin: `git@github.com:vpsfreecz/haveapi.git`.
- Fetched 2026-10-30; `origin/master` remains
  `7edb003dd5d5a058b3308510bb8a5f60387ad654` (`VERSION=0.31.0`).
- Latest fetched tag: annotated `v0.31.2`, object
  `815c033be8cfca22822d0b2f80c022e959c5d0c4`, commit
  `819bba5110e089465535ecd71ca2eb37a7d39caa`.
- Feature branch: `2026-10-30-haveapi-client-releases`; worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/haveapi`.
- Initial base: `7edb003dd5d5a058b3308510bb8a5f60387ad654`.
- The release tag is not an ancestor of master. `git cherry origin/master
  v0.31.2` shows equivalent backports for TypeScript normalization, renderer
  performance coverage, package-version performance comparisons and Go token
  transport matching. Release metadata and the maintenance-lineage fixture
  adaptation differ intentionally. Master keeps patch zero.
- The 26 master commits after the release ancestry include documentation UI and
  OAuth sessions, example styling/shell escaping, formatting and package checks.
  They are existing upstream content; this feature prepares their next release.
- No migrations, persistent-format changes, deployment or coordinated node
  update are part of this package. Older clients keep their existing contracts;
  optional documentation OAuth requires the operator configuration documented
  in HaveAPI's `doc/documentation-oauth.md`.

## Preparation and publication preflight

- The first native worktree creation completed checkout but returned an inherited
  Overcommit configuration-signature refusal. The clean resulting checkout and
  correct branch/base were inspected before continuing. The ordinary session
  manifest already records this repository and exact base. Hook configuration
  and custom hook sources were inspected before signing.
- Dependency preparation uses the top-level Nix shell and `make release-deps`.
  A fresh verification utility owns the operation. Catalog digest
  `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`
  selects `gpt-6-luna` / `low`; installed access is `full_access`.
  Logs: [haveapi-logs/release-deps.log](haveapi-logs/release-deps.log).
- Exact 0.32.0 endpoints returned HTTP 404 for all five Ruby gems,
  npm `haveapi-client` and PyPI `haveapi-client`. Canonical and cache-distinct
  reads are recorded during preparation. This neither reserves a version nor
  proves publisher ownership; publication must repeat artifact-aware preflight.
- GitHub read-only preflight: `HAVEAPI_RELEASE_ENABLED=true`; `release`
  environment has a required reviewer, allows tags matching `v*`, and names the
  `HAVEAPI_PHP_DEPLOY_KEY` secret. Secret values were never read. Trusted
  publisher bindings, deploy-key validity, PHP mirror compatibility and
  Packagist indexing remain publication-time gates.
- Lead applied `vpsfree-user-facing-writing` and `humanizer-en` to the technical
  changelog draft and supplied the final insertion verbatim; only line wrapping
  changed during installation.

## Verification plan

Before final review: synchronized metadata and prepared-input checks,
`git diff --check`, passing declared Overcommit hooks, and clean tracked source
check. Preserve all resolved local lock bytes before/after `make version` and
confirm that external dependency records do not change.

After independent final review, in the same prepared top-level shell:

```sh
make release-test
make release
make test
ruby utils/release/cli.rb smoke-npm dist
ruby utils/release/cli.rb verify dist
(cd clients/python && uv run --locked python utils/package_smoke.py)
```

`make release` already includes the retained Rust and TypeScript generator smoke
checks; repeat only for a changed input or unresolved failure. Preserve original
release artifacts/manifest/locks. The lead coordinates CI and publication. Do
not launch the longer batch before independent final review.

## Candidate

- Head: `f0465630595b4fd120561337b3d1d7fa96cbe221`, clean tracked checkout.
- Complete feature series: one commit, `release: prepare HaveAPI 0.32.0`.
  Diff from base: 18 files, 50 insertions, 17 deletions. No obsolete approaches,
  transitional versions, migrations or substantive source fixes in this series.
- The five gem versions, npm package/source/bundled constant, PHP manifest and
  constant, Python package and example dependency are all `0.32.0`; server and
  generator internal client constraints are `~> 0.32.0`. Elixir and the private
  Rust runtime harness keep their independent/excluded versions.
- `make release-deps`: passed, 181.103 seconds, exit 0. `make version
  VERSION=0.32.0`: passed. `make release-check`, explicit metadata `--master`,
  `git diff --check`, and postcommit `check-clean --master`: passed.
- All declared Overcommit pre-commit hooks passed: HaveapiI18n, PythonChecks,
  PhpCsFixer, JsFormat and RuboCop. Commit-message hooks passed with informational
  72-column warnings; every message line is within the required 80 columns.
  Full hook output: [metadata-commit.log](haveapi-logs/metadata-commit.log).
- Prepared server/Ruby/Go local locks were synchronized with `bundle lock
  --local` after versioning, avoiding implicit changes by downstream commands.
  All ten retained external dependency graphs remain unchanged. The npm lock
  also changed indentation through the repository's version command; its parsed
  records differ only in the two own-package version fields. Rust/TypeScript
  locks differ only in own package/internal dependency identities; Python only
  in its own editable package version. Original and updated bytes are retained
  under `haveapi-logs/locks-{before,after}-version/`.
- Root release toolchain: Ruby `3.4.11`, Prettier `3.9.10`, rustfmt `1.10.0`.
  The prepared Rust bundle uses isolated `clients/rust/.gems` with root Ruby
  3.4.11. The downstream Rust SDK must use its own Ruby 3.3 bundle and pinned
  rustfmt 1.9.0 rather than reusing these native gems/formatter.
- Independent final review completed for `f0465630`: reviewer0,
  `gpt-6.1-sol` / `xhigh`, four lanes, no findings, explicit whole-history and
  no-migrations conclusion. Report: [haveapi-final-review-result.md](haveapi-final-review-result.md).
- Feature branch pushed over SSH after that review; remote proof confirms
  `f0465630595b4fd120561337b3d1d7fa96cbe221`. Default remains `7edb003d`.
  The first ambient push was refused by Overcommit configuration-signature
  validation, with no remote mutation. Re-signing and pushing from the
  documented Nix shell succeeded without bypassing hooks.
- Fresh Luna/low utility monitors all eleven exact-head push workflow runs.
  Primary release run: `41048321578`. CI metadata/artifacts and complete logs
  belong under `haveapi-logs/ci-41048321578/`.
- RuboCop `41048321587` and i18n health `41048321539` fail before project checks:
  default `.ruby-version=3.2.0` is unavailable from ruby-builder for the new
  `ubuntu-latest` (26.04) runner. Logs state Ruby 3.2.11/latest 3.2 is available.
  Minimal proposed workflow fix is explicit `ruby-version: '3.2'`, retaining
  the source floor; sent through lead/architect before editing. Original
  failures and successful exact-head results remain evidence. No blind rerun.
  Any new source SHA requires coordinated downstream provenance rebind.
- Lead approved the bounded two-workflow fix. New clean head:
  `0e7166a0f8f15827bfac051666a53bf449e999ec`, separate commit
  `ci: select the supported Ruby 3.2 patch for tooling`; adds only
  `ruby-version: '3.2'` to the two setup steps. Full feature series is now the
  release metadata commit plus this CI fix, 20 files / 52 insertions / 17
  deletions. No repeated pin/update streams or migrations. Push held for
  affected-lane independent review.
- `actionlint 1.7.12`, `git diff --check`, applicable Overcommit i18n hook and
  all commit-message hooks passed. Verified official current refs:
  ruby/setup-ruby `v1.335.0` /
  `7f797815d8adceb1c412e7abefdd1ab4abc47a5f`; actions/checkout `v7.0.1` /
  `3d3c42e5aac5ba805825da76410c181273ba90b1`. Existing pinned/floating refs
  already select those compatible releases; no action changes were necessary.
- The old and new head have identical VERSION, components, server, generator,
  templates, utility and Nix inputs. Recomputed shared-schema, Rust/TS generator,
  copied runtime and all ten resolved-lock identities are identical. The new
  JSON receipt is [candidate-identities-ci-fix.json](haveapi-logs/candidate-identities-ci-fix.json).
  SDK owners must update source SHA evidence deliberately while retaining the
  old candidate and original CI evidence. This proves relevant source/input
  equivalence, not byte identity between separate complete package builds.
- Affected-lane follow-up review passed with no findings for clean final head
  `0e7166a0f8f15827bfac051666a53bf449e999ec`. Feature push completed over SSH;
  fresh remote proof confirms that head. Before and after build-only release
  dispatch, remote feature head still matched. No default, tag, protected release
  approval, registry or PHP mirror writes.
- Final-source release workflow manually dispatched as `41049401404`, event
  `workflow_dispatch`. New exact-head push runs: RuboCop `41049392568`, i18n
  health `41049392525`, performance `41049392558`. A fresh Luna/low utility owns
  this batch. Final release artifact tests/manifest/locks are required; source
  equality alone does not reuse the previous complete build's verification.
- Original `f0465630` batch is complete: nine successes (release, performance,
  server RSpec, Ruby/Go/Rust/JS/PHP/Python client checks), two Ruby setup failures.
  Historical release run `41048321578` succeeded in 7m42s and retained artifact
  `12974415564`, digest
  `fc0748a466158911f8c126a37bfc932bbe2d61148b775bb7ef64f16ec5fbb867`.
  Original receipts, complete logs, manifest and all ten locks remain under
  `haveapi-logs/ci-41048321578/`. They are historical evidence, not the final
  source's package proof.
- Final exact-source batch completed: build-only release `41049401404` passed
  in 7m30s, i18n health `41049392525` passed, RuboCop `41049392568` passed.
  Performance `41049392558` completed its no-work selection successfully; this
  is not a new measured performance result. Final release's own full suite
  supplies component verification, not reused historical job conclusions.
- The release job ran `make release-deps`, translation health,
  `make release-test`, `make release`, `make test`, retained npm smoke and Python
  wheel/sdist smoke. Build packaging includes extracted Rust/TypeScript
  generator checks. Retained-artifact verification passed. Publishing was
  skipped. Complete log, job/run/artifact API metadata and source/ten-lock
  manifest: [final CI evidence](haveapi-logs/ci-41049401404/).
- Final artifact ID `12973953100`, name `release-41049401404`, GitHub archive
  digest `a0266d819b241486bb8b31609f9df0ff771dad07c308852feca424e5cd37e1de`.
  Payload is twelve files, including manifest. Full run-log SHA-256:
  `45409a88451ae73651ed1fa26e28968d9ab9a0d137e5f49b8ab3dd493c735512`.
- Independently verified every artifact payload against manifest hashes and
  compared all 46 frozen Go executable/library/template/metadata and shared
  Ruby-schema inputs against the retained Go/Ruby gems. All matched. The final
  release's Go lock equals generation lock byte-for-byte. Receipt:
  [retained-package-correspondence.json](go-logs/retained-package-correspondence.json).
- Eight final locks match preparation byte-for-byte. npm lock differs only in
  whitespace; parsed JSON identical. PHP lock differs only in `content-hash`
  after synchronized manifest version, with identical package/dev-package and
  other records. All final external graphs match preparation; actual final
  bytes and hashes retained in `ci-41049401404/retained-locks/` and
  [final-lock-comparison.json](haveapi-logs/final-lock-comparison.json).
- Final fetch/SSH remote proof confirms feature `0e7166a0`, master unchanged
  `7edb003d`, clean worktree. Native comparison captured exact base/head.
  Package is ready, awaiting integration and publication approval. No resource
  claim, deployment, release tag, registry write or PHP mirror mutation.

## Final read-only predecessor/publication approval preflight

Checked 2026-10-30, without changing source, environment, secrets or publishers.

- Previous latest release `v0.31.2` is **finished**, rather than merely tagged.
  Exact source `819bba5110e089465535ecd71ca2eb37a7d39caa`; tagged workflow
  [40661462796](https://github.com/vpsfreecz/haveapi/actions/runs/40661462796)
  completed successfully, including `Publish approved artifacts` at
  2026-10-28 09:20:18 UTC. Its final log confirms all five gem destinations,
  npm, both Python files, PHP tag and `Release complete`.
- [GitHub Release v0.31.2](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.2)
  is public (`draft=false`, `prerelease=false`), published 2026-10-28 09:20:14 UTC.
  Downloaded retained manifest SHA-256
  `4ba5e7dba199b1d92d28f23f9d080b4331adacf39fb9d398838a99733ce1b8b9`
  binds that source/version/run. Current exact-version RubyGems SHA-256s for all
  five gems, downloaded npm tarball SHA-256 and both PyPI file SHA-256s match
  this manifest. Public GitHub Release asset digests also match.
- PHP annotated tag `v0.31.2` peels to
  `52cf471406593edd42db32a6b61156522318dac9` and records HaveAPI source
  `819bba5110e089465535ecd71ca2eb37a7d39caa`. Packagist `haveapi/client` 0.31.2
  currently indexes the same source/dist commit. The metadata uses version
  `0.31.2` without `v`; inspection normalized that spelling after an initial
  lookup assumed the tag prefix. No missing indexing or publication inferred.
- No noncompleted release workflow among the latest fifty runs; separate queued,
  in-progress and environment-waiting queries are empty. No unresolved running
  predecessor publication found. Read-only receipts, current registry hashes,
  original manifest and full tagged run log remain under
  `haveapi-logs/predecessor-0.31.2/`.
- Authenticated GitHub actor: `aither64`. Current protected `release`
  environment requires reviewer `aither64`, with `prevent_self_review=false`;
  custom deployment rule allows tags `v*`. This account can satisfy the
  environment reviewer rule after publication is explicitly authorized, without
  requiring a different maintainer. This is capability evidence, not approval
  to publish or change environment settings. The guard and explicit user/lead
  publication authorization still apply. Environment:
  [release deployments](https://github.com/vpsfreecz/haveapi/deployments/activity_log?environments_filter=release).

No predecessor blocker found. The 0.32.0 candidate, commits, retained artifacts
and existing test evidence remain unchanged; no new release or recovery started.

## Approved integration target preparation and ownership handoff

The lead recorded the user's explicit integration/publication direction and
assigned target preparation only. No merge, repository claim, default push,
release branch/tag or publication was performed by this preparation.

Fresh fetch and SSH remote proof retain master
`7edb003dd5d5a058b3308510bb8a5f60387ad654` and feature
`0e7166a0f8f15827bfac051666a53bf449e999ec`; complete reviewed two-commit
series unchanged. Created fresh detached target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/haveapi-merge-target`
at that master base. Feature and target are clean; fast-forward ancestry passes.

Prepared top-level Nix profile link:
`work/2026-10-30-haveapi-client-releases/haveapi-logs/merge-nix-profile`,
resolving to `/nix/store/aa4f7j8zvzjs7hygin4nr0v1nd8b0xsx-haveapi-env`.
It selects the existing committed flake toolchain; no dependency refresh or
test batch. Reuses the feature checkout's installed `.gems` (Ruby 3.4.11,
Bundler 4.0.23). Copied exact root `Gemfile.lock` to the target as an ignored
preparation input; `bundle check` passed. Inspected configuration and signed
Overcommit configuration/post-checkout/post-merge/pre-push hooks outside claims.
Native `git hook run` for all three hook types passed without bypass. Hook log:
[merge-hook-preparation.log](haveapi-logs/merge-hook-preparation.log).

For the lead's short claimed critical section, start in the **feature** HaveAPI
worktree so the shell selects its already prepared gem home:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop \
  --profile /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/haveapi-logs/merge-nix-profile \
  --command bash -c '
    set -e
    export BUNDLE_GEMFILE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/haveapi-merge-target/Gemfile
    export BUNDLE_FROZEN=true
    cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-haveapi-client-releases/haveapi-merge-target
    # Lead performs fresh target/head/cleanliness proof, ordinary ff-only merge,
    # hook inspection, normal HEAD:master SSH push and remote proof here.
  '
```

This is an environment recipe, not execution or an integration framework. Lead
acquires one exact repository claim only around the final checks/merge/hooks/
push/proof, releasing before records/CI. If a baseline or hook needs repair,
inspect effects and return to unlocked preparation. The feature ref/worktree
remain unchanged. Git mutation ownership is handed back to the lead; implementer0
will make no further ref mutations without a repair assignment. Exact target
receipt: [integration-target-preparation.json](haveapi-logs/integration-target-preparation.json).

### Native session CLI inside the project environment

The lead's first coordination acquire attempt inside this prepared shell failed
before ledger/main loading: the native workspace wrapper selects Ruby 3.4.9,
but inherited project `GEM_HOME`/`GEM_PATH` selected a native JSON extension built
under project Ruby 3.4.11 and a newer glibc. The loader reported missing
`GLIBC_2.44`. Outside the project environment, authoritative status for request
`5c252269-732c-423a-a252-0c229be4444e` reported unknown claim; target and remote
master remained `7edb003d`. No claim/merge/default mutation occurred.

Verified this minimal function **inside the exact prepared Nix shell**, with
target `BUNDLE_GEMFILE`, `BUNDLE_FROZEN=true` and target CWD:

```sh
native_dev_session() (
  for task_env_name in ${!GEM_@} ${!BUNDLE_@} ${!BUNDLER_@} ${!RUBY@}; do
    unset "$task_env_name"
  done
  exec /home/aither/bin/dev-session "$@"
)
```

Use this function only for native session/coordination commands. The subshell
removes inherited Ruby/gem/Bundler overrides; the installed wrapper selects its
own native Ruby. Parent project environment and Git/hooks remain unchanged.
Read-only `native_dev_session current` returned the bound session;
`native_dev_session coordination claim-status ... --id 5c252269-732c-423a-a252-0c229be4444e --json`
reached the runtime and returned `unknown session claim` (exit 2). Project Ruby
3.4.11 and `bundle check` passed before and after, target Gemfile remained
selected, target stayed clean at `7edb003d`. Verification:
[native-cli-environment-boundary.log](haveapi-logs/native-cli-environment-boundary.log).
No acquire, retry, release, merge or push was performed during this repair.
The lead can retry the exact uncreated request through this boundary and keeps
exclusive ownership of integration Git/ref operations.

## Integrated and published result

Lead integrated the exact reviewed head `0e7166a0f8f15827bfac051666a53bf449e999ec`
into remote master and `haveapi-0.32`, with annotated `v0.32.0` tag object
`e78e4b398819a82961cabb7c7ceea59c773c6a64`. Its short repository claim was
released and verified by the lead. No preparation head or generator input changed.

Tag run [41056909572](https://github.com/vpsfreecz/haveapi/actions/runs/41056909572)
built its own immutable artifact `12977097967`, passed all tagged tests/package
and extracted-generator gates, and completed approved publication successfully.
Independent current checks verify all five gems, npm integrity, Python wheel and
sdist hashes, all public GitHub assets, the complete PHP mirror snapshot and
Packagist indexing against that original tagged artifact. See the compact final
[release verification](release-verification.md) for exact source/run/manifest,
PHP graph, registry receipts and logs. No incomplete HaveAPI destination remains.

Source identities from the maintained generator identity functions:

| Input | SHA-256 |
| --- | --- |
| Shared schema, `haveapi-client` 0.32.0 | `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c` |
| Rust generator source | `923716b5f3eaca6352d82c8cbd8c194c9a8e4a7a743cf0cb8ce7c491dd08ddce` |
| Copied Rust runtime | `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739` |
| TypeScript generator source | `947a98d704dca737f8bef2e1042f710e77396a0a793cb7233e8093887a713d6e` |

Final prepared lock identities:

| Path | SHA-256 |
| --- | --- |
| `Gemfile.lock` | `d877e06242f07be3dd1f1abef41136901bef26d10b58126d4d37e4068449e96f` |
| `servers/ruby/Gemfile.lock` | `c46e1bb7a613ab46f02faf5d46e8aee4053234ecde997a88d8db88e1ad443a67` |
| `clients/ruby/Gemfile.lock` | `fb620940573325aad21ab09791eae43b36e7778555ce91ee9f19cfdc1159fa16` |
| `clients/go/Gemfile.lock` | `bb4b5eab29bef661b4b3b5cd64a26852eee795105d0a1d872a37623ffb70450d` |
| `clients/rust/Gemfile.lock` | `86c1d8b1846dee4046e59518585a6ab0a52b6c66f1394729ab767c0411dd942c` |
| `clients/typescript/Gemfile.lock` | `d71a09b1d8d4ce19ce5678e9c32d0962cdbfd75aa08cf895a8c861351f7e84ab` |
| `clients/rust/runtime/Cargo.lock` | `48e682446003c37e3ec111308a35a49fb895affe8b0ea3f7ae109b6655f00746` |
| `clients/js/package-lock.json` | `7b1a57b3d3f864258c62c5bd3cd98e909cad05b90ee731b736e9fc17c975160d` |
| `clients/php/composer.lock` | `cdf0006d6675a12a07cfcae1c6c6e4ed6bc3c91abeb7106b6b034ccdabe5bc93` |
| `clients/python/uv.lock` | `d31d982eb83322235567aca453ad4886e997599dca1e1b2d7d2012dee92494ec` |

The exact machine-readable identities are also retained in
[candidate-identities.json](haveapi-logs/candidate-identities.json). Downstream
readers must use this exact candidate SHA and isolated development bundles, and
must rebind if the candidate changes. This record claims no release/publication.
