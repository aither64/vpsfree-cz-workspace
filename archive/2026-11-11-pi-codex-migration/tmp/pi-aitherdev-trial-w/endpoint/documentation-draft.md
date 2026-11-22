docs/pi-providers.md: Immutable native endpoint composition

A downstream package may pass `piModelConfig` to `lib.mkPackage` to install
`share/dev-workspace/pi-models.json`. The optional native SDK input supports
one built-in OpenAI Responses endpoint:

```json
{"providers":{"openai":{"baseUrl":"https://gateway.example.test/v1","api":"openai-responses"}}}
```

The regular UTF-8 file is bounded to 64 KiB and accepts exactly these keys.
Duplicate, missing, null, unknown or trailing input refuses. The absolute HTTP
or HTTPS URL must have a host and no user information, query, fragment, controls
or interpolation. The declared path is preserved. Credentials, headers, OAuth,
commands, custom providers and custom model definitions are not accepted here.
Model IDs and capabilities still come from the installed catalog and pinned
native built-in model data. An installed catalog must map this endpoint to a
`native_id: openai`, `runtime_config_ref: builtin` provider and a canonical
`openai` API-key account. Validation reads no credential and proves no access
or model entitlement.

The supervisor loads this fixed file from its admitted `launch.AppStorePath`,
including when a retained runtime uses an earlier package than the portal's
current profile. It passes the frozen path only through trusted worker init.
Browser input, environment and member settings cannot select an endpoint.
The installed file takes precedence over a private `models.json`; they are not
merged. Missing optional package input retains the previous private-model
behavior. A supplied missing or invalid worker path refuses before native state
creation or send, without falling back to the public OpenAI endpoint.

The SDK's writable `models-store.json` remains in each private agent directory;
the immutable input directory receives no cache or lock writes. Credentials
remain at the explicitly configured canonical `AuthDirectory/auth.json` with
native locking and stored-auth checks. The catalog digest still hashes its
original catalog bytes. Endpoint bytes belong to the admitted immutable package
and its existing launch digest and generation. There is no record, receipt or
wire migration, automatic endpoint rebinding, account switch or retry. Existing
Accepted/Unknown ownership and guarded successor recovery continue to apply.

Endpoint-only packages may be prepared without `piProviderConfig`; Pi remains
unavailable. Credential provisioning, route/model acceptance and explicit host
and application activation remain separate prerequisites. A local synthetic
Responses check establishes SDK routing and isolation, not live gateway access
or installed privileged-host behavior.

docs/pi-runtime.md new paragraph:

A package may also supply the optional immutable `piModelConfig` endpoint input
[described in the provider guide](pi-providers.md#immutable-native-endpoint-composition).
The supervisor selects it from the admitted application package, while each
worker retains private model-cache/settings/history paths and canonical auth.
An endpoint alone does not install an available provider catalog or establish
real route access. No existing runtime is rebound to a different package or
endpoint automatically.

