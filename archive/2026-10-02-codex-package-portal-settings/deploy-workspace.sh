#!/usr/bin/env bash
# Coordinator-authorized supported user-profile switch, never a manual relink.
set -euo pipefail
umask 077
baseline=${1:?private complete baseline manifest required}
attempt=${2:-initial}
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
consumer=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings/workspace
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin
export DEV_SESSION_SLUG=2026-10-02-codex-package-portal-settings
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
unset CODEX_HOME CODEX_SQLITE_HOME
case "$attempt" in
  initial)
    log="$tracking/workspace-switch.log"
    status="$tracking/workspace-switch.status"
    expected_profile=/nix/store/z20g487rcankkgaprsrdya5na079i1rl-dev-workspace-0.2.0
    ;;
  selected-forward-retry)
    log="$tracking/workspace-switch-retry.log"
    status="$tracking/workspace-switch-retry.status"
    expected_profile=/nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0
    ;;
  *) exit 64 ;;
esac
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
cd "$consumer"
test "$(dev-session current)" = "$DEV_SESSION_SLUG"
test "$(git rev-parse HEAD)" = c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee
test -z "$(git status --porcelain --untracked-files=no)"
test -f "$baseline" && test -O "$baseline"
case "$baseline" in /home/aither/.local/state/dev-workspaces/backups/2026-10-02-codex-package-portal-settings/online-*/complete.json) ;; *) exit 65 ;; esac
jq -e '.kind == "per-database-online-baseline" and .global_snapshot == false and (.files | length >= 3) and all(.files[]; .integrity == "ok") and .finished_at != null' "$baseline" >/dev/null
test "$(<"$tracking/system-switch.status")" = 0
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = "$expected_profile"
test "$(readlink -f "$tracking/candidate-workspace-package")" = /nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0
workspace-host switch --source "$consumer"
