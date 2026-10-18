#!/usr/bin/env bash
set -euo pipefail
archive_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-session-archive-local-first
archive_runtime=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/dev-workspace
archive_workspace=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/workspace
cd "$archive_runtime"
export TMPDIR=/tmp
export ARCHIVE_TEST_HEAD
ARCHIVE_TEST_HEAD=$(git rev-parse HEAD)
export ARCHIVE_SCALE_RESULT="$archive_record/archive-scale.json"
printf '%s\n' scale-archive > "$archive_record/acceptance.phase"
nix develop --command ruby "$archive_record/archive-scale.rb" -n test_archive_scale_local_closure > "$archive_record/archive-scale.log" 2>&1
printf '%s\n' live-worker > "$archive_record/acceptance.phase"
DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/dev-workspace-archive-no-provider-catalog nix develop --command go -C portal test -mod=readonly -overlay "$archive_record/live-worker-overlay.json" ./internal/web -run TestArchiveWorkerLiveUserManagerRestartAcceptance -count=1 -v > "$archive_record/archive-worker-live.log" 2>&1
cd "$archive_workspace"
printf '%s\n' workspace-flake-check > "$archive_record/acceptance.phase"
nix flake check --print-build-logs > "$archive_record/workspace-flake-check.log" 2>&1
printf '%s\n' application-package > "$archive_record/acceptance.phase"
nix build --out-link "$archive_record/application-result" --json .#default > "$archive_record/application-build.json" 2> "$archive_record/application-build.log"

cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/vpsfree-cz-configuration
printf '%s\n' system-build > "$archive_record/acceptance.phase"
nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev > "$archive_record/system-build.log" 2>&1
