#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$tracking/creation-provider-recovery.status"' EXIT
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/dev-workspace
nix develop --command ruby "$tracking/creation-provider-recover-retained.rb"
