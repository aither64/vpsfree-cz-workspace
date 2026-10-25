# HaveAPI 0.30.0 release checklist

HaveAPI **0.30.0 is published and verified**. Source is
`b64fb25bea8d8222fb3263b99956c0b61438a859`, integrated into master and
`haveapi-0.30`, with annotated tag `v0.30.0`. The final source commit message is
exactly `Version 0.30.0`.

Original tagged run `39849807897`, artifact `12455689943`, succeeded on recovery
attempt 3. Its files were preserved without rebuild or substitution. All 18
external checks passed: four RubyGems hashes, npm identity/integrity, both PyPI
files, PHP provenance/content, Packagist source and public GitHub Release body
plus all eleven asset hashes. [Final verification](release-destination-verification.md)
and [machine-readable evidence](release-destination-verification.json).

Public release: https://github.com/vpsfreecz/haveapi/releases/tag/v0.30.0 .
PHP mirror/tag source is `397c95ff71ded9db98b214d58ea14a61c9973442`, recording
HaveAPI source `b64fb25b`; Packagist 0.30.0 references that commit.

Earlier metadata confirmation failures and all original artifacts remain
preserved. Follow-up fixes for publication confirmation and build warnings are
now authorized on a **development branch only**. No further release or follow-up
master integration without explicit user direction.

## Registry setup and observed publication

All HaveAPI entries use GitHub owner `vpsfreecz`, repository `haveapi`, workflow
filename `release.yml`, environment `release`:

- RubyGems existing publishers: `haveapi`, `haveapi-client`, `haveapi-go-client`.
- RubyGems pending publisher: new gem `haveapi-rust-client`.
- PyPI pending publisher: new project `haveapi-client`.
- npm existing package `haveapi-client`: trusted publisher must permit direct
  `npm publish`. A newly configured entry must complete its first successful
  publish within two days or be recreated.

The user confirmed both new pending publishers are configured, and successful
0.30.0 publication now verifies their effective permissions. RubyGems and
PyPI support pending publishers for new packages; no token seed version is
required there. See [registry evidence](registry-readiness.md).

## Repository setup and access limits

Read-only GitHub inspection confirmed HaveAPI's `release` environment, required
reviewer `aither64` and one tag rule `v*`. Self-review and administrator bypass
are currently allowed. Reads for the enablement variable, named PHP secret,
mirror deploy key and Packagist webhook returned 403; these remain unverified,
not proven missing. See [GitHub setup evidence](github-release-readiness.md).

- Protected GitHub environment `release`, with required reviewers and `v*` tag
  rules; match the registry environment exactly.
- Actions variable `HAVEAPI_RELEASE_ENABLED=true` after setup is complete.
- Environment secret `HAVEAPI_PHP_DEPLOY_KEY`, write deploy key on
  `vpsfreecz/haveapi-client-php`, and working Packagist push webhook.
- Final reviewed source/workflow and version metadata on the intended release
  revision. Eventual official branch `haveapi-0.30`, annotated tag `v0.30.0`.
  Integration/publication are now explicitly authorized; see
  [authorization](release-authorization.md).

## Separate Rust crate bootstrap

Repository `vpsfreecz/vpsadmin-rust-client` publishes Cargo package
`vpsadmin-client` (currently 0.1.0, import `vpsadmin_client`). The package and
repository names differ; do not rename by assumption. Its public registry API
returned 404. Current crates.io policy requires API-token first publication,
then crate ownership before configuring its trusted publisher. A credential is
available locally and has not been read.

The repository already has a manual workflow using protected environment
`release` and secret `CARGO_PUBLISH_BOOTSTRAP_TOKEN`. Its first-release command,
after explicit publication approval, secret setup and source/CI checks, is:

```sh
gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client \
  --ref v0.1.0 -f authentication=bootstrap
```

After the crate exists, configure crates.io trusted publisher with owner
`vpsfreecz`, repository `vpsadmin-rust-client`, workflow filename `release.yml`,
environment `release`. Future publication explicitly selects `authentication=oidc`;
the workflow has no token fallback. Exact main
`945af6a97717a7a6373507bbc9592d5cd53727c2` has green CI covering async/blocking,
MSRV, regeneration, packaging and docs. There is no version tag, and GitHub
lists zero environments; prepare the protected environment and bootstrap secret
before a separately authorized publication. Historical independent review evidence remains unverified.
See [the readiness receipt](vpsadmin-rust-client-readiness.md) for the source graph
and remaining gates. The command above has not been run. Generated runtime is embedded,
so this crate need not wait for HaveAPI 0.30 publication.

## Release verification

- Release tooling, Rust generator packaging, released 0.29.12 fixes and shared
  0.30.0 metadata are committed with all declared hooks passing.
- All requested documentation variants and optional generated-SDK profiles are
  implemented; unsupported samples show explicit limitations.
- [Final independent review](go-query-final-review.md) accepted the complete
  22-commit history and affected lanes with no findings or migrations. Earlier
  URL/auth risk reviews remain accepted through unchanged-input proof.
- Owner quick checks and mandatory hooks passed. Final assembled renderer
  checks passed 79 documentation specs plus assets and seven native Python
  checks; subsequent Go harness corrections passed focused native controls,
  syntax/style checks and independent review.
- Final exact-head artifacts/manifest and extracted Rust packaged smoke passed;
  all 12 retained files match [the SHA-256 inventory](final-artifacts-b64fb25b-sha256.json).
- Final exact-head Go acceptance compiled and executed all 16 programs, exit 0
  in 24.24 seconds. [Local result](go-query-verification-result.json).
- Installed npm/Python wheel+sdist and Rust rendered-program acceptance passed
  at the actual heads described above. Reviewed input equivalence retains their
  validity; earlier failures remain preserved as failures.
- All ten exact-head CI runs completed/success, including release packaging,
  component suites and Rust. [CI snapshot](go-query-ci-status.json).
- Feature branch is published. Integration into `master`, creation of the
  release branch/tag and registry publication are explicitly authorized in
  [release-authorization.md](release-authorization.md); execution is pending.

Publishing across registries is non-atomic. Preserve source tags, original
artifacts, checksums and draft release assets on partial failure. Retry exact
retained bytes; source corrections need a new authorized patch version.
