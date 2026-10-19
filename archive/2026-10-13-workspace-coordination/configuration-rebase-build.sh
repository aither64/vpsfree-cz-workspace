#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
trap 'build_status=$?; printf "%s\n" "$build_status" > "$tracking/configuration-rebase-build.status"' EXIT
confctl build --yes cz.vpsfree/machines/aitherdev
