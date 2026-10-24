#!/usr/bin/env bash
# Prepared exact published Git-cache provider check; root launches after final review/publication.
set -euo pipefail
workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-24-flake-update-downgrade-guard-replacement
source='github:vpsfreecz/confctl/822c0e35dbe2549111912f539116b4225dfd3035'
: "${B_GIT_ROOT:?set a fresh owned /tmp/flake-update-guard-b-git-cache-* directory}"
: "${B_GIT_REVIEW_RECEIPT:?set the completed final Git-cache affected-review receipt}"
[[ "$(dirname "$B_GIT_ROOT")" == /tmp && "$(basename "$B_GIT_ROOT")" == flake-update-guard-b-git-cache-* ]]
[[ ! -e "$B_GIT_ROOT" && ! -L "$B_GIT_ROOT" && -f "$B_GIT_REVIEW_RECEIPT" ]]
[[ "$(/home/aither/bin/dev-session current)" == "$slug" ]]
if [[ -n "${DEV_SESSION_SLUG+x}${DEV_SESSION_WORKSPACE+x}" ]]; then
  [[ "${DEV_SESSION_SLUG:-}" == "$slug" && "${DEV_SESSION_WORKSPACE:-}" == "$workspace" ]]
fi
repo="$workspace/worktrees/$slug/confctl"
[[ "$(git -C "$repo" rev-parse HEAD)" == 822c0e35dbe2549111912f539116b4225dfd3035 ]]
[[ -z "$(git -C "$repo" status --porcelain=v1)" ]]
[[ "$(git --git-dir="$workspace/repos/confctl.git" rev-parse "refs/heads/$slug")" == 822c0e35dbe2549111912f539116b4225dfd3035 ]]
mkdir -m 700 "$B_GIT_ROOT"
mkdir "$B_GIT_ROOT/sources"
B_GIT_SCRIPT="$(realpath "$0")"
export B_GIT_ROOT B_GIT_REVIEW_RECEIPT B_GIT_SCRIPT
phase=source
finish() {
  status=$?
  trap - EXIT
  python3 - "$status" "$phase" <<'PY'
import hashlib,json,os,pathlib,sys,time
root=pathlib.Path(os.environ['B_GIT_ROOT'])
(root/'status.json').write_text(json.dumps({
    'provider_head':'822c0e35dbe2549111912f539116b4225dfd3035',
    'exit_status':int(sys.argv[1]),'phase':sys.argv[2],
    'preceding_review_receipt_sha256':hashlib.sha256(pathlib.Path(os.environ['B_GIT_REVIEW_RECEIPT']).read_bytes()).hexdigest(),
    'finished_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
    'check':'checks.x86_64-linux.rspec','expected_examples':203,
    'source':'github:vpsfreecz/confctl/822c0e35dbe2549111912f539116b4225dfd3035',
    'driver_sha256':hashlib.sha256(pathlib.Path(os.environ['B_GIT_SCRIPT']).read_bytes()).hexdigest()
},indent=2)+'\n')
PY
  exit "$status"
}
trap finish EXIT
# Public immutable flake only. No auth loader, credential/config read, or environment dump.
nix flake metadata --json --no-write-lock-file "$source" | python3 -c '
import json,os,pathlib,sys
raw=sys.stdin.read()
data=json.loads(raw)
assert data["locked"]["rev"]=="822c0e35dbe2549111912f539116b4225dfd3035"
(pathlib.Path(os.environ["B_GIT_ROOT"])/"metadata.json").write_text(json.dumps(data,indent=2)+"\n")'
nix flake archive --json --no-write-lock-file "$source" | python3 -c '
import json,os,pathlib,sys
raw=sys.stdin.read()
root=pathlib.Path(os.environ["B_GIT_ROOT"]); data=json.loads(raw)
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
  nix-store --add-root "$B_GIT_ROOT/sources/source-$index" --indirect --realise "$path" > /dev/null
  index=$((index + 1))
done < "$B_GIT_ROOT/source-paths"
mapfile -t source_paths < "$B_GIT_ROOT/source-paths"
nix path-info --json --recursive "${source_paths[@]}" > "$B_GIT_ROOT/source-closure.json"
nix derivation show --recursive "$source#checks.x86_64-linux.rspec" > "$B_GIT_ROOT/check-derivations.json"
nix derivation show --recursive "$source#confctl" > "$B_GIT_ROOT/provider-derivations.json"
phase=provider
nix build "$source#confctl" --out-link "$B_GIT_ROOT/provider" --json \
  > "$B_GIT_ROOT/provider-build.json" 2> >(tee "$B_GIT_ROOT/provider-build.stderr" >&2)
