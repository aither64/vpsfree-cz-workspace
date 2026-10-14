#!/usr/bin/env bash
set -euo pipefail
set -o noclobber
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ! -e "$tracking/legacy-network-client-runtime-operation.log" && ! -e "$tracking/legacy-network-client-runtime-operation.exit" ]]
set +e
bash "$tracking/legacy-network-client-runtime-checks.sh" >"$tracking/legacy-network-client-runtime-operation.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/legacy-network-client-runtime-operation.exit"
exit "$result"
