# Affected-lane review: strict-module legacy globals

Final committed candidate ready; intended source changes complete and quick
gates pass. No long integration of this revised source started. Same independent
reviewer0, saved Sol/xhigh/read_only. Overall HIGH risk; affected lanes general,
architecture/repetition and risk/compatibility. Scope lane conclusions from the
original review retained; no generalized mechanism or product contract expansion.
Original full review: review-packet.md and review-findings.md. Final R1/R2/R3
narrow direct fixes remain accepted. Read updated architect design.md.

## Concrete failure and correction

Actual React packed candidate imports/builds in Vite but all Chromium adapter
cases fail module startup: Authentication is not defined. The callback migration
intentionally retained bare legacy global writes via erased TS declarations.
Raw sloppy UMD works (Chromium/Firefox actual native-XHR smoke pass); Vite embeds
it in strict ESM where bare assignment fails. Known ret/v1/v2 writes on later
callback paths are affected as well.

Accepted source bridge is internal and finite: Authentication/ret/v1/v2 access
actual host global properties, preserving live reads/registry identity/timing,
exports, callbacks, undefined returns and local behavior. Guard globalThis with
browser/worker/Node fallbacks; no new requirement, eval/Function, new entrypoint,
minification disable or WebUI workaround. UMD loader shell/strict:false remain.
Authentication module evaluation order retained. Unreachable opts untouched.

Owner0 edits helper and callback auth/client/resource_instance/build outputs;
peer1 adds independent strict-wrapper compatibility fixture/test docs. No new
WebUI application source or dependency pin. Source fix folded into TS migration
with generated callback-only and later async bundle/type stages kept coherent.

## Evidence before final commit

Original bundle strict8 fixture: raw4 pass/strict4 Authentication failures.
New exact built bundle: independent8/8 pass, plus callback26/async36/resource11,
both emitted type consumers and Mocha18 focused checks. Tests cover actual UMD
inside strict wrapper, setup/version checks, defaultParams ret, live global
registry replacement/direct authenticate/registerProvider and fallback contexts
without globalThis/Promise/AbortController. Self fallback uses fake CommonJS XHR,
not a claim of native worker transport. Real minified named import remains an
actual post-review acceptance gate.

Main-agent test README writing pass complete. No callback Parameters behavior
change. No migration/state/protocol/dependency/channel-pin change. All old local
tarballs retained as test evidence, not supported external release boundaries.
No registry publication, merge, deploy or lifecycle operation authorized.

## Independent conclusions requested

Inspect final committed source/diff and complete rewritten series, including
coherent source-associated outputs at both stages. Confirm original history/
stream/no-migration conclusions continue to hold and no obsolete bridge iteration
remains. Check preserved observable globals/live reads/module order and fallback
semantics, strict-context correctness and representative tests. Report only
concrete Blocking/Important/Advisory findings with lane/path/commit and residual
risks. Stay read-only; no nested reviewers or long integration/browser runs.

Final base/head/series/source delta/package receipt will be appended before
assignment. Actual WebKit environment failure is separate: matching runtime
cannot create EGL display before loading app. User-scoped matching graphics
libraries are being prepared; no host-validation bypass, unsupported engine or
product flag is part of this source review.


## Exact final candidate

HaveAPI worktree worktrees/2026-10-19-haveapi-async-client/haveapi.
Target/base master c14e7d3158b91c134c2817b489cd29772fc09f82 (fresh SSH unchanged).
Head76f190f9561eabee3414919ddd26e62e48c43f58, checked tree
157489d9351dae3ff669ee8f4827d272b99d22f7, clean index/tree/full-diff whitespace.

Complete series:

1.34f431e76d52508233a1753eab1bd7d096b54f19 original callback fixture unchanged.
2.0e63360e46a40dcbe744d7ee7475fb0151f8d37b callback TS migration with bridge.
3.81994d25cf6dc50754a7e9b2820aafc8fa00f0e2 async/source-associated output.
4.76f190f9561eabee3414919ddd26e62e48c43f58 source guidance unchanged patch.

Prior original full reviewed head ae0fe397, R1-R3 direct-fix head dc941578;
bridge old dc941->new delta exactly9 paths/+240-35. Source helper + callback
three modules, generated bundle/client/internal helper declarations, strict
fixture and test README only. No async feature source/dependency change.
Whole series/range-diff/full finaldiff and checked final package receipts in
evidence/bridge/ and haveapi-review-inventory.md. Preserve original reviewed
packet; this is affected mechanism/history review, not redundant full review.

Callback-only stage was regenerated/build checked (25 compatibility tests and
callback declarations); later async stage regenerated/build checked (26 tests,
both declarations); final combined gates26callback/36async/11resource/bothtypes/
18localMocha. Peer strict8 independently passes exact actual bundle. Final
rewritten tree equals checked checkpoint; normal Nix hooks passed. Original
independent final review's no-migration/single dependency stream/source-associated
output conclusions must be explicitly reconciled with the rewritten series.
No supported external package/release/state boundary; local test tarballs only.

New tar: /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/bridge/package/haveapi-client-0.29.0.tgz.
SHA2566efa9263f79c999f1efa11014d4674b0cfb8bab07afb4dfaab6e93193040c123,
55288bytes,51files/44declarations, every packed file equals committed source
artifact, guide links present, no src/build/node_modules. Old tars retained.

WebUI remains clean at fbf2a7f70f145a1bb87f659e68c84df0245448c3 on7860521f.
Its original reviewed e35 pilot + narrowly directly accepted lock/cwd runner fixes
are recorded in review-findings/evidence. No new WebUI edit for bridge. No need
to repeat unrelated lanes; inspect actual minified Vite failure evidence and
prepared unchanged named-import fixture as necessary for bridge assessment.

Do not launch browsers/server integration in review. WebKit blank-page diagnosis
isolated missing WPE EGL implementation before any app; scoped vendor library
proposal is separate environment-only work, no source or validation bypass.
After this review, rerun full HaveAPI JS/server suite due changed callback
source and then final actual package proof with pinned tools in real browsers.
