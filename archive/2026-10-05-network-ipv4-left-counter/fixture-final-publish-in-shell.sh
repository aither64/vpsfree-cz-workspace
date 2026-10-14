#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
mode=${1:?Missing v/w mode}
shift
source "$tracking/fixture-final-common.sh"
select_source "$mode"
[[ $(pwd -P) == "$repo_root" ]]
[[ ! -e "$tracking/fixture-final-published-$mode.sha" ]]
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$lease" ]]
git fetch --no-tags origin "refs/heads/$default:refs/remotes/origin/$default"
git merge-base --is-ancestor "origin/$default" "$revision"
git log --oneline --left-right "origin/$default...$revision" >"$tracking/fixture-final-publish-$mode-default-comparison.log"
git push "--force-with-lease=refs/heads/$branch:$lease" origin "$revision:refs/heads/$branch"
[[ $(git ls-remote --heads origin "refs/heads/$branch" | cut -f1) == "$revision" ]]
git fetch --no-tags origin "+refs/heads/$branch:refs/remotes/origin/$branch"
[[ $(git rev-parse "refs/remotes/origin/$branch") == "$revision" ]]
printf '%s\n' "$revision" >"$tracking/fixture-final-published-$mode.sha"
