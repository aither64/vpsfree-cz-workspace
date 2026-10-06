#!/usr/bin/env bash
# Continue after passed package, browser and protocol checks; no live state.
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
log="$tracking/verification-runtime-5.log"
status="$tracking/verification-runtime-5.status"
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
date -u
group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings
generic="$group/dev-workspace"
test "$(git -C "$generic" rev-parse HEAD)" = 40838aa28c8433e42a4a3fbed4586a3df0146de9
test "$(git -C "$group/workspace" rev-parse HEAD)" = c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee
test "$(git -C "$group/vpsfree-cz-configuration" rev-parse HEAD)" = 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d
candidate=$(readlink -f "$tracking/candidate-workspace-package")
test "$candidate" = /nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0
assembled=$(readlink -f "$candidate/libexec/codex")
cd "$generic/portal"
nix shell --inputs-from "$generic" nixpkgs#go nixpkgs#stdenv.cc^out nixpkgs#python3 -c \
  go build -o "$tracking/compat-probe" "$tracking/compat_probe.go"
nix shell --inputs-from "$generic" nixpkgs#python3 -c "$tracking/compat-probe" \
  /nix/store/4mxlhqv9angcqgjw4c067nfpjlxv3d4h-codex-0.159.2/bin/codex "$assembled/bin/codex"
# Host build and both-consumer daemon checks passed in separate operations.
date -u
