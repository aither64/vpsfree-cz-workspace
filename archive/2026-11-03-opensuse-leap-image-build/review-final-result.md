# Final independent whole-branch review

No Blocking or Important findings. One documentation advisory below. The committed branch can proceed to the planned final-source runtime checks; it is not yet verified for use.

## Advisory — document retained-builder refresh

General/risk, commit 4c2a38bc0: image-scripts/README.md:138 explains builder creation but does not explain that changing a builder's base release leaves an existing managed builder unchanged. UseOrCreate at osctl-image/lib/osctl/image/operations/builder/use_or_create.rb:25 starts the existing name-derived container without checking release metadata. An operator can therefore update these scripts yet keep using Leap 15.5; rollback has the converse problem.

The commit message and session design correctly record this, and final tests already require fresh state. Recommend a short durable Builders note describing reuse and recreation of the positively identified idle managed builder through the existing ct ls/ct del interface. No automatic refresh mechanism is needed. This advisory does not block the planned tests.

## Reviewed identity, scope and correctness

Reviewer0, retained gpt-6.1-sol/xhigh/read-only; exact current/env/session/roster/thread/settings verified. Read mandatory-change-review and all four lane references, applied the previously read workspace procedures, and inspected current repository instructions. No source edits, builds, tests, nested agents, merge or production action.

Reviewed complete dd188397abe37d0bc33f4c5dfb3605206ce5e326..742eb30cb1a8b6766c85e915d26b0400e38244b1, tree 19f423e70ff439867d4bb27e8ed07b9c95fdb703. Independently confirmed merge base, clean worktree and matching HEAD/local origin feature ref; the publication receipt records fresh SSH remote proof. The final message-only amendment has an empty source diff from c856aa1b9.

The seven-path +27/-14 result matches the user's clarified shared-builder request and additional actual device-unit fix. Its duration includes native image verification, reproduced failure and the controlled package/restart experiment; the delivered implementation has no new subsystem or speculative safety layer.

The shared Leap builder changes only its explicit base release to 16.0 and retains its name/setup. The new image uses it while targeting 16.1 through the existing bootstrap. Older image definitions remain, and 16.1 uniquely owns latest/stable. Explicit distro coverage remains in cgroupAll/systemd.

The helper installs udev through its existing minimal package list and native dependency solver, preserving --no-recommends and the network-only trigger override. A nearby comment explains the invariant. The device test removes the exception and special immediate-command path while retaining normal eth0, dummy0-before/after and cleanup assertions. No test framework contract changes.

## Architecture, evidence and compatibility

Consumer search confirms the shared helper serves Leap 15.6, 16.0, 16.1 and Tumbleweed; only the three Leap builds use the changed builder. The fix belongs in that shared helper. No duplicate implementation, new abstraction, mask, host privilege or namespace workaround is needed.

Independently inspected raw causal records and verified all three snapshot hashes against device-unit-result.md. Before installation, udev units were not-found; after the required package closure and a normal container restart, eth0.device returned 0, dummy0 returned 3 before creation and 0 afterward, and both interfaces had systemd tags. The PTY contains DEVICE_UNIT_CLOSURE_RESTART_PASS. This supports the cause and minimal package fix on historical AA; it does not prove the final rebuilt source.

The live-install reload/Lua warning is preserved, explained and not presented as a clean scriptlet pass. Fresh bootstrap must still be free of unexplained scriptlet/unpack failures. Existing mounts and control-stub behavior are unchanged. No persisted host format, API/protocol, kernel/device-policy or coordinated fleet change is introduced. Rebuilt images gain userspace packages; published images and existing containers are not retroactively changed. Existing-container installation/restart is a separate operator action.

## Complete history, consolidation and migrations

The entire series has three logical owners:

- 4c2a38bc02d1d10c208d478c01ec90057995825e: shared builder upgrade.
- 57871a8e3f8f429e86e3ad6abf16de99a44e9416: new 16.1 image/registration/coverage.
- 742eb30cb1a8b6766c85e915d26b0400e38244b1: independently requested baseline device-unit fix and its test correction.

The split is coherent: the existing-build upgrade and baseline udev defect are meaningful independently of adding the new release. No obsolete dedicated-builder files, fixups/WIP, abandoned compatibility path or transitional implementation remains in the final range. Backup refs preserve reviewed/failed/tested predecessors separately. The AA and final ranges are substantively different; earlier review/runtime results are historical evidence only.

The builder-release update is consolidated into one commit. No repeated dependency/channel/input/lock/generated update streams remain. **No migrations** exist, so merged/released/deployed/externally consumed migration provenance is empty. No obsolete history or migration consolidation remains necessary. Commit messages include rationale, validation and pending-runtime limits.

## Remaining verification and delivery limits

Source syntax/format/Overcommit/hooks are reported passed; no checks were rerun here. The native discovery failure involving the unrooted immutable source is an environment/input-availability problem before VM/build execution, not a product failure or a missing source quick check. Correct/root the input, bind the replacement to this exact tree/revision, and complete native selector validation before launching final tests.

Run the planned fresh-state normal image batch for all four helper consumers. Confirm actual Leap 16.0 builder identity, successful package transactions, absence of the old Lua/cpio or other unexplained scriptlet failures, normal image-suite results and exact candidate hashes. Then run complete original device assertions against all four rebuilt artifacts, plus final-16.1 start-stop, /run, routed networking and cgroups v1/v2 checks. Temporary local aliases must bind to the actual recorded candidate; old AA or public latest cannot substitute.

Stock public-image CI can still fetch old unfixed latest or lack explicit 16.1 until authorized publication. Local candidate success does not satisfy that public-availability dependency. Preserve the distinction in readiness/rollout records; this report performs or authorizes no production action. The user-reported merge-when-done approval remains for the lead to apply after required verification and integration preparation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/

## Lead disposition

Accepted source review; runtime verification remains required. The documentation advisory is recorded as a follow-up, without adding an automatic builder-refresh mechanism. The behavior predates this change, the builder commit and design describe it, and current verification uses fresh state. No source change or additional review rerun is needed for this acceptance decision.
