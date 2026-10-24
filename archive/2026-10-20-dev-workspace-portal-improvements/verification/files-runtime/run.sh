#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
expected_head=$1
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-runtime
test "$(dev-session current)" = 2026-10-20-dev-workspace-portal-improvements
test "${DEV_SESSION_SLUG:-2026-10-20-dev-workspace-portal-improvements}" = 2026-10-20-dev-workspace-portal-improvements
test "${DEV_SESSION_WORKSPACE:-/home/aither/workspace/ai/vpsfree.cz}" = /home/aither/workspace/ai/vpsfree.cz
test "$(git rev-parse HEAD)" = "$expected_head"
test -z "$(git status --porcelain)"
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json
test ! -e "$DEV_WORKSPACES_CODEX_PROVIDERS"
export PORTAL_BROWSER_TEST=1
unset PORTAL_FIREFOX_TABS_TEST PORTAL_FIREFOX_READ_BUDGET_TEST
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
test -f "$NODE_PATH/@playwright/test/package.json"
test -x "$PLAYWRIGHT_BROWSERS_PATH/chromium-1217/chrome-linux64/chrome"
python3 - <<'OVERLAY'
from pathlib import Path
import json
source=Path.cwd()/'portal/internal/web/static'
assets=Path('/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0')
files=list(assets.glob('review-*'))
assert len(files)==4
Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-runtime/review-overlay.json').write_text(json.dumps({'Replace':{str(source/file.name):str(file) for file in files}}))
OVERLAY
exec nix develop --no-update-lock-file -c bash "$packet/in-nix.sh"
