#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-cz-configuration
K=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts
for suffix in log exit; do test ! -e "$TRACK/network-layout-downstream-publish1.$suffix"; done
set +e
(
 set -euo pipefail
 cd "$C"
 test "$(git rev-parse HEAD)" = "$(cat "$TRACK/network-layout-c-final.sha")"
 test -z "$(git status --porcelain)"
 test "$(git ls-remote origin refs/heads/master | cut -f1)" = c1ee03a4db8ebaf6434984e344cba3c0e38a3d2a
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = a433e19a5aecdc934aedeecacc476404411de508
 unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_BIN_PATH BUNDLER_VERSION OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED
 nix develop --command git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:a433e19a5aecdc934aedeecacc476404411de508 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = "$(cat "$TRACK/network-layout-c-final.sha")"
 git fetch --no-tags origin +refs/heads/2026-10-05-network-ipv4-left-counter:refs/remotes/origin/2026-10-05-network-ipv4-left-counter
 cd "$K"
 test "$(git rev-parse HEAD)" = "$(cat "$TRACK/network-layout-k-final.sha")"
 test -z "$(git status --porcelain)"
 test "$(git ls-remote origin refs/heads/master | cut -f1)" = 873758fd6aec0c03f50a94600e0ceab97946f255
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = 819c4824eddbad89a3b1f797219becd8d33fcc48
 git push --force-with-lease=refs/heads/2026-10-05-network-ipv4-left-counter:819c4824eddbad89a3b1f797219becd8d33fcc48 origin HEAD:refs/heads/2026-10-05-network-ipv4-left-counter
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = "$(cat "$TRACK/network-layout-k-final.sha")"
 git fetch --no-tags origin +refs/heads/2026-10-05-network-ipv4-left-counter:refs/remotes/origin/2026-10-05-network-ipv4-left-counter
) > "$TRACK/network-layout-downstream-publish1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-layout-downstream-publish1.exit"
exit "$result"
