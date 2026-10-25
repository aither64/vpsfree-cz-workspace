# Python login rendering: affected final review

**No new Blocking, Important or Advisory findings.** The affected four-lane review
gate passes for this completed required-input correction. Actual installed wheel
and sdist login/challenge acceptance remains pending; prior successful builds or
reviews do not establish that result. This report grants no integration,
publication or lifecycle authority.

## Identity and exact range

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Independent retained `reviewer0`, purpose `review`, thread
  `01a16406-faaa-7cd0-bde3-c20802c18a72`, project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Live same-session roster confirmed ready state and saved/assigned
  `gpt-6.1-sol` / `xhigh` / `read_only`. No overrides, fallback or nested agents.
  `dev-session current` printed the bound slug; identity environment variables
  were both absent, consistent with the trusted thread binding.
- HaveAPI worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
- Complete final reviewed range: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` →
  `48543f8cd254eb0fc087931a5dc98ea730fd94af`.
- Final tree: `d240b01bc06f9a240e08f74452fc2700a795a0f1`.
- Previous affected-lane review: `ee150c8515aae399dc14e0fe9daefeb95a8bb17e`,
  tree `fed8aea303bb91eb488c4c4bbc639356a7488c21`.
- Exact final complete message remains `Version 0.30.0`, with no body; base is
  independently confirmed as the actual merge base. Tracked source/index stayed
  clean and final HEAD remained exact throughout review.

Read the mandatory-change-review skill, Shared Reviewer Instructions and all four
references. Applied general, architecture/repetition, scope/proportionality and
risk/compatibility lanes at high overall risk because emitted authentication code
selects required credential inputs. Inspected the frozen contract, packet, final
owner receipt, complete series/diff and old-to-new semantic delta. Unchanged
earlier content is supported by exact comparison to the retained prior review;
that reuse does not substitute for assessing this new auth-render contract.

## Required-input and authentication conclusions

The root cause and correction match the actual owning APIs. The server's
advertised initial token request declares required lifetime with the existing
`fixed`, `renewable_manual`, `renewable_auto` and `permanent` choices; interval is optional with its
existing server default. Python's sync and async `begin_token_login` forward
caller parameters unchanged to native validation. The runtime correctly rejects
the former omitted lifetime and needs no correction.

The shared `token_request_fields` accessor extracts the same advertised request
parameter map previously traversed by `token_login_fields`. The latter still
excludes token/lifetime/interval exactly as before, preserving every existing JS
caller and JS lifecycle selection. Python alone merges advertised required
initial fields into its previous selection. Both Python variants share this
owner and render values through the existing JSON `HAVEAPI_AUTH_*` convention.
No field/default/choice is inferred from an implementation-only catalog.

Required lifetime is therefore explicit caller input. Optional interval remains
omitted; a required interval is retained, as the focused regression demonstrates.
Optional ordinary login fields keep their prior behavior. The installed test
harness's JSON `"fixed"` is an explicit fixture choice from the advertised enum,
not a new client or server default. The fixture schema/provider and URL rules
remain unchanged.

Existing-token handling remains in its original conditional branch; that branch
does not evaluate initial-login environment mappings. Continuation input excludes
the token, and `step.submit` still uses the challenge object's owned token/nonce.
Inspected the actual sync/async `_login_step` and `_continuation_params` owners:
they retain token injection and validation. The correction adds no continuation
token environment requirement, credential printing, retry or fabricated success.
Only the authorized provider descriptor contributes field names; no additional
schema/default/source path is exposed in output.

Compatibility is limited to corrected documentation asking for inputs Python
already requires. No runtime API, URL, JS, generator, schema/default or persistent
state change is present. Corrected docs need no coordinated runtime upgrade.
Rollback restores the defective example without modifying stored tokens/state.
The guide accurately distinguishes required JSON environment inputs, omitted
optional lifecycle fields, explicit fixture choice and challenge ownership.

## Regression fidelity and scope

The supplemental native test uses unchanged real Rack OPTIONS metadata. It renders
the actual sync/async Python programs, parses their AST, finds the actual
`begin_token_login` argument and evaluates that emitted dictionary against
deterministic JSON environment values. It does not replace the mapping with an
independent expected dictionary before validation.

The real Python `parse_description`, `parse_resources` and `build_request` then
check the resulting request. Positive controls verify required lifetime, its
advertised fixed choice, exact token namespace/body, no optional interval and the
mounted origin-root destination. Removing lifetime from the recovered mapping
produces the exact native missing-field validation error. No transport/listener,
schema rewrite or substituted validator is used. Renderer checks also cover
required interval, existing-token source and continuation-token exclusion.

The new native file lives outside ordinary Ruby spec discovery. The existing
explicit Makefile target adds it alongside the native protocol checks and keeps
the existing prepared locked Python prerequisite. It installs nothing, adds no
skip/fallback and does not broaden ordinary Ruby CI discovery. This is a bounded
test seam proportional to a demonstrated installed-example failure, not a new
authentication framework or runtime capability.

## Complete history, streams and migrations

Independently reconstructed all 22 final commits/messages and the final 135-path
inventory. The seven-path delta from `ee150c85` is exactly Makefile, shared field
accessor, Python renderer, acceptance harness/guide, renderer regression and new
native regression. Direct diff confirmed no JS/Python runtime, Go/Rust, server
provider/schema/route or actual fixture change.

Independently computed stable patch IDs for every old/new position: **20 equal**;
only owning dynamic renderer commit `9b7d6670` and orchestration commit `94246292`
change. The first 13 commit hashes stay exact. Other logical purposes remain in
their reviewed order. Prefold `7792846af9f31fb841d637bb4789b45ffd8f41ee` and final
head have equal trees and identical complete binary base-to-head diffs. The
correction is folded into its owners; no obsolete approach, fixup-only commit,
transitional behavior or abandoned authentication path remains.

Repeated-stream conclusion: **no new dependency/input/generated stream**.
One cumulative JS bundle/declaration update `56ebccfe` remains after both authored
helper and URL features. Shared final version metadata/locks occur only in
`48543f8c`; npm test declarations remain the separate `593fac92` dependency update.
Highlighter pin/build/license/bundle remains one `ccf35513` stream; PyPA remains
the separate `1e810107` pin; shared CI action roles remain in the orchestration
purpose. `flake.lock` and private runtime `Cargo.lock` are unchanged. There are no
redundant intermediate pins/payload updates requiring consolidation or a consumer/
deployment exception. Released maintenance patches and both levels of `-x`
provenance remain exact within the unchanged initial range.

Migration conclusion: **no migrations**. Complete final history contains no
database/schema, persisted-format or state-conversion changes, no transitional
migrations, and no migration release/deployment/external-use lineage to reconcile.
Exact older refs/artifacts/reviews remain separate provenance rather than
justification for obsolete final history.

## Reviewer checks and remaining verification

Ran the known quick focused command in the declared tools-only root Nix shell:

```sh
cd servers/ruby
bundle exec rspec spec/client_examples/dynamic_python_spec.rb \
  test_support/dynamic_python_login_spec.rb
```

**11 examples, zero failures**, seed 59662, 1.76 seconds. This includes both actual
Rack-to-emitted-AST-to-native-builder cases. Independent full-range whitespace,
identity/tree, semantic scope, stable patch IDs, prefold equivalence, update-stream
and migration checks passed. Owner 16-example focused and assembled 79-doc/seven-
native/style/hook receipts were inspected as supporting evidence, not relabeled
reviewer-run checks.

These tests prove emitted initial input fidelity and the native validation
boundary, not complete installed authentication execution. Retry installed npm/
Python wheel and sdist rendered acceptance with exact final artifacts, including
both no-token Python branches through challenge completion and authenticated
result. Preserve separate existing-token/challenge logs and exact source/artifact
identity. Final-head CI and remaining Go/Rust documentation acceptance, including
the chosen minimum/development Rust verification, remain under the lead's plan.
Prior `ee150c85` success/failure evidence cannot certify the new candidate.

No listener, compiler, build, package/long acceptance, registry/default/tag or
lifecycle mutation was run. Only this assigned report was written. Lead owns
state reconciliation and subsequent authorized verification; session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
