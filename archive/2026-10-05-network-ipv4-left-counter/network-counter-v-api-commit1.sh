#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
cd "$V"
for suffix in log exit; do test ! -e "$TRACK/network-counter-v-api-commit1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = 5d5527a67315c18b595345aa6996d7724c1ed071
 test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
 git diff --cached --quiet
 sha256sum --check "$TRACK/network-counter-v-source1.sha256"
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command bash -ec '
   test -x "$(git rev-parse --git-path hooks)/pre-commit"
   test -x "$(git rev-parse --git-path hooks)/commit-msg"
   ruby -rovercommit -e "puts Overcommit::VERSION"
   mapfile -t paths < /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-api.paths
   git add -- "${paths[@]}"
   git diff --cached --name-only > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-api-commit1.staged
   cmp /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-api.paths /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-api-commit1.staged
   git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-api.message
   git rev-parse HEAD > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-api-commit1.sha
 '
 sha256sum --check "$TRACK/network-counter-v-source1.sha256"
) > "$TRACK/network-counter-v-api-commit1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-v-api-commit1.exit"
exit "$result"
