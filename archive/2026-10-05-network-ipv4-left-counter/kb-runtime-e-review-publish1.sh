#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsfree-dev-workspace
head=f6d2c080469b224ac77765aecd76a6d531358363
old=d2079f605ae87871037ae73c5e5daf20a3e0d03d
branch=2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-e-review-publish1
for suffix in log exit before.remote after.remote published.sha; do test ! -e "$tracking/$prefix.$suffix"; done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
cd "$repo"
test "$(git rev-parse HEAD)" = "$head"
test "$(git branch --show-current)" = "$branch"
test "$(git remote get-url origin)" = git@github.com:vpsfreecz/dev-workspace.git
test -z "$(git status --porcelain=v1 --untracked-files=all)"
test "$(cat "$tracking/kb-runtime-e-review-consolidated.head.sha")" = "$head"
test "$(cat "$tracking/kb-runtime-e-review-eval1.exit")" = 0
sha256sum --check "$tracking/kb-runtime-e-review-pair1-source.sha256" >/dev/null
sha256sum --check "$tracking/kb-runtime-e-review-pin1-generated.sha256" >/dev/null
git fetch origin master
test "$(git rev-parse origin/master)" = 0ff827df13e82dfab4b536ff29979280f264e8f5
git merge-base --is-ancestor origin/master "$head"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/$prefix.before.remote"
lease=
if test -n "$remote"; then
  test "$remote" = "$old"$'\t'"refs/heads/$branch"
  lease=$old
  git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
  test "$(git rev-parse "refs/remotes/origin/$branch")" = "$old"
fi
git push --force-with-lease="refs/heads/$branch:$lease" origin "$head:refs/heads/$branch"
remote=$(git ls-remote --heads origin "refs/heads/$branch")
printf '%s\n' "$remote" >"$tracking/$prefix.after.remote"
test "$remote" = "$head"$'\t'"refs/heads/$branch"
git fetch origin "+refs/heads/$branch:refs/remotes/origin/$branch"
test "$(git rev-parse "refs/remotes/origin/$branch")" = "$head"
test -z "$(git status --porcelain=v1 --untracked-files=all)"
printf '%s\n' "$head" >"$tracking/$prefix.published.sha"
