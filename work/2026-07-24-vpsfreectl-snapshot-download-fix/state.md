# 2026-07-24-vpsfreectl-snapshot-download-fix

## Repositories

- `repos/haveapi.git`
  - Branch `2026-07-24-vpsfreectl-snapshot-download-fix`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi`
  - Branch `2026-07-24-vpsfreectl-snapshot-download-fix-0.29`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-0-29`
- `repos/haveapi-client-php.git`
  - Branch `2026-07-24-vpsfreectl-snapshot-download-fix`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-client-php`
- `repos/vpsadmin.git`
  - Branch `2026-07-24-vpsfreectl-snapshot-download-fix`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/vpsadmin`
  - Release target branch `master`
  - Temporary integration worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/vpsadmin-release-master`
    (removed after release)
- `repos/vpsfree-client.git`
  - Branch `2026-07-24-vpsfreectl-snapshot-download-fix`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/vpsfree-client`
  - Release target branch `master`
  - Temporary integration worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/vpsfree-client-release-master`
    (removed after release)

## Status

The original coordinated release is complete: HaveAPI 0.29.5,
vpsadmin-client 4.2.0, and vpsfree-client 0.20.0 are published and verified.
A follow-up is in progress to fix resource-name collisions exposed by the new
dependency chain. HaveAPI 0.29.6 must be completed and released before any
vpsAdmin or vpsfree-client dependency update begins. No server deployment is
planned.

## Follow-up worktrees

- `repos/haveapi.git`
  - Branch `2026-07-24-haveapi-resource-name-collisions`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-collisions`
  - Branch `2026-07-24-haveapi-resource-name-collisions-0.29`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-collisions-0-29`
- `repos/haveapi-client-php.git`
  - Branch `2026-07-24-haveapi-resource-name-collisions`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-client-php-collisions`
- Downstream follow-up branches and worktrees will be created from the public
  release heads after HaveAPI 0.29.6 is published.

## Follow-up status

- Fetched current upstream heads.
- Confirmed HaveAPI master at
  `efd0314bee237aa3df5f0189eddc7267c05c0fd1` and `haveapi-0.29` at
  `2d9edf01cf39963e6fd48282ae6c137c04e692dc`.
- Confirmed the standalone PHP mirror remote master at
  `03201f582e37abc586a3ac308308808b0b663539`.
- Created fresh follow-up worktrees without rewriting the already released
  branches or tags.
- Implemented and committed the master-side HaveAPI changes as five focused
  commits:
  - `c8ad88ef6f24fdda33a4b3e47b8555a2c08e9081`
    `clients/ruby: traverse association resource registry`
  - `f62349c9b1174e284cad4063035b52fac28c9294`
    `clients/ruby: keep language configuration in options`
  - `89aaa8f32524012cc257474ffea016782f26d604`
    `clients/js: traverse association resource registry`
  - `c8c786f7f27fa4d621019641c0ee5dbe5916521c`
    `clients/go: allocate collision-safe API members`
  - `42b80198055c1bc24a266a566d6896e081840ab1`
    `clients/php: cover language resource associations`
- Added the identical PHP regression to the standalone mirror in
  `1089e33dbf54c0af70465460b20e09d1c1dace12`.
- Installed and signed the HaveAPI Overcommit hooks before committing. The
  i18n, RuboCop, and PHP CS Fixer pre-commit hooks passed.
- Quick follow-up verification:
  - Ruby association, description-name, option/i18n, and CLI i18n specs:
    11 examples, 0 failures.
  - JavaScript full client suite after regenerating `dist`: 43 passing.
  - Generated Go integration suite: 9 examples, 0 failures, including a
    compile test for `language`, Client method names, nested resources,
    actions, and aliases, plus absent-authentication member preservation.
  - PHP collision regression in both copies: 1 test, 6 assertions.
  - RuboCop on all changed Ruby generator/client/spec files: 11 files, no
    offenses.
- Full tree validation and the release-branch backport intentionally remain
  pending until the mandatory fresh-context review.

## Follow-up review packet

- Requested outcome: eliminate resource-name collisions in maintained HaveAPI
  clients, release coordinated HaveAPI 0.29.6, then update and release
  vpsadmin-client 4.2.1 and vpsfree-client 0.20.1 in dependency order.
- Initiative plan/state:
  `work/2026-07-24-vpsfreectl-snapshot-download-fix/plan.md` and this file.
- HaveAPI master worktree:
  `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-collisions`.
