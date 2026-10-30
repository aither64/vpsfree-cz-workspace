# Lane 0: retained impermanent guest state

Owner: implementer0. Read [design.md](design.md) in full; it defines scope,
evidence strength, acceptance and diagnostic proposal limits. Write only
`impermanence-findings.md` and `evidence/impermanence/` under this session.

Before action verify `dev-session current`, both environment markers if present,
and the trusted binding to `2026-10-22-ci-failure-analysis` in
`/home/aither/workspace/ai/vpsfree.cz`. Stop/report any mismatch. Read workspace
AGENTS.md and full sessions, lifecycle, documentation, projects, git,
verification and commits procedures in `docs/agent-instructions/`, plus
`docs/agent-teams.md` and `~/.codex/skills/dev-session-documentation/SKILL.md`.
Read exact vpsadminos AGENTS.md using:
`git --git-dir=repos/vpsadminos.git show 846bb469505789ba0b2a405fa5905ba6d8253006:AGENTS.md`.
Read relevant exact-source docs: `docs/os/testing.md` upgrade contract,
`docs/os/updates.md`, `docs/containers/nixos.md`, `docs/containers/datasets.md`.

Start from read-only source handoff `../2026-10-20-kernel-check/`:
`generic-sysctl-ci-failure.md`, design's current-product causal section,
`os-hardlockup-ci-failure-analysis.md`, historical ZIP/extract and current
native artifacts named in our plan. No mutation of that source session.

Trace all five failures: from-6.12-guests, from-6.12-guests-v1,
from-6.12-inherited-guests, from-6.18-guests and from-6.18-guests-v1.
Establish predecessor/target daemon state boundaries and intended ephemeral
root contract. Inspect `tests/suite/upgrade/common.nix`, case pins,
`osctld/lib/osctld/container{,/run_configuration,/impermanence}.rb`, pool import,
daemon recovery and direct callers. Trace clone selection, metadata writes,
stop/restart loader order, fallback and API export; use exact old and new
revisions, including historical b81c. Determine whether a definite source defect
can explain every observed step or whether competing mechanisms remain.

When reconciling passing history, account for target-side `adopt_run_conf` /
`adopt_live_root` and their unsafe-adoption revert at
`2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`. A passing target may repair or mask
stale predecessor metadata rather than demonstrate correct persistence. Do not
restore first-prefix-match mount adoption as a proposed fix; establish a safe
writer/reader contract and exact source/history boundaries instead.

Do not infer that the actual root changed, data was lost, or the mismatch is
harmless solely from API output. Preserve PID/birth/boot identity and distinguish
container uptime from daemon state. Generic service reachability after the
switch is real; missing logs and earlier recurrence do not exclude contribution.

Request historical artifact needs from implementer3; do not independently
download historical runs. Share exact case/signature criteria and important
source-history boundaries early. Consume immutable paths supplied by that owner.
No polling or new remote retrieval for source run 39767770407.

Deliver source causal chain with revision/path/line citations, log first-error
ordering, remaining unknowns and candidate classifications (product bug,
assertion mismatch, setup defect, evidence gap). Explain test purpose and
member impact, current coverage, measured cost/noise, whether five variants
cover distinct compatibility boundaries, and keep/revise/remove rationale.
Refine design's one-case diagnostic into exact source-validated paths/commands
and hypothesis-discriminating outputs; propose regression coverage for old/new
state readers, repeat activation, daemon restart, marker integrity and cleanup.
Do not execute the diagnostic or implement changes.

No Git mutation, source edits, tests/builds/VMs, reruns, operations, integration,
deployment or lifecycle actions. Lead owns shared records/index/commits. Report
blockers and final findings via report_to_lead with unique message IDs; send
architect0 consequential deviations and the finding path via verified peer
messaging. Preserve retained model/effort/access. Findings only need evidence
checks, not automatic independent review.
