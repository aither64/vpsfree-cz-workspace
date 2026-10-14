#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
prefix=kb-runtime-generic-quick1
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = e3315a483f3d3536d492ecbe40f2655449cf630f
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1)
}
run() {
  local name=$1
  shift
  set +e
  (cd "$repo"; "$@") >"$tracking/$prefix-$name.log" 2>&1
  local result=$?
  set -e
  printf '%s\n' "$result" >"$tracking/$prefix-$name.exit"
  cat "$tracking/$prefix-$name.log"
  return "$result"
}
verify
run syntax bash -c 'ruby -c libexec/workspace-host && ruby -c test/workspace_host/commands_and_locks_test.rb'
run commands ruby test/workspace_host_test.rb --name '/capture_lease|cluster_command|waiting_host_mutation|ordinary_dispatch|exec_with_workspace|dev_session_dispatch/'
verify
