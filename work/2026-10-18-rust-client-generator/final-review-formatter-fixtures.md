# Final affected review: formatter fixtures

No findings. No Blocking, Important or Advisory issue was established in the
committed five-file correction or selected package-verification operation.
Fresh complete HaveAPI Rust CI and corrected package reproduction remain
required; this review is not evidence that either has passed.

2026-10-21, retained independent `reviewer0`, thread
`01a1508b-81fd-7ab2-b787-a7adb733a710`, model `gpt-6.1-sol`, effort `xhigh`,
saved access `read_only`. Live same-session roster confirms review purpose,
ready state, identity and settings. No override, fallback, source authorship or
subreviewer. `dev-session current` prints `2026-10-18-rust-client-generator`;
both environment identity markers are absent, matching the trusted binding.

Applied mandatory-change-review and all four lane references. This bounded
fixture/documentation correction is Medium risk; prior High-risk production
source reviews remain intact. Read the complete
[packet](review-packet-formatter-fixtures.md), design Clarification 7, applicable
workspace/repository guidance, actual source/diffs, failure evidence, final
proof/range-diff and three hook logs. The
[previous integration review](final-review-integration-rebase.md) is preserved.

## Scope and lane conclusions

Actual HaveAPI delta
`68cc80b012b7a6b9bcdf35c008c338cbc3f4c000..e09142ad241bd63fc4c014ca3afa50ad75106103`
changes exactly `clients/rust/spec/spec_helper.rb`,
`clients/rust/spec/unit/generator_spec.rb` and three technical paragraphs in
`clients/rust/README.md`, `docs/generation.md` and `runtime/README.md`.
Client remains exactly `945af6a97717a7a6373507bbc9592d5cd53727c2`.
Both application worktrees/indexes were clean at inspection.

**General:** `spec/spec_helper.rb:12` invokes
`ENV.fetch('RUSTFMT', 'rustfmt')` with `--version` as separate process arguments,
matching production selection. It requires successful exit status and nonempty
stripped stdout. A missing/failing tool fails fixture setup; no skip, fixed
fallback or shell command interpolation is introduced. The per-example cached
configuration is reused for repeated generation/check assertions.

At `spec/unit/generator_spec.rb:69`, deliberate mismatch still exercises the
unchanged production guard, both before output creation and after valid
generation. The latter compares every file's bytes and mtime, including the
ownership marker. Actual formatter generation remains in the determinism and
ownership tests. Small real executable fixtures cover an override path with
spaces and a failing probe that prints plausible version text. They do not
mock away successful formatting or weaken the mismatch contract.

**Architecture/repetition:** the shared fixture helper owns temporary config;
production generator/runtime ownership is unchanged. The existing `RUSTFMT`
extension point selects the saved client's formatter without a second shell,
formatter registry or production compatibility path. The unchanged generic
integration runner remains scoped to current PATH with `RUSTFMT` unset; the
saved-client override must not be inherited by that separate operation.

**Scope/proportionality:** the correction addresses demonstrated failures:
the retained CI log reports 26 examples/four version-guard failures, and the
old package log reports the same guard failure. No new pin, client output
configuration, formatter downgrade, generated expectation or API behavior is
introduced. The three paragraphs now distinguish temporary fixtures using
current HaveAPI tools from saved clients retaining their recorded formatter.
The displayed 1.9.0 config is explicitly an example.

**Risk/compatibility:** production `generator.rb:27` still checks successful
status and exact configured version before rendering/replacing output.
Authentication, protocol, atomic ownership replacement, runtime behavior and
public interfaces are unchanged. No security or persisted-state boundary is
expanded. Retaining the client's existing formatter/config preserves its
reproducibility contract rather than assuming output equality across versions.

## Package operation and evidence reuse

Read the exact
[operation](artifacts/integration-formatter-acceptance/operations.json), formatter
selection/setup receipts and unchanged `verify-generator-package.rb`.
The operation clears inherited bundle/Ruby/gem/formatter variables before
entering current HaveAPI `.#client-rust`, records tool versions and both
repositories' lock/config hashes, then sets `RUSTFMT` only for the saved API 7.0
package probe. Its rooted formatter resolves to
`/nix/store/9a9y1zij83al5wqvdhx7lrs9b8cqv688-rustfmt-1.98.1/bin/rustfmt`;
the retained setup receipt records successful `rustfmt 1.9.0` output.
This keeps current HaveAPI Ruby 3.4.11 while using the unchanged client's
`fe13242281a...` formatter instead of HaveAPI's newer PATH formatter.

The helper checks exact source heads and clean inputs, builds/extracts the
current gem, compares each packaged file to current source, verifies loaded
generator logic comes from the extraction, and compares the entire ownership
manifest plus all generated file bytes. It also performs read-only `--check`
and rechecks heads/status. The child inherits the explicit formatter selection;
production version validation still applies. Operation heads bind final
HaveAPI `e09142ad...` and client `945af6a...`.

