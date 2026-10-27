# SDK 0.1.1 failed-run effects reconciliation

Read-only recovery package owned by implementer0, checked 2026-10-27 around
18:53Z. Source repair, tests and publication belong to implementer1/lead.
No source edits, Git/ref mutations, settings changes, uploads, retries, tests,
claim or machine reservation were performed in this package.

## Terminal workflow and deployment effects

Both exact tag runs bind source
`4689d00ca4acf0cc26a3507fc3c238b687b53475` and tag `v0.1.1`:

| Run | Build | Publish | Final state |
| --- | --- | --- | --- |
| Canonical `40562213084` | Job `122393957336`, success | Job `122394355033`, failure at 18:45:54Z in `Verify and publish the approved archive` | completed/failure |
| Duplicate `40562213605` | Job `122396680814`, success | Job `122397107267`, failure at 18:50:11Z, empty steps list | completed/failure |

Duplicate deployment `7367397343` records terminal failure at 18:50:11Z after
the lead rejected its protected request. Its check annotation says:
“The deployment was rejected or didn't satisfy other protection rules.”
The publish job ran no steps; its log endpoint has no blob. Neither run has a
pending deployment. The duplicate therefore executed no second publication.

The source owner's established canonical diagnosis remains the release record:
the bare `release/*.tgz` expansion was treated as GitHub shorthand before npm's
OIDC/upload path. This package does not repeat that diagnosis or its tests.
No account-authentication or provenance result is inferred from the failed run.

## Public npm state

Fresh cache-distinct exact-version and packument reads confirm:

- `vpsadmin-typescript-client@0.1.0` still has the expected name, version, MIT
  license and canonical repository identity.
- Its integrity is unchanged and matches the original retained 0.1.0 archive:
  `sha512-xAtEaXQ2OQF/arwCk0CQZNYzrHfe9CouhMN1oGchS6TU/Ul29HUWBP61rBIXs2jrA6ThvPxWbLcMHWHpLEaicg==`.
- Exact 0.1.1 version endpoint returned HTTP 404; the packument has no 0.1.1
  entry, and `latest` remains 0.1.0.

This is read-only effects reconciliation, not a request to republish 0.1.0 or a
claim about npm trusted-publisher acceptance.

## Original accepted build artifact retained

Original canonical artifact ID `12761282299` remains unexpired, expires
2026-11-26T18:41:34Z, name
`npm-package-4689d00ca4acf0cc26a3507fc3c238b687b53475`.
Fresh download of the actual original ZIP matches the API digest:
`sha256:b7910cb22652b39f45d3a0f5fab8191a1cc6112a5c904bc654374bbca38376ae`.
The two ZIP entries are `receipt.json` and
`vpsadmin-typescript-client-0.1.1.tgz`; both match the previously retained local
files byte-for-byte. The receipt binds the exact source/tag above, package
0.1.1 and archive SHA256
`9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`, integrity
`sha512-G7YlKCe4jX/ikmDYUT4SdZM2hf8Qvi1mQYNVetdNtHYYm4fzfLhBhcQEZYgDs7shVaAA5Bk6NCwcezqRPAWohA==`.
Original files remain in `sdk-0.1.1/tag/`. No repacking or replacement occurred.

The duplicate's separate artifact `12760669517` is also unexpired and belongs
only to duplicate run `40562213605`; it was not substituted for the canonical
accepted artifact. Its ZIP digest is
`b52fe79fbb34a2cfae2215439e879712af8393704badc0b30ea200051eb8763e`.

## Target refs and selected coordination guide

Implementer1 explicitly permitted a read-only remote-ref check after confirming
they were editing only their own feature worktree, with no shared main/tag
mutation. SSH `ls-remote` then showed:

- `main` and published session feature branch both
  `4689d00ca4acf0cc26a3507fc3c238b687b53475`.
- Annotated `v0.1.1` object
  `cb914823d2e74e9565e56a1af770b0d129fd0876`, peeled to the same source.

Read `workspace-host coordination guide` in full from selected package
`/nix/store/yi4hlb3s8lmm8w2bv34z35yhy6fmqk29-dev-workspace-0.2.0`, coordination
catalog digest `4b78710cec4cda72b150007131b36b252d54311fdfd438412d587f08e65c4a12`.
The short repository-claim contract still separates preparation/review/tests
from fresh target checks, approved fast-forward merge/hooks, SSH push, remote
proof and immediate release. Resource waits and uncertain mutations retain
their original reconciliation contracts. This read grants no integration,
failed-tag replacement or lifecycle authority.

Setup settings are unchanged. Lead owns the next concrete source/review and
failed-tag recovery approval boundary. No operation remains running from this
read-only package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/
