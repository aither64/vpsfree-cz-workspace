#!/usr/bin/env bash
set -euo pipefail
out=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/effective-mounts-quick
oldbase=4c25fa5f9d1dda58aa0d7019fe351356e6f66c05
newbase=7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8
[ "$(git rev-parse origin/staging)" = "$newbase" ]
[ -z "$(git status --porcelain)" ]
[ "$(git rev-parse HEAD)" = "$(cat "$out/committed-head")" ]
git branch backup/2026-10-15-config-imports-before-final-staging-rebase HEAD
git diff --binary "$oldbase..HEAD" > "$out/feature-before-rebase.diff"
git rebase --onto "$newbase" "$oldbase"
git diff --binary "$newbase..HEAD" > "$out/feature-after-rebase.diff"
cmp "$out/feature-before-rebase.diff" "$out/feature-after-rebase.diff"
git range-diff "$oldbase..backup/2026-10-15-config-imports-before-final-staging-rebase" "$newbase..HEAD" > "$out/rebase-range-diff.txt"
[ -z "$(git status --porcelain)" ]
git rev-parse HEAD > "$out/final-head"
git rev-parse 'HEAD^{tree}' > "$out/final-tree"
git log --format=fuller "$newbase..HEAD" > "$out/final-history.txt"
