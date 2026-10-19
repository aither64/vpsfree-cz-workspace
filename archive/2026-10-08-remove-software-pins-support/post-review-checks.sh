#!/usr/bin/env bash
set -u
check_repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-08-remove-software-pins-support/confctl
check_records=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-08-remove-software-pins-support
check_head=${1:?expected committed HEAD}
cd "$check_repo" || exit 1
[[ $(git rev-parse HEAD) == "$check_head" ]] || exit 2
[[ -z $(git status --porcelain=v1) ]] || exit 3
printf '%s\n' "$check_head" > "$check_records/post-review-source.txt"
check_failed=0
nix build --no-link --json .#confctl .#checks.x86_64-linux.rspec > "$check_records/package-build.json" 2> "$check_records/package-build.log"
check_status=$?
printf '%s\n' "$check_status" > "$check_records/package-build.exit"
if [[ $check_status != 0 ]]; then check_failed=1; fi
nix develop -c bash /tmp/confctl-flake-smoke.sh "$check_repo" > "$check_records/flake-smoke.log" 2>&1
check_status=$?
printf '%s\n' "$check_status" > "$check_records/flake-smoke.exit"
if [[ $check_status != 0 ]]; then check_failed=1; fi
if [[ $(cat "$check_records/flake-smoke.exit") == 0 ]]; then
  check_fixture=$(sed -n 's/^Disposable evaluation fixture: //p' "$check_records/flake-smoke.log" | head -1)
  nix develop -c bash "$check_records/example-init-smoke.sh" "$check_repo" "$check_fixture" > "$check_records/example-init-smoke.log" 2>&1
  check_status=$?
  printf '%s\n' "$check_status" > "$check_records/example-init-smoke.exit"
  if [[ $check_status != 0 ]]; then check_failed=1; fi
fi
if [[ $(cat "$check_records/package-build.exit") == 0 ]]; then
  check_package=$(nix eval --raw .#packages.x86_64-linux.confctl.outPath)
  printf '%s\n' "$check_package" > "$check_records/package-path.txt"
  "$check_package/bin/confctl" --help > "$check_records/package-help.txt" 2> "$check_records/package-help.log"
  check_status=$?
  if [[ $check_status == 0 ]] && rg -q 'swpins|migrate|outdated-swpins' "$check_records/package-help.txt"; then check_status=1; fi
  printf '%s\n' "$check_status" > "$check_records/package-help.exit"
  if [[ $check_status != 0 ]]; then check_failed=1; fi
fi
git status --porcelain=v1 > "$check_records/post-review-status.txt"
[[ ! -s "$check_records/post-review-status.txt" ]] || check_failed=1
[[ $(git rev-parse HEAD) == "$check_head" ]] || check_failed=1
exit "$check_failed"
