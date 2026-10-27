# Release preparation design

Status: implementation brief ready, 2026-10-27. Design owner: architect0.

## Scope and decisions

Release every maintained HaveAPI component together as **0.31.0**. Prepare
**vpsadmin-typescript-client 0.1.0**, licensed **MIT**, for the user's manual
first npm publication. The user confirmed MIT, 0.1.0 and that the new RubyGems
pending publisher is saved. Existing release tooling is sufficient; do not
redesign workflows or change application behavior.

The user has authorized HaveAPI publication. No additional generic publication
question is needed. Protected GitHub environment approval still applies.
Default-branch integration is separately unapproved. Never run SDK `npm publish`.
Keep this session open.

## Verified sources and release units

| Unit | Canonical repository and inspected remote default | Owner |
| --- | --- | --- |
| HaveAPI | `git@github.com:vpsfreecz/haveapi.git`, `master` at `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c` | implementer0 |
| vpsAdmin SDK | `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`, `main` at `149c72f11acef67224a47ed77711a3abb805fbd4` | implementer1 |

HaveAPI's bare local `master` was stale; start from fresh `origin/master`.
The minor-release branch is `haveapi-0.31`, as required by HaveAPI's release
procedure. SDK work uses this session's dated feature branch. Implementers own
their respective worktrees and Git operations. No vpsAdmin source edit or new
API export is needed.

HaveAPI 0.31.0 includes RubyGems `haveapi`, `haveapi-client`,
`haveapi-go-client`, `haveapi-rust-client`, `haveapi-typescript-client`; npm
`haveapi-client` and its browser bundle; PyPI `haveapi-client`; and Composer
`haveapi/client` through the `vpsfreecz/haveapi-client-php` mirror. Elixir is
unmaintained and excluded. There is no separate Rust crates.io publication.

## Package A: HaveAPI release metadata

Implementer0 owns the normal `make version VERSION=0.31.0` output and
`CHANGELOG.md`. Prepare dependencies in the top-level Nix shell first. Use the
lead-approved changelog text, preserve exact published 0.30.1/0.30.2 entries,
and describe 0.31 changes by comparing released trees rather than counting
cherry-picked commits. Keep version/changelog separate from any required
functional fix; route such a fix through the lead before widening scope.

Files include `VERSION`, five Ruby version files and dependent gemspecs,
JavaScript package/source version fields, PHP version metadata, Python metadata,
and the existing example dependency updated by the prescribed target. Retain
the target's tracked `clients/js/dist/haveapi-client.js` version-line update:
it is part of the standard release path and prior release practice. Do not
stage unrelated generated output or ignored library locks. Check that local
lock updates change only intended package identities, not external dependencies.

Acceptance: all maintained component identities are 0.31.0, required shared Ruby
dependencies agree, release metadata and hook checks pass, and retained release
artifacts include all five gems plus npm/browser/PHP/Python outputs. No claim
that the release is published until every destination and receipt is verified.

Known commands, from top-level `nix develop`:

```sh
make release-deps
make version VERSION=0.31.0
make release-check
make release-test
```

Use the declared Overcommit hooks. The release procedure and development
commands are authoritative: `doc/agent-instructions/releases.md` and
`doc/agent-instructions/development.md`. After committed changes and passing
quick checks, obtain independent final review, then run the longer full release
validation through a fresh verification watcher. Prefer the existing build-only
Actions release workflow as the complete batch: it runs maintained-component
tests, packaging and retained-artifact checks. Local equivalent is `make test`
and `make release` (clean tracked checkout, empty `dist`, prepared dependencies),
with `ruby utils/release/cli.rb verify dist`. Do not duplicate complete batches
without a changed input, failed result or missing check. Artifact packaging
already exercises extracted Rust/TypeScript generator consumers; preserve that
coverage. Any uncertain-duration dependency preparation/build/test is watcher work.

## Package B: SDK metadata and manual instructions

Implementer1 owns `package.json`, root identity/license fields in
`package-lock.json`, `LICENSE`, relevant `README.md`/`docs/releasing.md` wording,
and the corresponding package-lock digest in `tools/generator.json`. Set version
0.1.0, remove `private: true`, add MIT metadata and the standard MIT text with
the documented author Jakub Skokan. Do not invent extra owners. npm includes the
license automatically; no checker or workflow change is needed solely for that.

