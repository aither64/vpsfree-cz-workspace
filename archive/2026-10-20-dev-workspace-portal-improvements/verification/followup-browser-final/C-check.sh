#!/usr/bin/env bash
set -euo pipefail
umask 077
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-browser-final
bash "$packet/guards.sh"
export DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
attribute=${1:?Supply one declared check attribute}
case "$attribute" in
  agent-instructions|deployment-contract|cluster-provider-composition) ;;
  *) exit 2 ;;
esac
operation="$packet/run"
test -d "$operation/roots"
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace
expression="(builtins.getFlake \"git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace?rev=48215f8c24f29358af338ac153d4ece88e1f4da2\").checks.x86_64-linux.$attribute"
receipt="$operation/C-$attribute"
nix-instantiate --expr "$expression" --add-root "$operation/roots/C-$attribute.drv" --indirect \
 > "$receipt-instantiate.stdout" 2> "$receipt-instantiate.log"
drv=$(readlink -f "$operation/roots/C-$attribute.drv")
nix derivation show "$drv" > "$receipt-derivation.json"
nix-store --query --outputs "$drv" > "$receipt-expected-outputs.txt"
nix-store --realise "$drv" --add-root "$operation/roots/C-$attribute.out" --indirect \
 > "$receipt-realise.stdout" 2> "$receipt-realise.log"
output=$(readlink -f "$operation/roots/C-$attribute.out")
test "$output" = "$(cat "$receipt-expected-outputs.txt")"
nix path-info --json "$output" > "$receipt-path-info.json"
python3 - "$drv" "$output" "$receipt-identity.json" <<'IDENTITY'
import json,sys
from pathlib import Path
Path(sys.argv[3]).write_text(json.dumps({'source':'48215f8c24f29358af338ac153d4ece88e1f4da2','drv':sys.argv[1],'output':sys.argv[2],'derivationAndOutputRooted':True},indent=2)+'\n')
print('Retained declared check derivation and output:',sys.argv[1],sys.argv[2])
IDENTITY
