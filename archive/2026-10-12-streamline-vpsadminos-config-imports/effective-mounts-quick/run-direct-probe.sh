#!/usr/bin/env bash
set -u
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/effective-mounts-quick
nix eval --impure --json --file "$record/direct-probe.nix" > "$record/direct-probe.json" 2> "$record/direct-probe.log"
result=$?
printf '%s\n' "$result" > "$record/direct-probe.status"
exit "$result"
