#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ${DEV_SESSION_SLUG-} == 2026-10-05-network-ipv4-left-counter && ${DEV_SESSION_WORKSPACE-} == /home/aither/workspace/ai/vpsfree.cz ]]
case "${1-}" in
  v)
    repo=vpsadmin
    branch=2026-10-05-network-ipv4-left-counter
    default=master
    old=6b3628af665049dc095ba985ef0fbe8a22286863
    selected=30603a832d2848207bd7319c79c6b0388bc8646a
    ;;
  w)
    repo=vpsadmin-webui
    branch=dev/network-enabled
    default=main
    old=811742f50cce2b7724784d0a674c8d4d5dcb6273
    selected=b3b756a7b45864459bd39481a0d5245886777660
    ;;
  *) exit 2 ;;
esac
revision=$(cat "$tracking/remediation-source-$1.sha")
[[ $revision =~ ^[0-9a-f]{40}$ ]]
[[ $revision == "$selected" ]]
[[ $(pwd -P) == "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/$repo" ]]
[[ $(git branch --show-current) == "$branch" ]]
[[ $(git rev-parse HEAD) == "$revision" ]]
[[ -z $(git status --porcelain) ]]
[[ $(git remote get-url origin) == "git@github.com:vpsfreecz/$repo.git" ]]
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$old" ]]
git fetch --no-tags origin "refs/heads/$default:refs/remotes/origin/$default"
git merge-base --is-ancestor "origin/$default" "$revision"
git log --oneline --left-right "origin/$default...$revision" >"$tracking/remediation-publish-$1-default-comparison.log"
git push "--force-with-lease=refs/heads/$branch:$old" origin "$revision:refs/heads/$branch"
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$revision" ]]
printf '%s\n' "$revision" >"$tracking/remediation-published-$1.sha"
