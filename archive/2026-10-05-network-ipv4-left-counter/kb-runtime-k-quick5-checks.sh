#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
prefix=kb-runtime-k-quick5
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
# Observe the owning devShell without reproducing its Ruby declarations here.
run toolchain ruby -rjson -rrubygems -rminitest -rminitest/mock -rtimeout -rosvm -e '
  features = $LOADED_FEATURES.grep(%r{/(?:minitest(?:/mock)?|timeout|osvm)\.rb$})
  raise "non-Nix Ruby feature" unless features.size == 4 && features.all? { |p| p.start_with?("/nix/store/") }
  raise "non-Nix gem path" unless Gem.path.all? { |p| p.start_with?("/nix/store/") }
  raise "wrong OSVM source" unless features.find { |p| p.end_with?("/osvm.rb") }.start_with?(ENV.fetch("VPSADMIN_KB_OSVM_SOURCE") + "/")
  raise "ambient Ruby options retained" if ENV.key?("RUBYOPT")
  puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, ruby_executable: RbConfig.ruby,
    minitest: Minitest::VERSION, timeout: Timeout::VERSION, gem_home: Gem.dir,
    gem_path: Gem.path, features: features, ruby_lib: ENV.fetch("RUBYLIB"),
    osvm_source: ENV.fetch("VPSADMIN_KB_OSVM_SOURCE"))
'
run parse bash -ec '
  nix-instantiate --parse flake.nix >/dev/null
  bash -n bin/check
  shellcheck bin/check
'
run driver ruby tools/test-machine.rb --verbose
verify
