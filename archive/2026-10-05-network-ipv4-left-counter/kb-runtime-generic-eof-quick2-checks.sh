#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
prefix=kb-runtime-generic-eof-quick2
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = 9b5bb4d61413e1de7702f45b50ef3229d2b93244
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1)
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
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_BIN BUNDLE_WITH BUNDLE_WITHOUT
export GEM_HOME="$(ruby --disable-gems -rrubygems -e 'print Gem.default_dir')"
export GEM_PATH="$GEM_HOME"
run toolchain ruby -rjson -rrubygems -rminitest -rtimeout -e '
  features = $LOADED_FEATURES.grep(%r{/(?:minitest|timeout)\.rb$})
  raise "non-Nix Ruby gem source" unless features.size == 2 && features.all? { |p| p.start_with?("/nix/store/") }
  raise "non-Nix gem path" unless Gem.path.all? { |p| p.start_with?("/nix/store/") }
  puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, ruby_executable: RbConfig.ruby,
    minitest: Minitest::VERSION, timeout: Timeout::VERSION, gem_home: Gem.dir,
    gem_path: Gem.path, features: features)
'
run syntax bash -c 'ruby -c libexec/workspace-host && ruby -c test/workspace_host/commands_and_locks_test.rb'
run commands ruby test/workspace_host_test.rb --name '/capture_lease|non_streaming_provider|cluster_command|waiting_host_mutation|ordinary_dispatch|exec_with_workspace|dev_session_dispatch/'
verify
