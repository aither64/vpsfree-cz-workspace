#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
test ! -e "$tracking/kb-runtime-k-canonical.log"
test ! -e "$tracking/kb-runtime-k-canonical.exit"
set -o noclobber
exec > >(tee "$tracking/kb-runtime-k-canonical.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/kb-runtime-k-canonical.exit"' EXIT
cd "$tracking"
test "$(dev-session current)" = 2026-10-05-network-ipv4-left-counter
test -z "${DEV_SESSION_SLUG-}" || test "$DEV_SESSION_SLUG" = 2026-10-05-network-ipv4-left-counter
test -z "${DEV_SESSION_WORKSPACE-}" || test "$DEV_SESSION_WORKSPACE" = /home/aither/workspace/ai/vpsfree.cz
test "${DEV_SESSION_SLUG+x}" = "${DEV_SESSION_WORKSPACE+x}"
cd "$repo"
verify() {
  test "$(git rev-parse HEAD)" = 93a16d6cecb6bc847ec9335a3f170eb8b301ab56
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter-kb-runtime
  test -z "$(git status --porcelain=v1 --untracked-files=all)"
}
verify
nix develop --command bin/check
verify
