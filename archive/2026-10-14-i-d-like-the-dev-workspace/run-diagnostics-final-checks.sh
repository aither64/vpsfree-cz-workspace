#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
runtime=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
cd "$runtime"
source "$tracking/runtime-dev-env.sh"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
test "$(git rev-parse HEAD)" = 0b403305e085aa01884cf56acea7c717f78f7e86
test -z "$(git status --porcelain)"
test ! -e "$tracking/runtime-diagnostics-flake.log"
test ! -e "$tracking/runtime-diagnostics-flake.status"
started_at=$(date --iso-8601=seconds)
finish() {
  result=$?
  trap - EXIT
  printf 'revision=0b403305e085aa01884cf56acea7c717f78f7e86\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$started_at" "$(date --iso-8601=seconds)" "$result" > "$tracking/runtime-diagnostics-flake.status"
  exit "$result"
}
trap finish EXIT
nix flake check --print-build-logs > "$tracking/runtime-diagnostics-flake.log" 2>&1
