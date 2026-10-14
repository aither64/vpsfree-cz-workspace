#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
expected=$(cat "$tracking/kb-runtime-d-upstream-source.sha")
[[ "$expected" =~ ^[0-9a-f]{40}$ ]]
branch=2026-10-05-network-ipv4-left-counter
test "$(cat "$tracking/kb-runtime-d-upstream-source.sha")" = "$expected"
test "$(git rev-parse HEAD)" = "$expected"
test "$(git branch --show-current)" = "$branch"
test -z "$(git status --porcelain=v1)"
test "$(git remote get-url origin)" = git@github.com:aither64/dev-workspace.git
git fetch origin refs/heads/master:refs/remotes/origin/master
test "$(git rev-parse origin/master)" = a2bbf2f1c588de7eec0d7d52580a89a9d4bef984
git merge-base --is-ancestor origin/master HEAD
old=$(git ls-remote --heads origin "refs/heads/$branch")
test "$old" = $'9fe491218e35a3250f2a72c203c2cecc3cb7ae16\trefs/heads/2026-10-05-network-ipv4-left-counter'
git push --force-with-lease="refs/heads/$branch:9fe491218e35a3250f2a72c203c2cecc3cb7ae16" origin "$expected:refs/heads/$branch"
current=$(git ls-remote --heads origin "refs/heads/$branch")
test "$current" = "$expected"$'\t'"refs/heads/$branch"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
set -o noclobber
printf '%s\n' "$expected" > "$tracking/kb-runtime-d-upstream-published.sha"
