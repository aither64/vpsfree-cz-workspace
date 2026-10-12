#!/usr/bin/env bash
set -euo pipefail

cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-route-aitherdev-alerts/vpsfree-cz-configuration
test "$(git rev-parse HEAD)" = b17dbea2cb1b9bf93714c929da776a4d4a6618f8
test -z "$(git status --porcelain)"

nix develop --no-write-lock-file -c bash -c '
  set -euo pipefail
  nix build --no-write-lock-file --no-link .#checks.x86_64-linux.infra-monitoring-rules
  confctl build --yes "cz.vpsfree/containers/prg/int.alerts[12]"
'
