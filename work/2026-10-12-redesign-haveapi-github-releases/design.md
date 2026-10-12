# Proposed HaveAPI releases through GitHub Actions

Status: proposal, 2026-10-12. No workflow or publishing configuration is installed.

## Scope and baseline

Keep the shared HaveAPI version and existing `haveapi-X.Y` release branches.
Maintainers prepare version/changelog commits; automation tests, builds and
publishes their tagged source. Only the latest release branch remains supported.
Do not include either Elixir component in version changes, documentation
generation, builds, tests or publication.

The maintained deliverables are:

| Component | Artifact | Publication destination |
| --- | --- | --- |
| Ruby server | `haveapi-X.Y.Z.gem` | RubyGems.org |
| Ruby client and CLI | `haveapi-client-X.Y.Z.gem` | RubyGems.org |
| Go client generator, implemented in Ruby | `haveapi-go-client-X.Y.Z.gem` | RubyGems.org |
| JavaScript client | npm tarball and browser bundle | npm and GitHub release assets |
| PHP client | clean tracked subtree archive | `vpsfreecz/haveapi-client-php`, consumed through Composer/Packagist |

Current registry metadata reports `0.29.9` for the three gems and npm. The PHP
mirror has `v0.29.9`. Master still declares `0.29.0`; the supported release branch
declares `0.29.9`. Never choose a new version from master's VERSION implicitly.

## Maintainer interface

1. For a new minor/major line, prepare the new release branch from master.
   For a patch, prepare the existing supported release branch with the required
   backports, preserving the documented cherry-pick provenance.
2. Run the existing `make version VERSION=X.Y.Z`, update CHANGELOG.md, check and
   commit the release metadata under the repository's hooks.
3. Push the approved release commit and an annotated `vX.Y.Z` tag. A tag starts
   testing and building, while a protected GitHub `release` environment gates
   publication and provides the maintainer's explicit publication approval.
4. Inspect the workflow's artifact/version summary and approve publication.
5. The workflow publishes the maintained components and finishes a GitHub
   Release with the relevant changelog section and downloadable artifacts.

Provide `workflow_dispatch` as a build-only path, with no publication or mirror
write access. This permits pipeline validation on an implementation branch
before a real version is prepared. Recovery uses the original release run and
retained artifacts; it does not accept arbitrary new source for an existing tag.

## Workflow and artifact contract

Add `.github/workflows/release.yml`. Use GitHub-hosted Linux runners, the locked
top-level Nix development shell for release commands, and upstream-verified
action versions pinned to reviewed commit SHAs where practical. The current
default shell needs Go for the generator's integration specs.

The pipeline has these stages:

1. **Validate:** reject malformed tags, mismatches between tag and shared VERSION,
   mismatched maintained-component versions or gem dependency constraints, a
   missing changelog entry, and tags outside their intended release line.
   Inspect a clean tagged checkout; never silently bump versions in CI.
2. **Test and build:** install component dependencies; generate shared docs for
   `servers/ruby` only; run translation freshness checks and all maintained
   component tests; build the three gems, rebuild JS and `npm pack` it, and
   archive the tracked PHP subtree. Run existing server packaging specs and
   smoke-check the actual npm tarball and gem contents. New versions must not
   require the same version to be available remotely to build locally.
3. **Retain:** upload artifacts and a machine-readable manifest containing source
   commit, tag/version, package identities, resolved toolchain/dependency evidence
   and SHA-256 hashes. A draft GitHub Release can retain these before publication;
   build-only runs use Actions artifacts without creating a draft release.
4. **Publish:** protected jobs download and validate the retained artifacts.
   Push the Ruby client gem before the server and Go generator gems. Publish the
   prebuilt npm tarball. Synchronize and tag the PHP mirror over SSH. No publish
   job rebuilds a package or runs dependency installation from package source.
5. **Finalize:** check all destination receipts, then publish the GitHub Release.
   Packagist indexing is asynchronous; distinguish a successful mirror push from
   confirmed availability of its version through Packagist.

Serialize release publication across versions, with `cancel-in-progress: false`.
Build-only runs need not hold the publication lock. Preserve the source tag and
refuse to move or overwrite published tags, registry versions or release assets.
Retries download original artifacts; if they have expired, stop and use a
documented recovery path rather than assuming a rebuild is identical.

## Publishing and approvals

Configure three RubyGems trusted publishers and one npm trusted publisher for
the exact repository, workflow filename and `release` environment. Only publishing
jobs receive `id-token: write`; ordinary tests/builds use read permissions.
Use the official RubyGems credential action and explicit gem pushes of saved
artifacts rather than a release action that also rebuilds or creates tags.
Use a Node/npm version meeting current OIDC requirements. Fix the JS package's
repository metadata to point to `https://github.com/vpsfreecz/haveapi` and record
the `clients/js` directory. npm automatically supplies provenance when supported.

PHP needs separate authorization because GITHUB_TOKEN is scoped to the workflow's
repository. Use a write deploy key for `haveapi-client-php`, stored only in the
protected environment, with verified GitHub SSH host keys. Preserve its package
name `haveapi/client` and root-layout Composer repository. The mirror helper
uses the saved tracked subtree, preserves `.git` and repository-owned workflow
configuration, records the HaveAPI source commit, and refuses unexpected mirror
divergence. Commit the source update and push master plus the new tag atomically.
No force pushes. Verify or configure Packagist's push webhook once.

