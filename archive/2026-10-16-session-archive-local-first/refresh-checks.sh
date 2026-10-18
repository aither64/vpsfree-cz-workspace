#!/usr/bin/env bash
set -euo pipefail
archive_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-session-archive-local-first
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/workspace
test "$(git rev-parse HEAD)" = 2145891816cf88d2a648ace32018e975e810afda
test -z "$(git status --porcelain)"
printf '%s\n' workspace-checks > "$archive_record/refresh.phase"
nix flake check --print-build-logs > "$archive_record/refreshed-workspace-checks.log" 2>&1
printf '%s\n' application-build > "$archive_record/refresh.phase"
nix build --json --out-link "$archive_record/refreshed-application-result" .#default > "$archive_record/refreshed-application-build.json" 2> "$archive_record/refreshed-application-build.log"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/vpsfree-cz-configuration
test "$(git rev-parse HEAD)" = cf0c0d5b1d980c668b8d5bd588f644ef1b53afcb
test -z "$(git status --porcelain)"
printf '%s\n' system-build > "$archive_record/refresh.phase"
nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev > "$archive_record/refreshed-system-build.log" 2>&1
