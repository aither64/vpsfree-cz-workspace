#!/usr/bin/env bash
# Isolated normal daemon startup for both consumers; no live state or model turn.
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-codex-package-portal-settings
generic=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings/dev-workspace
log="$tracking/verification-daemon-1.log"
status="$tracking/verification-daemon-1.status"
test ! -e "$log" && test ! -e "$status"
exec >"$log" 2>&1
trap 'result=$?; printf "%s\n" "$result" > "$status.tmp"; mv "$status.tmp" "$status"' EXIT
date -u
test "$(git -C "$generic" rev-parse HEAD)" = 40838aa28c8433e42a4a3fbed4586a3df0146de9
test "$(readlink -f "$tracking/candidate-workspace-package")" = /nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0
nix shell --inputs-from "$generic" nixpkgs#python3 -c python3 "$tracking/daemon_probe.py" \
  /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex
nix shell --inputs-from "$generic" nixpkgs#python3 -c python3 "$tracking/daemon_probe.py" \
  /nix/store/zg389q4q7hcxxl7agg0y5nxdb3xpcz4h-nixos-system-aitherdev-26.05.20261001.4feb8eb/sw/bin/codex
date -u
