#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-kb-contracts-runtime
head=68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e
old=93a16d6cecb6bc847ec9335a3f170eb8b301ab56
branch=2026-10-05-network-ipv4-left-counter-kb-runtime
prefix=kb-runtime-review-fix-publish1
for suffix in log exit before.remote after.remote published.sha; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd "$repo"
test "$(git rev-parse HEAD)" = "$head"
test "$(git branch --show-current)" = "$branch"
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/vpsfree-kb-contracts.git
test -z "$(git status --porcelain=v1 --untracked-files=all)"
test "$(cat "$tracking/kb-runtime-review-fix-consolidated.sha")" = "$head"
test "$(cat "$tracking/kb-runtime-review-fix-canonical1.exit")" = 0
sha256sum --check "$tracking/kb-runtime-review-fix-quick2-source.sha256" >/dev/null
git fetch origin master
test "$(git rev-parse origin/master)" = 873758fd6aec0c03f50a94600e0ceab97946f255
git merge-base --is-ancestor origin/master "$head"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/$prefix.before.remote"
test "$remote" = "$old"$'\t'"refs/heads/$branch"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
test "$(git rev-parse "refs/remotes/origin/$branch")" = "$old"
git push --force-with-lease="refs/heads/$branch:$old" origin "$head:refs/heads/$branch"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/$prefix.after.remote"
test "$remote" = "$head"$'\t'"refs/heads/$branch"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
test "$(git rev-parse "refs/remotes/origin/$branch")" = "$head"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
printf '%s\n' "$head" >"$tracking/$prefix.published.sha"
