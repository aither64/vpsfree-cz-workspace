#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
exec >"$tracking/post-review-batch1.log" 2>&1
result=0
trap 'result=$?; printf "%s\n" "$result" >"$tracking/post-review-batch1.exit"' EXIT
for mode in sql-admission react-desktop react-mobile react-build; do
  bash "$tracking/run-network-post-review-check.sh" "$mode" 30603a832d2848207bd7319c79c6b0388bc8646a b3b756a7b45864459bd39481a0d5245886777660 a6243f09265398368e07695dd531e4a0e312350b
done
