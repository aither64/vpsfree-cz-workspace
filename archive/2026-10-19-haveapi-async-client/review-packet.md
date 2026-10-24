# Final committed-deliverable review packet

Session: `2026-10-19-haveapi-async-client`.
Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Authoritative intent: [plan](plan.md), [design](design.md), [state](state.md).

## Outcome and scope

One npm `haveapi-client` package provides the existing callback `Client` and a
separate Promise-based `AsyncClient`, both authored in TypeScript and shipped
as ordinary JavaScript with generated declarations. Existing JavaScript users
must not need source changes. Current browsers are the new async runtime target.
The new React WebUI gets an injectable adapter and reproducible packed-artifact
trial; its production default remains fetch with no unpublished dependency pin.

The public compatibility gate covers callback arguments, return values,
synchronous throws, hooks, fire-and-forget calls, callable/prototype/descriptor
behavior, browser HaveAPI global, CommonJS and zero-dependency AMD shapes, static
constructors, and callback-only usage without Promise/AbortController.

Async behavior includes structured failures, per-request abort/timeouts,
independent auth/description state, typed path requests, async-owned resources,
explicit save/association loading, and separate receipt/completion waiting.
WebUI retains OAuth renewal/session identity checks and read-only retry policy;
mutations are not automatically replayed. Dynamic endpoint schema generation is
not included. Legacy WebUI, server protocol/state changes, release/version bump,
merge, deployment and broad default React transport migration are out of scope.

## Review selection and lanes

Risk: high, due to authentication, public compatibility and cross-project
request contracts. Eligible retained reviewer: `reviewer0`, independent,
read_only purpose, saved `gpt-6.1-sol` / `xhigh`; no overrides or fallback.
Lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Read the mandatory-change-review skill and each lane.
All intended substantive changes are now committed, trees/indexes clean and
quick gates passed. No long integration tests have started.
Review directly; no nested reviewers.

## Repository inventory and evidence

HaveAPI target is `master`; React target is `main`. React final receipt is below.
Both feature branches are unmerged; no migration, registry release, deployment,
or external package consumption has been performed by this task.

Exact inventories, complete commit series/final diffs, update streams,
documentation, quick evidence and deferred integration commands follow.

### HaveAPI final candidate

Worktree: `worktrees/2026-10-19-haveapi-async-client/haveapi`.
Branch: `2026-10-19-haveapi-async-client`.
Initial base: `cb3f39f75e8a63416388d24293f936d1db97162b`.
Final upstream review base: `c14e7d3158b91c134c2817b489cd29772fc09f82`.
Head: `ae0fe39738c3eb10019377d0fce95dc249cdfd16`.

Complete feature series, in order:

1. `34f431e76d52508233a1753eab1bd7d096b54f19`: original callback bundle fixture.
2. `90722e09a7fa25af518a26f36abd02bb0156c9a3`: callback TS/build/declarations;
   includes necessary release tooling authored-source path change to client.ts.
3. `d6059a159f4114c075ef542d83c0a670937b0343`: shared core/additive async API,
   resources, generated output, tests and linked technical guides.
4. `ae0fe39738c3eb10019377d0fce95dc249cdfd16`: AGENTS TS authoring guidance.

The original-base series additionally contains upstream release tooling
`82c9e778d04e0228785413a515e9ca76b2956215` and release documentation
`c14e7d3158b91c134c2817b489cd29772fc09f82`; those already belong to upstream.
Review the feature diff against c14e7d3 while retaining this ancestry evidence.
Owner inventory and exact command account: [haveapi-review-inventory.md](haveapi-review-inventory.md).
Full series, final diff/name-status, range-diff and package receipt are in
[evidence/haveapi](evidence/haveapi/). Final feature diff: 117 files,
12060 insertions / 3509 deletions, largely TS conversion/generated bundle/types.

The split makes original behavior, behavior-preserving migration and additive
API independently assessable. Generated JS/types stay with their producing
source so each stage is usable. Async core/resources are one cohesive commit
because their public context and output types are mutually required, accompanied
by their focused tests/docs. The release path correction was autosquashed into
the owning TS migration; no abandoned async-suffix public design was committed.
One TS/Rollup build dependency/lock stream is introduced in the migration;
there is no repeated version/channel bump. Bundle/declarations are regenerated
at both meaningful stages, not superseded dependency-pin updates. Please
independently assess whether these boundaries and stream dispositions are sound.

No schema/data migrations, server/protocol edits, registry release, deployment,
or supported external consumer boundary was introduced. Source-only rollback
reverts consumer calls needing AsyncClient with the client bundle. The new React
client is not yet an npm consumer in its production manifest/locks.

Documentation: clients/js/README.md, doc-async-client.md,
doc-async-resources.md, test/README.md, and root AGENTS.md. Generated i18n catalog
is unchanged. Public prose received the required main-agent writing pass.

Quick evidence: strict TypeScript build, callback 18/18, async core 10/10,
resource 10/10, generated callback+async declaration consumers, existing focused
Mocha 18/18 all pass. Release-source-path integration checks: make release-check,
release-test (22 examples), make -n version pass. Normal declared hooks passed.
Exact candidate pack has 50 files/43 declaration files and matches committed
JS/declaration bytes, with resolvable shipped guide links and no src/build
runtime files. Tar SHA256:
`46fd526ac02d04fdbc9526c7b7e67cdde0a5cfe730cf865702a4a2b4167bf991`.
See package-receipt.json for exact build/pack command and owner provenance;
package metadata lacks gitHead, so the React pilot receives --haveapi-ref.

