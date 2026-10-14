#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
[[ ! -e "$tracking/fixture-final-publication-pins.log" && ! -e "$tracking/fixture-final-publication-pins.exit" ]]
exec >"$tracking/fixture-final-publication-pins.log" 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/fixture-final-publication-pins.exit"' EXIT
for operation in publish-v publish-w cancel-v cancel-w config kb; do
  bash "$tracking/fixture-final-operations.sh" "$operation" be136b6c00f03b85b7a12cc57550b4a1394a94a7 e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
done
