#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
runtime=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
cd "$runtime"
source "$tracking/runtime-dev-env.sh"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
test "$(git rev-parse HEAD)" = 0b403305e085aa01884cf56acea7c717f78f7e86
test -z "$(git status --porcelain)"
test ! -e "$tracking/provider-recovery-final.status"
test ! -e "$tracking/provider-recovery-final.log"
started_at=$(date --iso-8601=seconds)
finish() {
  result=$?
  trap - EXIT
  printf 'revision=0b403305e085aa01884cf56acea7c717f78f7e86\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$started_at" "$(date --iso-8601=seconds)" "$result" > "$tracking/provider-recovery-final.status"
  exit "$result"
}
trap finish EXIT
nix build --no-link --no-write-lock-file --print-build-logs .#checks.x86_64-linux.session-recovery-boot > "$tracking/provider-recovery-final.log" 2>&1