Deferred post-review: full npm/Ruby-server shared CallbackAdapter+AsyncAdapter
contracts and typed-input suite; actual package Vite/type/browser trial and
real-browser UMD callback+async smoke in Chromium, Firefox, WebKit. VM loader
coverage is not claimed as browser evidence. Browser fixtures are synthetic,
not deployed or real vpsAdmin lifecycle proof.


### Browser environment

Exact pinned Playwright CLI1.61.0 remains in the WebUI. Existing realised Nix
browser artifacts match all its revision/version pairs: Chromium/headless1228
(149.0.7827.55), Firefox1532 (151.0), WebKit2311 (26.5), ffmpeg1011. The browser
bundle comes from Nix1.61.1 with independently compared identical browser
revisions, not a substitute CLI. See evidence/haveapi/browser-environment.json,
browser-preflight.log and pinned-runner-browser-paths.log. Fifty ELF library
checks found no missing libraries; no browser has launched. No source, lock,
host configuration, system loader or validation policy was changed.
Use PLAYWRIGHT_BROWSERS_PATH=/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers.


### React WebUI final candidate

Worktree: `worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async`.
Branch: `dev/haveapi-async-client`.
Base/fetched origin/main: `7860521f30826c3886c89c35e8ab6f4e082e0a4b`.
Head: `e35f2720683d0c63cd10d56b49864800b727b766`.
Complete feature series: one commit, `e35f2720 api: add injectable HaveAPI package pilot`.
Final diff: 26 files, +1328/-159. Lead verified clean tree/index and diff check.

One cohesive change extracts request preparation/send behind the existing policy,
adds an optional structural adapter, and supplies isolated package-fit fixtures
and technical documentation. Default fetch and its observable policy are retained.
Review whether this chosen boundary and commit scope are proportional. There
are no migrations, persistent schema/data changes, dependency/pin update streams,
obsolete branch approaches, registry releases, deployed states or supported
external consumer boundaries. Root/BFF package locks, dependencies, flake and
Nix package hashes remain unchanged. The initial read-only same-session WebUI
worktree is unedited at base and is not part of the source deliverable.

Key paths: src/lib/api/haveapi.ts, haveapiTransport.ts, haveapiRequestClient.ts
and adapter tests; scripts/test-haveapi-package.mjs and its tests;
scripts/haveapi-package/{consumer.ts,browser.ts,browser.spec.ts,umd.spec.ts,
playwright.config.ts,vite.config.ts,tsconfig.json,index.html}; package.json script;
resolved haveapi structural-debt exception removed without new hash/allowance.

Documentation: docs/design/HAVEAPI_PACKAGE_PILOT.md; linked handbook,
architecture/API contracts/verification/domain coverage/requirements and generated
implementation inventory; dated docs/work-log/2026-10-19-haveapi-package-pilot.md
and WORK_LOG pointer. Main-agent public-prose pass complete. Requirements cited:
REQ-007, REQ-011, REQ-012, REQ-059. No UI/localization/visual changes.

Quick evidence in Nix Node24.21.0/npm11.19.0:

- npm run typecheck + typecheck:tooling pass.
- focused haveapi.call/refresh/RequestClient Vitest: 59/59 pass.
- selected new runner/design-doc/structural/package-contents Node scripts: 30/30.
- patterns/Tailwind/scoped lint, scoped format and targeted new-file lint/format pass.
- docs inventory, design-doc audit, structural audit and diff check pass.
- custom Playwright --list shows seven tests (four adapter Chromium + three UMD).
- source candidate declaration preflight uses committed HaveAPI declarations;
  actual installed-tar typecheck is deferred, not claimed passed.

The source owner reports a normal temp-file commit with verified required
Michal Janoušek author+committer. No declared hook framework was found; no hook
bypass. An initially opaque quick watcher recovered after parent fallback, so
some short quick gates overlapped; both sources agree. No integration/browser
run happened during that duplication.

### Exact post-review verification

Use fresh pinned Luna/low watcher after findings are addressed. Full JS/server
commands are in haveapi-review-inventory.md. WebUI full unit/build also remain
pending. Actual package proof from the WebUI implementation worktree:

```sh
nix develop -c env PLAYWRIGHT_BROWSERS_PATH=/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers npm run test:haveapi-package -- --package /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/package/haveapi-client-0.29.0.tgz --webui-ref e35f2720683d0c63cd10d56b49864800b727b766 --haveapi-ref ae0fe39738c3eb10019377d0fce95dc249cdfd16
```

Please report Blocking/Important/Advisory findings with path/line/commit and lane.
Independently conclude whole-branch history/consolidation, retained generated
boundaries, repeated streams (or none), migration lineage (explicit no migrations),
public compatibility, ownership and scope. Identify residual test gaps without
claiming deferred tests passed. Report directly to lead; stay read-only and
perform all lanes yourself without nested reviewers.
