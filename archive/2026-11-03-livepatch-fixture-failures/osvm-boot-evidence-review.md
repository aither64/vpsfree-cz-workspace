# OSVM boot evidence: final affected independent review

Final reviewed range: vpsfreecz/vpsadminos 54b4313404cea35b58ebb9df951ae75e27c44971..dc74bcdadef75f181934bad2178afb589c34644c.
New behavior reviewed: ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a..dc74bcdadef75f181934bad2178afb589c34644c.
Reviewer: retained reviewer0, gpt-6.1-sol/xhigh, review-purpose/read_only, settings unchanged.
Lanes: general, architecture/repetition, scope/proportionality and risk/compatibility.

## Findings and disposition

No Blocking, Important or Advisory findings in the four-file observational change or complete final history. The affected final-review gate passes for the planned publication and exact-final-head CI.

This change improves evidence for a future boot failure. It does not fix, classify or waive the old cgroup-v1 stall. Integration still requires the user's accepted complete native/nine-row CI and semantic, identity and recovery evidence on the final head.

Reuse source-identity-refresh-review.md for 54b..ad899 and the earlier review/reconciliation chain for the unchanged sixteen-file qualification feature. I independently inspected the new implementation and all its changed controls, relevant startup/reaper/rollback/logging context, actual packaging/consumers and complete two-commit series. I did not repeat the unrelated nine-site implementation audit.

## Scope and proportionality

The concrete failure-handling need is established: old5235 native run 41811208607 lost one shared cgroup-v1 guest before a working shell, leaving firmware/ROM output without sufficient launch/PID facts. Three before-hook timeouts do not establish three functional CPU/memory/tmpfs regressions. The prior same-head pass does not establish flakiness or a cause.

The existing debug route was considered first and stopped at its cache-only boundary because the plan required material guest-image/system builds. That is a bounded preparation result, not an exhaustive cache-absence claim. The selected fallback adds exactly four files, +653/-1: approximately 194 product/log lines and 459 spec lines. Those helpers address fixed launch inputs, PID ownership, bounded sampling and privacy in the existing Machine/MachineLog components. No QMP, new mode, generic diagnostic framework, guest change or package dependency is introduced.

The observation support has an independent purpose and can be reviewed/reverted separately from livepatch qualification, so the second commit is appropriate. The extra controls are proportionate to interrupt-sensitive spawn ownership and host-process privacy. I recommend no optional subsystem or hardening expansion before the next verification run.

## Startup ownership and deadline inspection

Machine#start now assembles qemu_command once and passes that same array to Process.spawn. It retains the existing PID publication, pipe/console handoff, running-state publication and reaper activation order. The new identity read occurs before the dedicated reaper can reap that child, so this initial read is still under the existing sole-child-ownership contract.

