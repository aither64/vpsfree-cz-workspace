# Scheduler observation lifetime: final affected committed review

## Findings and disposition

**No new Blocking, Important or Advisory findings.**

Exact diagnostic head **b361b8c600bc1d50c237a68ca5413d38be9a0e99** passes this affected committed review for the separately released one-case runtime check. It does not establish that the ordering remedy works in the guest, explain the enable timeout or original CPU127 warning, approve a scheduler correction, or provide final qualification/merge readiness.

Complete evidence range: **2951a632c4254a44747a8da326e3dde897eaa0e2..b361b8c600bc1d50c237a68ca5413d38be9a0e99**. New substantive tree delta from reviewed/tested **13b658f67c37418d6bbf91316ea7b3c6db99fe17**: **qualification.rb only, +177/-49**. All four lanes applied: general, architecture/repetition, scope/proportionality, risk/compatibility. Risk remains **HIGH** because privileged guest tracing and failure/resource ownership change.

## Scope and proportionality

The current need is concrete: the first13b execution accepted definition/filter syntax but timed out enabling the event after the full population was running. Its immediate disable/delete attempts also timed out. Moving global preparation earlier, limiting the loaded hotplug window to private recording, and moving observer release after drain are a bounded diagnostic ordering experiment. They are not an established kernel fix or proof of the earlier wait path.

The added state is local to this one qualification example and its after-hook: instance/event/arm/recording ownership plus prepared/release-attempted/released flags. Cross-phase state is necessary because ownership now spans early setup, workload execution, capture and late failure handling. Unknown effects must remain distinguishable from acknowledged ownership. The helpers do not add a generic resource manager, runner interface, configuration mode, retry loop, wait/killer, instrumentation subsystem or new data schema.

The actual delta matches the accepted one-file package. Site, fields, decoder, kernel/input/profile, command budgets, hotplug commands, cumulative health baseline and workflow remain unchanged. The user-directed shorter diagnostic age remains300; primary shipping remains14400. I found no speculative mechanism requiring removal or additional optional hardening before this next check.

## Actual code and failure ownership

### Early preparation

**qualification.rb:296-361,667-672**:
- The existing exact AMD/v5/128CPU/16384MiB/100000-task selector is extracted without widening it. Nonselected profiles return without observer commands/state.
- Preparation occurs immediately after acknowledged predecessor activation and before prepare_transition_state, start_stress or population creation. The workload-started flag is set before the first workload side effect, so partial startup cannot be misclassified as never started.
- Frozen notes, active release, unique native base, exact CALL+0xc3 and fetch declarations are retained. The private instance and global event must both be absent before creation; an existing resource is not adopted or removed.
- The new private instance must report current_tracer=nop. Recording OFF is written and read back before normal64KiB-per-CPU/mono/CPU127/filter preparation.
- Event enable must return and read back1, with recording still0 and tracer stillnop, before prepared becomes true. Failed/uncertain preparation never reaches workload creation.
- Attempted instance creation, event definition and arming are marked possible before their commands. An exception cannot silently turn uncertain mutation into none/disarmed.

The prepare ensure makes one owned reconciliation attempt on the diagnostics channel if setup did not complete. A notes/absence refusal with no created resource touches no foreign resource. A known safe partial setup can be released before workload; an uncertain create/arm is retained as incomplete instead of receiving stacked global rollback operations. Original setup exceptions/cancellation are not converted to success.

### Recording window and original error

**qualification.rb:363-420,758**:
- At the original pre-hotplug location, only acknowledged prepared/armed/OFF state permits recording.
- The window performs private recording ON plus readback, runs the original hotplug/health body, then OFF plus readback and capture. There is no event registration, global enable/disarm/delete, mask/clock/buffer reset or late clear in this window.
- On a body failure/cancellation, OFF/capture uses the reserved diagnostics channel. The original exception remains primary; command/decode failures are logged as diagnostic INCOMPLETE. If the body otherwise succeeds, incomplete recording/capture raises.
- Raw trace is printed even if recording-OFF acknowledgement is missing, but it cannot be accepted as a complete capture. The unchanged decoder and loss/miss/profile checks still govern accepted observations.

I checked the pinned trace.c/trace_nop.c/ring_buffer.c distinction: with nop, private tracing_on toggles recording flags without tracer start/stop callbacks or kprobe arm/disarm text-patching. It still takes a mutex and executes guest commands. This supports trying the narrower loaded operation; it does not prove prompt execution under stress.

No new error rescue encloses or weakens the original cumulative kernel-health predicate. The actual helpers retain StandardError-derived OsVm command/timeout failures while cancellation outside StandardError continues to unwind. The existing failure hook logs cleanup failures without replacing an already failed example. Hard runner/guest termination still cannot promise Ruby ensure/hook execution.

### Drain and one release attempt

