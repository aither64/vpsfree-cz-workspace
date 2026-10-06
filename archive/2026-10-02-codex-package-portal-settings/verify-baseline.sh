#!/usr/bin/env bash
# Read-only SQLite online baseline before any candidate access to real state.
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
log="$tracking/sqlite-baseline-1.log"
status="$tracking/sqlite-baseline-1.status"
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
date -u
test "$(<"$tracking/verification-runtime-5.status")" = 0
test "$(<"$tracking/verification-daemon-1.status")" = 0
test "$(readlink -f /run/current-system)" = /nix/store/cb7sziy9ijyf2sxw1ajdbjwrzj2ac591-nixos-system-aitherdev-26.05.20260928.7fc6f2c
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = /nix/store/z20g487rcankkgaprsrdya5na079i1rl-dev-workspace-0.2.0
test -z "${CODEX_HOME:-}" && test -z "${CODEX_SQLITE_HOME:-}"
python3 "$tracking/sqlite_baseline.py" /home/aither/.codex \
  /home/aither/.local/state/dev-workspaces/backups/2026-10-02-codex-package-portal-settings
date -u
