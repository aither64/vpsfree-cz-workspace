#!/usr/bin/env bash
# PREPARED ONLY. Run once through the authorized watcher after committed review.
set -euo pipefail

task_workspace=/home/aither/workspace/ai/vpsfree.cz
task_slug=2026-10-19-haveapi-async-client
haveapi_ref=19c20c90cc957d4225ece50a92e190855f252710
haveapi_repo="$task_workspace/worktrees/$task_slug/haveapi"
candidate_repo="$task_workspace/worktrees/$task_slug/dev-workspace"
seed_source=/home/aither/.local/state/dev-workspaces/coordination/sources/19c20c90cc957d4225ece50a92e190855f252710/checkout
seed_lock_sha=450de01a459fd59f8237065094ee4bf59d1263049af14244a768b29b7f2ebfc5
selected_package=/nix/store/ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp-dev-workspace-0.2.0
host_ruby=/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby
proof_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
candidate_ref=${1:?Supply the full committed, reviewed correction SHA}
[[ $candidate_ref =~ ^[0-9a-f]{40}$ ]]
[[ $(dev-session current) == "$task_slug" ]]
[[ ${DEV_SESSION_SLUG:-$task_slug} == "$task_slug" ]]
[[ ${DEV_SESSION_WORKSPACE:-$task_workspace} == "$task_workspace" ]]
[[ ${DEV_SESSION_SLUG+x} == "${DEV_SESSION_WORKSPACE+x}" ]]
[[ ! -v GIT_DIR && ! -v GIT_WORK_TREE && ! -v GIT_COMMON_DIR ]]
[[ $(readlink -f /home/aither/.local/state/dev-workspaces/profile) == "$selected_package" ]]
IFS= read -r selected_shebang < "$selected_package/libexec/.workspace-host-wrapped"
[[ $selected_shebang == "#!$host_ruby" ]]
[[ $(git -C "$haveapi_repo" rev-parse "$haveapi_ref^{commit}") == "$haveapi_ref" ]]
[[ $(git -C "$candidate_repo" rev-parse "$candidate_ref^{commit}") == "$candidate_ref" ]]

run_dir=$(mktemp -d /tmp/2026-10-19-haveapi-async-client-hook-abi.XXXXXX)
exec > >(tee "$run_dir/run.log") 2>&1
trap 'task_exit=$?; printf "%s\n" "$task_exit" > "$run_dir/run.exit"' EXIT
printf 'Evidence directory: %s\n' "$run_dir"
git -C "$haveapi_repo" archive --format=tar --output="$run_dir/source.tar" "$haveapi_ref"
git -C "$candidate_repo" show "$candidate_ref:libexec/workspace-coordination-execution.rb" > "$run_dir/candidate-execution.rb"
git -C "$haveapi_repo" ls-tree -r -z --name-only "$haveapi_ref" > "$run_dir/tracked-paths"
mkdir "$run_dir/source"
tar -xf "$run_dir/source.tar" -C "$run_dir/source"
cmp "$seed_source/Gemfile" "$run_dir/source/Gemfile"
# Gemfile.lock is generated/ignored, so retain it as dependency seed provenance.
cp "$seed_source/Gemfile.lock" "$run_dir/source/Gemfile.lock"
cmp "$seed_source/Gemfile.lock" "$run_dir/source/Gemfile.lock"
# A real file copy permits ordinary shell initialization without shared writes.
# No hardlinks, live GEM_HOME symlink, mounts, alternate ABI or installer flags.
cp -a --reflink=auto "$seed_source/.gems" "$run_dir/source/.gems"

python3 - "$run_dir" "$seed_source" "$proof_dir" "$candidate_ref" "$selected_package" "$seed_lock_sha" <<'PY'
from pathlib import Path
import hashlib, json, re, sys, textwrap
run, seed, proof = map(Path, sys.argv[1:4])
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
paths = [p.decode() for p in (run/'tracked-paths').read_bytes().split(b'\0') if p]
def fingerprint(root, path):
    file = root/path
    return {'symlink': str(file.readlink())} if file.is_symlink() else {'sha256': digest(file)}
source = (run/'candidate-execution.rb').read_text()
match = re.search(r"^      program = <<~'RUBY'\n(.*?)^      RUBY$", source, re.M | re.S)
assert match, 'candidate validation program not found'
validation = textwrap.dedent(match.group(1))
assert validation in (proof/'validate.rb').read_text(), 'candidate validation program changed'
snapshot = run/'source'
assert digest(seed/'Gemfile.lock') == digest(snapshot/'Gemfile.lock') == sys.argv[6], 'dependency seed lock changed'
for path in (snapshot/'.gems').rglob('*'):
    if path.is_symlink():
        assert path.resolve().is_relative_to((snapshot/'.gems').resolve()), 'copied gem symlink escapes snapshot'
