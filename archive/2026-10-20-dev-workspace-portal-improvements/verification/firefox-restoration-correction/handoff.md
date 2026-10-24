# Firefox restoration synchronization correction

Published B head: `3671c7901a9337d70fee0a48e2b3094926488a84` on
`2026-10-20-dev-workspace-portal-improvements`, SSH exact force-with-lease
from `d617ef3968280e9955da85e2d7464a47030e7087`. Remote master remains
`968646471b1190c16a8cf60ff50736cd0525fa3f`. Worktree and index are clean.
[Publication proof](publication-proof.json) and [remote receipt](post-push-remote.txt).
Local safety ref `safety/2026-10-20-portal-firefox-restoration-d617ef39`
retains the exact pre-correction head. All prior receipts and launchers remain
unchanged.

## Scope and evidence

The failed first-run restored-stream assertion lacked an ordering dependency on
asynchronous EventSource startup. An enabled composer and quiescent hidden tabs
could both precede the restored tab's first stream. The failure log did not
establish whether startup was late or product recovery remained broken; canceled
reads and the uncorrelated TLS handshake were not established causes.

Only four test paths changed: the native Firefox acceptance runner, its tiny
fixture-specific readiness helper, eight deterministic helper regressions and
Go regression wiring. The actual fixture invokes the helper once. A counter
snapshot immediately before native discard supplies the new-stream baseline.
After genuine native unload/restoration, expected tab identity, real visible
state and native pending-cleared/selected proof, the helper requires Count above
that baseline and exactly one active SSE within the existing 20-second budget.
A successful status first observed after the deadline is rejected. The existing
10-second status-request timeout is unchanged. Existing zero-other-hidden checks
and all later question, real read retry, retained draft and single durable
dispatch assertions remain. No browser navigation/reload substitutes for native
restoration.

Failure output now preserves fixed stage, observed native/visibility state and
bounded counters before owned cleanup, with previous counters retained if the
last status read fails. It contains no raw URLs, profile data or browser contents.
No production source, assets, TLS behavior, native code, API, schema, pins or
product prose changed. No product documentation update is useful: this corrects
test synchronization within the existing documented acceptance contract. Helper
comments and regressions explain the technical reason.

## Quick checks

All checks ran in B's Nix environment, without real browser/full-suite/package
checks or an extra utility:

- Node syntax for all three CJS paths; Go formatting; staged and whole-range
  whitespace: PASS.
- Eight deterministic readiness cases: 8/8 PASS, 204.938 ms. Delayed stream,
  unchanged counter, overlapping streams, absent/inactive stream, missing
  counters, transport failure and post-deadline arrival are covered.
- Tracking-only negative control substituted the old immediate Count assertion
  into the same cases: expected exit 1, observed exit 1, seven failures. The
  delayed-stream case fails under the old assertion.
- `TestFirefoxFixtureJournalReconcilesOriginalAttempt` and
  `TestFirefoxFixtureReadiness`: PASS, Go total 0.377 s. Go wiring also runs the
  Node readiness cases.

Logs: [Node](quick-node.log), [Go](quick-go.log),
[old-assert negative control](negative-old-assert.log). There is no declared hook
framework or installed pre-commit hook in B. The ordinary Nix-environment commit
ran with no hook bypass.

## Fold and exact-source proof

[Source proof](source-proof.json), [bounded final delta](bounded-final.patch),
[complete final range](complete-final-range.patch) and
[range diff](range-diff.txt) bind the result. Fifteen logical groups remain,
with no standalone fixup. The owning Firefox fixture group changed from
`3435e1be56cc938ff297acad85b3d184879daf33` to
`ef8453963868d77b30028cf2963b4cda00bcc0c3`. Fourteen of fifteen stable patch IDs
are identical. The two later group IDs changed only through reparenting; their
patch IDs match. The first twelve commit IDs are unchanged.

The final tree `61816fac1b093703681f555bf7e6e07f5827d1b2` exactly equals the
quick-tested pre-fold tree. Every final file equals the immutable candidate.
All 525 tree entries outside the four approved test paths have identical Git
blob/mode metadata to Bd617, covering every production source, asset, dependency,
configuration and documentation entry. No migrations or persisted formats
changed; existing reviewed no-migration conclusions remain applicable.

The parent accepted this bounded correction for direct narrow-fix verification.
This handoff does not claim a new independent full review, package build or real
Firefox acceptance. Earlier Bd617 receipts retain their original tested identity.

## Next owner

B source/index/Git are released clean to the lead after this report. The parent
owns direct final acceptance, downstream pin/guard closure and a fresh Luna
real50 native Firefox rerun. A persistent no-stream result must go to the product
owner/architect with the new evidence before any application patch.

CI was queried once only to identify superseded active runs after the force-push;
none existed. Current-head Check run `39657466104` was in progress at that query;
it was neither canceled nor awaited. No live session, claim, deployment, machine
reservation or lifecycle action occurred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
