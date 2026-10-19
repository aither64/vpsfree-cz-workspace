#!/usr/bin/env bash
set -euo pipefail
umask 077
phase=$1
repository=$2
case "$repository" in dev-workspace|vpsfree-dev-workspace|vpsfree-cz-configuration|workspace) ;; *) exit 2;; esac
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
helper=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/workspace/bin/bootstrap-merge-2026-10-13
plan_path=${BOOTSTRAP_MERGE_PLAN:-$tracking/bootstrap-integration-plan.json}
prefix="$tracking/bootstrap-integration-$repository-$phase"
trap 'operation_status=$?; printf "%s\n" "$operation_status" > "$prefix.status.tmp"; mv "$prefix.status.tmp" "$prefix.status"' EXIT
case "$phase" in
  prepare)
    ruby "$helper" --plan "$plan_path" --request "$tracking/bootstrap-integration-$repository-preparation-request.json" --prepare > "$prefix.json.tmp"
    ;;
  execute)
    ruby "$helper" --plan "$plan_path" --request "$tracking/bootstrap-integration-$repository-prepare.json" > "$prefix.json.tmp"
    ;;
  *) exit 2;;
esac
mv "$prefix.json.tmp" "$prefix.json"
