#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
expected=9fe491218e35a3250f2a72c203c2cecc3cb7ae16
branch=2026-10-05-network-ipv4-left-counter
test "$(cat "$tracking/kb-runtime-generic-eof-final.sha")" = "$expected"
test "$(git rev-parse HEAD)" = "$expected"
test "$(git branch --show-current)" = "$branch"
test -z "$(git status --porcelain=v1)"
test "$(git remote get-url origin)" = git@github.com:aither64/dev-workspace.git
git fetch origin master
git merge-base --is-ancestor origin/master HEAD
old=$(git ls-remote --heads origin "refs/heads/$branch")
test "$old" = $'9b5bb4d61413e1de7702f45b50ef3229d2b93244\trefs/heads/2026-10-05-network-ipv4-left-counter'
git push --force-with-lease="refs/heads/$branch:9b5bb4d61413e1de7702f45b50ef3229d2b93244" origin "$expected:refs/heads/$branch"
current=$(git ls-remote --heads origin "refs/heads/$branch")
test "$current" = "$expected"$'\t'"refs/heads/$branch"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
set -o noclobber
printf '%s\n' "$expected" > "$tracking/kb-runtime-generic-eof-final-published.sha"
