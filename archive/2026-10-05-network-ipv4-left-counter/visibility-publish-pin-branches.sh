#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
worktrees=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter
branch=2026-10-05-network-ipv4-left-counter
mode=${1:?Missing config/kb mode}
head=${2:?Missing exact committed head}
[[ $# == 2 && $head =~ ^[0-9a-f]{40}$ ]]
[[ ${DEV_SESSION_SLUG-} == "$branch" && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
case "$mode" in
  config) repo=vpsfree-cz-configuration; base=6f6aff9029cd57e1a0f9201356f7fdc9f6480671; count=2 ;;
  kb) repo=vpsfree-kb-contracts; base=873758fd6aec0c03f50a94600e0ceab97946f255; count=1 ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "$worktrees/$repo" ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
[[ $(cat "$tracking/visibility-$mode-final.sha") == "$head" ]]
[[ $(git rev-parse HEAD) == "$head" && -z $(git status --porcelain) ]]
[[ $(git rev-list --count "$base..$head") == "$count" ]]
[[ $(git rev-parse "HEAD~$count") == "$base" ]]
[[ ! -e "$tracking/visibility-$mode-published.sha" ]]
lease=$(cat "$tracking/visibility-current-base-$mode-old-remote.sha")
[[ $lease =~ ^[0-9a-f]{40}$ ]]
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$lease" ]]
git fetch --no-tags origin refs/heads/master:refs/remotes/origin/master \
  "+refs/heads/$branch:refs/remotes/origin/$branch"
[[ $(git rev-parse "refs/remotes/origin/$branch") == "$lease" ]]
git merge-base --is-ancestor origin/master "$base"
git log --oneline --left-right "origin/master...$head" >"$tracking/visibility-$mode-default-comparison.log"
# Rewrite only this initiative's verified unpublished pin replacements.
git push --force-with-lease="refs/heads/$branch:$lease" origin "$head:refs/heads/$branch"
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$head" ]]
git fetch --no-tags origin "+refs/heads/$branch:refs/remotes/origin/$branch"
[[ $(git rev-parse "refs/remotes/origin/$branch") == "$head" ]]
printf '%s\n' "$head" >"$tracking/visibility-$mode-published.sha"
