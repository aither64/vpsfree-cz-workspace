#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
cd "$C"
for suffix in log exit remote; do test ! -e "$TRACK/finish-http-c-publish1.$suffix"; done
set +e
(
  set -euo pipefail
  test "$(git rev-parse HEAD)" = 35b4fa2d664bde95db140240ac929b1f61c4e688
  test -z "$(git status --porcelain)"
  test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
  test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsfree-cz-configuration.git
  git fetch origin master
  test "$(git rev-parse origin/master)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
  test "$(git rev-parse HEAD~2)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
  test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = f1141690dd3592cc1e7fc14b91e85aac8ec5d51d
  git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:f1141690dd3592cc1e7fc14b91e85aac8ec5d51d origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
  git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter > "$TRACK/finish-http-c-publish1.remote"
  test "$(cut -f1 "$TRACK/finish-http-c-publish1.remote")" = 35b4fa2d664bde95db140240ac929b1f61c4e688
) > "$TRACK/finish-http-c-publish1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/finish-http-c-publish1.exit"
exit "$result"
