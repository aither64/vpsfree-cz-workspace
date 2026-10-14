# Sensitive sessions implementation

Implemented and published on `2026-10-14-sensitive-sessions`:

| Repository | Final head |
| --- | --- |
| dev-workspace | `54bb1172705cb41e1958a3e43323f4cc6213f0d6` |
| vpsfree-dev-workspace | `3f0777ffb020b5d02c21c65ee7bcd46804768ff1` |
| workspace | `46cc28c2e32ae249612fb39e595690f7e56e9154` |

Creation-time `--sensitive` and the portal checkbox keep records in the usual
work/archive locations with private metadata and local Git exclusions. Forks
and plan-derived sessions inherit sensitivity. Lifecycle recovery, package
compatibility, coordinator ownership and project Git workflows remain enforced.
Existing sessions cannot be converted. Portal badges identify sensitive sessions.

Independent review covered all four lanes and complete consolidated histories.
One blocking exclusion-probe gap was fixed and verified directly. A subsequent
packaged-layout test fixture omission was corrected; it changed no runtime
behavior. No migrations, dependency updates or deployed formats were introduced.

Exact runtime and extension CI passed. Runtime was cleanly rebased with unchanged
patch; focused archive/sensitivity checks passed again. All four Ruby suites pass; focused
Go/browser, skill-validation and workspace-instruction checks pass. Full local
Nix flake check passed, including package variants and the recovery VM. That
run used the pre-rebase source; exact rebased runtime CI and focused archive
checks verify the current baseline.
The direct-Go host catalog/test-isolation issue reproduces on the unchanged
base and does not affect sandboxed package checks.

Feature explanations are in the runtime's docs/dev-sessions.md (Sensitive
sessions), docs/session-archive-recovery.md and docs/workspace-portal.md.
Site procedures and the handoff skill preserve local-only tracking policy.
Detailed findings, remediation, heads and commands are linked from state.md.

No default-branch integration, dependency-pin selection, machine reservation,
deployment or live UI/activation review occurred. Any later integration or
rollout requires its applicable user authorization and coordinator workflow.
This tracking-only session lacks a retained Codex root for unattended submission;
resolve its actual thread binding before a later authorized operation. Do not
borrow another session or bootstrap owner. Retain branches and the active
session. Ready, awaiting merge approval.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-sensitive-sessions/
