# Publication contract preparation

Implementer1 package, 2026-10-22. Design: [design.md](design.md); registry
observations: [registry-readiness.md](registry-readiness.md). All application
commands used the existing initiative worktree. No publishing helper, registry
upload, tag operation or default integration was executed.

## Intended changes

- New `utils/release/spec/publish_spec.rb` exercises the real generic publisher
  against mocked registry reads and command writes, using the central gem
  catalog. Seven examples cover four-gem preflight, conflicting Rust gem refusal
  before Python staging or earlier gem pushes, client-first publication, retry
  skipping matching gems, and GitHub completion blocked until Rust is confirmed.
  Fixtures contain retained bytes and hashes; no real publishing command runs.
- The release workflow includes `clients/rust/**` in push and pull-request path
  filters. Existing publisher loops already cover preflight, push and completion;
  `publish.rb` therefore needs no redundant Rust special case.
- The shared release procedure, development-command guide and Rust packaging
  guide describe the four-gem release, pending publishers, registry constraints,
  shared checks and `ruby utils/release/rust_smoke.rb dist`. The lead performed
  the final user-facing prose pass and returned ownership for commit.
- A separately reviewable PyPA action security update pins v1.14.3 to
  `7245906fb61fa33a13554f9d5fb856fe61758086`.

## Official action verification

Queried each imported action's official GitHub latest release and resolved its
existing tag to a commit on 2026-10-22. Existing refs match the latest release
for checkout v7.0.1, install-nix-action v31.11.2, upload-artifact v7.0.2,
download-artifact v8.0.2 and configure-rubygems-credentials v2.1.0. Their existing
SHAs remain unchanged. PyPA v1.14.3 is newer than the existing v1.14.2 pin.

The [official PyPA release](https://github.com/pypa/gh-action-pypi-publish/releases/tag/v1.14.3)
describes fixes for
[GHSA-5xjx-3w67-w9x9](https://github.com/pypa/gh-action-pypi-publish/security/advisories/GHSA-5xjx-3w67-w9x9)
and hashed runtime dependencies. The
[official comparison](https://github.com/pypa/gh-action-pypi-publish/compare/v1.14.2...v1.14.3)
changes its dependency constraints/hash files, Dockerfile build configuration,
internal smoke workflow and funding metadata; it does not change `action.yml`
or the public inputs used by HaveAPI. The action remains Docker-based on the
existing GitHub-hosted Linux runner, and HaveAPI keeps `packages-dir:
dist/python-publish`. No interface or runner incompatibility was identified.
The [official tag ref](https://api.github.com/repos/pypa/gh-action-pypi-publish/git/ref/tags/v1.14.3)
resolves directly to the pinned SHA above. The lead approved this dependency
update as a separate small commit, in addition to the Rust path-filter change.

## Quick verification

- `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bundle exec rspec utils/release/spec/publish_spec.rb`:
  **7 examples, 0 failures**, approximately 0.1 seconds of examples.
- Ruby syntax check for the new spec: passed.
- Workflow YAML parsing plus checks for both Rust path filters, publishing
  environment `release` and job permission `id-token: write`: passed.
- Owned-file whitespace diff checks: passed.
- `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bundle exec rubocop utils/release/spec/publish_spec.rb`:
  **1 file inspected, no offenses**.

Initial style inspection found memoized-helper count, alignment and combined-stub
issues. Refactoring those test helpers briefly exposed spy expectation ordering
and exact-count assumptions; both were corrected without application changes.
Publication specs then passed. Concurrent Nix evaluations emitted an ignored
SQLite cache-busy message; the tools ran and returned their own results normally.

No long build/integration verification has been run for this package. The lead
owns final committed-deliverable review and later long verification. Registry
account configuration and actual publication remain unverified and unauthorized.

## Commits and ownership handoff

Committed only the five approved paths during the lead-granted serialized Git
turn:

- `dd49a3d177b3863f8885b63b88a1b401e49f1f86` — publication regression specs,
  three prose-approved guides, Rust workflow path filters.
- `20998ec1901749bdc17d91858901d1925f2e036b` — PyPA v1.14.3 action pin only.

Executable Overcommit pre-commit and commit-msg hooks were verified before
commit. HaveapiI18n and RuboCop passed on the first logical commit; HaveapiI18n
passed on the workflow-only second commit. All commit-msg checks passed. An
initial width warning was fixed by wrapping the first commit's message to 72
columns and amending that unpublished commit with hooks enabled; the hashes
above are final and warning-free.

After both commits, the index was empty and all five owned paths matched HEAD.
Other owners' metadata, build, CHANGELOG and smoke-helper work was preserved.
No Git/hook operation remained running. Git/index/hooks ownership was explicitly
returned to the lead; no push was made.