**qualification.rb:422-477,795-817**:
- Normal release is after the existing successful exit/sctp.exit/tun.exit checks, population state=stopped/tasks=1 and stop_stress. Only then is the normal drained flag set.
- I inspected stop_stress: it requests the existing stop, waits for the recorded controller to exit and removes its pid file. No new workload wait or killer is introduced here.
- Failure reconciliation does not equate a stop request with drain. It performs at most one read-only ten-second diagnostics-channel check of all three successful exits, stopped/tasks1 population and the existing stress stop-marker/no-pid postconditions.
- Release is idempotent for released or never-created state. For retained ownership, release_attempted is set before reconciliation so unknown drain or command effects cannot produce another destructive attempt.
- Positive drain (or no workload ever started), acknowledged recording OFF, and no possible instance/event/arm mutation are required before global observer release.
- Disarm, deletion and instance removal are each marked possible before mutation and confirmed by readback/absence before advancing state. A failed or unacknowledged disarm stops before deletion; a failed deletion stops before instance removal. Later calls refuse a retry.
- A normal-path release failure prevents reaching final health/completed. Release is not just a best-effort success-path cleanup.

This contract concerns the new scheduler observer. It does not claim that all preexisting qualification cleanup operations have been redesigned.

### After-hook and partial effects

**qualification.rb:546-636** preserves the original pre-cleanup snapshots, workload stop/release and CPU restoration sequence. The new observer snapshot is taken first when acknowledged instance ownership exists. The after-hook ensure then attempts the bounded observer release only for an unreleased, incomplete example.

If the guest is unavailable, drain is false/unknown, recording OFF is unacknowledged or a mutation remains possible, it reports incomplete in-guest cleanup and leaves resource lifetime to ordinary failed-VM teardown. It does not assert removal from a Ruby flag, QEMU exit or successful instance removal alone. No foreign cleanup, background cleanup or destructive retry is added.

These branches address the concrete previous mistake of treating setup's unarmed Ruby flag as proof that a timed-out kernel write had no effect. They intentionally prefer incomplete retained guest resources over unverified rollback.

## Runtime evidence and residual limits

I read **package-c-scheduler-capture-runtime-audit.md** in full. Exact13b/run41938327930:
- Reached the declared workload/age under v5; notes/native address, typed event definition and filter writes succeeded.
- Event enable timed out; no arm acknowledgement, recording-on, pre-hotplug operation or counter record followed.
- Private OFF and instance removal succeeded, while global disable/deletion remained unconfirmed. Later ordinary QEMU exit0 proves failed-case VM teardown, not in-guest event removal.
- Wrapper124/replies_consumed and the logged7.78-second interval do not identify shell desynchronization, a kernel wait stack, deadlock or the actual wait duration.

Thus registration preparation is partly observed, but no actual field fetch, record formatting, queue/counter state, loss/miss result or original hotplug health outcome was collected in that run. The old bda1 CPU127 warning remains distinct and unresolved. The fair-server explanation remains a hypothesis. This lifetime change must not be described as its correction.

Early enable can still fail; asynchronous optimization/synchronization may continue later. Loaded private toggles, actual capture, positive late drain/removal and preservation of real failure/teardown remain unproved. No timeout, stress, health or kernel/input adjustment is justified by this review.

## Quick evidence and adequacy

I inspected **package-c-scheduler-lifetime-checks.log** and the actual-method inspector. It loads the real helpers, decoder, example prefix and after-hook; guest I/O is stubbed. The final **44 controls pass**, including:
- Early nop/OFF/enable/readback before the first actual workload boundary; failed enable cannot reach it.
- Recording-only window, original health exception, cancellation identity and missing/loss/miss refusals.
- Preexisting resource refusal, uncertain create/definition/enable/readback and unacknowledged OFF.
- Positive failure-channel drain, unknown drain, one release attempt, uncertain disarm/deletion and no later retry.
- Actual failure-hook snapshot-before-stop ordering and cleanup error precedence; nonselected-profile no-op.

Ruby parse, declared RuboCop and whitespace pass. These are **precommit executions** of the frozen source, not a rerun on b361 or guest validation. I independently matched:
- Source SHA **4013ec1737f2f876382dbc8a84dc28243213ff5209132eb36949c5f256bde20d** to the final committed blob.
- Inspector SHA **b402bfc13008976f5af993b7fc680a937db7586240637eea8c0b5d5360b74e4a**.
- Exact old13b-to-new Git diff to C's saved diff, byte-for-byte, SHA **7f8b3569f07a7a9e0f663044ade2d92cc7238f456ae882be69cda129be8a2eef**.

Normal Bundler Nixfmt/RuboCop/message hooks and the final owner amend/workflow replay pass in A's receipts. No bypass is claimed. Both checkouts/indexes/nonignored-untracked states are clean; independent whole-range whitespace passes. This is adequate quick coverage for committed review before the separately released runtime attempt. It proves the intended local control/error ordering, not kernel synchronization, actual guest state or complete termination.

I reused scheduler-capture-review.md for the unchanged notes/site/BTF/fields/decoder and workflow. The entire source prefix through the decoder is byte-identical; no new metadata query or original-feature audit was needed. Earlier component checks retain their actual input scope; the owning osctld whole-unit suite remains unavailable before examples. No old whole-guest closure or final-head runtime proof transfers merely from unchanged component bytes.

## Complete history, equivalence and migration conclusion

I independently inventoried the final six-purpose evidence series:

