#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/.local/state/dev-workspaces/profile/bin:/home/aither/.nix-profile/bin:$PATH
TRACK=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
K=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts
cd "$K"
for suffix in log exit; do test ! -e "$TRACK/network-counter-k-pin1.$suffix"; done
set +e
(
 set -euo pipefail
 test "$(git rev-parse HEAD)" = a50f8c1a11ea642edf823f04521f9eaa97132fd2
 test "$(git rev-parse origin/master)" = 873758fd6aec0c03f50a94600e0ceab97946f255
 test -z "$(git status --porcelain)"
 test "$(git rev-list --count origin/master..HEAD)" = 1
 git diff --name-only origin/master..HEAD > "$TRACK/network-counter-k-old.paths"
 printf '%s\n' captures.json contract/navigation.yml contract/pages.yml flake.lock flake.nix > "$TRACK/network-counter-k-expected.paths"
 cmp "$TRACK/network-counter-k-old.paths" "$TRACK/network-counter-k-expected.paths"
 git log --format=fuller origin/master..HEAD > "$TRACK/network-counter-k-old.history"
 git diff --binary --full-index origin/master..HEAD > "$TRACK/network-counter-k-old.diff"
 git rev-parse HEAD^{tree} > "$TRACK/network-counter-k-old.tree"
 test "$(git ls-remote origin refs/heads/2026-10-05-network-ipv4-left-counter | cut -f1)" = a50f8c1a11ea642edf823f04521f9eaa97132fd2
 git rebase --onto origin/master HEAD
 python3 "$TRACK/fixture-final-pin-guards.py" set-kb "$K" a50f8c1a11ea642edf823f04521f9eaa97132fd2 cc8e9e7e421a258a46279304c910f88e2ad33147 0000000000000000000000000000000000000000
 nix flake update vpsadmin
 python3 "$TRACK/fixture-final-pin-guards.py" kb "$K" a50f8c1a11ea642edf823f04521f9eaa97132fd2 cc8e9e7e421a258a46279304c910f88e2ad33147 0000000000000000000000000000000000000000
 git diff --name-only > "$TRACK/network-counter-k-candidate.paths"
 cmp "$TRACK/network-counter-k-candidate.paths" "$TRACK/network-counter-k-expected.paths"
 git diff --binary --full-index > "$TRACK/network-counter-k-candidate.diff"
 git diff --exit-code a50f8c1a -- screenshots scenarios fixtures contract/pages > "$TRACK/network-counter-k-protected.diff"
) > "$TRACK/network-counter-k-pin1.log" 2>&1
result=$?
printf '%s\n' "$result" > "$TRACK/network-counter-k-pin1.exit"
exit "$result"