- HaveAPI master base/head:
  `efd0314bee237aa3df5f0189eddc7267c05c0fd1`..
  `42b80198055c1bc24a266a566d6896e081840ab1`.
- HaveAPI 0.29 backport worktree:
  `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-collisions-0-29`;
  it remains at base `2d9edf01cf39963e6fd48282ae6c137c04e692dc`.
- PHP mirror worktree:
  `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/haveapi-client-php-collisions`.
- PHP mirror base/head:
  `03201f582e37abc586a3ac308308808b0b663539`..
  `1089e33dbf54c0af70465460b20e09d1c1dace12`.
- Compatibility assumptions:
  - Ruby removes the 0.29.0-only `language`, `language=`,
    `language_header`, and `language_header=` Client methods. Constructor
    options and the pre-existing `set_opts`/`opts` interface replace them.
  - Generated Go clients replace the 0.29.5-only exported `Language` and
    `LanguageHeader` fields with setters/getters. Normal generated member
    names remain unchanged; colliding names receive deterministic suffixes.
  - JavaScript changes only association traversal. PHP runtime is unchanged.
  - There is no API wire, server, database, persisted-state, or deployment
    change, and no mixed-version ordering requirement beyond publishing
    HaveAPI before downstream dependency updates.
  - The standalone `vpsadmin-go-client` remains unchanged. A temporary client
    generated from vpsAdmin will be compiled during downstream verification.

## Follow-up mandatory change review

- One fresh standalone reviewer completed the mandatory review on the
  committed master and PHP mirror ranges.
- Important finding: the Go allocator initially reserved the union of all
  authentication-specific Client methods even when the corresponding backend
  was absent. That unnecessarily renamed otherwise valid resource members and
  contradicted the compatibility goal.
- Resolved by deriving authentication-specific reservations from the
  authentication methods present in the API description. The regression suite
  now verifies that `revoke_access_token` is suffixed when OAuth2 emits the
  conflicting method and retains its normal name when OAuth2 is absent.
- The correction was folded into the focused Go commit before publication.
  RuboCop passes and the complete generated Go suite now has 9 examples with
  no failures.
- The same reviewer inspected the rewritten head and confirmed that the
  Important finding is closed with no remaining follow-up finding.
- The reviewer found no other Blocking, Important, or Advisory issues. It
  confirmed the commit split, Ruby/JavaScript structural traversal, Go
  collision handling, generated JavaScript scope, PHP mirror equality,
  backport applicability, and the documented intentional compatibility
  changes.
- Backported the five master commits to `haveapi-0.29` with `cherry-pick -x`:
  - `1da1f49c13f611e7e81a425c1b13cbd4c00fb2cb`
  - `2f226aa2c811daf104aee9dc84c83b5e6e1d5e88`
  - `082c31dd4da229157314582d667b6d12ed0df83f`
  - `f58ad100a3c99b6906488e3ae1be5662b810bbb0`
  - `190a6a3a0871ffd224bf9227c75d0f545209c4fe`
- Stable patch IDs match between every master commit and its release-branch
  backport.
- Added the separate coordinated version/changelog commit
  `e4c19cfe751928be4b89a2297691591d69c0b5f3` for HaveAPI 0.29.6.
- Synchronized the PHP subtree into the standalone mirror. Its separate
  version commit is `27da6934f0497501187f77d14b566469dd4a7e14`.
- Full HaveAPI 0.29.6 suite on the release branch:
  - Ruby server: 347 examples, 0 failures.
  - Ruby client: 47 examples, 0 failures.
  - Generated Go client: 9 examples, 0 failures.
  - JavaScript client: 43 passing.
  - PHP client: 51 tests, 144 assertions.
- The full HaveAPI Overcommit run passes i18n freshness, PHP CS Fixer, and
  RuboCop.
- `nix develop --command make release` built the unpublished 0.29.6
  artifacts:
  - `haveapi-client-0.29.6.gem` SHA-256
    `b47338161b312fa91407e43f96db50c9617c1b17039a1a3f2eba01b897d68fc2`
  - `haveapi-0.29.6.gem` SHA-256
    `1e3257a0601566ac1fa713833d70882c6a8fa7f8e86f2b723c1130d5e092b9bd`
  - `haveapi-go-client-0.29.6.gem` SHA-256
    `83076666a49201a4f8a8409d14aa01afb407c367634ad149b7e1cf2079102923`
  - `haveapi-client.js` SHA-256
    `c65e005670928b12987245f5f2a52181ebbb7092d41be6aad91f92de39202630`
