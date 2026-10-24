#!/usr/bin/env bash
set -euo pipefail
verification_logs=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/post-review-packages-3de65bbd
verification_supplement="$verification_logs/registration-contract-correction"
verification_package=$(cat "$verification_logs/workspace-package.path")
mkdir -p "$verification_supplement"
python3 /tmp/portal-improvements-post-review-metadata.py "$verification_package" \
  > "$verification_supplement/metadata-assertions.log" 2>&1
python3 /tmp/portal-improvements-post-review-registration.py \
  "$verification_logs/registration.json" "$verification_package" \
  "$verification_logs/disposable-registration/state" \
  "$verification_logs/disposable-registration/workspace" \
  > "$verification_supplement/original-registration-check.log" 2>&1
printf '{"schema":1}\n' | env -i PATH=/empty \
  "$verification_package/bin/workspace-portal" agent-teams registration \
  --package-root "$verification_package" \
  --state-root "$verification_logs/disposable-registration/state" \
  --workspace "$verification_logs/disposable-registration/workspace" \
  > "$verification_supplement/registration.json" 2> "$verification_supplement/registration.log"
python3 /tmp/portal-improvements-post-review-registration.py \
  "$verification_supplement/registration.json" "$verification_package" \
  "$verification_logs/disposable-registration/state" \
  "$verification_logs/disposable-registration/workspace" \
  > "$verification_supplement/registration-assertions.log" 2>&1
cmp "$verification_logs/registration.json" "$verification_supplement/registration.json"
printf '%s\n' 'PASS: existing metadata; original and fresh PATH=/empty disposable registration; byte-identical registration argv/digest; no builds rerun'
