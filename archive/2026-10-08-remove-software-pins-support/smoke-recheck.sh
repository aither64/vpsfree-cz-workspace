#!/usr/bin/env bash
set -u
check_repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-08-remove-software-pins-support/confctl
check_records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-08-remove-software-pins-support
cd "$check_repo" || exit 1
[[ $(git rev-parse HEAD) == 3be154b5f86125146e444d5fb6aa60916e99b77d ]] || exit 2
[[ -z $(git status --porcelain=v1) ]] || exit 3
nix develop -c bash /tmp/confctl-flake-smoke.sh "$check_repo" > "$check_records/flake-smoke2.log" 2>&1
check_status=$?
printf '%s\n' "$check_status" > "$check_records/flake-smoke2.exit"
[[ $check_status == 0 ]] || exit "$check_status"
check_fixture=$(sed -n 's/^Disposable evaluation fixture: //p' "$check_records/flake-smoke2.log" | head -1)
nix develop -c bash "$check_records/example-init-smoke.sh" "$check_repo" "$check_fixture" > "$check_records/example-init-smoke2.log" 2>&1
check_status=$?
printf '%s\n' "$check_status" > "$check_records/example-init-smoke2.exit"
git status --porcelain=v1 > "$check_records/smoke2-status.txt"
[[ ! -s "$check_records/smoke2-status.txt" ]] || exit 4
exit "$check_status"
