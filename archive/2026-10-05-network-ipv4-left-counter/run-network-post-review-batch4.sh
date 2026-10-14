#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_sha=be136b6c00f03b85b7a12cc57550b4a1394a94a7
w_sha=e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
c_sha=$(cat "$tracking/fixture-final-pin-c-w.sha")
[[ $c_sha =~ ^[0-9a-f]{40}$ ]]
[[ ! -e "$tracking/post-review-batch4.log" && ! -e "$tracking/post-review-batch4.exit" ]]
exec >"$tracking/post-review-batch4.log" 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/post-review-batch4.exit"' EXIT
printf 'Selected V=%s W=%s C=%s\n' "$v_sha" "$w_sha" "$c_sha"
for mode in vm-routes vm-export vm-migration vm-restore legacy-admin-cluster config-build; do
  [[ ! -e "$tracking/post-review4-$mode.log" && ! -e "$tracking/post-review4-$mode.exit" ]]
  bash "$tracking/run-network-post-review-check4.sh" "$mode" "$v_sha" "$w_sha" "$c_sha"
done
