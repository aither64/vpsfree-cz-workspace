# Final forward package B review input

Main owns independent review and all longer verification. Source is published,
clean and frozen at B `529e075ad07e2d967a8af4902584e37527115454`, checked tree
`c9c3286858934ba63ff11c9e37879e7803a8351f`, above deployed/current SSH master
`10bb047513c82d1310e8fcaa797e8772f948dd8a`. Repository and own worktree are
`git@github.com:aither64/dev-workspace.git` and
`worktrees/2026-10-20-workspace-session-naming/dev-workspace`.
The initial tracking prerequisite remains7e66. Design is in `design.md`;
selected-baseline audit is `deployed-baseline-20261025.{md,json}`.
User deployment HOLD prohibits deployment effects; source publication grants
neither merge nor lifecycle authority. C113d/7510 remain frozen.

## Requested result and scope

Preserve newer installed message admission/delivery/recovery and replay the
accepted naming contract: one absolute30s deadline before queue admission, two
held operation slots through cleanup, max two calls only after A proves safe
retry, frozen provider/input/settings,200ms cancelable backoff, remaining1s
inference+250ms cleanup. Failure stops before base/slug/handoff and retains
saved-input retry/manual recovery; attachment-only input requires a manual name.
No native/model/catalog/provider/policy/API/schema change is intended.

The new diagnostic owner is test-only: creation browser and Nix VM, one focused
support helper and quick tests. Standard external flock-only strace attaches
existing service MainPID. It records busy EAGAIN/EWOULDBLOCK syscall PID/TID/FD/path/mode/errno
and trace timing, with separately bounded later path/proc ownership snapshots.
Descriptor identity and original holder remain unproved. Browser monotonic
chronology is temporal context only. No wrapper, MainPID replacement, product
hook/logging, custom tracer/FD-reconstruction framework, lock acquisition,
operation retry/sleep/timeout workaround, changed first assertion or acceptance
sequence. Observer timing can change scheduling; green evidence never identifies
the old holder or claims a fix. Missing/proc-exited/truncated evidence is explicit.
New serialization excludes argv/env/body/header/cookie/error/URL-credential text.
The helper docstring/comments own lasting diagnostic limits; temporary failing
VM/CI history stays in session records, so no additional product docs are needed.

## Complete series and provenance

1. `6c963d70cedcec6d76aadae9ddc83b24e75071ce` — one final dependency stream.
2. `d328def7` — original naming/manual recovery owner.
3. `5f922701` — original bounded archive diagnostics.
4. `447aeda8` — existing failed read-only retirement-observation correction.
5. `529e075a` — bounded creation refusal diagnostics.

Use exact full commit identities from `package-b-forward-20261025-final-proof.json`
and history text; abbreviated entries above are labels. The complete23-path diff,
history and old/new range-diff are `package-b-forward-20261025-final-{diff,history,range-diff}.txt`.
All four owner patches are patch-ID and range-diff equivalent to original024,
556,37,c63. Independent temporary index: start installed10bb, apply those exact
four patches, overlay only five final dependency blobs; resulting tree equals
checked/final tree. Six newer upstream message-recovery blobs are exact;
workspace-portal recovery prose section is exact, original naming prose unchanged
and main-approved.88/90 prior selected preservation blobs are exact; the two
intentional retirement fixture/client corrections remain unchanged B37 behavior.
Upstream attention stage synchronization is exact; old915 is semantically
redundant and remains omitted, without literal equivalence claim.

Retirement retention has a distinct source-backed responsibility: A872c joins
cancellation for failed Request only. Loaded-list and metadata validators may
return observation errors after successful Request. Existing B37 normalizes only
those two failed observation boundaries. Main and architect accepted retention;
no successful observation or mutation receipt handling changes.

There is one A801099 dependency update (flake input/lock, Go module/sum, vendor
hash), before its consumer. The old pin stream was replaced, not retained in the
final series. Old B37/c63 source, reviews, failures and diagnostic patch are
preserved in before37 manifests, `package-b-before-refresh-20261025.bundle` and
local `...-before-refresh-20261025` ref. Earlier full history/check/build/native
receipts remain unchanged and bounded; no initiative activation occurred.
Old same-initiative C/CI inputs are provenance, not a supported external release
boundary. **No migrations or new persisted format/public API/state policy.**
Installed10bb is an ancestor; old feature commits were reconstructed rather than
literally merged. Forward recovery readers/browser fields and contracts survive.

## Exact dependency and checks

A is final `801099102ef9af4a82c1f3853c53d6b442ecd4dc`, immutable source
`/nix/store/7nl4zslrkchbnfzzbvbfkb1qcl2n11jx-source`, NAR
`sha256-Eoqdgi+a8BFdVGOMp7CnV3jXWmsajcyN332Jixis00M=`, module
`v0.0.0-20261025080000-801099102ef9`, no replacement. Vendor hash is
`sha256-Zp42oaLBpFXcdzZNo8jdNJOGuVxDojvYugf/7sm3SeI=` from copied-portal
`go mod vendor` plus `nix hash path`; regeneration from the final committed
portal also matched exactly. No package build here. All other flake nodes
are exact installed baseline. Ten module source/test/asset files match immutable
A; Luna catalog SHA remains049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1.

Quick commands/results are fully saved in `package-b-forward-20261025-*-result.json`
and logs. All commands used repository Nix and absent disposable provider catalog.

- Go `./internal/web ./internal/workspacecodex`, readonly, regex
  `^Test(SessionNam|SessionPreparation|RetireThread)`, count1 timeout55s:
  PASS69 top-level/175 test records, zero fail/skip. Web36.420s, codex5.731s;
  wall67.994s including compilation. Earlier known-quick classification came
  from51s prior run; no repeat. Future uncertain cold invocation needs watcher.
- Go admission/source-lock/Node composer+submission/response-loss recovery:
  PASS7 top-level/12 records, zero fail/skip, package6.692s, wall38.518s.
- Nine controlled diagnostic tests pass1.299s: real standard attachment and
  held descriptor, release-before-observation, both actor roles/lock kinds,
  unknown/proc/truncation/caps/canary/failure/exit preservation. They do not prove
  original VM holder or real portal acceptance.
- Node/Python/Nix/VM Python/emitter syntax, exact pin and negative pin contracts,
  immutable module-source comparisons, formatting/diff checks pass. No hook
  framework/active non-sample hooks; normal Nix commits, no bypass.

The selected recovery component contracts run real shipped JS snippets and
preparation HTTP serializer/handler tests. Full Chromium+Firefox
`TestQuestionBrowser/message_delivery_browser_test.cjs` is preserved unchanged
and pending the appropriate post-review watcher; it was not silently treated as
covered by a skipped default browser test. Packaged/native/creation/archive/full
flake and collection/switch checks need main's exact-input verification plan.
The collection probe binding remains architect-owned; no new-head execution is claimed.
Old local collection/client/package successes are retained separately; old local
creation failed and archive/fullflake never ran. CI archive success is a separate
observed receipt, not new-head acceptance or certified input reuse.

## Review and execution gates

Risk is high because preserved components own persistent attempts, recovery and
cross-project/native contracts. Main should use its retained independent reviewer
with all four affected lanes; no review has been self-certified here. Inspect
whole history/migration/consolidation as well as the new diagnostic delta. Main
accepted original prose unchanged; no new UI strings. Source and refs are frozen
for findings. No long/native/VM/live check, CI trigger/rerun/wait, source selection,
claim/deploy/merge/lifecycle action was performed. One post-push CI snapshot sees
Check40175804431 in_progress; no superseded active own-branch run to cancel.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/)
