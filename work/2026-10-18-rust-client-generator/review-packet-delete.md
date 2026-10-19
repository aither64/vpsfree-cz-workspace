# Final review follow-up: DELETE JSON and fixture correction

All intended correction changes and the regenerated client are committed; quick
checks pass and both worktrees/indexes are clean. No long check is active.
This packet is ready for assignment to the retained independent reviewer0,
gpt-6.1-sol/xhigh/read_only, without overrides or nested reviewers.

Preserve [original review and history addendum](final-review.md). Risk remains
High because a shared protocol contract changed. Apply all four lanes to the
post-review delta: general, architecture/repetition, scope/proportionality,
risk/compatibility. Review the final full branch histories/migration provenance
as well. Do not repeat unrelated source review or run builds/server tests.

## Outcome and bounded correction

The user authorized implementation of a HaveAPI Rust generator and the actual
vpsadmin-rust-client targeting the public saved API7.0 description. Ruby/ERB,
embedded runtime, async default and optional blocking are locked. API version
alone defines the target; no application-release compatibility dimension.

Post-review real generic-server acceptance proved DELETE lost input in both
transports: runtime sent query, server returned received:{} while GET received
its expected fields. Server.rb721-739 and Go action.go.erb435-475 prove only GET
uses query among supported action methods. Design [Clarification5](design.md)
controls the correction: Method::query selects Get only; DELETE uses the existing
shared JSON body encoder with POST/PUT/PATCH. Preserve method, namespaces,
Content-Type, omitted/null/falsy/Custom/named-list inputs and metadata. No new
method, API type/schema format, retry/fallback/compatibility mode or server change.

Owning provider is HaveAPI runtime under clients/rust/runtime/src/runtime;
generation copies it byte-for-byte into the actual client. Both transports use
one common prepare/decode path. Runtime fixes require regenerating consumers;
there is no separately published runtime crate. Saved API7 snapshot, generator
Ruby code, dependencies/locks/toolchain and generated models/actions are unchanged.

Review runtime classifier/preparation/wire regressions, strict actual generic
DELETE input/metadata assertions with GET control, and aligned runtime/generator/
fixture/client docs. Additional directly inspected fixture corrections address
compilation (distinct typed responses, action constant naming), required string
validation, redacted action diagnostics and startup: unique0700 short /tmp DB
state avoids107byte Unix socket limit, same explicit owned TestDb/cleanup; EOF
is distinct from readiness timeout. Logs stay session-private. No arbitrary DBURL,
production mutation, timeout expansion or library server behavior change.

## Exact final ranges and source delta

Worktree prefix: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-rust-client-generator/
Tracking: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-18-rust-client-generator/

HaveAPI base c14e7d3158b91c134c2817b489cd29772fc09f82,
final head e9173e20a38de4e4e71bd5f2d4d79967950ca900. Complete3featurecommits:

1. 9818ebc19947322025d6ac552b0d7dd6b8e05ffb embedded runtime.
2. 573bc23f570e0dfe6b542f9d6592fa2d0b63976d generator/tooling/docs.
3. e9173e20a38de4e4e71bd5f2d4d79967950ca900 integration fixtures.

Tree25902e7d68387f9fb033b2f7b90e0a2c7cbe2aed equals corrected pre-fold165000c0
exactly (owner and parent independent gitdiff checks). Full branch60files8169+/2-.
Last independent history-certified head was874e8f2, not later2ac6da81.
Complete post-review delta874e8f2..e9173e20 is14files516+/54-, listed by gitdiff.
Runtime production code change is exactly classifier/comment; rest is tests/docs
and the bounded fixture startup helper/EOF correction. Inspect actual final source
and [consolidation](haveapi-delete-consolidation.md), haveapi-delete-reviewed and
haveapi-delete-remediation range-diffs. Earlier2ac intermediate corrections were
lead-inspected narrow fixes; do not assume an additional independent review.

Client neutral empty root b67a3ba5eef89b2bd6533050aa8769aaa0574114,
final head1a818c424259713147d9ac6970b7247c744422df. Complete2featurecommits:

1. cee40a458aa06e3186cbac27b22681b7080fc0ed handwritten package/schema/docs.
2. 1a818c424259713147d9ac6970b7247c744422df generated source/runtime.

Finaltree0262269d61ac39a4dde396c22704dd2ab19fa638. Compare last independently
history-certified58acdd6..final:5files15+/12- (README, provenance, ownership
manifest, runtime/types.rs and handwritten real_vpsadmin assertion). The test-only
Update fix validates its named-empty success then Show.info/hostname against the
captured schema. Compared to later tested e4f4638, final delta4files11+/9-.
685/686 generated Rust files byte-identical; sole changed Rustfile is copied
runtime/types.rs3line classifier/comment hunk, all models/actions unchanged.
API snapshot/inventory/Cargo.lock/flake.lock/config/formatter unchanged.
Runtime digest9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739;
generator sourceb2f1408d9a53eda4bdf33054f4293e5e1ae712d69c66863e6c0ee71902bcfc13;
schema70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d.

No migrations in either repository. Existing generated migration-action names are
API bindings, not DB migrations. No feature version was merged, released, deployed,
pushed or externally consumed. Histories introduce final behavior directly; all
followups/fixups/provenance refreshes folded into their original logical commits.
No repeated dependency/pin/lock/capture/generated-update stream remains. Verify
these conclusions independently against complete base-to-head series.

## Quick checks and documentation

Runtime fmt/whitespace pass; new tests authored, not yet compiled. Generator
unit26specs/lint previously passed, Ruby implementation unchanged by V1. Final
fixture quick set19examples/0failures in5.1s: isolated bundle activation, separate
serverbundle loading without sockets, readiness/path contracts and actual DSL/
Params validation; Ruby syntax/lint and Rustfmt pass. Final source logical commits
explicitly ran mandatory hooks clean without bypass; rewrite tree equality proven.

Actual client exact final regeneration+read-only check, fmt, provenance, shell and
whitespace checks pass; clean. Main-agent factual/writing passes cover runtime
README, generation.md, integration README and client README. Durable docs explain
wire semantics; temporary branch/review evidence stays in session records.

Historical old-encoding checks passed runtime both modes+Clippy, client both
modes/docs/MSRV1.95/Cargo package, extracted generator package reproduction, and
public async/blocking GET smoke. They do not prove corrected DELETE behavior.
After review fresh watchers run [corrected verification plan](verification-plan-delete.md):
updated runtime matrix, root/mounted generic tests, disposable actual vpsAdmin,
corrected client/default/blocking/MSRV/package and packaged generation. PublicGET
smoke need not repeat solely for this classifier change. No active process now.

No server deployment, release, publication, default-branch integration or session
lifecycle action is authorized by this review. Feature publication/CI follows
local verification; explicit user direction is still needed to merge named
repositories/default targets. Session remains active and open.

Return concrete severity-ordered findings with lanes/evidence, or none plus
residual gates. Explicit whole-history/migration/repeated-update conclusions
required for both final heads. Record follow-up in final-review-delete.md,
preserving original report and reviewed hashes. No code edits or long checks.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/
