# Dependency refresh while HaveAPI 0.30.1 is held

Architect brief, 2026-10-23. User held publication, requested our own dependency
update and prohibited accepting the Dependabot PR. Lead accepted the bounded
dependency selection below; lead grants source execution separately. No bot
merge/close/comment/branch mutation, installation/build or application edit was
performed in this investigation. Existing integrations/artifacts stay intact.

## Actual PR and package evidence

[Dependabot PR #3](https://github.com/vpsfreecz/haveapi/pull/3) opened at
2026-10-23T20:02:42Z against master090a; bot head is
`1387b67fdf608915589245ac0b8193c12554b1da`. Its body advertises
linkify-it3.0.3→6.1.0 and markdown-it12.3.2→15.0.3. Its **complete actual diff**
changes only `clients/js/package-lock.json` (51 additions/107 deletions), hoisting
already-present **5.0.2/14.3.3**, removing their duplicate nested chain and changing
several root `latest` strings to `*`. It does not install the advertised latest
majors or change package.json. Do not copy its lock output.

Current JSDoc4.0.5 declares markdown-it^14.1.0 and anchor^8.6.7. The lock retains
stale root12.3.2/3.0.3 alongside safe nested14.3.3/5.0.2. Official advisories
[GHSA-vfgh-jcmw-g37q](https://github.com/advisories/GHSA-vfgh-jcmw-g37q) and
[GHSA-v245-v573-v5vm](https://github.com/advisories/GHSA-v245-v573-v5vm), among
others retained below, confirm quadratic parsing issues in the old chain.
Markdown14.3.3 and15.0.3 both contain current fixes; linkify5.0.2 and later
contain its fixes. These are development-documentation dependencies, not shipped
browser or Ruby request-parser code. JSDoc enables HTML, so preserve the bounded
build-time risk without claiming a demonstrated production exploit.

Evidence, including official URLs and observation timestamps:

- [Complete PR/diff and public advisories](dependency-refresh-pr3-evidence.json).
- [Official npm/RubyGems metadata](dependency-refresh-official-metadata.json).
- [Pinned upstream source/changelogs and retained-major metadata](dependency-refresh-upstream-evidence.json).

## Exact recommendation and compatibility

| Dependency | Resolved now | Selected value and reason |
| --- | --- | --- |
| Rollup | 4.64.10 | **4.65.0**, current stable, within resolver16's ^4 peer/Node24 requirements |
| TypeScript | 5.9.3 | **6.0.3**, highest stable ES5-capable line; latest7.0.2 removes ES5 |
| markdown-it | root12.3.2/nested14.3.3 | **15.0.3**, current stable, exact direct dev dependency |
| markdown-it-anchor | 8.6.7 | **10.0.0**, current stable, exact direct dev dependency |
| linkify-it | root3.0.3/nested5.0.2 | **6.1.0**, current stable through Markdown15 |
| @types/node | 24.19.2 | Retain highest stable24 matching actual Node24; latest26.6.5 describes a different host API |
| JSDoc / node-resolve / tslib / Acorn | 4.0.5 / 16.0.3 / 2.8.1 / 8.19.0 | Retain: each is verified current stable |
| chai / gulp / mocha | 6.3.0 / 5.0.1 / 12.0.3 | Retain: each is verified current stable |
| xmlhttprequest / Ruby Fiddle | 1.8.0 / 1.1.8 | Retain: each is verified current stable; no runtime/native upgrade needed |

Add exact direct dev Markdown/anchor versions and explicitly scope their
compatibility override to JSDoc:

```json
"overrides": {
  "jsdoc": {
    "markdown-it": "$markdown-it",
    "markdown-it-anchor": "$markdown-it-anchor"
  }
}
```

This is our tested compatibility responsibility, not a claim that JSDoc declares
15 support. Actual JSDoc4 uses root CJS `new MarkdownIt`, `render` and
`.use(anchor, {tabIndex:false})`, not removed private Markdown subpaths. Current15
provides a callable CJS root. Anchor10 shares heading uniqueness only when an
explicit env is reused; JSDoc calls render without a shared env. Test repeated
documents/headings. JSDoc does not enable linkify and escapes bare URLs, so the
new fuzzy-link default must not alter that behavior. Preserve links, inline
JSDoc tags, fenced code, headings, API navigation and the existing Action alias.
No node_modules patches, fork, unrelated overrides or automatic audit-fix.
The new resolved graph must contain no stale12/3 chain or invalid peers.
JSDoc/anchor's metadata-only `@types/markdown-it` dependency may remain; it is
not a client declaration input and must not be replaced with a fake package.

Official [TypeScript6 notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
document ES5/node10 as deprecated but available with `ignoreDeprecations: "6.0"`,
and removed in7. The7.0.2 exports also exclude existing `typescript/bin/tsc`
lookups. Select6.0.3 with that explicit setting only in the owned compiler
configs/invocations that need the established ES5/legacy-resolution contract.
Explain these two options in developer guidance. Preserve strict/noEmitOnError,
declarations, actual ES5 parse and runtime/type tests; no skipLibCheck, warning
filter, relaxed assertions or blanket diagnostic suppression. Do not introduce
a second transpiler or silently drop ES5 to select7. Non-mechanical public type
changes require lead assessment. This is a justified compatibility pin, not a
claim that6 is the newest overall compiler.

Node24/Nix pins stay unchanged. Preserve UMD/AMD/CommonJS entrypoints, callback
alias/async interface, bundled ES5 tslib module/license and no external browser
require. Generated bytes may change from the tool update; inspect actual build
output and public declarations instead of hand editing or assuming equality.

## Frozen state, owners and history

Owner0's reconciled patch is `worktrees/2026-10-22-haveapi-release/haveapi-0-30-1`,
branch `2026-10-22-haveapi-release-0.30.1`, HEAD
`8270b519a2ea1d60735634d34cc1a451a3e904b4`, tree e947 equal090a. Six -x
backports passed hooks/intermediate equality; VERSION0.30.0 and CHANGELOG remain
untouched. No later setup/versioning/push/tag, active command/watcher or claim.
Preserve this frozen worktree; its receipts are
`release-0301-source-20261023T201151Z/preversion-equivalence.json` and
`user-hold-state.json` in that receipt directory.

**Owner0** prepares a separate registered `haveapi-dependency-refresh` worktree
under this session, branch `2026-10-22-haveapi-release-dependency-refresh`, from
merged `090a188cb4ef3477324718627f4ae3415d1c0975` after fresh target checks.
Owner0 retains sole Git/index/hooks. **Implementer1** owns the cohesive source
package after lead grant (live roster34: ready/workspace_write):

- `clients/js/package.json`, package-manager-generated `package-lock.json`.
- `clients/js/tsconfig.json`, relevant `test/**/*.tsconfig.json`, temporary
  compiler config in `test/compatibility/module_graph.spec.cjs`.
- New `test/compatibility/jsdoc_markdown.spec.cjs` and narrowly necessary existing
  JSDoc/ES5/loader/type regressions, beneath `clients/js`.
- Compiler-only options in `utils/release/artifacts.rb` npm consumer smoke and
  `servers/ruby/spec/client_examples/dynamic_js_spec.rb`; no publisher changes.
- Bounded `clients/js/README.md`/`test/README.md` compatibility guidance.
- Tracked `clients/js/dist/**` produced only by the normal build.

Use our manifest and normal npm resolution in the declared shell. Pin newly
selected direct tools/dev dependencies exactly; preserve unrelated direct
ranges and do not copy the bot's latest→* changes. Refresh/deduplicate the
justified graph, retaining npm integrities. Unexpected peers/extra dependency
scope return to lead. **Implementer3** independently checks the frozen lock,
generated/public surface after owner1 yield; evidence only, no overlapping edits.
Lead owns final user-facing prose once technical facts settle.

One final authored dependency/config/test/docs commit, then a generated-only
commit if dist changed. Consolidate intermediate unpublished selections/fixes
before final review. Do not rewrite merged090a: downstream main pins it and its
source ref/artifacts are required. The patch's six exact -x commits preserve that
supported source boundary. Do not squash new behavior into them while retaining
misleading provenance. After new review and separately confirmed expanded
integration/release direction, backport the new commits -x onto8270b, then
prepare version metadata. Earlier integration approval does not cover this
expanded change, and investigation does not resume the release grant.

## Checks and release-resume gates

Quick: exact graph/peer/integrity inventory; strict typecheck and declaration
fixtures; actual ES5 parsing, browser/AMD/CommonJS loaders and three-facade graph
checks; real JSDoc navigation/alias and Markdown/plugin tests including repeated
heading renders. Preserve diagnostic output. Regenerate normally and prove
deterministic output; inspect all declaration/export differences against090a.
Run release quick checks after its compiler-only adjustment. Known short checks
stay inline; uncertain setup/build duration uses the fresh utility policy.

Commit the entire intended result before **new independent final review** by
retained reviewer0, including complete base/head series, lock/source/generated
split, scoped overrides, compiler compatibility, public declarations, preserved
090a lineage and no migrations. Prior090a review is insufficient for this change;
general, architecture, proportionality and compatibility concerns are affected.

After review, affected longer gates are the full JS suite including real local
client tests, actual gulp documentation task, server dynamic-JS compiler specs,
and isolated npm package consumption/strict declaration smoke. Fresh watcher
handles long/uncertain checks; exact new manifest/compiler and generated artifact
identities must be retained, without borrowing old node_modules. Ordinary feature
CI runs normally; no duplicate dispatch. No repeat Rust/MSRV/native campaign
with unchanged Rust inputs. Eventual final release/tag checks still cover all
maintained packages and original artifact identities under the
[release plan](release-0.30.1-plan.md).

Lead accepts the reviewed concrete result and coordinates the still-held
expanded integration/release decision before versioning/tag/publication resumes.
No database, protocol, persisted-state, deployment or downstream crate change.
Rollback selects prior development source/build inputs; published bytes remain
immutable. Bot PR remains untouched.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
