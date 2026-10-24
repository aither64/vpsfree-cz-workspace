#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 965aadc51dfb4a7d838a401b20ecafa38c8a70db
test -z "$(git status --porcelain)"
test "$(dev-session current)" = 2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json
export PORTAL_BROWSER_TEST=1
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
test ! -e "$DEV_WORKSPACES_CODEX_PROVIDERS"
test -f "$NODE_PATH/@playwright/test/package.json"
test -x "$PLAYWRIGHT_BROWSERS_PATH/chromium-1217/chrome-linux64/chrome"
test -x "$PLAYWRIGHT_BROWSERS_PATH/firefox-1511/firefox/firefox"
python3 - <<'OVERLAY'
from pathlib import Path
import json
source=Path.cwd()/'portal/internal/web/static'
assets=Path('/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0')
files=list(assets.glob('review-*'))
if not files: raise SystemExit('Pinned review assets are unavailable')
Path('/tmp/portal-followup-imp3-browser-assets-overlay.json').write_text(json.dumps({'Replace':{str(source/file.name):str(file) for file in files}}))
OVERLAY
exec nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
  -overlay /tmp/portal-followup-imp3-browser-assets-overlay.json ./internal/web \
  -run '^TestQuestionBrowser$/(optional_questions_browser_test[.]cjs|recovery_display_browser_test[.]cjs|usability_browser_test[.]cjs)$' \
  -count=1 -timeout=10m -v
