#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
test "$(git rev-parse HEAD)" = 9b5bb4d61413e1de7702f45b50ef3229d2b93244
test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
cmp "$tracking/kb-runtime-generic-eof-final-staged.diff" <(git diff --cached --binary)
sha256sum --check --quiet "$tracking/kb-runtime-generic-eof-quick4-source.sha256"
for suffix in exit toolchain.exit syntax.exit commands.exit; do
  name="$tracking/kb-runtime-generic-eof-quick4-$suffix"
  test "$suffix" != exit || name="$tracking/kb-runtime-generic-eof-quick4.exit"
  test "$(cat "$name")" = 0
done
set -o noclobber
git write-tree > "$tracking/kb-runtime-generic-eof-final.tree"
git commit --amend -F "$tracking/kb-runtime-generic-eof-final.message"
git rev-parse HEAD > "$tracking/kb-runtime-generic-eof-final.sha"
test "$(git rev-parse HEAD^{tree})" = "$(cat "$tracking/kb-runtime-generic-eof-final.tree")"
test -z "$(git status --porcelain=v1)"
test "$(git rev-list --count e3315a483f3d3536d492ecbe40f2655449cf630f..HEAD)" = 1
git log --format=fuller e3315a483f3d3536d492ecbe40f2655449cf630f..HEAD > "$tracking/kb-runtime-generic-eof-final.history"
git diff --binary e3315a483f3d3536d492ecbe40f2655449cf630f..HEAD > "$tracking/kb-runtime-generic-eof-final.diff"
