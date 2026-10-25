# B retirement cancellation correction handoff

Published exact `37a87a8a81cd3c705b7c5ee4f39338c1db1cc6ce`; clean own worktree,
source/refs frozen pending main's affected independent review. Ordinary SSH
fast-forward from reviewed556; no rewrite. Exact checked/final tree:
`149b827753359c9ea9f140895b77dbac2f630f31`.

This additive packet supersedes556 only for the narrow baseline cancellation
correction. Original forward/source/review/check receipts remain untouched.
All were copied before edits to `package-b-forward-fast-ci-before-fix-556/`
with a verified36-file SHA manifest. Main owns shared state and review/long checks;
C remains unchanged until main releases its dependent update.

## Evidence and corrected behavior

Exact fast job120973723284 in run40128088687 failed
`TestRetireThreadLoadedDiscoveryRefusesUnsafeEvidence/cancel` because a canceled
read returned a disconnect error without a cancellation cause. Complete raw log
277217bytes SHA2566fc137693cd9a9d03824afe887d7c825e1e24822b9f5b5b447cc959c1c69144d:
`package-b-forward-fast-ci-original.raw.log`. No downloadable artifact was available.
Bounded excerpt, exact check/derivation/source identities and source-backed
mechanism/limits: `package-b-forward-fast-ci-{excerpt.txt,boundary.json,diagnosis.md}`.
The exact remote write/cancellation scheduling remains untraced. Deterministic
coverage verifies the category loss and correction; it does not reproduce that
remote interleaving.

Main's bounded brief releases only failed read-only loaded-list/metadata
observations. Those failures now include ctx.Err when present while retaining
the original error and transport classification. Noncanceled errors keep exact
identity. Successful observations, all metadata/uniqueness/archive proofs,
mutation receipt handling and attempt clearing are unchanged. A private reader
interface permits deterministic observation errors without exposing mutations.
No generic A RPC arbitration or RetireThread-wide cancellation override was added.

Three files changed after556:

- `portal/internal/workspacecodex/client.go`: local failed-observation normalization
  and private read-only test seam; one existing caller follows that private shape.
- `portal/internal/workspacecodex/client_test.go`: four-line metadata cancellation
  fixture mode. The existing unsafe-evidence test/assertion body is byte-identical.
- `portal/internal/workspacecodex/loaded_retirement_test.go`: eight deterministic
  list/metadata × transport/generic × active/canceled cases and two real-protocol
  retirement cases proving retained attempts, exact stage and zero archive calls.

Existing deletion docs already describe fail-closed retained recovery. The code
comment records this internal error-category rationale; the failure diagnosis
owns temporary CI details. No UI or product prose changed.

## Quick verification

Repository Nix environment; final published A6e469, no replacement and absent
disposable test provider catalog.

- Regression-red overlay removes only the two normalization blocks, retaining the
  private seam for compilation. The deterministic error test fails all four
  canceled cases, expected exit1, elapsed4.164s. Active cases do not fail. This
  models the old error behavior, not an unmodified old source-tree run.
- Final `go -C portal test -mod=readonly -json ./internal/workspacecodex
  -run '^TestRetireThread' -count=1 -timeout=30s`: PASS5.694s package time,
  9.836s command;16 top-level and73 total test/subtest pass records, no failures.
  Includes original unsafe refusals and archive successes plus new regressions.
- Go formatting, staged/final diff checks, exact final/checked tree equality and
  unchanged A source/lock/module/checksum/vendor files: PASS.
- Normal Nix-environment commit with ordinary hooks; no framework/active executable
  hook declared and none bypassed. No long/native/live check or CI rerun was used.

Complete logs/results and overlay are named `package-b-forward-fast-ci-red*`
and `package-b-forward-fast-ci-focused*`. Checked-tree identity:
`package-b-forward-fast-ci-checked-tree.json`.

## Complete history and preservation

Base remains deployed/current `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`.
Exactly four commits:

1. `29d64ff4da4ba7f5e5856418b9049a82f14f8ee6` — single dependency-first A stream.
2. `024f4b0e05e2fa918818610fbeb52acaa45a79e6` — naming/manual recovery owner.
3. `556a6e51b141fa419d620ad0d4ccd629fd2be6f5` — retained archive diagnostics.
4. `37a87a8a81cd3c705b7c5ee4f39338c1db1cc6ce` — this independent baseline fix.

First three exact commit objects and their18 changed paths are unchanged.
All five pin/hash files still select A6e469; no repeated pin stream. Whole final
base-to-head diff has21 paths.88 of the90 preserved newer-baseline paths remain
exact; only the two explicitly released retirement code/fixture paths change.
Newer retry/policy readers/writers, runtime capability flags, admission/deletion
recovery, provider/native/catalog policy, and upstream attention synchronization
remain preserved. Old915's semantic omission and old→new history/reconstruction
proof from the forward refresh are retained; no literal equivalence claim changed.

**No migrations or persisted-format/public-API changes** in this correction.
556 remains an ancestor with all original review and failed-CI provenance. The
separate fourth commit owns a distinct, newly diagnosed baseline failure rather
than a superseded naming/pin approach. No deployment/activation has occurred here.

Full series/diff/delta/ranges and preservation/migration proof:
`package-b-forward-fast-ci-{final-history.txt,final-diff.txt,owning.diff,range-diff.txt,old-to-final-range-diff.txt,final-proof.json}`.
Captured portal comparison binds b3..37. Main retains whole-branch history
assessment and affected review.

## CI and remaining work

One postpush snapshot at20:37:35Z: current-head Check40130503508 in_progress.
https://github.com/aither64/dev-workspace/actions/runs/40130503508
No superseded queued/in_progress own-branch run existed; no cancellation needed.
No CI wait/manual trigger/rerun or credential workaround. Exact snapshot and
cancellation disposition: `package-b-forward-fast-ci-postpush-{snapshot,disposition}.json`.

Main owns affected independent review, dependent C release and long verification.
The original naming/collection/smoke coverage limits remain in the preserved
forward handoff; this correction supplies no new live or usable-native-session
claim. New deployment/source bindings must use final37, not the obsolete556
candidate identity. No C edit, claim, merge, deployment, package selection or
session lifecycle action occurred. B owner retains follow-up fixes.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/
