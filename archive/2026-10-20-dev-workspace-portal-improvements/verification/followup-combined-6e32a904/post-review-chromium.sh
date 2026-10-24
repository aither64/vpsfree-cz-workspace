#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 0ba320a5a7bba9234f4d713bf8e142fe10f000b4
test -z "$(git status --porcelain)"
test ! -e /tmp/portal-followup-absent-providers.json
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json
export PORTAL_BROWSER_TEST=1
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
test -f "$NODE_PATH/@playwright/test/package.json"
test -x "$PLAYWRIGHT_BROWSERS_PATH/chromium-1217/chrome-linux64/chrome"
python3 - <<'PYOVERLAY'
from pathlib import Path
import json
source=Path.cwd()/'portal/internal/web/static'
assets=Path('/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0')
files=list(assets.glob('review-*'))
assert files, 'review assets unavailable'
Path('/tmp/portal-followup-browser-assets-overlay.json').write_text(json.dumps({'Replace':{str(source/file.name):str(file) for file in files}}))
PYOVERLAY
exec nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
 -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
 -run '^TestQuestionBrowser$/^portal_improvements_browser_test[.]cjs$' -count=1 -v
