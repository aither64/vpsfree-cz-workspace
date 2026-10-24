# Final affected-lane review: DELETE and fixture corrections

No new findings. No Blocking, Important or Advisory issue was established in the
assigned correction. Corrected compilation and acceptance remain required;
this review is not evidence that those checks passed.

Reviewed on 2026-10-19 by retained independent `reviewer0`, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, `gpt-6.1-sol`, effort `xhigh`, saved
access `read_only`. Rechecked the live roster: identity, review purpose, settings
and ready state match. No override, fallback, source authorship or subreviewer.
`dev-session current` prints `2026-10-18-rust-client-generator` from the bound
tracking directory; both identity environment variables are absent, consistent
with the trusted workspace/thread binding.

Applied mandatory-change-review and all four lane references: general,
architecture/repetition, scope/proportionality, risk/compatibility. Risk remains
High because the correction changes a shared protocol contract. Read the full
[packet](review-packet-delete.md), design Clarification 5, consolidation records,
range-diffs, repository guidance, relevant source/tests and aligned docs.
[Original review and history addendum](final-review.md) remain unchanged.

## Scope and evidence

The source review covers the complete post-review deltas:

- HaveAPI `874e8f2fd8c94a4bc34008936e13b856b82cdd2b` to
  `e9173e20a38de4e4e71bd5f2d4d79967950ca900`: 14 files, 516 insertions and
  54 deletions. Only `runtime/src/runtime/types.rs` changes production Rust;
  the rest is tests, docs, fixture support and the runtime target ignore entry.
- Client `58acdd6f95c6e03f57edeb3a533a9563649590a4` to
  `1a818c424259713147d9ac6970b7247c744422df`: five files, 15 insertions and
  12 deletions. README, provenance/ownership, copied classifier and the
  handwritten real-vpsAdmin assertion change.

Independent read-only Git/Python inspection verified:

- The generator source digest is unchanged:
  `b2f1408d9a53eda4bdf33054f4293e5e1ae712d69c66863e6c0ee71902bcfc13`.
- The final runtime digest is
  `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`;
  client provenance selects exact HaveAPI `e9173e20...`, and all copied runtime
  files match that committed source byte for byte.
- Every generated ownership-file hash matches. Of 686 retained Rust files,
  685 are unchanged; the sole changed file is `runtime/types.rs`.
- Saved schema, inventory, Cargo.lock, flake.lock and generator.toml are
  unchanged. Generated action/model source and API 7.0 surface are unchanged.
- Both application worktrees/indexes are clean. No source, Git, session-state,
  build, server or live-request mutation was performed by this reviewer.

## Lane conclusions

General: the classifier at HaveAPI
`clients/rust/runtime/src/runtime/types.rs:74` now selects only GET for query
encoding. The existing common `prepare` path supplies DELETE's JSON body,
Content-Type and namespaces while preserving the DELETE method. This matches
the actual baseline server parser at `servers/ruby/lib/haveapi/server.rb:721`
and the Go client's GET-only query selection in
`clients/go/template/action.go.erb:435`.

Runtime preparation regressions cover DELETE/POST/PUT/PATCH input and metadata,
omission/null/falsy values, nested Custom, unnamespaced objects, named lists,
empty `{}`, Content-Type and absence of query input. HTTP tests assert actual
DELETE bytes and the unchanged GET query control in both transports. Existing
nested-query rejection now exercises GET. The real generated-server fixture
asserts exact DELETE input and both metadata channels at
`clients/rust/spec/integration/rust/real_server.rs:53`; it does not accept the
old empty received input as success. The same case source runs async/blocking
at both mounts through the existing runner.

The fixture corrections are supported by the actual DSL and captured contract:
separate typed responses avoid the invalid mixed Rust array; `EchoCustom`
avoids an inherited constant collision; the required string case uses a valid
nonempty string while the optional fixture retains an empty string assertion.
The quick fixture-action spec inspects actual Params validation. Static action
names in `expect` diagnostics leave the runtime's redacted error formatting in
place. The actual client's update test checks success, then uses Show to verify
stored info and preserved hostname, matching the named-empty Update schema.

Architecture/repetition: HaveAPI remains the runtime owner and the actual
client/fixture crates remain consumers. One common classifier/preparation path
governs both transports; no second DELETE encoder or consumer-specific exception
was introduced. Runtime byte copying and consumer provenance are consistent.
The small database-directory helper isolates an actual fixture constraint and
does not introduce a new lifecycle or database abstraction. No finding.

Scope/proportionality: the correction implements design Clarification 5 using
the existing JSON encoder. It adds no method, retry, query fallback,
compatibility mode, API schema type or server change. Short private database
state and early EOF diagnostics address demonstrated fixture failures without
expanding deadlines or broadening accepted targets. Regression coverage is
proportional to the wire behavior that failed. No finding.

