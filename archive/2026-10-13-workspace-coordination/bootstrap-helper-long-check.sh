#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination
trap 'check_status=$?; printf "%s\n" "$check_status" > "$tracking/bootstrap-helper-long-check.status.tmp"; mv "$tracking/bootstrap-helper-long-check.status.tmp" "$tracking/bootstrap-helper-long-check.status"' EXIT
cd "$group/dev-workspace"
DEV_WORKSPACE_TEST_SOURCE="$group/dev-workspace" \
DEV_WORKSPACE_INSTALLED_PACKAGE=/nix/store/m12vcm73v1ld944ay9j284r5ikyi9x2n-dev-workspace-0.2.0 \
BOOTSTRAP_MERGE_SYSTEMD_TEST=1 \
nix develop --command ruby "$group/workspace/test/bootstrap_merge_2026_10_13_test.rb" -n test_dated_systemd_driver_exit_preserves_and_resumes_the_original_job > "$tracking/bootstrap-helper-systemd.log" 2>&1
cd "$group/workspace"
nix build --no-link .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions > "$tracking/bootstrap-helper-workspace-checks.log" 2>&1
