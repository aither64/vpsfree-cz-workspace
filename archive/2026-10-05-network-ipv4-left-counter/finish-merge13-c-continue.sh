#!/usr/bin/env bash
set -uo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration || exit 1
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
nix develop --command bash -ec 'bundle install; GIT_EDITOR=true git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --continue' > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-merge13-c-continue.log 2>&1
code=$?
printf '%s\n' "$code" > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-merge13-c-continue.exit
exit "$code"
