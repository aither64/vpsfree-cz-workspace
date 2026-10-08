#!/run/current-system/sw/bin/bash
set -euo pipefail
export PATH=/nix/store/q9wb526c4vn8mz2sh24hpfxha83vqbsf-git-2.54.0/bin:/home/aither/bin:/run/current-system/sw/bin:/nix/var/nix/profiles/default/bin:/usr/bin:/bin
task_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-workspace-file-links
exec >"$task_record/host-deploy.log" 2>&1
trap 'deploy_status=$?; printf "%s\n" "$deploy_status" >"$task_record/host-deploy.exit.tmp"; mv "$task_record/host-deploy.exit.tmp" "$task_record/host-deploy.exit"' EXIT
export DEV_SESSION_SLUG=2026-10-07-workspace-file-links
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-workspace-file-links/vpsfree-cz-configuration
test "$(dev-session --workspace vpsfree-cz current)" = "$DEV_SESSION_SLUG"
test "$(git rev-parse HEAD)" = 5447020fccf99705e65a907cfe6e80684a5a1577
test "$(readlink -f /run/current-system)" = /nix/store/r3c1kcrjmqgq48vjsvkmz3nwkzj6hggy-nixos-system-aitherdev-26.05.20261006.b253099
test "$(cat "$task_record/host-build-9e8e6e8.exit")" = 0
test "$(cat "$task_record/runtime-check-9e8e6e8.exit")" = 0
test "$(cat "$task_record/composed-check-9e8e6e8.exit")" = 0
nix develop --command confctl deploy --yes --no-interactive --dry-activate-first cz.vpsfree/machines/aitherdev switch
