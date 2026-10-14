#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
prefix=kb-runtime-e-integrated-quick1
mapfile -t paths <"$tracking/$prefix-paths.txt"
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = 0ff827df13e82dfab4b536ff29979280f264e8f5
  test "$(git -C "$repo" branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  sha256sum --check "$tracking/$prefix-source.sha256"
  sha256sum --check "$tracking/$prefix-metadata.sha256"
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
export VPSFREE_KB_ENGINE_METADATA=/nix/store/8h3aayb16fhr7h36r6gvwx5a824rh80k-vpsfree-kb-runtime-source.json
run toolchain ruby "$tracking/$prefix-toolchain.rb"
run syntax bash -ec '
  for path in dev-clusters/kb/bin/devcluster dev-clusters/kb/lib/*.rb test/kb_{devcluster,guards,connection,lease,cli,portable}_test.rb test/support/kb_snapshot_fixture.rb; do
    ruby -c "$path"
  done
  for path in flake.nix nix/organization-tools.nix nix/site-config.nix; do
    nix-instantiate --parse "$path" >/dev/null
  done
  ruby -rjson -e "abort unless JSON.parse(File.read(ARGV.fetch(0))).is_a?(Hash)" test/fixtures/kb-config.json
'
run binding-status ruby test/kb_devcluster_test.rb --verbose
run guards ruby test/kb_guards_test.rb --verbose
run connection ruby test/kb_connection_test.rb --verbose
run lease ruby test/kb_lease_test.rb --verbose
run cli ruby test/kb_cli_test.rb --verbose
run portable ruby test/kb_portable_test.rb --verbose
verify
