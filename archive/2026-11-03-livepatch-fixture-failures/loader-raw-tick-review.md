# Raw proc ticks without host CLK_TCK: final affected review

**No Blocking, Important or Advisory findings.** Removing the unused host-frequency prerequisite is correct within the supported raw-counter contract. Source inspection and the recorded finite controls are adequate for the lead's separately released first runtime of this revision. This is a code-review conclusion, not publication/runtime authorization or qualification, merge or deployment approval.

**Review COMPLETE; session OPEN.** Overall risk HIGH. All four affected lanes completed directly: general, architecture/repetition, scope/proportionality, risk/compatibility.

## Exact scope and verified reviewer

Complete reviewed range: `2951a632c4254a44747a8da326e3dde897eaa0e2..c08a59956c4a905e5a787046251234a615c7e807`.
Affected substantive comparison: `23db05954b7b69c382a696ff6d202d5654c2c52c..c08a59956c4a905e5a787046251234a615c7e807`, exactly two paths,+3/-11.
Final owner parent remains `b361b8c600bc1d50c237a68ca5413d38be9a0e99`.
Complete inventory: seven purposes,27 paths,+4660/-274. Loader owner: four coupled paths,+757/-2.

Before session-file review, dev-session current printed the exact bound session `2026-11-03-livepatch-fixture-failures`. Both DEV_SESSION markers are absent. The trusted developer instruction binds this thread to that exact slug, workspace `/home/aither/workspace/ai/vpsfree.cz`, and reviewer0. The freshly inspected live roster confirms reviewer0 ready, reviewer behavior, review purpose, independent/read_only, `gpt-6.1-sol`/xhigh, thread `01a1a24e-920c-7b82-9fff-7754d1f947ab`. Saved settings retained; no override, fallback, authorship or nested reviewer.

Actual diagnostic checkout HEAD is c08a59956c4a905e5a787046251234a615c7e807 and status is clean. Primary checkout remains clean at645927e22809a29c67ffd59c072e553e05e2a72b. The diagnostic head is not in primary ancestry.

I read the FULL root packet, current mandatory-change-review SKILL and ALL FOUR full lane references, repository AGENTS and full current loader design/implementation sections, C freeze/closed23db audit and controls/checks, A current result/launch/hooks/history evidence. Applicable workspace Git/verification/commits/documentation/package/session guidance, documentation/handoff skills and repository patch policy were read in the current context and reused unchanged; the latest relevant workspace guidance commit remains2b5944e8df2ba06fb3193264c231adafa8329b5c. Prior reports retain their scope for unchanged baseline/clock/ownership, guest event/LC1 and original prefix work; I did not repeat an unrelated full implementation audit.

Reviewer activity was bounded local source, Git/history/hash and receipt inspection plus report delivery. No source/session writes, check/test reruns, eval/build/compiler, VM, network/API/CI, Git mutation, service/lifecycle or cleanup actions occurred.

## Scope and proportionality

The user outcome remains normal current-module qualification with valid semantic witnesses and unchanged health/recovery. Temporary shorter aging is separately bounded; the production shutdown correction was separately approved. Shared-node VPS context motivates avoiding unnecessary node-wide scheduler accounting, but creates neither a performance/safety guarantee nor new product authority.

This revision removes one host command gate with no computational consumer. It does not repair PATH, install a provider, introduce a fallback or second mode, guess100, change node settings, or add SSH, privileges, dependencies, a runner API, kernel correction or framework. It reduces implementation and operational surface while retaining the required evidence boundary. No extra hardening subsystem is warranted.

The two-file +3/-11 delta matches that narrow outcome. Refining the existing seventh loader-evidence owner is appropriate; no new independent purpose or separate caused-repair commit is needed. The four owner paths still implement a coupled diagnostic package: native guest records, owned host samples, existing workflow lifetime and exact-profile thread naming. They remain distinct from the earlier dying-runqueue purpose and outside shipping ancestry.

## General correctness and actual consumers

