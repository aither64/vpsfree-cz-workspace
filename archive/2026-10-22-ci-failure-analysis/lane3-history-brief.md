# Lane 3: historical recurrence and independent test utility

Owner: implementer3, sole historical GitHub metadata/log/artifact collector.
Read [design.md](design.md) in full. Write only `history-findings.md`,
`recurrence.tsv` and `evidence/history/` under this session. Other owners write
their own findings and source excerpts. Share immutable downloaded paths with
implementer0 (impermanence), implementer1 (Podman) and implementer2 (hotplug).

Verify `dev-session current`, environment and trusted binding to
`2026-10-22-ci-failure-analysis`, `/home/aither/workspace/ai/vpsfree.cz`.
Stop/report mismatches. Read workspace AGENTS.md; full sessions, lifecycle,
documentation, projects, git, verification and commits procedures;
`docs/agent-teams.md`; `~/.codex/skills/dev-session-documentation/SKILL.md`.
Read exact vpsadminos AGENTS.md with
`git --git-dir=repos/vpsadminos.git show 846bb469505789ba0b2a405fa5905ba6d8253006:AGENTS.md`.
Read exact-source test registration/workflows, relevant `docs/os/testing.md`
upgrade/livepatch/prebuild contracts and `docs/os/livepatches/6.12.95.md`.

Read authorized handoff root `../2026-10-20-kernel-check/`:
`generic-sysctl-ci-failure.md`, `generic-sysctl-ci-nested-podman.md`, design's
handoff/current-product/AMD boundary sections, `synthesis.md`, focused receipt,
`os-hardlockup-ci-failure-analysis.md`, `os-hardlockup-ci-new-result.json`,
`os-hardlockup-ci-new-jobs.log` and historical native ZIP/extract. These are
read-only; no source record, branch, index, artifact or watcher changes.

Run 39767770407 is owned by the source watcher. Do not query it individually,
poll it, download more of its logs/artifacts or launch an observer. Existing
preserved evidence is usable. If returned by historical listing, exclude it
before retrieval. Current run is separate context outside historical sample.

Using authorized read-only gh API, declare a recent sample rule/window and
collect initially 10–15 relevant completed runs per family, spanning staging
and relevant feature heads. Include selected runs with unexecuted/cancelled/
prebuild outcomes. Do not cherry-pick exact failures. Reuse source historical
seed 39600028637 at b81c; its archive SHA256 is
`85eadc310707dc36ffc4f1c662214172a1abf857fed9aef317d0176a7dab30fa` (950 members).
852826 run 39745935323 prebuild HTTP429 and cancelled runs 39759039117/
39764186292 are coverage exclusions, not negative signature observations.

Metadata first; obtain native artifacts or job log proof for per-test execution.
Store run/attempt/artifact IDs, exact head/branch/date, job IDs/URLs, retrieval
timestamp/size/hash and errors/retention limits. Download shared native archive
once. Coordinate requests before downloading additional archives. Do not fetch
Git or construct worktrees. Request missing Git objects through lead.

Each recurrence.tsv row must identify run/attempt/job/test, exact head, date,
URLs, first error/phase/signature, result category, duration, evidence path and
strength; include predecessor/image/kernel/module identities where available.
Categories: executed-pass, exact-signature-failure, other-failure, unexecuted,
cancelled, prebuild-failure, unavailable-evidence. Distinguish first error from
cleanup and generic failure from exact signature. Report eligible/executed/
available denominators per family and each of five dataset variants. Attempts
are not independent heads; five failures in one run are not five independent
runs. Do not infer harmlessness, flakiness or exclusion from repetition.

Independently assess all three families' intended behavior/invariants, user
importance, whether assertions measure them, setup dependency and noise, runtime
and maintenance cost, unique coverage and keep/revise/remove disposition.
Use source contract and measured history; do not adopt causal owners' verdicts
without reasoning. Reconcile differences with them and report unresolved
disagreements to lead/architect. Suggest concrete priorities and smallest
diagnostics/regression acceptance, not changing tests to make CI green.

No code edits, test/build/VM diagnostics, reruns, operations, merge/deploy/pins
or lifecycle actions. Historical downloads are evidence retrieval, not CI
monitoring. Report any availability/resource barrier promptly rather than
starting unbounded collection. Lead alone owns plan/state/portal/index/commits.
Send results/blockers with report_to_lead using unique message IDs and share
final path/architectural deviations with architect0 via verified same-session
messaging. Retain saved settings. No automatic reviewer assignment.
