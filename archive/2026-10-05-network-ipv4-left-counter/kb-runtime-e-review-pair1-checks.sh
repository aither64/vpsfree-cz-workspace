#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
prefix=kb-runtime-e-review-pair1
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = d2079f605ae87871037ae73c5e5daf20a3e0d03d
  test "$(git -C "$repo" branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  sha256sum --check "$tracking/$prefix-source.sha256"
  sha256sum --check "$tracking/$prefix-immutable.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary -- . ':!flake.lock')
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary)
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1 --untracked-files=all -- . ':!flake.lock')
  for gate in preflight generate graph whitespace; do
    test "$(cat "$tracking/kb-runtime-e-review-pin1-$gate.exit")" = 0
  done
  test "$(cat "$tracking/kb-runtime-e-review-pin1.exit")" = 0
  sha256sum --check "$tracking/kb-runtime-e-review-pin1-generated.sha256"
  cmp "$tracking/kb-runtime-e-review-pin1-generated.lock" "$repo/flake.lock"
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
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH
while IFS= read -r name; do unset "$name"; done < <(compgen -v BUNDLE_ || true)
export GEM_HOME="$(ruby --disable-gems -rrubygems -e 'print Gem.default_dir')"
export GEM_PATH="$GEM_HOME"
export TMPDIR=/tmp
run toolchain ruby "$tracking/$prefix-toolchain.rb" "$tracking/$prefix-d-receipt.json" "$tracking/$prefix-k-receipt.json"
run syntax bash -ec '
  for path in dev-clusters/kb/bin/devcluster dev-clusters/kb/lib/*.rb test/support/kb_snapshot_fixture.rb test/kb_portable_test.rb test/kb_public_dispatch_test.rb; do ruby -c "$path"; done
'
run sdk ruby test/kb_portable_test.rb --verbose
run composition ruby test/kb_public_dispatch_test.rb --verbose
verify