The exact diff removes unused ticks/tick_status locals and the host getconf CLK_TCK invocation, exit/value validation and associated readiness failures from `tests/suite/kernel/livepatch-6.12.95/loader_host_sched.sh`. At current line249, the header explicitly states:
`CLK_TCK=UNAVAILABLE cpu_units=proc_stat_ticks`.
The only qualification change is the summary at `qualification.rb:575`, which states the same units/frequency limitation.

I searched actual source/consumers and inspected the preserved relevant functions. No hidden frequency consumer exists:
- The helper's :157-164 logic compares user/system raw counters only for the same TID/start identity. It performs no conversion to seconds, percentage, rate or resolution.
- Its :55-82 clock/cap functions use elapsed runner-visible uptime from the pre-child wrapper origin; they do not use process-start ticks divided by CLK_TCK.
- Qualification consumes the existing ready/map/status records, not a numeric frequency or sample counters.
- The workflow invokes the helper and consumes sampling/completion/error status; it does not convert CPU measurements.

Removing the gate therefore cannot leave an undefined frequency variable in a surviving calculation or invalidate the elapsed cap. The raw-counter field meanings remain explicit without claiming a known frequency. Same-identity zero counters remain valid; increases indicate only raw tick progress, and decreases mark that interval unavailable. No cross-host rate comparison is supported.

Guest getconf _NPROCESSORS_ONLN assertions are byte-preserved and remain required. The change is host-specific; it does not weaken guest CPU-count assertions.

The full helper prefix before loader_main and its snapshot-and-later ready/sampling/cancel/status/lifetime tail are independently byte-equal to23db. Qualification is summary-only. Thus required PID/start/executable/ancestry, bounded stat/state/processor/raw user/sys validation,128-vCPU/APIC mapping, optional bounded switch counts, zero/decrease handling, cap/clock checks and original required error semantics remain. Runtime/wait/slices remain UNAVAILABLE on every node, with no opportunistic statistics mode.

The workflow and common.nix are byte-identical to23db. Their wrapper-origin, EXIT/join, original failure/cancellation precedence, nominal-success completion guard and exact naming selector are unchanged. The LC1 marker command, five guest events, first-fault freeze/join, loss/no-overwrite semantics, shared1800-second budget, full stress, health, positive drain and uncertain-effect cleanup contracts are unchanged.

## Architecture, compatibility, privacy and documentation

The owning boundary remains one private diagnostic helper/example and its temporary workflow. Discovery found no public runner/OSVM API or external numeric-frequency consumer to migrate. Ready/map/status grammar is unchanged; only descriptive temporary evidence metadata becomes explicit about unavailable frequency. Old logs remain tied to their exact old revisions rather than reinterpreted as new-contract passes.

No new host reads, writes, privileges, process discovery or cleanup are introduced. The unchanged helper reads only owned proc identities/counters, not scheduler-statistics sysctls or schedstat files. Optional status is bounded and prints only the two numeric fields/fixed unavailable reasons. No argv/environment/raw status content or unrelated host process scan is added. No coordinated node/fleet update is required.

Current source header/qualification summary and owner message explain raw units and unavailable metrics. Updated design/implementation sections preserve the rationale and prohibit CPU-duration/percentage/rate/resolution, runnable-wait/starvation or callback-cause claims. Temporary branch/failure/check facts appropriately remain in session records. No public manual/API or new general operational documentation is needed for this temporary two-line evidence contract.

## Verification assessment

I inspected actual control code and RED/GREEN logs, not only totals. The new control-file hashes match the check receipt:
- helper controls:2ae9f305e41242eb37415b03a7e19261086e9eba8869219fff8abc45086f478f;
- qualification controls:d930f484bdb789cbfc436a1e24f6454eb3ddb600b743c0806e2e7aff4e68d391;
- wrapper controls:f3cad130b54eef5dc951748d08b11bc05eded9cd908df0af43759996508324fd.

The representative RED control on unchanged23db supplies the helper's existing standard utilities while deliberately omitting getconf. The helper records command status127 and fails to acknowledge readiness; the control exits1, not timeout. The actual qualification-summary control separately rejects the old positive-frequency wording. This exercises the real obsolete prerequisite rather than an empty-PATH model.

