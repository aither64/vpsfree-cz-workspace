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
git push --force-with-lease="refs/heads/$branch:6abc650f378a8cd4cc8ef4ecc25d74929ab6e1ed" origin "HEAD:refs/heads/$branch"
