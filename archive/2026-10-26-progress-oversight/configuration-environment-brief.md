# Verification utility: configuration environment

Follow /home/aither/.codex/skills/dev-session-monitor/SKILL.md. You are the fresh
site-policy Luna/low utility; no nested delegation, source edits, diagnosis,
retries, commits or deployment. Execution is danger-full-access/never under the
installed policy. No credentials in output. Workspace/session identity is
2026-10-26-progress-oversight at /home/aither/workspace/ai/vpsfree.cz.

Read workspace AGENTS.md plus docs/agent-instructions/{verification,commits}.md
and the configuration worktree AGENTS.md before action. This bounded operation
prepares the owned configuration Nix environment and ordinary Overcommit trust;
source is clean270d348a. Worktree creation previously completed but post-checkout
failed due missing gems; do not recreate the checkout or bypass hooks.

Working directory:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-progress-oversight/vpsfree-cz-configuration

Run exactly once:
nix develop --command bash -c 'set -e; bundle exec overcommit --sign; configuration_hook=$(git rev-parse --git-path hooks/post-checkout); configuration_head=$(git rev-parse HEAD); "$configuration_hook" "$configuration_head" "$configuration_head" 1'

Capture complete output and exit status in
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-progress-oversight/configuration-environment.log.
Report the actual result/elapsed/remaining handles. No blind retry; return any
failure to parent. Stop only this operation if an unexpected local kernel build
starts and report it. No arbitrary quiet timeout.
