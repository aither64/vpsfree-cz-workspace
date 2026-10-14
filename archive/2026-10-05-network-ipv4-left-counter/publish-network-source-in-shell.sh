#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=${1:?Missing repo}
branch=${2:?Missing branch}
default=${3:?Missing default}
revision=${4:?Missing revision}
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
case "$repo:$branch:$default" in
  vpsadmin:2026-10-05-network-ipv4-left-counter:master|vpsadmin-webui:dev/network-enabled:main) ;;
  *) exit 2 ;;
esac
[[ $(pwd -P) == "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo" ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git rev-parse HEAD) == "$revision" ]]
[[ -z $(git status --porcelain) ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
git fetch --no-tags origin "refs/heads/$default:refs/remotes/origin/$default"
git log --oneline --left-right "origin/$default...$revision" >"$tracking/source-$repo-default-comparison.log"
git diff --stat "origin/$default...$revision"
git merge-base --is-ancestor "origin/$default" "$revision"
git push origin "$revision:refs/heads/$branch"
git ls-remote --heads origin "refs/heads/$branch"