The GREEN actual-helper controls retain those standard utilities and establish ready/map/completion without getconf. A second fixture exposes a failing, recording getconf sentinel; completion and cancellation leave it uncalled. The controls also cover raw zero/increased/decreased counters, optional switch bounds/faults, disabled/absent stats and never-opened FIFO canaries, identity/stat/map failures, clock regressions/stalls/uncertainty, resource caps and reaped fixture children.

Fresh finite total is80:
-28 actual proc/helper controls;
-41 actual qualification controls, including the new printed summary through the real prepare/ready/status method and retained APIC, LC1 actual-exec, event/loss/freeze, original error/cancel/drain and bracket controls;
-11 actual wrapper/origin/EXIT controls, including complete workflow equality to tested23db, origin before both stub children, nominal success/missing coverage, original failure/cancellation and stop-marker error.

The controls are proportional and adequate quick evidence for the next separately authorized runtime. They are not real proc/QEMU/tracefs or guest acceptance. I ran none of them.

The recorded cached Ruby/Bash/rendered-workflow/YAML/whitespace and declared one-file RuboCop checks pass. Normal amend hooks show Nixfmt/RuboCop and all message checks PASS, exit0 at10:31:01.892333Z; explicit Git release follows at10:31:02.121162Z. Exact frozen source/diff hashes match committed bytes, supporting reuse of those precommit checks for their recorded input scope. No hook bypass, source-format drift or provider installation is indicated.

Earlier44 and unchanged workflow/common evidence retain only exact component/control/tool scope, not additional fresh passes. Unchanged official action metadata is reused within that scope. Shellcheck remains unavailable without installation. No Nix module evaluation, native CI, VM or actual new-head readiness is claimed. The broader osctld suite remains unavailable before examples as already assessed; this revision does not repair or relabel that gap.

## Old runtime evidence and residual limits

I read the CLOSED23db/run42003244138 audit, its independent-verification JSON and actual retained inventory. They record183446bytes, SHA256d10f51ddba4c53ba98e77d74b965d400289a1475972eadb11d98f34e61cc4ea5, and21 unique relative regular members. The correction from a relay's20 to the actual21 is transparent and not a product failure; I did not download or extract artifacts.

That run's first example failure is host CLK_TCK command status127, before the first baseline header/snapshot/ready/map, workload or new CSD setup/activation/LC1 execution. It establishes failed command execution, not the exact PATH/provider/interpreter cause. Operator-login100 is not that job's value. Removing an unused prerequisite does not require speculative environment repair and does not retroactively pass the failed run.

The launch metadata does not prove the later full QEMU/TID identity snapshot or naming/APIC map. Earlier observer setup and pre-workload release0, recovery0 and QEMU0/SIGNAL NONE establish only their limited failed-VM cleanup observations. They establish no baseline, complete aligned host window, new guest capture or qualification health pass.

Old9805's combined gate, b361's healthy CPU127 instant then first-EBUSY loader/TLB fault, second EBUSY and third timeout with unknown PID, bda warning,13b setup failure and5235 incidents remain separate/unwaived. This change supplies no historical root-cause attribution.

Actual c08 runtime must still establish ordinary proc permissions and usable required data, exact QEMU labels/owned identity/APIC-TID readiness, valid named clocks and sample coverage, native event formats/filters, actual attempt/PID execution, first-fault freeze/loss history, original stress/shared1800 deadline/cumulative health, positive drain, observer release and graceful teardown.

Raw ticks/switches provide coarse thread progress only. Unknown frequency forbids CPU-duration, percentage, resolution or cross-host rate claims. Even with frequency, sampled state R or no tick growth would not prove continuous runnable wait, starvation, descheduling cause or a specific guest callback. Queue is not dispatch/delivery; target PID is interrupted context; token reuse/loss and missing clock associations retain their existing limits. Complete RED diagnostics are progress, not qualification; a clean nonrecurrence does not explain prior faults.

