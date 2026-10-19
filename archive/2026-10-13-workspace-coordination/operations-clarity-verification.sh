#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
trap 'verification_status=$?; printf "%s\n" "$verification_status" > "$tracking/operations-clarity-verification.status.tmp"; mv "$tracking/operations-clarity-verification.status.tmp" "$tracking/operations-clarity-verification.status"' EXIT
cd "$group/workspace"
bash "$tracking/operations-clarity-candidate-build.sh" > "$tracking/operations-clarity-candidate-build.log" 2>&1
nix build --no-link .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions > "$tracking/operations-clarity-workspace-checks.log" 2>&1
cd "$group/dev-workspace"
nix build --no-link --print-build-logs .#checks.x86_64-linux.host-module-idempotency .#checks.x86_64-linux.session-recovery-boot > "$tracking/operations-clarity-vm-checks.log" 2>&1
cd "$group/vpsfree-cz-configuration"
nix develop --command bash "$tracking/operations-clarity-system-build.sh" > "$tracking/operations-clarity-system-build.log" 2>&1
gh run watch 38457798619 --repo aither64/dev-workspace --exit-status > "$tracking/operations-clarity-ci-watch.log" 2>&1
gh run view 38457798619 --repo aither64/dev-workspace --json databaseId,headSha,status,conclusion,url,jobs > "$tracking/operations-clarity-ci-final.json"
