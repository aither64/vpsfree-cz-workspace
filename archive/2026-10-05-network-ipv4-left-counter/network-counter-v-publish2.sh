#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
for suffix in log exit; do test ! -e "$TRACK/network-counter-v-publish2.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = cc8e9e7e421a258a46279304c910f88e2ad33147
 test -z "$(git status --porcelain)"
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 5d5527a67315c18b595345aa6996d7724c1ed071
 test "$(git ls-remote origin refs/heads/master | cut -f1)" = 81f1f1aabdd18a042d276aa4be3ca32173ff14d0
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command bash -ec '
   ruby -rovercommit -e "puts Overcommit::VERSION"
   git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:5d5527a67315c18b595345aa6996d7724c1ed071 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
 '
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = cc8e9e7e421a258a46279304c910f88e2ad33147
 test -z "$(git status --porcelain)"
) > "$TRACK/network-counter-v-publish2.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-v-publish2.exit"
exit "$result"
