#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
prefix=kb-runtime-e-inputs1
mapfile -t paths <"$tracking/$prefix-paths.txt"
verify_source() {
  test "$(git -C "$repo" rev-parse HEAD)" = 0ff827df13e82dfab4b536ff29979280f264e8f5
  test "$(git -C "$repo" branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary -- "${paths[@]}")
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary)
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1 --untracked-files=all -- . ':!flake.lock')
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
verify_source
cmp "$tracking/$prefix-before.lock" "$repo/flake.lock"
run preflight bash -ec '
  nix --version
  python3 --version
  git fetch origin master:refs/remotes/origin/master
  git merge-base --is-ancestor refs/remotes/origin/master HEAD
  nix-instantiate --parse flake.nix >/dev/null
'
run generate nix flake update dev-workspace kb-runtime
verify_source
run graph python3 "$tracking/$prefix-graph.py" "$tracking/$prefix-before.lock" "$repo/flake.lock" "$tracking/$prefix-selected-d.lock" "$tracking/$prefix-selected-k.lock" "$tracking/$prefix-d-receipt.json"
run whitespace git diff --check -- flake.nix flake.lock
cp --no-clobber "$repo/flake.lock" "$tracking/$prefix-generated.lock"
git -C "$repo" diff --binary -- flake.lock >"$tracking/$prefix-generated.diff"
sha256sum "$repo/flake.lock" >"$tracking/$prefix-generated.sha256"
verify_source
