# TypeScript final prose

Main-agent vpsfree-user-facing-writing and humanizer-en pass applied after the
package owner's technical facts. Use only when final generation proves these
features. Version0.3.0 remains conditional on actual code changes/fresh tags.

## CHANGELOG.md

```markdown
# 0.3.0

- Regenerate from the full vpsAdmin API fixture with HaveAPI 0.32.2 and require
  exact `haveapi-client` 0.32.0.
- Add live API and action descriptions, typed response metadata and metadata
  namespace overrides.
- Report generated input validation failures as `ClientInputError` before
  calling the executor. Preserve the identity of transport errors.
```

## README.md live descriptions

````markdown
## Live descriptions

Read the API description or an action's current input requirements through the
authenticated executor:

```ts
const description = await api.describe({ timeoutMs: 30_000 });
const action = await api.vps.update.describe({
  path: { vps_id: vpsId },
  timeoutMs: 30_000,
});
const required = action.data.input?.parameters?.['hostname']?.required;
```

These calls send OPTIONS requests to the saved help routes. The server can
filter fields and actions by permission. Descriptions can contain extension
fields. The generated client does not validate descriptions or infer
authorization from them.

Action results include types for their declared global metadata fields and
permit unknown extension fields. These types do not validate server responses.

For an API with a different metadata namespace, pass `metaNamespace` when
creating the client. Input and output object metadata retain their saved schema
keys. The original response envelope remains available.
````

## README.md errors

```markdown
Generated input and path checks throw `ClientInputError`, a `TypeError` subclass
with `code: 'HAVEAPI_CLIENT_INPUT_ERROR'` and `phase: 'pre-dispatch'`. This error
means the executor was never called. Executor failures pass through unchanged;
a transport `TypeError` does not prove that a write was never sent.
```

## Mechanical updates

Retain the exact runtime pairing in development guidance for reproducibility.
Update the installation example only after the release gate. Preserve all
fixture/plugin counts until a verified export proves a real inventory change.
