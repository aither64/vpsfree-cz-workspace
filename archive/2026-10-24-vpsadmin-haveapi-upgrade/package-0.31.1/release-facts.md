# HaveAPI 0.31.1 released artifact and rendering facts

Implementer2, 2026-10-27, after the 22:26:35 UTC registry-availability handoff.
Read-only public metadata/archive/source inspection; no install, executable
import, test, build, CI query, Git/ref mutation, KB or cluster action. This is
the single new receipt for this package. Session identity was reconfirmed from
the exact tracking CWD; both ambient session markers were absent and the trusted
session/workspace binding matched.

## Source and relevant release delta

[v0.31.1](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.1) is annotated
tag `4d665d6bc1a2f6a62710219150afd2175c312347`, peeling to
**`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`**. The tag is unsigned.
[Comparison from v0.31.0](https://github.com/vpsfreecz/haveapi/compare/v0.31.0...v0.31.1)
(`c9124da141adc258fbbaf67d4ec19ee3f8580849`) contains four commits:

- `f47aacc1545fc768743055d35aa4582821d97427`: bound TypeScript documentation normalization.
- `baa736f2f3e3c2e7a50027f7abdc019dca672f5a`: all-renderer performance coverage.
- `4dd137d6f354f312ea09bf41b6063cd5f7519067`: synchronized own-package version comparisons.
- `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`: 0.31.1 release metadata.

The actual released TypeScript generator gem contains the fix. Its
[`Documentation` source](https://github.com/vpsfreecz/haveapi/blob/d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42/clients/typescript/lib/haveapi/typescript_client/documentation.rb)
is byte-identical to the tagged file, SHA256
`57a9d866a548c86c06c7351bff70b8b8afa18b8c281407053586639ed0b6fd53`.
It is also identical to the implementation retained in our stopped local patch;
that local worktree/ref was only read and remains unchanged.

- Rendering no longer recursively normalizes `context.description`. Shallow
  member maps select the resource path/action, advertised authentication provider
  and `meta.namespace`, then normalize selected values.
- Last-inserted string/symbol key collision semantics, canonical action
  precedence, unique-alias fallback and ambiguous-alias rejection remain.
  Basic-before-token selection, advertised-provider/explicit-description
  validation and token-header matching remain. Existing selected action/sample
  validation, mount/version handling and frozen detached snapshot ownership stay.
- No shared cache or new authorization/locale policy was introduced. The renderer
  consumes the current request description; anonymous-help visibility is not
  changed by this release. Emitted program construction and limitation wording
  are unchanged. No server HTML template, server authorization implementation,
  Context implementation or profile registration code changed in this range.
- The release adds deterministic selected-subtree and all-renderer/mode work and
  allocation contracts, including full pages and authorization filtering. Those
  checks become required before paired performance comparisons; the performance
  workflow covers all client directories. Paired comparisons may synchronize
  HaveAPI's own package versions while retaining strict external dependency and
  runtime comparisons. These are development verification-policy changes.
- Generic JS and PHP runtime-source changes are version constants only. Python
  project metadata changes its version; package names, protocol 2.0 and declared
  runtime floors/dependency ranges remain unchanged.

Static source presence does **not** establish consuming-page latency. A31-R1
remains dependent on A0's installed-source identity and actual qualified
anonymous/member/admin measurements and authorization/locale/output checks.

## Downloaded release bytes

All five gem SHA256 values, npm SHA512 integrity/SHA1 and Python wheel/sdist
SHA256 were computed over downloaded archive bytes and matched registry metadata.
The PHP registry provides no archive checksum; its digest below is observed.

| Archive | SHA256 |
| --- | --- |
| [haveapi 0.31.1](https://rubygems.org/api/v2/rubygems/haveapi/versions/0.31.1.json) | `fcfe0dcfb6ef22bb08909ecdcccc8567ddf8eab15e07136ee87b5d9a191c66e8` |
| [haveapi-client 0.31.1](https://rubygems.org/api/v2/rubygems/haveapi-client/versions/0.31.1.json) | `c7767dde7597e385c262935892d2d8961bfaecee9017b046c75c78354d878fff` |
| [haveapi-go-client 0.31.1](https://rubygems.org/api/v2/rubygems/haveapi-go-client/versions/0.31.1.json) | `ff4659404996fd17ab77d848ce99a0693416a3728e1a4f730143bbb1a43088cc` |
| [haveapi-rust-client 0.31.1](https://rubygems.org/api/v2/rubygems/haveapi-rust-client/versions/0.31.1.json) | `93f8a71c92f00b2b2057aed7329f490f5d50966ba9c8c1a1aa7bf4cd3c26a773` |
| [haveapi-typescript-client 0.31.1](https://rubygems.org/api/v2/rubygems/haveapi-typescript-client/versions/0.31.1.json) | `597a6fe9f7d95f4e40cb6a4795352e5798082d3df65944f19ea060841742bb02` |
| [npm haveapi-client 0.31.1](https://registry.npmjs.org/haveapi-client/0.31.1) | `08383df15f590e319d0140c7fda6c096b04a8237ca316e609424bf7745e31d54` |
| [Python wheel 0.31.1](https://pypi.org/pypi/haveapi-client/0.31.1/json) | `a552c2e864231acad8399998add5cd0c14172356449f456c369c73392360e529` |
| Python sdist 0.31.1, same registry link | `be85d1b664d1c2c778de2340cae1943589eff76582459f65d92a85c798b342d5` |
| [PHP 0.31.1 GitHub distribution](https://api.github.com/repos/vpsfreecz/haveapi-client-php/zipball/29db964d90b69aa8a37518d5f16ca7e9743fa638), observed only | `b348582b5d6c48d2d67c8c6eaf6d26d1a141dd5b5544ecaa97b4905fa5e259fe` |

Source comparisons were bounded to relevant authored content. Packaged
`lib/`, `bin/` and `templates/` files that also exist at the tag all matched:
server 114, Ruby client 49, Go 26, Rust 10, TypeScript 10. Generated server docs
and every embedded/generated artifact were not exhaustively compared. The npm
bundle, package manifest, README and both async guides match tagged bytes.
All 18 Python runtime modules match in both archives. Sdist `pyproject.toml`
has formatting-only differences; parsed TOML equals the tagged file. No
byte-identical whole-sdist/source claim is made.

The npm integrity is
`sha512-W3pgK2807qLVr3Yr1yQ+illlvcNasVDM7Dr/zxUuMUK7a0lHEkkxhdUeICGkWXb9Smy9FPIY5UcQCn6JlXEtag==`.
[Published provenance fields](https://registry.npmjs.org/-/npm/v1/attestations/haveapi-client@0.31.1)
identify the same source commit/tag, `.github/workflows/release.yml`, run
`40592240342`, attempt 1; its artifact subject digest matches downloaded bytes.
No workflow status or provenance signature verification was performed.

[Packagist](https://repo.packagist.org/p2/haveapi/client.json) and the PHP
[`v0.31.1` tag](https://github.com/vpsfreecz/haveapi-client-php/tree/v0.31.1)
agree on mirror commit `29db964d90b69aa8a37518d5f16ca7e9743fa638`.
Its 20 `src/` files and `composer.json` match the HaveAPI tag's PHP subtree.
The GitHub source-tarball digest observed for the HaveAPI commit was
`fb3adbf60954bba392ecfbdbc5c75d0b6608842f8ed7782c7a4045ec4dac20bd`;
this identifies the observed archive, not an independently signed release.

## Reverified generated SDK/runtime and profile contract

Registry latest remains
[`vpsadmin-typescript-client@0.1.1`](https://registry.npmjs.org/vpsadmin-typescript-client/0.1.1).
Downloaded SDK archive SHA256 remains
`9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`.
Its package manifest and declarations still specify API 7.0, ESM/ES2022, root
export `.` with `dist/index.js` and `dist/index.d.ts`, and exact peer
**`haveapi-client: "0.30.2"`**. Root exports retain `createClient`,
`createVpsAdminClient` and `createHaveApiExecutor`.

The actual 0.31.1 gem's
[profile guide](https://github.com/vpsfreecz/haveapi/blob/d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42/clients/typescript/docs/documentation.md)
and renderer still specify **runtime 0.30.2** for generated SDK examples;
the guide itself matches tagged bytes. Generic consumer runtime 0.31.1 adoption
is separate. Do not change the generated pair or claim an SDK peer upgrade.

Minimal profile remains `typescript: { package_name: 'vpsadmin-typescript-client' }`.
Optional `package_version` accepts concrete SemVer; omission delegates package
selection. Optional `snapshot_path` and matching installed `generator_version`
remain available. No new SDK wrapper/factory config is required. Rendered code
imports public `createClient` and supplies `execute: spec => runtime.request(spec)`
using a mounted **versioned base URL**. The SDK's generated calls return raw
`RequestResult<T>` (`data`, `meta`, `envelope`, `httpStatus`); generic async client
actions retain `{value, response}`. No consumer install/typecheck/runtime result
is asserted here; A/C/E3 own their actual installed artifacts and checks.

The user owns upstream fix implementation/release elsewhere. Our stopped local
patch remains reference evidence only. No readiness, release approval, source
adoption, staging or default integration follows from this facts receipt.
