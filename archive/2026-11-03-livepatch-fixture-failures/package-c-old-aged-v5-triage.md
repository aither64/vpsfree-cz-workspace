# Old-5235 aged-v5 failure triage

Read-only diagnostic of run `41773470432`, attempt 1, aged-v5 job
`126392676352`, source `5235bfd57c92bc05a25946937fe77f9803fe1c93`.
This is not a result from current e175 run `41865572140`. Binding/env, retained
implementer3 Sol/xhigh/workspace-write roster and current verification guidance
were rechecked. No API request, download, test, build, guest or Git action.

Artifact `13339254852`: independently verified 1769854 bytes and ZIP SHA-256
`d3c122101b7b02caeb56e5cf4c14aa2e0eae42527877ce3e55bd9a759d40341c`.
The supplied list has 16 safe relative members. Only runner/result/test log,
identity/sites/SHA and the 38 KiB prebuild context were extracted to
`package-c-old-aged-v5-evidence/`, plus bounded numbered console fault context
and the first 110 failure-diagnostic lines. No large shell logs were extracted.

Identity binds normal producer `qi47yi2...livepatch_7`, module SHA
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`,
sites `aiqijlwh...`, input-lock SHA
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
Extracted site bytes independently hash to
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.
`test-result.txt` says `unexpected_failure`.

## Primary and timeline

The earliest reported test failure is a genuine cumulative kernel-health
assertion, not a timeout/cancellation exception. Runner lines 104–110 report
that dmesg unexpectedly matches the existing BUG/WARNING/stall/hung-task regex.
The first matching fault in that captured interval is at runner 138–177:

- Guest uptime `14925.356780`: soft lockup, CPU 25 stuck 23 seconds in
  `insmod:9997`, release `6.12.95.5`.
- RIP `smp_call_function_many_cond`; stack includes cross-CPU TLB work,
  `set_memory_rox`, `module_enable_text_rox`, `load_module`.
- Later stack-recursion warnings, RCU stalls and hung tasks are also present.

The bounded console excerpt independently contains that first fault (original
console line 165 onward). The test does not fail merely because a command
took a long time: activation completes in 1061.789 seconds under its 1800-second
ceiling, and all declared transition/callback trace counts match (runner
6555–6576). Post-transition CPU-127 hotplug then checks cumulative health and
fails (6577–6578). Source mapping is the existing `qualification_hotplug`
health assertion at `livepatch-6.12.95/qualification.rb:245`, invoked after
activation at line 509. Eventual patching completion cannot erase prior faults.

| Recorded event | UTC |
| --- | --- |
| Primary example assertion, runner/test.log | 2026-11-04 15:50:30 |
| Generic `run_examples` exception and diagnostic capture | 15:50:47 |
| Failed test summary | 15:51:06 |
| A publication push starts/finishes | 16:16:24 / 16:16:29 |
| New run created / initial job started | 16:16:30 / 16:16:31 |
| Single old-run cancellation request | After the above ordered reads; exact instant not separately timestamped |

The original log offsets are explicit `+0100`; conversion above removes that
hour. `package-a-e175-publication.log:25–46` places the request after the
16:16:31Z job observation. Thus the primary assertion precedes cancellation
by more than 26 minutes, regardless of the missing exact request timestamp.
The generic runner exception is secondary; no raw-job evidence is available
to classify later upload/evaluation or cancellation/cleanup step outcomes.

## Classification and next owner

The recorded envelope is v5 predecessor, 100000 tasks, 128 guest vCPUs and
16 GiB guest memory, aged beyond four hours. Diagnostic capture at 15:50:47Z
shows the guest alive on release `6.12.95.7`, with load averages around 134–142
and about 10 GiB available memory after the event. These snapshots do not
establish host scheduling, the initiating defect or fault causality.

This is a real old-head qualification/kernel-loader liveness failure, separate
from C's corrected symbol lookup and its accepted fragment/FUSE/TCP evidence.
The existing health guard correctly refuses the faulted run. There is no
narrow consumer/selector correction justified here, and no claim that current
e175 has failed or passed. The lead's unchanged feature-source lineage does
not turn the old failed attempt into new-head acceptance.

If further action is needed, route the kernel-loader/qualification liveness
question under this declared envelope to the architect/kernel owner; the
artifact does not distinguish a kernel defect from scheduling/resource stress.
No design change, weaker warning filter, rerun or waiver is proposed by C.
The factual triage is settled and stopped; the lead owns the next action.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
