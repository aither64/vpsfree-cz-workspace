#!/usr/bin/env bash
set -uo pipefail
exec > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/host-dry-activate.log 2>&1
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/vpsfree-cz-configuration
finish() {
  printf '%s\n' "$1" > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/host-dry-activate.exit.tmp
  mv /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/host-dry-activate.exit.tmp /home/aither/workspace/ai/vpsfree.cz/work/2026-10-04-upload-display-limits/host-dry-activate.exit
  exit "$1"
}
test "$(git rev-parse HEAD)" = e179a58ee3f7ceb4cf0b253d368c8ad94967b2d5 || finish 90
test -z "$(git status --porcelain)" || finish 90
test "$(readlink -f /run/current-system)" = /nix/store/4wa4aiamhn1cm63j7gsaiqdqfn0f9ign-nixos-system-aitherdev-26.05.20261001.4feb8eb || finish 90
nix develop --command confctl deploy -y 'cz.vpsfree/machines/aitherdev' dry-activate
rc=$?
readlink -f /run/current-system
finish "$rc"
