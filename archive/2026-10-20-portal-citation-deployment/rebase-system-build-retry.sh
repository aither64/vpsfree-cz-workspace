#!/usr/bin/env bash
set -euo pipefail
root=/home/aither/workspace/ai/vpsfree.cz
out="$root/work/2026-10-20-portal-citation-deployment"
export BUNDLE_PATH="$root/worktrees/2026-10-20-portal-citation-investigation/vpsfree-cz-configuration/.gems"
(
  cd "$root/worktrees/2026-10-20-portal-citation-deployment/workspace"
  nix build --out-link "$out/rebased-app-root" --print-out-paths .#default > "$out/rebase-app-rooted-path.txt"
) > "$out/rebase-app-rooted-build.log" 2>&1 &
app_pid=$!
(
  cd "$root/worktrees/2026-10-20-portal-citation-deployment/vpsfree-cz-configuration"
  nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
  nix develop --command confctl deploy --copy-only --no-reboot --yes cz.vpsfree/machines/aitherdev
) > "$out/rebase-system-build-retry.log" 2>&1 &
system_pid=$!
set +e
wait "$app_pid"; app_exit=$?
wait "$system_pid"; system_exit=$?
set -e
printf '{"applicationExit":%s,"systemExit":%s}\n' "$app_exit" "$system_exit" > "$out/rebase-build-retry-result.json"
if ((app_exit || system_exit)); then exit 1; fi
