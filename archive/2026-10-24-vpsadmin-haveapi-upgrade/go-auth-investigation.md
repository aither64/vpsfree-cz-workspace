# Go token-auth documentation rejection — 2026-10-28

HaveAPI 0.31.1 rejects a compatible token-auth example because its saved
description contains the String `"_auth_token"` while request-time help contains
the Symbol `:_auth_token`. The Go renderer compares these Ruby values directly.
The generated vpsAdmin Go SDK supports this token transport. The smallest correct
remediation belongs to the upstream Go documentation adapter, not vpsAdmin's
profile or the generated SDK.

Investigation only: no application, HaveAPI, SDK, configuration, ref, release,
KB or deployment change. Upstream implementation remains user-owned elsewhere.
Session identity was confirmed with `dev-session current`; both environment
markers were absent and the trusted thread binding matched. The same-session
roster confirmed retained architect0/implementer0 settings and access.

## Observed failure and expected result

Implementer0's [consumer reproduction](go-auth-investigation/consumer-reproduction.md)
used one anonymous English GET of the running API7 help page, with strict CA
verification: HTTP200, curl0, TLS verification0. Its 2,811,894-byte body has
SHA256 `591952089773748c2c2e891f662eaf275c4ecb1349079cf1ff8eb8382fc5eaa5`,
identical to the existing E4 body digest.

The `auth-token-go` panel shows:

> This authentication method does not match the configured Go SDK.

It should emit `api.SetExistingTokenAuth(os.Getenv("HAVEAPI_TOKEN"))`, as the
renderer already does for a compatible token descriptor. The public HTML lists
header `X-HaveAPI-Auth-Token` and query parameter `_auth_token`. Basic and OAuth2
Go panels emit code. Of 17 Go action panels, 16 emit code; the separate VPS-index
response-field limitation is outside this investigation.

## Exact source path

All HaveAPI references below use released tag `v0.31.1`, source
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`.

1. `servers/ruby/lib/haveapi/authentication/token/config.rb:53–69`:
   `Config.http_header` defaults to String `"X-HaveAPI-Auth-Token"`;
   `Config.query_parameter` defaults to Symbol `:_auth_token`.
   `authentication/token/provider.rb:184–189`, `Provider#describe`, retains them.
2. `servers/ruby/lib/haveapi/authentication/chain.rb:51–71` localizes the
   descriptor. `i18n.rb:108–120`, `HaveAPI.localize`, preserves ordinary Symbols.
   `server.rb:640–645` builds HTML help directly from `describe_version`;
   `server.rb:254–263` supplies that help to `ClientExample::Context`.
   `documentation_context.rb:63–73` preserves Symbol values in its detached copy.
3. The automatic saved profile takes a different path:
   `servers/ruby/lib/haveapi/documentation_clients.rb:67–81`, `Profiles#finalize`,
   calls `StructuralSchema.copy`. In `documentation_schema.rb:9–16`,
   `JSON.parse(JSON.generate(description))` converts the Symbol value to String.
4. `clients/go/lib/haveapi/go_client/documentation.rb:18–31` stores its copy.
   `Documentation#copy:483–496` converts Hash keys to Symbols, but preserves
   String and Symbol **values**.
5. `Documentation#render_auth:405–428` selects the visible and saved token
   descriptors. At lines414–415 it requires both header and query values to
   compare equal, otherwise returning the observed limitation.

The values implied by this inspected source path are:

| Field | Saved automatic profile | Live help | Strict comparison |
| --- | --- | --- | --- |
| `http_header` | String `"X-HaveAPI-Auth-Token"` | String `"X-HaveAPI-Auth-Token"` | equal |
| `query_parameter` | String `"_auth_token"` | Symbol `:_auth_token` | unequal: rejection |

These Ruby types are established by the source path, **not live Ruby object
introspection**. Public HTML confirms only the transport names and actual
limitation. No second request or executable reproduction was run by architect0.

