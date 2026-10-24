#!/usr/bin/env bash
set -euo pipefail

# Preparation only. The lead owns repository claims and all default mutations.
session=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement

prepare() {
  local project=$1 base=$2 path="$group/integration-$1"
  test "$(git -C "$path" rev-parse HEAD)" = "$base"
  test -z "$(git -C "$path" symbolic-ref -q HEAD || true)"
  test -z "$(git -C "$path" status --porcelain=v1 --untracked-files=all)"
  printf 'Preparing declared shell and ordinary hooks: %s at %s\n' "$project" "$base"
  (
    cd "$path"
    nix develop --no-write-lock-file -c bash -euo pipefail "$session/integration-preparation-c7/sign-owned-target-hooks.sh"
  )
  test "$(git -C "$path" rev-parse HEAD)" = "$base"
  test -z "$(git -C "$path" status --porcelain=v1 --untracked-files=all)"
  printf 'Prepared clean target: %s at %s\n' "$project" "$base"
}

prepare haveapi 1103a3a14b1dc6dec17fc4859df80220a54f111d
prepare vpsfree-cz-configuration bec5556f6c60414e482550dd735321ebe3c3703b
