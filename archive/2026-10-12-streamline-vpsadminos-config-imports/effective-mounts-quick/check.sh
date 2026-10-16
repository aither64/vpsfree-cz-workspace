#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
product=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos
out="$record/effective-mounts-quick"
cd "$product"
status=1
trap 'printf "%s\n" "$status" > "$out/status"' EXIT
run() {
  local label=$1
  shift
  local result=0
  "$@" > "$out/$label.log" 2>&1 || result=$?
  printf '%s\n' "$result" > "$out/$label.status"
  printf '%s %s\n' "$label" "$result"
  return "$result"
}
git rev-parse HEAD > "$out/head"
git diff --binary > "$out/source.diff"
git diff --name-only -z | xargs -0 sha256sum > "$out/source.sha256"
run persistence nix build .#checks.x86_64-linux.nixos-container-persistence --no-link --print-build-logs
run evaluator bash tests/nixos-container-eval.sh
run generated bash -c 'nix eval --impure --json --file "$1" > "$2"' generated "$record/persistence-store-fixture-diagnosis/generated-scripts.nix" "$out/generated.json"
python3 - "$out" <<'PY'
import json, sys
from pathlib import Path
out = Path(sys.argv[1])
scripts = json.loads((out/'generated.json').read_text())
expected = {'upgrade-25.11','upgrade-26.05','upgrade-unstable',
 'root-backed-26.05','declared-backing-26.05','dependent-mount-26.05',
 'storage-failures-26.05','fresh-26.05','ancestor-var-26.05',
 'ancestor-var-lib-26.05','direct-filesystem-bind-26.05','fresh-ancestor-26.05'}
assert set(scripts) == expected, set(scripts)
for name, body in scripts.items():
 (out/(name+'.rb')).write_text(body)
print('Actual generated scripts:',len(scripts))
PY
for script in "$out"/*.rb; do
  label=$(basename "$script" .rb)
  run "$label-syntax" ruby -c "$script"
done
run docs make doc
run hooks overcommit --run
run discovery ./test-runner.sh ls -t ci 'dist-config/nixos-persistence-upgrade*'
sha256sum --check "$out/source.sha256" > "$out/frozen-source.log"
status=0
