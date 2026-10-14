#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.nix-profile/bin:$PATH
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
source_tree=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
prefix=$tracking/network-counter-tools1
cd "$tracking"
test "$(dev-session current)" = "$DEV_SESSION_SLUG"
cd "$source_tree"
test "$(git rev-parse HEAD)" = 5d5527a67315c18b595345aa6996d7724c1ed071
git diff --quiet --cached
git diff --quiet -- flake.nix flake.lock
test ! -e "$prefix.log"
test ! -e "$prefix.exit"
set -o noclobber
exec >"$prefix.log" 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$prefix.exit"; exit "$result"' EXIT
step() {
  local name=$1 result
  shift
  set +e
  "$@" >"$prefix-$name.log" 2>&1
  result=$?
  set -e
  printf '%s\n' "$result" >"$prefix-$name.exit"
  return "$result"
}
step api-shell env -u VPSADMIN_PLUGINS -u RUBYOPT nix develop .#api --command bash -ec '
  test "$PWD" = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin/api
  ruby --version
  command -v ruby
  command -v bundle
  bundle exec ruby -e "require \"rake\"; puts Rake::VERSION"
'
step webui-shell nix develop .#webui --command bash -ec '
  test "$PWD" = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin/webui
  for tool in xgettext msgmerge msgfmt; do command -v "$tool"; done
'
test "$(git rev-parse HEAD)" = 5d5527a67315c18b595345aa6996d7724c1ed071
git diff --quiet --cached
git diff --quiet -- flake.nix flake.lock
