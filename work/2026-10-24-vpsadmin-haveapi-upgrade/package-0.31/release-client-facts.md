# HaveAPI 0.31.0 release and TypeScript client facts

Observed 2026-10-27, approximately 19:20–19:26 UTC, by implementer2.
Scope: public release metadata and published archive inspection only. No package
installation, executable import, build, test, SDK regeneration, CI observation,
repository/ref mutation or cluster/KB write was performed. This receipt is the
only new local file. Public package availability is not consumer acceptance.

Identity: both ambient `DEV_SESSION_*` variables were absent. `dev-session
current` from the workspace root reported no current session; rerunning from
the exact session tracking directory printed
`2026-10-24-vpsadmin-haveapi-upgrade`, matching this conversation's trusted
workspace/session binding. The live roster retained implementer2 and architect0
as ready with `workspace_write`. Workspace routing, documentation/handoff skills
and KB guidance were read. Architect0 owns server configuration/source design;
this lookup read only the generator's public configuration guide.

## Released HaveAPI artifacts

[HaveAPI v0.31.0](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.0)
is annotated tag `d300dfa8715cca35c29bce312333ece886b5e74e`, peeling to
`c9124da141adc258fbbaf67d4ec19ee3f8580849`. The tag is unsigned.
The five Ruby archives, both Python archives and both npm archives below were
downloaded into memory and hashed. Ruby/Python SHA256 and npm SHA512 match the
corresponding registries. No registry signature/provenance signature verification
was run; npm provenance payload fields were inspected and their artifact subject
digests matched the downloaded packages. Full archive-to-source equality was
not established by this package.

All five Ruby packages are released at **0.31.0**. Registry metadata links:

