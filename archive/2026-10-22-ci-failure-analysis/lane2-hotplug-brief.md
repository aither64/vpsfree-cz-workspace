# Lane 2: AMD aged-scale CPU-hotplug warning

Owner: implementer2. Read [design.md](design.md) in full. Write only
`hotplug-findings.md` and `evidence/hotplug/` under this session.

Verify `dev-session current`, environment and trusted binding to
`2026-10-22-ci-failure-analysis` at `/home/aither/workspace/ai/vpsfree.cz`.
Stop/report mismatch. Read workspace AGENTS.md; full sessions, lifecycle,
documentation, projects, git, verification and commits procedures;
`docs/agent-teams.md`; documentation skill at
`~/.codex/skills/dev-session-documentation/SKILL.md`. Read exact vpsadminos
AGENTS.md using `git --git-dir=repos/vpsadminos.git show 846bb469505789ba0b2a405fa5905ba6d8253006:AGENTS.md`.
Read relevant `docs/os/testing.md`, `docs/os/updates.md`,
`docs/os/livepatches/6.12.95.md` and frozen boot/livepatch package contracts.
Check for Linux repository instructions at the exact inspected revision. If
there is no AGENTS.md, workspace/reference guidance and relevant in-tree source
documentation apply; its absence does not block read-only inspection. No
separate Linux instruction path is specified here. Linux stays reference only,
with no source/build changes.

Start from read-only `../2026-10-20-kernel-check/generic-sysctl-ci-failure.md`,
design's AMD hotplug warning section, and preserved AMD artifact root in plan
for run 39767770407/job 119793311395. Do not observe that run remotely.

Trace first CPU127 offline under v6 on current 846bb OS, frozen 6.12.95 boot
source `a2384967b90f24d2470c9eb15f0e66d938df7e08`, and exact effective v6
module. Relevant sources: `tests/suite/kernel/livepatch-qualification.nix`,
`livepatch-6.12.95-common.nix`, `livepatch-6.12.95/qualification.rb`,
`os/packages/linux/boot-6.12.95.nix`, Linux scheduler/hotplug callback path.
Use recorded binary/toolchain/source identity rather than uname alone.

Explain `rq->nr_running != 1 || rq_has_pinned_tasks(rq)` at teardown and why
the callback still returns zero. The dump's count two and named migration/127
do not prove a second task exists or identify pin state: deadline/fair-server
entities can contribute to runqueue accounting without a task_struct. Include
their lifecycle and the server stop after the warning. Use source and retained logs to
narrow wakeup, callback order, affinity/pinning or accounting explanations only
as far as evidence permits. Assess whether available traces can identify the
owner. Avoid broad kernel or production-hang attribution.

Preserve timing: warning occurs before incoming v7 insertion; later activation
757.998s and second hotplug succeed. The post-transition no-fault assertion
correctly retains the earlier warning. The subsequent move back to cgroup B,
corrected-patch disable/unload and normal stopped-task checks do not execute;
this attempt does not establish full end-of-scenario or downgrade health.
An earlier health checkpoint after first hotplug may localize the failure while
retaining cumulative dmesg history and all required later no-fault checks.
Current generic service could apply at boot;
service presence/down and later stress sysctl writes do not prove actual
earlier values or causal exclusion. This is not a hardlockup/panic report.

Send exact signature/source boundaries to historical collector implementer3,
request shared artifacts there and avoid duplicate downloads. Provide plain
test purpose, why aged 128-CPU stress/hotplug matters, actual assertion coverage,
cost and phase diagnostics, and a justified keep/revise/remove recommendation.
Separate pre-transition health, activation correctness and post-transition
health without suppressing faults. Propose exact smallest discriminating trace
capture through first hotplug, with budgets/loss accounting, source identities
and required authorization; identify if instrumentation needs a separate kernel
build. Preserve quarantine/ABI/recovery constraints. No diagnostic execution.

Findings require exact log/source citations, evidence strength, remaining
unknowns, prioritized proposals and regression acceptance for hotplug invariants,
transition bounds and final health. No Git mutations, code/tests/builds/VMs,
reruns, operations, merges, deployment, pins or lifecycle actions. Lead owns
shared records/index/commits. Report blockers/results using report_to_lead with
unique IDs; send architectural deviations and finding path to architect0 using
verified peer messaging. Retain saved settings; no automatic review.
