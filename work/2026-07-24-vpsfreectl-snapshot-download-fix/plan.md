# 2026-07-24-vpsfreectl-snapshot-download-fix

## Goal

Fix the Ruby HaveAPI client's handling of localized choice maps, release the
fix as coordinated HaveAPI 0.29.5, then update every vpsAdmin HaveAPI consumer
and prepare the cleaned vpsAdmin 4.2.0 branch for review. Downstream client
publication is deferred until separately approved.

## Affected repositories

- `haveapi`: canonical Ruby client fix, cross-client regression coverage, and
  coordinated 0.29.5 release.
- `haveapi-client-php`: standalone PHP mirror for the coordinated 0.29.5 tag.
- `vpsadmin`: coordinated HaveAPI dependency update and cleaned 4.2.0 review
  branch.
- `vpsfree-client`: a dependency/version branch exists from the initial plan,
  but its integration and release are explicitly deferred.

## Implementation

1. Implement the canonical fix against HaveAPI `master`. For hash-valued
   inclusion metadata, compare keys and typed input by their JSON-visible
   string values; retain exact array matching.
2. Add a localized-choice action to the shared client test API. Cover valid
   localized choices in the maintained Ruby, JavaScript, PHP, and generated Go
   client integration tests, plus focused Ruby rejection/type cases.
3. Backport the functional commit with `cherry-pick -x` to `haveapi-0.29`.
   Update the coordinated version and changelog in a separate 0.29.5 commit.
4. Synchronize the 0.29.5 PHP subtree into `haveapi-client-php`.
5. On current vpsAdmin master, require `haveapi-client ~> 0.29.5`, document the
   client changes since 4.1.0, create a separate shared `Version 4.2.0`
   commit using the repository task, and update the packaged-client
   lock/gemset metadata to the same dependency graph.
6. In `vpsfree-client`, require `vpsadmin-client ~> 4.2`, then create the
   historical separate changelog/version commit for 0.20.0.

## Compatibility and deployment

- There is no API wire, database, persisted-state, or server deployment
  change. The Ruby fix only accepts values that the server already declares
  valid.
- Old and new servers can be used with the fixed client. Rolling back the
  client is mechanically safe, but restores the localized-choice failure.
- `vpsadmin-client` 4.2.0 is intentionally cut from current master and includes
  accumulated client fixes since 4.1.0. Shared vpsAdmin version markers are
  updated by the established version task, but no server rollout is implied.
- HaveAPI 0.29.5 is coordinated across the Ruby server/client, Go generator,
  JavaScript package, and PHP metadata, although only Ruby client runtime
  behavior changes.
- HaveAPI 0.29.5 is published and verified. vpsAdmin and vpsfree-client tags,
  default-branch integration, and package publication are not authorized by
  the HaveAPI-only approval.
- The vpsAdmin review branch must resolve only published artifacts and remain
  safe to review and test without implying a server deployment.

## Testing and review

- Run focused HaveAPI Ruby specs and quick syntax/lint checks first.
- After all intended commits and quick checks, run the mandatory standalone
  change review and resolve or discuss significant findings.
- Run HaveAPI's full `make test`, hooks, and `make release` in top-level
  `nix develop`.
- Test downstream gems before publication with temporary Bundler path
  overrides to the local 0.29.5/4.2.0 sources, without editing tracked
  dependency files.
- Run vpsAdmin client RSpec, RuboCop, hooks, gem build, and isolated install
  smoke tests.
- Verify that `rake vpsadmin:gems` reproduces the prepared package metadata
  after HaveAPI 0.29.5 becomes visible on RubyGems. Any vpsadmin-client
  publication remains a separately approved future action.
- Build and install `vpsfree-client` in an isolated gem home and verify the
  resolved dependency graph and CLI version.
- Verify the published HaveAPI RubyGems/npm/Composer artifacts and repeat
  vpsAdmin generation from those registries before submitting the review.
