---
lifecycle: active
---

# HaveAPI TypeScript and async client

## Current status

Implementation, independent review, local integration and package/browser
verification are complete. Both feature branches are published. HaveAPI CI is
fully green, and WebUI CI passed on the corrected commit identities. Both
branches are ready, awaiting merge approval. No further source changes are planned.

PR #74 remains open and **not draft**: the current GitHub token refuses
`convertPullRequestToDraft`, including in the original creator's context. The
user was told that GitHub's **Convert to draft** UI is needed. Do not mark it
ready automatically. This is a GitHub permission failure, not an automatic
approval rejection.

No npm release, version bump, default WebUI transport switch, merge, deployment
or session lifecycle action is authorized. Leave this session open and active.

## Phase checklist

- [x] Verify bound session identity and retained Full-team roster.
- [x] Agree design: callback Client and separate AsyncClient in one npm package.
- [x] Convert both surfaces to TypeScript; ship ordinary JS and generated types.
- [x] Preserve callback behavior and existing browser/CommonJS/AMD exports.
- [x] Implement typed requests, auth, async resources and separate completion wait.
- [x] Add the React injectable adapter and isolated actual-package proof.
- [x] Commit intended deliverables and pass quick checks.
- [x] Complete independent final and affected-lane reviews; resolve findings.
- [x] Pass final Ruby-server-backed JS and real-browser package checks.
- [x] Publish HaveAPI branch and pass all five CI workflows.
- [x] Publish WebUI branch and required PR #74.
- [x] Rewrite WebUI commit authors/committers as explicitly requested by user.
- [x] Finish CI on the rewritten WebUI head (both workflows/all six jobs pass).
- [ ] Draft PR #74: blocked by current token permission; user informed.
- [x] Final handoff with CI result and remaining release/integration limits.

## Repositories and exact heads

| Repository | Feature branch | Base | Current head |
| --- | --- | --- | --- |
| HaveAPI | `2026-10-19-haveapi-async-client` | `c14e7d3158b91c134c2817b489cd29772fc09f82` | `76f190f9561eabee3414919ddd26e62e48c43f58` |
| React WebUI | `dev/haveapi-async-client` | `7860521f30826c3886c89c35e8ab6f4e082e0a4b` | `5dd2333b9af230d4a81c8f772cbbb08d39b14913` |

Worktrees are beneath `worktrees/2026-10-19-haveapi-async-client/`: `haveapi`
and `vpsadmin-webui-async`. The initial read-only `vpsadmin-webui` worktree
remains unedited at its initial base; do not remove it without authorization.

HaveAPI branch:
https://github.com/vpsfreecz/haveapi/tree/2026-10-19-haveapi-async-client

WebUI PR:
https://github.com/vpsfreecz/vpsadmin-webui/pull/74

HaveAPI's original session base was `cb3f39f75e8a63416388d24293f936d1db97162b`.
Its two later upstream release commits were preserved. Final four feature
commits are fixture `34f431e`, callback TS migration `0e63360`, async `81994d2`,
and source guidance `76f190f`. The independent reviewer accepted the complete
series, coherent generated outputs at both source stages, single dependency
stream and no-migration conclusion.

