#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
trap 'verification_status=$?; printf "%s\n" "$verification_status" > "$tracking/integration-rebase-verification.status"' EXIT
cd "$group/vpsfree-cz-configuration"
nix develop /home/aither/.local/state/dev-workspaces/verification/coordination-configuration-environment --command bash "$tracking/configuration-rebase-build.sh" > "$tracking/configuration-rebase-build.log" 2>&1
cd "$group/workspace"
nix build --no-link .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions > "$tracking/integration-rebase-workspace-checks.log" 2>&1
