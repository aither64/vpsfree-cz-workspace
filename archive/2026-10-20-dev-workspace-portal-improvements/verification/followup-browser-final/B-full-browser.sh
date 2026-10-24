#!/usr/bin/env bash
set -euo pipefail
umask 077
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-browser-final
bash "$packet/guards.sh"
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export PORTAL_BROWSER_TEST=1
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
test ! -e "$DEV_WORKSPACES_CODEX_PROVIDERS"
test -f "$NODE_PATH/@playwright/test/package.json"
test -x "$PLAYWRIGHT_BROWSERS_PATH/chromium-1217/chrome-linux64/chrome"
test -x "$PLAYWRIGHT_BROWSERS_PATH/firefox-1511/firefox/firefox"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
python3 - <<'OVERLAY'
from pathlib import Path
import json
source=Path.cwd()/'portal/internal/web/static'
assets=Path('/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0')
files=list(assets.glob('review-*'))
if not files: raise SystemExit('Pinned review assets are unavailable')
Path('/tmp/portal-followup-browser-assets-overlay.json').write_text(json.dumps({'Replace':{str(source/f.name):str(f) for f in files}}))
OVERLAY
exec nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
 -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
 -run '^(TestQuestionBrowser|TestNewSessionSettingsBrowser|TestIndexRefreshPreservesSelection|TestArchiveFailurePage)$' \
 -count=1 -timeout=20m -v
