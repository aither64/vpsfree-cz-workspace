#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-packages2
# Preparation only: an accepted exact-head affected-review receipt is mandatory.
python3 - "$tracking/kb-runtime-remediation-review-gate.json" <<'PY'
import json,sys
value=json.load(open(sys.argv[1]))
assert value['accepted'] is True
assert value['heads']=={'k':'68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e','d':'51aba080b264c28f5584867b6cf006bf423ae2f3','e':'f6d2c080469b224ac77765aecd76a6d531358363'}
PY
for suffix in log exit k.paths k.log k.exit e.log e.exit before.sha after.sha; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
check_tree() {
  test "$(git -C "$worktrees/$1" rev-parse HEAD)" = "$2"
  test -z "$(git -C "$worktrees/$1" status --porcelain=v1 --untracked-files=all)"
}
check_all() {
  check_tree vpsfree-kb-contracts-runtime 68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e
  check_tree dev-workspace 51aba080b264c28f5584867b6cf006bf423ae2f3
  check_tree vpsfree-dev-workspace f6d2c080469b224ac77765aecd76a6d531358363
}
check_all
sha256sum "$worktrees/vpsfree-kb-contracts-runtime/flake.nix" "$worktrees/vpsfree-kb-contracts-runtime/flake.lock" \
  "$worktrees/vpsfree-dev-workspace/flake.nix" "$worktrees/vpsfree-dev-workspace/flake.lock" >"$tracking/$prefix.before.sha"
set +e
(cd "$worktrees/vpsfree-kb-contracts-runtime"; nix build --no-link --no-update-lock-file --print-out-paths \
  github:vpsfreecz/vpsfree-kb-contracts/68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e#kb-runtime \
  github:vpsfreecz/vpsfree-kb-contracts/68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e#capture \
  github:vpsfreecz/vpsfree-kb-contracts/68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e#standalone-test-config) \
  >"$tracking/$prefix.k.paths" 2>"$tracking/$prefix.k.log"
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix.k.exit"
cat "$tracking/$prefix.k.log"
test "$result" = 0
cat "$tracking/$prefix.k.paths"
check_all
# Exact D51 fast CI already passed; do not select its unrelated host VM check.
# E's host-migration-test is a separate package, not a regular flake check.
set +e
(cd "$worktrees/vpsfree-dev-workspace"; nix flake check --print-build-logs --no-update-lock-file) \
  >"$tracking/$prefix.e.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/$prefix.e.exit"
cat "$tracking/$prefix.e.log"
test "$result" = 0
check_all
sha256sum "$worktrees/vpsfree-kb-contracts-runtime/flake.nix" "$worktrees/vpsfree-kb-contracts-runtime/flake.lock" \
  "$worktrees/vpsfree-dev-workspace/flake.nix" "$worktrees/vpsfree-dev-workspace/flake.lock" >"$tracking/$prefix.after.sha"
cmp "$tracking/$prefix.before.sha" "$tracking/$prefix.after.sha"
