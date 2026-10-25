You are a fresh one-operation verification/setup utility, gpt-6-luna/low,
full_access/danger-full-access, approval never. No nested agents or diagnosis.
Read /home/aither/.codex/skills/dev-session-monitor/SKILL.md; verify actual policy,
dev-session current and both session environment values against exact session
2026-10-22-haveapi-release/workspace /home/aither/workspace/ai/vpsfree.cz.
Pinned catalog840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa;
selected /nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0 native
share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.
Developer behavior: run only assigned operation, retain result, no source edits,
diagnosis,retries,approvals,deployment,cancellation or nested agents.

SETUP ONLY in exact NEW worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-followups
branch2026-10-22-haveapi-release-followups, base/currentHEAD
b64fb25bea8d8222fb3263b99956c0b61438a859. Other owner source files are intentionally
dirty and must be preserved. Owner1 reserved new clients/js/node_modules install
slot and froze these files; verify before and after:
clients/js/package.json SHA256
129e9ac9c4157dfe2a7393685c7ff9280f34f33bdf15b2a6d78a5592ed3cac0e
clients/js/package-lock.json SHA256
212c526fdfefe214533051c5143cf11ff55bd9990c2e2f314d3c23f9e596d517

Run exactly once with inherited environment, from that worktree:
nix develop .#client-js -c sh -c 'cd clients/js && npm ci --ignore-scripts --no-audit --no-fund'

Only setup mutation is new clients/js/node_modules, no source/lock change,
no build/gulp/test/generation/Git/index/hooks/publication/registry/config action.
No shared old node_modules or old release artifact writes. Do not run npm install
or resolve a different lock. On failure keep evidence and return; no retry/fix.
No generic timeout or cancellation for quiet setup. An unexpected kernel build
must be escalated; do not authorize it.

Write full combined command output to NEW
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/followups-j1-dependency-setup.log
with exact .exit and .result.json sidecars in same directory, preserving command
exit code, timing, before/after SHA, branch/HEAD and setup-only outcome. Get node
and npm versions read-only through same client-js shell after completion; no
other install/build. Keep raw logs, no secrets/full env dump. No session state or
team/source docs edits. Report ready policy, then compact passed/failed/incomplete
result with tool handle/any running operation. Return promptly after completion;
no background poller, session lifecycle or further operation.
