#!/usr/bin/env bash
# Launched by the coordinator only after verification and baseline gates.
set -euo pipefail
umask 077
mode=${1:?dry-activate or switch required}
baseline=${2:?private complete baseline manifest required}
case "$mode" in dry-activate|switch) ;; *) exit 64 ;; esac
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
configuration=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings/vpsfree-cz-configuration
export PATH=/home/aither/bin:/run/wrappers/bin:/home/aither/.nix-profile/bin:/nix/profile/bin:/home/aither/.local/state/nix/profile/bin:/etc/profiles/per-user/aither/bin:/nix/var/nix/profiles/default/bin:/run/current-system/sw/bin
export DEV_SESSION_SLUG=2026-10-02-codex-package-portal-settings
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
unset CODEX_HOME CODEX_SQLITE_HOME
log="$tracking/system-$mode.log"
status="$tracking/system-$mode.status"
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
cd "$configuration"
test "$(dev-session current)" = "$DEV_SESSION_SLUG"
test "$(git rev-parse HEAD)" = 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d
test -z "$(git status --porcelain --untracked-files=no)"
test -f "$baseline" && test -O "$baseline"
case "$baseline" in /home/aither/.local/state/dev-workspaces/backups/2026-10-02-codex-package-portal-settings/online-*/complete.json) ;; *) exit 65 ;; esac
jq -e '.kind == "per-database-online-baseline" and .global_snapshot == false and (.files | length >= 3) and all(.files[]; .integrity == "ok") and .finished_at != null' "$baseline" >/dev/null
test "$(readlink -f /run/current-system)" = /nix/store/cb7sziy9ijyf2sxw1ajdbjwrzj2ac591-nixos-system-aitherdev-26.05.20260928.7fc6f2c
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = /nix/store/z20g487rcankkgaprsrdya5na079i1rl-dev-workspace-0.2.0
if test "$mode" = switch; then test "$(<"$tracking/system-dry-activate.status")" = 0; fi
nix develop --command confctl deploy --yes --generation 2026-10-02--14-04-08 \
  cz.vpsfree/machines/aitherdev "$mode"
