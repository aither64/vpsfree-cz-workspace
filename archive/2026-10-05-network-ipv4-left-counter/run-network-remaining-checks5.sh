#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ! -e "$tracking/post-review-remaining5.log" && ! -e "$tracking/post-review-remaining5.exit" ]]
exec >"$tracking/post-review-remaining5.log" 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/post-review-remaining5.exit"' EXIT
for mode in config-build; do
  [[ ! -e "$tracking/post-review4-$mode.log" && ! -e "$tracking/post-review4-$mode.exit" ]]
  bash "$tracking/run-network-post-review-check4.sh" "$mode" \
    be136b6c00f03b85b7a12cc57550b4a1394a94a7 \
    e4c49bcdc91b33b7f644a2f125231cb413cf4bf4 \
    dd10d88073da3aed6c4512e938abe4374422aab1
done
