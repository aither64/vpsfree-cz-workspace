# Development follow-ups: final independent review

**No Blocking, Important or Advisory findings.** All four assigned lanes pass
for the committed follow-up range. This is source review with focused checks;
full build, installed-package acceptance, real Rust lint compilation and final
CI remain pending. No integration or publication authority is implied.

## Binding and scope

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`; `dev-session current` matched the trusted
  binding. Both identity environment variables were absent.
- Retained independent reviewer `reviewer0`, purpose `review`, ready in live
  roster revision 34; actual saved/assigned settings **gpt-6.1-sol / xhigh /
  read_only**. No override, fallback, nested agents or substantive authorship.
- Thread `01a16406-faaa-7cd0-bde3-c20802c18a72`; project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Repository `vpsfreecz/haveapi`; worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-followups`.
- Complete range **`b64fb25bea8d8222fb3263b99956c0b61438a859` →
  `090a188cb4ef3477324718627f4ae3415d1c0975`**, final tree
  **`e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`**.

Applied mandatory-change-review, Shared Reviewer Instructions and the full
general, architecture/repetition, scope/proportionality and risk/compatibility
references. Reused unchanged procedures read in this context and read the
follow-up repository guidance and changed release procedure. Inspected the full
packet, frozen design/plan/state/authorization, six-commit history, final diff,
source and declaration changes, relevant tests/docs and supplemental exports.
Risk remains high because publication is irreversible and loader/declaration/
generated contracts are public. Earlier released-source reviews do not cover
these new changes.

## Lane conclusions and concrete evidence

**General and risk: registry observation preserves exact publication guards.**
Commit `c424c579` separates metadata transport in `utils/release/registry_query.rb`
from package validation and publication in `publish.rb`. Only fixed exact-version
HTTPS registry endpoints are accepted, without URL credentials, redirects or
arbitrary query strings. The additional query is a fresh nonsecret token on the
same endpoint; it does not establish guaranteed origin freshness. GET requests
retain normal Net::HTTP proxy behavior, verified TLS and no upload credentials
or cookies. Diagnostics allowlist and bound cache/retry headers and exclude
response bodies and arbitrary exception contents.

RubyGems checks exact name/version/ruby-platform/SHA-256; npm checks name/version
and retained tarball SHA-512; Python checks identity, expected unique filenames
and every retained SHA-256. Conflicts and malformed successful metadata fail
before alternate reads or writes. Preflight missing metadata is bounded by one
canonical/fresh pair, with up to 60 seconds only for transient failures.
Confirmation uses monotonic 600-second deadlines; final destinations share one
deadline. Normal positive backoff remains under zero/past Retry-After, while a
larger valid server minimum is honored or refused if it cannot fit. Transport
attempts have a total timeout in addition to socket timeouts.

The retry loop never encloses an upload. Python's invocation-local validated
filename union affects staging only; final completeness requires a single whole
validated response. A later 404 cannot make a known matching file eligible for
reupload in that invocation. Gem/npm upload failures stop rather than retry;
accepted-but-unconfirmed uploads prevent later destinations and GitHub completion.
The existing PHP, protected-workflow, retained-artifact and publication-order
boundaries remain. Recovery documentation preserves original tagged helpers and
bytes, requires visibility/hash checks before an explicit recovery run, and does
not retrofit these helpers into the released 0.30.0 workflow.

**Architecture and risk: module relocation preserves implementation ownership.**
For `41251117`, independently compared the original callback functions and their
documentation with `clients/js/src/haveapi/client_invocation.ts`: exact bodies.
The main entry imports the installer before exposing the namespace; both paths
retain lookup on the original live `Action.waitForCompletion`. Independently
stripped import lines and compared the three original async implementation
bodies with `async/resource_model.ts`: exact concatenation. The three prior
module paths explicitly re-export their original names and constructor types.
This retains class identity, private-field ownership, nonthenability, association
references, request snapshots and save semantics without a new injection API.
The shipped declarations include the new implementation path and installer
declaration, while keeping public/deep facade imports resolvable. Actual npm
runtime entry remains the bundled distribution; declaration compatibility does
not assert an additional deep runtime packaging format.

**General, architecture and scope: tooling changes address the demonstrated causes.**
Commit `01a30a39` removes the obsolete gulp-jsdoc3/ink-docstrap chain and uses
maintained JSDoc with a deliberate template change. The fixed Action alias helper
requires exactly one canonical heading, rejects collisions and is idempotent;
it is bounded to the documented local destination. Imported tslib helpers are
bundled through one Rollup options owner used by gulp and graph tests. ES5 target,
UMD shell, factory-local catalog and existing async runtime requirements remain;
no normal-build warning filter or context override was introduced. The generated
bundle includes the helper license and has no standalone tslib import.

Lock inspection found the intended exact pins (JSDoc 4.0.5, tslib 2.8.1,
node-resolve 16.0.3, Acorn 8.19.0), existing TypeScript 5.9.3 retained, and no
unrelated common-package version changes. Obsolete dependencies are removed;
new entries belong to the selected tooling chains. The original full build log's
actionable diagnostic categories agree with the design. Nix account/Git fixture
informational messages remain visible.

