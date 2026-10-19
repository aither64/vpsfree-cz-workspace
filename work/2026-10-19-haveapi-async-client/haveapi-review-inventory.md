# HaveAPI final-review preparation

## Current bridge candidate: 76f190f9

Owner: implementer0. This section supersedes the candidate identity and pending
commands in the historical dc941578 evidence below. It is owner evidence, not
independent review or integration approval. Lead owns the review packet/state.

- Original session base: `cb3f39f75e8a63416388d24293f936d1db97162b`.
- Fresh SSH-fetched master remains `c14e7d3158b91c134c2817b489cd29772fc09f82`.
- Final head: `76f190f9561eabee3414919ddd26e62e48c43f58`.
- Final tree: `157489d9351dae3ff669ee8f4827d272b99d22f7`.
- Final tree equals the complete checked bridge checkpoint `20d8165` exactly.
  Index/worktree are clean; no upstream-only commits remain.

| Final feature commit | Retained boundary |
| --- | --- |
| `34f431e76d52508233a1753eab1bd7d096b54f19` | Original callback fixture, unchanged |
| `0e63360e46a40dcbe744d7ee7475fb0151f8d37b` | Callback TypeScript migration/build/release-path repair, now including strict-context bridge and regression |
| `81994d25cf6dc50754a7e9b2820aafc8fa00f0e2` | Shared core/additive async and accepted R1/R2/R3, with coherent generated output |
| `76f190f9561eabee3414919ddd26e62e48c43f58` | TypeScript workflow guidance, patch unchanged |

The original-base range also retains upstream `82c9e778` and `c14e7d31`
unchanged. Whole original-base diff: 136 rename-aware paths, 13,885 insertions,
3,587 deletions. Feature-only diff: 124 paths, 12,730 insertions, 3,516 deletions.
Old accepted head `dc941578` to current is exactly nine approved paths,
240 insertions and 35 deletions. Source changes are the four-property internal
host-global bridge and its three callback consumers; the remaining paths are
independent strict-context fixture/docs and generated bundle/declarations.
Authentication module evaluation order, live registry lookup, public/static
registry identity, live defaultParams return and protocol scratch values are
preserved. No public entrypoint or eager async runtime was added.

Bridge history was consolidated into the owning callback migration. Mechanical
source-import and generated-bundle conflicts were resolved by retaining the
approved final imports and rebuilding from each stage, without changing intent.
Callback-only stage: build, 25 compatibility cases and callback declaration
consumer passed. Async stage: build, 26 compatibility cases and both declaration
consumers passed. The final all-path tree equality proves the previously checked
36 async/11 resource/18 local Mocha results apply to this candidate. Normal Nix
checkpoint and final callback-amend Overcommit hooks passed; no bypass was used.
The original Authentication side-effect dependency remains before Client code.

Dependency stream remains the single TypeScript/Rollup/lock update in the
migration; async scripts/manifest do not change resolutions. Generated bundle
and declaration outputs are retained at two independently buildable functional
boundaries, not as superseded standalone refreshes. No transitional runtime or
abandoned implementation remains. The generated translation catalog is unchanged.
There are no database, disk, server-protocol or persistent-state migrations,
and none was merged, released or deployed. Prior npm tarballs were consumed only
in disposable local verification; they create no supported deployed revision or
migration boundary. Old receipts/artifacts remain intact.

