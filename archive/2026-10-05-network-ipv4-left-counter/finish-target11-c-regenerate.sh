#!/usr/bin/env bash
set -euo pipefail
T=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
test ! -e "$T/finish-target11-c-regenerate.log"
set +e
(
set -euo pipefail
cd "$C"
test "$(git rev-parse HEAD)" = d275b5f3455fd25633a053e49989fc1d33f1c620
test -z "$(git status --porcelain)"
test "$(git rev-parse origin/master)" = bfb1d89c95308024a9269974c207bf7cefe1fb1c
unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
nix develop --command bash -ec '
 git -c rebase.autoStash=false -c rebase.updateRefs=false rebase --onto bfb1d89c95308024a9269974c207bf7cefe1fb1c d275b5f3455fd25633a053e49989fc1d33f1c620
 test "$(git rev-parse HEAD)" = bfb1d89c95308024a9269974c207bf7cefe1fb1c
 confctl inputs channel set --commit --no-editor vpsadmin vpsadmin 4a21dd25b23de9832166def98526f410416b651e
 confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui cce681424b866f6a51cbc0a1e4daa226ed33fc07
'
test -z "$(git status --porcelain)"
test "$(git rev-parse HEAD~2)" = bfb1d89c95308024a9269974c207bf7cefe1fb1c
git rev-parse HEAD > "$T/finish-target11-c.head"
) > "$T/finish-target11-c-regenerate.log" 2>&1
result=$?
printf '%s\n' "$result" > "$T/finish-target11-c-regenerate.exit"
exit "$result"
