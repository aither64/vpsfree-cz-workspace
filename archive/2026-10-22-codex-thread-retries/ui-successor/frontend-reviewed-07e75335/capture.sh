#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace
test "$(git rev-parse HEAD)" = 07e753357f743e4ad6c7a8f4d225ae473ee8292f
test -z "$(git status --porcelain)"
export DEV_SESSION_SLUG=2026-10-22-codex-thread-retries
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
export PORTAL_BROWSER_TEST=1
export PORTAL_RETRY_SCREENSHOTS="${PORTAL_RETRY_SCREENSHOTS:-/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/ui-successor/screenshots}"
export TMPDIR=/tmp
nix develop --no-update-lock-file --command bash -c 'set -e; cd portal; go test -mod=readonly ./internal/web -run "^TestQuestionBrowser$/^(retry_activity_browser_test|composer_handoff_browser_test|required_question_keyboard_browser_test)[.]cjs$" -count=1 -v -timeout=360s'
