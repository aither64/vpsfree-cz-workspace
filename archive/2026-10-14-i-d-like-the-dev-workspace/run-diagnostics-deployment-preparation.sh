#!/usr/bin/env bash
# Build/copy only. Approval and owned queued activation are separate steps.
slug=2026-10-14-i-d-like-the-dev-workspace
record=/home/aither/workspace/ai/vpsfree.cz/work/$slug
for kind in machine profile; do
  for suffix in prepared.json prepare.log prepare.status; do
    test ! -e "$record/$kind-diagnostics-$suffix" || exit 2
  done
done
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/$slug/vpsfree-cz-configuration || exit 2
source "$record/config-dev-env.sh" || exit $?
set -u
for kind in machine profile; do
  if test "$kind" = machine; then request=machine_activate; else request=profile_activate; fi
  dev-session coordination prepare "$slug" --as-is --request "$record/$request-diagnostics-prepare-request.json" --json > "$record/$kind-diagnostics-prepared.json" 2> "$record/$kind-diagnostics-prepare.log"
  result=$?
  printf '%s\n' "$result" > "$record/$kind-diagnostics-prepare.status"
  if test "$result" -ne 0; then exit "$result"; fi
done
