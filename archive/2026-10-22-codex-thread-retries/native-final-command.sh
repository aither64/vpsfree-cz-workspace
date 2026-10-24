#!/usr/bin/env bash
set -u
umask 077

# Lead supplies immutable reviewed heads and a new run directory in the packet.
if [ "$#" -ne 3 ]; then
  exit 90
fi
retry_a_head=$1
retry_b_head=$2
retry_batch=$3
retry_tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries
retry_group=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries
retry_a="$retry_group/codex-web"
retry_b="$retry_group/dev-workspace"
retry_native=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex
retry_underlying=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/libexec/codex/bin/codex

[[ "$retry_a_head" =~ ^[0-9a-f]{40}$ ]] || exit 90
[[ "$retry_b_head" =~ ^[0-9a-f]{40}$ ]] || exit 90
[[ "$retry_batch" == "$retry_tracking"/native-verification/run-4-* ]] || exit 90
[[ "$retry_batch" != *..* ]] || exit 90
cd "$retry_tracking" || exit 90
retry_current=$(dev-session current) || exit 90
[ "$retry_current" = 2026-10-22-codex-thread-retries ] || exit 90
if [ -n "${DEV_SESSION_SLUG+x}${DEV_SESSION_WORKSPACE+x}" ]; then
  [ "${DEV_SESSION_SLUG-}" = 2026-10-22-codex-thread-retries ] || exit 90
  [ "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz ] || exit 90
fi

# The watcher may already own logs in batch; evidence is created only once.
mkdir -p "$retry_batch" || exit 90
mkdir "$retry_batch/evidence" || exit 90
retry_evidence="$retry_batch/evidence"
printf '%s\n' "$retry_current" > "$retry_evidence/session.txt"
for retry_source in "$retry_a" "$retry_b"; do
  retry_name=${retry_source##*/}
  git -C "$retry_source" rev-parse HEAD > "$retry_evidence/$retry_name.head" || exit 91
  git -C "$retry_source" rev-parse 'HEAD^{tree}' > "$retry_evidence/$retry_name.tree" || exit 91
  git -C "$retry_source" status --porcelain > "$retry_evidence/$retry_name.status" || exit 91
  [ ! -s "$retry_evidence/$retry_name.status" ] || exit 91
done
[ "$(cat "$retry_evidence/codex-web.head")" = "$retry_a_head" ] || exit 91
[ "$(cat "$retry_evidence/dev-workspace.head")" = "$retry_b_head" ] || exit 91
"$retry_native" --version > "$retry_evidence/binary-identity.txt" || exit 92
sha256sum "$retry_native" "$retry_underlying" >> "$retry_evidence/binary-identity.txt" || exit 92
[ "$(sha256sum "$retry_native" | cut -d ' ' -f 1)" = dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b ] || exit 92
[ "$(sha256sum "$retry_underlying" | cut -d ' ' -f 1)" = 5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5 ] || exit 92
nix --version > "$retry_evidence/nix-version.txt" || exit 92

retry_run() {
  local retry_label=$1
  local retry_cwd=$2
  shift 2
  cd "$retry_cwd" || return 90
  pwd > "$retry_evidence/$retry_label.cwd"
  local retry_started
  local retry_ended
  local retry_result
  retry_started=$(python3 -c 'import time; print(time.monotonic_ns())')
  TMPDIR=/tmp nix develop "$retry_b" -c "$@" > "$retry_evidence/$retry_label.jsonl" 2> "$retry_evidence/$retry_label.stderr"
  retry_result=$?
  retry_ended=$(python3 -c 'import time; print(time.monotonic_ns())')
  printf '%s\n' "$retry_result" > "$retry_evidence/$retry_label.exit"
  python3 -c 'import sys; print((int(sys.argv[2])-int(sys.argv[1]))/1e9)' "$retry_started" "$retry_ended" > "$retry_evidence/$retry_label.elapsed"
  return "$retry_result"
}

retry_run library "$retry_a" env CODEX_WEB_TEST_BINARY="$retry_native" go test -mod=readonly ./codex -run '^TestPinnedCodex(RecoveryRemainsColdUntilActivation|FailedTurnRetryContract)$' -count=1 -json -timeout=5m
retry_library_exit=$?
retry_run runtime "$retry_b/portal" env LIVE_SWITCH_CODEX="$retry_native" go test -mod=readonly -tags=live_switch_integration ./cmd/workspace-portal -run '^TestNative(LiveSwitchReconnect|TurnRetryController)$' -count=1 -json -timeout=5m
retry_runtime_exit=$?
printf '%s\n' "$retry_library_exit" > "$retry_evidence/library.command-exit"
printf '%s\n' "$retry_runtime_exit" > "$retry_evidence/runtime.command-exit"
if [ "$retry_library_exit" -ne 0 ] || [ "$retry_runtime_exit" -ne 0 ]; then
  exit 1
fi
exit 0