All current review artifacts are under:
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/bridge/`:

- `reviewed-to-final.diff` and `reviewed-to-final-range-diff.txt` bind dc941578
  to the current whole series; `feature-series.txt`,
  `complete-original-base-series.txt`, `feature-final.diff`,
  `original-base-final.diff`, `feature-name-status.txt`, `feature-diff-stat.txt`
  and `final-status.txt` inventory the final deliverable.
- `callback-stage.log`, `async-stage.log`, `callback-hooks.log` retain coherent
  stage regeneration and hook evidence. `../bridge-quick.log` retains the final
  integrated local gates. Peer strict-context baseline/positive receipts remain
  in its assigned evidence directory, with eight positive actual-bundle cases.
- The accidental inclusion of server-dependent `typed_input.spec.js` in the
  initial client-js-shell local Mocha command failed its server hooks before
  any test assertions. It is not counted as a product result and was not retried.
  The corrected self-contained local set passed 18/18; real-server coverage
  remains the post-review top-level command below.

### Current packed artifact

- Path: `/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/bridge/package/haveapi-client-0.29.0.tgz`
- SHA256: `6efa9263f79c999f1efa11014d4674b0cfb8bab07afb4dfaab6e93193040c123`.
- Size 55,288 bytes; 51 files, including 44 generated declarations.
- Packed after the committed async-stage build using `npm pack --ignore-scripts`.
  Every packed file equals its committed bytes. Relative Markdown links resolve;
  no src/build/node_modules are included. Package main/types/version remain
  unchanged. No gitHead is present: provenance is the pack-owner assertion plus
  committed-file byte equality, not cryptographic source-build proof.
- Receipts: `package-receipt.json`, `package-files.txt`, `package.sha256`,
  `npm-pack.json`. Prior candidate tarballs remain historical, unmodified.

### Review and verification status

Lead reported the affected final review of committed head `76f190f9` complete:
no findings in the same-reviewer **general, architecture and risk/compatibility**
lanes. Whole-history, generated/dependency-stream and no-migration conclusions
were accepted; reviewer independently passed callback 26 cases, an additional
strict globalThis probe and packed-byte parity. This corrects the package
mechanism after actual Vite strict-module import failed at dc941578. Raw UMD
Chromium/Firefox passes at that earlier head do not establish fit of the current
minified import.

After affected review acceptance, the final full JS/Ruby-server command passed
once at this bridge candidate (exit 0, 49 seconds) through fresh pinned Luna/low
full-access watcher `bridge_full_js_watcher`. It passed callback 26/26, async
36/36, resource units 11/11, both emitted-declaration consumer configurations and
all 50 **Mocha** cases. Those include seven CallbackAdapter and seven AsyncAdapter
contracts against the local Ruby test API, 18 typed-input cases and 18 existing
local regressions. This was not a full Ruby/RSpec suite; the raw watcher receipt's
`rspec` label is inaccurate, and the log establishes the actual coverage.

HEAD/tree remained exactly `76f190f9` / `157489d9`; the worktree/index stayed
clean. Parent checks confirmed no matching Ruby test-server process and the tar
SHA256 remained `6efa9263…`. No retry, source change or unrelated suite ran.
The watcher operation ended and its utility slot was released to lead/peer.
Full evidence: `bridge/integration/{full-js.log,exit-status,receipt.json,
parent-confirmation.json}` beneath the evidence root above. Exact executed
command (the earlier dc941578 success remains historical below):

```sh
nix develop -c bash -c '
set -e
export BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"
bundle install
cd clients/js
npm test
'
```

Peer's final actual-package proof passed once (exit 0, about 52 seconds) using
WebUI `1ef5b7b079366a94461d5d467d7f6d3969d98217`, this exact HaveAPI head and
this tarball. Installed declarations and minified named-import Vite build passed;
all four adapter Chromium cases plus raw UMD in Chromium, Firefox and WebKit
passed, without skips or retries. Actual engine versions were 149.0.7827.55,
151.0 and 26.5. All 407 installed baseline packages retained their names/versions;
manifest/lock hashes stayed unchanged through final reconciliation. Both source
trees remained clean. The candidate install and browser fixtures were disposable,
with synthetic BFF identity/API responses: no production/OAuth deployment claim
or default application transport/dependency switch follows.

Peer receipts independently inspected by implementer0:
`/tmp/2026-10-19-haveapi-async-client-implementer1-verification.zpVPaN/package-proof-runtime/parent-receipt.json`
and `/tmp/webui-haveapi-package-wycRMT/result.json`. The source/tree/tar were
rechecked unchanged.

Later, the user requested an author/committer-only rewrite of the two WebUI
commits. The actual package-tested `1ef5b7b0` maps to equivalent source commit
`0d05a2584bf30ee4acfa1d64bf00325cdda62934`; final WebUI PR74 head is
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`. Peer's final receipt proves identical
trees/messages/patches, with both identities now Jakub Skokan
`<jakub.skokan@havefun.cz>`. Current-head WebUI CI `39306325205` and smoke
`39306325290` passed all six jobs. This metadata rewrite did not change HaveAPI,
the tarball, runtime/dependency content, or the exact earlier execution identity.
Receipt: `/tmp/2026-10-19-haveapi-async-client-implementer1-verification.zpVPaN/authorship-rewrite/final-receipt.json`.
The peer reports the requested PR draft conversion remains token-permission
blocked; no authentication workaround or mark-ready action occurred.

