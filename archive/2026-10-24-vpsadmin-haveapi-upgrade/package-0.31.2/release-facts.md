# HaveAPI 0.31.2 release facts

Implementer2, 2026-10-28. Exact session/current and the ready retained roster
were verified from this session's tracking directory; both ambient session
markers were absent and the trusted binding matched. This bounded read-only
lookup downloaded public release archives into memory and inspected their
contents/source. No install, test, compiler, CI poll, source/ref/release/default,
cluster or KB action occurred. The stopped HaveAPI patch remains untouched.

## Actionable release and source delta

All requested packages are published at **0.31.2**: five Ruby gems, npm client,
Python wheel and sdist, and PHP client. No availability gap or watch is needed.
[HaveAPI v0.31.2](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.2) is
annotated tag `815c033be8cfca22822d0b2f80c022e959c5d0c4`, peeling to
**`819bba5110e089465535ecd71ca2eb37a7d39caa`**; the tag is unsigned.

[The complete 0.31.1 → 0.31.2 source comparison](https://github.com/vpsfreecz/haveapi/compare/v0.31.1...v0.31.2)
contains two commits: Go token documentation fix/regressions
`5a016f080bf39c184f71f6b15f904fc165448d6f`, then coordinated release metadata
`819bba5110e089465535ecd71ca2eb37a7d39caa`.

- The material implementation change is
  [`GoClient::Documentation#render_auth`](https://github.com/vpsfreecz/haveapi/blob/819bba5110e089465535ecd71ca2eb37a7d39caa/clients/go/lib/haveapi/go_client/documentation.rb).
  Both token header and query-parameter names now use `same_transport_name?`:
  each operand must be a String or Symbol, and their `to_s` values must match.
  Automatic profiles serialize the saved `:_auth_token` to `"_auth_token"`;
  live token help retains the Symbol. This now renders existing-token code.
- This also explicitly rejects nil, false and numeric transport names, even
  when both sides contain the same invalid value. Previous plain equality
  could accept equal invalid values. Different valid names still produce the
  existing mismatch limitation; absent provider/descriptor remains unavailable.
  Basic/OAuth handling, token acquisition policy, environment credential usage,
  SDK setter name and limitation wording are unchanged.
- No other server/generator implementation, HTML template, request visibility,
  authentication policy, localization, Context, route or protocol behavior changed
  in this range. Protocol remains **2.0**. The existing TypeScript normalization
  remedy is retained byte-for-byte in the new released gem.
- Generic JS source and browser bundle change only the client version constant;
  its npm manifest version changes. All **46 packaged declaration files** were
  compared directly with published npm 0.31.1 and are byte-identical. PHP changes
  its version constant/manifest; Python changes project version metadata only.
  Ruby/generator version files and sibling `haveapi-client ~> 0.31.2`
  requirements are coordinated release changes; other dependency ranges and
  runtime floors are unchanged.

## Actual archive verification

Downloaded bytes matched each gem/Python registry SHA256 and npm SHA512/SHA1.
Source comparisons are limited to the relevant Go implementation/regressions,
retained TypeScript implementation, npm bundle and PHP Client source; this is
not a repeated full-release manifest/source-inventory campaign.

| Archive / registry metadata | SHA256 of actual downloaded bytes |
| --- | --- |
| [haveapi 0.31.2](https://rubygems.org/api/v2/rubygems/haveapi/versions/0.31.2.json) | `f1c3869bea92a3902c0e52d22f036906db5d1ca964303db587c506c6d49f04a0` |
| [haveapi-client 0.31.2](https://rubygems.org/api/v2/rubygems/haveapi-client/versions/0.31.2.json) | `230e0380c24c205f1cafa6170fdeaedf0f6d0f55642ca908b5a96207e7b8d891` |
| [haveapi-go-client 0.31.2](https://rubygems.org/api/v2/rubygems/haveapi-go-client/versions/0.31.2.json) | `7fe8d1f0f1804318f97869fd9343a0bb95e125f6087be49a51407ee80aef6b6f` |
| [haveapi-rust-client 0.31.2](https://rubygems.org/api/v2/rubygems/haveapi-rust-client/versions/0.31.2.json) | `2bdd0141b75e3270c29610a3b7607a5f683eac09a4dccdaf371b4e0f37544dc5` |
| [haveapi-typescript-client 0.31.2](https://rubygems.org/api/v2/rubygems/haveapi-typescript-client/versions/0.31.2.json) | `8862b04369286a93e377717f4061b4813bf19353d2c6b47e55f003277a05bcbf` |
| [npm haveapi-client 0.31.2](https://registry.npmjs.org/haveapi-client/0.31.2) | `4fbe3543cea865aee70d858e3c65c2e182b2208aa977eb031ed49ff949a8118a` |
| [Python wheel 0.31.2](https://pypi.org/pypi/haveapi-client/0.31.2/json) | `61af39dc9da491470a2f11381c09804af48bf392f26b0f54c311c48a5af7459b` |
| Python sdist 0.31.2, same registry link | `09ad150b55e657c00681e0c9ab2bd922741d99a93796e821280f3184944d0091` |
| [PHP 0.31.2 distribution](https://api.github.com/repos/vpsfreecz/haveapi-client-php/zipball/52cf471406593edd42db32a6b61156522318dac9), observed checksum only | `32ee31846e230f0352bc74d4786d2f9bd34a13044c1ae7f39bee72ce2aa9261c` |

The Go gem **actually packages** the following files; their bytes match the
0.31.2 source tag:

| Packaged path, relative to `clients/go` | SHA256 |
| --- | --- |
| `lib/haveapi/go_client/documentation.rb` | `532b38627deec0c2c884506e514875ce696d12522276768815ac104eee7ed1e9` |
| `spec/unit/documentation_spec.rb` | `06c0e0bc28bc11cfec8c481ffad6a7682ad7c98b0ee37f40a0fdca7ddc1ace8f` |
| `spec/documentation_profile_check.rb` | `870c090f0076fed2cc0b5eccbf85be0f839508f944e777f2ec7ab19236980e1e` |
| `spec/support/documentation_profile_fixture.rb` | `9c749000af3a89c39631bec072238d6b6978fd9a2cb7f897f3fcb8061ae6df05` |

The packaged unit regressions cover all String/Symbol pairings, changed header
or query names, unsupported transport types and missing provider/descriptor.
The packaged mounted-profile regression asserts saved String versus live Symbol
query names and successful `SetExistingTokenAuth` code, using a real configured
token provider. Their presence/source parity is verified here; they were not
executed by this facts package.

The 0.31.2 TypeScript gem's `Documentation` still hashes to
`57a9d866a548c86c06c7351bff70b8b8afa18b8c281407053586639ed0b6fd53`,
matching 0.31.1 and its tag. No full-description render normalization returned.

npm integrity:
`sha512-cksLaGqdGk9c4yTm4Egwl3G4MKXUm9ICP7V+2ptW8pGe+cKICwXQvFCXZMCgqbz/Rf9rFWGdmrxC4o7gGwQs5Q==`.
Its actual browser bundle matches the tagged distribution. The
[provenance payload](https://registry.npmjs.org/-/npm/v1/attestations/haveapi-client@0.31.2)
names the same release source/tag and release workflow `40661462796`, attempt1;
its subject digest matches the downloaded archive. No signature verification
or workflow-status query was performed. Runtime/declaration entries remain
`dist/haveapi-client.js` / `dist/types/haveapi.d.ts`.

[Packagist](https://repo.packagist.org/p2/haveapi/client.json) and the separate
[PHP v0.31.2 tag](https://github.com/vpsfreecz/haveapi-client-php/tree/v0.31.2)
agree on `52cf471406593edd42db32a6b61156522318dac9`. The downloaded PHP Client
source matches the HaveAPI tag. Packagist supplies no archive checksum, so the
observed GitHub archive hash is not a registry integrity assertion.

## Generated SDK versions and profile/runtime pairing

- Go import remains `github.com/vpsfreecz/vpsadmin-go-client/client`; no generated
  Go SDK update is part of this release. The public SDK head is now
  `73f164dd5eeebfc494705ae27981d30872fa88c3`. Its
  [comparison with previously checked `1d9240f3d27b5831baf3694baab5fe06294875d8`](https://github.com/vpsfreecz/vpsadmin-go-client/compare/1d9240f3d27b5831baf3694baab5fe06294875d8...73f164dd5eeebfc494705ae27981d30872fa88c3)
  contains one README-only commit; library/module bytes have not changed.
- [Rust registry](https://crates.io/api/v1/crates/vpsadmin-client) still reports
  `vpsadmin-client` **0.1.0** as its latest stable version. Existing `0.1` registry
  guidance and async/blocking profiles are unchanged; no Rust SDK 0.31 claim.
- [Generated TypeScript registry](https://registry.npmjs.org/vpsadmin-typescript-client/latest)
  still reports **0.1.1**, with exact peer **`haveapi-client: "0.30.2"`** and the
  previously verified package integrity. The actual 0.31.2 renderer still names
  runtime0.30.2; its unchanged public SDK factory/profile contract uses
  `createClient`, `execute: spec => runtime.request(spec)` and a versioned base
  URL. `typescript: { package_name: 'vpsadmin-typescript-client' }` remains the
  minimal profile. Generic client0.31.2 adoption is separate from this pair.

These facts support a minimal adoption scope: released dependency bytes/version
metadata and actual Go token-documentation behavior. They do not replace each
owner's installed-artifact checks, appropriate consumer regression/render proof,
review, deployment checks or existing authorization. No upstream fix or local
SDK/source change is requested or performed by this receipt.
