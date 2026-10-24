#!/usr/bin/env bash
set -euo pipefail
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-runtime
cd portal
go test -mod=readonly ./internal/web -run '^TestTrackingFilesArchiveRevive$' -count=1 -v > "$packet/lifecycle.log" 2>&1
go test -mod=readonly -overlay "$packet/review-overlay.json" ./internal/web -run '^TestQuestionBrowser$/^portal_improvements_browser_test[.]cjs$' -count=1 -v > "$packet/browser.log" 2>&1
