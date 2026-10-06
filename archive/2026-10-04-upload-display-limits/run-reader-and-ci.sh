#!/usr/bin/env bash
set -eu
root=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-04-upload-display-limits
records="$root/work/$slug"
cd "$root/worktrees/$slug/dev-workspace"
test "$(git rev-parse HEAD)" = 3edc605d81a30a4d49560426e0128b388b856493
nix shell --inputs-from . nixpkgs#go nixpkgs#gcc nixpkgs#nodejs -c bash \
 "$records/older-reader-experiment/run.sh" \
 3edc605d81a30a4d49560426e0128b388b856493 > "$records/older-reader.log" 2>&1
nix shell --inputs-from . nixpkgs#gh -c gh run view 37231243553 \
 --repo aither64/dev-workspace \
 --json headSha,status,conclusion,url > "$records/runtime-ci-before.json"
nix shell --inputs-from . nixpkgs#gh -c gh run watch 37231243553 \
 --repo aither64/dev-workspace --exit-status --interval 30 > "$records/runtime-ci-watch.log" 2>&1
nix shell --inputs-from . nixpkgs#gh -c gh run view 37231243553 \
 --repo aither64/dev-workspace \
 --json headSha,status,conclusion,url > "$records/runtime-ci-final.json"
