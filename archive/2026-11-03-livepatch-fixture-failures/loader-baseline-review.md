# Owned-vCPU baseline and clock contract: final affected review

**No Blocking, Important or Advisory findings.** The committed baseline revision is proportionate to the demonstrated host prerequisite failure and shared-node deployment context. Source inspection and the recorded finite controls are adequate to proceed to the lead's separately released publication and ONE exact-head diagnostic runtime. This review does not authorize those actions, establish runtime acceptance, or clear qualification, merge or deployment gates.

**Review COMPLETE; session OPEN.** Overall risk HIGH. Lanes completed directly: general, architecture/repetition, scope/proportionality, and risk/compatibility.

## Exact range, identity and method

- Complete reviewed diagnostic series: `2951a632c4254a44747a8da326e3dde897eaa0e2..23db05954b7b69c382a696ff6d202d5654c2c52c`.
- Substantive affected comparison: `9805ea20e336aa6e2559f5f7af73de36fce3ecc8..23db05954b7b69c382a696ff6d202d5654c2c52c`, exactly three paths, +158/-38.
- Final owner parent: `b361b8c600bc1d50c237a68ca5413d38be9a0e99`. New owner: four coupled paths, +765/-2. Complete series: seven purposes, 27 paths, +4668/-274.
- Diagnostic checkout: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos-diagnostic-300s`. Actual HEAD matches the packet and its index/tracked/nonignored-untracked status is clean.
- Primary checkout remains clean at `645927e22809a29c67ffd59c072e553e05e2a72b`; the diagnostic head is not its ancestor.
- Before session-file inspection, `dev-session current` printed the exact bound slug `2026-11-03-livepatch-fixture-failures`. Both DEV_SESSION markers are absent, consistent with the trusted developer instruction binding this thread to that exact session and absolute workspace `/home/aither/workspace/ai/vpsfree.cz`.
- Live same-session roster independently inspected: reviewer0, ready, review purpose, reviewer behavior, read_only, `gpt-6.1-sol`, xhigh, thread `01a1a24e-920c-7b82-9fff-7754d1f947ab`. Settings retained; no override, fallback, nested reviewer or authorship of the changes.

I read the FULL packet, mandatory-change-review SKILL and ALL FOUR full references, current applicable workspace/repository guidance, design/implementation sections, C/A receipts, actual controls and raw logs, LC1 reconciliation and old9805 runtime audit. I inspected source, current consumers and complete history directly. Earlier independent reviews retain their scope for the unchanged prefix; no unrelated implementation audit was repeated.

All reviewer operations were bounded local reads, Git/history/hash inspections and report delivery. No test/check rerun, evaluation, build/compiler, VM, network/API/CI operation, Git mutation, source/session write, service, lifecycle or cleanup action occurred.

## Scope and proportionality

The user outcome remains current-module qualification with valid witnesses and unchanged health/recovery. Shorter aging and temporary diagnostics relate to demonstrated failures; the separately approved production shutdown correction stays separate. Internal design acceptance does not add product authority.

The new revision removes a node-wide scheduler-accounting prerequisite after the operator explained that the runners are VPSs sharing a vpsAdminOS node. It introduces one ordinary owned-proc baseline, not a second collector mode or an automatic infrastructure repair. It neither reads nor changes the scheduler-statistics setting and does not add SSH, privileges, dependencies, a runner API, kernel correction, broader tracing, workload reduction, timeout increase or health waiver.

The added clock handling corrects a real assumption in the former cap: process-start ticks and runner-visible uptime must not be presumed to have one usable absolute origin in a container/proc view. Capturing an earlier same-view origin in the existing wrapper is a small conventional correction. Labelled command intervals and explicit unavailable measurements are sufficient for this supported evidence boundary; no general clock calibration, scheduler monitor or compatibility framework is needed.

The +158/-38 refinement stays in its actual consumers. Helper, wrapper and qualification need the already accepted exact-profile naming option to establish one coupled guest/host evidence package. Their seventh purpose is coherent and distinct from dying-runqueue observation and shipping behavior.

## General correctness and failure handling

At `loader_host_sched.sh:7-21,118-176,249-258`, required stat records retain bounded reads, field validation and nonnegative bounded integer CPU ticks. The positional fields still correspond to PPID, user/system ticks, thread count, start identity and processor. Zero initial counters are accepted. CLK_TCK is now checked independently, logged as CPU units, and has distinct bounded diagnoses for command failure versus invalid/zero output.

The helper contains no sysctl or per-TID schedstat read path. At :87-115 it reads only two supplemental status fields through the already pinned owned TID directory, with a 16-KiB limit plus overflow byte and a subsequent identity recheck. Missing/unreadable, duplicate, malformed or oversized observations become fixed-reason UNAVAILABLE; they do not destroy a valid required baseline or become fabricated zero counts. Full status contents, argv, environment, arbitrary comm strings and exception text are not emitted by this new path.

At :157-164, CPU comparisons are keyed by TID and start identity. A decrease labels the affected interval unavailable, while preserving raw tick observations. Subsequent intervals use their own baseline. Every row explicitly retains `runtime=UNAVAILABLE wait=UNAVAILABLE slices=UNAVAILABLE`, even if node accounting happens to be enabled. No opportunistic second mode or numerical wait substitute remains.

Pinned local Linux a2384967b90f24d2470c9eb15f0e66d938df7e08 confirms ordinary per-task CPU/switch fields (fs/proc/array.c, kernel/sched/core.c), their independence from dynamic schedstats, and possible zero schedstat output when accounting is off (fs/proc/base.c). This does not establish the actual node kernel, proc virtualization, permissions or overhead.

The actual consumers discovered by source search remain the one workflow, this helper and this qualification example. Ruby consumes the existing ready/map/status grammar, not numeric sample counters. `qualification.rb:560-580` still requires acknowledged ready data, the full validated guest APIC-to-owned-TID map and status exactly sampling before workload. :776-777 rejects missing required host coverage during capture. The wrapper still joins the sampler and requires complete status for an otherwise successful result.

The entire LC1-protected command is byte-identical to9805: :644-651 preserves exclusive per-attempt PID files under set-C and uses `>|` only for the preexisting trace_marker. I inspected the representative existing-marker, distinct-attempt and duplicate-file controls; this review does not reopen the earlier rejected marker implementation or presume LC1 runtime execution.

## Clocks, coverage and ownership

At `.github/workflows/ci.yml:515-537`, the wrapper records validated runner-visible uptime with a wall read bracket before starting either sampler or test child, then passes that origin as the fourth private argument. Invalid origin/wall observations stop before those children. This does not add an ambient Ruby requirement.

At `loader_host_sched.sh:55-82,123-128,217-230`, the cap uses only elapsed runner-proc-uptime from that wrapper origin, including preparation. Start ticks remain identity tokens; removal of old cross-process start-order arithmetic does not remove the actual ancestry/start/executable checks. Observations reject invalid/regressing required clocks and cap expiry. Required polling and sample intervals must progress; snapshot internal observations may be equal at finite resolution. Integer conversions are bounded within the signed arithmetic range.

Samples record begin/end times and gaps in named clock views. Two seconds is a target including collection/scheduling gaps. The elapsed cap is enforced at observation boundaries; it is not hard real-time cancellation of arbitrary kernel operations.

At `qualification.rb:560-574,624-641,654-668,899-909`, host request/ready, guest clock commands, freeze and returned activation attempts have labelled wall/monotonic send/reply intervals. Missing, malformed, nonfinite or regressing command brackets fail explicitly. A timed-out attempt prints reply unavailable and warns that the command may remain active; it is not assigned a fabricated completion time. The new calls remain within original error handling and do not turn a diagnostic error into a successful activation.

No cross-base subtraction equates proc uptime, process-start ticks, Ruby monotonic, wall time or guest trace time. Forward wall changes remain recorded uncertainty, not calibrated offsets or evidence of descheduling. A valid bracket establishes an interval association, not simultaneous samples or a point conversion. The first acknowledged snapshot is bounded by the request/ready interval; later whole-window alignment and gaps must be assessed from actual runtime data. Missing relations cannot support a complete aligned fault-window claim.

Existing exact job-child ancestry, QEMU PID/start/executable identity, pinned proc directories, 128 unique vCPU identities and stable map checks remain. The new optional fields are read only inside those owned directories. The existing 256-thread, 64-MiB output and finite elapsed bounds remain. No unrelated host process discovery or cleanup is introduced.

The actual workflow EXIT function is unchanged. It writes its own stop marker, waits only for its saved sampler child, preserves original failure/cancellation and turns nominal success into failure when required completion is absent. Guest observer join/freeze and post-drain release/uncertain-effect guards are unaffected. Source evidence supports these ownership/error contracts; actual cancellation and final runtime coverage remain separately observable facts.

## Verification adequacy and residual gaps

I inspected actual controls and raw logs:
- 40 Ruby controls cover extracted qualification methods, map/trace validation, error/cancel ownership, real LC1 command execution with an existing marker and matching PIDs, and invalid/regressing/missing/nonfinite clock brackets.
- 29 actual-helper proc controls cover zero ticks/switches, disabled/absent stats and never-opened FIFO canaries, optional-field bounds, CPU decreases, required identity/stat/map failures, caps, distinct CLK_TCK errors, unrelated start/uptime bases, clock regression/stall/forward-wall uncertainty and reaped ready/complete/cancel fixtures.
- 11 actual-wrapper controls establish origin before both stub children, invalid-origin rejection before children, and unchanged EXIT completion/error/cancel/stop-marker outcomes.

That is **80 fresh finite controls**, not guest/kernel passes. They are useful coverage of the revised owned contract and adequate for the first separately authorized runtime. They do not simulate or prove real QEMU/proc/tracefs behavior.

The retained initial wrapper failure was a relative-CWD fixture error corrected only in that control. Parse, rendered Bash/YAML, whitespace and declared RuboCop receipts pass. Normal Nixfmt/RuboCop/message hooks ended PASS at09:10:09.056682Z. I matched their frozen bytes to committed source and reran no checks.

Earlier44 observer controls and unchanged common.nix parse/nixfmt/selector evidence are reused only for their unchanged component/tool inputs, not added as fresh passes. Official unchanged action metadata retains its recorded compatibility scope. Shellcheck remains unavailable; syntax checks, actual finite Bash/wrapper controls and direct inspection provide the available quick coverage without installing tooling. No Nix module evaluation, new package realization, native CI or VM execution is claimed. The broader osctld unit-suite preload gap remains transparent and is unaffected by this diagnostic revision.

Actual next-runtime gates remain:
ordinary runner permissions and proc values; positive usable CLK_TCK and actual clock views; exact QEMU labels/topology and guest APIC-to-TID association; acknowledged native event formats/filters and early setup; attempt/PID execution; first-fault freeze and loss bounds; complete usable host timestamps/gaps through the activation window; original stress, shared1800-second activation budget, cumulative kernel health, positive workload drain, observer release and graceful teardown.

CPU-time or switch growth proves coarse thread progress, not execution of a particular guest callback. Sampled state R or a processor field cannot prove continuous runnable state or execution at that instant. No growth at finite tick/sample resolution cannot prove starvation. This baseline cannot measure runnable-wait duration or distinguish host descheduling, KVM/blocking behavior and guest causes by itself. There is no performance or shared-node safety guarantee.

## Old runtime evidence remains separate

The9805/run41972655273 audit establishes an early failure at the combined stats/CLK gate, before the first complete host snapshot/map, workload, loader events or activation. Neither original capability value was logged. Later operator stats0/CLK_TCK100 cannot recover them or retroactively pass that run. Its launch line does not prove later identity/TID validation. There is no host baseline, observed naming/map, CSD, LC1 execution, health qualification or complete window. Pre-workload observer removal and normal QEMU0 establish only failed-VM teardown.

The earlier b361 healthy CPU127 sample and later first EBUSY loader/TLB softlockup remain distinct from the second EBUSY and third timeout with unknown PID. The bda scheduler warning,13b setup timeout and5235 incidents remain separate and unwaived. Neither source review, complete RED diagnostics nor later clean nonrecurrence establishes their root cause.

## Independent whole-history, consolidation and migration conclusion

I independently inspected the complete ordered series, messages, final path/stat inventory and old/new ownership. The seven purposes are:

1. `8169b8189c29f471b2ecf27a33b6f71dbde5e70e`: current-module semantic witnesses.
2. `e1751c917f216897292ab0b893727a6e5553a540`: bounded OSVM host boot evidence.
3. `645927e22809a29c67ffd59c072e553e05e2a72b`: separately approved shutdown coordination.
4. `bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`: temporary300-second aging.
5. `538706790c459bfefae4593bf963fa0d37961870`: dying-runqueue observation and its final lifetime.
6. `b361b8c600bc1d50c237a68ca5413d38be9a0e99`: temporary one-case execution selection.
7. `23db05954b7b69c382a696ff6d202d5654c2c52c`: loader CSD/IPI with baseline owned-vCPU progress.

The first six exact objects remain identical to9805, which also preserves their messages/patches. Only the final owner is revised; the three-path affected diff is intentional behavior change, not mechanical equivalence. The four coupled owner paths remain one coherent evidence purpose. The final source directly implements the baseline contract: the superseded stats1 requirement and LC1 defect are absent, and there is no second compatibility mode.

**No obsolete implementation, final fixup/WIP or separately retained caused-repair history remains in2951..23db.** Folding this refinement into its loader owner follows patch ownership policy. Tested9805 and reviewed12df remain exact local provenance refs outside the new ancestry; the other nine local provenance refs also remain. Keeping those refs and incident records does not put obsolete source back into the shipping series.

**No repeated dependency/channel/input/pin/generated-update stream exists in the seven-commit feature range.** Canonical rake-compiler updates are in base2951, not feature repins. Repeated edits to workflow/qualification here implement distinct diagnostic or witness purposes, not redundant dependency streams.

**No migrations.** The complete inventory introduces no database/schema/seed, persistent format or service-protocol migration, and no intermediate migration was merged, released, deployed or externally consumed. There is no transitional migration lineage or predecessor-schema shim to preserve. Temporary diagnostic state files are run-local evidence, not a supported mixed-version persistence contract.

All four diagnostic purposes4-7 remain outside primary645927/final shipping ancestry. They must not be integrated then reverted as a shipping route. No coordinated fleet/node update is required by the revised baseline; it changes only this diagnostic branch's private helper/wrapper/summary. Enduring limitations are present in source comments/evidence summaries; temporary branch/operator/incident facts appropriately remain in the session design and receipts. No new public manual/API or generic operations framework is warranted.

## Independent bindings and disposition

Committed source hashes independently matched the frozen receipt and working files:
- helper: fcb8f61fa90d043569410e015cfcafef56caa4d271bb4c336e7bdfce42b7ead4;
- qualification: f95be083743443da04a429c26b4c70557d1e75b8a287df022dd6c204ceeb9959;
- workflow: ac0b3bc76cb82de019fd94f0cd3cfcedf117ea1a83239dcc540847ec51de460e;
- unchanged common: 8acb93d5d59568b65e35e0a7fb436ce1354da149a5b882b7e66f9e94518c0509.

All four modes are100644; helper is invoked through Bash. Actual old9805..new Git binary diff is byte-equal to C's saved diff, SHA2563c429a3cfc7107170d2ac1abf12c7ba9858fbc27c2db261a9c699a9af5342f8d. Owner stable patch ID309ee50cf14d57ae702cd0edad53b7708558612d and raw message SHA25623ce6016c5707d7fa5870243948fd88186550a40490defc40c293ad42285c884 match the packet. Earlier observer prefix, five event definitions and entire LC1 attempt method are byte-identical to9805; no other feature path changed.

**Code-review gate: PASS for this affected committed revision, subject to the existing separately released ONE-case diagnostic route and all stated runtime limits.** No automatic rerun, publication, warning waiver, kernel correction,14400 escalation, merge or deployment follows.

Final shipping still returns to primary/original14400/full workflow, excludes the four diagnostic purposes, removes the isolated production skip paragraph through the separately prepared normal-hooked message path, and requires exact-final-head native plus all nine semantic/identity/health/recovery cases and ordinary integration approval/checks. Path-filtered CI must actually execute or be explicitly reconciled; review is not proof that a message-only push triggers it. Root owns reconciliation, saving this report and any later release. Reviewer work is COMPLETE and the session remains OPEN.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