Independent Git/archive reconstruction verifies all 12 listed production/build
input objects against `68cc80b...`: lib, templates, runtime source/manifest/lock,
Ruby Gemfile/lock, integration source, flake/lock, server source and Ruby client
library are equal. Recomputed digests remain:

- Generator: `b2f1408d9a53eda4bdf33054f4293e5e1ae712d69c66863e6c0ee71902bcfc13`.
- Runtime: `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`.
- Ruby lock: `7ab15ed0bf0ded01fbb03f2f8e6b4ad73ef2806b1ee9199acea8a5269080b2f1`.

The retained client CI receipt identifies successful run `39600821857` at exact
unchanged client `945af6a...`; it remains evidence for that client's own pinned
inputs and recorded compatible generator source `68cc80b...`. It is not a pass
of the corrected HaveAPI tests or current packaged documentation. Client
provenance need not change for this spec/docs-only correction.

The exact compatible source is locally preserved at
`refs/heads/2026-10-18-rust-client-generator-reviewed-68cc`, independently
confirmed to resolve to `68cc80b...`. **Publish and verify its planned remote
backup before rewriting the source feature ref**, so the unchanged client's
recorded source remains obtainable. Remote preservation is a pending lead-owned
precondition, not something this read-only review performed or certified.

The new gem includes changed README/generation documentation. Its archive bytes
and complete packaged-file inventory cannot be reused from the old package;
the corrected operation must build/extract the current payload as planned.

## Complete histories, migrations and repeated streams

Independently inspected actual complete feature series/messages and final
base-to-head inventory, reconstructed the range-diff and stable patch IDs,
and compared final tree with corrected pre-fold `fe3902d...`. Both trees are
`408531478de497f59399dc04ae0cc50f73f86928`.

HaveAPI retains exactly three logical commits above
`7835acafdda19779815a0f1ba905d78e0085456d`:

1. `62d7b3c0d71a761df1e7bce8fa8b81f0df1e1fdb`: runtime.
2. `5cad449cae7239df4d0a42112c8bdc3ab4c71326`: generator/tooling/fixtures/docs.
3. `e09142ad241bd63fc4c014ca3afa50ad75106103`: integration fixtures.

Runtime and integration patches map with `=`; only the generator patch contains
the five approved correction paths. The registered initial base
`c14e7d3158b91c134c2817b489cd29772fc09f82` remains an ancestor, with the same
22 upstream baseline commits followed by these three feature commits. The
prior upstream-preservation review remains applicable because no other path
changed. Actual final inventory agrees with the supplied proof.

Client's complete series above neutral empty root
`b67a3ba5eef89b2bd6533050aa8769aaa0574114` is unchanged:
`3353620fcd796976563be444d8241f4d867b1398` package/schema/tests,
`38750a527961b817a8e51e8638abc4b8305b5a54` generated source,
`f5f28cbb4e4db51b21e0c0ae8c7784f2e289fd5a` user README,
`945af6a97717a7a6373507bbc9592d5cd53727c2` Actions publication capability.

**Obsolete-history conclusion:** neither complete final series retains an
abandoned approach, separate corrective fixup, transitional shim or superseded
formatter mechanism. The bounded correction is folded into the owning
generator commit. The retained exact source ref serves the current client and
does not add obsolete commits to the new feature series.

**Migration conclusion: no migrations.** Neither complete feature introduces
a database/persisted-format migration or transitional schema. No intermediate
migration was merged, released, deployed or externally consumed. Existing
generated migration-action bindings remain ordinary API methods.

**Repeated-update conclusion:** no repeated dependency/input pin, lockfile,
schema, generated-output or provenance stream remains in either final series.
This correction changes none of those inputs. There is no redundant refresh
commit or new release/state boundary requiring one.

## Residual verification and disposition

The packet/proof records eight focused generator examples passing in 1.97s,
two-file RuboCop and syntax/whitespace passes under current tools. All three
final mandatory hook logs pass. These quick results do not establish full
current-toolchain acceptance. The old failed Rust CI/package records remain
failures; later runtime/lint/server CI steps were skipped.

After this review, require fresh exact-head `e09142ad...` Rust CI including all
unit/style, runtime formatting/default/blocking/Clippy, server dependencies and
generic root/mounted acceptance stages. Require the corrected current-Ruby,
client-formatter extracted-gem/API 7.0 reproduction. Unexpected output/digest
differences require diagnosis, not changing expected generated files.
Other retained passes remain scoped to their exact inputs as previously
reviewed; no whole old HaveAPI environment/matrix reuse is claimed.

All four affected lanes and complete history conclusions are complete for
HaveAPI `e09142ad...` and unchanged client `945af6a...`, with no findings.
The lead owns remote source preservation, fresh verification and the user's
authorized default merges. The user explicitly holds releases; no tag,
release dispatch, registry, credential or secret action is included.

Only this report was written. No application/source, Git or session-state
mutation, test/build, server, CI request, registry or lifecycle action occurred.
The session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/>
