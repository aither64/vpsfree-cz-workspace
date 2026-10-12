#!/usr/bin/env bash
set -eu
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/vpsadmin
nix develop -c ./test-runner.sh test services-up