Retain `haveapi-client` peer and development dependencies at **0.30.2**. Retain
HaveAPI generator revision **18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875**, source
digests, API 7.0/protocol 2.0 schema and provenance, and all generated bytes.
Only `tooling_sha256["package-lock.json"]` changes with the lock's release
metadata; this is required to keep offline `--check` meaningful. Do not regenerate
or repin source. This package is independent of the 0.31.0 publication schedule.

The repository has no AGENTS.md or declared hook framework at the inspected head.
Use its pinned `nix develop`; docs/development.md and docs/releasing.md provide
commands. Known setup and validation, with the exact recorded generator checkout:

```sh
npm ci --ignore-scripts --no-audit --no-fund
./tools/regenerate --haveapi-source /path/to/exact-haveapi-source --check
npm run build
npm run typecheck
npm run typecheck:consumer
node --test test/client.test.mjs test/release.test.mjs
mkdir /path/to/fresh-release-directory
npm pack --ignore-scripts --pack-destination /path/to/fresh-release-directory
node tools/check-package.mjs --archive /path/to/fresh-release-directory/vpsadmin-typescript-client-0.1.0.tgz
node tools/release.mjs receipt --archive /path/to/fresh-release-directory/vpsadmin-typescript-client-0.1.0.tgz --output /path/to/fresh-release-directory/receipt.json
node tools/release.mjs verify --archive /path/to/fresh-release-directory/vpsadmin-typescript-client-0.1.0.tgz --receipt /path/to/fresh-release-directory/receipt.json
```

Choose an actual fresh session-owned artifact directory and substitute it in
the handoff; record exact committed source and SHA256/SHA512. Build/pack only
after the source is committed so receipt HEAD identifies the payload. Quick
metadata/format checks precede independent review; longer compilation/package
consumer checks use a watcher after review. Source-only regeneration `--check`
does not change the generated tree. No live API calls are required.

Acceptance: exact 0.1.0 public metadata and MIT license in the tarball, unchanged
runtime/schema/generated contracts, matching lock provenance, passing consumer
and archive checks, and an exact tarball/receipt with manual instructions. Keep
individual artifact paths and run outcomes in session records; put reusable
first-publication guidance in docs/releasing.md and link it from README.

Manual instructions must direct the user to authenticate as the intended npm
owner (`npm login`, browser/2FA as required), verify the retained archive, then
publish **that file** with:

```sh
npm publish /exact/path/vpsadmin-typescript-client-0.1.0.tgz --ignore-scripts --access public --registry https://registry.npmjs.org
npm view vpsadmin-typescript-client@0.1.0 version dist.integrity --json --registry https://registry.npmjs.org
```

Compare registry integrity to the receipt. Never ask for credentials in chat or
record them. Do not add `--provenance` to a local manual upload. Do not claim npm
name ownership from a 404. Keep automated publication disabled for bootstrap;
tag pushes invoke publication preflight, so do not use a tag run to bootstrap
the missing npm package. Main integration and release tagging remain lead-owned
decisions; prepare everything concrete before requesting integration approval.

## Publisher setup, ordering and recovery

The new RubyGems pending publisher is **haveapi-typescript-client**, GitHub owner
**vpsfreecz**, repository **haveapi**, workflow filename **release.yml**,
environment **release**, optional Workflow Repository fields **blank**.
The user reports it saved at
https://rubygems.org/profile/oidc/pending_trusted_publishers . Its first successful
upload creates the gem and normal publisher; no seed upload or persistent token.

Before a HaveAPI tag, check the whole existing setup without reading secrets:
`HAVEAPI_RELEASE_ENABLED=true`, protected `release` environment with required
reviewers/tag policy, publishers for the other four gems, npm direct-publish
permission, PyPI publisher, PHP deploy-key secret presence and mirror state, and
Packagist indexing. Existing recent releases support readiness but do not prove
current account-only publisher settings. Record what is verified versus asserted.

After review/checks and these prerequisites, publish `haveapi-0.31` and an
annotated `v0.31.0` tag through the existing workflow. Do not move an existing
tag. The protected approval authorizes the retained artifact set; no rebuilding
after approval. The existing workflow preflights all destinations, uploads
Python, Ruby client before dependent gems, npm, then PHP, and completes the
GitHub Release after all destinations succeed. PHP mirror master synchronization
needs the lead to resolve the workspace's separate integration-approval rule
before environment approval; HaveAPI release authorization alone does not
waive that workspace gate. No HaveAPI master or SDK main merge is authorized.

