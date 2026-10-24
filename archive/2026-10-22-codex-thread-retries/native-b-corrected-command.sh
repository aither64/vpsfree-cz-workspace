#!/usr/bin/env bash
set -u
umask 077
retry_batch=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/native-verification/run-3b-731bb742
mkdir -p "$retry_batch"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/portal || exit 90
pwd > "$retry_batch/cwd.txt"
git rev-parse HEAD > "$retry_batch/head.txt"
git rev-parse 'HEAD^{tree}' > "$retry_batch/tree.txt"
git status --porcelain > "$retry_batch/status.txt"
if [ "$(cat "$retry_batch/head.txt")" != 731bb742e07b4374cb8ee9a3a1379eb751cf44c4 ] || [ -s "$retry_batch/status.txt" ]; then
  exit 91
fi
/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex --version > "$retry_batch/binary-identity.txt"
sha256sum /nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex /nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/libexec/codex/bin/codex >> "$retry_batch/binary-identity.txt"
retry_started=$(date +%s%N)
TMPDIR=/tmp nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace -c env LIVE_SWITCH_CODEX=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex go test -mod=readonly -tags=live_switch_integration ./cmd/workspace-portal -run '^TestNative(LiveSwitchReconnect|TurnRetryController)$' -count=1 -json -timeout=5m > "$retry_batch/runtime.jsonl" 2> "$retry_batch/runtime.stderr"
retry_result=$?
retry_ended=$(date +%s%N)
printf '%s\n' "$retry_result" > "$retry_batch/runtime.exit"
python3 -c 'import sys; print((int(sys.argv[2])-int(sys.argv[1]))/1e9)' "$retry_started" "$retry_ended" > "$retry_batch/runtime.elapsed"
exit "$retry_result"
