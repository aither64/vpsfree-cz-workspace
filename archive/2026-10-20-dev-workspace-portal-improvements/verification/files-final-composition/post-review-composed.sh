#!/usr/bin/env bash
set -euo pipefail
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-final-composition/guards.py
umask 077
# PREPARED ONLY. Lead launches a fresh Luna/low utility after final review.
root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-final-composition
operation="$packet/packages-final"
selected=/nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0
expected_drv=/nix/store/v466ppdwhax565z8a53z5zmx0yp1dl34-dev-workspace-0.2.0.drv
expected_output=/nix/store/m8bqmkdzgk85vng42hcsavqmaz56rwgc-dev-workspace-0.2.0
test "$expected_drv" != PENDING_EVALUATION
test "$expected_output" != PENDING_EVALUATION
cd "$root/workspace"
python3 - <<'GUARDS'
import os,subprocess
from pathlib import Path
assert subprocess.check_output(['dev-session','current'],text=True).strip()=='2026-10-20-dev-workspace-portal-improvements'
slug=os.environ.get('DEV_SESSION_SLUG');workspace=os.environ.get('DEV_SESSION_WORKSPACE')
assert (slug is None and workspace is None) or (slug=='2026-10-20-dev-workspace-portal-improvements' and workspace=='/home/aither/workspace/ai/vpsfree.cz')
root=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
for name,head in {'workspace': '12b4491bd6e5bfa6799e938fd555c8f15d588a1d', 'dev-workspace': '483d4e7eafeda974dfe19de45687795562072d7d', 'codex-web': 'ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5', 'vpsfree-cz-configuration': '354e944f9dcf071e4878f0a0bbf2e71f52693801'}.items():
    assert subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip()==head,name
    assert not subprocess.check_output(['git','-C',str(root/name),'status','--porcelain']),name
assert Path('/home/aither/bin/workspace-host').resolve()==Path('/nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0/bin/workspace-host')
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
stage workspace workspace 12b4491bd6e5bfa6799e938fd555c8f15d588a1d packages.x86_64-linux.default
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
stage deployment-contract workspace 12b4491bd6e5bfa6799e938fd555c8f15d588a1d checks.x86_64-linux.deployment-contract
stage agent-instructions workspace 12b4491bd6e5bfa6799e938fd555c8f15d588a1d checks.x86_64-linux.agent-instructions
stage cluster-provider-composition workspace 12b4491bd6e5bfa6799e938fd555c8f15d588a1d checks.x86_64-linux.cluster-provider-composition
stage agent-team-policy workspace 12b4491bd6e5bfa6799e938fd555c8f15d588a1d checks.x86_64-linux.agent-team-policy
stage runtime-generic-source dev-workspace 483d4e7eafeda974dfe19de45687795562072d7d checks.x86_64-linux.generic-source
stage shared-default codex-web ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 checks.x86_64-linux.default
stage shared-generic-source codex-web ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 checks.x86_64-linux.generic-source
printf '%s\n' 'PASS: exact sources, rooted outputs and derivations, capacity8, native Codex and reporting-only registration; no profile selection. Keep roots through activation.'
