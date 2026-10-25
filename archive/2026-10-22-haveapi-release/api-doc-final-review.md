# Expanded HaveAPI 0.30.0 independent final review

**Result: three Important findings, one Advisory; no Blocking findings.**
Resolve the Important findings, or record explicit accepted decisions, before
long verification. The original release-only review remains separate. This
report reviews the expanded committed deliverable and grants no integration or
publication approval.

## Findings

### I1 — Important — Python examples ignore existing GET encoding limits

Lanes: general; risk/compatibility. Commit `aee69b7b`.
Location: `servers/ruby/lib/haveapi/client_examples/python_client.rb:103`.

Both Python variants accept any JSON-shaped object/list after checking only its
outer shape and the list namespace. The actual Python request encoder supports
a bounded Rack query subset: Custom query leaves must be strings, complex empty
values cannot be represented, and list/object-row shapes have restrictions.
These are existing client boundaries, not capabilities to add in this change.

Minimal confirmed case: GET `/v1/widgets`, hash input namespace `widget`, one
Custom parameter `payload`, no authentication/path parameters, successful sample
`request: {payload: {enabled: false, count: 0}}, response: {}, status: true`.
Both renderers return `status: :code` and emit:

```python
response = api.resources["widget"].actions["show"].call(
    params={"payload": {"enabled": False, "count": 0}}
)
```

The async variant adds `await`. The real `build_request` for exactly that
description/input raises `ValidationError: input cannot be represented by a GET
query` before transport. Inspected owning checks at
`clients/python/src/haveapi_client/_protocol/request.py:154` and `:283`.
Thus the panel presents a successful executable sample that cannot issue the
documented request. The installed-package acceptance fixture covers POST and
does not catch this GET case.

Requested remediation: return a specific limitation for samples outside the
existing Python query subset, with sync/async regression cases and a safe GET
control. Prefer a conservative documented boundary over duplicating the entire
Python encoder in Ruby. Do not change the Python client or sample wire format.

### I2 — Important — JavaScript query guard uses the wrong HTTP-method set

Lanes: general; risk/compatibility. Commit `aee69b7b`.
Location: `servers/ruby/lib/haveapi/client_examples/js_client.rb:171`.

