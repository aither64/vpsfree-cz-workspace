#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
prefix=kb-runtime-review-fix-canonical1
head=68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e
for suffix in log exit before-lock.sha after-lock.sha; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd "$repo"
verify() {
  test "$(git rev-parse HEAD)" = "$head"
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter-kb-runtime
  test -z "$(git status --porcelain=v1 --untracked-files=all)"
  test "$(cat "$tracking/kb-runtime-review-fix-consolidated.sha")" = "$head"
  sha256sum --check "$tracking/kb-runtime-review-fix-quick2-source.sha256" >/dev/null
}
verify
sha256sum flake.nix flake.lock >"$tracking/$prefix.before-lock.sha"
nix develop --command bin/check
verify
sha256sum flake.nix flake.lock >"$tracking/$prefix.after-lock.sha"
cmp "$tracking/$prefix.before-lock.sha" "$tracking/$prefix.after-lock.sha"
