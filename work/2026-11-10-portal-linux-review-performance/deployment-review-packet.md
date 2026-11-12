# Deployment composition and final branch history review

User direction (2026-11-12): "you can deploy aitherdev using
vpsfree-cz-configuration. merge after verification". Prepare and deploy the
reviewed portal performance change, verify live behavior, then integrate the
application and matching configuration/workspace pins into remote master.

Coordination root: /home/aither/workspace/ai/vpsfree.cz.
Initiative: 2026-11-10-portal-linux-review-performance. Read plan.md, design.md,
state.md and final-review.md here. Application review and its narrow-fix
reconciliation are already complete. Inspect the new deployment composition
and complete branch histories; do not redo unchanged application review.

All worktrees are beneath worktrees/2026-11-10-portal-linux-review-performance/:

| Repository | Base | Final head | Complete series |
| --- | --- | --- | --- |
| dev-workspace | 6587c4c1cedabee95bcc52f4667e7d33e3a82859 | 02881b401955ff0db71bb74f6fb84f6e475a7879 | one portal feature commit, already reviewed |
| workspace | 05ad6ab3e430ac69ec20d94a481843a7e1f57124 | 42c76e8cb61e0d2063a3d25b4b448e66abee523f | one exact nested runtime pin |
| vpsfree-cz-configuration | dda57166bd8bb6d85a74decdd05a8810933bdecc | 5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c | one generated confctl channel pin |

Read each repository's AGENTS.md. Compare the complete base-to-head series and
diffs. No migrations, dependency churn, superseded pin commits or deployed
intermediate feature versions. Workspace and configuration pins are mechanical;
they select the same independently reviewed runtime. Workspace retains the
direct nested override, extension 0c7168f3, follows and sibling inputs.
Configuration uses the existing dev-workspace/devWorkspace channel and preserves
confctl's generated commit message. No PR required.

Quick verification: all three diff checks pass. Configuration's Nixfmt and
commit hooks passed (generated message width warning only). The workspace
deployment checker passes against final locks at 02881b40. Source runtime
flake.lock, nix and libexec are unchanged against 6587c4c1. Active and selected
Codex resolve to /nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/bin/codex.
Prior application tests, package build and GitHub run 42805944135 passed.
No need to repeat unchanged application tests; composed package and host build,
dry-activation and live verification follow this review.

Deployment: build/copy before machine ownership; use a schema-2 aitherdev claim
from the registered configuration. Verify exact mapping, confctl dry-activate
and no-reboot switch with auto-rollback preserved. Verify live and system-profile
paths before ordinary guarded workspace-host switch --source on the workspace
feature checkout. Pass exact session identity and held machine claim. No
maintenance/interrupt flag or provider change. Verify portal health, real Linux
metadata/content, naming health and existing native daemon continuity. Integrate
only after verification, one short repository claim at a time. Release machine
after complete deployed lineage reaches all approved remote masters.

Recovery: retain confctl generations, package roots and ordinary journals;
system rollback remains confctl-owned, profile recovery is forward-only. Do not
work around refusals or uncertain effects. No session archival or deletion.

Documentation inventory: portal users/reference -> dev-workspace README and
docs/workspace-portal.md (already reviewed and unchanged); deployment operators/
operations -> configuration docs/operations/codex-providers-aitherdev.md and
workspace docs/agent-instructions/deployment.md plus installed coordination
guide (checked, existing procedure applies); exact execution -> initiative
state.md and forthcoming rollout.md. Routine pins need no project doc change.

Risk: high operational deployment, with unchanged state and native contracts.
Use general, architecture, scope and risk lanes. Former reviewer native identity
is no longer live (list_agents has only root), so installed default fallback is
fresh gpt-6.1-sol/xhigh. Do not delegate. Write deployment-review.md here with
findings, explicit complete-history/migration and repeated-stream conclusions.

Workspace rebased during review from 290a659de onto 05ad6ab3 (observability
guidance only). Final head 42c76e8cb61e0d2063a3d25b4b448e66abee523f.
Range-diff reports the single pin commit equal; diff check passed. Read the
updated AGENTS.md and observability procedure; they do not change this rollout.
