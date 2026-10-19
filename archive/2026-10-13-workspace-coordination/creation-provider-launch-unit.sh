#!/usr/bin/env bash
set -euo pipefail
operation=$1
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination
case "$operation" in
  prepare) script=creation-provider-bootstrap-prepare.sh; unit=workspace-coordination-creation-bootstrap-prepare-20261013.service; log=creation-provider-bootstrap-prepare.log;;
  prepare-recovered) script=creation-provider-bootstrap-prepare.sh; unit=workspace-coordination-creation-bootstrap-prepare-recovered-20261014.service; log=creation-provider-bootstrap-prepare-recovered.log;;
  execute) script=creation-provider-bootstrap-execute.sh; unit=workspace-coordination-creation-bootstrap-execute-20261013.service; log=creation-provider-bootstrap-execution.log;;
  *) exit 2;;
esac
systemd-run --user --no-block --unit="$unit" --property=Type=oneshot --property=RemainAfterExit=yes --property="StandardOutput=append:$tracking/$log" --property="StandardError=append:$tracking/$log" --working-directory=/home/aither/workspace/ai/vpsfree.cz --setenv=DEV_SESSION_SLUG=2026-10-13-workspace-coordination --setenv=DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz /run/current-system/sw/bin/bash "$tracking/$script"
systemctl --user show "$unit" -p InvocationID --value > "$tracking/creation-provider-$operation-invocation"
