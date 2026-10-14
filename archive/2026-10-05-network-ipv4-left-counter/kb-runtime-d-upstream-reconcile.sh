#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
old=9fe491218e35a3250f2a72c203c2cecc3cb7ae16
base=a2bbf2f1c588de7eec0d7d52580a89a9d4bef984
start=e3315a483f3d3536d492ecbe40f2655449cf630f
save="$tracking/kb-runtime-d-upstream-preservation"
test "$(git rev-parse HEAD)" = "$old"
test "$(git branch --show-current)" = 2026-10-05-network-ipv4-left-counter
test "$(git remote get-url origin)" = git@github.com:aither64/dev-workspace.git
test "$(git rev-parse origin/master)" = "$base"
test "$(git rev-list --count "$start..$old")" = 1
git diff --cached --quiet
sha256sum --check --quiet "$tracking/kb-runtime-d-go-final1-source.manifest"
sha256sum --check --quiet "$tracking/kb-runtime-d-go-final1-source.sha256"
git status --short > "$tracking/kb-runtime-d-upstream-pre-status"
cmp "$tracking/kb-runtime-d-upstream-pre-status" "$tracking/kb-runtime-d-go-final1-source.status"
test "$(git ls-remote origin refs/heads/master | cut -f1)" = "$base"
mkdir "$save"
git rev-parse HEAD origin/master > "$save/heads"
git status --short > "$save/status"
git diff --cached --binary --full-index > "$save/index.patch"
cp "$tracking/kb-runtime-d-go-final1-source.sha256" "$save/source.sha256"
git diff --binary --full-index HEAD -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go > "$save/local-quick1.patch"
git diff --binary --full-index "$base" -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go > "$save/residual-on-a2bb.patch"
sha256sum "$save/local-quick1.patch" "$save/residual-on-a2bb.patch" > "$save/patches.sha256"
sha256sum --check --quiet "$save/patches.sha256"
git apply --reverse --check "$save/local-quick1.patch"
GIT_INDEX_FILE="$save/verification.index" git read-tree "$base"
GIT_INDEX_FILE="$save/verification.index" git apply --cached --check "$save/residual-on-a2bb.patch"
GIT_INDEX_FILE="$save/verification.index" git apply --cached "$save/residual-on-a2bb.patch"
for path in portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go; do
  expected=$(sha256sum "$path" | cut -d' ' -f1)
  actual=$(GIT_INDEX_FILE="$save/verification.index" git show ":$path" | sha256sum | cut -d' ' -f1)
  test "$actual" = "$expected"
done
GIT_INDEX_FILE="$save/verification.index" git write-tree > "$save/reconstructed.tree"
git diff --cached --quiet
sha256sum --check --quiet "$save/source.sha256"
git restore --source="$old" --worktree -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go
test -z "$(git status --porcelain)"
git rebase --onto "$base" "$start"
test -z "$(git status --porcelain)"
git diff --exit-code "$base" -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go
git range-diff "$start..$old" "$base..HEAD" > "$save/lease.range-diff"
git rev-parse HEAD > "$save/rebased-lease.sha"
git log --format=fuller "$base..HEAD" > "$save/rebased-history"
cat "$save/lease.range-diff" "$save/rebased-lease.sha"
