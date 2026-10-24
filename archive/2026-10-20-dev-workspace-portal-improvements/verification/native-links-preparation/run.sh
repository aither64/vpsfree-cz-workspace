#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = db25364999aa4bf12b67506662a08e9e464bee33
test -z "$(git status --porcelain)"
test ! -e /tmp/portal-improvements-absent-provider-catalog.json
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export PORTAL_BROWSER_TEST=1
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-improvements-absent-provider-catalog.json
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
exec nix develop --command go -C portal test -mod=readonly -overlay /tmp/portal-improvements-native-links/overlay.json ./internal/web -run '^TestQuestionBrowser$' -count=1 -v
