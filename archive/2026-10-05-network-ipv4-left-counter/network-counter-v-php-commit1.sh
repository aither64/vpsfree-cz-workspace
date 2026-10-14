#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
for suffix in log exit; do test ! -e "$TRACK/network-counter-v-php-commit1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = adb6bb9cb24e0cf833fff6a9de40b87588cc13cf
 git diff --cached --quiet
 sha256sum --check "$TRACK/network-counter-v-source1.sha256"
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command bash -ec '
   test -x "$(git rev-parse --git-path hooks)/pre-commit"
   test -x "$(git rev-parse --git-path hooks)/commit-msg"
   ruby -rovercommit -e "puts Overcommit::VERSION"
   mapfile -t paths < /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-php.paths
   git add -- "${paths[@]}"
   git commit -F /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-php-final.message
   git rev-parse HEAD > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/network-counter-v-php-commit1.sha
 '
 sha256sum --check "$TRACK/network-counter-v-source1.sha256"
 test -z "$(git status --porcelain)"
 git rev-parse HEAD^{tree} > "$TRACK/network-counter-v-pre-rebase.tree"
) > "$TRACK/network-counter-v-php-commit1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-v-php-commit1.exit"
exit "$result"