- Gem metadata reports 0.29.6 throughout; the server and Go generator require
  `haveapi-client ~> 0.29.6`.
- `npm pack --dry-run` reports `haveapi-client` 0.29.6 with the expected
  license, README, bundled client, and package metadata files.
- Composer validates both PHP copies with only the existing explicit-version
  warning, and the standalone mirror is checksum-identical to the monorepo
  PHP subtree after excluding local dependency/cache files.
- Pushed the three follow-up feature branches over SSH. GitHub Actions started
  on exact heads `42b80198055c1bc24a266a566d6896e081840ab1` and
  `e4c19cfe751928be4b89a2297691591d69c0b5f3`; per user instruction, their
  completion is not awaited.
- RubyGems and npm still end at 0.29.5, and neither source repository has a
  `v0.29.6` tag. No target branch, tag, or package has been published.

## Commands run

- `bin/dev-session current`
- Inspected workspace status and verified
  `VPSFREE_DEV_SESSION_SLUG=2026-07-24-vpsfreectl-snapshot-download-fix`.
- Fetched `origin` for `haveapi`, `vpsadmin`, and `vpsfree-client`.
- Compared `haveapi-client` 0.26.5 and 0.29.4, `vpsadmin-client` 4.1.0 and
  current `vpsadmin` master, and `vpsfree-client` 0.19.0 and master.
- Retrieved the public production API v7.0 description in English and Czech
  with read-only `OPTIONS` requests.
- Reproduced local parameter validation using exact released
  `haveapi-client` 0.26.5 and 0.29.4 gems in isolated temporary gem homes.
- Queried RubyGems for published versions of the three client gems.
- Created isolated initiative worktrees for HaveAPI master/release, the PHP
  mirror, vpsAdmin, and vpsfree-client.
- Repaired the canonical `vpsfree-client` bare clone's `HEAD` to point at a
  local `master` branch, following
  `notes/cross-project/2026-05-28-bare-head-worktree.md`.
- Focused HaveAPI checks:
  - Ruby client inclusion/i18n specs: 7 examples, 0 failures.
  - Ruby server inclusion specs: 6 examples, 0 failures.
  - JavaScript localized-choice integration: 1 passing.
  - PHP localized-choice integration: 1 test, 2 assertions.
  - Generated Go integration group: 7 examples, 0 failures.
- The JS component shell and the initial Go component invocation could not
  start the shared Ruby test server. The JS suite passed in the documented
  full shell. The Go suite passed after installing the server bundle with
  `RUBYOPT` unset; see
  `notes/haveapi/2026-07-24-client-go-shared-server-bundle.md`.
- HaveAPI commits:
  - Master fix `efd0314bee237aa3df5f0189eddc7267c05c0fd1`.
  - Release-branch backport
    `4f0b1166a21e478ed139be68faa969f70599935a`.
  - Coordinated version commit
    `2d9edf01cf39963e6fd48282ae6c137c04e692dc`.
- PHP mirror commit:
  `03201f582e37abc586a3ac308308808b0b663539`.
- Final cleaned vpsAdmin commits:
  - HaveAPI dependency and generated metadata:
    `707ed74f89677174184c59b029dbd5093999cd9b`.
  - Release-task package-pin synchronization:
    `3c0fff6e47f3b46aec9bf481a7c5d918bcd82d92`.
  - WebUI fallback-version assertion:
    `a0187018d87ea1171472ed8dccb18fad356754d5`.
  - Coordinated version update:
    `f01121b3ce8e809858d5443bb1306d72765b8b9b`.
- vpsfree-client commits:
  - Dependency commit `35b53b42846d3fac75a12a2046a59cbca7042707`.
  - Version/changelog commit
    `936536f59e34ba3be5a7de19d7c0ffc39b3839cc`.
- Installed and signed the vpsAdmin Overcommit hooks from the root Nix shell.
  The API i18n hook uses `api/.gems`, so its bundle had to be installed with
  the hook's exact `BUNDLE_GEMFILE` and `BUNDLE_PATH` environment. All
  pre-commit and commit-message hooks then passed for both vpsAdmin commits.
