# Follow-up review reconciliation

Risk: High (private persistent comparison descriptors and cross-project/browser
contracts). All reviewers use fresh gpt-5.6-sol with xhigh effort. Original
reviewed heads and boundaries are in follow-up-review-packet.md.

## General lane

- Blocking: independently reversible changes were bundled in b924a15 and the UI
  commit preceded its required backend endpoints. Accepted. Reconstruct the
  unmerged runtime series into dependency order, splitting discovery/process
  budgets, cache/coalescing, durable descriptors/restore and batches/preview.
  Separate accepted receipt behavior, waiting copy and repository tab/helper
  wiring. Retain exact final source and prove intermediate backend compilation.
- Important: trimEditors could retain more than eight views by exempting nearby
  and loading records. Fixed in temporary follow-up7d2c272: trim before mounting,
  preserve only selected/current renderer, invalidate evicted async generations.
  Actual Chromium tall-viewport/many-short-files regression passes, retains the
  selected file, never leaves more than eight mounted views and completes syntax.
- Advisory: full-file navigation to an added/deleted file could put the wrong
  version in its URL. Fixed in534ce67 by normalizing fileRoute. Browser regression
  crosses Before -> added -> deleted and checks new/old URL versions.
- Advisory: upstream notices contained trailing whitespace; the packet's clean
  claim was worktree-only. Fixed in3410222 without altering license meaning.
  git diff --check d3bfd0f..working-tree now passes; verify the committed range
  again after reconstruction.

The three direct fixes will be folded into their owning reconstructed commits.
They preserve the reviewed design/resource/public contracts and need focused
verification, not another general review merely to confirm requested edits.
Architecture and risk review continue on the original frozen heads; scope is
pending the next available reviewer slot. No long manual integration has begun.

## Architecture lane

One Important and three Advisories; no Blocking findings. The editor-bound and
series-order findings duplicate General and receive the same fixes.

- Native Git counted newline bytes, allowing12,001 logical lines if the last was
  unterminated, while the worker rejected that file. Fixed in03f06b3 with exact
  and over-limit native fixtures; focused test passed0.493s.
- Removed unused projection-module limit exports. The existing editor tests now
  cover every shipped language and prove its detected grammar is loaded, and
  exercise both final-newline forms at the worker's line limit. Seven tests
  passed4.7s in2ddfc9e. Retain two explicit small registries because worker imports
  must stay static/bundled and filename/shebang detection belongs to the UI;
  their complete supported set is now covered without adding a registry framework.

The reconstruction target is now2ddfc9e; these narrow fixes will be folded into
owning source commits. Committed-range whitespace check d3bfd0f..2ddfc9e passes.

## Risk and compatibility lane

No Blocking or Important findings. Advisory: exact-pair descriptors have no
aggregate expiry/cleanup policy. Accepted for this scope: records are small,
content-deduplicated and require actual branch changes to grow; retention keeps
frozen links valid for active and archived sessions. Deletion/replacement makes
old scoped links unusable but leaves private records. Adding lifecycle cleanup
or expiry would introduce a separate retention contract and is deferred. No Git
objects are pinned/fetched; missing objects remain an explicit unavailable result.

Deferred gaps remain full-handler/live browser and package deployment acceptance.
No forced live rollback or interruption of unrelated sessions is authorized.

## Scope lane

No Blocking findings. Important: overview mounting eagerly imported the editor
and warmed its2.4MiB syntax worker. Fixed by deferring import to renderFile and
worker creation to createReviewEditor. Actual Chromium acceptance now checks the
overview requests neither asset, then opens a comparison and verifies syntax.
The full component run passed all15 checks with the final packaged syntax assets
/nix/store/2bpajwwfsvh1wdkfy0qsbqfxhh0xdrz2-workspace-repository-review-assets-1.0.0.

Advisory: createCopyButton offers both text callbacks and an explicit getText
callback. Accepted: the small additive API is documented and tested, the
transcript wrapper uses getText and repository controls use text. It does not
create a second clipboard implementation or resource path. No further callback
forms or generalized button framework are being introduced.

All four lanes are complete. Behavior findings have focused verification;
series reconstruction/equality and final coupled package/live acceptance remain.

## Reconstructed committed series

The final detached head820277e6cc3aa7ff9acb0396feb3314e7f84996a has the exact
same tree as reviewed fixes0474e62:
19a507d97a5cce1a51490807a7ddf4fab853d550. Root independently verified full-tree
equality and git diff --check d3bfd0f..820277e. The clean primary branch was
updated with a checked ref update; no working-tree contents changed.

Dependency order:

1.36a2997 matching provider pins
2.1e33b23 accepted receipt lifecycle
3.b1374e8 waiting wording
4.541e077 native messages/statistics and logical line limit
5.3c14009 direct registration, discovery and process admission
6.4cfa56c immutable cache/coalescing
7.3557355 durable descriptors and exact restore
8.eea9497 batches and first preview
9.c1265c2 editor, syntax worker, build/lock/licenses and tests
10.e9a037d query tabs and shared helper wiring
11.820277e repository navigation/UI and direct review regressions

Discovery, cache, durable restore and batch stages passed focused Go checks;
cache and subsequent stages passed-race, and durable restore was tested without
batch routes or inline preview. The renderer precedes all ready/revealLine/full
view callers. The series Blocking issue is resolved. Direct fixes preserve or
reduce the reviewed design; no new design/contract requires a lane rerun.

Final reconstructed full Go suite passed with GOWORK=off (repository8.736s,
web39.684s, all other packages passed). Exact mapping and intermediate commands
are retained in follow-up-series-reconstruction.md/json. Downstream pins are
mechanical updates to the final reviewed runtime head; no public interface or
state format changed during pin propagation. Long package acceptance starts
only after this reconciliation and quick verification.

## Final acceptance

All reconciled changes are deployed as profile 30, exact package 8a2c8nb. All
final project CI and Nix package/flake checks pass. Full-handler conversation
browser acceptance, live repository browser/CSP/clipboard/line-link checks,
TLS/authentication smoke and the direct metadata improvement target pass.
See follow-up-verification.md and its retained evidence. No Blocking or Important
finding or required acceptance check remains open. Branches remain unmerged.