Risk/compatibility: body parsing matches the existing server contract; the
unchanged validation path still rejects invalid input and unsupported layouts.
Authentication, redaction, URL construction, retry/redirect policy, deadlines
and response handling are unchanged. There is no automatic replay to discover
DELETE encoding. Existing generated clients receive the fix only after
regeneration; the actual consumer was regenerated without changing its schema
or models. No released predecessor client requires the discarded query behavior.

The fixture state helper at
`clients/rust/spec/integration/support/vpsadmin_database.rb:6` uses a unique short
directory under `/tmp`; Ruby creates it privately, and the caller explicitly
sets mode 0700. The existing explicit TestDb instance, DATABASE_URL rejection,
loopback target checks and owned cleanup remain. EOF at
`clients/rust/spec/integration/run_vpsadmin.rb:38` fails immediately rather than
being mislabeled as a readiness timeout. Diagnostic logs retain their private
artifact location. No new security or data-safety finding.

The owning runtime/generation/integration guides and client README now
consistently distinguish GET query input from DELETE/POST/PUT/PATCH JSON body
input, with null/Custom/list limitations stated for the correct methods.
No stale GET/DELETE-query statement remains in those current owning docs.

## Final complete histories and migration provenance

Independently assessed the entire base-to-head series and final diff inventory
for both repositories, together with the prior source review and all changes
since its certified heads. The gate is not limited to the latest commit.

| Repository | Final complete feature series |
| --- | --- |
| HaveAPI, base `c14e7d3158b91c134c2817b489cd29772fc09f82` | `9818ebc19947322025d6ac552b0d7dd6b8e05ffb` embedded runtime; `573bc23f570e0dfe6b542f9d6592fa2d0b63976d` generator/tooling/docs; `e9173e20a38de4e4e71bd5f2d4d79967950ca900` integration fixtures |
| vpsadmin-rust-client, neutral empty root `b67a3ba5eef89b2bd6533050aa8769aaa0574114` | `cee40a458aa06e3186cbac27b22681b7080fc0ed` handwritten package/schema/docs; `1a818c424259713147d9ac6970b7247c744422df` generated source/runtime |

HaveAPI has exactly three feature commits and a 60-file final diff. Its final
tree `25902e7d68387f9fb033b2f7b90e0a2c7cbe2aed` independently compares equal
to corrected pre-consolidation `165000c05c675edf8d04c53ddb8abde0ed8285ae`.
The packet's range-diffs use the later intermediate `2ac6da81...` as their
comparison; this review also inspected the actual complete delta from the last
independently certified `874e8f2...`, including the intervening fixture fixes.
The client has exactly two feature commits after its empty root, with final
tree `0262269d61ac39a4dde396c22704dd2ab19fa638`. Its actual range-diff from
the previously certified `58acdd6...` agrees with the five-file delta above.

**History conclusion:** no obsolete unmerged approach, compatibility shim,
separate fixup or superseded encoding remains in either final series. Runtime
wire behavior/tests stay in the runtime commit; generation docs stay with the
generator; disposable fixture corrections stay with integration. Handwritten
client material and generated output remain separated. The corrected behavior
is introduced directly, and the logical split is sound.

**Migration conclusion: no migrations.** Neither complete branch introduces a
database or persisted-format migration. Existing generated API migration-action
bindings remain ordinary methods. There is no transitional migration lineage
or intermediate schema to preserve. Recorded provenance states that no feature
revision was merged, released, deployed, published or externally consumed;
the inspected corrections require no server deployment or migration ordering.

**Repeated-update conclusion:** no repeated dependency/channel/input pin,
lockfile, schema-capture or generated-artifact update stream remains in either
final series. Runtime/fixture/documentation corrections and the client
provenance/runtime refresh are folded into their owning original logical
commits. Locks and saved snapshot are unchanged; no supported consumer, release
or state boundary requires an intermediate update commit.

## Remaining verification and disposition

The packet records final quick checks passing: runtime formatting/whitespace;
19 fixture examples, syntax/lint and Rustfmt; actual client regeneration/check,
provenance and formatting; and required hooks. These reported checks do not
establish corrected Rust compilation or server acceptance. Historical passes
with the old DELETE encoding are not proof of the corrected behavior.

After this review, follow the
[corrected verification plan](verification-plan-delete.md) against these exact
heads: runtime default/blocking/Clippy; root and mounted generated real-server
acceptance with strict DELETE/GET assertions; actual client both modes/docs and
disposable vpsAdmin acceptance; Rust 1.95, Cargo packaging and packaged-generator
reproduction. The prior public GET smoke is supplemental and need not repeat
solely for this classifier correction. No tests or long checks ran in this
review.

All four assigned lanes and the final history/migration/repeated-update gate
are complete for HaveAPI `e9173e20...` and client `1a818c4...`, with no new
findings. Longer verification still gates readiness for use. The lead owns
evidence acceptance, state/portal updates and subsequent narrow-fix decisions.
This review grants no merge, publication, deployment or lifecycle authority.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>

Subsequent consolidated/rebased heads and retained verification-input equality
are assessed in the [final history addendum](final-review-history.md). The review
above retains its original scope and revision references.
