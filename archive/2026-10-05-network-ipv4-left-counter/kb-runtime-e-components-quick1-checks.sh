#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
prefix=kb-runtime-e-components-quick1
mapfile -t paths <"$tracking/$prefix-paths.txt"
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = 0ff827df13e82dfab4b536ff29979280f264e8f5
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
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_BIN BUNDLE_WITH BUNDLE_WITHOUT
export GEM_HOME="$(ruby --disable-gems -rrubygems -e 'print Gem.default_dir')"
export GEM_PATH="$GEM_HOME"
export TMPDIR=/tmp
run toolchain ruby -rjson -rrubygems -rminitest -rtimeout -e '
  features = $LOADED_FEATURES.grep(%r{/(?:minitest|timeout)\.rb$})
  raise "non-Nix test feature" unless features.size == 2 && features.all? { |p| p.start_with?("/nix/store/") }
  raise "non-Nix gem path" unless Gem.path.all? { |p| p.start_with?("/nix/store/") }
  puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, ruby_executable: RbConfig.ruby,
    minitest: Minitest::VERSION, timeout: Timeout::VERSION, features: features, gem_paths: Gem.path,
    runtime_contract: ENV.fetch("DEVCLUSTER_RUNTIME_CONTRACT"))
'
run syntax bash -ec '
  for file in dev-clusters/kb/lib/{managed,provider,guards,connection,lease}.rb test/kb_{devcluster,guards,connection,lease}_test.rb; do ruby -c "$file"; done
'
run binding-status ruby test/kb_devcluster_test.rb --verbose
run guards ruby test/kb_guards_test.rb --verbose
run connection ruby test/kb_connection_test.rb --verbose
run lease ruby test/kb_lease_test.rb --verbose
verify
