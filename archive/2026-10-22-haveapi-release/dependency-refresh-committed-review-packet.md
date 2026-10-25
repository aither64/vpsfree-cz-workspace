# Dependency refresh: committed final review packet

The authored package is complete and committed; independent final review and
affected long verification remain pending. Release 0.30.1 and new default
integration remain held. Nothing was pushed. No command, utility or claim is
active under implementer0. Lead assigns retained reviewer0 separately.

| Binding | Exact value |
| --- | --- |
| Repository | `git@github.com:vpsfreecz/haveapi.git` |
| Worktree | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-dependency-refresh` |
| Registered name | `haveapi-dependency-refresh` |
| Branch | `2026-10-22-haveapi-release-dependency-refresh` |
| Base | `090a188cb4ef3477324718627f4ae3415d1c0975` |
| Final head | `4dc0f7e11c494d1a0dc852dabcc312411699fcab` |
| Final tree | `a5c78fa77f4647e75d3f485ab12d7657bfcfab01` |
| Full-index binary diff SHA-256 | `274af4eb0e56be731f75a937d2e33401bb990d67ff84085516cf5a97367b5bc3` |
| Accepted 765-file canonical inventory SHA-256 | `3d4002b1fbf484ce93b10311ec7049822e375708b7ca2fd5348cb385568539a2` |

The complete series is one commit:
`4dc0f7e11c494d1a0dc852dabcc312411699fcab`,
`clients/js: refresh build and documentation dependencies`.
Its parent is exactly the supported, merged 090a boundary. See the complete
[series](dependency-refresh-final-series.json),
[full final diff](dependency-refresh-final.diff),
[path/blob/mode map](dependency-refresh-final-path-map.json),
[input graph](dependency-refresh-committed-input-graph.json) and
[machine-readable packet](dependency-refresh-committed-review-packet.json).

## Requested result and boundaries

The user requested our own dependency update and prohibited accepting the
Dependabot PR while holding the release. The accepted scope is in the
[architect addendum](dependency-refresh-addendum.md). This commit selects
Rollup 4.65.0, TypeScript 6.0.3, markdown-it 15.0.3 and anchor 10.0.0; linkify-it
resolves 6.1.0. JSDoc overrides reference the exact direct Markdown/anchor
dependencies and apply only beneath JSDoc. Unrelated direct ranges and runtime
dependencies remain unchanged. The lock has 240 entries including root and
239 retained SHA-512 integrity values; the owner peer graph has no problems.

TypeScript 6 retains the required ES5 output; TypeScript 7 removes it. The
explicit compatibility option appears only in the five compiler seams that
need ES5 or legacy node resolution. Strictness, declaration checks and
noEmitOnError remain. There is no skipLibCheck, diagnostic filter, second
transpiler or dropped ES5 contract. The JSDoc integration is our compatibility
responsibility; the override does not assert upstream support for new majors.

The package changes exactly ten authored paths: package manifest/lock, main
compiler config, callback fixture config, deep-module consumer config, the
server dynamic-JS compiler seam, the installed npm consumer compiler seam, two
developer guides and one new actual-JSDoc Markdown regression test. Its tests
cover independent renders, repeated heading identities, retained links and
navigation, inline JSDoc tags, fenced code and unchanged bare-URL behavior.

All 47 distributed files, including all 46 declarations, remain byte-identical
to 090a after two ordinary builds. The bundle remains SHA-256
`df8012e07294e50da26165803ac44e928c9cf7b594ff5d9228ba70379a133938`.
There is no generated delta and no empty generated commit. Public exports,
loader entrypoints, runtime source, shared VERSION, Rust inputs, Nix pins and
downstream generator pin are unchanged. No bot PR action, release resumption,
versioning, tag, default integration or publication was performed.

## History, migrations and compatibility

This is one final frontend build/documentation dependency update stream.
Selected dependencies, compiler settings, regression coverage and compatibility
guidance are bundled because the refreshed compiler and JSDoc graph need these
consumers to remain valid together. There are no intermediate selections,
fixups, repeated pin commits or superseded branch approaches. The independent
reviewer must assess this complete series and rationale, not only its final
tree. Exact dispositions are in
[history and migration inventory](dependency-refresh-history-migrations.json).

There are **no migrations in this change**. Baseline migration/schema/template
paths are unchanged under the complete source proof. None of the new changes
has been merged, released, deployed, published as a feature branch or consumed
by a known external consumer. Preserve merged HaveAPI 090a and downstream
main ff876abe, whose generator pin is 090a. Preserve the held patch head
8270b519 and its six provenance backports; this package does not rewrite or
backport into that boundary.

There is no database, persisted-state, wire protocol or downstream crate
change. Existing mixed client/server versions remain unaffected by the exact
unchanged bundle and declarations. Developer build inputs and JSDoc rendering
are the compatibility boundaries under review. Rollback selects the previous
development tool graph; no public registry bytes have changed.

Durable compatibility rationale belongs in `clients/js/README.md` and
`clients/js/test/README.md`; both lead-approved prose hashes match the accepted
inventory. Temporary execution history stays in session receipts.

## Verification and retained failures

The [owner receipt](dependency-refresh-final-receipt.md) records JS 105/0
(compatibility 55, async 39, resources 11), strict/public/deep declaration
fixtures, actual ES5 parsing, UMD/AMD/CommonJS loaders, module graph, real
JSDoc/Markdown checks, graph/peer/integrity checks, two-build 47-file equality,
release-check, focused release fixture 1/0, release unit 170/0, Python artifact
checks 6/0, and both Ruby compiler seams passing style and syntax. Commands and
full logs are linked from that receipt and hashed in the JSON review packet.

The accepted independent
[source crosscheck](dependency-refresh-crosscheck.md) found zero discrepancies;
its [full comparison](dependency-refresh-independent-comparison.json) binds
all 765 candidate files, 47 outputs, six public exports and 66 protected inputs.
It supports this review and does not replace committed final review.

Original missing-local-prerequisite failures, Prism setup failure, corrected
frozen setup and the sole generated Python-bytecode relocation remain intact.
These are setup/evidence history, not product fixes or suppressed tests. No
test was repeated for the accepted one-file relocation.

The first normal commit failed because the session wrapper omitted the already
installed gem executable directory from PATH. It created no commit and left
the exact ten accepted blobs staged. The separately granted recovery changed
only a new session wrapper's PATH. The one normal retry passed HaveapiI18n,
RuboCop and all commit-message hooks, including text width, without warnings.
No application, hook configuration, signature or dependency installation changed.
Original and recovery evidence is in
`dependency-refresh-commit-20261023T210841Z/`; successful hook transcripts,
exact executable/Ruby/gem proof, source equality and commit exports are under
its `path-recovery/` directory.

Before and after the commit, every candidate mode, blob and SHA-256 matched
the accepted 765-file inventory. Root/component lock and prose hashes match;
tracked source, index and nonignored untracked state are clean. The registered
comparison was captured with the documented method for the exact base/head;
its receipt is
`dependency-refresh-commit-20261023T210841Z/comparison-capture.log`.

No long check, local build, test, regeneration, installation or utility was
launched by the Git owner beyond the required normal commit hooks. After final
review, the architect brief calls for affected full JS/live-client, actual gulp
documentation, server dynamic-JS and isolated installed npm consumer checks.
Those checks and feature publication remain subject to separate lead grants.

## Independent review assignment boundary

Overall risk is medium: bounded development-tool and parser/plugin updates,
with a required existing compiler compatibility contract. Cover all four lanes:
general, architecture/repetition, scope/proportionality, and risk/compatibility.
Inspect the explicit overrides, exact lock scope, no suppression of unrelated
compiler errors, unchanged distributed/public surface, actual JSDoc behavior
and whole-series/migration conclusions independently.

Retained eligible reviewer0 is ready/read-only, model `gpt-6.1-sol`, effort
`xhigh`, thread `01a16406-faaa-7cd0-bde3-c20802c18a72`, checked from live
roster revision 34. Lead owns the separate assignment with no settings override.
No reviewer turn was launched here. Follow
`/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all four lane
references; this packet is not a review conclusion.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
