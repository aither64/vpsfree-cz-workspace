#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
cd "$tracking"
result=0
{
  bash "$tracking/prepare-network-remediation-pins.sh" config 30603a832d2848207bd7319c79c6b0388bc8646a b3b756a7b45864459bd39481a0d5245886777660 &&
  bash "$tracking/prepare-network-remediation-pins.sh" kb 30603a832d2848207bd7319c79c6b0388bc8646a
} >"$tracking/remediation-pins2-wrapper.log" 2>&1 || result=$?
printf '%s\n' "$result" >"$tracking/remediation-pins2-wrapper.exit"
printf 'Pin batch exit %s\n' "$result"
exit "$result"