Exact successful proof environment and tested candidate identities:

```sh
nix develop -c env \
  PLAYWRIGHT_BROWSERS_PATH=/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers \
  __EGL_VENDOR_LIBRARY_FILENAMES=/nix/store/fdw09ayics8bwzb6k7vr8kfgmwmv35h5-mesa-26.1.8/share/glvnd/egl_vendor.d/50_mesa.json \
  GBM_BACKENDS_PATH=/nix/store/fdw09ayics8bwzb6k7vr8kfgmwmv35h5-mesa-26.1.8/lib/gbm \
  npm run test:haveapi-package -- \
  --package /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/bridge/package/haveapi-client-0.29.0.tgz \
  --webui-ref 1ef5b7b079366a94461d5d467d7f6d3969d98217 \
  --haveapi-ref 76f190f9561eabee3414919ddd26e62e48c43f58
```

The first authorized unchanged WebKit blank-page probe (no candidate code)
failed before application execution: `Could not create WPE EGL display:
EGL_SUCCESS. Aborting...`; newPage timed out. Logs/exit/cleanup receipt remain
in the sibling `webkit-diagnosis/` directory.

Lead then authorized one scoped dependency operation. A fresh Luna/low watcher
realised Mesa 26.1.8 from the exact WebUI locked nixpkgs revision
`5e2305d577ca00acbba631b05cb1094d172b29f3`, source
`/nix/store/pgy8nq09hh4mdgr30ir9v0lcjpz34vxb-source`, using substitute-only
`--max-jobs 0 --builders ''` (exit 0, 11 seconds). No local build, kernel,
host graphics link, source or project dependency change occurred. Its GC root is
`webkit-diagnosis/mesa-runtime`, pointing at the vendor package path in the
proposed proof environment above. The absolute vendor JSON, referenced
`libEGL_mesa.so.0`, GBM backend and complete closure were verified and hashed.

With only the two approved vendor/backend environment variables above added,
the same public blank-page probe passed once (exit 0, three seconds). Actual
WebKit version 26.5 created a page and returned the local content. This proves
that the scoped EGL/vendor/GBM ABI supports that blank operation; it is not
application or three-engine acceptance. Nonfatal automation-context, EGL device
and ZINK incompatible-driver warnings remain in the full log. No render,
version, sandbox or host-validation overrides were introduced. Browser exit 0
and owned temporary cleanup were recorded; the parent found no remaining
MiniBrowser/WPE process. No operation remains running, and no blind retry ran.

New receipts: sibling `webkit-diagnosis/mesa-probe/{mesa-build.receipt,
probe.receipt,probe.log,mesa-hashes.txt,mesa-requisites.txt}`. The same exact
environment was sent to lead and implementer1. The later final package proof
above passed the unchanged Chromium adapter and all-three-engine native-UMD cases
with this scoped environment after affected review and explicit verification
release. No owned process remained at completion; the utility slot was released.

### Feature branch publication

After explicit lead authorization, a fresh SSH fetch confirmed master remained
`c14e7d31`. The complete final history and binary final diff exactly match the
accepted bridge review artifacts; head/tree were unchanged, with no migrations
or dependency/generated-stream changes. Supported comparison capture succeeded:
`dev-session worktree capture-comparison 2026-10-19-haveapi-async-client haveapi --as-is`,
base `c14e7d3158b91c134c2817b489cd29772fc09f82`, head
`76f190f9561eabee3414919ddd26e62e48c43f58`.