The release procedure must explicitly explain that approving publication also
authorizes the source synchronization into `haveapi-client-php/master`. Preparing
this design or its implementation does not approve any current default-branch
integration, account configuration or new-version publication.

## Proposed files and boundaries

| Path | Responsibility |
| --- | --- |
| `.github/workflows/release.yml` | Events, dependency graph, permissions, approval gates, retained artifacts and release summary |
| `utils/release/` helpers | Validate metadata; build and inspect artifacts; produce manifest; verify existing registry content; synchronize PHP |
| `Makefile` | Keep `make version`; expose useful build/check commands; make shared docs Ruby-only; replace unsafe unqualified local publishing with the Actions procedure |
| `flake.nix` | Ensure the top-level release/test shell includes required tools, notably Go |
| `clients/js/package.json` | Correct publishing repository metadata and expose a useful packaging command if needed |
| `doc/agent-instructions/releases.md` | Authoritative maintainer procedure, one-time setup, build-only verification and recovery |
| `README.md`, `AGENTS.md` | Discoverable link and consistent agent publication rules |

Use small helpers with explicit inputs (source tag, artifact directory, manifest)
and nonzero failure statuses. Choose filenames and language during implementation
to fit nearby code; do not add a generic release-management framework. Add only
meaningful release tests for rejection, content verification and recovery paths.
Application libraries, protocol behavior, translations, downstream pins, separate
JS mirror development and generated API-specific Go clients are outside scope.
Do not modify generated translation artifacts as part of release automation.

## Invariants and failure recovery

All artifacts describe one source commit and shared version. Publication uses
exactly the tested and retained files. Documentation must be inside the server
gem, and the npm tarball must contain the freshly built browser bundle. Archives
must exclude credentials, dependencies, caches and incidental build files.

Registry publication is not an atomic transaction. After partial success, retain
the draft and successful receipts; report what remains. A rerun checks each
destination before writing. Skip an already published version only if its
downloaded content matches the saved artifact (gem checksum, npm integrity and
expected package identity, or PHP source/tree provenance). Conflicts fail loudly;
do not catch all push failures or assume an existing version is ours.

An npm or gem error after an accepted upload can be recovered through that same
content comparison. A PHP failure after an accepted atomic push is recovered by
checking the expected tag and source tree. A missing Packagist version calls for
hook/indexing diagnosis rather than retagging or rebuilding. Defective published
content requires a new patch version; never mutate the accepted version.

## Compatibility, deployment and rollback

No changes to persisted state, schemas, seeds, APIs, CLI contracts, protocol
messages, generated module options or configuration pins. No migrations. Package
identities and supported versions remain unchanged; mixed runtime versions and
rollback compatibility remain the existing application's responsibility.
No coordinated machine or vpsAdminOS update is required.

Rollout: implement on the session feature branch, pass quick checks, commit and
obtain final independent review, then run longer checks and safe Actions builds.
Integrate into explicitly approved master/release targets. The workflow must
exist in the tagged source on the supported release branch before its first tag
is pushed. Set up registry trust, approval protections and PHP credentials before
authorizing that first real publication. Do not invent a release version now.

Before publication, recovery can disable the new workflow and continue with a
documented manual process after explicit authorization. After publication,
consumers may select an earlier package version; do not delete registry versions
or move tags. No database or on-disk state conversion is introduced.

## Acceptance criteria and verification

- All maintained components can be built from a clean checkout; Elixir is not
  accessed by release operations.
- A dry run creates the expected artifacts and summary without credentials or
  any production write.
- Invalid tags/version metadata and missing shared docs fail before publication.
- All maintained-component tests and artifact smoke checks pass before approval.
- Publication uses saved artifacts and minimum job permissions, with OIDC for
  RubyGems/npm and scoped SSH credentials for PHP.
- Successful publication preserves package names and tags and creates a complete
  GitHub Release. Partial publication remains visible and recoverable.
- Existing identical versions resume safely; differing content fails. A
  mismatched or moved tag and missing retained artifacts cannot silently publish.
- Release docs agree with implementation and cover one-time setup, operator
  approval, normal releases, dry runs and partial-failure recovery.

Quick checks: workflow lint, helper syntax, version/checksum/manifest validation,
meaningful isolated rejection and recovery checks, doc command/link consistency,
and declared hooks. Commit the full deliverable, then use retained reviewer0
(Astra/xhigh, read-only) for mandatory final review, including complete
base-to-head history, final diff and an explicit no-migrations conclusion.

Longer checks, launched and monitored by a fresh Luna/low utility watcher after
review: complete component suites in Nix, clean build, extracted gem/npm smoke
checks, PHP synchronization against disposable local Git repositories, rerun and
concurrency exercises, and a build-only GitHub Actions run. A live registry push
is a separately authorized release operation, not an automatic test.

## Primary references

- [RubyGems trusted publishing](https://guides.rubygems.org/trusted-publishing/)
- [Official RubyGems credential action](https://github.com/rubygems/configure-rubygems-credentials)
- [npm trusted publishers](https://docs.npmjs.com/trusted-publishers/)
- [GitHub token scope](https://docs.github.com/en/actions/concepts/security/github_token)
- [GitHub repository credentials](https://docs.github.com/en/actions/concepts/security/compromised-runners)
- [Packagist version discovery and hooks](https://packagist.org/about)

Account-side settings and the current Packagist hook were not inspected. Exact
action revisions must be checked against their upstream repositories during
implementation. Dependency locking is incomplete in the existing tree; retain
and reuse artifacts rather than claiming that independent builds are identical.
