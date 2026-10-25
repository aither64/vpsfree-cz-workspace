You are a fresh, single-operation verification watcher. Follow
/home/aither/.codex/skills/dev-session-monitor/SKILL.md watcher instructions.
No nested agent, source edit, diagnosis, retry, approval, deployment or cleanup.

Binding: session 2026-10-22-haveapi-release in /home/aither/workspace/ai/vpsfree.cz.
The authorized new worktree is
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-dependency-refresh,
branch 2026-10-22-haveapi-release-dependency-refresh, exact HEAD
090a188cb4ef3477324718627f4ae3415d1c0975. Parent authorizes only the assigned
frozen dependency setup; source is deliberately dirty with the accepted manifest.
Do not borrow old node_modules or alter any other worktree.

Read the skill and local AGENTS.md + doc/agent-instructions/development.md, verify
dev-session current and complete DEV_SESSION_SLUG/DEV_SESSION_WORKSPACE identity.
Then execute exactly once from /home/aither/workspace/ai/vpsfree.cz:

python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/dependency-refresh-npm-setup/setup.py

This parent-authored script checks exact HEAD/branch and package/lock SHA-256,
then enters the declared client-js shell, records node/npm and runs npm ci with
scripts/audit/fund disabled and an own-worktree cache. No build or test occurs.
Own execution and its tool handle; wait until it exits and return raw result.
Do not retry if it fails or modify the command/script/lock/source. No generic
quiet timeout; escalate actual failures, wrong identity, unexpected source writes
or kernel build. Cancellation is not authorized absent a concrete hazard.

Logs/result: this same dependency-refresh-npm-setup directory, install.log,
result.json and exit. Preserve them. Return result, tested revision, elapsed
time, bounded failure excerpt and any still-active handle. Do not diagnose.
