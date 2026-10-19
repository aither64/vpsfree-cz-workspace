#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
workspace=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/workspace
mkdir -p "$workspace/lib"
cp "$tracking/bootstrap-merge-2026-10-13" "$workspace/bin/bootstrap-merge-2026-10-13"
cp "$tracking/bootstrap_merge_2026_10_13.rb" "$workspace/lib/bootstrap_merge_2026_10_13.rb"
cp "$tracking/bootstrap_merge_2026_10_13_test.rb" "$workspace/test/bootstrap_merge_2026_10_13_test.rb"
cp "$tracking/bootstrap-merge-2026-10-13-procedure.md" "$workspace/docs/maintenance/bootstrap-merge-2026-10-13.md"
chmod 0755 "$workspace/bin/bootstrap-merge-2026-10-13"
