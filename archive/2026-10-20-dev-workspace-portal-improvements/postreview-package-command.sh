#!/usr/bin/env bash
set -euo pipefail
# Prepared only. Launch once after the lead accepts final review findings.
verification_workspace=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace
verification_runtime=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
verification_shared=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/codex-web
verification_logs=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/post-review-packages-3de65bbd
python3 - <<'PREFLIGHT'
import subprocess
repos = {
'/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace': '3de65bbd0e90f0c3b19e0d64ed925158155647a6',
'/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace': 'db25364999aa4bf12b67506662a08e9e464bee33',
'/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/codex-web': '852e8c51091512bc79ca6c921ef1f5ccc46a9535',
}
for path, revision in repos.items():
    assert subprocess.check_output(['git','-C',path,'rev-parse','HEAD'],text=True).strip() == revision, path
    assert not subprocess.check_output(['git','-C',path,'status','--porcelain']), path
print('Exact clean three-repository composition verified')
PREFLIGHT
mkdir -p "$verification_logs"
run_package_build() {
  verification_label="$1"
  shift
  printf '%s\n' "Starting $verification_label"
  if nix build --no-link --no-update-lock-file --json --print-build-logs "$@" \
      >"$verification_logs/$verification_label.json" 2>"$verification_logs/$verification_label.log"; then
    printf '%s\n' "Passed $verification_label"
  else
    verification_exit=$?
    printf '%s\n' "Failed $verification_label; exit=$verification_exit; log=$verification_logs/$verification_label.log" >&2
    exit "$verification_exit"
  fi
}
run_package_build workspace \
  "$verification_workspace#packages.x86_64-linux.default" \
  "$verification_workspace#checks.x86_64-linux.agent-team-policy" \
  "$verification_workspace#checks.x86_64-linux.agent-instructions" \
  "$verification_workspace#checks.x86_64-linux.deployment-contract"
run_package_build codex-web \
  "$verification_shared#checks.x86_64-linux.default" \
  "$verification_shared#checks.x86_64-linux.generic-source"
run_package_build dev-workspace \
  "$verification_runtime#checks.x86_64-linux.package" \
  "$verification_runtime#checks.x86_64-linux.generic-source"
verification_package=$(nix eval --no-update-lock-file --raw "$verification_workspace#packages.x86_64-linux.default.outPath")
printf '%s\n' "$verification_package" > "$verification_logs/workspace-package.path"
python3 /tmp/portal-improvements-post-review-metadata.py "$verification_package" \
  > "$verification_logs/metadata-assertions.log" 2>&1
mkdir -p "$verification_logs/disposable-registration/state" "$verification_logs/disposable-registration/workspace"
printf '{"schema":1}\n' | env -i PATH=/empty \
  "$verification_package/bin/workspace-portal" agent-teams registration \
  --package-root "$verification_package" \
  --state-root "$verification_logs/disposable-registration/state" \
  --workspace "$verification_logs/disposable-registration/workspace" \
  > "$verification_logs/registration.json" 2> "$verification_logs/registration.log"
python3 /tmp/portal-improvements-post-review-registration.py \
  "$verification_logs/registration.json" "$verification_package" \
  "$verification_logs/disposable-registration/state" \
  "$verification_logs/disposable-registration/workspace"
printf '%s\n' "Package verification and disposable metadata assertions passed"
