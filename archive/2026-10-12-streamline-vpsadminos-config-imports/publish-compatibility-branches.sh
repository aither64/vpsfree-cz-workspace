#!/usr/bin/env bash
set -eu
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports
branch=2026-10-12-streamline-vpsadminos-config-imports
expected_head=$(cat "$record/compatibility-final-head")
[ "$(cat "$record/compatibility-review-runtime-clearance")" = "$expected_head" ]
cd "$group/vpsadminos"
[ "$(git rev-parse HEAD)" = "$expected_head" ]
[ -z "$(git status --porcelain)" ]
git fetch origin staging
git merge-base --is-ancestor FETCH_HEAD HEAD
git push --force-with-lease="refs/heads/$branch:29e26835047071022227968db964fdf2736b4bc0" origin "HEAD:refs/heads/$branch"
cd "$group/workspace"
[ -z "$(git status --porcelain)" ]
git push --set-upstream origin "HEAD:refs/heads/$branch"
cd "$group/vpsfree-dev-workspace"
[ -z "$(git status --porcelain)" ]
git push origin "HEAD:refs/heads/$branch"
