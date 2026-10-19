#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
trap 'verification_status=$?; printf "%s\n" "$verification_status" > "$tracking/merge-environment-verification.status"' EXIT
cd "$group/workspace"
nix build --out-link "$tracking/merge-environment-candidate-gc-root" --print-out-paths .#default > "$tracking/merge-environment-candidate.path" 2> "$tracking/merge-environment-candidate-build.log"
nix build --no-link .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions > "$tracking/merge-environment-workspace-checks.log" 2>&1
cd "$group/vpsfree-cz-configuration"
nix develop /home/aither/.local/state/dev-workspaces/verification/coordination-configuration-environment --command confctl build --yes cz.vpsfree/machines/aitherdev > "$tracking/merge-environment-system-build.log" 2>&1
