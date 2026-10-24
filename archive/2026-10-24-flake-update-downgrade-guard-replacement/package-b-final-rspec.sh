#!/usr/bin/env bash
# Prepared only; root assigns this operation after affected review and publication.
set -euo pipefail
workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-24-flake-update-downgrade-guard-replacement
source=github:vpsfreecz/confctl/bdaed19e901237e05bd0a779f368e76cb311143f
: "${B_FINAL_ROOT:?set a fresh owned /tmp/flake-update-guard-b-final-* directory}"
: "${B_FINAL_REVIEW_RECEIPT:?set the completed affected-review receipt}"
[[ "$(dirname "$B_FINAL_ROOT")" == /tmp && "$(basename "$B_FINAL_ROOT")" == flake-update-guard-b-final-* ]]
[[ ! -e "$B_FINAL_ROOT" && ! -L "$B_FINAL_ROOT" && -f "$B_FINAL_REVIEW_RECEIPT" ]]
[[ "$(/home/aither/bin/dev-session current)" == "$slug" ]]
if [[ -n "${DEV_SESSION_SLUG+x}${DEV_SESSION_WORKSPACE+x}" ]]; then
  [[ "${DEV_SESSION_SLUG:-}" == "$slug" && "${DEV_SESSION_WORKSPACE:-}" == "$workspace" ]]
fi
mkdir -m 700 "$B_FINAL_ROOT"
mkdir "$B_FINAL_ROOT/sources"
export B_FINAL_ROOT B_FINAL_REVIEW_RECEIPT
phase=source
finish() {
  status=$?
  trap - EXIT
  python3 - "$status" "$phase" <<'PY'
import hashlib,json,os,pathlib,sys,time
root=pathlib.Path(os.environ['B_FINAL_ROOT'])
(root/'status.json').write_text(json.dumps({
    'provider_head':'bdaed19e901237e05bd0a779f368e76cb311143f',
    'exit_status':int(sys.argv[1]),'phase':sys.argv[2],
    'review_receipt_sha256':hashlib.sha256(pathlib.Path(os.environ['B_FINAL_REVIEW_RECEIPT']).read_bytes()).hexdigest(),
    'finished_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
    'check':'checks.x86_64-linux.rspec','expected_examples':197
},indent=2)+'\n')
PY
  exit "$status"
}
trap finish EXIT
# Validate metadata in memory before writing it; never print token/environment values.
nix flake metadata --json --no-write-lock-file "$source" | python3 -c '
import json,os,pathlib,sys
raw=sys.stdin.read()
assert not any(os.environ.get(k) and os.environ[k] in raw for k in ("GITHUB_TOKEN","GH_TOKEN")), "Credential in metadata"
data=json.loads(raw)
assert data["locked"]["rev"]=="bdaed19e901237e05bd0a779f368e76cb311143f"
(pathlib.Path(os.environ["B_FINAL_ROOT"])/"metadata.json").write_text(json.dumps(data,indent=2)+"\n")'
nix flake archive --json --no-write-lock-file "$source" | python3 -c '
import json,os,pathlib,sys
raw=sys.stdin.read()
assert not any(os.environ.get(k) and os.environ[k] in raw for k in ("GITHUB_TOKEN","GH_TOKEN")), "Credential in archive"
root=pathlib.Path(os.environ["B_FINAL_ROOT"]); data=json.loads(raw)
assert data["path"]==json.loads((root/"metadata.json").read_text())["path"]
(root/"archive.json").write_text(json.dumps(data,indent=2)+"\n")
paths=set()
def collect(item):
 paths.add(item["path"])
 for child in item.get("inputs",{}).values(): collect(child)
collect(data)
(root/"source-paths").write_text("".join(p+"\n" for p in sorted(paths)))'
index=0
while IFS= read -r path; do
  nix-store --add-root "$B_FINAL_ROOT/sources/source-$index" --indirect --realise "$path" > /dev/null
  index=$((index + 1))
done < "$B_FINAL_ROOT/source-paths"
mapfile -t source_paths < "$B_FINAL_ROOT/source-paths"
nix path-info --json --recursive "${source_paths[@]}" > "$B_FINAL_ROOT/source-closure.json"
nix derivation show --recursive "$source#checks.x86_64-linux.rspec" > "$B_FINAL_ROOT/check-derivations.json"
nix derivation show --recursive "$source#confctl" > "$B_FINAL_ROOT/provider-derivations.json"
phase=provider
nix build "$source#confctl" --out-link "$B_FINAL_ROOT/provider" --json \
  > "$B_FINAL_ROOT/provider-build.json" 2> >(tee "$B_FINAL_ROOT/provider-build.stderr" >&2)
nix path-info --json --recursive "$B_FINAL_ROOT/provider" > "$B_FINAL_ROOT/provider-closure.json"
phase=rspec
nix build "$source#checks.x86_64-linux.rspec" --out-link "$B_FINAL_ROOT/rspec" --json --print-build-logs \
  > "$B_FINAL_ROOT/check-build.json" 2> >(tee "$B_FINAL_ROOT/check-build.stderr" >&2)
nix path-info --json --recursive "$B_FINAL_ROOT/rspec" > "$B_FINAL_ROOT/check-closure.json"
nix path-info --derivation "$B_FINAL_ROOT/rspec" > "$B_FINAL_ROOT/check-derivation"
nix log "$(cat "$B_FINAL_ROOT/check-derivation")" > "$B_FINAL_ROOT/check-build.log"
python3 - <<'PY'
import json,os,pathlib,re
root=pathlib.Path(os.environ['B_FINAL_ROOT'])
summaries=re.findall(r'(\d+) examples?, (\d+) failures?(?:, (\d+) pending)?',(root/'check-build.log').read_text())
assert summaries and summaries[-1]==('197','0',''), 'Expected complete final suite with 197 examples, no failures or pending cases'
(root/'coverage.json').write_text(json.dumps({'examples':197,'failures':0,'pending':0,'source':'Exact exported check build log'},indent=2)+'\n')
PY
phase=passed
printf 'Final exact-source exported RSpec check passed; retained provider/check/source roots: %s\n' "$B_FINAL_ROOT"