I inspected the actual pre-commit bound correction:
- observation_deadline is min(monotonic now + 10, caller's existing startup deadline).
- spawned_boot_process_identity uses a distinct ::Timeout timeout, capped by the remaining shared deadline and reserving part of the normal budget for the launch record.
- If spawn already consumed the startup deadline, the identity helper returns before proc IO.
- record_boot_launch uses only the remaining shared budget; it does not start another ten-second startup allowance.
- The masked OsVm::TimeoutError remains distinct from the local timeout. The explicit OsVm timeout rescue propagates it; ordinary observation errors are contained.
- Reaper handoff finishes before a queued startup timeout is delivered. Existing rollback still owns the exact child/reaper/pipe and performs the established kill/join/resource cleanup.

The four new focused boundary controls are meaningful: blocked identity reads with/without a future caller deadline, consumed startup budget skipping IO, and an exact asynchronously queued original error preserved through ordered reaper start/kill/join rollback. The last control asserts object identity, rather than merely accepting any timeout. Existing spawn-failure and startup/console rollback controls remain.

Machine#wait_for_boot forwards the same timeout/deadline/message options and returns the original successful result. Only a StandardError path adds observation; bare raise preserves the original exception after collection. Failure observation has an outer ten-second cap and a shorter collection budget to leave time for the log entry. It adds no readiness retry, guest command, signal, wait/reap or process-state mutation. The original start/stop/recovery APIs and deadlines remain authoritative.

## PID safety, boundedness and privacy

Initial identity records the spawned PID and proc start-time ticks only after verifying the proc PID and PPID match that child and the current owner. Failure collection opens the numeric proc directory once and resolves subsequent files through its live descriptor. It checks PID/PPID/start time before collection, after the executable read, during task iteration and before accepting the final snapshot. Changed/unowned/exited/missing processes yield fixed unavailability results.

The pinned proc-directory approach agrees with the owning Linux documentation: open descriptors do not prevent numeric PID reuse, but operations through descriptors for a dead process do not act on a newly reused PID. I checked that primary contract in the local canonical Linux object's Documentation/filesystems/proc.rst:130-136. The implementation uses the descriptor path rather than repeatedly reopening /proc by the bare numeric PID during a collection.

Reads have explicit small limits: parent/task stat 4096 bytes, wchan 128 bytes, and at most 32 task entries, all within the collection timeout. The stat parser drops comm text and retains only numeric fixed fields plus a recognized state. The executable and selected launch paths must pass the constrained Nix-store path predicate. The task wait-channel string is limited to a safe fixed character set. No command line, environment, raw configuration, arbitrary kernel parameters, proc comm or exception text enters these events.

The launch parser derives only the finite input/topology fields from the actual assembled command. Duplicate/ambiguous options and unsafe/non-store paths become unavailable; opaque arguments are explicitly omitted. The log methods themselves emit only their fixed field list and bounded tasks, ignoring unknown keys. Read, timeout and log failures cannot replace the primary boot error, and ordinary launch-log errors do not roll back a successful child. A real OsVm startup timeout still reaches the established rollback path.

I inspected the real owned-child control and the negative cases for missing/reused/unowned/exited PID, identity changing after the executable read, unsafe exe/wchan, caps, blocked collection/logging, exact error preservation, duplicate launch options, secret-bearing arguments and ordinary successful boot behavior. The real child is released through its pipe and then reaped by the test; the observation methods themselves do not signal or reap it.

## Actual consumers and delivery

MachineLog remains the existing per-machine text log at the existing *-log.log path. TestRunner's Machine instances and start_all/wait_for_osctl_pool paths reach the new wait_for_boot observer even when the guest shell is unavailable, before the later guest-dependent failure collector. Native and lifecycle upload actions already collect **/*.log, so no artifact/protocol change is needed.

I also checked the packaged path, not only the unit loader: test-runner.sh builds .#test-runner; test-runner/nix/package.nix places the current local osvm/lib in RUBYLIB. Thus a final-head runner will carry these source changes without a separate generated gem pin/update. Machine/MachineLog ship together; no public runner argument, configuration option, API removal or consumer migration is introduced.

This is additive host-test observation. It does not alter kernel/guest configuration, production state, boot identity guards or livepatch semantics. The source-capture/guest-version integration reviewed at ad899 remains unchanged; whole runner/test derivations still need new-head verification because OSVM source and captured revision changed.

Near-code comments explain the lasting identity, interrupt, budget and omission invariants. Existing project test/source-identity docs retain their contracts. No new user workflow or mode requires another document; individual failures, cache preflight and execution receipts properly remain in session records.

## Verification and exact reuse

I inspected the final receipts:
- Two changed spec files: 81 examples, 0 failures, seed 50896, 1.32s.
- Full OSVM suite: 207 examples, 0 failures, seed 39087, 7.38s.
- Declared RuboCop: four files, no offenses.
- Post-commit shared-runner integration: 99 examples, 0 failures, seed 27981, 35.56s.
- Final ordinary pre-commit and all message hooks passed.

I independently verified that all four current files equal their committed dc74 blobs and match D's exact frozen SHA256 values:
- machine.rb: 8f4ebdc91fc3d303e6c61b3c7f850066e14e6a8463a6d19f96894330e65ba67e.
- machine_log.rb: 9fd3f18555bedb875468c7701acaee88dc97327c03cabeb3617ce1a8b9306a50.
- machine_spec.rb: 922c9887e069a609ba1efa191eacd0e2e36c129f0ca1d6c1c7255b5eced8988d.
- machine_log_spec.rb: 0b35767db2978c1d349908c21f900cb82b8cc351ba572e8ea4ed38d253df22ea.

The older 77/203 prototype results are superseded evidence, not final counts. The initial unbundled RuboCop invocation was an environment failure, corrected by the declared Bundler context at 1.75.8; the final commit log confirms normal enabled hooks passed without a source/configuration suppression or bypass.

I independently compared package-a-osvm-identity.json structurally with the reviewed ad899 ten-field receipt: they are exactly equal, including all drv/output pairs. The normal producer/module/sites/resolver/control/frozen boot/SDK/config/compiler identities therefore retain the documented reuse boundary. A's current receipt rechecks module SHA 7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f, sites SHA 093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1 and lock SHA 604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa. Prior parser/ELF/SDK/helper checks remain bounded to those inputs. No whole-guest/test-closure equality or old-runtime transfer follows.

My own actions were read-only source/history/receipt inspection, primary proc documentation inspection, hash/tuple comparisons and final-range git diff --check. I ran no unit suite, build, Nix evaluation, VM or new process observation.

## Complete final history, consolidation and migrations

Independently verified the complete final series:
1. ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a — tests/livepatch: qualify current module probe sites.
2. dc74bcdadef75f181934bad2178afb589c34644c — osvm: record bounded host evidence for boot failures.

HEAD is exactdc74; its parent is exactad899, whose parent and the final merge base are exact54b4313404cea35b58ebb9df951ae75e27c44971. The full range has twenty paths +2923/-184. The new delta is exactly four OSVM paths +653/-1, disjoint from the original sixteen.

All sixteen original livepatch file modes/blobs remain identical to the reviewed ad899 tree; the unchanged raw prefix message hashes to 620322a1820f2a1f3527d677f6d54be378985dc870dc8e1e31a03d7d978f1fcd. The original reviewed commit itself remains the parent object. Both final commits have clear independently meaningful purposes; retaining the diagnostic support separately is justified.

No obsolete feature approach, fixup/tidy residue, transitional migration or unsupported compatibility iteration remains. Superseded diagnostic prototypes exist only in retained check receipts, not the final branch history.

No repeated dependency/channel/input/pin/lock/generated update streams exist in the final series. No consolidation exception or deployed intermediate is needed.

No migrations. No database/schema/production persisted-format or protocol migration, deployed schema intermediate or externally consumed transitional state is introduced. No coordinated fleet update is required.

Final source/index/nonignored-untracked status was clean at exactdc74. git diff --check for the complete range passes. Existing local provenance refs and detached old5235 source remain retained; I did not remove or publish them. Canonical staging54b/remote feature5235 are A's recorded last SSH check, not a new remote check performed by this reviewer.

## Readiness, identity and handoff

The next planned step is lead-owned publication and full exact-dc74 native plus all nine lifecycle CI rows with the established source/guest metadata, artifact/boot identity, semantic and recovery evidence. Unit/owned-child checks do not constitute a product VM pass. A future green run qualifies its own inputs; it does not retrospectively explain old418's firmware-only stall. Preserve that failure and its unclassified cause. Any actual new failure needs evidence-based handling.

The old original5235 run remains observer-owned with seven of nine lifecycle rows passed and aged/fresh work unfinished at the assignment boundary. Old5235 selected-image cases now pass, while the three shared-guest before-hook timeouts remain unwaived. No result here changes the user's complete-success integration condition.

Identity was reverified before session files: dev-session current matched 2026-11-03-livepatch-fixture-failures; both environment identity markers were absent; trusted thread-bound developer instructions name this exact slug and /home/aither/workspace/ai/vpsfree.cz. Live roster confirms reviewer0/thread 01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh, review/read_only, ready. No overrides or nested reviewer.

Applied mandatory-change-review and all four lane references, reusing unchanged current-context guidance as permitted. Repository instructions remain applicable with no nested OSVM AGENTS; changed workspace AGENTS/lifecycle routing at 4d58b5877 was read. No temporary service or lifecycle action was launched.

I remained read-only: no source/session writes, build/evaluation/VM, CI polling/retry/cancel, fetch/push/merge/deploy or lifecycle action. Full report is delivered through report_to_lead for root to save as osvm-boot-evidence-review.md. Session remains open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
