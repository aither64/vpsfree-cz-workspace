#!/usr/bin/env bash
# PREPARED ONLY. Lead acceptance and fresh watcher own this one diagnostic run.
set -eo pipefail
umask 077
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
bundle="$record/notification-controls-browser-diagnostic-55af7283"
checkout=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
revision=55af728332471ef16a9587723c6964c563227748
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz
fi
test "$(git -C "$checkout" rev-parse HEAD)" = "$revision"
test -z "$(git -C "$checkout" status --porcelain)"
test -z "${NODE_OPTIONS-}"
test -z "${NOTIFICATION_FIXTURE_DIAGNOSTIC-}"
test ! -e "$bundle/run"
python3 - "$bundle" <<'VERIFY'
import hashlib,json,sys
from pathlib import Path
bundle=Path(sys.argv[1]);record=bundle.parent
for name,digest in json.loads((bundle/'manifest.json').read_text()).items():
    assert hashlib.sha256((bundle/name).read_bytes()).hexdigest()==digest
inputs=json.loads((bundle/'preserved-inputs.json').read_text())
for name in ['notification-controls-55af-browser.log','notification-controls-55af-browser.status']:
    assert hashlib.sha256((record/name).read_bytes()).hexdigest()==inputs[name]
gate=json.loads((record/'notification-controls-55af-source-gate.json').read_text())
assert gate['revision']=='55af728332471ef16a9587723c6964c563227748' and gate['decision']=='accepted'
for name,digest in gate['artifacts'].items():
    assert hashlib.sha256((record/name).read_bytes()).hexdigest()==digest
VERIFY
source "$record/runtime-dev-env.sh"
export GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-portal-go-cache GOPROXY=off
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
mkdir "$bundle/run"
started=$(date --iso-8601=seconds)
set +e
NOTIFICATION_FIXTURE_DIAGNOSTIC=1 NODE_OPTIONS="--require=$bundle/preload.cjs" PORTAL_BROWSER_TEST=1 \
  go -C "$checkout/portal" test -mod=readonly -count=1 -v ./internal/web -run '^TestNotificationsBrowser$' \
  > "$bundle/run/browser.log" 2>&1
result=$?
set -e
finished=$(date --iso-8601=seconds)
printf 'revision=%s\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$revision" "$started" "$finished" "$result" > "$bundle/run/browser.status"
python3 "$bundle/summarize.py" "$bundle/run/browser.log" "$result" > "$bundle/run/summary.json"
printf 'Diagnostic fixture exit=%s; inspect bounded summary.json\n' "$result"
exit "$result"