- Downstream quick checks with temporary Bundler path overrides:
  - vpsadmin-client: 23 examples, 0 failures, resolved local
    `haveapi-client` 0.29.5, and built
    `/tmp/vpsadmin-client-4.2.0.gem`.
  - vpsfree-client: resolved local `vpsadmin-client` 4.2.0 and
    `haveapi-client` 0.29.5, loaded version 0.20.0, and built
    `/tmp/vpsfree-client-0.20.0.gem`.
  - The vpsAdmin client development shell first attempts its checked-in
    Gemfile and prints the expected pre-publication resolution failure for
    0.29.5; the explicit temporary Gemfiles then resolve the local worktrees
    and the commands exit successfully.

## Results

- The current session slug is verified. A separate
  `2026-07-24-vpsfreectl-snapshot-download` initiative exists and must not be
  touched.
- The request never reaches `SnapshotDownload::Create` on the server. The
  stack enters the `haveapi-client` local validation branch in
  `Action#execute`.
- For an authenticated Czech user, vpsAdmin selects `cs` from
  `current_user.language` when the old client sends no explicit language
  header.
- The English API description exposes snapshot download formats as an array:
  `["archive", "stream", "incremental_stream"]`.
- The Czech API description exposes the same values as a localized map:
  `{"archive":"archiv", ...}`. `JSON.parse(..., symbolize_names: true)` turns
  those keys into `:archive`, `:stream`, and `:incremental_stream`.
- The Ruby client's inclusion validator compares the symbol map keys directly
  with the string input `"archive"`. It therefore rejects the valid default
  format with `{format: ["archive nelze použít"]}`.
- This is a latent Ruby-client hash-choice bug exposed by HaveAPI 0.29.2
  localized choice metadata, not a rejection caused by stricter server-side
  input coercion.
- `haveapi-client` 0.26.5 then masks that validation error:
  `ValidationError` passes a string to `ActionFailed`, whose constructor calls
  `response.action`. This produces the reported `NoMethodError`.
- The exception-rendering defect was fixed in HaveAPI 0.27.0, but the
  inclusion defect remains in released 0.29.4 and current master.
- Reproduction matrix for `snapshot_download#create` with the normal default
  `format: "archive"`:
  - 0.26.5 with English metadata: valid.
  - 0.26.5 with Czech metadata: invalid, followed by the reported
    `NoMethodError`.
  - 0.29.4 with English metadata: valid.
  - 0.29.4 with Czech metadata: invalid with a readable
    `HaveAPI::Client::ValidationError`.
- At investigation time, RubyGems published `haveapi-client` 0.29.4,
  `vpsadmin-client` 4.1.0, and `vpsfree-client` 0.19.0. The reporter has the
  latest two outer gems. Released `vpsadmin-client` 4.1.0 constrains
  `haveapi-client` to `~> 0.26.0`, explaining 0.26.5.
- The then-unreleased `vpsadmin` master changed that dependency to
  `~> 0.29.4`, but upgrading to it would only expose the real Czech validation
  error; it would not make the download work.
- A complete client fix belongs in HaveAPI's Ruby inclusion validator and
  needs a localized-choice regression test. Existing 0.26-constrained clients
  need either a compatible 0.26 patch release or a newly released
  `vpsadmin-client` 4.x depending on a fixed 0.29 patch. `vpsfree-client`
  0.19.0 already accepts later 4.x `vpsadmin-client` releases through
  `~> 4.0`.
- A server-side compatibility mitigation is also warranted for already
  installed clients: do not change `validators.include.values` from an array
  to a map based on locale, or temporarily withhold localized choice labels.
  For this specific command, using English account/API metadata avoids the
  map and validates successfully.

## Open questions

- None.

## Cleanup

- Worktrees will use
  `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/`.
- Removed both isolated temporary gem homes and downloaded API descriptions.
- Removed the clean temporary vpsAdmin and vpsfree-client release-integration
  worktrees after verifying their remote branch and tag targets. Feature
  branches and feature worktrees remain.

## Implementation decisions

- Fix the Ruby inclusion validator, not the server metadata shape. Hash choice
  keys are normalized by their JSON string representation; array membership
  remains exact.
- Release HaveAPI 0.29.5 from `haveapi-0.29` after first committing the
  canonical change against `master`.
- Release current vpsAdmin master as 4.2.0, then release vpsfree-client 0.20.0
  after the public vpsadmin-client dependency is available.
- JavaScript already validates map choices correctly. PHP and generated Go
  clients defer inclusion checks to the server. Legacy Elixir has no
  corresponding local validator/i18n path. `vpsadmin-go-client` is unaffected,
  and the Terraform provider has no snapshot-download surface.

## Review packet

