# Lane 1: predecessor nested Podman networking

Owner: implementer1. Read [design.md](design.md) in full. Write only
`podman-findings.md` and `evidence/podman/` under this session.

Verify `dev-session current`, environment and trusted binding to
`2026-10-22-ci-failure-analysis`, `/home/aither/workspace/ai/vpsfree.cz`; stop
and report mismatch. Read workspace AGENTS.md and full procedures sessions,
lifecycle, documentation, projects, git, verification, commits under
`docs/agent-instructions/`, `docs/agent-teams.md`, and documentation skill
`~/.codex/skills/dev-session-documentation/SKILL.md`. Read vpsadminos AGENTS.md
with `git --git-dir=repos/vpsadminos.git show 846bb469505789ba0b2a405fa5905ba6d8253006:AGENTS.md`.
Read exact-source `docs/os/testing.md` upgrade contract, `docs/os/updates.md`,
networking docs matching the actual fixture and nested-workload documentation.

Start with read-only source handoff `../2026-10-20-kernel-check/`:
`generic-sysctl-ci-nested-podman.md`, `generic-sysctl-ci-failure.md` and the
preserved `os-test-upgrade__from-6.18-nested-podman-3db70126` artifacts named
in our plan. No mutation of that source session.

Trace exact predecessor `3cb830e596a7fed900bec49f50c9b6cf51e76bb5`, kernel
6.18.49, Debian 13.7/dhcpcd 10.1.0 package identity, fixture networking/LXC
policy and readiness code. Relevant sources include
`tests/suite/upgrade/{from-6.18-nested-podman,from-6.18,common}.nix`,
`osvm/lib/osvm/vpsadminos_machine.rb`, image scripts, osctld generated LXC and
network configuration, and precise dhcpcd sandbox source if needed. Use
official upstream/package sources for external source facts, pinning versions.

Observed chain: sandbox permission error -> ifup/networking failure -> no
IPv4/default route -> 126 failed DNS-dependent readiness probes -> 900s
timeout before package installation and target activation. Distinguish failure
to install a seccomp filter from a syscall denied by a filter; the log wording
alone does not establish which. Identify effective credentials/filter and
source-compatible causes without guessing the denied syscall or introducer.
Include the exact predecessor AUTH_GUARD EACCES entry paths in the candidate
comparison, distinguishing configured source from actual binary/runtime state.
Require call/arguments/errno and credential/NNP/config evidence before choosing
among guard rejection, ordinary preconditions and an installed filter rule.
The incoming generic service did not execute here; do not transfer that
exclusion to other tests or imply all networking was healthy from host probes.

Explain what nesting Podman inside a system container protects for users and
what this attempt never reached. Assess supported predecessor/new image
compatibility, mutable image provenance, readiness dependencies and timeout
diagnostics. Distinguish layer checks (link/address/route/DNS/external endpoint)
from nested application continuity; do not recommend masking DHCP failure.

Coordinate historical artifact requests with sole collector implementer3;
send exact signature criteria and useful image/version boundaries. No duplicate
downloads or source-current run polling/retrieval. Findings need source/log
citations, evidence strength, uncertainty, utility/cost/noise, justified
keep/revise/remove and prioritized proposals. Refine design's minimal single
predecessor-container trace into exact commands, captured identities and errno
interpretation, with regression acceptance retaining sandbox confinement and
nested workload continuity. Proposal only; do not run it.

No Git mutations, source edits, tests/builds/VMs, reruns, production operations,
merge, deployment, pins or lifecycle actions. Lead alone owns shared records
and commits. Report blockers/results to lead with report_to_lead and unique
message IDs; send architect0 material deviations and the final finding path
through verified peer messaging. Retain member settings. No automatic review.