1. **8169b8189c29f471b2ecf27a33b6f71dbde5e70e** — current module witnesses.
2. **e1751c917f216897292ab0b893727a6e5553a540** — bounded OSVM boot observation.
3. **645927e22809a29c67ffd59c072e553e05e2a72b** — production shutdown correction.
4. **bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf** — temporary300s age.
5. **538706790c459bfefae4593bf963fa0d37961870** — dying-runqueue observation with lifetime remedy folded.
6. **b361b8c600bc1d50c237a68ca5413d38be9a0e99** — exact one-case workflow replay.

Merge base is assigned2951. Final parents are b361->538706->bda1. Complete range: **26 paths,+3903/-272**; affected bda1-to-new range is two paths,+264/-34. Relative to old13b, only qualification.rb changes,+177/-49. All other **25** feature modes/blobs remain exact.

The first four objects/messages/patches are unchanged. Workflow blob, **full raw patch and message** are exact to13b, patch ID **6387060d6947849d323842ae543dabb6443aba62**. New observation patch ID is **c988d517b1fa341616e371814afabf3208b46ad6**; its message describes early arm/OFF, recording-only window, confirmed drain, uncertain effects and diagnostic-only lineage. Message lines remain within80 columns.

Old13b is preserved by **refs/heads/2026-11-03-livepatch-fixture-failures-tested-13b658f6** and is not an ancestor of the new head. Its prior observation object/provenance remains reachable there. The earlier f412 formatter variant and prior provenance refs remain evidence outside the new series.

**No obsolete implementation, final fixup/WIP, duplicate repair or transitional compatibility path remains in the reviewed six-purpose evidence history.** Folding the caused lifetime correction into the observation owner and replaying the unchanged execution commit preserves distinct logical purposes. The intentional behavior change is explicitly accounted for, not mislabeled a purely equivalent rebase.

**No repeated dependency/channel/input/pin/generated-update streams exist.** Canonical bootstrap dependencies remain baseline2951; there is one final observation owner and one final execution selection, with old iterations retained as evidence refs rather than shipped repair commits.

**No migrations.** There is no new schema/database/on-disk/protocol transition, unapplied intermediate migration, or migration merge/release/deployment/external-use provenance.

Primary delivery remains exact645927, original14400/profile SHA **367dd4ce864b36c4807cb974857d7b58e22b18bb51343ad2724757132da12f2f**. Diagnostic profile remains300/SHA **2fb34cb01efc54b9ec0fa96af20805bbe49bb986c977e5ad86e0b374244411d3**. The three temporary diagnostic purposes remain outside primary ancestry and must remain outside final shipping ancestry. This is not a staging-ready six-commit shipping series.

## Compatibility, documentation and next gate

Only this example and its existing after-hook consume the new lifetime helpers. No public API, runner interface, persistent format, kernel/input pin, CLI, deployment order or fleet update changes. Near-owner comments explain partial effects, one drain check and incomplete cleanup; session design/audit/receipts appropriately retain temporary execution and incident evidence. No product-manual change is required for this diagnostic-only internal lifetime.

Next separately released execution must bind exactb361 and the existing expected-old13b publication lease, then prove:
- Early successful enable/readback with nop/OFF before workload creation.
- Unchanged128CPU/16GiB/100000 tasks and age>=300.
- Private recording around the original CPU127 hotplug, complete frozen-bound fields/records and zero losses/misses.
- Original health result, actual late drain/disarm/delete/instance absence, and ordinary graceful teardown for a passing qualification.

A valid capture with the warning remains RED; incomplete enable/read/cleanup remains incomplete diagnostic evidence. One outcome returns for assessment, with no automatic retry, timeout increase, warning exemption or14400 escalation. Publication may trigger a run; bind the actual eligible exact-head run or one existing dispatch after the ordinary exact-ref/no-duplicate reconciliation.

Final delivery still returns to retained primary lineage with original14400/full workflow, excluding all three diagnostic purposes and any reverts. Preserve tested645927, remove only its isolated skip-message directive through the separately released normal-hooked path, prove final tree/patch/message/history equivalence and apply affected review rules. Require full **exact-final-head native plus all nine rows**, semantic/identity/health/recovery proof and ordinary conditional integration checks. None of the focused/short/one-case results substitutes. No merge, deployment, service or lifecycle action is authorized by this review.

Identity was freshly verified: dev-session current prints the exact bound session; both environment markers are absent and trusted developer binding supplies exact workspace/session/reviewer ownership. Live roster retains reviewer0/thread01a1a24e-920c-7b82-9fff-7754d1f947ab, ready/review-purpose **gpt-6.1-sol/xhigh/read_only**, no override/fallback. Mandatory skill and all four lane references, applicable current workspace/repository routing and Git/verification/commits/package/patch-series guidance were read or reused unchanged in this context.

Read-only source/history/receipt and pinned-source inspection only. No source/session writes, tests/suite/eval/build/VM/network/CI operation, Git mutation, nested reviewer, service or lifecycle action.

**Affected review package complete.** No source fix requested. Root owns saving this full report as scheduler-lifetime-review.md and any separately released reconciliation/publication/one-case execution. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