WebUI's final two commits are pilot
`0d05a2584bf30ee4acfa1d64bf00325cdda62934` and evidence
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`. Both author and committer are
`Jakub Skokan <jakub.skokan@havefun.cz>`. The user explicitly authorized rewriting
these published commits. All paired trees, messages, patches and the complete
head tree match the former `1ef5b7b0` / `72b852df` commits. The update used an
explicit force-with-lease against the verified previous remote head. Main and
AGENTS were unchanged. The user confirmed that the erroneous Michal Janoušek
identity rule will be corrected by Kerrycek.

Both source trees were verified clean, and supported comparison captures were
updated. The final evidence-only WebUI commit changes just its dated work log;
all 2,307 other tracked blobs match the browser-tested source commit.

## Verification and review

- Final HaveAPI full JS suite against a real local Ruby test API passed:
  callback 26, async 36, resource units 11, both emitted declaration consumers,
  and Mocha 50 (including both adapters' seven contract cases and typed input).
  This is not a claim of a full local Ruby RSpec run.
- Full WebUI unit suite passed: 301 files / 1,867 tests; production build passed.
  Later runner/fixture/evidence and author-only changes preserve normal app
  source, with focused checks and explicit equivalence receipts.
- Final actual npm tarball proof passed generated declarations, a minified Vite
  named import, four Chromium adapter cases and one ordinary UMD callback/async
  native-XHR case in each of Chromium, Firefox and WebKit. No skips or retries.
- Actual browsers: Chromium 149.0.7827.55, Firefox 151.0, WebKit 26.5.
  Node 24.21.0, npm 11.19.0, TypeScript 5.9.3, Vite 7.3.5, Playwright 1.61.0.
- All 407 installed baseline dependencies and manifest/lock hashes stayed
  unchanged in the disposable proof. Production dependencies and fetch default
  are unchanged. BFF identity is synthetic and treated as already validated;
  this does not certify real OAuth/bootstrap, deployed API permissions or VPS
  lifecycle completion.
- Final tar SHA256:
  `6efa9263f79c999f1efa11014d4674b0cfb8bab07afb4dfaab6e93193040c123`.
  It has 51 files / 44 declarations; packed bytes equal committed artifacts.
  Path: `/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/bridge/package/haveapi-client-0.29.0.tgz`.
- Full and affected review used independent retained reviewer0,
  `gpt-6.1-sol` / xhigh / read_only. The initial three Important findings were
  fixed and directly checked. A later strict-module bridge received affected
  general/architecture/risk review with no findings. No migrations or obsolete
  branch/pin history remain. Scope and compatibility conclusions are recorded
  in the review ledger.

See [verification-results.md](verification-results.md),
[review-findings.md](review-findings.md),
[bridge-review-packet.md](bridge-review-packet.md), and
[haveapi-review-inventory.md](haveapi-review-inventory.md). Original failed
proofs/traces, source and package receipts remain preserved. Matching browser
artifacts and scoped Mesa EGL/GBM paths solved WebKit's pre-application runtime
failure; no host configuration or validation bypass was used.

## Final CI and ownership

HaveAPI's five exact-head workflows all passed: JS `39302667511`, RuboCop
`39302667566`, i18n `39302667599`, Ruby matrix `39302667597`, and build-only
release `39302667616`. The publishing job was skipped. No tags or registries
were written.

Corrected WebUI head `5dd2333b` passed both workflows: `39306325205` (CI: required
nonbrowser checks, production build, Chromium script regression) and
`39306325290` (Playwright: Chromium, mobile Chrome, mobile WebKit). All six jobs
passed. Fresh Luna/low watcher completed normally after 1,434.96 seconds; no
watcher or remote run remains active. Final parent remote/PR/status readback
confirms exact head, clean tree/index, main unchanged, both identities corrected.
Receipts are copied to evidence/final-ci/.

Old CI `39303472764` succeeded. Only superseded active smoke `39303472803` was
cancelled after the authorized metadata-only force update. That cancellation is
supersession, not a source/test failure. No blind retry or current-run cancellation.

All Git and utility slots are released. Owners remain architect0 (design),
implementer0 (HaveAPI/build), implementer1 (resources/WebUI), reviewer0 (independent
review), lead (coordination/writing/tracking). Implementation, review, verification,
feature publication and CI are complete. No source work remains. Draft conversion
is the sole unmet requested action and needs GitHub permission unavailable to the
current token. Do not change auth or mark ready. Keep branches and session open;
integration still requires explicit user direction.

## Remaining limits

- Draft conversion requires GitHub permission unavailable to the current token.
- Supported Node minimum is a release prerequisite; Node 24.21.0 was tested.
- The portal's retained WebUI default-branch label says master although the
  actual target is main. Remote HEAD was corrected; supported registration
  metadata correction remains separate before eventual integration.
- The shared WebUI Git-config regression was repaired: worktreeConfig extension
  restored absent, common repository still bare, both owned worktrees usable.
  Use command-scoped identity for future commits; do not change shared identity.

## Documentation and portal

Design and decisions: [design.md](design.md). Durable component guides ship in
HaveAPI's package; WebUI has its pilot guide and dated work-log evidence.
Session records/receipts are under this directory, with reusable lessons in
`notes/haveapi/2026-10-19-umd-strict-consumers.md`.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-haveapi-async-client/
