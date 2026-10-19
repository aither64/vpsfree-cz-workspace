#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
export DEV_SESSION_SLUG=2026-10-13-workspace-coordination
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
trap 'build_status=$?; printf "%s\n" "$build_status" > "$tracking/creation-provider-system-build.status.tmp"; mv "$tracking/creation-provider-system-build.status.tmp" "$tracking/creation-provider-system-build.status"' EXIT
confctl build --yes cz.vpsfree/machines/aitherdev
