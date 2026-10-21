#!/usr/bin/env bash
set -euo pipefail
root=/home/aither/workspace/ai/vpsfree.cz
out="$root/work/2026-10-20-portal-citation-deployment"
ws="$root/worktrees/2026-10-20-portal-citation-deployment/workspace"
cfg="$root/worktrees/2026-10-20-portal-citation-deployment/vpsfree-cz-configuration"
export BUNDLE_PATH="$root/worktrees/2026-10-20-portal-citation-investigation/vpsfree-cz-configuration/.gems"
(
  cd "$ws"
  nix build --no-link --print-out-paths .#default > "$out/rebase-app-path.txt"
) > "$out/rebase-app-build.log" 2>&1 &
app_pid=$!
(
  cd "$cfg"
  nix develop --command confctl build cz.vpsfree/machines/aitherdev
  nix develop --command confctl deploy --copy-only --no-reboot --yes cz.vpsfree/machines/aitherdev
) > "$out/rebase-system-build.log" 2>&1 &
system_pid=$!
set +e
wait "$app_pid"; app_exit=$?
wait "$system_pid"; system_exit=$?
set -e
printf '{"applicationExit":%s,"systemExit":%s}\n' "$app_exit" "$system_exit" > "$out/rebase-build-result.json"
if ((app_exit || system_exit)); then exit 1; fi
