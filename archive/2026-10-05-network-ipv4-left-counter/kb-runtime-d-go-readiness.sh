#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
test ! -e "$tracking/kb-runtime-d-go-readiness.log"
test ! -e "$tracking/kb-runtime-d-go-readiness.exit"
set -o noclobber
exec > >(tee "$tracking/kb-runtime-d-go-readiness.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/kb-runtime-d-go-readiness.exit"' EXIT
cd "$tracking"
test "$(dev-session current)" = 2026-10-05-network-ipv4-left-counter
test -z "${DEV_SESSION_SLUG-}" || test "$DEV_SESSION_SLUG" = 2026-10-05-network-ipv4-left-counter
test -z "${DEV_SESSION_WORKSPACE-}" || test "$DEV_SESSION_WORKSPACE" = /home/aither/workspace/ai/vpsfree.cz
test "${DEV_SESSION_SLUG+x}" = "${DEV_SESSION_WORKSPACE+x}"
cd "$repo"
test "$(git rev-parse HEAD)" = 9fe491218e35a3250f2a72c203c2cecc3cb7ae16
nix develop .#dev-workspace --command bash -ec 'command -v gofmt; readlink -f "$(command -v gofmt)"; go version; go env GOROOT'
