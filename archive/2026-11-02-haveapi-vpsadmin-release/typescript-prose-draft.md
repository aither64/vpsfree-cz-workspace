# TypeScript prose draft for main-agent writing pass

These are proposed package edits for the lead's required main-agent prose pass.
The version and coverage sentence remain conditional on final generation.

## CHANGELOG.md proposed new entry

```markdown
# 0.3.0

- Regenerate from the full vpsAdmin API fixture with HaveAPI 0.32.2 and require
  exact `haveapi-client` 0.32.0.
- Add live API and action descriptions, typed response metadata and metadata
  namespace overrides.
- Identify generated validation failures with `ClientInputError` before the
  executor is called. Transport failures keep their original identity.
```

## README.md proposed insertion before Responses, errors and timeouts

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

These calls send OPTIONS requests using the saved help routes. The server can
filter fields and actions by permission. Descriptions are extensible wire data;
the generated client does not validate them or infer authorization from them.

Each action result types its declared global metadata fields and permits unknown
extension fields. Metadata types do not validate server responses.

For an API with a different metadata namespace, pass `metaNamespace` when creating
the client. Input and output object metadata retain their saved schema keys.
The original response envelope remains available.
````

## README.md proposed error paragraph replacement

```markdown
Generated input and path checks throw `ClientInputError`, a `TypeError` subclass
with `code: 'HAVEAPI_CLIENT_INPUT_ERROR'` and `phase: 'pre-dispatch'`. This error
means the executor was never called. Executor failures pass through unchanged;
an ordinary transport `TypeError` does not prove a write was never sent.
```

## Mechanical prose edits

- README installation example moves to 0.3.0 only after conditional release gate.
- docs/development.md exact runtime pairing moves from 0.30.2 to 0.32.0.
- Keep complete fixture/all six plugins and recorded resource/action counts;
  change a coverage count only if the final export proves a real inventory change.

## Settled technical facts

HaveAPI source is exact 1ef9b204 (0.32.2), npm runtime exact 0.32.0. The released
generator adds root/action describe, typed metadata/receipts, namespace override
and ClientInputError. Description calls use OPTIONS and encoded saved help
selectors; they do not accept write params/arbitrary routes. Namespace projection
touches declared object metadata only, retaining raw envelopes and Custom data.
Final source export and generated diff are pending; no release is yet selected.
