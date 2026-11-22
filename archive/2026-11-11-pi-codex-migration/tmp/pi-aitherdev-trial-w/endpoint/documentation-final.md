docs/pi-providers.md: Immutable native endpoint composition

A downstream package can pass `piModelConfig` to `lib.mkPackage` to install
`share/dev-workspace/pi-models.json`. This optional native SDK input configures
one built-in OpenAI Responses endpoint:

```json
{"providers":{"openai":{"baseUrl":"https://gateway.example.test/v1","api":"openai-responses"}}}
```

The input must be a regular UTF-8 file of at most 64 KiB with exactly these
keys. Validation rejects duplicate, missing, null or unknown fields and trailing
input. The URL must use HTTP or HTTPS, have a host, and contain no user
information, query, fragment, control characters or interpolation. It retains
the declared path. The file cannot contain credentials, headers, OAuth,
commands, custom providers or custom model definitions.

Model IDs and capabilities come from the installed catalog and pinned native
built-in model data. An installed catalog must map the endpoint to a provider
with `native_id: openai` and `runtime_config_ref: builtin`, and a canonical
`openai` API-key account. Validation reads no credentials and does not establish
account access or model entitlement.

The supervisor loads the fixed file from its admitted `launch.AppStorePath`,
including when a retained runtime uses an earlier package than the portal's
current profile. It passes that path through trusted worker initialization.
Browser input, environment variables and member settings cannot select the
endpoint. The installed file takes precedence over private `models.json`;
the runtime does not merge them. If the package has no optional file, the worker
keeps its existing private-model behavior. An explicitly supplied worker path
that is missing or invalid is rejected before native state creation or sending,
without falling back to the public OpenAI endpoint.

The SDK's writable `models-store.json` stays in each private agent directory.
The immutable input directory receives no cache or lock writes. Credentials stay
at the configured canonical `AuthDirectory/auth.json`, with native locking and
stored-auth checks. The catalog digest continues to hash the original catalog
bytes. The admitted immutable package, launch digest and generation bind the
endpoint bytes.

This input requires no record, receipt or wire migration. It does not
automatically rebind endpoints, switch accounts or retry requests. Existing
Accepted/Unknown ownership and guarded successor recovery continue to apply.

A package can contain the endpoint configuration without `piProviderConfig`;
Pi remains unavailable in that case. Credential provisioning, route/model
acceptance, and host and application activation are separate prerequisites.
A local synthetic Responses check verifies SDK routing and isolation. It does
not prove live gateway access or installed host behavior.

docs/pi-runtime.md new paragraph:

A package can supply the optional immutable `piModelConfig` endpoint input
[described in the provider guide](pi-providers.md#immutable-native-endpoint-composition).
The supervisor selects it from the admitted application package. Each worker
keeps private model-cache, settings and history paths, with canonical auth.
The endpoint configuration alone does not supply an available provider catalog
or establish real route access. Existing runtimes are not automatically rebound
to another package or endpoint.
