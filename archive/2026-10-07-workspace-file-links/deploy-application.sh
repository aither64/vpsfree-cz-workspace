#!/run/current-system/sw/bin/bash
set -euo pipefail
export PATH=/nix/store/q9wb526c4vn8mz2sh24hpfxha83vqbsf-git-2.54.0/bin:/home/aither/bin:/run/current-system/sw/bin:/nix/var/nix/profiles/default/bin:/usr/bin:/bin
task_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-workspace-file-links
exec >"$task_record/application-deploy.log" 2>&1
trap 'deploy_status=$?; printf "%s\n" "$deploy_status" >"$task_record/application-deploy.exit.tmp"; mv "$task_record/application-deploy.exit.tmp" "$task_record/application-deploy.exit"' EXIT
export DEV_SESSION_SLUG=2026-10-07-workspace-file-links
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
cd /home/aither/workspace/ai/vpsfree.cz
test "$(dev-session current)" = "$DEV_SESSION_SLUG"
test "$(cat "$task_record/host-deploy.exit")" = 0
test "$(readlink -f /run/current-system)" = "$(cat "$task_record/posthost-system.txt")"
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = /nix/store/b2q12p1725bqrb4nrd6yfjg28hgsggcf-dev-workspace-0.2.0
test "$(git -C worktrees/2026-10-07-workspace-file-links/workspace rev-parse HEAD)" = 70035dfe565058054e30efe2562c655c80dd183c
test "$(cat "$task_record/composed-check-9e8e6e8.exit")" = 0
test "$(cat "$task_record/runtime-check-9e8e6e8.exit")" = 0
test "$(cat "$task_record/ci-9e8e6e8.exit")" = 0
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-workspace-file-links/workspace
