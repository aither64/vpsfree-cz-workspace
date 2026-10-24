#!/usr/bin/env bash
# PREPARED ONLY. Launch once after explicit lead release and utility-slot release.
set -euo pipefail
proof_dir=$(cd -- "$(dirname -- "$0")" && pwd)
mkdir -p "$proof_dir/runs"
run_dir=$(mktemp -d "$proof_dir/runs/ordinary.XXXXXX")
printf '%s\n' "$run_dir" > "$proof_dir/latest-run"
phase=preflight
trap 'status=$?; printf "%s\n" "$status" > "$run_dir/exit-status"; printf "phase=%s\nexit=%s\n" "$phase" "$status" > "$run_dir/operation-result.txt"' EXIT
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async
{
  date -u +%FT%TZ
  test "$(dev-session current)" = 2026-10-19-haveapi-async-client
  test "$(git rev-parse HEAD)" = 8772bab21cd8739bf4672cdf4976aea2a6e59de3
  test -z "$(git status --porcelain=v1)"
  test -z "${VITE_RUNTIME_MODE:-}"
  test -z "${E2E_CHROMIUM_EXECUTABLE_PATH:-}"
  test -z "${E2E_STORAGE_STATE:-}"
  git rev-parse HEAD HEAD^{tree}
  sha256sum --check <<'HASHES'
482f447856e2a9b825be4f615f6b4434ef331da737a68b862c74da8e858889a8  package.json
0f1d21926f6d3a00527bcd486b7f3dae50134ca1e5316b990e3538e3c99b1a87  package-lock.json
ee39bc924bc3d1bd895626c2910f1292d109bbfeeb5abd113acb45e1951cc942  node_modules/playwright-core/browsers.json
HASHES
  test -x /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers/chromium_headless_shell-1228/chrome-headless-shell-linux64/chrome-headless-shell
} > "$run_dir/preflight.log" 2>&1
phase=browser
set +e
nix develop --command env \
  CI=1 \
  PLAYWRIGHT_BROWSERS_PATH=/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers \
  E2E_START_SERVER=1 E2E_BASE_URL=http://127.0.0.1:5173 \
  E2E_AUTO_SYSTEM_CHROMIUM=0 E2E_RELAX_CHROMIUM_POLICY=0 E2E_NO_ARTIFACTS=0 E2E_RECORD_ARTIFACTS=1 \
  PLAYWRIGHT_HTML_OPEN=never PLAYWRIGHT_HTML_OUTPUT_DIR="$run_dir/html" \
  PLAYWRIGHT_JSON_OUTPUT_FILE="$run_dir/result.json" \
  node scripts/playwright.mjs test \
  e2e/specs/public/overview.spec.ts \
  e2e/specs/public/news_compact.spec.ts \
  e2e/specs/app/authenticated_home_smoke.spec.ts \
  e2e/specs/app/session_expiry_redirect.spec.ts \
  e2e/specs/app/header_session_limit.spec.ts \
  e2e/specs/app/vps_create_failures.spec.ts \
  e2e/specs/app/vps_create_admin_flow.spec.ts \
  e2e/specs/app/blocking_action_progress_modal.spec.ts \
  e2e/specs/app/action_state_detail_page.spec.ts \
  --project=chromium --workers=2 --retries=0 --max-failures=1 \
  --trace=retain-on-failure --output="$run_dir/test-results" --reporter=line,json,html \
  > "$run_dir/verification.log" 2>&1
browser_status=$?
set -e
printf '%s\n' "$browser_status" > "$run_dir/browser-exit-status"
phase=postflight
set +e
{
  date -u +%FT%TZ
  git rev-parse HEAD HEAD^{tree}
  git status --porcelain=v1
  sha256sum package.json package-lock.json node_modules/playwright-core/browsers.json
} > "$run_dir/final-status.txt" 2>&1
metadata_status=$?
set -e
# Preserve the test's failure status even if a subsequent integrity check fails.
if [ "$browser_status" -ne 0 ]; then
  phase=browser-failed
  exit "$browser_status"
fi
if [ "$metadata_status" -ne 0 ]; then exit "$metadata_status"; fi
test "$(git rev-parse HEAD)" = 8772bab21cd8739bf4672cdf4976aea2a6e59de3
test -z "$(git status --porcelain=v1)"
sha256sum --check > "$run_dir/postflight.log" 2>&1 <<'HASHES'
482f447856e2a9b825be4f615f6b4434ef331da737a68b862c74da8e858889a8  package.json
0f1d21926f6d3a00527bcd486b7f3dae50134ca1e5316b990e3538e3c99b1a87  package-lock.json
ee39bc924bc3d1bd895626c2910f1292d109bbfeeb5abd113acb45e1951cc942  node_modules/playwright-core/browsers.json
HASHES
phase=complete