| Package | Required Ruby | Verified archive SHA256 |
| --- | --- | --- |
| [haveapi](https://rubygems.org/api/v2/rubygems/haveapi/versions/0.31.0.json) | >=3.2.0 | `c4e535b8f760ddd4feeeb79f7a239fcffe3df6cde9bb7a41e06d9474ec6fe541` |
| [haveapi-client](https://rubygems.org/api/v2/rubygems/haveapi-client/versions/0.31.0.json) | >=3.0 | `513e0ecde4c7afa289e970503e9a588507f70de051354c2fa95e0f5f3fd9254a` |
| [haveapi-go-client](https://rubygems.org/api/v2/rubygems/haveapi-go-client/versions/0.31.0.json) | >=3.2.0 | `fe1a0ac06ad643d11bbbea8d9d541156d4230517c21465c1f3f2a7103a0906ed` |
| [haveapi-rust-client](https://rubygems.org/api/v2/rubygems/haveapi-rust-client/versions/0.31.0.json) | >=3.2 | `28f5411113f7780b6e3d76a22aa5191e18abe18ed3ae02e167b19be4bb452d2b` |
| [haveapi-typescript-client](https://rubygems.org/api/v2/rubygems/haveapi-typescript-client/versions/0.31.0.json) | >=3.2 | `34815ad52c59f59513f710fb123d290536ec9886ecd11634f53262964f69f6ff` |

Each archive contains its own `VERSION = '0.31.0'`; server and Ruby client retain
protocol **2.0**. The server and all three generators require Ruby
`haveapi-client ~> 0.31.0`. The Rust generator additionally requires
`fiddle ~> 1.1, >= 1.1.8` and `tomlrb ~> 2.0`. Generator release versions are
separate from generated SDK and API schema versions.

- **Generic JS/TS:** npm [`haveapi-client@0.31.0`](https://registry.npmjs.org/haveapi-client/0.31.0).
  SHA256 `1f01aea5cd29415013b21cbe763ae5823d6889d8b6a93567916801ac50705af3`;
  integrity `sha512-KdEEu7jMFWFTHBVWtSSjZoB6WA68BDSE68IMW8LXUverfcg8V1tzptBcgu+IUOwOcqayq9OaPxJX676Cir+S0g==`.
  Runtime entry `dist/haveapi-client.js`, declarations
  `dist/types/haveapi.d.ts`, no `engines` minimum or `exports` map declared.
  [npm provenance](https://registry.npmjs.org/-/npm/v1/attestations/haveapi-client@0.31.0)
  identifies the HaveAPI tag/commit above and release workflow
  `40554625752`, attempt 1. No CI status was queried.
- **Python:** [`haveapi-client==0.31.0`](https://pypi.org/pypi/haveapi-client/0.31.0/json),
  Python >=3.11, `httpx>=0.28.1,<1`, `anyio>=4.15,<5`.
  Wheel SHA256 `016a08dfe2ca6c629034bb2308267c234a21cb00edda019bd56a206e8c1e1aca`;
  sdist SHA256 `75c48e61e7cb87639f6b0e32f4beca4cd458a3a591a99b1afbb9e1f41d78f7cf`.
  Public imports remain `Client`, `AsyncClient`, `BasicAuth`, `TokenAuth`,
  `OAuth2Auth` from `haveapi_client`, verified in the wheel's `__init__.py`.
- **PHP:** [`haveapi/client:0.31.0`](https://repo.packagist.org/p2/haveapi/client.json),
  PHP >=8.0.0; PSR-4 `HaveAPI\\` maps to `src/`.
  [Separate source tag](https://github.com/vpsfreecz/haveapi-client-php/tree/v0.31.0)
  peels to `eafc2a9b77990dd5c927f0d412d14801261223cc`, matching Packagist.
  Packagist supplies no distribution checksum. SHA256 of the observed
  [GitHub zipball](https://api.github.com/repos/vpsfreecz/haveapi-client-php/zipball/eafc2a9b77990dd5c927f0d412d14801261223cc)
  was `0360e5eed8b8a09dbaec1fe729e3555c52a3ef75c54aeaa4693a24331c8a0b72`;
  this is an observed archive digest, not a registry integrity assertion.

## Published generated TypeScript SDK

Package [`vpsadmin-typescript-client@0.1.1`](https://registry.npmjs.org/vpsadmin-typescript-client/0.1.1)
is npm `latest` at observation time. Repository:
[`vpsfreecz/vpsadmin-typescript-client`](https://github.com/vpsfreecz/vpsadmin-typescript-client).
Tag [`v0.1.1`](https://github.com/vpsfreecz/vpsadmin-typescript-client/tree/v0.1.1)
and [npm provenance](https://registry.npmjs.org/-/npm/v1/attestations/vpsadmin-typescript-client@0.1.1)
both identify `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc` (release workflow
`40566122638`, attempt 1; status not queried).

Archive SHA256 `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`;
integrity `sha512-G7YlKCe4jX/ikmDYUT4SdZM2hf8Qvi1mQYNVetdNtHYYm4fzfLhBhcQEZYgDs7shVaAA5Bk6NCwcezqRPAWohA==`.
Published `package.json`, README, root exports, generated declarations and
provenance were inspected directly in those verified bytes.

- API **7.0**, protocol **2.0**, ESM package (`type: module`), emitted ES2022
  JavaScript plus declarations. The sole public package export is `.` with
  `import: ./dist/index.js`, `types: ./dist/index.d.ts`; no CommonJS export or
  minimum Node engine is declared. No package subpath import is supported.
- Exact peer dependency is **`haveapi-client: "0.30.2"`**. The released SDK
  records generator version **0.30.0**, generator source revision
  `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875`, and schema SHA256
  `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`.
  Do not describe this published SDK as generated by 0.31.0 or as declaring
  compatibility with generic runtime 0.31.0.
- Public root exports include `createClient`, `createVpsAdminClient` and
  `createHaveApiExecutor`. `ClientOptions` requires only `execute`, a function
  taking `RequestSpec` and returning `Promise<RequestResult<unknown>>`.
  The wrapper retains the receiver through `spec => runtime.request(spec)`.
- The SDK README uses `AsyncClient` from `haveapi-client` with the **versioned**
  base `https://api.vpsfree.cz/v7.0`, authenticates an existing token, constructs
  `createVpsAdminClient({execute: createHaveApiExecutor(runtime)})`, then calls
  `api.vps.index({params: {limit: 50}})` and iterates `page.data`.
  This is inspected published usage, not a newly executed consumer check.

The [released generator configuration guide](https://github.com/vpsfreecz/haveapi/blob/c9124da141adc258fbbaf67d4ec19ee3f8580849/clients/typescript/docs/documentation.md)
explicitly uses **runtime 0.30.2** for generated documentation examples, matching
the SDK peer. That differs from generic 0.31.0 client adoption and is not by
itself an incompatible server upgrade. Architect0 was informed of both facts.
The guide documents the following minimal profile, without requiring a saved
snapshot or SDK wrapper-specific factory option:

```ruby
api.documentation_clients('7.0',
  typescript: { package_name: 'vpsadmin-typescript-client' }
)
```

Optional `package_version` accepts a concrete SemVer, not a range or tag;
omission lets the package manager select a version. `snapshot_path` is optional;
the default model comes from the full mounted declaration. Optional
`generator_version` must match the installed generator, not the published SDK's
historical generator metadata. The emitted code imports **`createClient`**,
available from this SDK's public root, and supplies an inline runtime executor.
Actual mounted-schema compatibility, emitted examples and runtime/compile
acceptance remain implementer checks after the design/execution release.

## KB distinction

Current public [English](https://kb.vpsfree.org/manuals/vps/api) and
[Czech](https://kb.vpsfree.cz/navody/vps/api) articles list JavaScript via
HaveAPI `clients/js` among generic clients and describe downloading API
documentation during setup. Existing local Package D TypeScript candidates use
this same generic package; neither establishes use of the generated SDK.
The [generic 0.31.0 README](https://github.com/vpsfreecz/haveapi/blob/c9124da141adc258fbbaf67d4ec19ee3f8580849/clients/js/README.md)
and [SDK README](https://github.com/vpsfreecz/vpsadmin-typescript-client/blob/60a1b5d1b911c610bd993d93ae2b28d1932a0ccc/README.md)
support this concise technical distinction for the lead's final writing pass:

| Interface | Package and API | Typing and result |
| --- | --- | --- |
| Generic callback JS/TS | `haveapi-client@0.31.0`; `CallbackClient`, with `Client` as its alias; discovers authorized resources/actions | Library declarations, dynamic endpoint names; callback result wrappers, `reply.isOk()` |
| Generic async JS/TS | Same package; `AsyncClient`; explicit resource/action lookup available in TS | Promises return `{value, response}`; resources materialize at runtime; a generic type argument does not generate endpoint types |
| Generated vpsAdmin TS | `vpsadmin-typescript-client@0.1.1` plus its declared `haveapi-client@0.30.2` runtime; `createClient` / SDK wrapper | Saved-schema operation/input/output types; generated calls return raw `RequestResult<T>` with `data`, `meta`, `envelope`, `httpStatus` |

The callback interface is asynchronous callback code, not a blocking/synchronous
HTTP client. JavaScript and TypeScript can use either generic interface; these
are not separate JS-only and TS-only packages. Generated SDK coverage follows
its recorded schema; server authorization and validation still apply. Do not
extend the KB's blanket runtime-discovery description to all generated clients.
No member-facing wording or KB candidate was changed by this facts package.
