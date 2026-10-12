#!/usr/bin/env bash
set -eu
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-11-diagnose-vpsadmin-api-exception/vpsfree-cz-configuration
nix develop -c bash -c 'set -e; confctl ls "cz.vpsfree/vpsadmin/int.api*"; confctl build --yes "cz.vpsfree/vpsadmin/int.api*"'
