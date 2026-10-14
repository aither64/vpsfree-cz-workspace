#!/usr/bin/env bash
set -euo pipefail
umask 077
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ! -e "$tracking/visibility-final-runtime-operation.log" && ! -e "$tracking/visibility-final-runtime-operation.exit" ]]
set +e
bash "$tracking/visibility-final-runtime-checks.sh" >"$tracking/visibility-final-runtime-operation.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" >"$tracking/visibility-final-runtime-operation.exit"
exit "$result"
