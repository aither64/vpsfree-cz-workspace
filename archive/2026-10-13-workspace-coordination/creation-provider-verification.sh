#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
trap 'verification_status=$?; printf "%s\n" "$verification_status" > "$tracking/creation-provider-verification.status.tmp"; mv "$tracking/creation-provider-verification.status.tmp" "$tracking/creation-provider-verification.status"' EXIT
cd "$group/workspace"
bash "$tracking/creation-provider-candidate-build.sh" > "$tracking/creation-provider-candidate-build.log" 2>&1
nix build --no-link .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions > "$tracking/creation-provider-workspace-checks.log" 2>&1
cd "$group/dev-workspace"
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-recovery-boot > "$tracking/creation-provider-recovery-vm.log" 2>&1
cd "$group/vpsfree-cz-configuration"
nix develop --command bash "$tracking/creation-provider-system-build.sh" > "$tracking/creation-provider-system-build.log" 2>&1
gh run watch 38470155400 --repo aither64/dev-workspace --exit-status > "$tracking/creation-provider-ci-watch.log" 2>&1
gh run view 38470155400 --repo aither64/dev-workspace --json databaseId,headSha,status,conclusion,url,jobs > "$tracking/creation-provider-ci-final.json"
