# Investigation: repeated copying in generated TypeScript examples

Source inspected read-only at HaveAPI
`4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c` (local `origin/master`). This is a
source/history investigation, not a production benchmark or a claim about a
particular hosted CI run. No tests were run during the investigation. Implementer0
independently checked history and coverage. Subsequent fix work follows
[design.md](design.md).

## Confirmed defect and cost

The defect is in the generated TypeScript adapter implemented in Ruby, not the
Ruby client and not the separate callback/async dynamic TypeScript examples.
The generated variant is enabled only by a configured TypeScript SDK profile.

Exact call path at the inspected revision:

1. `servers/ruby/lib/haveapi/views/version_page/resource_body.erb:98-107`
   loops samples and calls `documentation_panels(:example, ...)`.
2. `servers/ruby/lib/haveapi/server.rb:254-274` selects available renderers and
   derives their request context, sharing the authorized description.
3. `servers/ruby/lib/haveapi/client_example.rb:49-59` invokes the renderer;
   `client_examples/ts_generated_client.rb:10-11,22-33` requires the profile,
   derives the sample context and calls its real adapter.
4. [TypeScript adapter](https://github.com/vpsfreecz/haveapi/blob/4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c/clients/typescript/lib/haveapi/typescript_client/documentation.rb#L254)
   calls `authorized_action` once, then `compatible_action!` twice. Each calls
   `normalize(context.description)` (`:158`, `:186`). Protected examples also
   call it in `action_authentication` (`:148`) and `authentication` (`:128`).

Thus a successful public example performs **three** complete normalizations; a
successful Basic/token-protected example performs **five**. A separate auth panel
performs one. Initialization does not do this; early limitations can stop sooner.
`normalize` at `:79-85` recursively rebuilds every Hash and Array, stringifies keys
and Symbol values, and retains ordinary scalar/String values. “Copying the whole
description” therefore means reconstructing/traversing its entire container tree,
not necessarily duplicating every String byte.

For E rendered samples and D description nodes, this adds O(E × D) recursive work
and cumulative allocations. When sample count and description size grow together
with resource count, that term is quadratic. This is a source-derived complexity
conclusion, not measured production latency or an assertion that all copies stay
resident simultaneously. The legitimate mount-time private SDK copy and the
request's initial owned snapshot are separate from this repeated render work.

## Chronology

Dates below are recorded author dates. Commit order and content, rather than dates
alone, establish the sequence.

| Commit | Date | Evidence |
| --- | --- | --- |
| `8dbf66acffe5613d93b5c00e91c4b5d5935982bb` | Oct 22 | Introduces Rust documentation adapter with full-description normalization. |
| `5003ded2a47db6b1637a3fef2fdd40474ea7de06` | Oct 24, 23:10 +02 | Fixes another copying layer: `Context#with` shares unchanged owned fields. |
| `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c` | Oct 24, 23:15 +02 | Rust selects raw action/provider subtrees before normalization; adds recursive-work regression specs. Commit body explicitly identifies complete-description normalization per example. |
| `de799b595d04e880d092b3e5ef47bce2f4587130` | Oct 24, 23:17 +02 | Adds deterministic context allocation/identity and real HTML isolation regressions. |
| `b85ec364057f536940d689b09e612512ffffaf82` | Oct 24, 23:21 +02 | Adds opt-in documentation benchmark, later used as fixed performance reference. |
| `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` | Oct 25 | Adds hosted endpoint performance gate; subsequent `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` and `39e98020070fabcceca32f8fabcf0440f0d8763e` develop paired gates and representative complete Rust pages. |
| `e6d4f797fc92090fff265585196970e6b017003f` | Oct 26, 21:00 +01 | Adds generated TypeScript examples with the repeated normalization, after the Rust fix and performance tests. Adds correctness/compilation/profile tests, but no performance fixture/runner or recursive-work coverage. |

The supplied patch uses the same selected-subtree approach as the Rust fix and
adds useful collision, alias, auth, immutability and isolation checks. Its
unrelated-subtree spy is useful; an explicit small/large recursive-work assertion
will make the performance regression independently visible.

## What the tests and CI actually cover

All references in this section are `4d36efcf…:<path>:<line>`.

| Check | Actual assertion and invocation | Why TypeScript copying escapes |
| --- | --- | --- |
| Rust adapter traversal | `clients/rust/spec/unit/documentation_performance_spec.rb:20-32,43-101` grows unrelated descendants from 1 to 64; wraps every recursive normalization call; asserts equal output and equal recursive-call count for action/credentials/auth/limitations in async and blocking modes. `.github/workflows/clients-rust.yml:32-37` runs `bundle exec rspec spec/unit`. | It tests the Rust class only. Reintroducing full normalization there increases the count and fails; a different adapter is outside its scope. |
| Server context cost | `servers/ruby/spec/client_examples/context_performance_spec.rb:30-69` asserts identity for unchanged fields; sizes 8/128 with 40 derivations permit at most 32 extra allocated objects per derivation. | The TypeScript adapter copies internally; the shared input context still has the same identity. |
| Ordinary HTML ownership/isolation | `servers/ruby/spec/documentation/performance_spec.rb:7,34-43,47-77` uses the default fixture, checks shared input descriptions and admin/member/admin isolation. `:38` asserts dynamic TypeScript callback/async panels. Server workflow delegates to `_ruby-rspec.yml:78-82`, `bundle exec rspec`. | There is no generated TypeScript profile and no measurement of internal adapter copies. |
| Paired full-page performance | `servers/ruby/benchmarks/endpoints.rb:36-58` selects ordinary HTML shapes and Rust cases. `performance_compare.rb:25-29` adds complete Rust pages with 16/32 resources, 4 actions, 2 samples, 4 parameters, admin/member. | Real Rack full pages are timed for wall/CPU and allocations, but optional generated TypeScript and Go are absent. |
| Shared fixture | `servers/ruby/test_support/documentation_performance_fixture.rb:16-17,41-43` has only optional `rust:` registration. | A bigger ordinary/Rust fixture cannot exercise an unavailable generated TypeScript renderer. |
| TypeScript-specific tests | `clients/typescript/spec/unit/documentation_spec.rb:6-103` checks frozen models, output, auth and rejected contracts; compilation specs compile real snippets. Server `ts_generated_client_spec.rb:8-9,33-49` uses a spy adapter; profile/mount tests likewise isolate adapters. `Makefile:68-69` runs generator unit tests. | Correct output, compilation and frozen input do not assert bounded traversal or allocation work. There is no size-dependent performance assertion. |

TypeScript tests are not wholly missing from CI: `.github/workflows/release.yml`
includes `clients/typescript/**` at `:17,32`; its fresh build path calls `make test`
at `:95-103`, which invokes `test-typescript` and `test-documentation-generated`
(`Makefile:16-17,32-33`). This is correctness coverage, not performance coverage.

There is also a routing gap:
[`utils/performance_ci.rb:13`](https://github.com/vpsfreecz/haveapi/blob/4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c/utils/performance_ci.rb#L13)
includes `clients/ruby/` and `clients/rust/`, but omits `clients/typescript/` and
`clients/go/`. The performance workflow runs on pushes/PRs, but only measures
when this resolver reports relevance (`servers-ruby-performance.yml:83-118`);
an explicit no-work outcome can pass the aggregate (`:120-138,158-166`).
**This did not explain the initial TypeScript escape:** its introducing commit
also changed server code, docs and Makefile, so it was relevant. It still had no
generated-TypeScript workload. The filter is an additional gap for later
client-only changes. No hosted run receipts were inspected, so this establishes
configured selection behavior, not which individual run passed.

This is primarily missing workload/assertion coverage, not evidence that the
existing timing thresholds were too permissive. Making those thresholds stricter
cannot measure an adapter that the fixture never enables.

## Go answer

Go is also absent from the optional performance profiles and relevance filter.
However the same source defect is not present:
`clients/go/lib/haveapi/go_client/documentation.rb:27` copies the private model
once in initialization; `render_example:115-137` uses `visible_action:470-477`
to look up the selected live path. `render_auth:405-428` selects the provider.
Recursive `copy:483-497` is not called while rendering. Resolution scans sibling
resource/action arrays (`:36-54`), so this is not a claim of constant-time lookup
at arbitrary width. No Go production rewrite is justified by this investigation.

## Accountable explanation and prevention

The previous work protected the shared context and the Rust-specific adapter,
but did not make bounded rendering work a tested requirement for every newly
registered renderer. Generated TypeScript reintroduced the same implementation
pattern in a new class. Its addition included meaningful correctness tests, but
did not extend the performance workload or enforce the earlier traversal
invariant. That is the concrete test-design/integration gap. The history cannot
establish what an author remembered, why a review missed it, or any person's
intent.

Smallest direct repair: apply selected-subtree normalization without caching live
authorization, and add a deterministic regression that fails on the old code.
The user's expanded requirement now calls for every registered renderer/mode in
a required current-source work/allocation and complete-page contract, real
optional adapters, exact inventory accounting, code/auth/action output and user
isolation, plus routing for every client source. Historical wall/CPU comparisons
remain useful, but their fixed old baseline cannot render a new TypeScript
profile. The accepted design keeps those comparisons separate and names the new
coverage honestly; it does not claim a new all-client historical timing gate.
