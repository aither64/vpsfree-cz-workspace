#!/usr/bin/env bash
set -euo pipefail
# ALTERNATIVE ONLY: parent chooses exact final-head CI creation+archive receipts OR
# this local fresh-utility batch. Do not run both for the same coverage.
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/final-coordinated-ea64ef57/guards.py
root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements
operation=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/final-coordinated-ea64ef57/creation-archive-final
test ! -e "$operation"
mkdir -p "$operation/roots"
cd "$root/dev-workspace"
for label in session-creation session-archive-lifecycle; do
  nix-instantiate --expr "(builtins.getFlake \"git+file://$root/dev-workspace?rev=0c0dd2d22ce4e03c22a7bd0c471267deb6ee3a2a\").checks.x86_64-linux.$label" --add-root "$operation/roots/$label.drv" --indirect > "$operation/$label-instantiate.stdout" 2> "$operation/$label-instantiate.log"
  drv=$(readlink -f "$operation/roots/$label.drv")
  nix-store --realise "$drv" --add-root "$operation/roots/$label" --indirect > "$operation/$label.stdout" 2> "$operation/$label.log"
  nix derivation show "$drv" > "$operation/$label-derivation-raw.json"
  python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/final-coordinated-ea64ef57/normalize-derivation.py "$operation/$label-derivation-raw.json" > "$operation/$label-derivation.json"
done
