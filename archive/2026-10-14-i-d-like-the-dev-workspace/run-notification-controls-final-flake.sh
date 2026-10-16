#!/usr/bin/env bash
# One exact-source verification operation. No retries or deployment.
set -eo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
checkout=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
revision=6c7d3851b005b47357e43688efccddde56f4e53b
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace || exit 2
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz || exit 2
fi
test ! -e "$record/notification-controls-final-flake.log" && test ! -e "$record/notification-controls-final-flake.status" || exit 2
test "$(git -C "$checkout" rev-parse HEAD)" = "$revision" || exit 2
test -z "$(git -C "$checkout" status --porcelain)" || exit 2
test -s "$record/notification-controls-review.md" || exit 2
test -s "$record/notification-controls-review-dispositions.md" || exit 2
test -s "$record/notification-controls-final-browser.status" || exit 2
rg -q '^exit_status=0$' "$record/notification-controls-final-browser.status" || exit 2
python3 - <<'VERIFY_SOURCE_GATE'
import json, hashlib
from pathlib import Path
root=Path.cwd()
gate=json.loads((root/'notification-controls-source-gate.json').read_text())
assert gate['revision']=='6c7d3851b005b47357e43688efccddde56f4e53b' and gate['decision']=='accepted'
for name,digest in gate['artifacts'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest, name
VERIFY_SOURCE_GATE
source "$record/runtime-dev-env.sh"
started=$(date --iso-8601=seconds)
set +e
nix flake check --no-write-lock-file --print-build-logs "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=$revision" > "$record/notification-controls-final-flake.log" 2>&1
result=$?
set -e
finished=$(date --iso-8601=seconds)
printf 'revision=%s\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$revision" "$started" "$finished" "$result" > "$record/notification-controls-final-flake.status"
printf 'Full flake verification exit=%s revision=%s\n' "$result" "$revision"
exit "$result"
