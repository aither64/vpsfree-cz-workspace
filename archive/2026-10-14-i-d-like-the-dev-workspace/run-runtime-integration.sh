#!/usr/bin/env bash
set -euo pipefail
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/browser-verification-env.sh
export GOCACHE=/tmp/session-attention-go-build
export GOPROXY=off
export PORTAL_BROWSER_TEST=1
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace/portal
go test -mod=readonly ./internal/web -run '^TestNotificationsBrowser$' -v
cd ..
nix flake check --print-build-logs