nix path-info --json --recursive "$B_GIT_ROOT/provider" > "$B_GIT_ROOT/provider-closure.json"
python3 - <<'PY_PACKAGE'
import hashlib,json,os,pathlib,re,subprocess
root=pathlib.Path(os.environ['B_GIT_ROOT'])
build=json.loads((root/'provider-build.json').read_text())
assert len(build)==1 and set(build[0]['outputs'])=={'out'}
package=pathlib.Path(build[0]['outputs']['out'])
assert (root/'provider').resolve()==package and package.is_dir()
wrapper=package/'bin/confctl'
text=wrapper.read_text()
(root/'confctl-wrapper').write_text(text)
match=re.search(r'export PATH="([^"\n]+):\$PATH"',text)
assert match,'Package PATH contract changed'
runtime=match[1].split(':')
binaries={name:next((str(pathlib.Path(directory)/name) for directory in runtime if (pathlib.Path(directory)/name).is_file()),None) for name in ('git','nix')}
ruby=re.search(r'exec (/nix/store/[^ \n]+/bin/ruby) --disable=rubyopt ',text)
assert ruby,'Package Ruby startup contract changed'
binaries['ruby']=ruby[1]
assert all(binaries.values()),'Package runtime executable missing'
versions={name:subprocess.check_output([binary,'--version'],text=True).strip() for name,binary in binaries.items()}
metadata=json.loads((root/'metadata.json').read_text())
info={
 'provider_head':'822c0e35dbe2549111912f539116b4225dfd3035',
 'source':metadata['path'],'source_nar_hash':metadata['locked'].get('narHash'),
 'package_output':str(package),'package_drv':build[0]['drvPath'],
 'wrapper_sha256':hashlib.sha256(wrapper.read_bytes()).hexdigest(),
 'runtime_binaries':binaries,'runtime_versions':versions
}
(root/'package.json').write_text(json.dumps(info,indent=2)+'\n')
PY_PACKAGE
phase=rspec
nix build "$source#checks.x86_64-linux.rspec" --out-link "$B_GIT_ROOT/rspec" --json --print-build-logs \
  > "$B_GIT_ROOT/check-build.json" 2> >(tee "$B_GIT_ROOT/check-build.stderr" >&2)
nix path-info --json --recursive "$B_GIT_ROOT/rspec" > "$B_GIT_ROOT/check-closure.json"
nix path-info --derivation "$B_GIT_ROOT/rspec" > "$B_GIT_ROOT/check-derivation"
nix log "$(cat "$B_GIT_ROOT/check-derivation")" > "$B_GIT_ROOT/check-build.log"
python3 - <<'PY'
import json,os,pathlib,re
root=pathlib.Path(os.environ['B_GIT_ROOT'])
summaries=re.findall(r'(\d+) examples?, (\d+) failures?(?:, (\d+) pending)?',(root/'check-build.log').read_text())
assert summaries and summaries[-1]==('203','0',''), 'Expected complete final suite with 203 examples, no failures or pending cases'
(root/'coverage.json').write_text(json.dumps({'examples':203,'failures':0,'pending':0,'source':'Exact exported check build log'},indent=2)+'\n')
PY
python3 - <<'PY_IDENTITIES'
import json,os,pathlib
root=pathlib.Path(os.environ['B_GIT_ROOT'])
package=json.loads((root/'package.json').read_text())
metadata=json.loads((root/'metadata.json').read_text())
check=json.loads((root/'check-build.json').read_text())
assert len(check)==1 and set(check[0]['outputs'])=={'out'}
assert (root/'rspec').is_symlink() and (root/'rspec').resolve()==pathlib.Path(check[0]['outputs']['out'])
source_closure=json.loads((root/'source-closure.json').read_text())
source_info=source_closure[metadata['path']] if isinstance(source_closure,dict) else next(p for p in source_closure if p['path']==metadata['path'])
assert source_info['narHash']==metadata['locked']['narHash'],'Source NAR disagreement'
package.update({
 'source_nar_hash':source_info['narHash'],
 'check_drv':check[0]['drvPath'],'check_output':check[0]['outputs']['out'],
 'coverage':json.loads((root/'coverage.json').read_text()),
 'recursive_provider_derivations':'provider-derivations.json',
 'recursive_check_derivations':'check-derivations.json',
 'source_archive':'archive.json','source_closure':'source-closure.json',
 'provider_closure':'provider-closure.json','check_closure':'check-closure.json'
})
(root/'identities.json').write_text(json.dumps(package,indent=2)+'\n')
PY_IDENTITIES
[[ "$(git -C "$repo" rev-parse HEAD)" == 822c0e35dbe2549111912f539116b4225dfd3035 ]]
[[ -z "$(git -C "$repo" status --porcelain=v1)" ]]
phase=passed
printf 'Final exact-source exported RSpec check passed; retained provider/check/source roots: %s\n' "$B_GIT_ROOT"
