#!/usr/bin/env bash
set -eo pipefail
umask 077

tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
probe="$tracking/push-provider-probe/diagnostic"
expected_slug=2026-10-14-i-d-like-the-dev-workspace
expected_workspace=/home/aither/workspace/ai/vpsfree.cz
cd "$tracking"
if [[ "$(dev-session current)" != "$expected_slug" ]]; then
  printf '%s\n' 'Refusing provider probe: session identity mismatch.' >&2
  exit 2
fi
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  if [[ "${DEV_SESSION_SLUG-}" != "$expected_slug" || "${DEV_SESSION_WORKSPACE-}" != "$expected_workspace" ]]; then
    printf '%s\n' 'Refusing provider probe: environment identity mismatch.' >&2
    exit 2
  fi
fi
source "$tracking/runtime-dev-env.sh"
export GOMODCACHE=/tmp/session-webpush-mod
export GOCACHE=/tmp/session-attention-go-build
export GOFLAGS=-mod=readonly
export GOPROXY=off
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/session-attention-no-provider-catalog
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
unset DEBUG PWDEBUG NODE_DEBUG
cd "$probe/source"
sha256sum --quiet -c "$probe/source-sha256.txt"
node --check portal/internal/web/notifications_browser_test.cjs
if ! mkdir "$probe/run"; then
  printf '%s\n' 'Refusing to overwrite or repeat the disposable provider probe.' >&2
  exit 2
fi
export PORTAL_PROVIDER_PROBE=1
export PROVIDER_PROBE_RESULT_FILE="$probe/run/results.json"
cd "$probe/source/portal"
date --iso-8601=seconds > "$probe/run/started-at"
set +e
go test -mod=readonly ./internal/web -run '^TestNotificationProviderProbe$' -count=1 -v > "$probe/run/go-test.log" 2>&1
probe_status=$?
set -e
printf '%s\n' "$probe_status" > "$probe/run/status"
date --iso-8601=seconds > "$probe/run/finished-at"
cat "$probe/run/go-test.log"
exit "$probe_status"
