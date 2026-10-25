# Dependency refresh independent surface crosscheck

Status: **PASS, zero discrepancies** after the lead's frozen-candidate comparison
grant. The candidate contains exactly ten authored changes, with no generated or
protected-input change. No command remains active. Release 0.30.1 and new default
integration remain held. This supports, and does not replace, committed final
review or an integration/release decision.

The binding, complete environment identity and live same-session roster were
verified. Implementer3 retains workspace_write access, gpt-6.1-sol/xhigh and
installed full_access. The complete
[dependency refresh brief](dependency-refresh-addendum.md), workspace guidance,
canonical HaveAPI AGENTS/development guidance and JS README/test guidance were
read. No nested AGENTS exists for the affected JS/release/server paths at base.

## Final frozen comparison

Candidate: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-dependency-refresh`,
branch `2026-10-22-haveapi-release-dependency-refresh`. Its committed HEAD remains
canonical `090a188cb4ef3477324718627f4ae3415d1c0975`, tree
`e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`, with an empty index and the yielded
uncommitted source. Independently read every tracked/nonignored candidate file,
recomputed filesystem mode, SHA-256 and Git blob identity, and compared them with
the canonical baseline and owner1's complete final inventory. Repeated the
candidate path/mode/hash and HEAD/index comparison after inspection; it remained
identical.

- **765 files** equal the yielded inventory, versus 764 canonical baseline
  files: nine modifications, one new JSDoc test, no deletion or unexpected path.
- The exact ten authored path/hash records and the complete 765-file inventory
  match owner1. Inventory SHA-256 is
  `3d4002b1fbf484ce93b10311ec7049822e375708b7ca2fd5348cb385568539a2`, calculated
  over UTF-8 `json.dumps(all_files, sort_keys=True, separators=(',', ':'))`.
  Each entry contains mode, SHA-256, Git blob OID and canonical base mode/OID;
  blob OID is SHA-1 over `blob <decimal byte count>\0<bytes>`.
- All **47 distributed outputs**, comprising the bundle and **46 declarations**,
  exactly match canonical SHA-256 values. There is no generated delta. The
  bundle SHA-256 remains
  `df8012e07294e50da26165803ac44e928c9cf7b594ff5d9228ba70379a133938`.
- All **66 protected inputs** retain mode/hash, including every Rust source,
  template, runtime, fixture, Cargo input, relevant provenance, flake and shared
  version. Every other out-of-scope canonical path is also unchanged.

The package manifest equals the old manifest with only the four selected exact
dev-dependency changes/additions and the two JSDoc-scoped direct-reference
overrides. Runtime dependencies, unrelated ranges, scripts, package identity,
version 0.30.0, entrypoints and publication metadata remain identical. Root lock
specifications agree with the manifest.

The resolved lock has **240 entries including root**, with **239 SHA-512
integrities**. All five selected version/integrity/tarball triples (Rollup,
TypeScript, Markdown, anchor and linkify) match retained official metadata;
no network recheck occurred. Every retained package-name/version integrity
matches baseline, including argparse3.0.3 and mdurl2.1.0 moved from nested nodes.
There are 41 full lock-record changes: the root, 25 Rollup platform packages,
nine changed root package records and six removed nested records. No package
path was added. The non-Rollup changes follow the selected Markdown/linkify
dependency edges and deduplication; there is no unrelated dependency expansion.

All actual markdown-it nodes are15.0.3 and all linkify-it nodes are6.1.0. The
remaining @types/markdown-it12.2.3 is preexisting metadata, not a Markdown12
runtime. JSDoc still declares its original upstream ranges; the manifest's
scoped overrides deliberately select15/10. The retained npm graph shows those
effective versions beneath JSDoc and contains no problems, invalid, missing or
extraneous flags across280 version-bearing records. Its owner exit is0.
Anchor's wildcard Markdown peer and node-resolve's Rollup4 peer agree with the
selected graph. The candidate's own nonsymlink node_modules root contains a
214-package platform-installed hidden lock whose versions, resolved URLs and
integrities all match the frozen source lock. Only package metadata was read;
no installed code or npm command was executed.

Independent text/JSON comparisons isolate exactly five compiler seams:
`ignoreDeprecations: "6.0"` in the two existing JSON configs and the module-graph
and dynamic-JS temporary configs, plus the equivalent two compiler arguments in
the retained-package smoke. Removing just those additions restores canonical
contents. Inherited configs, strict/noEmitOnError/declaration settings, targets,
resolution, library checks and existing assertions remain unchanged; no
skipLibCheck or warning filter was added. The release helper has no other change.

The two new boundary tests use JSDoc's actual loader/Markdown plugin, verify
selected package resolution and compare repeated renders on the same and fresh
parsers. They assert independent heading IDs, links and inline JSDoc link
rendering, fenced code, retained HTML, no tabindex, unlinked bare URLs and final
navigation. Child failure or stderr fails the test. No existing assertion is
relaxed. Both tests have passing entries in the retained owner quick log.

The six static bundle exports, version, UMD/AMD/CommonJS wrapper and bundled
tslib license remain equal to base. Entire bundle/declaration equality establishes
no public generated change. Actual ES5 parsing, loaders, class identity and
strict/deep declarations are owner-executed quick evidence, not tests repeated
by this crosschecker.

Lead-approved prose hashes independently match:

| Path | SHA-256 |
| --- | --- |
| clients/js/README.md | `4e90056eacb5709821497d2fa69f5e1245f557e27cbdb9a3e356a82a9086c8e1` |
| clients/js/test/README.md | `c0ba78931fc34f5fde68fb2c2ee6d74d5d087bc514021884a47d3a159ca56549` |

Supporting owner results were inspected without rerunning them: JS105/0
(55 compatibility,39 async,11 resources), strict/declaration fixtures, two-build
47-output determinism, release170/0 and Python6/0 after prerequisite recovery,
and two changed Ruby files passing style/syntax. The original failures and
outer98 are preserved. The sole generated bytecode relocation is reconciled;
the original path is absent and the retained destination independently matches
SHA-256 `c0757dcd00012466dff162a03870dc1bfb0d1d1887e3d7bcf48d72b5d411ca54`.
It did not change intended source or locks, and no test was repeated for that move.

Full supporting evidence, exact path records, lock deltas, metadata hashes,
compiler comparisons and owner-receipt hashes are retained in
[independent comparison JSON](dependency-refresh-independent-comparison.json),
SHA-256 `9ffb2ef2577cf67fdd4528293d242d1a0b089d66c1b366696f313d896d251112`.
The original baseline JSON remains unchanged. Sole Git ownership stays with
implementer0; lead accepts this supporting comparison before the scoped commit
and later independent committed final review.

## Retained canonical baseline preparation

Read only canonical Git objects in `repos/haveapi.git` at
`090a188cb4ef3477324718627f4ae3415d1c0975`, tree
`e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`. At baseline preparation, no candidate
worktree, installed graph or generated candidate output was read. No fetch, PR action, npm command,
compiler, build, generation, CI/network probe or Git/index mutation ran.

[Full baseline JSON](dependency-refresh-baseline.json) retains mode, Git blob,
byte count and SHA-256 for all **764 tracked paths**; the complete **246-entry npm
lock graph**, manifest and direct ranges; compiler configs; all **46 declaration
files** and their export lines; bundle identity/static loader markers; and
**66 protected Rust/runtime/Cargo/provenance/toolchain/version input paths**.

Sorted path-NUL-bytes-NUL SHA-256 of the complete canonical tree is
`18f7a1e6fe04ade30fa78842aeced7ff3c98a8ba6c63ea52cf5823587316d132`.
Baseline JSON SHA-256 is
`d7779da636402a0a8b7ea8da6972885a6c8998ad995c279ee7416997c3796f96`.

| Dependency | Canonical resolved baseline | Accepted candidate selection |
| --- | --- | --- |
| Rollup | 4.64.10 | 4.65.0 |
| TypeScript | 5.9.3 | 6.0.3 |
| markdown-it | root 12.3.2; JSDoc nested 14.3.3 | 15.0.3 |
| markdown-it-anchor | 8.6.7 | 10.0.0 |
| linkify-it | root 3.0.3; JSDoc nested 5.0.2 | 6.1.0 |
| @types/node | 24.19.2 | retain 24.19.2 |
| JSDoc / node-resolve / tslib / Acorn | 4.0.5 / 16.0.3 / 2.8.1 / 8.19.0 | retain |
| chai / gulp / mocha / xmlhttprequest | 6.3.0 / 5.0.1 / 12.0.3 / 1.8.0 | retain |

The canonical manifest keeps `xmlhttprequest`, chai, gulp and mocha at `latest`,
@types/node at `^24.19.2`, and Rollup at `^4.0.0`. Compare the final authored
manifest against this exact baseline and the brief's selected direct pins;
unrelated ranges must not inherit the bot's `latest` to `*` rewrite. The accepted
JSDoc-scoped overrides are `$markdown-it` and `$markdown-it-anchor`; their scope
does not establish upstream JSDoc support for the new majors.

The base compiler targets ES5 with node resolution, strict=true,
noEmitOnError=true, declarations=true and importHelpers=true. Its declaration
fixtures are strict/noEmit; async fixtures inherit the relevant main settings.
Later comparison must isolate the TypeScript 6 compiler compatibility options
and preserve strictness, emitted/public type constraints and meaningful tests.

Static bundle export names are `AsyncClient`, `AsyncError`,
`AsyncResourceInstance`, `AsyncResourceList`, `CallbackClient` and `Client`.
The baseline has the bundled tslib license prefix and existing AMD/CommonJS/
browser-global wrapper markers. These are source observations; they do not
certify ES5 parsing or loader behavior. Those conclusions must cite the owner's
actual quick commands/results, without presenting them as crosscheck execution.

## Comparison boundary retained from preparation

The comparison above fulfilled this prepared scope after the explicit frozen
yield: bind the exact candidate HEAD plus uncommitted
path/mode/byte hashes and retain before/after stability proof. Compare all changed,
added and deleted paths; selected manifest versions, override scope, lock graph
integrities and any stale Markdown12/linkify3 node. Read existing owner graph/
peer output and quick receipts without rerunning npm or compilers. Preserve
invalid/unknown peer evidence as such rather than assuming the override is valid.

Inspect all generated bundle and declaration changes, actual public exports,
strict compiler option deltas, tests and documentation assertions. Compare the
complete protected input inventory and all other out-of-scope paths against the
canonical base. Distinguish direct static checks from owner-executed ES5, loader,
license, public identity, Markdown/JSDoc, declaration and graph tests.
Report concrete unexpected changes through lead; no source repair or broader
compatibility decision is delegated to this crosscheck.

No test was executed by implementer3.
Lead owns user-facing README prose after the technical draft; implementer0 owns
all Git/index/hooks. Existing release/artifact/source boundaries stay intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