- Requested outcome: fix localized choice validation in HaveAPI 0.29.5 and
  prepare vpsadmin-client 4.2.0 plus vpsfree-client 0.20.0.
- HaveAPI master base/head:
  `e3749669d6034d529095ccbd3a40148fcb243a27`..
  `efd0314bee237aa3df5f0189eddc7267c05c0fd1`.
- HaveAPI 0.29 base/head:
  `6a8ca97fc8c0f3db4ef33fd9d9f62703d807572f`..
  `2d9edf01cf39963e6fd48282ae6c137c04e692dc`.
- PHP mirror base/head:
  `44bb8d1e4f786f3a84794c5ffe845d9afd2d50e5`..
  `03201f582e37abc586a3ac308308808b0b663539`.
- vpsAdmin base/head:
  `d0bb3c8ee8610ee941853912dc86768e66d3c726`..
  `f01121b3ce8e809858d5443bb1306d72765b8b9b`.
- vpsfree-client base/head:
  `121f4e4a5709f8ea8f46c1ba732a522378b09039`..
  `936536f59e34ba3be5a7de19d7c0ffc39b3839cc`.
- Dependency pins: HaveAPI clients/server 0.29.5,
  `vpsadmin-client` requires `haveapi-client ~> 0.29.5`, and
  `vpsfree-client` requires `vpsadmin-client ~> 4.2`.
- Compatibility assumptions are recorded in `plan.md`; no API wire, server,
  database, or persisted-state change is included.

## Mandatory change review

- One fresh standalone reviewer completed the required review after the
  initial intended commits and quick checks.
- Important finding: `packages/client/Gemfile.lock` and `gemset.nix` still
  represented vpsadmin-client 4.1.0 and HaveAPI 0.29.4. Addressed in
  `4aef5bbfb5e0d40057264c98f4ceb18f8788a84e`.
  - A standalone Ruby build was byte-stable but differed from the official
    top-level Nix release-shell artifact. The final correction is
    `fb28d1a708a7268786a818ca54bc4c3da371fa4f`; see
    `notes/haveapi/2026-07-24-release-shell-artifact-hash.md`.
  - The committed Nix base32 hash
    `1diyzs51dl74sc44pn9phn4ci663m53l5ql17xg2k99pgmynr0sd`
    matches the exact artifact built by `nix develop . --command make release`.
  - The normal `rake vpsadmin:gems` refresh was rerun after HaveAPI 0.29.5
    became visible on RubyGems and produced no unexpected difference.
- Advisory finding: the no-revision Playwright assertion hard-coded
  `Version: 4.1.0`. Addressed in
  `121ba5c01ae7981e17c068b85f4aa97d8328f59e` by reading the shared `VERSION`
  marker. `node --check` passes.
- The initial reviewer found no other issues. It confirmed identical
  master/backport
  patch IDs, exact array semantics, normalized map-key semantics, PHP mirror
  equality, consistent HaveAPI 0.29.5 markers, correct downstream dependency
  ranges, and appropriate commit splitting.
- The same standalone reviewer performed the required follow-up review after
  the history cleanup. It found that the authoritative `libnodectld`,
  `nodectl`, and `nodectld` package Gemfiles still pinned local gems to 4.1.0
  while their generated metadata used 4.2.0.
- Resolved the blocking follow-up finding by updating those three pins and
  lockfiles and teaching `vpsadmin:version` to maintain the pins. Repeated
  version/dependency generation is clean, and all three Nix packages build as
  4.2.0.
- Residual gap: a real Czech snapshot-download end-to-end run.

## Full validation and release artifacts

- The initial `nix develop . --command make test` lacked component bundles.
  Installed the declared Ruby, npm, and Composer component dependencies in the
  same shell, then reran the unchanged full suite.
- Full HaveAPI 0.29.5 suite:
  - Ruby server: 347 examples, 0 failures.
  - Ruby client: 43 examples, 0 failures.
  - Generated Go client: 7 examples, 0 failures.
  - JavaScript client: 40 passing.
  - PHP client: 50 tests, 138 assertions.
- HaveAPI Overcommit: i18n, PHP CS Fixer, and RuboCop all pass.
- `nix develop . --command make release` completed successfully.
- `npm pack --dry-run` reports `haveapi-client` 0.29.5 with the expected four
  files. Composer validation accepts both PHP copies with the existing warning
  that a published package contains an explicit `version` field.
- The standalone PHP mirror is checksum-identical to `clients/php`, excluding
  local dependency/cache files.
