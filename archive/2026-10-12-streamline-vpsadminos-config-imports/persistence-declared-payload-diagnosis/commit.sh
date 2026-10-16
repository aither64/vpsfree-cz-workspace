#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
unit="$record/persistence-declared-payload-diagnosis"
[ "$(cat "$unit/quick/source-wrapper.status")" = 0 ]
[ "$(cat "$unit/quick/source-checks.status")" = 0 ]
[ "$(cat "$unit/quick/eval.status")" = 0 ]
[ "$(cat "$unit/quick/ruby.status")" = 0 ]
[ "$(cat "$unit/quick/hooks.status")" = 0 ]
[ "$(git rev-parse HEAD)" = edb90d2fe2190d88d8b9d2d21bd0def79eedc898 ]
[ -z "$(git diff --cached --name-only)" ]
[ "$(git status --porcelain)" = ' M tests/suite/dist-config/nixos-persistence-upgrade.nix' ]
[ "$(sha256sum tests/suite/dist-config/nixos-persistence-upgrade.nix | cut -d ' ' -f 1)" = 685d34b22f83d2a354989c48927feb7f1ac722d15903d2f343021d24a700b3eb ]
[ -x "$(git rev-parse --git-path hooks/pre-commit)" ]
git branch backup/2026-10-15-config-imports-before-declared-payload HEAD
git add -- tests/suite/dist-config/nixos-persistence-upgrade.nix
git write-tree > "$unit/expected-tree"
message_file=$(mktemp)
trap 'rm -f "$message_file"' EXIT
cp "$unit/persistence-v10-message.txt" "$message_file"
git commit --amend -F "$message_file"
[ "$(git rev-parse 'HEAD^{tree}')" = "$(cat "$unit/expected-tree")" ]
[ "$(git rev-parse HEAD^)" = b2669ce00d440c1e05eb07b0e5bb4d201f3e5161 ]
[ -z "$(git status --porcelain)" ]
git rev-parse HEAD > "$unit/final-head"
git rev-parse 'HEAD^{tree}' > "$unit/final-tree"
git log --format=fuller 7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8..HEAD > "$unit/final-series.txt"
git diff 7fd09b9b1f87f0563d3ba0be47081bfe4342b9b8..HEAD > "$unit/final-complete.diff"
git diff edb90d2fe2190d88d8b9d2d21bd0def79eedc898..HEAD > "$unit/final-delta.diff"
