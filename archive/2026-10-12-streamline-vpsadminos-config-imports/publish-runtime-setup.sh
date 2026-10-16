#!/usr/bin/env bash
set -eu
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
product=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
branch=2026-10-12-streamline-vpsadminos-config-imports
expected_head=$(cat "$record/compatibility-final-head")
[ "$(cat "$record/compatibility-review-runtime-clearance")" = "$expected_head" ]
cd "$product"
[ "$(git rev-parse HEAD)" = "$expected_head" ]
[ -z "$(git status --porcelain)" ]
git fetch origin staging
git merge-base --is-ancestor FETCH_HEAD HEAD
git push --force-with-lease="refs/heads/$branch:96b69056cb16017dfef2c9a73a1acc755c032b72" origin "HEAD:refs/heads/$branch"