- vpsadmin-client full RSpec: 23 examples, 0 failures. Repeated root
  Overcommit runs pass.
- An isolated temporary gem home installed the official HaveAPI artifact,
  vpsadmin-client 4.2.0, and vpsfree-client 0.20.0 with dependencies, loaded
  the exact three versions, and reported
  `4.2.0 based on haveapi-client 0.29.5`.
- Release artifact SHA-256 values:
  - `haveapi-0.29.5.gem`:
    `51f90402050a38f07cc3d13378c5639ee5ee77e98918b053af28ac6333778892`.
  - `haveapi-client-0.29.5.gem`:
    `4d836c7d7d37a5295e3f81e24247a9c398c8888537d94b08d3e4d0168afe3eb6`.
  - `haveapi-go-client-0.29.5.gem`:
    `95973461028a2f73701cbd95b45f2173a901d3bd6f2ad98c585f66d267df1208`.
  - `haveapi-client.js`:
    `548afcc40266d62d4ddb86a434c25bbb2352b9f5a83ce03dbd80ca87f6307dd9`.
  - `haveapi-client-0.29.5.tgz`:
    `d2dcf56b7966d0c6d2f9aeea9dbbef0ad170cc8b96103f4bae2eb22c78c6bd49`.
  - `vpsadmin-client-4.2.0.gem`:
    `d33ca8bcb7b10071762f1236ed854ce1851719b466d9a018671538e354e5816e`.
  - `vpsfree-client-0.20.0.gem`:
    `325751cfc215358d7cc05fcd494356ee4840dc4dd111867217bebd2c036126aa`.
- RubyGems, npm, Packagist, and both HaveAPI repositories contain the verified
  0.29.5 release. Downstream target tags/packages remain absent.
- All five feature branches were pushed over SSH. HaveAPI and vpsAdmin CI
  started on the exact tested heads; the standalone PHP and vpsfree-client
  repositories have no push workflows.

## Source integration and CI

- Fast-forwarded HaveAPI `master` to
  `efd0314bee237aa3df5f0189eddc7267c05c0fd1` and `haveapi-0.29` to
  `2d9edf01cf39963e6fd48282ae6c137c04e692dc` from fresh target worktrees.
- Fast-forwarded `haveapi-client-php` `master` to
  `03201f582e37abc586a3ac308308808b0b663539` from a fresh target worktree.
- Removed the temporary integration worktrees. At this pre-release checkpoint,
  no tag had been created and no package had been published; the later
  HaveAPI-only release is recorded below.
- All HaveAPI workflows passed on the feature heads and again on the exact
  integrated `master` and `haveapi-0.29` heads.
- Completed vpsAdmin workflows and API/CI jobs are green except for Client
  Specs run `30111588172`. Its log was inspected: Bundler cannot resolve the
  deliberately unpublished `haveapi-client ~> 0.29.5`, after which the shell
  also lacks the bundle-provided `rake`. This is the expected release-order
  bootstrap failure, not a test regression. The job must be rerun after
  HaveAPI 0.29.5 is published.
- At the release-approval handoff, API Specs run `30111588148` and integration
  run `30111588247` are still in progress on the exact vpsAdmin feature head.
  Every completed job in those runs is green. Their result must be checked
  before integrating or publishing vpsadmin-client.

## HaveAPI 0.29.5 release

- The user explicitly approved only the coordinated HaveAPI release.
- Fast-forwarded `haveapi-client-php` `master` to
  `03201f582e37abc586a3ac308308808b0b663539`; its stale local
  `origin/master` tracking ref did not update from a fetch without an explicit
  refspec, but `ls-remote` confirmed the remote branch.
- Created and pushed annotated `v0.29.5` tags:
  - HaveAPI tag target
    `2d9edf01cf39963e6fd48282ae6c137c04e692dc`.
  - PHP mirror tag target
    `03201f582e37abc586a3ac308308808b0b663539`.
- The initial HaveAPI tag push was stopped by Overcommit's changed-signature
  check. Verified the clean configuration, ran `overcommit --sign` in the
  top-level Nix shell, and pushed normally without bypassing hooks.
- Ran `nix develop . --command make publish`; it published only:
  - `haveapi-client` 0.29.5 to RubyGems.
  - `haveapi` 0.29.5 to RubyGems.
  - `haveapi-go-client` 0.29.5 to RubyGems.
  - `haveapi-client` 0.29.5 to npm.
