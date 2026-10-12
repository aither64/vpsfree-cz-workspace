#!/usr/bin/env bash
set -eu
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/haveapi-release
nix develop -c bash -c 'set -e
for component in clients/ruby servers/ruby clients/go; do
  BUNDLE_GEMFILE="$PWD/$component/Gemfile" bundle install
done
cd clients/js
npm install --package-lock=false
'
