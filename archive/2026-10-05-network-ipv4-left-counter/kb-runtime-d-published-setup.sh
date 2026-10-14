#!/usr/bin/env bash
set -euo pipefail
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
prefix=kb-runtime-d-published-setup
cd "$tracking"
test "$(cat kb-runtime-d-upstream-published.sha)" = 51aba080b264c28f5584867b6cf006bf423ae2f3
for suffix in log exit metadata.json source.path metadata.exit ci.log ci.exit; do
  test ! -e "$tracking/$prefix.$suffix"
done
set -o noclobber
exec > >(tee "$tracking/$prefix.log") 2>&1
trap 'result=$?; printf "%s\n" "$result" >"$tracking/$prefix.exit"' EXIT
nix flake metadata --json --no-write-lock-file github:aither64/dev-workspace/51aba080b264c28f5584867b6cf006bf423ae2f3 > "$tracking/$prefix.metadata.json"
python3 - "$tracking/$prefix.metadata.json" <<'PY' > "$tracking/$prefix.source.path"
import json,sys,pathlib
value=json.load(open(sys.argv[1]))
assert value['locked']['rev']=='51aba080b264c28f5584867b6cf006bf423ae2f3'
source=pathlib.Path(value['path'])
assert str(source).startswith('/nix/store/') and source.is_dir()
print(source)
PY
printf '0\n' > "$tracking/$prefix.metadata.exit"
cat "$tracking/$prefix.source.path"
set +e
(set -e; nix shell --inputs-from github:aither64/dev-workspace/51aba080b264c28f5584867b6cf006bf423ae2f3 nixpkgs#gh nixpkgs#python3 nixpkgs#git --command bash "$tracking/kb-runtime-d-upstream-cancel-ci.sh") > "$tracking/$prefix.ci.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" > "$tracking/$prefix.ci.exit"
cat "$tracking/$prefix.ci.log"
exit "$result"
