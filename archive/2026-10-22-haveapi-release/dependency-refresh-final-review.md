# Dependency refresh: final independent review

**No Blocking, Important or Advisory findings.** General, architecture/repetition,
scope/proportionality and risk/compatibility lanes pass for the committed refresh.
Affected longer checks remain pending. This review grants no release or default
integration authority.

## Identity and exact range

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`; `dev-session current` matched the trusted
  binding, with both identity environment variables absent.
- Independent retained `reviewer0`, review purpose, ready in live roster revision
  34. Actual saved/assigned settings: **gpt-6.1-sol / xhigh / read_only**.
  No override, fallback, nested reviewer/agent or substantive authorship.
- Thread `01a16406-faaa-7cd0-bde3-c20802c18a72`; project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Repository `vpsfreecz/haveapi`; worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-dependency-refresh`.
- Complete range **`090a188cb4ef3477324718627f4ae3415d1c0975` →
  `4dc0f7e11c494d1a0dc852dabcc312411699fcab`**, tree
  **`a5c78fa77f4647e75d3f485ab12d7657bfcfab01`**.

Read mandatory-change-review and all four lane references in full, including
Shared Reviewer Instructions. Read the complete committed packet, architect
addendum, owner and independent receipts, relevant source/config/test/docs and
history/input inventories; reused unchanged required workspace/repository
procedures already read in this context. Risk classification remains medium:
bounded development-tool changes with existing ES5, compiler and public consumer
compatibility requirements. Earlier 090a review does not certify the refresh.

## Four-lane assessment

**General: the selected graph and consumer changes are consistent.**
Commit `4dc0f7e` pins Rollup 4.65.0 and TypeScript 6.0.3, adds exact direct
markdown-it 15.0.3 and markdown-it-anchor 10.0.0 development dependencies, and
resolves linkify-it 6.1.0. Unrelated direct ranges and production dependencies
are unchanged. The JSDoc override uses only `$markdown-it` and
`$markdown-it-anchor` under `overrides.jsdoc`; no global dependency replacement
or patched node_modules is introduced.

Inspected the complete lock graph: 240 entries including root, with 239 valid
SHA-512 integrity strings. Changed versions belong to Rollup/platform binaries,
TypeScript and the selected Markdown dependency chain; duplicate nested parser
nodes and argparse are deduplicated consistently. Unchanged js-yaml already
requires the selected argparse 3 line. No stale markdown-it 12/linkify-it 3
runtime parser node remains. Retained `@types/markdown-it` metadata is a distinct
package, not that old runtime parser. The retained owner graph contains no
invalid/missing/problem markers; this is supporting owner evidence, not a fresh
npm resolution or install by the reviewer.

**Architecture/repetition: existing owning compiler/parser interfaces remain.**
TypeScript compatibility is added only at the five actual compiler seams:
main config, callback declaration config, deep-module fixture config, server
dynamic-JS spec config and retained npm consumer invocation. Async/resource
fixtures inherit their existing owning configs. No new transpiler, compiler
wrapper, generic suppression helper or parallel rule registry was added.

The setting selects the TypeScript 6 compatibility period for existing ES5/
Node10 options; it does not disable type checking. Strictness, noEmitOnError,
declarations, libraries, full declaration checks, targets and resolution remain
unchanged. The npm smoke still checks package-name resolution and permits only
the isolated consumer, installed package declarations and compiler libraries.
The server spec still compiles real rendered examples against public declarations.

Inspected actual installed JSDoc source as static context: it uses the public
MarkdownIt constructor/render and anchor plugin interface, enables retained HTML,
and calls render without a shared environment. The new test at
`clients/js/test/compatibility/jsdoc_markdown.spec.cjs` runs within JSDoc's real
loader/plugin lifecycle, checks package resolution, compares repeated and fresh
renders, and verifies heading IDs, links, inline JSDoc links, fenced code, retained
HTML, unlinked bare URLs and final navigation. Child failure or stderr fails the
test. Existing alias/navigation tests and other assertions are unchanged. The
override remains our tested compatibility responsibility, not an upstream claim
that JSDoc declares support for these new majors.

**Scope/proportionality: changes match one frontend tool refresh.**
There are exactly ten authored paths, nine modifications plus one real-JSDoc
regression file. Compiler seam changes, parser integration controls and two
short developer-guide additions support the selected graph. No application
runtime feature, second transpiler, unrelated override, broad upgrade or reduced
ES5 contract was added. TypeScript 6 is a deliberate compatibility selection
because the accepted TypeScript 7 line removes the required ES5 target; docs
explain that boundary without presenting 6 as the newest overall compiler.

