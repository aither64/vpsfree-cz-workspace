# Observe published v2 CI only

You are a fresh verification watcher, GPT-6 Luna/low, not a team member.
Read `/home/aither/.codex/skills/dev-session-monitor/SKILL.md` and follow only
its watcher instructions. Matching managed catalog digest is
`437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd`;
utility behavior `verification_watcher`, lifetime `operation`. Its native
configuration is under `/nix/store/m12vcm73v1ld944ay9j284r5ikyi9x2n-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`.

Canonical record directory:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports`.
Use `login:false`; `gh` is `/home/aither/.nix-profile/bin/gh`.

Observe existing GitHub Actions in `vpsfreecz/vpsadminos` only:

- Image run `38562488356`.
- RSpec run `38562488281`.
- Core CI run `38562487990`.
- Verify all have exact SHA `4a40154539bf6dc73d391c30326af255b4dc15b2`.

Do not launch any new run, retry, Nix operation or local VM. No cancellation is
authorized. Old v1 core run `38549964340` cancellation was already requested
by the parent; it is not one of your observed runs.

Keep concise durable status in `v2-ci-observer-status.json` and complete failure
logs/artifacts in `v2-ci-failure-artifacts/`. Use blocking waits where possible,
otherwise bounded status reads with reasonable intervals. Return any failure
promptly with exact assertion/raw evidence, while retaining observation of
still-running specified runs until instructed otherwise. Download failed logs
and the relevant existing artifacts without rerunning jobs. Do not diagnose,
edit source/records, approve, publish, deploy or spawn agents. Status/artifact
files requested here are permitted.

The parent awaits a scope decision on a separate impermanence defect. These
runs were triggered automatically by branch publication, not a new local
runtime retry. No generic timeout exists; silence is not a failure or reason
to cancel. Return passed/failed/incomplete, exact run/SHA, elapsed time,
log/artifact paths, bounded failing excerpt and all still-running ownership.
