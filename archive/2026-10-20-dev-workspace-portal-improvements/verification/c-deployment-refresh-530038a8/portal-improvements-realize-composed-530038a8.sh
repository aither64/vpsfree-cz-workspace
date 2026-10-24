#!/usr/bin/env bash
set -euo pipefail
umask 077
# PREPARED ONLY: lead launches a fresh policy-bound utility after review.
candidate_source=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace
candidate_operation=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-candidate-530038a8
candidate_installed=/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0
candidate_expected_drv=/nix/store/cscdy7ahywqp1lw8lc5jrmh3776n6y2q-dev-workspace-0.2.0.drv
candidate_expected_package=/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0
python3 - <<'GUARDS'
import os, subprocess
from pathlib import Path
assert subprocess.check_output(['dev-session', 'current'], text=True).strip() == '2026-10-20-dev-workspace-portal-improvements'
assert os.environ.get('DEV_SESSION_SLUG') == '2026-10-20-dev-workspace-portal-improvements'
assert os.environ.get('DEV_SESSION_WORKSPACE') == '/home/aither/workspace/ai/vpsfree.cz'
assert Path('/home/aither/bin/workspace-host').resolve() == Path('/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0/bin/workspace-host')
root=Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements')
for name, head in {'workspace':'530038a8ee2bf6772144b07ca0cb02426fc1e6d6',
                   'dev-workspace':'f8f2938b4e2cfd6e5b82657d08f014357817808f',
                   'codex-web':'852e8c51091512bc79ca6c921ef1f5ccc46a9535'}.items():
    assert subprocess.check_output(['git','-C',str(root/name),'rev-parse','HEAD'],text=True).strip()==head
    assert not subprocess.check_output(['git','-C',str(root/name),'status','--porcelain'])
print('Exact session, selected predecessor and clean final A/B/C verified')
GUARDS
mkdir -p "$candidate_operation/roots"
nix-instantiate --expr '(builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace?rev=530038a8ee2bf6772144b07ca0cb02426fc1e6d6").packages.x86_64-linux.default' \
  --add-root "$candidate_operation/roots/candidate.drv" --indirect \
  > "$candidate_operation/instantiate.stdout" 2> "$candidate_operation/instantiate.log"
candidate_drv=$(readlink -f "$candidate_operation/roots/candidate.drv")
candidate_source_drv=$(nix eval --no-update-lock-file --raw "$candidate_source#packages.x86_64-linux.default.drvPath")
test "$candidate_drv" = "$candidate_expected_drv"
test "$candidate_drv" = "$candidate_source_drv"
printf '%s\n' "$candidate_drv" > "$candidate_operation/candidate.drv.path"
nix-store --realise "$candidate_drv" --add-root "$candidate_operation/roots/candidate" --indirect \
  > "$candidate_operation/realise.stdout" 2> "$candidate_operation/realise.log"
candidate_package=$(readlink -f "$candidate_operation/roots/candidate")
test "$candidate_package" = "$candidate_expected_package"
test "$candidate_package" = "$(nix-store --query --outputs "$candidate_drv")"
printf '%s\n' "$candidate_package" > "$candidate_operation/candidate.package.path"
nix derivation show "$candidate_drv" > "$candidate_operation/derivation.json"
nix path-info --json "$candidate_package" > "$candidate_operation/package-path-info.json"
python3 /tmp/portal-improvements-deployment-metadata.py "$candidate_package" \
  > "$candidate_operation/metadata-assertions.log" 2>&1
"$candidate_package/bin/workspace-host" check-codex \
  --codex "$candidate_package/libexec/codex/bin/codex" \
  > "$candidate_operation/codex-compatibility.log" 2>&1
mkdir -p "$candidate_operation/disposable-registration/state" "$candidate_operation/disposable-registration/workspace"
for candidate_check_package in "$candidate_installed" "$candidate_package"; do
  if test "$candidate_check_package" = "$candidate_installed"; then
    candidate_plan_label=selected
  else
    candidate_plan_label=candidate
  fi
  printf '{"schema":1}\n' | env -i PATH=/empty \
    "$candidate_check_package/bin/workspace-portal" agent-teams registration \
    --package-root "$candidate_check_package" \
    --state-root "$candidate_operation/disposable-registration/state" \
    --workspace "$candidate_operation/disposable-registration/workspace" \
    > "$candidate_operation/$candidate_plan_label-registration.json" \
    2> "$candidate_operation/$candidate_plan_label-registration.log"
  python3 /tmp/portal-improvements-post-review-registration.py \
    "$candidate_operation/$candidate_plan_label-registration.json" "$candidate_check_package" \
    "$candidate_operation/disposable-registration/state" \
    "$candidate_operation/disposable-registration/workspace" \
    > "$candidate_operation/$candidate_plan_label-registration-assertions.log" 2>&1
done
nix build --no-update-lock-file --json --print-build-logs \
  --out-link "$candidate_operation/roots/agent-team-policy" \
  "$candidate_source#checks.x86_64-linux.agent-team-policy" \
  > "$candidate_operation/agent-team-policy.json" 2> "$candidate_operation/agent-team-policy.log"
nix build --no-update-lock-file --json --print-build-logs \
  --out-link "$candidate_operation/roots/runtime-generic-source" \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace#checks.x86_64-linux.generic-source \
  > "$candidate_operation/runtime-generic-source.json" 2> "$candidate_operation/runtime-generic-source.log"
printf '%s\n' 'PASS: exact composed candidate rooted with derivation; metadata/contracts/native executable and reporting-only registration verified. Roots retained; no profile selection.'
