#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
prefix=kb-runtime-k-quick3
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
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_BIN BUNDLE_WITH BUNDLE_WITHOUT
export GEM_HOME="$(ruby --disable-gems -rrubygems -e 'print Gem.default_dir')"
export GEM_PATH="$GEM_HOME"
export TMPDIR=/tmp
export RUBYLIB="$VPSADMIN_KB_OSVM_SOURCE/osvm/lib:$VPSADMIN_KB_OSVM_SOURCE/test-runner/lib:$VPSADMIN_KB_OSVM_SOURCE/libosctl/lib"
run toolchain ruby -rjson -rrubygems -rminitest -rminitest/mock -rtimeout -rosvm -e '
  features = $LOADED_FEATURES.grep(%r{/(?:minitest(?:/mock)?|timeout|osvm)\.rb$})
  raise "non-Nix Ruby feature" unless features.size == 4 && features.all? { |p| p.start_with?("/nix/store/") }
  raise "non-Nix gem path" unless Gem.path.all? { |p| p.start_with?("/nix/store/") }
  raise "wrong OSVM source" unless features.find { |p| p.end_with?("/osvm.rb") }.start_with?(ENV.fetch("VPSADMIN_KB_OSVM_SOURCE") + "/")
  puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, ruby_executable: RbConfig.ruby,
    minitest: Minitest::VERSION, timeout: Timeout::VERSION, gem_home: Gem.dir,
    gem_path: Gem.path, features: features, osvm_source: ENV.fetch("VPSADMIN_KB_OSVM_SOURCE"))
'
run syntax bash -ec '
  for file in cluster/lib/kb_*.rb cluster/lib/devcluster_runner.rb cluster/launcher.rb cluster/source-metadata.rb cluster/artifact-lock.rb runner/validate*.rb tools/test-runtime.rb tools/test-closure.rb tools/test-machine.rb tools/fixtures/fake-kb-runner.rb; do ruby -c "$file"; done
  for file in runner/*.cjs lib/*.cjs fixtures/*.cjs scenarios/*.cjs tools/test-*.cjs; do node --check "$file"; done
  bash -n bin/devcluster bin/check bin/capture bin/validate bin/contact-sheet test-runner.sh
  shellcheck bin/devcluster bin/check bin/capture bin/validate bin/contact-sheet test-runner.sh
'
run runtime ruby tools/test-runtime.rb --verbose
run closure ruby tools/test-closure.rb --verbose
run driver ruby tools/test-machine.rb --verbose
run connection-artifacts node --test tools/test-connection.cjs tools/test-artifacts.cjs tools/test-browser.cjs
run nix-json bash -ec '
  for file in flake.nix cluster/nix/test.nix tests/all-tests.nix tests/suite/runtime/standalone.nix; do nix-instantiate --parse "$file" >/dev/null; done
  node -e "JSON.parse(require(\"fs\").readFileSync(\"cluster/default-config.json\"))"
'
verify
