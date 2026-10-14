#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-packages1
# Preparation only until root records accepted final review at these exact heads.
python3 - "$tracking/kb-runtime-review-gate.json" <<'PY'
import json,sys
x=json.load(open(sys.argv[1]))
assert x['accepted'] is True
assert x['heads']=={'k':'93a16d6cecb6bc847ec9335a3f170eb8b301ab56','d':'51aba080b264c28f5584867b6cf006bf423ae2f3','e':'d2079f605ae87871037ae73c5e5daf20a3e0d03d'}
PY
for suffix in log exit k-paths.txt k.log k.exit d.log d.exit e.log e.exit; do test ! -e "$tracking/$prefix.$suffix"; done
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
check_tree() {
  test "$(git -C "$worktrees/$1" rev-parse HEAD)" = "$2"
  test -z "$(git -C "$worktrees/$1" status --porcelain=v1 --untracked-files=all)"
}
check_tree vpsfree-kb-contracts-runtime 93a16d6cecb6bc847ec9335a3f170eb8b301ab56
check_tree dev-workspace 51aba080b264c28f5584867b6cf006bf423ae2f3
check_tree vpsfree-dev-workspace d2079f605ae87871037ae73c5e5daf20a3e0d03d
run_step() {
 local step=$1
 shift
 set +e
 "$@" > >(tee "$tracking/$prefix.$step.log") 2>&1
 local result=$?
 set -e
 printf '%s\n' "$result" >"$tracking/$prefix.$step.exit"
 return "$result"
}
cd "$worktrees/vpsfree-kb-contracts-runtime"
run_step k nix build --no-link --no-update-lock-file --print-out-paths \
 github:vpsfreecz/vpsfree-kb-contracts/93a16d6cecb6bc847ec9335a3f170eb8b301ab56#kb-runtime \
 github:vpsfreecz/vpsfree-kb-contracts/93a16d6cecb6bc847ec9335a3f170eb8b301ab56#capture \
 github:vpsfreecz/vpsfree-kb-contracts/93a16d6cecb6bc847ec9335a3f170eb8b301ab56#standalone-test-config
cd "$worktrees/dev-workspace"
run_step d nix flake check --print-build-logs --no-update-lock-file
cd "$worktrees/vpsfree-dev-workspace"
run_step e nix flake check --print-build-logs --no-update-lock-file
check_tree vpsfree-kb-contracts-runtime 93a16d6cecb6bc847ec9335a3f170eb8b301ab56
check_tree dev-workspace 51aba080b264c28f5584867b6cf006bf423ae2f3
check_tree vpsfree-dev-workspace d2079f605ae87871037ae73c5e5daf20a3e0d03d