**Risk/compatibility: published runtime and public types remain exact.**
Independently proved all 47 distributed files, including 46 declarations and the
complete bundle, byte-identical to supported 090a. The six static exports remain
AsyncClient, AsyncError, AsyncResourceInstance, AsyncResourceList, CallbackClient
and Client. UMD/AMD/CommonJS entrypoints, callback alias, bundled tslib license,
async runtime requirements and public declarations therefore retain their exact
committed representation. There is no new external browser helper dependency.

All 66 protected inputs match canonical base identities. Rust source/runtime,
generator and downstream pin inputs, shared VERSION, Nix pins, wire/auth behavior
and stored state are unchanged. The changed release helper only adds the compiler
compatibility arguments to declaration smoke; publisher behavior is untouched.
Existing mixed client/server versions are unaffected. Rollback selects the prior
development graph and needs no state conversion; no registry bytes change here.
Build-time JSDoc HTML handling remains the existing local documentation boundary,
not a new production request parser or demonstrated production vulnerability.

## Complete history, update streams and migration provenance

The complete series is exactly one commit, `4dc0f7e`, with parent and merge base
equal to supported `090a188c`. Its message describes the final dependency,
compiler and documentation result. The coherent selected tool graph, required
compiler consumer adjustments, real integration regression and compatibility
guidance form one reviewable dependency-update purpose.

History conclusion: no obsolete branch approach, intermediate selection,
fixup-only commit or transitional compatibility path remains. There is **one
final frontend dependency update stream**, no redundant repeated pin update and
no generated stream or empty generated commit. The two owner builds produced no
committed generated change. No release/consumer/state-boundary exception is
needed to retain an intermediate update.

Supported merged HaveAPI 090a, downstream ff876abe's 090a generator pin, original
release history and held patch 8270b519/six provenance backports remain outside
this new series. This review neither rewrites those boundaries nor grants a
backport, expanded integration or release decision. The packet records no merge,
release, deployment, feature publication or known external consumption of this
new change; no remote probing was performed by the reviewer.

Migration conclusion: **no migrations**. No database/schema, persisted-format,
protocol/API-version or downstream crate conversion is introduced. Protected
schema/template/runtime inputs remain equal. There are no new migration versions
with merge/release/deployment/external-use lineage or transitional migrations to
reconcile.

## Independent evidence and residual gates

Without running builds, installs or tests, independently reconstructed all
**765** committed mode/blob/SHA records and compared their actual live bytes
with the accepted inventory. Baseline has 764 paths; final adds only the new test.
All ten changed paths match the approved inventory; every other path is unchanged.

- Canonical inventory SHA-256:
  `3d4002b1fbf484ce93b10311ec7049822e375708b7ca2fd5348cb385568539a2`.
- Full-index binary diff independently equals the export, SHA-256:
  `274af4eb0e56be731f75a937d2e33401bb990d67ff84085516cf5a97367b5bc3`.
- Unchanged bundle SHA-256:
  `df8012e07294e50da26165803ac44e928c9cf7b594ff5d9228ba70379a133938`.
- All 47 outputs/46 declarations and 66 protected input identities independently
  match base. Whole-range whitespace passes; exact source/index remain clean.

Owner quick evidence records JS 105/0, strict/public/deep declarations, actual
ES5/loaders/graph/JSDoc/Markdown checks, two-build output equality, release-check,
focused 1/0 and full release 170/0 plus Python 6/0, and two Ruby seams passing
style/syntax. Original prerequisite/Prism/PATH failures and the sole bytecode
relocation are retained separately. No existing assertion was weakened to
obtain those results. These are owner executions, not reviewer-run checks.

Remaining affected gates: full JS including live-client tests, actual gulp
documentation, server dynamic-JS compiler specs and isolated installed npm
consumption/strict declaration smoke, with exact final input/artifact identities
and lead-selected feature CI. No fresh Rust/MSRV/native campaign is required
solely for this unchanged Rust input. Earlier successful artifacts are not
relabeled as execution of the new tool graph.

No build, install, test, compiler, listener, registry probe, Git or source mutation
was run by the reviewer. Parallel owner2 setup state/logs were not inspected.
Only this assigned report was written. Lead owns reconciliation and longer
verification. New default integration, 0.30.1/version/tag/publication, bot PR and
lifecycle actions remain held; the session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
