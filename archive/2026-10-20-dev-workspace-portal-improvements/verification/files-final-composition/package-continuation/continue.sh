#!/usr/bin/env bash
set -euo pipefail
umask 077
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-final-composition
continuation="$packet/package-continuation"
operation="$continuation/run"
roots="$packet/packages-final/roots"
root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements
selected=/nix/store/f5h1qmr03qva6khyijgc2wxd1ff4k4cw-dev-workspace-0.2.0
expected_drv=/nix/store/v466ppdwhax565z8a53z5zmx0yp1dl34-dev-workspace-0.2.0.drv
candidate=/nix/store/m8bqmkdzgk85vng42hcsavqmaz56rwgc-dev-workspace-0.2.0
python3 "$packet/guards.py"
test "$(readlink -f "$roots/workspace.drv")" = "$expected_drv"
test "$(readlink -f "$roots/workspace")" = "$candidate"
nix-store --check-validity "$expected_drv" "$candidate"
test "$(nix-store --query --outputs "$expected_drv")" = "$candidate"
test ! -e "$operation"
mkdir -p "$operation"
cd "$root/workspace"
nix derivation show "$expected_drv" > "$operation/workspace-reuse-derivation-raw.json"
python3 "$packet/normalize-derivation.py" "$operation/workspace-reuse-derivation-raw.json" > "$operation/workspace-reuse-derivation.json"
nix path-info --json "$candidate" > "$operation/workspace-reuse-path-info.json"
python3 - "$packet" "$continuation" "$operation" "$expected_drv" "$candidate" <<'REUSE'
import hashlib,json,sys
from pathlib import Path
p,c,o=map(Path,sys.argv[1:4]);drv,out=sys.argv[4:]
for name,expected in json.loads((c/'checkpoint/original-sha256.json').read_text()).items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==expected
actual=json.loads((o/'workspace-reuse-derivation.json').read_text())
recorded=json.loads((p/'packages-final/workspace-derivation.json').read_text())
evaluated=json.loads((p/'stage-derivations-normalized.json').read_text())
assert actual[drv]==recorded[drv]==evaluated[drv]
assert actual[drv]['outputs']['out']['path']==out
before=json.loads((p/'packages-final/workspace-path-info.json').read_text())[out]
current=json.loads((o/'workspace-reuse-path-info.json').read_text())[out]
for field in ['deriver','narHash','narSize','references']:
 assert current[field]==before[field],field
assert current['deriver']==drv
print('Completed workspace realization reused: exact output/derivation/inputs/NAR receipts; original evidence unchanged')
REUSE
stage() {
  local label=$1 source=$2 revision=$3 attribute=$4 drv package
  test ! -e "$roots/$label"
  test ! -L "$roots/$label"
  test ! -e "$roots/$label.drv"
  test ! -L "$roots/$label.drv"
  nix-instantiate --expr "(builtins.getFlake \"git+file://$root/$source?rev=$revision\").$attribute" \
    --add-root "$roots/$label.drv" --indirect \
    > "$operation/$label-instantiate.stdout" 2> "$operation/$label-instantiate.log"
  drv=$(readlink -f "$roots/$label.drv")
  python3 - "$packet" "$label" "$drv" <<'EXACT_STAGE'
import json,sys
from pathlib import Path
ids=json.loads((Path(sys.argv[1])/'stage-derivation-identities.json').read_text())
keys={'deployment-contract':'deployment','agent-instructions':'instructions','cluster-provider-composition':'cluster','agent-team-policy':'policy','runtime-generic-source':'Bgeneric','shared-default':'Adefault','shared-generic-source':'Ageneric'}
assert ids[keys[sys.argv[2]]]==sys.argv[3]
EXACT_STAGE
  nix-store --realise "$drv" --add-root "$roots/$label" --indirect \
    > "$operation/$label.stdout" 2> "$operation/$label.log"
  package=$(readlink -f "$roots/$label")
  test "$package" = "$(nix-store --query --outputs "$drv")"
  nix derivation show "$drv" > "$operation/$label-derivation-raw.json"
  python3 "$packet/normalize-derivation.py" "$operation/$label-derivation-raw.json" > "$operation/$label-derivation.json"
  nix path-info --json "$package" > "$operation/$label-path-info.json"
}
python3 "$continuation/metadata-app56.py" "$candidate" > "$operation/metadata.log" 2>&1
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
