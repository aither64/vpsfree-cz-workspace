# 2026-10-28-token-auth-compatibility

## Goal

here's a haveapi bug report:

```
**Title: Go token-auth documentation rejects equivalent String/Symbol query parameter names**

In HaveAPI **0.31.1**, the Go token-auth example displays:

> This authentication method does not match the configured Go SDK.

The configured Go client supports token authentication. The documentation incorrectly rejects matching transport metadata because its query parameter name has different Ruby types.

Reproduction:

1. Enable the default token provider.
2. Configure an automatic documentation profile:

   ```ruby
   api.documentation_clients(
     '7.0',
     go: {
       import_path: 'github.com/vpsfreecz/vpsadmin-go-client/client'
     }
   )
   ```

3. Open the API documentation and select Go under token authentication.

Expected: a token example containing:

```go
api.SetExistingTokenAuth(os.Getenv("HAVEAPI_TOKEN"))
```

Actual: the compatibility warning above. Basic and OAuth2 examples render normally.

The source trace identifies this sequence:

- [`Token::Config#query_parameter`](https://github.com/vpsfreecz/haveapi/blob/v0.31.1/servers/ruby/lib/haveapi/authentication/token/config.rb#L64) defaults to the Symbol `:_auth_token`.
- The automatic profile’s [`StructuralSchema.copy`](https://github.com/vpsfreecz/haveapi/blob/v0.31.1/servers/ruby/lib/haveapi/documentation_schema.rb#L9) performs a JSON round trip, converting that value to the String `"_auth_token"`.
- The Go adapter normalizes hash keys but preserves scalar value types.
- [`Documentation#render_auth`](https://github.com/vpsfreecz/haveapi/blob/v0.31.1/clients/go/lib/haveapi/go_client/documentation.rb#L405) compares the saved and visible values using strict equality:

  ```ruby
  saved[:query_parameter]   # "_auth_token"
  visible[:query_parameter] # :_auth_token
  ```

Both identify the same wire parameter. The HTTP header also matches: `X-HaveAPI-Auth-Token`.

Suggested correction: normalize supported String/Symbol parameter names before comparison, preserving rejection of genuinely different headers/query parameters and missing providers.

Regression coverage should include:

- An automatic mounted profile passing through the real JSON-copy boundary.
- Equivalent String/Symbol names rendering token code.
- Different transport names and missing providers remaining rejected.

The public documentation response reproduced the warning. Ruby value types were traced from released source; no live token-authentication request was performed.

Investigation complete; upstream fix and regression tests remain. [Evidence and session details](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/).
```

asses the situation and implement a fix. when done, merge it into master and then backport to haveapi 0.31, making a new patch release.

## Affected repositories

## Approach

## Decisions

## Compatibility and deployment

## Documentation

## Testing plan

## Delivery scope and ownership

Fix HaveAPI only. Architect0 owns diagnosis and design.md; implementer0 owns
the bounded code/regression package and subsequent 0.31 backport/release metadata.
Lead owns acceptance, records, independent final review coordination, approved
integration and release workflow. Other implementers stay available; splitting
this small shared-file fix would create unnecessary overlap.

Acceptance: automatic mounted Go documentation traverses real structural JSON
copy and emits SetExistingTokenAuth; equivalent supported String/Symbol names
match; different transport names and missing providers remain rejected. No
persistent state, protocol, API or generated SDK change is intended. No runtime
deployment or downstream pin updates are in scope. Existing installations can
upgrade or roll back independently.

After committed deliverable and quick checks, use independent mandatory final
review with whole-branch/migration conclusions, then relevant longer checks.
Integrate master first; cherry-pick -x onto haveapi-0.31 and prepare next unused
patch version using project release tooling. All maintained packages share the
version. Inspect release candidate/build evidence and respect protected release
approval. User explicitly requested master integration, 0.31 backport and a new
patch release in the initial task. Keep the session open.

Documentation readers are maintainers and release operators. A concise code
comment/tests and CHANGELOG entry should suffice; design, checks, exact heads and
release receipts belong in these session records.
