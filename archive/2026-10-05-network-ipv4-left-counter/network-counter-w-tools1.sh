#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.nix-profile/bin:$PATH
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd "$tracking"
test "$(dev-session current)" = "$DEV_SESSION_SLUG"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui
test "$(git rev-parse HEAD)" = e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
git diff --quiet --cached
git diff --quiet -- flake.nix flake.lock package.json package-lock.json
prefix=$tracking/network-counter-w-tools1
test ! -e "$prefix.log"
test ! -e "$prefix.exit"
set -o noclobber
exec >"$prefix.log" 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$prefix.exit"; exit "$result"' EXIT
nix develop --command bash -ec '
  node --version
  command -v node
  npm --version
  node -e "console.log(require.resolve(\"typescript\"))"
'
git diff --quiet --cached
git diff --quiet -- flake.nix flake.lock package.json package-lock.json
