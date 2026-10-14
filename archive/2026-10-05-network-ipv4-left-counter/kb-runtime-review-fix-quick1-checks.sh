#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
prefix=kb-runtime-review-fix-quick1
mapfile -t paths <"$tracking/$prefix-paths.txt"
mapfile -t protected <"$tracking/$prefix-protected-paths.txt"
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = "$(cat "$tracking/$prefix-source.head")"
  test "$(git -C "$repo" branch --show-current)" = "$(cat "$tracking/$prefix-source.branch")"
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary -- "${paths[@]}")
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary)
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1 --untracked-files=all)
  diff -u "$tracking/$prefix-source.protected.diff" <(git -C "$repo" diff HEAD --binary -- "${protected[@]}")
  ruby -rjson -e '
    JSON.parse(File.read(ARGV.fetch(1))).each do |row|
      path = File.join(ARGV.fetch(0), row.fetch("path"))
      abort "source mode changed" unless "0o#{(File.stat(path).mode & 0o777).to_s(8)}" == row.fetch("mode")
      abort "source size changed" unless File.size(path) == row.fetch("bytes")
    end
  ' "$repo" "$tracking/$prefix-source.files.json"
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
unset NODE_OPTIONS
run toolchain ruby -rjson -rrbconfig -rminitest -rtimeout -ropen3 -e '
  gems = %w[minitest timeout].to_h { |name| [name, Gem.loaded_specs.fetch(name).full_gem_path] }
  features = $LOADED_FEATURES.grep(%r{/(?:minitest|timeout)(?:/|\.rb)} )
  abort "Undeclared Ruby gems" unless gems.values.all? { |value| value.start_with?("/nix/store/") } && features.all? { |value| value.start_with?("/nix/store/") }
  bytes, status = Open3.capture2("node", "-e", "process.stdout.write(JSON.stringify({ executable: process.execPath, versions: process.versions }))")
  abort "Node toolchain failed" unless status.success?
  node = JSON.parse(bytes)
  abort "Undeclared Node" unless node.fetch("executable").start_with?("/nix/store/")
  abort "Undeclared Ruby" unless RbConfig.ruby.start_with?("/nix/store/")
  puts JSON.pretty_generate({ ruby: { version: RUBY_VERSION, executable: RbConfig.ruby, minitest: Minitest::VERSION,
    timeout: Timeout::VERSION, gems: gems, loaded_features: features, gem_home: ENV["GEM_HOME"], gem_path: ENV["GEM_PATH"] }, node: node })
'
run syntax bash -ec '
  for source in lib/artifacts.cjs lib/browser.cjs lib/capture-session.cjs lib/connection.cjs runner/capture.cjs tools/test-capture-lease.cjs; do
    node --check "$source"
  done
  ruby -c cluster/lib/kb_runtime.rb
  ruby -c tools/test-runtime.rb
  bash -n bin/check
  shellcheck bin/check
  git diff --check
'
run node bash -ec '
  node --test --test-reporter=tap tools/test-connection.cjs tools/test-artifacts.cjs tools/test-capture-lease.cjs
  node tools/test-browser.cjs
'
run runtime ruby tools/test-runtime.rb --verbose
verify