- RubyGems reports SHA-256 values identical to all three reviewed local
  artifacts. npm reports SHA-1
  `37c931ff06f05123cdf3d389d6cbdfff767abb98`, identical to the prepared
  tarball. Packagist resolves 0.29.5 to the reviewed PHP commit.
- A clean registry install in the HaveAPI Nix shell loaded server, Ruby client,
  and Go generator versions as `0.29.5`. An ambient install attempt failed
  first because the minimal shell lacked a compiler for native dependencies;
  no package defect was involved.

## Final vpsAdmin update and release

- The repository's `vpsadmin-update-haveapi` skill is stale: its script still
  requires removed `tools/bundix_all.sh`. Used its declared five source
  targets, then the current `AGENTS.md` command
  `nix develop . --command rake vpsadmin:gems`.
- Updated all active consumers:
  - Ruby API, CLI, download mounter, mail templates, and outage-report utility.
  - API, client, and download-mounter package lockfiles/gemsets.
  - WebUI Composer lock/Nix metadata.
  - WebUI and console-router bundled JavaScript clients.
- Regeneration selected the published HaveAPI 0.29.5 hashes:
  - `haveapi`: `14l8fwrn7b18mx9v0649x5vyxrcycg2phcyiqdyg0f0a0l109yai`.
  - `haveapi-client`:
    `1diyzs51dl74sc44pn9phn4ci663m53l5ql17xg2k99pgmynr0sd`.
- Initially rewrote the five unmerged vpsAdmin development commits into two
  commits. After review of the commit boundaries, split the independent
  release-task and WebUI test changes from the version update. The final
  history is:
  - `707ed74f8`: `deps: update HaveAPI to 0.29.5`.
  - `3c0fff6e4`: `release: update packaged gem pins with shared version`.
  - `a0187018d`: `webui: derive fallback version assertion from VERSION`.
  - `f01121b3c`: `Version 4.2.0`.
- The final tree `f99f434844fbd62cf7c0f6e2764885b2dd71e82c` is
  byte-identical to the superseded `64d2493d1` tree. All three replacement
  commits passed the repository pre-commit and commit-message hooks.
- The first history rewrite attempt was paused by hooks because Git was run
  outside Nix. Refreshed the API hook's isolated bundle to published 0.29.5
  and completed all commits/rewording inside the root Nix shell. All
  pre-commit and commit-message hooks pass without bypasses.
- Quick verification:
  - `rake vpsadmin:gems` is idempotent with a clean worktree.
  - vpsadmin-client: 23 examples, 0 failures; gem build passes and loads
    `4.2.0` with `haveapi-client` 0.29.5.
  - WebUI: 82 tests, 332 assertions; Composer installs 0.29.5 and validates
    for application use. Strict validation still reports the pre-existing
    missing publish-only name/description/license metadata.
- Both bundled JavaScript files are byte-identical to the reviewed HaveAPI
  0.29.5 artifact and pass `node --check`.
- The mandatory follow-up review found three package Gemfiles still pinned to
  local gem version 4.1.0. Updated the canonical pins and generated lockfiles,
  extended `vpsadmin:version` to maintain them, and amended the second commit.
  Repeated `vpsadmin:version` plus `vpsadmin:gems` leaves the worktree clean.
- Nix builds of `libnodectld`, `nodectl`, and `nodectld` all pass and produce
  version 4.2.0.
- `nix develop .#console-router` currently fails before entering the shell
  because its flake still references removed `nodePackages`. JavaScript syntax
  was therefore checked with `nix shell nixpkgs#nodejs`; this unrelated shell
  maintenance issue is recorded separately.
- The previous feature head's API Specs run `30111588148` passed. Its selected
  integration run `30111588247` and Client Specs run `30111588172` failed
  before HaveAPI publication. Downloaded and inspected the integration
  artifact: all 116 unexpected failures share the same root build error,
  `cannot download haveapi-client-0.29.5.gem`, after RubyGems mirrors returned
  HTTP 403 for the not-yet-published artifact. The cleaned post-publication
  head must start fresh runs; these are dependency-order bootstrap failures,
  not test-behavior failures.
- Force-pushed the first cleaned history over SSH with an exact
  `--force-with-lease`. After the focused split, force-pushed again with an
  exact lease from `64d2493d1` to `f01121b3c`.
- Prepared the pull-request title/body and attempted submission with `gh`.
  GitHub returned `Resource not accessible by personal access token
  (createPullRequest)`: the configured fine-grained token can inspect
  branches, workflows, and PRs but cannot create a PR.
