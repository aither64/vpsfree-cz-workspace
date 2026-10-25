# Go documentation query assertion diagnosis

Implementer2, 2026-10-22. Session current/environment identity and saved
workspace-write access were reverified. Source examined:
`ee67d27419c48d27a01c83a29114adf9a82062ba`. This records the bounded diagnosis
preceding the direct lead grant for an exact harness expectation/diagnostic fix.

## Failure and evidence limit

`go-wire-verification.log:123` reports `query: query values were not preserved`.
The retained exit/result bind the 27.4-second failed run to this exact head.
Artifact verification and compilation of all 16 actual rendered Go programs
passed. Execution reached query after object, empty, omitted, list, failure and
association cases passed. The remaining operation/auth/hostile cases were not
executed successfully in that run.

The failed query assertion printed neither parsed nor raw query. Its temporary
consumer directory and in-memory request queue are gone after ordinary runner
exit. There is no retained actual Go query capture; none is inferred from the
constructed controls below.

## Source-proven mismatch

- `clients/go/template/action.go.erb#convertInputToQueryParams` sends selected
  nullable nil as an empty query string; Boolean input calls
  `convertBoolToString`, and Integer input calls `convertInt64ToString`.
- `clients/go/template/types.go.erb:150-155` explicitly returns `"1"` for true
  and `"0"` for false. Integer zero is formatted as `"0"`.
- The query sample sets `name: nil`, `enabled: false`, `count: 0` and omits
  `unused`. The renderer uses the generated setters and selection mechanism.
- `clients/go/template/request.go.erb#DoQueryStringRequest` adds these string
  values to `url.Values` and assigns its encoded query to the request.
- The harness expected `widget[enabled]` to equal `"false"`. Its other expected
  strings, `widget[name] == ""` and `widget[count] == "0"`, already match the SDK.

The harness serves this fixture directly with WEBrick and captures
`request.query`; Rack parsing is not involved in this capture path.

## Listener-free parser and actual-verifier reproduction

Using the existing dedicated documentation bundle, an in-memory
`WEBrick::HTTPRequest` parsed this constructed template-established request query:

```text
widget%5Bcount%5D=0&widget%5Benabled%5D=0&widget%5Bname%5D=
```

Calling the actual harness `serve` captured:

```json
{"widget[count]":"0","widget[enabled]":"0","widget[name]":""}
```

The actual private `verify` rejected the old `"false"` expectation with the exact
existing error. The same captured request passed with only the expected enabled
string corrected to `"0"`. The probe exited 0, started no HTTP server/listener,
generated no SDK, invoked no compiler and installed nothing. This demonstrates
fixture-parser/assertion behavior, not execution of a Go request.

## Remaining existing verifier seams

| Remaining cases | Source assessment and constructed control |
| --- | --- |
| `operation` | The generated blocking/no-output response explicitly decodes global metadata. Fixture output supplies action-state id 55; the generated helper uses the saved show route. Actual `serve` and `verify` accepted constructed operation and `/mounted/v7/action_states/55` requests. |
| `basic_call`, `token_call`, `oauth2_call` | Existing setters configure Basic auth and the advertised token/OAuth headers without an extra login request. Their action path/body match the already passed object case. Actual WEBrick parsing, `serve` and `verify` accepted constructed fixture headers and exact expected bodies. |
| `hostile` | Same action and metadata envelope; strict comparison uses JSON-decoded strings. Actual WEBrick parsing, `serve` and `verify` accepted the constructed quoted/backslash/newline/Unicode body. |

No further proven expectation mismatch or product-contract need was found in
these scoped seams. These controls do not claim actual Go execution of the
remaining cases, provider execution or a retained raw wire capture.

## Accepted narrow remedy

Change only the expected false query string to `"0"`; preserve strict complete
query-hash equality and the nullable-empty/integer-zero/omission expectations.
Extend the existing pure checker through real `HTTPRequest -> serve -> verify`
with an exact positive and wrong false/count/null, missing and extra-key negatives.

For future failures, capture WEBrick's existing request-owned `query_string` and
print expected/actual parsed query plus raw query only at this controlled fixture's
query assertion. Do not log auth headers, bodies or tokens; add no product logger,
normalization, subset comparison or new wire behavior. The fixed query sample
contains no credentials. Final source/check/yield evidence is in
[the correction receipt](package2-go-query-fix-receipt.md).

No application or Git mutation occurred during diagnosis. Subsequent granted
changes remain confined to the harness and its existing pure checker. Prior
artifacts/logs, product inputs and source history are retained. Full Go execution
requires the hooked commit/fold and affected final review before an authorized run.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