Publication is not atomic. Preserve source tags, accepted tarballs/manifests,
Actions artifacts and draft release. On an uncertain upload, reconcile exact
registry identity/hashes before any retry. Follow original tooling's failed-job
recovery, never repack/overwrite accepted versions, move tags or delete releases.
Defective published content needs a new authorized patch version. SDK manual
recovery follows the same retained-file rule.

## Compatibility and evidence

No database, persisted-state, protocol, Terraform, Nix configuration or machine
deployment changes are introduced by this preparation. No coordinated node update
is required. SDK continues its documented API 7.0, ESM/ES2022, optional/nullable
response and explicit asynchronous-write handling contracts. Older runtime
0.30.2 remains intentional. The HaveAPI generator's new shared Ruby schema API
requires the coordinated Ruby-client gem; gem version/dependency and extracted
consumer checks cover this. No migrations exist in these release changes.
Consumers can retain previous runtime versions; generated source need not change.

Read-only registry observations on 2026-10-27: RubyGems new TypeScript generator
and npm SDK endpoints returned 404; RubyGems `haveapi`, npm `haveapi-client/latest`
and PyPI `haveapi-client` report 0.30.2. Public metadata cannot establish pending
publisher state.

## Release setup inspection receipt

Read-only inspection on 2026-10-27 established:

- GitHub API: `HAVEAPI_RELEASE_ENABLED` is `true`. The `release` environment has
  a required reviewer (`aither64`), allows tags `v*`, and does not prevent
  self-review. Environment secret **name** `HAVEAPI_PHP_DEPLOY_KEY` exists; no
  credential value was read. Presence does not prove the key is still valid.
- RubyGems: all four existing gems (`haveapi`, `haveapi-client`,
  `haveapi-go-client`, `haveapi-rust-client`) report 0.30.2. The TypeScript gem
  returns 404. Pending publisher configuration is user-confirmed, not API-verified.
- npm `haveapi-client` and PyPI `haveapi-client` report 0.30.2; exact 0.31.0
  version endpoints return 404. Their account-level trusted publisher identities,
  permissions and current validity were not inspected. Existing setup has recent
  publication evidence; workflow preflight and protected publication remain
  authoritative for the next release.
- PHP mirror remote default is `master`, at
  `a02dd2506209f54ea782fbd949243207bf9f93bc`, equal to peeled `v0.30.2`; there is
  no intervening untagged master commit. Its commit records
  `HaveAPI-Source: 321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`.
  Packagist indexes 0.30.2 at that exact mirror SHA. This verifies current indexing,
  not the webhook or deploy-key configuration itself. No v0.31.0 mirror tag was
  returned by the fresh remote query.