- Preserved the exact review title/body in `vpsadmin-pr.md`. The GitHub compare
  page is
  `https://github.com/vpsfreecz/vpsadmin/compare/master...2026-07-24-vpsfreectl-snapshot-download-fix?expand=1`.
- Fresh post-push workflow status when the user asked not to wait:
  - RuboCop, Download Mounter Specs, Console Router Specs, WebUI PHPUnit,
    Client Specs, libnodectld Specs, and i18n health passed.
  - CI and API Specs were still running with no reported failure.
- Stopped the local CI watcher immediately on request. The GitHub workflows
  themselves were initially left running. After the subsequent history
  rewrite, canceled the superseded CI run `30120345597` and API Specs run
  `30120345766`, which still targeted `64d2493d1`. Replacement workflows on
  `f01121b3c` are not being awaited.

## Downstream integration and release

- The user subsequently gave explicit approval to merge and release vpsAdmin,
  then release vpsfree-client. This superseded the earlier downstream-release
  deferral but did not authorize or require a server deployment.
- Before integration, the cleaned vpsAdmin feature head had seven successful
  replacement workflows; CI and API Specs were still running. They were not
  awaited, following the user's instruction.
- The canonical vpsAdmin bare repository's local `master` was at unrelated
  unpushed commit `b3ec1a757`, while the fetched `origin/master` was
  `d0bb3c8ee`. Preserved the local branch and used a detached temporary
  worktree from `origin/master`; see
  `notes/vpsadmin/2026-07-24-local-master-ahead-release-worktree.md`.
- Fast-forwarded the detached vpsAdmin release worktree from
  `d0bb3c8ee8610ee941853912dc86768e66d3c726` to
  `f01121b3ce8e809858d5443bb1306d72765b8b9b`.
- Final vpsadmin-client validation:
  - Client RSpec: 23 examples, 0 failures.
  - Fresh build SHA-256:
    `d33ca8bcb7b10071762f1236ed854ce1851719b466d9a018671538e354e5816e`,
    identical to the reviewed artifact.
  - Isolated Nix-shell install loaded vpsadmin-client 4.2.0 with
    haveapi-client 0.29.5.
  - The ambient isolated install lacked a compiler for native dependencies;
    the root Nix toolchain completed the same install successfully.
- Atomically pushed vpsAdmin `master` and lightweight tag `v4.2.0`; both
  resolve to `f01121b3ce8e809858d5443bb1306d72765b8b9b`.
- Published vpsadmin-client 4.2.0 to RubyGems. The RubyGems API and direct
  public download report the exact reviewed SHA-256 and dependency
  `haveapi-client ~> 0.29.5`.
- vpsfree-client's public-registry dependency resolution selected
  vpsadmin-client 4.2.0 and haveapi-client 0.29.5.
- The legacy vpsfree-client `shell.nix` cannot compile the current Prism gem
  because `prism.h` is unavailable. Its shell hook also continues to the
  requested command after Bundler fails. The isolated install passed in the
  maintained vpsAdmin root Nix toolchain; see
  `notes/vpsfree-client/2026-07-24-prism-header-shell.md`.
- Fast-forwarded the detached vpsfree-client release worktree from
  `121f4e4a5709f8ea8f46c1ba732a522378b09039` to
  `936536f59e34ba3be5a7de19d7c0ffc39b3839cc`.
- An ambient vpsfree-client rebuild initially differed from the reviewed gem
  only because RubyGems used 1980-01-02 instead of the Nix release epoch.
  Rebuilding with `SOURCE_DATE_EPOCH=315532800` reproduced the reviewed
  artifact byte-for-byte; see
  `notes/vpsfree-client/2026-07-24-source-date-epoch-gem-checksum.md`.
- Atomically pushed vpsfree-client `master` and lightweight tag `v0.20.0`;
  both resolve to `936536f59e34ba3be5a7de19d7c0ffc39b3839cc`.
- Published the exact vpsfree-client 0.20.0 artifact to RubyGems. The API and
  direct public download report SHA-256
  `325751cfc215358d7cc05fcd494356ee4840dc4dd111867217bebd2c036126aa`
  and dependency `vpsadmin-client ~> 4.2`.
- A clean installation by public gem name loaded:
  - vpsfree-client 0.20.0;
  - vpsadmin-client 4.2.0;
  - haveapi-client 0.29.5.
- Removed both clean temporary release-integration worktrees after verifying
  the final remote branch and tag targets. No feature branches were deleted.
