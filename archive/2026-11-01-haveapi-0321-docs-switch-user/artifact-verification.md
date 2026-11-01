# Published HaveAPI 0.32.1 verification

Result: passed. All maintained packages are published as **0.32.1** and actual
registry downloads match the approved original release artifacts. This proves
package availability and the finite installed-gem capability checks below;
production consumer/browser verification remains downstream.

## Release identity

- Master: `391b0190241cf195a69b06f7297d3e4eebec5a83` (VERSION 0.32.0).
- Stable/tagged source: `9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`.
- Annotated `v0.32.1` tag object:
  `ceebc179cd4266ac4353360acf248f8d7493d5bf`.
- Original run: [41333460242](https://github.com/vpsfreecz/haveapi/actions/runs/41333460242),
  concluded success; publish job completed 2026-11-01 18:03:29 UTC.
- Original retained artifact: `13094149459`, candidate directory
  `evidence/release-41333460242`.
- Approved original manifest SHA-256:
  `37d48672acfbef768f10bb1b86787880a215056b5dc092e48ee8b6db348abe0d`.
- Public [GitHub Release](https://github.com/vpsfreecz/haveapi/releases/tag/v0.32.1)
  is published, neither draft nor prerelease. All eleven public assets match
  manifest hashes; its public manifest is byte-identical to the approved one.

## Downloaded registry artifacts

Each row records SHA-256 of the actual downloaded public-registry bytes,
independently compared with the approved manifest. RubyGems package identities,
platform `ruby` and metadata hashes also match. npm SHA-512 integrity matches the
retained tarball; PyPI lists exactly the retained wheel and sdist.

| Package/artifact | SHA-256 |
| --- | --- |
| `haveapi-client` | `fd4de589cc10ff0a446a906318b170abf22e6628771181cfb5d8a7b2a87533d4` |
| `haveapi` | `fc93f449080dc3e62d938e6d5a21f4cbed0b28dade75f5314d1fe918c16ecf18` |
| `haveapi-go-client` | `d5de7f957f9f116099ac7e69dfdd3a22ec6bedcc8f9ab464d7b74509d0ad21ba` |
| `haveapi-rust-client` | `04198e0be8d68e6edb1966a05e9c6c087ed36dee20dcd3fb5d22c489a4fd4277` |
| `haveapi-typescript-client` | `c85fd88ccebc8a12a5781ecc0e3c2f9f153c062e2c70de8dc70f438dc6274090` |
| `haveapi_client-0.32.1-py3-none-any.whl` | `2dffc07808e7c325f7254182b0c8a6939665118df74c729e984d4acbc4c4ecb0` |
| `haveapi_client-0.32.1.tar.gz` | `38031fe34556007f28f3c0a0393623427ad59fb4f17116319a41d7d0c2166d48` |
| npm `haveapi-client` | `bd7f01c18ab3e000cf1f6fc7f614b89152c9613a19c4f1bcbcff09c32dbd0166` |

PHP `haveapi/client` version 0.32.1 is indexed by Packagist at mirror commit
`4b3260d36a070ad9590ff6c3ee8a91eb873b4e84`. The mirror master and version tag
point to that commit; its `HaveAPI-Source` trailer names the exact tagged HaveAPI
source above. File content and modes from its public archive match the retained
PHP source tar after excluding mirror-owned `AGENTS.md` and `.github` metadata.

## Isolated installation and capability smoke

All five downloaded registry gems installed with conventional
`gem install --local --ignore-dependencies --no-document` into
`evidence/final-artifact-verification/gems`. They loaded under Ruby 3.4.11 with
all `BUNDLE_*`, `RUBYOPT`, `RUBYLIB` and Bundler setup overrides cleared. Existing
prepared external dependencies were reused from the stable root and Rust gem
homes; no dependency installation campaign or package rebuild ran.

Explicit gem activation proved version 0.32.1 for all five packages. All 154
loaded HaveAPI source files came from the isolated registry installation. All
five top-level libraries loaded. Ruby client construction passed, as did
`DocumentationOAuth.new` with `switch_user: true` and static
`switch_user_revoke_params: { 'close_sso' => '1' }`; the copied configured hash
and published option capability were checked without API requests or services.

The finite verification command was
`HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash /tmp/haveapi-0321-postpublish.sh`.
A fresh Luna/low utility owned it, exited 0 after 19 seconds, and left no running
operation. A separate earlier fresh utility observed the original publication
without approving, retrying or canceling it. No source/Git, build, deployment or
session lifecycle action occurred in this package.

## Evidence and limits

- `evidence/publication-ci/run-status-final.json` and `publication-job.log`
  retain original workflow success and upload/confirmation receipts.
- `evidence/final-artifact-verification/registry-provenance.json` records URLs,
  precise downloaded paths, byte lengths, hashes, GitHub Release identity and
  PHP/Packagist provenance.
- `evidence/final-artifact-verification/installed-ruby-provenance.json` records
  exact installed package paths, versions and all loaded HaveAPI source files.
- Actual downloaded packages and public release assets remain under that same
  evidence directory. The original candidate files remain unchanged.
- Complete local log:
  `/tmp/2026-11-01-haveapi-0321-docs-switch-user-postpublish-verify.log`.

This check establishes installed Ruby package capabilities, not a deployed
browser/provider flow. The existing fixed initial documentation-cookie expiry
remains unchanged. Consumer rollout must upgrade every worker before enabling
the new option and remove that option before reverting to an older HaveAPI.
No production deployment or session cleanup was requested or performed.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-haveapi-0321-docs-switch-user/
