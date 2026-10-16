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
sha256sum --check "$out/source.sha256" > "$out/post-generated-frozen-source.log"
python3 - "$out" <<'PY'
import hashlib,json,sys
from pathlib import Path
out=Path(sys.argv[1]);assert (out/'generated.status').read_text().strip()=='0'
raw=(out/'generated.log').read_text()
start=raw.index('\n{')+1
prefix=raw[:start]
assert all(line.startswith(('warning: Git tree ', 'evaluation warning: ')) for line in prefix.splitlines()),prefix
data,end=json.JSONDecoder().raw_decode(raw[start:])
assert not raw[start+end:].strip()
assert set(data)=={'upgrade-25.11','upgrade-26.05','upgrade-unstable','root-backed-26.05','declared-backing-26.05','dependent-mount-26.05','storage-failures-26.05','fresh-26.05','ancestor-var-26.05','ancestor-var-lib-26.05','direct-filesystem-bind-26.05','fresh-ancestor-26.05'}
(out/'generated.json').write_text(raw[start:start+end]+'\n')
(out/'generated-warning-prefix.log').write_text(prefix)
(out/'generated-extraction-receipt.json').write_text(json.dumps({'original_sha256':hashlib.sha256((out/'generated.log').read_bytes()).hexdigest(),'prefix_bytes':len(prefix.encode()),'json_bytes':len(raw[start:start+end].encode()),'trailing_nonwhitespace':False,'keys':sorted(data)},indent=2)+'\n')
for name,body in data.items(): (out/(name+'.rb')).write_text(body)
print('Preserved original output; extracted actual12scripts without another evaluation.')
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
