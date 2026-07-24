# 2026-07-24-vpsfreectl-snapshot-download-fix

## Goal

Fix the Ruby HaveAPI client's handling of localized choice maps, release the
fix as coordinated HaveAPI 0.29.5, and release downstream
`vpsadmin-client` 4.2.0 and `vpsfree-client` 0.20.0 so
`vpsfreectl snapshot download` works for Czech-language users.

## Affected repositories

- `haveapi`: canonical Ruby client fix, cross-client regression coverage, and
  coordinated 0.29.5 release.
- `haveapi-client-php`: standalone PHP mirror for the coordinated 0.29.5 tag.
- `vpsadmin`: `vpsadmin-client` dependency update and 4.2.0 release.
- `vpsfree-client`: dependency update and 0.20.0 release.

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
- Publish in dependency order: HaveAPI 0.29.5, `vpsadmin-client` 4.2.0, then
  `vpsfree-client` 0.20.0. Stop if an upstream artifact is not visible with
  the expected dependency metadata.
- Package publication and release-tag pushes require a final explicit approval
  after tested artifacts and checksums are presented.

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
- Verify that `rake vpsadmin:gems:client` reproduces the prepared packaged
  client metadata after HaveAPI 0.29.5 becomes visible on RubyGems, before
  publishing vpsadmin-client.
- Build and install `vpsfree-client` in an isolated gem home and verify the
  resolved dependency graph and CLI version.
- After publication, repeat registry-backed dependency resolution and verify
  every RubyGems/npm/Composer version and tag.
