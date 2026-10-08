#!/run/current-system/sw/bin/bash
set -euo pipefail
export PATH=/nix/store/q9wb526c4vn8mz2sh24hpfxha83vqbsf-git-2.54.0/bin:/home/aither/bin:/run/current-system/sw/bin:/nix/var/nix/profiles/default/bin:/usr/bin:/bin
task_record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-workspace-file-links
exec >"$task_record/live-acceptance.log" 2>&1
trap 'check_status=$?; printf "%s\n" "$check_status" >"$task_record/live-acceptance.exit.tmp"; mv "$task_record/live-acceptance.exit.tmp" "$task_record/live-acceptance.exit"' EXIT
export DEV_SESSION_SLUG=2026-10-07-workspace-file-links
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
cd /home/aither/workspace/ai/vpsfree.cz
test "$(dev-session current)" = "$DEV_SESSION_SLUG"
test "$(cat "$task_record/application-deploy.exit")" = 0
test "$(readlink -f /run/current-system)" = "$(cat "$task_record/posthost-system.txt")"
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = /nix/store/y0j44svpcdpqzvjj43n5kg06iqfnxvzv-dev-workspace-0.2.0
test "$(git -C worktrees/2026-10-07-workspace-file-links/dev-workspace rev-parse HEAD)" = 9e8e6e87a5a4844d4639ddf4008de483d1897f4c
test "$(git -C worktrees/2026-10-07-workspace-file-links/workspace rev-parse HEAD)" = 70035dfe565058054e30efe2562c655c80dd183c
/nix/store/9r02ykx9y35lf4gk6gc30gnag1y8ncp7-python3-3.13.15/bin/python3.13 "$task_record/verify-live.py"
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node "$task_record/verify-live-browser.cjs"
