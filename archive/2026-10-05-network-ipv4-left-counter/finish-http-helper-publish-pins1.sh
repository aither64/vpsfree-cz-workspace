#!/usr/bin/env bash
set -euo pipefail
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
V=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
cd "$TRACK"
for suffix in log exit remote c-remote; do test ! -e "$TRACK/finish-http-helper-publish-pins1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(cat "$TRACK/finish-http-helper-operation1.exit")" = 0
 cd "$V"
 test "$(git rev-parse HEAD)" = ebe4fab3d50a51bda1f94014ca95c73ba2a967a8
 test -z "$(git status --porcelain)"
 test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsadmin.git
 git fetch origin master
 test "$(git rev-parse origin/master)" = 6c706c285681f1bc356cdc2569f5bd53817c6326
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 7e86ee211d898256bd93cac7221c256636f3fcc3
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop .#vpsadmin --command git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:7e86ee211d898256bd93cac7221c256636f3fcc3 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
 git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter > "$TRACK/finish-http-helper-publish-pins1.remote"
 test "$(cut -f1 "$TRACK/finish-http-helper-publish-pins1.remote")" = ebe4fab3d50a51bda1f94014ca95c73ba2a967a8
 bash "$TRACK/finish-http-helper-c-pins1.sh"
 test "$(cat "$TRACK/finish-http-helper-c-pins1.exit")" = 0
 cd "$C"
 test -z "$(git status --porcelain)"
 test "$(git rev-parse HEAD)" = "$(cat "$TRACK/finish-http-helper-c-pins1.sha")"
 test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsfree-cz-configuration.git
 git fetch origin master
 test "$(git rev-parse origin/master)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 35b4fa2d664bde95db140240ac929b1f61c4e688
 nix develop --command git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:35b4fa2d664bde95db140240ac929b1f61c4e688 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
 git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter > "$TRACK/finish-http-helper-publish-pins1.c-remote"
 test "$(cut -f1 "$TRACK/finish-http-helper-publish-pins1.c-remote")" = "$(cat "$TRACK/finish-http-helper-c-pins1.sha")"
) > "$TRACK/finish-http-helper-publish-pins1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-helper-publish-pins1.exit"
exit "$result"