The guard rejects nested query values only for GET/HEAD. Both actual JavaScript
clients query-encode GET/**OPTIONS**; HEAD follows their body path. Consequently
the four JS/TS variants emit code for OPTIONS input whose values are silently
changed by the client rather than explaining the unsupported sample.

Minimal confirmed case: change I1's method to OPTIONS. `JsClient` and
`JsAsyncClient` return `status: :code`; the TypeScript variants inherit the same
method. Native checks against the committed built package returned:

```text
api.sendAsQueryParams('OPTIONS') => true
api.addParamsToQuery('https://example.test/v1/widgets', 'widget',
  {payload: {enabled: false, count: 0}})
=> https://example.test/v1/widgets?widget[payload]=%5Bobject%20Object%5D
```

The async request owner uses the same GET/OPTIONS split at
`clients/js/src/haveapi/async/request.ts:65`; the shared serializer stringifies
the object at `clients/js/src/haveapi/protocol.ts:85`. This violates the accepted
no-silent-input-loss boundary.

Requested remediation: align renderer capability checks with the actual client
method split and add nested OPTIONS plus scalar OPTIONS controls for both client
families. No transport changes or new query capability are needed.

### I3 — Important — successful examples omit required input metadata

Lanes: general; architecture/repetition; risk/compatibility.
Commits `aee69b7b` and `09f6b22c`.
Locations: `servers/ruby/lib/haveapi/client_examples/dynamic_helpers.rb:68`,
`servers/ruby/lib/haveapi/client_examples/python_client.rb:103`,
`servers/ruby/lib/haveapi/client_examples/js_client.rb:159`, and
`clients/go/lib/haveapi/go_client/documentation.rb:272`.

The example DSL has no metadata-input channel. Nevertheless dynamic renderers
and Go return executable code for a successful sample on an action requiring
global metadata. The calls send no metadata; Go prints commented setter guidance
without supplying the required field. Required metadata is therefore lost from
the prerequisites for the claimed successful program. Rust already returns a
limitation for this condition in `compatible_action!`.

Minimal confirmed case: POST with empty hash input/request and
`meta.global.input.parameters.confirm = {type: 'Boolean', required: true}`;
sample `request: {}, response: {}, status: true`. JS callback and Python sync
return `status: :code`; their sibling variants share this path. The actual
Python request builder raises `ValidationError: input parameters are not valid`
without `meta`. Server validation independently requires this field at
`servers/ruby/lib/haveapi/action.rb:659`; the existing server regression at
`servers/ruby/spec/action/runtime_spec.rb:636` demonstrates missing required
global metadata rejection.

Also reproduced with `GoDocumentationFixture.description`: replace the existing
global input metadata with required Boolean `confirm`, retain its ordinary
successful sample, and render with the real Go adapter. It returns code with only:

```go
// metadata := invocation.NewMetaInput().SelectParameters()
// metadata.SetConfirm(value) // value has type bool
```

Requested remediation: explicitly limit purported successful samples that need
metadata absent from the fixed sample contract. Check the corresponding required
global/object metadata boundaries where applicable, and cover them with focused
tests. Keep optional advertised metadata guidance; do not invent values, extend
the example DSL or make new client capabilities part of this correction. Keep
dynamic checks in their owning shared helper where the rule must remain equal.

### A1 — Advisory — Rust Float conversion can emit `Infinity_f64`

Lanes: general; risk/compatibility. Commit `1f8aac4c`.
Locations: `clients/rust/lib/haveapi/rust_client/documentation.rb:287` and `:320`.

`valid_value?` checks the original Numeric's `finite?`; `typed_literal` converts
it to f64 afterwards. An arbitrarily large Ruby Integer is finite but converts
to infinity. A Float input `amount: 10**400` was accepted by both validation and
rendering, producing:

```rust
let response = api.widget().update("1").amount(Infinity_f64).send().await?;
```

`Infinity_f64` is not a valid emitted numeric literal. This is an extreme invalid
sample boundary rather than a demonstrated normal-operation or security failure,
so severity is Advisory. The narrow correction is to validate the converted f64
and return a limitation for overflow; test ordinary finite integers/floats and
overflow in both modes. No Rust runtime/generator capability expansion is needed.

## Identity, range and workflow

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Retained independent `reviewer0`, thread
  `01a16406-faaa-7cd0-bde3-c20802c18a72`, project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Live same-session roster confirmed purpose `review`, ready state, saved and
  assigned `gpt-6.1-sol` / `xhigh` / `read_only`. No overrides, fallback or nested
  agents. `dev-session current` printed the bound slug; both identity environment
  variables were absent, consistent with the trusted thread binding.
- HaveAPI worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Reviewed full range `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` →
  `607941c035af0c7466cedb5ca6c2d36841ea34a5`, tree
  `17916258a4191edd85d5e543356aee2df7efa77e`.
- Exact final complete message is `Version 0.30.0`; base is the actual merge base.
- All four lanes applied at high overall risk: authenticated generated examples,
  literal/HTML boundaries, saved-SDK compatibility and irreversible publication.
  Read the mandatory-review skill, Shared Reviewer Instructions and all four
  lane references; used applicable workspace and repository guidance and the
  authoritative contract/acceptance/packet/design and owner receipts.

## Complete history and consolidation conclusion

Independently inventoried all 18 commits/messages and final changed-file set
(112 paths), reviewed the final source and relevant tests/docs, and compared with
the original release range using `git range-diff`. Its first six commits are
patch-equivalent to the earlier independently reviewed release tooling,
maintenance fixes, publication coverage and PyPA update. Original version
metadata remains coherent; the final changelog adds the accepted server examples.

All added source precedes final `Version 0.30.0`. File-system removal, context/
profiles, filtered panels, test dependency, Go/Rust adapters, authored callback
helper, mechanical helper output, dynamic renderers, highlighter/assets and
shared packaging/CI have distinct reviewable ownership/purposes. The offline Go
constructor has an actual acceptance-fixture consumer and preserves the URL
constructor. No obsolete unmerged design, fixup-only history, discarded shim or
transitional implementation remains. Findings above concern the final behavior,
not obsolete commits that should have been consolidated.

Independently proved the pre-consolidation `6204d0d3` and final trees equal.
The three maintenance patches have exactly equal diffs to original review commits
`c305117`, `1973057` and `62cb54e`; both original and release-branch `-x` provenance
remain. Their released compatibility boundary remains valid, even though the
new dynamic JavaScript renderer intentionally replaces the old example syntax.

Repeated-stream conclusion:

- One shared 0.30 version stream in `607941c0`; Rust/Python locks change only
  there, without registry-resolution drift.
- One Node declaration dependency stream in `593fac92`; its package/lock change
  is distinct from final version fields in the same files.
- One authored helper (`788dde10`) followed by one mechanical bundle/declaration
  generation (`29b0415a`); final bundle version literal is separate metadata.
- One highlighter dependency/build/license/bundle stream (`ee10f589`).
- Independent PyPA security pin (`1e810107`) and shared Ruby CI action pins
  (`5f0e9f96`); no redundant updates to the same role remain.
- `flake.lock` and private Rust runtime `Cargo.lock` are unchanged; Go acceptance
  lock is ignored. No intermediate pins or generated iterations require retention
  or an unsupported deployment/consumer exception.

Migration conclusion: **no migrations**. The entire range has no database schema,
migration or persisted-state conversion paths; no transitional migrations or
migration merge/release/deployment/external-use provenance are outstanding.

## Architecture, compatibility and verification limits

Request-local contexts copy/freeze data without retaining another user's help.
Optional profiles load trusted local files before mount and preserve optional
generator dependencies. Go resolves the saved canonical model; Rust reuses
Snapshot/IR/Naming and type rules. Filtered help/sample checks constrain emitted
fields; generic limitation reasons do not expose saved schema paths/defaults.
No new cross-user cache or confirmed security bypass was found.

Legacy constructor/method entrypoints remain callable; registry wrapping and
stable variant IDs are coherent. The callback canonical map has a null prototype,
canonical names win, and ambiguous aliases fail without changing direct-property
compatibility. Local highlighter grammars/license and escaping fallback are
packaged; keyboard tabs retain visible selectors and no-JS readable source.
Provider docs own supported contracts and bounded limitations; temporary rollout
and toolchain evidence remain in session records. Publication catalog/preflight/
retained-artifact recovery remains covered by the preserved baseline plus the
new guide packaging requirement. No default-branch or registry approval is implied.

Reviewer-run quick checks: three native callback lookup tests passed; local
highlighter/worker escaping and keyboard/ARIA tests passed; whole-range whitespace,
identity/tree/history/stream/migration checks passed. The four finding reproductions
used pure Ruby renderer calls, the real Python request builder and the built
JavaScript serializer. No listener, compiler, package acceptance, registry helper
or long integration suite was run. Nix supplied the declared tools. Author quick
receipts were inspected as supporting evidence, not relabeled reviewer-run tests.

After narrow corrections/decisions, focused verification must cover the changed
capability checks before the prepared full release/build/component and installed-
package/generated-SDK acceptance batch. New exact-head CI, full packaging/HTML,
Rust development and independently selected 1.95 acceptance remain outstanding.
Their toolchain/input graph is prepared in `api-doc-msrv-readiness.md`; availability
and a pure harness check do not establish compiler acceptance. Actual registry
account configuration and publication remain separate unverified operations.

Application source/Git remained read-only. Only this assigned report was written;
session and all existing artifacts remain open/preserved. Lead owns findings
reconciliation and state tracking.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
