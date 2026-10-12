#!/usr/bin/env bash
set -eu
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/haveapi-release
nix develop -c bash -c 'set -e
(cd servers/ruby && BUNDLE_GEMFILE="$PWD/Gemfile" bundle exec rspec)
make release
BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle exec ruby /home/aither/workspace/ai/vpsfree.cz/work/2026-10-11-diagnose-vpsadmin-api-exception/verify-release-artifact.rb dist/haveapi-0.29.9.gem
sha256sum dist/*.gem
git diff --exit-code
'
