#!/usr/bin/env bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
test "$(git rev-parse HEAD)" = 133d23f5d341808559b08a533409e748d6a400aa
test -z "$(git status --porcelain)"
test ! -e /tmp/portal-followup-absent-providers.json
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json
export PORTAL_FIREFOX_TABS_TEST=1
export FIREFOX_BINARY=/nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0/bin/firefox
export GECKODRIVER_BINARY=/nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0/bin/geckodriver
xvfb_run=/nix/store/iyzy0zy23i1njxar2sd1hr4hmk56dalh-xvfb-run-1+g87f6705/bin/xvfb-run
test -x "$FIREFOX_BINARY"
test -x "$GECKODRIVER_BINARY"
test -x "$xvfb_run"
exec nix develop --no-update-lock-file -c "$xvfb_run" --auto-servernum \
 --server-args='-screen 0 1920x1080x24 -nolisten tcp' \
 go -C portal test -mod=readonly ./internal/web -run '^TestFirefoxTabs$' -count=1 -v
