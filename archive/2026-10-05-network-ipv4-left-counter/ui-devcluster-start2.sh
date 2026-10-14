#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-05-network-ipv4-left-counter
export PATH=/home/aither/bin:$PATH
export DEV_SESSION_SLUG=$slug DEV_SESSION_WORKSPACE=$workspace
test "$(dev-session current)" = "$slug"
for suffix in exit private-log.path; do test ! -e "$tracking/ui-devcluster-start2.$suffix"; done
private=$(mktemp -d /tmp/vpsfree-network-ui-start.XXXXXXXX)
printf '%s\n' "$private/start.log" >"$tracking/ui-devcluster-start2.private-log.path"
trap 'result=$?; printf "%s\n" "$result" >"$tracking/ui-devcluster-start2.exit"' EXIT
cd "$workspace"
vpsadmin-devcluster start "$slug" --topology single --network bridge >"$private/start.log" 2>&1
