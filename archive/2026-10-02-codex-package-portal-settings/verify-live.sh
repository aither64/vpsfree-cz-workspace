#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
log="$tracking/verification-live-2.log"
status="$tracking/verification-live-2.status"
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
date -u
unset CODEX_HOME CODEX_SQLITE_HOME
test "$(<"$tracking/workspace-switch-retry.status")" = 0
test "$(<"$tracking/system-switch.status")" = 0
test "$(readlink -f /run/current-system)" = /nix/store/zg389q4q7hcxxl7agg0y5nxdb3xpcz4h-nixos-system-aitherdev-26.05.20261001.4feb8eb
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = /nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0
python3 "$tracking/live_cli_probe.py"
codex-ds --strict-config --help >/dev/null
workspace-host status
test ! -e /home/aither/.local/state/dev-workspaces/codex/pending
for unit in workspace-codex@vpsfree-cz.service workspace-portal@vpsfree-cz.service workspace-router.service; do
  test "$(systemctl --user show "$unit" --property=ActiveState --value)" = active
done
server_pid=$(systemctl --user show workspace-codex@vpsfree-cz.service --property=MainPID --value)
server_executable=$(readlink -f "/proc/$server_pid/exe")
test "$server_executable" = /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/libexec/codex/bin/codex
test "$("$server_executable" --version)" = 'codex-cli 0.160.0'
portal_pid=$(systemctl --user show workspace-portal@vpsfree-cz.service --property=MainPID --value)
test "$(readlink -f "/proc/$portal_pid/exe")" = /nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0/bin/workspace-portal
curl --fail --silent --show-error --max-time 15 --output /dev/null \
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-codex-package-portal-settings/
printf '%s\n' 'PASS: live workspace server 0.160.0, selected portal executable and stable session URL'
date -u
