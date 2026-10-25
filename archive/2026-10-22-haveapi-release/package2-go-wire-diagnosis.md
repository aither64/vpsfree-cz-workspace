# Go documentation request-envelope diagnosis

Implementer2, 2026-10-22. Session current/environment identity and saved
workspace-write access reverified. Source examined at
`3fb91caf783eaeacf49bf3647b8409d536339d71`. This records the bounded read-only
diagnosis that preceded the lead's direct harness-only correction grant.

## Actual failure and established SDK behavior

`go-final-verification.log:123` records the first executed object program's body:

```json
{"widget":{"count":0,"enabled":false,"name":null},"_meta":{}}
```

The actual rendered programs compiled successfully. Execution then failed at the
harness's whole-body equality check (`documentation_acceptance.rb:218` at this
head). The retained `.exit` is 1; `go-final-verification-result.json` binds the
196.15-second run to the exact source head. Final artifact build/verification and
both installed dynamic package runs passed before this failure. This does not
establish execution success for Go cases after `object`.

The captured `widget` preserves `name: null`, `enabled: false`, `count: 0`, and
omits `unused`. The only difference from the harness's expected body is the
empty metadata envelope. Its presence follows directly from existing source:

- `clients/go/spec/support/documentation_fixture.rb:43-52`: the shared client
  action advertises optional global `includes` metadata; the saved API metadata
  namespace is `_meta`.
- `clients/go/lib/haveapi/go_client/metadata.rb`: `has_global_input?` is true when
  the advertised global input has parameters.
- `clients/go/template/action.go.erb:183-191`: such body-request types contain a
  `Meta map[string]interface{}` field with that JSON namespace. The generated
  tag has no `omitempty` (`go_client/utils.rb#go_json_tag`).
- `action.go.erb:604-612`: `makeAllInputParams` always assigns
  `Meta: inv.makeMetaInputParams()` for these actions.
- `action.go.erb:640-659`: `makeMetaInputParams` allocates an empty nonnil map.
  With no `MetaInput`, it returns that empty map, without an `includes` value.
- `clients/go/template/request.go.erb#DoBodyRequest` marshals the complete
  request using `json.Marshal(params)`.
- The documentation adapter supplies no metadata setters for these samples;
  its optional metadata guidance is commented out.

This is the established generated SDK envelope, confirmed by the actual wire
capture. It is not evidence of a supplied-value/omission defect, nor a reason to
change the generator, renderer, SDK schema or runtime.

## All 16 existing cases assessed

| Existing cases | Assertion/metadata assessment |
| --- | --- |
| `init`, `basic`, `token`, `oauth2` | Initialization only; require no request. No body-envelope assumption. |
| `object` | Shared metadata-bearing client action; strict expected body omitted `_meta: {}`. This is the observed failure. |
| `hostile` | Same action and same expected-envelope omission; would encounter the equivalent mismatch when reached. |
| `basic_call`, `token_call`, `oauth2_call` | Same action and same sample as `object`; currently check auth only. Add the same exact body expectation while preserving auth checks. |
| `empty`, `omitted` | Separately constructed metadata-free actions. Their exact expected body remains `{"widget":{}}`; do not add `_meta`. |
| `query` | Separate metadata-free GET action; exact query assertion remains unchanged. |
| `list`, `fail`, `association` | Separate metadata-free GET actions; route/output assertions remain unchanged. |
| `operation` | Metadata is output-only. Existing route/state follow-up assertion remains unchanged. |

This assessment is bounded to existing fixture definitions and assertions; the
unreached cases have not been executed again.

## Accepted smallest correction and controls

The lead accepted exact per-case expected `_meta: {}` for the metadata-bearing
client action, with strict whole-body equality intact. Add body checks for the
three existing authenticated calls of the same action. Keep metadata-free
empty/omitted expectations unchanged. Do not strip or normalize arbitrary
metadata, accept nonempty metadata, invent payload values, or alter SDK behavior.

The focused Ruby check will call the actual harness verifier using a captured
object body and the harness's shared expected-case table. Positive controls cover
the five metadata-bearing calls and two metadata-free calls. Negative controls
must reject nonempty/null/missing metadata, extra top-level/input keys, changed
false/zero/null values, missing supplied fields, and accidental `_meta` on the
metadata-free empty/omitted cases. Final quick results and source yield belong in
[the fix receipt](package2-go-wire-fix-receipt.md).

No compiler, listener, package install/build, acceptance retry, source or Git
mutation occurred during diagnosis. Ambient files, all earlier artifacts and
verification records remain retained. Subsequent authorized source changes are
harness-only and require hooked commit/fold plus affected final review before
the next actual Go acceptance execution.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
