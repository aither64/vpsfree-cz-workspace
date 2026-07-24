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
- `repos/vpsfree-client.git`
  - Branch `2026-07-24-vpsfreectl-snapshot-download-fix`
  - Worktree
    `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/vpsfree-client`

## Status

All intended source, version, and review follow-up commits are prepared in
isolated worktrees. Focused and full local checks pass. The mandatory
standalone review is complete and both findings are addressed. HaveAPI master,
the 0.29 release branch, and the standalone PHP mirror are integrated
upstream. Downstream release branches are pushed but remain unmerged until
their registry-backed dependency checks can pass. Package publication and
release tags remain behind the required final approval gate.

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
- vpsAdmin client commits:
  - Dependency/changelog commit
    `c38cccdec3ad9360ad0c3fe4fb9109aabdd4efd2`.
  - Shared version commit
    `4042c9fd34651141eb8f13d19c44fa0e0cc17f88`.
  - Packaged-client metadata follow-up
    `4aef5bbfb5e0d40057264c98f4ceb18f8788a84e`.
  - WebUI fallback-version test follow-up
    `121ba5c01ae7981e17c068b85f4aa97d8328f59e`.
  - Official release-artifact hash correction
    `fb28d1a708a7268786a818ca54bc4c3da371fa4f`.
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
- RubyGems currently publishes `haveapi-client` 0.29.4,
  `vpsadmin-client` 4.1.0, and `vpsfree-client` 0.19.0. The reporter has the
  latest two outer gems. Released `vpsadmin-client` 4.1.0 constrains
  `haveapi-client` to `~> 0.26.0`, explaining 0.26.5.
- Current unreleased `vpsadmin` master changes that dependency to
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

- None for implementation. The user selected current-master downstream minor
  releases and the coordinated HaveAPI 0.29.5 release model.

## Cleanup

- Worktrees will use
  `worktrees/2026-07-24-vpsfreectl-snapshot-download-fix/`.
- Removed both isolated temporary gem homes and downloaded API descriptions.

## Implementation decisions

- Fix the Ruby inclusion validator, not the server metadata shape. Hash choice
  keys are normalized by their JSON string representation; array membership
  remains exact.
- Release HaveAPI 0.29.5 from `haveapi-0.29` after first committing the
  canonical change against `master`.
- Release current vpsAdmin master as `vpsadmin-client` 4.2.0 and
  `vpsfree-client` 0.20.0 with a `~> 4.2` dependency.
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
  `fb28d1a708a7268786a818ca54bc4c3da371fa4f`.
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
  - The normal `rake vpsadmin:gems:client` refresh still has to be rerun
    after HaveAPI 0.29.5 is visible on RubyGems and must produce no unexpected
    difference before publishing vpsadmin-client.
- Advisory finding: the no-revision Playwright assertion hard-coded
  `Version: 4.1.0`. Addressed in
  `121ba5c01ae7981e17c068b85f4aa97d8328f59e` by reading the shared `VERSION`
  marker. `node --check` passes.
- The reviewer found no other issues. It confirmed identical master/backport
  patch IDs, exact array semantics, normalized map-key semantics, PHP mirror
  equality, consistent HaveAPI 0.29.5 markers, correct downstream dependency
  ranges, and appropriate commit splitting.
- Residual gaps: registry-backed resolution and packaged-client regeneration
  after publication, plus a real Czech snapshot-download end-to-end run.

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
- RubyGems, npm, Packagist, and the remote repositories do not yet contain
  any target version/tag.
- All five feature branches were pushed over SSH. HaveAPI and vpsAdmin CI
  started on the exact tested heads; the standalone PHP and vpsfree-client
  repositories have no push workflows.

## Source integration and CI

- Fast-forwarded HaveAPI `master` to
  `efd0314bee237aa3df5f0189eddc7267c05c0fd1` and `haveapi-0.29` to
  `2d9edf01cf39963e6fd48282ae6c137c04e692dc` from fresh target worktrees.
- Fast-forwarded `haveapi-client-php` `master` to
  `03201f582e37abc586a3ac308308808b0b663539` from a fresh target worktree.
- Removed the temporary integration worktrees. No tag was created and no
  package was published.
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
