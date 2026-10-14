#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
prefix=kb-runtime-k-quick4
mapfile -t paths <"$tracking/$prefix-paths.txt"
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = a50f8c1a11ea642edf823f04521f9eaa97132fd2
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary -- "${paths[@]}")
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary -- "${paths[@]}")
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
run nix-json bash -ec '
  for file in flake.nix cluster/nix/test.nix tests/all-tests.nix tests/suite/runtime/standalone.nix; do nix-instantiate --parse "$file" >/dev/null; done
  node -e "JSON.parse(require(\"fs\").readFileSync(\"cluster/default-config.json\"))"
'
verify
