# vpsAdmin TypeScript client 0.1.0 manual publication

The user reports publishing version 0.1.0. A read-only public registry check on
2026-10-27 confirmed its identity and exact SHA512 integrity against the retained
receipt. No upload was performed by this session. Repository integration remains
a separate user decision; automated publishing remains disabled.

## Package identity

- Name/version: `vpsadmin-typescript-client@0.1.0`.
- License: MIT; copyright 2026 Jakub Skokan, the sole documented repository author.
- Repository: `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`.
- Base: `149c72f11acef67224a47ed77711a3abb805fbd4` on `main`.
- Branch: `2026-10-27-prepare-client-releases`.
- Reviewed source: `38a25ad88d0bf3018670184620cf69cdb71e92e7` (one release
  preparation commit; no migrations or repeated dependency updates).
- Runtime: exact `haveapi-client@0.30.2` peer/development dependency.
- Generator: `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875`; API 7.0/protocol 2.0
  schema, provenance and generated sources remain unchanged.

The public registry records publication at `2026-10-27T17:40:04.673Z`, with
`latest` pointing to `0.1.0`. Name, version, MIT license, canonical repository
and `dist.integrity` match the prepared package. The earlier E404 observation
preceded this upload.

## Retained artifact and verification

- [Archive](sdk-0.1.0/vpsadmin-typescript-client-0.1.0.tgz) and
  [receipt](sdk-0.1.0/receipt.json).
- [Successful Actions run 40550139596](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40550139596),
  immutable artifact `12755255825`, built from the reviewed source above.
- Archive: 308,649 bytes, 1,358 files. It includes MIT metadata and the exact
  `LICENSE`, README, compiled ESM/declarations, schema/provenance, exporter lock,
  generator record and generated ownership manifest.
- SHA256: `5fa36fa9afa55b147bcbe9950d10579907d69ca0e3d41e2c823c42fabeeec492`.
- SHA512 integrity:
  `sha512-xAtEaXQ2OQF/arwCk0CQZNYzrHfe9CouhMN1oGchS6TU/Ul29HUWBP61rBIXs2jrA6ThvPxWbLcMHWHpLEaicg==`.

Independent review cleared the exact source with no findings. The workflow passed
locked dependency installation, offline regeneration verification, compilation,
source/consumer type checks, all 10 unit/release tests and the extracted package
consumer. Existing release tooling verified the downloaded archive's receipt;
metadata and included source records match the reviewed checkout. The archive
was downloaded from that run without rebuilding or repacking. See the
[workflow log](sdk-ci.log) for the complete batch.

## Original manual publication commands (completed)

These commands document the prepared first upload. Do not repeat publication of
0.1.0; its public integrity already matches the retained receipt.

Run from the SDK worktree:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-prepare-client-releases/vpsadmin-typescript-client
nix develop
```

Verify the retained archive against its receipt before publishing. The worktree
must remain at the reviewed source commit above:

```sh
node tools/release.mjs verify \
  --archive /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-prepare-client-releases/sdk-0.1.0/vpsadmin-typescript-client-0.1.0.tgz \
  --receipt /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-prepare-client-releases/sdk-0.1.0/receipt.json
npm login --registry https://registry.npmjs.org
npm whoami --registry https://registry.npmjs.org
npm publish /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-prepare-client-releases/sdk-0.1.0/vpsadmin-typescript-client-0.1.0.tgz \
  --ignore-scripts --access public --registry https://registry.npmjs.org
npm view vpsadmin-typescript-client@0.1.0 version dist.integrity \
  --json --registry https://registry.npmjs.org
```

Use the intended npm owner account and complete browser authentication or any
2FA prompt locally. Keep credentials out of chat and session files. Compare the
registry integrity with `receipt.json`. Publish the retained file without
rebuilding or repacking it. Local manual publication does not request OIDC
provenance.

If publication fails or its result is uncertain, check the registry's version
and integrity before retrying. A matching integrity means the registry has the
prepared bytes. A different integrity requires investigation; keep the original
archive. Do not overwrite a published version or move a release tag. Keep
`NPM_RELEASE_ENABLED` unset or false; trusted-publisher setup is a separate step
for a later release.

## Trusted publisher for a later release

Open the package's [npm settings](https://www.npmjs.com/package/vpsadmin-typescript-client/access),
find Trusted Publisher, and select GitHub Actions. The account must be permitted
to manage the published package.

| Field | Value |
| --- | --- |
| Organization or user | `vpsfreecz` |
| Repository | `vpsadmin-typescript-client` |
| Workflow filename | `release.yml` |
| Environment name | `release` |
| Allowed action | Enable direct `npm publish` |

Use the filename alone. The existing workflow calls `npm publish`, so the
default staged-publication permission is insufficient. It uses GitHub-hosted
runners and grants `id-token: write` only to its environment-protected publish
job. See the [current npm guide](https://docs.npmjs.com/trusted-publishers/).
That guide does not state the older two-day validation deadline recorded in
project documentation; its current validity was not established here.

Read-only GitHub API checks found no repository environments, no repository
variables and no rulesets. Before the next automated release, configure the
[`release` environment](https://github.com/vpsfreecz/vpsadmin-typescript-client/settings/environments)
with required reviewers and release-tag restrictions, and protect release-tag
creation. The existing workflow requires an exact `vX.Y.Z` tag matching the
package version, on `main`, and reuses its retained validated archive.

`NPM_RELEASE_ENABLED` is currently unset. Set it to `true` only after the trusted
publisher and GitHub protections are ready for a new, separately authorized
release, with reviewed source integrated into `main` under explicit integration
approval. Do not enable or tag a new run to republish 0.1.0. No npm or GitHub
settings were changed during this verification.
