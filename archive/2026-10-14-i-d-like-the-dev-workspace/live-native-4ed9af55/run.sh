#!/usr/bin/env bash
set -eo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace
probe="$tracking/live-native-4ed9af55"
cd "$tracking"
if [[ "$(dev-session current)" != 2026-10-14-i-d-like-the-dev-workspace ]]; then
  printf '%s\n' 'Refusing live acceptance: session identity mismatch.' >&2
  exit 2
fi
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  if [[ "${DEV_SESSION_SLUG-}" != 2026-10-14-i-d-like-the-dev-workspace || "${DEV_SESSION_WORKSPACE-}" != /home/aither/workspace/ai/vpsfree.cz ]]; then
    printf '%s\n' 'Refusing live acceptance: environment identity mismatch.' >&2
    exit 2
  fi
fi
source "$tracking/runtime-dev-env.sh"
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
unset DEBUG PWDEBUG NODE_DEBUG
cd "$probe"
sha256sum --quiet -c harness-sha256.txt
node --check live-check.cjs
if ! mkdir run; then
  printf '%s\n' 'Refusing to overwrite or repeat the live acceptance run.' >&2
  exit 2
fi
export LIVE_NOTIFICATION_RESULT="$probe/run/results.json"
exec python3 "$probe/run_live.py" "$tracking/xvfb-path.txt" "$probe/run" "$probe"
