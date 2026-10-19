#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
trap 'verification_status=$?; printf "%s\n" "$verification_status" > "$tracking/operations-tab-verification.status.tmp"; mv "$tracking/operations-tab-verification.status.tmp" "$tracking/operations-tab-verification.status"' EXIT
cd "$group/workspace"
bash "$tracking/operations-tab-candidate-build.sh" > "$tracking/operations-tab-candidate-build.log" 2>&1
nix build --no-link .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions > "$tracking/operations-tab-workspace-checks.log" 2>&1
cd "$group/vpsfree-cz-configuration"
nix develop --command bash "$tracking/operations-tab-system-build.sh" > "$tracking/operations-tab-system-build.log" 2>&1
gh run watch 38464731968 --repo aither64/dev-workspace --exit-status > "$tracking/operations-tab-ci-watch.log" 2>&1
gh run view 38464731968 --repo aither64/dev-workspace --json databaseId,headSha,status,conclusion,url,jobs > "$tracking/operations-tab-ci-final.json"
