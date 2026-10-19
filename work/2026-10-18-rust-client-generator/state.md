---
lifecycle: active
---

# Rust HaveAPI generator and vpsAdmin client

Ready, awaiting merge approval. Implementation, independent review, all local
acceptance gates and exact-head CI passed. Both feature branches are published;
no feature has entered a default branch, been released or deployed.

## Phase checklist

- [x] Design: embedded runtime, async default and optional blocking, API 7.0.
- [x] Generator/runtime, actual generated client and disposable fixtures implemented.
- [x] Quick checks and independent four-lane review; R1/R2 remediations complete.
- [x] DELETE JSON correction, affected-lane review and corrected verification.
- [x] Runtime default/blocking tests and strict Clippy.
- [x] Actual client default/blocking tests, examples, docs and Cargo package.
- [x] Rust 1.95 with the committed lockfile in both feature modes.
- [x] Extracted generator gem reproduces all generated Rust and manifest.
- [x] Real/scripted HaveAPI suite at root and mounted paths, both modes.
- [x] Actual disposable vpsAdmin tests: VPS show/update/paging, DNS null, Custom,
      token request/use/renew/revoke and expected authentication failures.
- [x] Public read-only async/blocking public_stats smoke, HTTP 200 in both modes.
- [x] Final three/two logical commit histories and source/provenance consolidation.
- [x] Independent final history/rebase/input-equivalence addendum: no new findings.
- [x] Publish both feature branches; all six exact-head CI workflows passed.
- [ ] Explicit user direction for default-branch integration; not authorized.

## Repositories and final heads

| Repository | Branch and worktree | Final head and base |
| --- | --- | --- |
| HaveAPI | 2026-10-18-rust-client-generator; worktrees/2026-10-18-rust-client-generator/haveapi | 9e4c29a0412a25256ce944641f60ba13e9f03c2b; comparison base 526648131af45df68c25ac0042a52f22c7a81df5 |
| vpsadmin-rust-client | same branch; worktrees/2026-10-18-rust-client-generator/vpsadmin-rust-client | 62753f006d7bd3e5befe1033c49a2c630ca3ff02; neutral empty root b67a3ba5eef89b2bd6533050aa8769aaa0574114 |
| vpsAdmin | fixture-only same-session checkout; worktrees/2026-10-18-rust-client-generator/vpsadmin | unchanged fb2f51222503a45f2e5a42af505f719e44279ed0; no application edits |

HaveAPI initial registered base c14e7d3158b91c134c2817b489cd29772fc09f82 is
preserved. Final feature commits: runtime 930a5f3, generator 8701baa, fixtures 9e4c29a.
The rebase onto 5266481 adds only two unrelated upstream release-tool files;
three patches are equivalent, no conflicts or feature source edits.
Client commits: handwritten f88d86a, generated 62753f0. All corrections and
provenance refreshes are folded into their owners. No migrations, obsolete
shims/fixups, repeated dependency streams or consumed intermediate state.

Both feature branches are now published. The new repository main points only
to neutral empty rootb67a3ba and is verified as its GitHub default; the feature
points exactly to62753f0. HaveAPI feature points exactly to9e4c29a. No default
feature integration was performed.

## Contract and provenance

Crate vpsadmin-client, Rust edition 2024, MSRV 1.95; embedded maintained runtime,
no separate runtime dependency. Public snapshot profile public-live-api-7.0,
protocol 2.0, 152 resources/524 actions/8720 parameters. Plugin completeness unknown.
Schema SHA256 70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d.
Runtime SHA256 9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739.
API version alone selects compatibility. GET uses query input; DELETE and other
supported body methods use JSON. No automatic mutation retries or auth refresh.

## Reviews and verification

Original review: reviewer0, retained Sol/xhigh/read_only, all four lanes,
two Important findings (reserved-name collisions, locked-bundle activation),
fixed and folded. DELETE correction received another four-lane review with no
new findings. The same reviewer accepted final cleaned histories and rebase/input equivalence
with no new findings; exact reports are linked below.

All local gates passed. Corrected runtime/client/MSRV/package receipts are bound
to tested e9173e20/1a818c4; generic root/mounted to 3aaf7cf; full actual vpsAdmin
to 41bbb37/client 7279dd9. Final component sources, locks, flake derivations and
compiler identities match their scopes. Final client differs from passing 7279
only in one provenance revision line. No archive byte hash equivalence is claimed;
CI also verified the exact final head.

- [Verification summary](verification-summary.md)
- [Original review](final-review.md)
- [DELETE correction review](final-review-delete.md)
- [Final history packet](review-packet-final-history.md)
- [Accepted final history addendum](final-review-history.md)
- [Source history](haveapi-final-history.md)
- [Source input receipt](haveapi-final-input-receipt.json)
- [Client history](client-final-history.md)
- [Client input receipt](client-final-input-receipt.json)
- [Actual vpsAdmin pass](artifacts/vpsadmin-token-prereq/watcher-result.txt)
- [Final CI results](artifacts/final-ci/final-summary.json)
- [Detailed earlier checkpoints](progress-history.md)

No production mutation or credentialed production request occurred. Public live
verification made two unauthenticated public_stats GET requests. Actual updates
and token actions ran only against a fresh private database and loopback API.
Owned fixture processes/databases were cleaned by their wrappers.

## Owners and next action

Implementer0 owns runtime; implementer1 generator/tooling/history/publication;
implementer2 fixtures; implementer3 actual client; reviewer0 independent review.
Lead accepts evidence, coordinates Git/verification and maintains tracking.
Both feature publications completed; remote heads and clean worktrees verified.
HaveAPI9e4c29a and client62753f0 are the exact published heads.
A fresh Luna/low watcher completed all six exact-head workflow observations:
every workflow passed, with release publication correctly skipped. No operation
remains active. No known verification blocker remains. Next action is explicit
user direction to integrate HaveAPI into master and the client into main;
neither integration is authorized yet. Keep the session and branches open.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-rust-client-generator/


## Published branches and passed CI

- HaveAPI: https://github.com/vpsfreecz/haveapi/tree/2026-10-18-rust-client-generator
- Client: https://github.com/vpsfreecz/vpsadmin-rust-client/tree/2026-10-18-rust-client-generator

| Workflow | Result |
| --- | --- |
| [HaveAPI Rust](https://github.com/vpsfreecz/haveapi/actions/runs/39310683647) | Passed |
| [HaveAPI RuboCop](https://github.com/vpsfreecz/haveapi/actions/runs/39310683493) | Passed |
| [HaveAPI build](https://github.com/vpsfreecz/haveapi/actions/runs/39310683496) | Passed; publication skipped |
| [HaveAPI server RSpec](https://github.com/vpsfreecz/haveapi/actions/runs/39310683502) | Passed |
| [HaveAPI i18n](https://github.com/vpsfreecz/haveapi/actions/runs/39310683509) | Passed |
| [Client](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/39310893770) | Passed: async, blocking, MSRV, regeneration |

Retained Luna/low utility thread 01a155a0-480a-7b63-ad77-7f3ae8518210 completed
read-only monitoring without retries, cancellations or dispatch. Results bind
the exact final heads above, with no active authorized workflow remaining.

Both portal comparisons captured at final heads. HaveAPI base5266481/head9e4c29a;
client exact recorded neutralbaseb67/head62753f0. Automatic client capture could
not resolve its newly born remote base locally, so explicit known registered
base/head were supplied (not guessed), and capture succeeded. Initial bootstrap
fetch similarly reported unbornremoteHEAD before explicitzero-refcheck; no
unexpectedref or featuredefaultpush occurred.