native = [str(p.relative_to(seed)) for p in (seed/'.gems/gems').rglob('*.so')]
assert native, 'no seed native files'
baseline = {'candidateRef': sys.argv[4], 'haveapiRef': '19c20c90cc957d4225ece50a92e190855f252710',
    'selectedPackage': sys.argv[5],
    'selectedWrapperSha256': digest(Path(sys.argv[5])/'libexec/.workspace-host-wrapped'),
    'candidateExecutionSha256': digest(run/'candidate-execution.rb'),
    'validationProgramSha256': hashlib.sha256(validation.encode()).hexdigest(),
    'sourceArchiveSha256': digest(run/'source.tar'),
    'externalDependencySeed': {'kind': 'ignored shell-generated Gemfile.lock and matching Ruby 3.3 gems',
        'source': str(seed), 'gemfileSha256': digest(seed/'Gemfile'),
        'seedLockSha256': digest(seed/'Gemfile.lock'),
        'snapshotLockSha256': digest(snapshot/'Gemfile.lock')},
    'trackedFiles': {p: fingerprint(snapshot,p) for p in paths},
    'seedNativeFiles': {p: digest(seed/p) for p in native}}
(run/'baseline.json').write_text(json.dumps(baseline,indent=2)+'\n')
PY

env -u GEM_HOME -u GEM_PATH -u RUBYOPT -u BUNDLE_GEMFILE "$host_ruby" --disable-gems -rrbconfig \
  -e 'abort "unexpected coordinator Ruby/API" unless RUBY_VERSION == "3.4.9" && RbConfig::CONFIG["ruby_version"] == "3.4.0"; puts [RbConfig.ruby, RUBY_VERSION, RbConfig::CONFIG["ruby_version"]].join("\t")' > "$run_dir/host-ruby.tsv"
cd "$run_dir/source"
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  printf 'Disposable source unexpectedly belongs to a Git checkout\n' >&2
  exit 1
fi
allowed=(PATH GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_APP_CONFIG BUNDLER_VERSION NIX_SSL_CERT_FILE SSL_CERT_FILE)
env -u GEM_HOME -u GEM_PATH -u BUNDLE_GEMFILE -u BUNDLE_PATH -u BUNDLE_APP_CONFIG -u BUNDLER_VERSION \
  HAVEAPI_RELEASE_TOOLS_ONLY=0 nix develop "path:$PWD" --command ruby -e "$(cat "$proof_dir/validate.rb")" "${allowed[@]}" \
  2>&1 | tee "$run_dir/validation.log"

python3 - "$run_dir" "$seed_source" <<'PY'
from pathlib import Path
import hashlib, json, sys
run, seed = map(Path, sys.argv[1:])
baseline = json.loads((run/'baseline.json').read_text())
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
dependency_seed = baseline['externalDependencySeed']
assert digest(seed/'Gemfile') == dependency_seed['gemfileSha256'], 'original seed Gemfile changed'
assert digest(seed/'Gemfile.lock') == dependency_seed['seedLockSha256'], 'original seed lock changed'
assert digest(run/'source/Gemfile.lock') == dependency_seed['snapshotLockSha256'], 'snapshot dependency lock changed'
for path, expected in baseline['trackedFiles'].items():
    file = run/'source'/path
    actual = {'symlink': str(file.readlink())} if file.is_symlink() else {'sha256': digest(file)}
    assert actual == expected, f'committed product file changed: {path}'
for path, expected in baseline['seedNativeFiles'].items():
    assert digest(seed/path) == expected, f'original seed native file changed: {path}'
lines = (run/'validation.log').read_text().splitlines()
def receipt(marker):
    matches = [line[len(marker):] for line in lines if line.startswith(marker)]
    assert len(matches) == 1, f'expected exactly one {marker}'
    return json.loads(matches[0])
environment = receipt('WORKSPACE_MERGE_HOOK_ENV=')
allowed = 'PATH GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH BUNDLE_APP_CONFIG BUNDLER_VERSION NIX_SSL_CERT_FILE SSL_CERT_FILE'.split()
assert set(environment).issubset(allowed)
assert all(isinstance(v,str) for v in environment.values())
assert environment.get('PATH')
assert environment.get('GEM_HOME') == str(run/'source/.gems')
abi = receipt('HAVEAPI_HOOK_ABI_PROOF=')
host_path, host_version, host_api = (run/'host-ruby.tsv').read_text().strip().split('\t')
result = {'status':'PASS', 'scope':'real repository environment, not coordinator job execution',
    'haveapiRef':baseline['haveapiRef'], 'candidateRef':baseline['candidateRef'],
    'selectedPackage':baseline['selectedPackage'],
    'selectedWrapperSha256':baseline['selectedWrapperSha256'],
    'candidateExecutionSha256':baseline['candidateExecutionSha256'],
    'validationProgramSha256':baseline['validationProgramSha256'],
    'sourceArchiveSha256':baseline['sourceArchiveSha256'],
    'externalDependencySeed':dict(dependency_seed, originalLockUnchanged=True, snapshotLockUnchanged=True),
    'coordinatorHost':{'ruby':host_path,'version':host_version,'extensionApi':host_api},
    'repository':abi, 'declaredEnvironmentKeys':sorted(environment),
    'unchangedTrackedProductFiles':len(baseline['trackedFiles']),
    'unchangedOriginalSeedNativeFiles':len(baseline['seedNativeFiles']),
    'snapshot':str(run/'source')}
(run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
PY
