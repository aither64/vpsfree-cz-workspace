# Prefix relative npm archive paths with ./

The first trusted-publishing attempt for SDK 0.1.1 failed before OIDC or upload.
`npm publish release/*.tgz` expanded to `release/package.tgz`; pinned npm 11.19
parsed that two-segment argument as a GitHub shorthand and ran `git ls-remote`
against a nonexistent `github.com/release/package.tgz.git` repository.

Use `npm publish ./release/*.tgz --ignore-scripts --access public --registry
https://registry.npmjs.org`. The explicit `./` makes npm-package-arg classify it
as a local file. Its package-manifest resolution runs before OIDC and the registry
upload, so this error did not test the configured publisher.

Verify the actual command with `--dry-run` against the original tarball, with
scripts disabled and isolated empty auth/config state. Parser classification
alone is useful diagnosis; the dry run checks the full package preparation path.
Keep the original accepted artifact and inspect registry effects before any
release recovery. Do not use token fallback to hide a workflow argument error.

See [session recovery](../../work/2026-10-27-prepare-client-releases/sdk-0.1.1.md).