**General and risk: Rust dependency and naming contracts are bounded.**
Commit `cbf6a3f0` adds the real runtime Fiddle requirement (`~> 1.1`, `>= 1.1.8`),
one consistent 1.1.8 lock/checksum and libffi in its two owning Nix shells.
Atomic exchange code is unchanged. Retained-gem inspection enforces the declared
dependency; isolated smoke activates that requirement and rejects default-gem
fallback rather than silently relying on the checkout's Ruby defaults.

Commit `431d7ffe` adds non_snake_case allowances only to generated module/accessor
items whose preserved public names contain double underscores. Existing naming,
route, IR, runtime, Cargo dependency and MSRV contracts remain. Unit fixtures
distinguish nested `widget__task` from ordinary `widget_task` and retain ownership/
determinism checks. The focused compile mode selects development Cargo plus
explicit Rust 1.95, rejects inherited compiler wrappers and fails on either lint
compile. Its mock tests are not evidence that either compiler actually passed.
Module-level attributes intentionally inherit within those generated modules;
there is no crate-wide or handwritten-code warning suppression.

These changes have demonstrated consumers and failures. Shared rules have
clear owners, and no speculative compatibility framework, retrying upload path,
new schema/protocol behavior or unrelated upgrade was added. Supporting tests
and lasting guidance fit their owning purposes.

## Whole history, streams and migration provenance

Independently inspected all six messages, per-commit path sets and final diff:

1. `cbf6a3f0`: runtime Fiddle/native prerequisite/retained-package acceptance.
2. `431d7ffe`: generated naming attributes and focused lint checks.
3. `01a30a39`: JS documentation/helper tooling and coherent lock update.
4. `41251117`: callback/async graph relocation and compatibility checks.
5. `c424c579`: registry confirmation, fake transport/clock tests and recovery docs.
6. `090a188c`: exactly eight cumulative generated JS/declaration outputs.

The split is coherent and matches the frozen plan; shared doc/spec hunks follow
their owning purpose. Messages describe the final behavior/rationale and fit
the 80-column rule. All six pre-reword/final commit pairs have independently
equal trees and raw patches. Final merge base equals the stated released base.
No obsolete iteration, fixup-only commit, temporary protocol or redundant branch
compatibility path remains. Released history is outside the rewrite.

Repeated streams: exactly **one Fiddle dependency/lock update, one coherent JS
tooling/package-lock update, and one cumulative generated JS output update**.
There is no intermediate pin/payload requiring a release/consumer/state-boundary
exception. The generated output follows both authored JS purposes. No version
bump or follow-up release commit was introduced.

Migration conclusion: **no migrations**. No database schema, persistent-format
conversion, protocol/API-version or generated public-name migration appears in
the full range. There are no follow-up migrations merged, released, deployed or
externally consumed, and no transitional migration lineage to preserve.

The complete full-index binary diff independently matches the export SHA-256
`c10184dfaf126e9f6bfcef210ac5f9f3a8ffa9decba55b6d325bd289967d5b41`.
Independently checked all 45 committed/live source hashes against the accepted
yield inventory: 44 exact, plus the single accepted extra EOF LF removal in
`client_invocation.ts`. Re-adding that LF reconstructs its original yield hash.
All eight generated hashes are unchanged. Whole-range whitespace passes.

## Reviewer verification and residual gaps

Known quick checks ran in the repository's tools-only Nix environment:

- RegistryQuery/Publisher fake transport and clock specs: **97 examples, 0 failures**.
  The fixture forbids real registry access and stubs publication commands.
- Existing distributed bundle helper/ES5/lock/CJS/AMD/browser checks: **8 passed**.
- Name-selected callback completion and strict-wrapper VM checks: **5 passed**.
  Compiler/build-oriented cases in that file were not selected or executed.
- Independent mechanical source relocation, full history/diff/hash and lock
  comparisons described above.

Owner JSDoc, graph, source/public/deep typing, async/resource, Fiddle setup and
Rust/release unit results remain owner evidence. No compiler, listener, build,
install, registry probe or long acceptance was run by the reviewer. A transient
Nix evaluation-cache busy notice did not prevent the quick checks from passing.

Remaining: clean full dependency setup; real full gulp documentation and JS/server
acceptance; full release build/test; installed npm/Python/Rust artifact checks;
real generated naming lint at root/mounted paths with development and independent
1.95 tools; exact final-head build-only CI. Package activation and declaration
checks must use the final retained artifacts. Rust's current integration runner
removes its temporary generated tree: do not claim retained schema/Cargo.lock/
generated-source input graphs or reuse from logs alone. That documented evidence
limit remains distinct from a compiler pass. The corrected tracked/index plus
known-cache verification gate supersedes the stale literal-status note in the
supplemental packet.

Source and index remained clean at the exact reviewed head. Existing untracked
caches were preserved; only this assigned report was written. Lead owns state
reconciliation and post-review verification. No push/default integration,
version/tag/release, registry, deployment or lifecycle action occurred. Follow-up
release and any separate generated-crate publication still need their own user
direction. The session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
