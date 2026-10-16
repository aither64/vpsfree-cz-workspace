#!/usr/bin/env bash
set -u
slug=2026-10-14-i-d-like-the-dev-workspace
record=/home/aither/workspace/ai/vpsfree.cz/work/$slug
cd /home/aither/workspace/ai/vpsfree.cz
for kind in machine profile; do
  if test "$kind" = machine; then request=machine_activate; else request=profile_activate; fi
  dev-session coordination prepare "$slug" --as-is --request "$record/$request-prepare-refresh-request.json" --json > "$record/$kind-prepared.json" 2> "$record/$kind-prepare.log"
  result=$?
  printf '%s\n' "$result" > "$record/$kind-prepare.status"
  if test "$result" -ne 0; then exit "$result"; fi
done
