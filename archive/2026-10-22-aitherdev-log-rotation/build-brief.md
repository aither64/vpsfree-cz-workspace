# Build watcher brief

One operation: build the committed aitherdev configuration. Read the monitor
skill at /home/aither/.codex/skills/dev-session-monitor/SKILL.md and act only
as its verification watcher. No diagnosis, source edits, retries, deployments,
acceptance decisions or nested agents.

Worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-aitherdev-log-rotation/vpsfree-cz-configuration
Expected head: 52b8ccd33fdf60d231816cfb6f166e34671122f0.
Command: nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
The --yes flag answers only this already-authorized build confirmation; it does
not activate or deploy a system.
Set DEV_SESSION_SLUG=2026-10-22-aitherdev-log-rotation and
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz.
Keep full stdout/stderr in this directory's build.log and preserve the actual
command exit status. Write build-result.json containing the exact head, command,
exit status, elapsed time, and any cancellation or still-running operation.
The watcher owns process execution and observation; do not assume a parent handle.
The parent will interpret results and resume automatically.

No quiet-output timeout. If the command starts an unexpected local Linux kernel
build, stop only this owned command/process tree and notify the parent with the
exact derivation and log evidence. This task changes no kernel and supplies no
kernel-build exception. Do not cancel unrelated builds or services. Escalate
interactive prompts or other conditions requiring a parent decision without
retrying or answering unrelated authorization questions.

Caller policy: workspace AGENTS.md and dev-session-monitor require a fresh
verification utility for uncertain builds. This tracking-only initiative has no
native lead thread or retained catalog, so use explicit site policy and the
currently installed catalog. Its utilities.verification_watcher is gpt-6-luna,
low effort, workspace_write; package-wide execution_access is full_access.
Catalog: /nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json
Digest: 840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa.
Matching native utility:
/nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml
Identity: dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12.
Read it and verify the launch/access settings in the report. Native tools inherit
full filesystem/network access with approvals never; do not set sandbox_permissions.
This utility is not a roster member. Read repository AGENTS.md plus workspace
verification procedure before running the exact command. Applicable monitoring
instructions are supplied above; do not expand into development or session setup.

Return passed/failed/incomplete, exact head and command, elapsed time, exit code,
log/result paths, bounded failure or escalation excerpt, and any still-running
process or authorized cancellation. Retain ownership until the command is accounted
for, and do not relaunch an existing run.