## Consumer and SDK contract

Reviewed vpsAdmin `9697bf28c3171d4ee3e0980160be60764ae2c4aa`,
`api/lib/vpsadmin/api.rb:46–55`, configures API7 with only
`go: { import_path: 'github.com/vpsfreecz/vpsadmin-go-client/client' }`.
Its authentication chain at lines348–358 uses
`Token.with_config(Authentication::TokenConfig)`. That subclass does not override
the header or query parameter defaults. There is no stale saved-description
file selected by this consumer.

The retained published module is
`v0.0.0-20260604065514-1d9240f3d27b`, source
`1d9240f3d27b5831baf3694baab5fe06294875d8`; the
[existing module receipt](package-b/b3/sdk-run-1/go-module.json) records its sum
`h1:Wrmp6NHg7JJV41izyS1om3ou6udmPWi3OkbXpW1ELyU=`.
In `client/auth_token.go:29–37`, `TokenAuth.Authenticate` sends either the exact
header or query parameter above. `Client.SetExistingTokenAuth:170–176` selects
header mode. `Client.SetTokenAuthMode:179–182` supports the alternate query mode;
`Client.SetNewTokenAuth:51` also exists. `README.md:39–57` documents token support.
The cached module's auth source byte-matches that Git revision (SHA256
`e2dad16d12455b098a76a98e25c994d463d1a95741ff03ebbc5e74dcb8380a7e`).
The newer retained local ref `73f164dd5eeebfc494705ae27981d30872fa88c3`
changes only README; its auth implementation is identical. No fresh claim about
registry `latest` resolution is made.

The server never downloads or introspects the Go module. Its guard compares
saved schema against live help, not actual SDK metadata. Changing the module
version selector therefore cannot fix this mismatch. A JSON `description_path`
also retains the string-vs-symbol boundary. Changing vpsAdmin's auth
configuration merely to influence documentation is unnecessary and is not the
recommended remedy; no configuration workaround was tested or applied.

## Installed-source binding

E4's [packaged identities](devcluster/e4-runtime/packaged-identities.json) bind
the actual server package `rky0n9ar47p1l4blp2l0qdcla9391d42-ruby3.4-haveapi-0.31.1`
and Go generator `zi93sfpg1xx3hc3989hjdy9f8hi6fca0-ruby3.4-haveapi-go-client-0.31.1`.
Read-only byte comparison confirmed the installed Go `documentation.rb` equals
the release source, SHA256
`9fc0cb67a8fec31ede747a02e1887e2e86d590410a139e4d5a3a9c42e05afbf2`.
Installed server `documentation_clients.rb`, `documentation_schema.rb`,
`documentation_context.rb`, `authentication/token/config.rb` and
`authentication/token/provider.rb` also equal their release-tag source.

## Proposed upstream remedy and focused regression

Normalize supported String/Symbol query-parameter names at the Go adapter's
comparison boundary, preserving actual header/query mismatch and missing-method
rejections. Keep absent/invalid values distinct from valid names; avoid broad
untyped coercion, full-tree normalization or caches. This changes documentation
compatibility handling only; no SDK regeneration, wire protocol or data migration
is needed for this finding.

Extend existing `clients/go/spec/unit/documentation_spec.rb` auth coverage with
a saved JSON string and live Symbol for the same parameter, including the reverse
representation. Both must emit existing-token code; changed header/query names
and a missing advertised provider must still limit. Add one small mounted
automatic-profile case using the real default token provider to cover the JSON
boundary. The existing fixture uses String `'token'` on both sides
(`clients/go/spec/support/documentation_fixture.rb:14`), and the auth example at
`clients/go/spec/unit/documentation_spec.rb:161–170` misses this representation
difference. No tests or fixes were executed here.

After an independently reviewed upstream release is adopted, one actual token
documentation panel check can confirm consumer closure. No new SDK compilation
campaign or full browser suite is justified by this source-only diagnosis.
