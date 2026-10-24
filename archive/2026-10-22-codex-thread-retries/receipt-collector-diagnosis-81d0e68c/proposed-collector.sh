#!/usr/bin/env bash
# PROPOSED ONLY: lead owns release and execution. No build/test/deployment.
set -u
set -o pipefail
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/vpsfree-cz-configuration
W=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/workspace
RUN=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/verification-build/composed-81d0e68c
GENERATION_DIR="$C/.confctl/generations/cz.vpsfree:machines:aitherdev/2026-10-22--22-16-53"
PREFIX="$RUN/system-build-receipt-recovered-81d0e68c"
NEW_RECEIPT_JSON="$PREFIX.json"
for suffix in json stdout stderr exit cwd elapsed source-after; do
  if test -e "$PREFIX.$suffix"; then
    echo "Refusing to overwrite prior recovery evidence: $PREFIX.$suffix" >&2
    exit 2
  fi
done
cd "$C" || exit 2
test "$(pwd -P)" = "$C" || exit 2
test -f "$C/Gemfile" || exit 2
test "$(git rev-parse HEAD)" = 81d0e68c52762d3804e00e4c4ef99a421bafc05f || exit 2
test -z "$(git status --porcelain)" || exit 2
printf '%s\n' "$(pwd -P)" > "$PREFIX.cwd"
started=$(date +%s)
# The shellHook banner stays in .stdout; only Ruby writes the .json artifact.
env   DEV_SESSION_SLUG=2026-10-22-codex-thread-retries   DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz   CONFCTL_TTY=0   BUNDLE_GEMFILE="$C/Gemfile"   BUNDLE_APP_CONFIG="$C/.bundle"   BUNDLE_PATH="$C/.gems"   C="$C" GENERATION_DIR="$GENERATION_DIR" NEW_RECEIPT_JSON="$NEW_RECEIPT_JSON"   nix develop "$C" -c bash --noprofile --norc -c '
    test "$(pwd -P)" = "$C" || exit 2
    exec ruby -rjson -rdigest - "$GENERATION_DIR" > "$NEW_RECEIPT_JSON"
  ' > "$PREFIX.stdout" 2> "$PREFIX.stderr" <<'RUBY'
dir = ARGV.fetch(0)
metadata_path = File.join(dir, 'generation.json')
g = JSON.parse(File.read(metadata_path))
abort 'not a flake generation' unless g.fetch('mode') == 'flakes'
top = g.fetch('toplevel')
abort 'toplevel link mismatch' unless File.realpath(File.join(dir, 'toplevel')) == File.realpath(top)
abort 'rollback link mismatch' unless File.realpath(File.join(dir, 'auto_rollback')) == File.realpath(g.fetch('auto_rollback'))
config_path = File.join(top, 'etc/confctl/configuration-info.json')
inputs_path = File.join(top, 'etc/confctl/inputs-info.json')
config = JSON.parse(File.read(config_path))
inputs = JSON.parse(File.read(inputs_path))
abort 'wrong or dirty configuration' unless config.fetch('schemaVersion') == 1 && config.fetch('revision') == '81d0e68c52762d3804e00e4c4ef99a421bafc05f' && config.fetch('revisionDirty') == false
abort 'input metadata mismatch' unless inputs == g.fetch('inputs_info')
abort 'wrong runtime' unless inputs.fetch('devWorkspace').fetch('rev') == 'd819ad044ef7fcc7bb4a111dc7676fe251383249'
puts JSON.pretty_generate({
  schema: 1, machine: 'cz.vpsfree/machines/aitherdev',
  generation: File.basename(dir), generationDirectory: dir,
  metadataSHA256: Digest::SHA256.file(metadata_path).hexdigest,
  configurationInfoSHA256: Digest::SHA256.file(config_path).hexdigest,
  inputsInfoSHA256: Digest::SHA256.file(inputs_path).hexdigest,
  metadata: g, configuration: config
})
RUBY
result=$?
finished=$(date +%s)
printf '%s\n' "$result" > "$PREFIX.exit"
printf '%s\n' "$((finished-started))" > "$PREFIX.elapsed"
# Read-only end-source comparison omitted by the failed original collector.
python3 - "$W" "$C" > "$PREFIX.source-after" <<'PY_SOURCE'
import hashlib,json,pathlib,subprocess,sys
expected=[('workspace','ebf6ab35c7754f9ac2e5474959259fdcef24a7c8','e46dfa5027a2e34cc083e6d41da78f7c60106d3e','bc2c2f8bb547154214645142108a986b3f45171ae33edd2e95cf9e9959a2c80d'),('configuration','81d0e68c52762d3804e00e4c4ef99a421bafc05f','27b3b4425c9104269b5909a5d935eb94c6c954df','ccf709ff6eb0cc34bb2e3ffeacb1b2d3d2069faef43d361abf606b378f087574')]
records=[]
for location,(name,head,tree,locksha) in zip(sys.argv[1:],expected):
 p=pathlib.Path(location)
 git=lambda *args:subprocess.check_output(['git',*args],cwd=p,text=True).strip()
 actual={'name':name,'cwd':location,'head':git('rev-parse','HEAD'),'tree':git('rev-parse','HEAD^{tree}'),'status':git('status','--porcelain'),'lockSHA256':hashlib.sha256((p/'flake.lock').read_bytes()).hexdigest()}
 assert actual['head']==head and actual['tree']==tree and actual['status']=='' and actual['lockSHA256']==locksha,actual
 records.append(actual)
print(json.dumps(records,indent=2))
PY_SOURCE
source_result=$?
if test "$result" -ne 0; then exit "$result"; fi
exit "$source_result"
