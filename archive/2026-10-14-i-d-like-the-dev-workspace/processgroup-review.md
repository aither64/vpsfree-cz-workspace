# Final affected review: descendant exit assertions

No Blocking or Important findings. One Advisory coverage improvement is recorded below. The committed observer correction fits the accepted test-only boundary; original failure causes remain unproved.

Reviewer: retained independent reviewer0, GPT-6.1 Sol/xhigh/read_only. Reverified exact bound session/current, both absent identity environment variables and live same-session roster/settings. Read mandatory-change-review and all four assigned lane references, applicable workspace/runtime guidance, plan/state, accepted design addendum, packet and frozen evidence. No nested agents or filesystem writes.

## Advisory: exercise identity rejection with terminal samples

General/coverage lane; portal/internal/processgroup/processgroup_test.go:278-288 at b4b90aca3198b6d0ab5171044c6731708af8776e.

wrongPID and wrongGroup are constructed from sample("S"). A matching live S sample is already rejected independently of either identity guard, so both named negative cases would still pass if the waiter's PID comparison or terminal PGID comparison were removed.

Construct these negative samples from Z or X while retaining the expected start time. That makes the cases exercise the required PID/PGID rejection boundary. The current implementation correctly enforces those guards; this is a nonblocking regression-coverage improvement. A direct narrow adjustment can be inspected and verified by the lead under mandatory-review steps 9–10 without a confirmation-only reviewer rerun.

## Affected correctness, architecture, scope and risk conclusions

Both original real cancellation tests remain. They consume one bounded wait result, preserve the two-second limit and 10ms polling, and cannot reverse an established exit with a separate final probe. Real time.Now/Sub retains monotonic timing. Matching live or unresolved unknown observations fail at the bound.

The parser locates the final parenthesized command delimiter and reads the correct state, PGID and start-time positions. It validates positive identity fields, distinguishes wrong PID and unknown state, and supports spaces/parentheses in comm. Only validated absence, a reused start-time identity, or matching PID/start-time/PGID in Z/X proves exit. Read/permission/parse errors remain unknown; the identity-free kill-zero fallback is removed.

Both fixtures verify captured PGID against the leader. The live-child negative control observes an actually spawned sleep for the same bound and cleans up only through its exact child handle and Wait. No scan, foreign PID operation or additional process-group signaling is introduced. I did not inspect or signal original builder PID12682.

Failure context retains only numeric identity/timing/errno fields and fixed state/category labels, capped at 1KiB. Raw comm/stat, arbitrary error/path strings, argv and environment do not enter that projection. Only the last observation is retained.

The helpers are local to one _test.go file and shared by the two assertions and focused controls. Explicit observer/clock/pause callbacks support deterministic testing without a new product abstraction or generic process framework. The change is proportional to the demonstrated ambiguity. Existing comments, commit rationale and session investigation explain it; no product guide update is needed because no supported product behavior changes.

## Exact range and complete history

Affected range: bb9e6291bec10227c961c36559fba406938f1eaa..b4b90aca3198b6d0ab5171044c6731708af8776e.
Complete own range: 832d9f1a6a21337dd44063ddf39f7a88cfc95450..b4b90aca3198b6d0ab5171044c6731708af8776e.

HEAD, parent and merge base match the freeze; worktree is clean. The affected diff changes only portal/internal/processgroup/processgroup_test.go, +233/-22. All four frozen artifact hashes match and affected/whole-branch patches, complete series and stat match Git byte-for-byte:
- affected patch SHA256 97cfc8af86b0f623d16c7f8327a08917c8867d4a8e1e480ac2e1752222bd4f30
- whole-branch patch SHA256 022c2cafdcf17832f2245c1d270afaa3d668523b000a5973a131c19f69d06ed4

Complete own series:
1. 96717cdeb5f733391846a95d78c117068ce77de8 — accepted attention/Web Push and inseparable module/import/vendorHash boundary.
2. bb9e6291bec10227c961c36559fba406938f1eaa — accepted bounded provider diagnostics.
3. b4b90aca3198b6d0ab5171044c6731708af8776e — independently justified correction to the upstream test observer.

The first two commits are unchanged. Full final inventory is 41 paths, +4126/-104; no merge commits. Initial-registration ancestry retains protected sensitive-session and admission/sharding/integration history. The separate third commit corrects a pre-existing baseline test observer discovered during verification, so folding it into either unrelated feature commit is unnecessary.

No obsolete unmerged approaches, follow-up fix series or repeated runtime dependency/channel/generated-update streams remain. No additional consolidation is required. The original parent/test are preserved under the session-owned ref/artifacts. Earlier source and downstream reports retain their exact older-head conclusions.

## Production, migration and composition provenance

Production processgroup.go is unchanged at blob 9e7d02c4e8c234d2d4f12fb446e7e082bf74b45a. Independently confirmed unchanged module declarations, flake.lock, packaging/vendorHash, runtime and coordination contracts. The new test blob matches the freeze.

No migrations or persistent/private format conversions in the complete own branch. Initial notification schema1, strict optional preference/old omitted-receipt compatibility and protected upstream integration journal/capability lineage remain as previously reviewed. The test helper has no product consumer; the owning Go package is exercised by packaged checks and their VM package dependency.

Per packet, no own version has been merged, released, deployed or externally consumed as product state; disposable probes remain evidence fixtures. This new head is unpublished. Workspace ab25878e and configuration 9afddccb still select bb9e6291. Future b4b90aca source publication and consolidated final pin selections require their separate exact composition/history refresh; none is certified here.

## Verification limits and next step

Inspected the preserved compile-only variable-collision failure and corrected deterministic run. The failure occurred before any real child check. Supplied uncached focused Go1.26.6 evidence passes five top-level tests with fifteen deterministic wait subcases, including both original cancellation tests and the owned live-child control: package3.089s / command3.735s, exit0. I ran no tests or builds.

Derivation comparison is evaluation-only evidence; it does not establish new package/VM success. The original exact-bb9 local flake failure and same-head CI success remain preserved. Passing corrected tests does not establish a Z-to-X cause, exonerate production cancellation, or explain the earlier provider recovery failure.

After the lead records the Advisory disposition, no Blocking/Important review finding prevents the authorized finite verification step. Final changed derivations, required packaged/recovery checks, final pins, fresh deployment preparation and native/physical acceptance remain outstanding. Do not retry until green or increase deadlines as proof.

No source publication, network/host/provider/queue/reservation action, merge or session lifecycle operation was performed or authorized by this review. Keep the session active/open.

Lead should persist this report as processgroup-review.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
