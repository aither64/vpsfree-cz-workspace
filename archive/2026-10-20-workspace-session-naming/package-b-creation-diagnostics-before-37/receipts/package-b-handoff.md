# Current package B handoff

Published and frozen at `37a87a8a81cd3c705b7c5ee4f39338c1db1cc6ce`, clean source
tree `149b827753359c9ea9f140895b77dbac2f630f31`. Main accepted affected final
review with no findings in all four lanes. Main's fresh Luna six-check batch owns
frozen A6e469/B37 verification. This artifact-only reconciliation performs no
compilation, tests, generation, source/ref change, CI poll or live call.

Repository: `git@github.com:aither64/dev-workspace.git`; own worktree
`worktrees/2026-10-20-workspace-session-naming/dev-workspace`, feature
`2026-10-20-workspace-session-naming`. Current baseline remains deployed
`b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`. No default integration or activation
has occurred in this package's execution. C owner is released for one mechanical
refresh; C publication/composition evidence remains with its owner and main.

## Exact source and accepted review

Runtime source `/nix/store/d4l45ifray9zd5mw7g5i472dfp9nbif3-source`, NAR
`sha256-jzlNJ4RgAYPZVNlku3lBy4fcp9R2nf9QEyNU7uedbSM=`. This reuses owner0's
existing [C source receipt](package-c-forward-2026-10-24/runtime-37-source.json),
without generating or compiling anything again. Current expected identities and
receipt hash are in [package-b-current-source.json](package-b-current-source.json).

A remains exactly `6e469863a69c7d35941ca2e15de9514223b58f4f`, NAR
`sha256-qji0vZYo7sxR+cBxhYksk0oBQXXhTCZuCkLi5VNfmlQ=`, Go module
`v0.0.0-20261024195456-6e469863a69c`, no replacement. All five pin/hash files
are unchanged after556; vendor hash remains
`sha256-HjUyLpUfNyEbNZ3Kx1y4tnFbVcjlQq8bc8yBTluoS/E=`.

- [Original full forward review](forward-review-20261024/review.md) covers A6e469,
  B556 and its then-selected C ranges; its conclusions remain bounded to that
  content and its exact revisions.
- [Accepted B37 affected review](forward-review-20261024/cancellation-review.md)
  covers the556→37 delta, final tree149b and complete current B history in all
  four lanes, with no Blocking, Important or Advisory findings. It confirms the
  original review remains applicable to unchanged content.
- [Correction handoff](package-b-forward-fast-ci-handoff.md) and
  [failure diagnosis](package-b-forward-fast-ci-diagnosis.md) retain original
  failed-job/raw evidence, causal limits, scope and quick evidence.

## Complete final history and preservation

Exactly four commits above b3:

1. `29d64ff4da4ba7f5e5856418b9049a82f14f8ee6` — single dependency-first stream.
2. `024f4b0e05e2fa918818610fbeb52acaa45a79e6` — naming/manual recovery owner.
3. `556a6e51b141fa419d620ad0d4ccd629fd2be6f5` — retained archive diagnostics.
4. `37a87a8a81cd3c705b7c5ee4f39338c1db1cc6ce` — separate baseline observation
   error correction, preserving cancellation alongside transport/error causes.

The original three commits and all18 prior feature paths are byte-identical.
Only three correction paths were added/changed afterward. The complete current
base-to-head diff has21 paths. Of90 originally preserved newer-baseline blobs,
**88 remain exact**; the two intentionally corrected blobs are
`portal/internal/workspacecodex/client.go` and its existing fixture
`client_test.go`. New regression coverage is in `loaded_retirement_test.go`.
The upstream attention synchronization, retry/policy state readers and writers,
runtime schema-1 capabilities, admission/deletion recovery, descriptor limit,
native/catalog/provider policy and deployment contracts remain preserved.

