#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
repo=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/dev-workspace
prefix=kb-runtime-d-go-quick1
verify() {
  test "$(git -C "$repo" rev-parse HEAD)" = 9fe491218e35a3250f2a72c203c2cecc3cb7ae16
  sha256sum --check "$tracking/$prefix-source.sha256"
  diff -u "$tracking/$prefix-source.diff" <(git -C "$repo" diff --binary -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go)
  diff -u "$tracking/$prefix-source.index" <(git -C "$repo" diff --cached --binary)
  diff -u "$tracking/$prefix-source.status" <(git -C "$repo" status --porcelain=v1 --untracked-files=all)
}
run() {
  local name=$1; shift
  set +e
  (cd "$repo"; "$@") >"$tracking/$prefix-$name.log" 2>&1
  local result=$?
  set -e
  printf '%s\n' "$result" >"$tracking/$prefix-$name.exit"
  cat "$tracking/$prefix-$name.log"
  return "$result"
}
verify
export TMPDIR=/tmp
run toolchain bash -ec 'test "$(readlink -f "$(command -v gofmt)")" = /nix/store/3yh8g6m3balbhzxsx77jlyyx443bxqii-go-1.26.6/share/go/bin/gofmt; go version; go env GOROOT; go env GOMODCACHE'
run formatting bash -ec 'test -z "$(gofmt -l portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go)"; git diff --check -- portal/internal/web/operation_state.go portal/internal/web/operation_state_test.go'
run focused go -C portal test -mod=readonly ./internal/web -json -count=1 -timeout=5m -run '^(TestLifecycleFreshOwnerReconciliation.*|Test(Archive|Delete)JournalRetryRefusesASameKindReplacementWhileWaitingForTheLock|TestLifecycleRetryCompareAndSwapRejectsAReplacementReceipt|TestLifecycleReconciliationCannotOverwriteRetryOrResurrectDismissedReceipt|TestLifecycleTargetAttemptRejectsLateResultWithTheSameReceipt|TestLifecycleSnapshotGETDoesNotWaitForGenerationOrReceiptMutex|TestDisplayGenerationContentionKeepsReceiptUnchanged)$'
run web go -C portal test -mod=readonly ./internal/web -json -count=1 -timeout=5m
verify
