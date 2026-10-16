#!/usr/bin/env bash
set -euo pipefail
record=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports
out="$record/effective-mounts-i1-quick"
mkdir -p "$out"
[ "$(git rev-parse HEAD)" = bf74af0b76accdf844ad6ffbea75db6c409f386e ]
[ -z "$(git diff --cached --name-only)" ]
sha256sum --check "$out/source.sha256"
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
[ "$(cat "$out/persistence-eval.status")" = 0 ]
[ "$(cat "$out/focused-shell.status")" = 0 ]
run generated bash -c 'nix eval --impure --json --file "$1" > "$2"' generated "$record/persistence-store-fixture-diagnosis/generated-scripts.nix" "$out/generated.json"
python3 - "$out" <<'PY2'
import json,sys
from pathlib import Path
out=Path(sys.argv[1]);scripts=json.loads((out/'generated.json').read_text())
assert set(scripts)=={'upgrade-25.11','upgrade-26.05','upgrade-unstable','root-backed-26.05','declared-backing-26.05','dependent-mount-26.05','storage-failures-26.05','fresh-26.05','ancestor-var-26.05','ancestor-var-lib-26.05','direct-filesystem-bind-26.05','fresh-ancestor-26.05'}
for name,body in scripts.items(): (out/(name+'.rb')).write_text(body)
PY2
for script in "$out"/*.rb; do run "$(basename "$script" .rb)-syntax" ruby -c "$script"; done
run hooks overcommit --run
sha256sum --check "$out/source.sha256"
status=0
