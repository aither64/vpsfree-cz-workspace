#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
webui=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/vpsadmin-webui
[[ $(dev-session current) == 2026-10-05-network-ipv4-left-counter ]]
export DEV_SESSION_SLUG=2026-10-05-network-ipv4-left-counter
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
[[ $(git -C "$webui" rev-parse HEAD) == b3b756a7b45864459bd39481a0d5245886777660 ]]
[[ -z $(git -C "$webui" status --porcelain) ]]
exec >"$tracking/post-review-react-batch1.log" 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/post-review-react-batch1.exit"' EXIT
run_step() {
  local name=$1 result=0
  shift
  (cd "$webui" && "$@") >"$tracking/post-review-$name.log" 2>&1 || result=$?
  printf '%s\n' "$result" >"$tracking/post-review-$name.exit"
  printf '%s: exit %s\n' "$name" "$result"
  return "$result"
}
run_step react-desktop nix develop --command env CI=1 E2E_BASE_URL=http://127.0.0.1:15173 E2E_START_SERVER=1 E2E_RECORD_ARTIFACTS=1 node scripts/playwright.mjs test e2e/specs/admin/network_availability.spec.ts --project=chromium --workers=1 --retries=0 --reporter=line --output="$tracking/post-review-react-desktop-results"
run_step react-mobile nix develop --command env CI=1 E2E_BASE_URL=http://127.0.0.1:15173 E2E_START_SERVER=1 E2E_RECORD_ARTIFACTS=1 node scripts/playwright.mjs test e2e/specs/admin/network_availability.spec.ts --project=mobile-chrome --workers=1 --retries=0 --reporter=line --output="$tracking/post-review-react-mobile-results"
run_step react-build nix develop --command npm run build -- --outDir "$tracking/post-review-react-dist"
