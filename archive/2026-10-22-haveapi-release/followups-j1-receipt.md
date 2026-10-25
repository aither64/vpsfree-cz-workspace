# J1 dependency/build follow-up receipt

Source yielded for hooked commits; independent review and long acceptance remain pending.

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-followups`. Branch `2026-10-22-haveapi-release-followups`, base `b64fb25bea8d8222fb3263b99956c0b61438a859`. Released source, tag, original artifacts and old checkout were not changed.

J1 replaces gulp-jsdoc3/ink-docstrap with JSDoc 4.0.5, bundles tslib 2.8.1 ES5 ESM through node-resolve 16.0.3 and checks ES5 syntax with Acorn 8.19.0. TypeScript 5.9.3, runtime dependency and all other retained locked package versions remain unchanged. The complete tslib 0BSD notice is embedded in the generated bundle. No Rollup context changes or warning filters.

The maintained default JSDoc template deliberately changes appearance. Actual generated Client, Action and Resource pages/navigation passed; the documented Action#invoke__anchor remains beside canonical#invoke. The fixed alias rejects absent/duplicate headings and collisions, is idempotent and propagates generation failure. No generated HTML is tracked.

## Authored paths (11)

- `clients/js/package.json`
- `clients/js/package-lock.json`
- `clients/js/tsconfig.json`
- `clients/js/gulpfile.js`
- `clients/js/jsdoc.json`
- `clients/js/rollup.config.js`
- `clients/js/jsdoc_aliases.js`
- `clients/js/test/compatibility/build_helpers.spec.cjs`
- `clients/js/test/compatibility/jsdoc_aliases.spec.cjs`
- `clients/js/test/async-resources.tsconfig.json`
- `clients/js/test/README.md`

## Generated paths (8), separate cumulative commit

- `clients/js/dist/haveapi-client.js`
- `clients/js/dist/types/haveapi.d.ts`
- `clients/js/dist/types/haveapi/client.d.ts`
- `clients/js/dist/types/haveapi/client_invocation.d.ts`
- `clients/js/dist/types/haveapi/async/resource.d.ts`
- `clients/js/dist/types/haveapi/async/resource_instance.d.ts`
- `clients/js/dist/types/haveapi/async/resource_list.d.ts`
- `clients/js/dist/types/haveapi/async/resource_model.d.ts`

## Quick evidence

- Setup: one new-worktree locked npm ci, exit 0 in 11.5 seconds, Node 24.21.0 / npm 11.19.0, 220 packages; manifest/lock before/after exact SHA matches. Setup was utility-owned.
- One cumulative `npm run build` after J1/J2 source readiness; `npm run typecheck` passed. No Rollup CIRCULAR_DEPENDENCY or THIS_IS_UNDEFINED diagnostic.
- Final compatibility 53/0 (includes actual JSDoc pages+anchor, ES5+helper adversarial globals, loaders, graph/facade/deep types); async 39/0; isolated resources 11/0; public callback/async declarations compile.
- All three isolated facade.js outputs exist; shared config explicitly names their existing source entrypoints.
- Initial fixture-only failures retained in followups-js-quick.log; CommonJS VM host and strict consumer ambient-type isolation corrected, compatibility rerun passed without another product build.
- Syntax 5/0, owned whitespace scan and git diff --check pass. README main-agent prose pass preserved.

Bundle SHA256: `df8012e07294e50da26165803ac44e928c9cf7b594ff5d9228ba70379a133938`. Package/lock and exact file hashes are in [JSON](followups-j1-receipt.json). Logs: [initial](followups-js-quick.log), [remainder](followups-js-quick-remainder.log), [final compatibility](followups-js-compatibility-final.log).

No commands remain active. Implementer0 owns Git/index/hooks; commit the authored and cumulative generated groups separately. No version, ref, publication, registry, lifecycle or cleanup action was taken. No migrations.

The actual JSDoc CLI runs in a temporary output directory as a quick regression; the full gulp doc task and clean installed npm/package consumer checks remain post-review long acceptance. Existing release smoke-npm verifies an isolated installed package and strict declarations; retain loader/ES5/helper and deep-path checks in that batch.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