- The latest public GitHub HaveAPI Release is
  [v0.30.2](https://github.com/vpsfreecz/haveapi/releases/tag/v0.30.2), published
  2026-10-25T22:29:45Z. The five-gem tooling's existing build-only run
  [40529570376](https://github.com/vpsfreecz/haveapi/actions/runs/40529570376)
  succeeded at `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875`. This is historical
  evidence only; the release candidate still requires its own checks.
- SDK GitHub repository variable listing is empty: `NPM_RELEASE_ENABLED` is
  absent. npm SDK metadata returns 404. Keep bootstrap manual and do not enable
  automated publication as part of preparation.

No registry, repository, environment or publisher settings were changed by this
investigation. Refresh mutable preflight facts immediately before release.

## Release-blocking fixture isolation follow-up

Scope revision, 2026-10-27: implementer0 owns a test-only correction in
`servers/ruby/spec/performance/release_lineage_spec.rb`. Both native runs
40551776399 and 40551850652 failed the same seven examples with
`Expected own 0.30 patch version`; exact logs are retained in this session.
The tag run passed 213 release-tool examples and package construction, then
failed the server suite (637 examples, seven failures) before artifact retention.
This does not authorize a retry, tag change or new release version.

Root cause: the test's `contents` helper validates the live checkout VERSION
through the production 0.30-only normalizer *before* substituting its synthetic
0.30 identities. Two worker tests also request maintenance normalization against
the actual 0.31 source directory. The production restriction is intentional:
`doc/performance.md` binds this exception to one reviewed 0.30 ancestry mapping.
Do not change production normalization, ancestry, budgets, constants or workflows.

Smallest implementation:

1. In `contents(version, profile:)`, obtain the template's current own version
   directly from its `VERSION` bytes (the existing checkout is only template
   input), then substitute VERSION, local version assignments and internal
   gemspec requirements as today. Do not call `described_class.version` on the
   live template. Keep production validation on the completed synthetic fixture.
2. Add one small block-scoped helper that materializes `contents('0.30.2')` into
   a temporary source directory, creating parent directories and cleaning it
   through `Dir.mktmpdir`. Use that source for the successful `Worker.inputs`
   maintenance calls. Within that example, use RSpec `stub_const` for
   `HaveAPI::VERSION`, `HaveAPI::Client::VERSION` and
   `HaveAPI::RustClient::VERSION`, all exactly 0.30.2. Retain the separate owned
   lock/benchmark harness and actual `release: false` input check. Compare receipts
   with `capture(contents('0.30.2'))`, and require `validate_inputs` to return
   0.30.2. Keep the 0.30.99 source case to prove loaded-component mismatch rejection.
3. For the actual-worker HTML measurement example, use the same owned 0.30.2
   source directory and a matching body/version expectation. Keep actual
   `Worker#measure`, normalizer and retained raw-body assertions. Do not stub
   `Release.version`, `capture`, `html`, worker logic or `File.read` globally.
4. Preserve the real served-HTML/replay test: its existing adaptation from the
   checkout's actual rendered version to each synthetic version remains valid.
   Add or extend the minor-version rejection check using a *fully synchronized*
   `contents('0.31.0')` fixture, so the suite still proves the production guard
   rejects a different minor even when its component versions agree.

Acceptance: all previously failing examples pass under actual source VERSION
0.31.0 (and whichever subsequent version the user authorizes); synchronized
0.30 patch inputs normalize, 0.31 inputs reject, 0.30.99 loaded-version mismatch
rejects, and raw/replay tampering cases retain their coverage. All production
benchmark/runtime/reference/budget files remain byte-identical. Fixture stubs
are scoped to their example and do not leak into real served HTML or other specs.

Quick checks in the prepared top-level Nix shell: `make doc`, then
`cd servers/ruby && bundle exec rspec spec/performance/release_lineage_spec.rb`,
and targeted RuboCop plus required hooks. Keep the fix as a separate focused
test commit after the already-tagged release commit; do not rewrite the tag's
source history. Pass the committed delta and this diagnosis for affected final
review. Then run the deterministic `make test-performance`/server-suite batch
through the normal watcher where duration is uncertain, followed by the authorized
native release workflow once the lead settles tag/version recovery. No timing
benchmark campaign, reference migration or wider performance project is needed.

The lead owns the user's pending choice between an explicitly authorized failed
tag replacement and a new patch release; absent such direction the documented
recovery is a new authorized patch version with the original tag retained.

Current recovery decision (supersedes the earlier 0.31.1 direction): the user
explicitly corrected the intended version to **0.31.0** and authorized fixing
and retrying that failed, unaccepted release. The lead will replace this exact
failed tag only after the fix, recurrence verification and final review. Retain
the original tag object/source SHA and failed-run receipts. Keep the original
0.31.0 metadata commit plus one focused fixture-fix commit; do not prepare 0.31.1
or reconstruct the branch around it. No other tag rewrite is authorized.

Add one focused regression in the same spec that materializes `contents('0.32.0')`
before overriding the example's own `root` helper to that temporary template.
With that example-local root, assert `capture(contents('0.30.2'))` succeeds with
own version 0.30.2 and `capture(contents('0.32.0'))` raises the explicit 0.30
version-contract error. This covers a later-minor source template separately
from rejecting unsupported normalized input. Do not stub production methods or
global file reads. Run the focused suite on actual source version **0.31.0**
after adding the regression; retain the synthetic 0.32.0 regression permanently.
No broader fixture framework or performance changes are required.

## SDK 0.1.1 trusted-publication milestone

The lead reports HaveAPI 0.31.0 fully published/verified and SDK 0.1.0 publicly
verified. The user explicitly requests SDK **0.1.1** to verify trusted publishing.
This is a separate authorized milestone; the earlier manual-only constraint
applied to the first 0.1.0 upload. Preserve its published source
`38a25ad88d0bf3018670184620cf69cdb71e92e7` and retained archive/receipt.

Implementer1 owns only the four-file 0.1.1 version/lock/provenance-digest/README
literal update assigned by the lead. No runtime, generator, schema, behavior or
workflow changes. Independent final source/history review and applicable checks
remain required. Integration into SDK `main` needs separate explicit user
approval after the candidate is concrete; release direction does not grant it.

Implementer0 owns routine GitHub setup for
`vpsfreecz/vpsadmin-typescript-client`, using existing `docs/releasing.md` and
`.github/workflows/release.yml`. Read-only API inspection confirmed zero
environments and zero repository variables; GitHub user `aither64` is ID
`4717906`. Apply the following in order, using JSON files with `gh api --input`
and recording only safe selected response fields:

1. `PUT /repos/vpsfreecz/vpsadmin-typescript-client/environments/release`:

   ```json
   {
     "wait_timer": 0,
     "prevent_self_review": false,
     "reviewers": [{"type": "User", "id": 4717906}],
     "deployment_branch_policy": {
       "protected_branches": false,
       "custom_branch_policies": true
     }
   }
   ```

2. `POST /repos/vpsfreecz/vpsadmin-typescript-client/environments/release/deployment-branch-policies`
   with `{"name":"v*","type":"tag"}`. Inspect policies first and reuse an
   identical entry rather than creating duplicates on a retry. Do not silently
   replace settings created concurrently; inspect any changed prerequisite.
3. `POST /repos/vpsfreecz/vpsadmin-typescript-client/actions/variables` with
   `{"name":"NPM_RELEASE_ENABLED","value":"true"}`. If an uncertain prior
   response already created it, read back and accept an exact match; use the
   documented variable-specific PATCH endpoint only if an intentional update is
   actually needed. This enables the existing tagged path for this authorized
   release; it does not itself trigger a workflow or publication.

Verify `GET .../environments/release` shows the required reviewer ID/login,
self-review allowed and custom tag policy; `GET .../deployment-branch-policies`
shows the `v*` **tag** entry; `GET .../actions/variables/NPM_RELEASE_ENABLED`
shows string `true`. Record repository, environment ID, reviewer, tag-policy ID
and variable value as a compact session receipt. No credentials, secret reads,
token fallback, new workflow or ruleset redesign. No source Git operations,
main/tag push, environment approval or npm publication belongs to this setup
package. Existing authorization covers these prerequisites; report actual API
privilege/validation failures to the lead rather than inventing another gate.

The npm account's publisher must match organization `vpsfreecz`, repository
`vpsadmin-typescript-client`, workflow `release.yml`, environment `release`, with
direct-publish permission. Those account fields are user-controlled; GitHub
setup readbacks do not prove npm OIDC acceptance. The actual 0.1.1 tagged run
tests it. After separately approved main integration, the lead verifies source
and ready configuration, then runs the existing tag/environment workflow.
Its preflight checks version, license, package identity, enable flag and main
ancestry; required-reviewer/policy readiness is established by the API readbacks
above, since that helper does not query environment protection itself.
Preserve the exact workflow-built tarball/receipt and verify registry integrity
after publication. If publication is uncertain, reconcile before retrying only
the failed publish job; the existing workflow refuses repeated tag builds.

### Required release-tag creation protection

Correction to the initial setup scope: docs/releasing.md also explicitly says
to protect release tag **creation**. Environment deployment policy `v*` does
not do that. The lead approved this smallest conventional completion; it is a
documented prerequisite, not a broader ruleset redesign. Both inspected HaveAPI
and SDK ruleset baselines were empty. Do not copy that missing protection.

Implementer0 applies one SDK repository ruleset with
`POST /repos/vpsfreecz/vpsadmin-typescript-client/rulesets`:

```json
{
  "name": "Release tag creation",
  "target": "tag",
  "enforcement": "active",
  "bypass_actors": [
    {"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "always"}
  ],
  "conditions": {
    "ref_name": {"include": ["refs/tags/v*"], "exclude": []}
  },
  "rules": [{"type": "creation"}]
}
```

The current authenticated caller is `aither64` (4717906); repository permission
API confirms `permission: admin`, `role_name: admin`, and repository API
`permissions.admin: true`. Recheck before mutation. GitHub's current REST schema
defines `creation` as allowing only bypass actors to create matching refs,
permits `RepositoryRole`/`always`, and uses the ref-name conditions above.
Built-in repository role ID **5 = admin** is explicitly documented in
[GitHub's repo-standardizer reference](https://github.com/github/awesome-copilot/blob/main/skills/repo-standardizer/SKILL.md)
and used by
[GitHub Docs' own ruleset](https://github.com/github/docs/blob/main/.github/rulesets/docs/main-branch-protection.json).
Schema checked against
[GitHub's REST API description](https://github.com/github/rest-api-description/blob/main/descriptions/api.github.com/api.github.com.json).
The organization custom-role listing returned 404; that does not contradict the
verified built-in role or caller's admin permission.

Read back the returned ruleset ID with `GET .../rulesets/<ID>` and require exact
target, active enforcement, include/exclude list, sole creation rule and sole
admin/always bypass. Record baseline empty and the full nonsecret JSON/ID in
`sdk-trusted-publishing.md`, alongside environment and tag-policy IDs. On an
uncertain create, list/read before retrying; do not create duplicates. Treat any
unexpected concurrent setting or privilege/schema refusal as a lead escalation.
Do not add update, deletion, signing, status-check or other restrictions. The
existing workflow does not create its own tag, so no Actions bypass is needed.

Preparation now includes environment 25494232596 and tag deployment policy
64571929 reported by implementer0, with `NPM_RELEASE_ENABLED=true`; the creation
ruleset completes the separate outstanding prerequisite. Preserve exact IDs and
baseline evidence for independent risk review before feature/tag publication.
Rollback, only if needed and directed during this setup, deletes this exact new
ruleset ID after confirming it still has the recorded configuration and no
release run depends on it; never bulk-delete rulesets or touch concurrent policy.
For the other initially absent settings, restoration likewise means deleting
only the exact newly created variable/policy/environment after reconciling active
work. This describes recovery, not an instruction to roll back working setup.

## SDK 0.1.1 archive-path publication fix

Bounded failure diagnosis: canonical tagged run **40562213084** passed preflight
and retained-archive verification, then npm exited 128 while running
`git ls-remote ssh://git@github.com/release/vpsadmin-typescript-client-0.1.1.tgz.git`.
The preserved publish log confirms the unprefixed argument was `release/*.tgz`.
Independent inspection of pinned npm **11.19.0** confirms npm-package-arg parses
the expanded two-segment path as GitHub shorthand (`type: git`); prefixing `./`
selects `type: file`. npm's initial manifest resolution occurs before OIDC and
registry upload. This failure provides no evidence of an account/publisher fault.

Implementer1 changes only `.github/workflows/release.yml`: use
`npm publish ./release/*.tgz --ignore-scripts --access public --registry
https://registry.npmjs.org`, with one inline comment immediately above:
`# Prefix local paths so npm does not interpret them as GitHub shorthand.`
No helper, framework, new literal-assertion test, imported-action changes or
account-setting mutation. Source version remains 0.1.1 while preparing the fix;
the lead/user owns any tag/version/main integration decision.

Meaningful verification uses original tag artifact **12761282299**, preserved at
`sdk-0.1.1/tag/`, source `4689d00ca4acf0cc26a3507fc3c238b687b53475`, archive
SHA256 `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`.
In a disposable directory containing only `release/<original-tarball>`, run the
actual corrected shell command/arguments from the workflow with **`--dry-run`**
appended, using the repository's pinned Node 24.21.0/npm 11.19.0 environment.
Use empty temporary npm user/global configs and an isolated cache, unset token
and GitHub OIDC request variables without printing them, and keep
`--ignore-scripts`. Do not supply credentials or impersonate Actions. Registry
GETs during a dry run are acceptable; npm's dry-run branch suppresses upload.
Do not repack, rebuild or modify the retained tarball. Verify its SHA256 before
and after, capture dry-run success/package identity, and retain compact evidence.
This proves the actual file reaches npm's publish preparation; it does not prove
OIDC authorization, which only a subsequent authorized protected run can test.

Run existing six release unit tests and metadata checks, commit the focused fix,
then affected final review before the ordinary metadata workflow CI. No new
test merely checking command text. No main push, tag replacement, workflow rerun
or publication is authorized by this fix brief. Preserve original tag/artifact
and failure receipts. The lead reports the duplicate run **40562213605** was
rejected at its protected request (deployment **7367397343**), preventing a second
publisher. If another upload outcome becomes uncertain, reconcile registry
identity/integrity before any retry. Default recovery remains a new version
unless the user explicitly authorizes replacement of this exact failed tag.
