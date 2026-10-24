#!/usr/bin/env bash
set -euo pipefail
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/targeted-read-budget-successor/guards.py
umask 077
# PREPARED ONLY. Lead launches a fresh Luna/low utility after final review.
root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/targeted-read-budget-successor
operation="$packet/packages-final"
selected=/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0
expected_drv=__FINAL_DERIVATION_PENDING__
expected_output=__FINAL_OUTPUT_PENDING__
cd "$root/workspace"
python3 - <<'GUARDS'
import os,subprocess
from pathlib import Path
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
slug=os.environ.get('DEV_SESSION_SLUG');workspace=os.environ.get('DEV_SESSION_WORKSPACE')
assert (slug is None and workspace is None) or (slug=='2026-10-20-dev-workspace-portal-improvements' and workspace=='/home/aither/workspace/ai/vpsfree.cz')
root=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
for name,head in {'workspace': '__FINAL_C_PENDING__', 'dev-workspace': '__FINAL_B_PENDING__', 'codex-web': 'ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5', 'vpsfree-cz-configuration': '__FINAL_CONFIG_PENDING__'}.items():
    assert subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip()==head,name
    assert not subprocess.check_output(['git','-C',str(root/name),'status','--porcelain']),name
assert Path('/home/aither/bin/workspace-host').resolve()==Path('/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0/bin/workspace-host')
print('Exact session, selected predecessor and clean final A/B/C/config verified')
GUARDS
test ! -e "$operation"
mkdir -p "$operation/roots"
stage() {
  local label=$1 source=$2 revision=$3 attribute=$4 drv package
  nix-instantiate --expr "(builtins.getFlake \"git+file://$root/$source?rev=$revision\").$attribute" \
    --add-root "$operation/roots/$label.drv" --indirect \
    > "$operation/$label-instantiate.stdout" 2> "$operation/$label-instantiate.log"
  drv=$(readlink -f "$operation/roots/$label.drv")
  if test "$label" = workspace; then test "$drv" = "$expected_drv"; fi
  nix-store --realise "$drv" --add-root "$operation/roots/$label" --indirect \
    > "$operation/$label.stdout" 2> "$operation/$label.log"
  package=$(readlink -f "$operation/roots/$label")
  test "$package" = "$(nix-store --query --outputs "$drv")"
  nix derivation show "$drv" > "$operation/$label-derivation-raw.json"
  python3 "$packet/normalize-derivation.py" "$operation/$label-derivation-raw.json" > "$operation/$label-derivation.json"
  nix path-info --json "$package" > "$operation/$label-path-info.json"
}
stage workspace workspace __FINAL_C_PENDING__ packages.x86_64-linux.default
candidate=$(readlink -f "$operation/roots/workspace")
test "$candidate" = "$expected_output"
python3 "$packet/metadata.py" "$candidate" > "$operation/metadata.log" 2>&1
"$candidate/bin/workspace-host" check-codex --codex "$candidate/libexec/codex/bin/codex" \
  > "$operation/codex.log" 2>&1
mkdir -p "$operation/disposable-registration/state" "$operation/disposable-registration/workspace"
for label in selected candidate; do
  if test "$label" = selected; then package=$selected; else package=$candidate; fi
  printf '{"schema":1}\n' | env -i PATH=/empty \
    "$package/bin/workspace-portal" agent-teams registration --package-root "$package" \
    --state-root "$operation/disposable-registration/state" \
    --workspace "$operation/disposable-registration/workspace" \
    > "$operation/$label-registration.json" 2> "$operation/$label-registration.log"
  python3 "$packet/registration.py" "$operation/$label-registration.json" "$package" \
    "$operation/disposable-registration/state" "$operation/disposable-registration/workspace" \
    > "$operation/$label-registration-assertions.log" 2>&1
done
stage deployment-contract workspace __FINAL_C_PENDING__ checks.x86_64-linux.deployment-contract
stage agent-instructions workspace __FINAL_C_PENDING__ checks.x86_64-linux.agent-instructions
stage cluster-provider-composition workspace __FINAL_C_PENDING__ checks.x86_64-linux.cluster-provider-composition
stage agent-team-policy workspace __FINAL_C_PENDING__ checks.x86_64-linux.agent-team-policy
stage runtime-generic-source dev-workspace __FINAL_B_PENDING__ checks.x86_64-linux.generic-source
stage shared-default codex-web ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 checks.x86_64-linux.default
stage shared-generic-source codex-web ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 checks.x86_64-linux.generic-source
printf '%s\n' 'PASS: exact sources, rooted outputs and derivations, capacity8, native Codex and reporting-only registration; no profile selection. Keep roots through activation.'
