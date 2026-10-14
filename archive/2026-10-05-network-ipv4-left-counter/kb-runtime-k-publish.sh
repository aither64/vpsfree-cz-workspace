#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
head=93a16d6cecb6bc847ec9335a3f170eb8b301ab56
branch=2026-10-05-network-ipv4-left-counter-kb-runtime
cd "$repo"
test "$(git rev-parse HEAD)" = "$head"
test "$(git branch --show-current)" = "$branch"
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsfree-kb-contracts.git
test -z "$(git status --porcelain=v1 --untracked-files=all)"
test "$(cat "$tracking/kb-runtime-k-source.sha")" = "$head"
test "$(cat "$tracking/kb-runtime-k-canonical.exit")" = 0
test ! -e "$tracking/kb-runtime-k-published.sha"
git fetch origin master
git merge-base --is-ancestor origin/master "$head"
git log --oneline "$head"..origin/master >"$tracking/kb-runtime-k-publication-default-comparison.log"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/kb-runtime-k-publication-before.remote"
test -z "$remote"
git push origin "$head:refs/heads/$branch"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/kb-runtime-k-publication-after.remote"
test "$remote" = "$(printf '%s\trefs/heads/%s' "$head" "$branch")"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
test "$(git rev-parse "refs/remotes/origin/$branch")" = "$head"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
printf '%s\n' "$head" >"$tracking/kb-runtime-k-published.sha"
