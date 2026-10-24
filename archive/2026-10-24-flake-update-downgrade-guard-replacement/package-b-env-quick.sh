#!/usr/bin/env bash
set -euo pipefail

workspace=/home/aither/workspace/ai/vpsfree.cz
slug=2026-10-24-flake-update-downgrade-guard-replacement
repo="$workspace/worktrees/$slug/confctl"
: "${B_ENV_OUTPUT:?set a new owned /tmp/flake-update-guard-b-env-* receipt directory}"
[[ "$(dirname "$B_ENV_OUTPUT")" == /tmp && "$(basename "$B_ENV_OUTPUT")" == flake-update-guard-b-env-* ]]
[[ ! -e "$B_ENV_OUTPUT" && ! -L "$B_ENV_OUTPUT" ]]
[[ "$(/home/aither/bin/dev-session current)" == "$slug" ]]
if [[ -n "${DEV_SESSION_SLUG+x}${DEV_SESSION_WORKSPACE+x}" ]]; then
  [[ "${DEV_SESSION_SLUG:-}" == "$slug" && "${DEV_SESSION_WORKSPACE:-}" == "$workspace" ]]
fi
cd "$repo"
[[ "$(git rev-parse HEAD)" == 7ba361d22a4aac044cb02abf8397800bcf5726bf ]]
mkdir -m 700 "$B_ENV_OUTPUT"
export B_ENV_OUTPUT
phase=source
finish() {
  status=$?
  trap - EXIT
  python3 - "$status" "$phase" <<'PY'
import json,os,pathlib,sys,time
root=pathlib.Path(os.environ['B_ENV_OUTPUT'])
(root/'status.json').write_text(json.dumps({
    'exit_status':int(sys.argv[1]),'phase':sys.argv[2],
    'finished_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
    'scope':'Candidate package build and two package-environment regressions only',
    'provider_out_link':str(root/'provider')
},indent=2)+'\n')
PY
  exit "$status"
}
trap finish EXIT
python3 - <<'PY'
import hashlib,json,os,pathlib,subprocess
root=pathlib.Path(os.environ['B_ENV_OUTPUT'])
paths=['nix/package.nix','spec/confctl/cli/package_environment_spec.rb',
       'docs/flake-inputs.md','man/man8/confctl.8.md','flake.nix','flake.lock','Gemfile','Gemfile.lock','gemset.nix']
data={'slug':'2026-10-24-flake-update-downgrade-guard-replacement',
      'base_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
      'source_files':{p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest() for p in paths}}
(root/'source.json').write_text(json.dumps(data,indent=2)+'\n')
(root/'source.diff').write_bytes(subprocess.check_output(['git','diff','--binary','HEAD']))
PY
phase=build
printf 'Candidate package build starting; owned output link: %s/provider\n' "$B_ENV_OUTPUT"
nix build .#confctl --out-link "$B_ENV_OUTPUT/provider" --print-out-paths \
  > "$B_ENV_OUTPUT/package-output" 2> >(tee "$B_ENV_OUTPUT/build.stderr" >&2)
mapfile -t outputs < "$B_ENV_OUTPUT/package-output"
[[ "${#outputs[@]}" == 1 && -x "${outputs[0]}/bin/confctl" ]]
export CONFCTL_BIN="${outputs[0]}/bin/confctl"
python3 - <<'PY'
import hashlib,json,os,pathlib,re,subprocess
root=pathlib.Path(os.environ['B_ENV_OUTPUT'])
binary=pathlib.Path(os.environ['CONFCTL_BIN'])
wrapper=binary.read_text()
runtime=re.search(r'export PATH="([^"\n]+):\$PATH"',wrapper).group(1)
nix=next(pathlib.Path(p)/'nix' for p in runtime.split(':') if (pathlib.Path(p)/'nix').is_file())
(root/'package.json').write_text(json.dumps({
    'package_output':str(binary.parent.parent),'wrapper_sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),
    'packaged_nix':str(nix),'packaged_nix_version':subprocess.check_output([str(nix),'--version'],text=True).strip()
},indent=2)+'\n')
PY
phase=regression
printf 'Running exactly two package caller-environment regressions\n'
nix develop -c bundle exec rspec --format documentation \
  spec/confctl/cli/package_environment_spec.rb 2>&1 | tee "$B_ENV_OUTPUT/spec.log"
phase=source-recheck
python3 - <<'PY'
import hashlib,json,os,pathlib
data=json.loads((pathlib.Path(os.environ['B_ENV_OUTPUT'])/'source.json').read_text())
assert all(hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()==value for p,value in data['source_files'].items()), 'Source changed during the focused operation'
PY
phase=passed
printf 'Focused candidate package build and two regression cases passed\n'
