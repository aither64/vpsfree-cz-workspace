#!/usr/bin/env bash
# Prepared single verification operation; lead must reconcile final review first.
set -eo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
checkout=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
revision=4ed9af55127743b7564cb4dd01d10c9f7fee5120
cd "$record"
test "$(dev-session current)" = 2026-10-14-i-d-like-the-dev-workspace
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-14-i-d-like-the-dev-workspace
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz
fi
test "$(git -C "$checkout" rev-parse HEAD)" = "$revision"
test -z "$(git -C "$checkout" status --porcelain)"
test -s "$record/delivery-feedback-refresh-review.md"
test -s "$record/delivery-feedback-refresh-review-dispositions.md"
test ! -e "$record/feedback-4ed-browser.log"
test ! -e "$record/feedback-4ed-browser.status"
source "$record/runtime-dev-env.sh"
cd "$checkout"
export GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-portal-go-cache GOPROXY=off
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
started=$(date --iso-8601=seconds)
set +e
PORTAL_BROWSER_TEST=1 go -C "$checkout/portal" test -mod=readonly -count=1 -v ./internal/web -run '^TestNotificationsBrowser$' > "$record/feedback-4ed-browser.log" 2>&1
result=$?
set -e
finished=$(date --iso-8601=seconds)
printf 'revision=%s\nstarted=%s\nfinished=%s\nexit_status=%s\n' "$revision" "$started" "$finished" "$result" > "$record/feedback-4ed-browser.status"
printf 'Browser fixture exit=%s revision=%s\n' "$result" "$revision"
exit "$result"
