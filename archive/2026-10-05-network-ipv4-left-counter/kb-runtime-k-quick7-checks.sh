#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
prefix=kb-runtime-k-quick7
mapfile -t paths <"$tracking/$prefix-paths.txt"
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = a50f8c1a11ea642edf823f04521f9eaa97132fd2
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary -- "${paths[@]}")
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary -- "${paths[@]}")
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1 --untracked-files=all)
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
export TMPDIR=/tmp
test "$(cat "$tracking/kb-runtime-k-quick6-toolchain.exit")" = 0
test "$(cat "$tracking/kb-runtime-k-quick6-syntax.exit")" = 0
run syntax bash -ec 'bash -n bin/check; shellcheck bin/check'
run profile nix-instantiate --eval --read-write-mode --strict --json tools/test-standalone-profile.nix
run scenarios ruby -rjson -ropen3 -e '
  bytes, errors, status = Open3.capture3("nix-instantiate", "--eval", "--strict", "--json", "tools/standalone-scripts.nix")
  abort errors unless status.success?
  JSON.parse(bytes).each do |name, source|
    out, err, result = Open3.capture3(RbConfig.ruby, "-c", stdin_data: source)
    puts "#{name}: #{out}#{err}"
    abort unless result.success?
  end
'
run export ruby tools/test-capture-export.rb --verbose
verify
