#!/usr/bin/env bash
set -euo pipefail
export PATH=/home/aither/bin:$PATH
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
head=d2079f605ae87871037ae73c5e5daf20a3e0d03d
base=0ff827df13e82dfab4b536ff29979280f264e8f5
branch=2026-10-05-network-ipv4-left-counter
test ! -e "$tracking/kb-runtime-e-publish1.log"
test ! -e "$tracking/kb-runtime-e-publish1.exit"
exec > >(tee "$tracking/kb-runtime-e-publish1.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/kb-runtime-e-publish1.exit"' EXIT
test "$(dev-session current)" = "$branch"
test "$(cat "$tracking/kb-runtime-e-eval1.exit")" = 0
test "$(git rev-parse HEAD)" = "$head"
test "$(git branch --show-current)" = "$branch"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/dev-workspace.git
test "$(git rev-list --count "$base..$head")" = 2
git fetch origin refs/heads/master:refs/remotes/origin/master
test "$(git rev-parse origin/master)" = "$base"
test -z "$(git ls-remote --heads origin "refs/heads/$branch")"
git push origin "$head:refs/heads/$branch"
test "$(git ls-remote --heads origin "refs/heads/$branch" | cut -f1)" = "$head"
git fetch origin "refs/heads/$branch:refs/remotes/origin/$branch"
test "$(git rev-parse "origin/$branch")" = "$head"
printf '%s\n' "$head" >"$tracking/kb-runtime-e-published.sha"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