Normal top-level Nix SSH push created the feature branch without force:
[2026-10-19-haveapi-async-client](https://github.com/vpsfreecz/haveapi/tree/2026-10-19-haveapi-async-client).
`git ls-remote` confirmed exact head `76f190f9`; tracking is
`origin/2026-10-19-haveapi-async-client`, remote
`git@github.com:vpsfreecz/haveapi.git`. The tree/index remain clean. No PR was
created, consistent with this repository's workflow.

Exact-head push runs initially queued: clients/js `39302667511`, RuboCop
`39302667566`, i18n health `39302667599`, servers/ruby `39302667597` and release
`39302667616`. The automatic release workflow is build-only on branches; its
publish job requires a tag push. No tag, version change or package publication
was requested or performed. One fresh pinned Luna/low full-access watcher batch
(`published_haveapi_ci_watcher`) observed all five exact IDs/SHA to completion.
All five succeeded; no failed or pending runs, retries, cancellations or manual
dispatches occurred. The release publish job was skipped as expected. JS took
about 37 seconds, RuboCop 16, i18n 12, server RSpec 20–21 across its three jobs,
and release validation/build about 2 minutes 21 seconds. Monitoring itself took
about 15 seconds because the runs had already completed. Parent inspected each
job/step receipt and confirmed remote head plus local clean tree were unchanged.
The watcher ended and its utility slot was released to lead and peer.

CI boundaries are automatic branch triggers: JS workflow runs `npm test` with
Ruby 3.3/Node LTS; i18n checks translation health; RuboCop checks Ruby formatting;
server RSpec uses Ruby 3.2/3.3/3.4; build-only release validates/builds/tests the
maintained packages and performs npm smoke checks. These broader remote checks
are observed as triggered by the authorized feature push, not separate manually
selected local language suites. The branch cannot enter the tag-only publish job.

Receipts are in `bridge/publication/{push.log,publication-receipt.json,
ci-initial.json}` plus `ci/<run-id>.json` and `ci/local-status.txt` beneath the
evidence root above. [Published CI runs](https://github.com/vpsfreecz/haveapi/actions?query=branch%3A2026-10-19-haveapi-async-client)
are bound to the exact head in those receipts. Git/utility slots released.
HaveAPI is verified and published, awaiting any later merge direction. No package
release, merge, deployment or session closure occurred.

## Historical dc941578 preparation and executed checks

The remaining record is retained provenance for the prior candidate. Its old
"final" labels and commands identify that earlier checkpoint, not the current
bridge package or its pending review/verification.

Owner: implementer0. Prepared 2026-10-19 for lead/reviewer0. This is evidence and
prepared verification, not an independent review or merge-readiness conclusion.

## Exact revisions and history

- Initial session base: `cb3f39f75e8a63416388d24293f936d1db97162b`.
- SSH-fetched upstream base: `c14e7d3158b91c134c2817b489cd29772fc09f82`.
- Final HaveAPI head: `dc94157808966c12418b4009085fec237a869789`.
- Branch: `2026-10-19-haveapi-async-client`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/haveapi`.
- Origin: `git@github.com:vpsfreecz/haveapi.git`.
- After fetch/rebase: zero upstream-only commits, four feature-only commits.
  Tracked worktree/index clean after final build/pack; diff whitespace check passes.

Complete original-base series, oldest first:

| Commit | Purpose and disposition |
| --- | --- |
| `82c9e778d04e0228785413a515e9ca76b2956215` | Upstream release automation, retained without rewriting |
| `c14e7d3158b91c134c2817b489cd29772fc09f82` | Upstream release documentation, retained without rewriting |
| `34f431e76d52508233a1753eab1bd7d096b54f19` | Independent original-bundle callback compatibility fixture |
| `90722e09a7fa25af518a26f36abd02bb0156c9a3` | Checked callback TypeScript conversion/build/declarations; includes necessary release-tool authored-source path fix |
| `8e331fe97819ad0a6591c754aaa270152c8d7564` | Shared pure core and independent additive AsyncClient/resources/tests/docs, including narrow R1/R2/R3 remediation |
| `dc94157808966c12418b4009085fec237a869789` | Repository guidance for TypeScript source/generated output |

The feature-review range is `c14e7d3..dc941578`; the full session provenance range
is `cb3f39f..dc941578`. Original-base final diff: 133 rename-aware paths,
13,677 insertions and 3,584 deletions. Feature-only final diff: 121 rename-aware
paths, 12,522 insertions and 3,513 deletions.

Normal Nix/Overcommit rebase completed without conflicts. The original
`ad34c196 / bbb923eb / a8f6e675 / 6302642d` boundaries were preserved.
Range-diff shows identical fixture/guidance patches; callback/async package
hunks retain upstream repository URL/directory context. The only substantive
addition during rebase preparation is the lead-approved source-path repair:
`Makefile:42` and `utils/release/artifacts.rb:71` use `client.ts`, with a
mismatched-TS-source-version regression in the existing release spec. It is
folded into the owning unmerged migration commit. No version action ran.
HaveapiI18n, RuboCop and normal commit hooks passed; no bypass was used.

Lead reported full final review complete at
`ae0fe39738c3eb10019377d0fce95dc249cdfd16`: no Blocking findings; Important
R1/R2/R3 were released as bounded remediation. The final reviewed-head delta is
14 paths, 493 insertions and 35 deletions. Entity-valued Resource inputs now
retain local references until normalization (peer R1); async coercion invokes
the unchanged shared coercer once per field and validates the full map once
(R2); validated raw response receipts survive metadata/payload/namespace
failures so definitely accepted creates cannot repeat (R3). Shared callback
Parameters/action/validator sources are unchanged. No public-interface expansion,
new validation policy or ambiguous-network success classification was added.

The cohesive narrow fixup was folded into the owning async commit with normal
Nix/Overcommit hooks. Fixture and TS migration commits are unchanged. A fresh SSH
fetch before final freeze confirmed upstream still at `c14e7d3`; no additional
upstream rebase was needed. `reviewed-to-final.diff` and
`reviewed-to-final-range-diff.txt` preserve the exact delta. Lead directly
accepted the committed narrow fixes before integration. No redundant independent
review rerun was requested for these approved narrow fixes.

## Final-diff scope and update streams

Feature changes comprise `clients/js` source/build/package/declarations/tests/
guides, the scoped root `AGENTS.md` guideline, and the three release-path-fix
files above. No feature edits affect Ruby server/client, PHP/Go clients,
translations, shared VERSION, Nix inputs or GitHub workflows.

- Build dependencies form one update stream in `90722e09`: replace gulp-concat/
  gulp-umd with TypeScript 5.9.3 and Rollup ^4; add the single package lock.
  Lock resolves Rollup 4.64.10, gulp 5.0.1 and unchanged runtime dependency
  xmlhttprequest 1.8.0. Async commit changes scripts/docs/manifest, not dependency
  resolutions. There are no repeated/superseded dependency/channel-pin updates.
- Bundle/declaration regeneration occurs in two functional boundaries:
  independently buildable callback conversion and additive async behavior.
  Both are retained per lead direction so callback parity is assessable before
  async additions. These are source-associated outputs, not redundant pin-only
  refresh commits. Reviewer must independently assess this retained boundary.
- Final dist was rebuilt from the final committed sources and remained clean.
  Packed bundle and all 43 declarations match final committed bytes.
  Generated source catalog `src/haveapi/i18n_messages.js` is untouched.
- No abandoned implementation, temporary mixed-source build mode or extra
  handwritten public declarations remain. Limited runtime module cycles and
  Rollup ES5-helper top-level-this warnings remain visible, with initial-load
  and callback parity covered; they were not suppressed.

## Migration and consumption provenance

There are **no database, on-disk, server protocol or persistent-state
migrations** in the feature range. No migrations were merged, released, deployed
or consumed. Old/new clients use existing servers; rollback is the consumer
bundle/dependency and associated call-site revert, with no data rollback.

This work has not been published, merged or deployed by implementer0. The actual
candidate tarball below is a local unreleased artifact for the peer's disposable
WebUI proof. No package version was changed. Remote refs/tags do not establish a
consumer boundary requiring retention of a superseded update; none was observed.
Lead should reconcile any external consumption not visible to this implementer.

## Quick evidence

On the final remediation tree, verified before commit and byte-matched afterward:

- strict typecheck and build passed;
- callback compatibility 18/18; actual-bundle async 36/36; resource units 11/11;
- both emitted-declaration consumer configurations passed;
- existing self-contained path/query/name/OAuth2 Mocha specs 18/18;
- final committed-source build reproduced tracked outputs and pack passed;
- peer independently reran its actual-bundle Resource/save regression 14/14.

The new core regressions reproduced eight failures on the old bundle, then
passed on the fixed build. They cover all four scalar types, MFA, accumulated
type errors, cross-field validation and validated/ambiguous response boundaries.
The callback behavior control passed against both bundles. Final SHA256 values
of all 14 checked paths match the committed head.

The release-path fix passed `make release-check`, `make release-test`
(22 examples, zero failures) and `make -n version VERSION=0.29.0` under a fresh
policy watcher, exit 0 in about 15 seconds. This was a dry run, not versioning.
Runtime: Node 24.21.0, npm 11.19.0, Ruby 3.3.10.

Detailed evidence directory:
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj`.

Current final series/diffs, reviewed-to-final range/diff, checked-path hashes,
quick/build logs, final status and new pack receipts are in its `remediation/`
subdirectory. The parent retains the pre-remediation review/package evidence,
release-path checks, failure baseline logs and browser-environment receipt.
Full JS/Ruby-server integration subsequently passed as recorded below. No
browser test was launched by this package.

## Actual candidate package

- Tarball: `/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/remediation/package/haveapi-client-0.29.0.tgz`
- SHA256: `de55212e85ceb2bceac77e249272e20e1062afa8aa733df42e02eae981c094b8`
- Source head: `dc94157808966c12418b4009085fec237a869789`
- Command after final build: `npm pack --ignore-scripts --json --pack-destination /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/remediation/package`
- 50 files: UMD JS, 43 generated declarations, package metadata and linked docs;
  every relative Markdown link resolves inside the tarball; no src/build/
  node_modules content.
- main/types stay `dist/haveapi-client.js` / `dist/types/haveapi.d.ts`.
- Packed metadata has no gitHead. Source provenance is this pack-owner assertion
  plus committed-artifact byte checks, not a cryptographic source-build proof.
- Exact receipt and manifest: `package-receipt.json`, `npm-pack.json`,
  `package-files.txt`, `package.sha256` in the `remediation/` evidence directory.

The final head/tar/SHA receipt was sent to lead and implementer1 for the package
pilot. The earlier tarball for reviewed head
`ae0fe39738c3eb10019377d0fce95dc249cdfd16` remains at
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/package/haveapi-client-0.29.0.tgz`,
SHA256 `46fd526ac02d04fdbc9526c7b7e67cdde0a5cfe730cf865702a4a2b4167bf991`.
Its unchanged checksum was rechecked; it is historical, not the next test input.

## Executed full JS/Ruby-server integration

After lead's final direct acceptance, one fresh pinned Luna/low full-access
watcher ran the exact HaveAPI command below once. It passed with exit 0 in
57 seconds. Tested head `dc94157808966c12418b4009085fec237a869789` and tree
`e6abec93ed21ea2dd593c3b80f750cb7fd9b5f5b` remained unchanged and clean.

The run passed callback compatibility 18/18, async bundle 36/36, resource units
11/11, both generated-declaration consumer configurations and all 50 Mocha
cases. The Mocha cases include seven CallbackAdapter and seven AsyncAdapter
shared contracts against the actual local Ruby test API, 18 localized typed-input
cases and 18 other existing local regressions. Helper-owned test servers exited;
no matching test-server process remained at the parent check. No credentials or
production API were used. No retry, source change or unrelated language suite
was needed. The watcher ended and its single-operation slot was released.

Receipts under the parent evidence directory: `integration/full-js.log`,
`integration/full-js.exit` (0) and `integration/full-js-receipt.json`. The parent
verified the log sections/counts, final head/tree/status and absence of test
server processes before reporting to lead. The final package remains the same
committed artifact recorded above.

## Post-review commands and remaining browser verification

The HaveAPI command below has passed; the WebUI package/browser commands remain
for their owner. All uncertain/long operations use fresh policy watchers.

From the HaveAPI root, full JS including both-adapter Ruby-server contracts and
localized typed-input checks:

```sh
nix develop -c bash -c '
set -e
export BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"
bundle install
cd clients/js
npm test
'
```

This deliberately supplies the Ruby server bundle as well as Node; the
Node-only client-js shell is insufficient. The diagnostic subset, if a failure
needs isolation, is `./node_modules/.bin/mocha test/contract.spec.js
test/typed_input.spec.js` in the same environment, not an additional routine run.
The helper owns localhost test-server startup/reset/stop.

If lead selects full Ruby server regression independently, from HaveAPI root:

```sh
nix develop -c bash -c '
set -e
export BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"
bundle install
make doc
cd servers/ruby
bundle exec rspec
'
```

No other-language full suites are implied by this client-only package.

Peer-owned WebUI packed-package command from
`worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async`, after its
final source is committed/reviewed:

```sh
nix develop -c env \
  PLAYWRIGHT_BROWSERS_PATH=/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers \
  npm run test:haveapi-package -- \
  --package /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/remediation/package/haveapi-client-0.29.0.tgz \
  --webui-ref HEAD \
  --haveapi-ref dc94157808966c12418b4009085fec237a869789
```

The script snapshots the resolved committed WebUI head, installs only in its
disposable copy, compiles emitted-package declarations, Vite-builds the actual
package import and runs the Chromium adapter pilot plus the committed
ordinary-script/raw-UMD case across Chromium, Firefox and WebKit. No browser
test has run. The exact browser environment below is prepared; VM loader cases
and static library checks alone do not prove real-browser support.

### Browser runtime preparation receipt

Existing realised Nix browsers were found and retained without downloading or
installing another copy. The user-owned indirect GC root is
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers`,
pointing to
`/nix/store/bcf8w1529mgspizwjsp3iwvaq26plrgj-playwright-browsers`.

| Engine | Pinned build | Version from matching manifests |
| --- | --- | --- |
| Chromium and headless shell | 1228 | 149.0.7827.55 |
| Firefox | 1532 | 151.0 |
| WebKit | 2311 | 26.5 |
| FFmpeg | 1011 | No manifest version |

The repository CLI remains Playwright 1.61.0. The existing Nix 1.61.1 browser
manifest has identical revision and version values for all five artifacts;
only those matching browsers are used, not the Nix CLI. The WebUI locked
nixpkgs 1.59.1 browser set and HaveAPI current 1.64.1 set were inspected and
rejected because they do not match. No project pin was changed.

The existing pinned wrapper's `install --dry-run chromium firefox webkit`
resolves the selected paths. All 50 ELF executables/shared libraries checked
with `ldd` resolve without missing libraries, using only each engine's normal
wrapper environment. No host loader/library/policy edits or validation bypass
were used. All preparation checks were known quick; no uncertain installation
needed a watcher. No browser was launched, so actual engine startup/version
and fixture results remain post-review gates.

Receipts in the evidence directory: `browser-environment.json`,
`browser-preflight.log`, and `pinned-runner-browser-paths.log`. The environment
and exact command above were sent to lead and implementer1. No separate
Chromium executable override is set; the registry selects matching Nix paths
for all engines.

The final inventory preserves whole-history consolidation, retained generated
boundaries and **no migrations** for lead's reconciliation with the completed
review. Git slot is released. No integration/publication approval is supplied
by this preparation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-haveapi-async-client/