## Independent full-history and migration conclusion

I inspected the full ordered base-to-head series and final inventory:
1.8169b8189c29f471b2ecf27a33b6f71dbde5e70e: current-module semantic witnesses.
2.e1751c917f216897292ab0b893727a6e5553a540: bounded OSVM host boot evidence.
3.645927e22809a29c67ffd59c072e553e05e2a72b: separately approved shutdown coordination.
4.bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf: temporary300-second aging.
5.538706790c459bfefae4593bf963fa0d37961870: dying-runqueue observation/lifetime.
6.b361b8c600bc1d50c237a68ca5413d38be9a0e99: temporary one-case workflow.
7.c08a59956c4a905e5a787046251234a615c7e807: loader CSD/owned-vCPU raw-tick evidence.

The first six exact objects are unchanged from23db, preserving their raw messages/patches. The refinement is folded into the seventh coherent owner, whose message truthfully describes final raw-counter behavior and limits. The two-file comparison is intentional contract change, not mechanical equivalence or an LC1 step9 exemption.

**No obsolete implementation, final fixup/WIP, separate caused-repair history or abandoned compatibility mode remains in2951..c08.** The unused frequency gate is absent from final source and not retained as another commit. Tested23db is preserved at the exact ordinary local provenance ref and is not an ancestor ofc08. Reviewed12df/tested9805 and the other retained provenance refs remain separate from final shipping source. All12 local provenance refs were present on inspection.

**No repeated dependency/channel/input/pin/generated-update streams exist in this feature range.** Canonical rake-compiler updates belong to base2951. Repeated workflow/qualification edits here have distinct witness/diagnostic purposes rather than redundant dependency streams.

**No migrations.** The full path/behavior inventory adds no database/schema/seed, persisted service/on-disk format or public protocol migration. No intermediate migration was merged, released, deployed or externally consumed; there is no transitional lineage or predecessor-schema shim to preserve. Temporary run-local evidence metadata is not a supported persisted mixed-version service contract.

The four diagnostic purposes4-7 remain outside primary645927/final shipping ancestry. They must not be merged/cherry-picked then reverted into delivery. Separate provenance refs and raw incident records preserve development evidence without retaining obsolete implementations in the shipping series.

## Independent source bindings and disposition

Committed/working/frozen SHA256 equality independently verified:
- helper6e03390f52ff9c6e525f5abf6f908794c1533fea53deeaa30f2ee99a1960f815;
- qualification81e6192a0ddbfaa5fce6fc33af82954e00496a822d54c285f480143bbdf7025a;
- unchanged workflowac0b3bc76cb82de019fd94f0cd3cfcedf117ea1a83239dcc540847ec51de460e;
- unchanged common8acb93d5d59568b65e35e0a7fb436ce1354da149a5b882b7e66f9e94518c0509.

All modes100644; helper is invoked through Bash. Actual old23db..new Git binary diff is byte-equal to C's saved diff, SHA256e97b88f8999f0cf5b17d6577de3a857f757e8f5ace0af22cacc2256ac25bc51f.
Owner patch ID7e76a06e8073edf8e80868569df212ab94e74988 and raw message SHA256cc01f96f132bb9bdfbc0fd6a3e64d4aab580d26eb2536f2e0856d6b1b0fccc95 match the packet.

**Affected committed code-review gate: PASS with the stated runtime limits.** Root owns reconciliation, saving this report and any separately released publication/ONE-case run. No automatic retry, warning waiver, timeout extension, kernel correction or14400 escalation follows.

Final shipping still requires primary/original14400/full workflow, exclusion of all four diagnostic purposes, later normal-hooked removal of the isolated production skip paragraph with final history/equivalence preparation, actual exact-FINAL-head native plus all nine semantic/identity/health/recovery cases, ordinary integration checks and applicable user direction. A message-only push is not assumed to trigger path-filtered CI. No merge/deploy/service/lifecycle action is authorized. Reviewer assignment COMPLETE; session OPEN.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