Old915 remains omitted as semantically redundant with the upstream2s explicit
stage/diagnostic implementation; no literal patch-equivalence claim is made.
Original naming and archive patches remain range-diff equivalent, with one
consolidated dependency stream. The fourth commit owns the separately exposed
baseline failure. No repeated pins or obsolete approaches remain.

**No migrations, new persisted format, wire format or public API change.**
Existing reserved identities/old preparation records and deployed retry/policy
state keep their supported contracts. Prior undeployed iterations remain
provenance. B556 remains an ancestor; older original naming history was
reconstructed rather than literally merged.

Full history, current diff, owning delta, old/new ranges and exact preservation
proof are the `package-b-forward-fast-ci-{final-history.txt,final-diff.txt,owning.diff,range-diff.txt,old-to-final-range-diff.txt,final-proof.json}`
artifacts. The saved portal comparison binds b3..37.

## Behavior, documentation and focused evidence

Naming retains one30s deadline before queue admission, two held operation slots,
at most two safely proved utility calls, frozen provider/input/settings,200ms
cancelable backoff and the1s+250ms remaining admission threshold. Ultimate failure
stops before base/slug/handoff allocation and reuses saved-input retry/manual
controls. Generic success fallback and attachment-only placeholders are removed.
The three owning docs retain main's accepted wording and newer recovery sections.

B37 changes only failed read-only loaded-list/metadata observations: canceled
context and original error remain discoverable through errors.Is/As. Active
errors keep identity. Successful observations, archive proofs, mutation receipts
and attempt clearing retain their previous handling. Existing unsafe-evidence
assertions are unchanged; no product prose was added.

- [Final focused result](package-b-forward-fast-ci-focused-result.json):16 top-level
  tests and73 test/subtest passes,5.694s package time, final tree149b. Complete
  output: [focused log](package-b-forward-fast-ci-focused.log).
- [Controlled red result](package-b-forward-fast-ci-red-result.json): removing only
  the two normalization blocks while retaining the private seam fails all four
  canceled list/metadata transport/generic cases. [Red output](package-b-forward-fast-ci-red.log).
  This is old-behavior regression proof, not an unmodified old-tree run.
- Naming/preparation36.625s, admission/fork5.963s, attention71/71, fixture/helper
  checks and overlay compile0.043s belong to original forward B556, treecd57256.
  Their exact logs/results and original source expectations remain preserved;
  they are not fresh B37 long/native or overlay-compilation proof.

Original B556 forward/handoff/smoke expectations were copied before this update
into `package-b-before-current-37-reconciliation/` with a SHA manifest. The earlier
36-file pre-fix source/review snapshot and complete pre-forward163-file evidence
snapshot also remain intact. Original forward/full-review receipts are unchanged.

## Remaining verification and smoke limits

Main owns the fresh six-check batch and its results; this package does not
execute, duplicate or poll it. Main reports A6e469 native success separately;
that does not certify B37 runtime checks. CI status is bounded by the earlier
20:37:35Z snapshot in `package-b-forward-fast-ci-postpush-snapshot.json`;
no fresh CI query/wait/trigger/rerun was made for reconciliation.

[Current live smoke recipe](package-b-live-naming-smoke.md) now expects exact B37
and A6e469 and reuses owner0's immutable source receipt. It preserves original556
compilation evidence as historical. Main may execute the helper/backend smoke
after authorized activation under machine ownership, binding deployed profile
and build/input receipts first. It uses service `vpsfree-cz`, all-thread child
ownership discovery and the discovered provider. It bypasses HTTP admission and
the provider-resolution wrapper; it creates no registered session and has no
session lifecycle cleanup. No live discovery/inference has been performed here.

Collection-plan rebind remains architect-owned. Its custom-name portal
admission/handoff and preparation/switch exclusion scope stays separate from
usable native conversation readiness and packaged creation. Main retains all
review/verification/activation/merge/lifecycle decisions. B follow-up ownership
remains with implementer1; the session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/
