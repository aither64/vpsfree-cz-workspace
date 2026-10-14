#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
prefix=kb-runtime-e-fixture-name-publish1
head=06eefd98d09d756a8791c494cd855ffcfa625548
old=f6d2c080469b224ac77765aecd76a6d531358363
branch=2026-10-05-network-ipv4-left-counter
for suffix in log exit before.remote after.remote published.sha; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd "$repo"
test "$(git rev-parse HEAD)" = "$head"
test "$(git branch --show-current)" = "$branch"
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/dev-workspace.git
test -z "$(git status --porcelain=v1 --untracked-files=all)"
test "$(cat "$tracking/kb-runtime-e-fixture-name-consolidated.head.sha")" = "$head"
sha256sum --check "$tracking/kb-runtime-e-fixture-name-fix1-source.sha256" >/dev/null
test "$(git rev-list --count 0ff827df13e82dfab4b536ff29979280f264e8f5..HEAD)" = 2
git fetch origin master
test "$(git rev-parse origin/master)" = 0ff827df13e82dfab4b536ff29979280f264e8f5
git merge-base --is-ancestor origin/master "$head"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/$prefix.before.remote"
test "$remote" = "$old"$'\t'"refs/heads/$branch"
git push --force-with-lease="refs/heads/$branch:$old" origin "$head:refs/heads/$branch"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/$prefix.after.remote"
test "$remote" = "$head"$'\t'"refs/heads/$branch"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
test "$(git rev-parse "refs/remotes/origin/$branch")" = "$head"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
printf '%s\n' "$head" >"$tracking/$prefix.published.sha"
