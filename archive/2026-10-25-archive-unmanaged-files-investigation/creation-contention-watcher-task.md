# Fresh verification watcher

Use /home/aither/.codex/skills/dev-session-monitor/SKILL.md. You are the watcher;
do not delegate. Read /home/aither/workspace/ai/vpsfree.cz/AGENTS.md and its
absolute docs/agent-instructions/verification.md before acting. Do not edit source,
tracking or docs, diagnose, retry jobs, deploy, approve or create an initiative.

Installed policy digest 840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa:
verification_watcher is gpt-6-luna / low, full_access, native utility
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`. CLI explicitly uses
--sandbox danger-full-access --ask-for-approval never. No writable-root additions.

Working directory:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace
Tested exact head b974f2f3f83792a494610d1ea03f3d69e97bc1a4, clean and published.
Independent review is complete with no findings. This operation observes only
CI run 40223710351, repo aither64/dev-workspace, already started by that push.
The fast job builds packaged/component checks; creation and archive jobs run the
shipped native VM workflows. Do not relaunch any operation.

Run exactly:
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-archive-unmanaged-files-investigation/watch-contention-ci.py

You own this invocation/tool handle. The fixed script preserves gh watch status,
queries the exact run and downloads completed failure logs without rerunning jobs.
Evidence stays beside this brief under creation-contention-ci-* filenames.
No generic timeout; do not cancel CI. Wait through queued/resource contention.
Use blocking waits under 60 seconds and bounded output. If an unexpected local
kernel build appears, report it; this observation command should not build locally.

On completion, return pass/fail/incomplete, exact revision/run ID, elapsed time,
job conclusions, evidence paths and a bounded failure excerpt without diagnosis.
If API/watch fails while CI is still running, report that uncertainty and exact
run identity. Do not treat timeout or observation failure as a test failure.
Return a final compact report; the CLI saves it as creation-contention-watcher.md.
