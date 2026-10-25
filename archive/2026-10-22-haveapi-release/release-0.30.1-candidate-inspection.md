# HaveAPI 0.30.1 candidate inspection package

Prepared by implementer3; **not executed**. No new tag-run artifact exists at this
checkpoint. The lead must first hand off the successful original annotated-tag
run, exact source, attempt, build job, artifact ID/digest and utility slot. Every
future identifier below remains unset. This package neither approves the
protected environment nor establishes publication success.

Authority: [release plan](release-0.30.1-plan.md). Binding and live roster checked:
session `2026-10-22-haveapi-release`, workspace
`/home/aither/workspace/ai/vpsfree.cz`, implementer3 workspace_write, retained
gpt-6.1-sol/xhigh, installed full_access. Read HaveAPI AGENTS and full release,
development and Rust packaging instructions from the same session's read-only
090a source; the future patch worktree does not yet exist. Recheck the final
source's instructions and unchanged helper behavior at handoff.

## Later execution handoff

Resolve a **fresh** watcher from the retained catalog's verification utility and
current installed execution policy. Current policy is gpt-6-luna/low, native
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, full_access with explicit
danger-full-access/approval never. Read effective thread turn_context/launch
settings, not the user's base config, to establish model, effort and policy.
The watcher reports its actual thread/readiness before execution and owns the
single operation, tool handle, full outer log, exit and timing. No nested agent,
diagnosis, retry, repair, setup, smoke check or compilation is delegated.

Fresh absolute guidance paths:

- `/home/aither/.codex/skills/dev-session-monitor/SKILL.md`
- `/home/aither/workspace/ai/vpsfree.cz/AGENTS.md`
- `/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/sessions.md`
- `/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/verification.md`
- `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/release-0.30.1-plan.md`
- Final yielded `$CANDIDATE_SOURCE/AGENTS.md`,
  `$CANDIDATE_SOURCE/doc/agent-instructions/releases.md`,
  `$CANDIDATE_SOURCE/doc/agent-instructions/development.md` and
  `$CANDIDATE_SOURCE/clients/rust/docs/releasing.md`, expanded to absolute paths
  and read before launch.

Owner0 supplies these exact values after tagged build success; none may be
inferred from a branch build or the 0.30.0 artifact:

```sh
export CANDIDATE_SOURCE=''          # final registered absolute patch worktree
export CANDIDATE_COMMIT=''          # exact reviewed tagged commit, full SHA
export CANDIDATE_TAG_OBJECT=''      # annotated v0.30.1 tag object, full SHA
export CANDIDATE_RUN=''             # NEW original release.yml tag run ID
export CANDIDATE_ATTEMPT=''         # attempt that actually built/uploaded it
export CANDIDATE_BUILD_JOB=''       # successful Validate, test and build job ID
export CANDIDATE_ARTIFACT=''        # original release-<run> Actions artifact ID
export CANDIDATE_DIGEST=''          # Actions sha256:<64 hex> archive digest
```

Use the prepared command below only after the lead's explicit execution grant.
Wrap its one invocation with full stdout/stderr, exact exit, UTC/monotonic timing
and actual utility identity. A first failure stops; retain its directory and
all partial files. No re-download, alternate artifact, rerun or source edit.

## Exact command package

Run from the workspace root. The only network requests are exact GitHub GETs
for the handed-off tag/run/job/artifact and its logs/archive. No discovery loop,
registry polling, Actions mutation, environment approval or credential reading.

```bash
set -euo pipefail
cd /home/aither/workspace/ai/vpsfree.cz
test "$(dev-session current)" = 2026-10-22-haveapi-release
if [[ -v DEV_SESSION_SLUG || -v DEV_SESSION_WORKSPACE ]]; then
  test "${DEV_SESSION_SLUG-}" = 2026-10-22-haveapi-release
  test "${DEV_SESSION_WORKSPACE-}" = /home/aither/workspace/ai/vpsfree.cz
fi
: "${CANDIDATE_SOURCE:?}" "${CANDIDATE_COMMIT:?}" "${CANDIDATE_TAG_OBJECT:?}"
: "${CANDIDATE_RUN:?}" "${CANDIDATE_ATTEMPT:?}" "${CANDIDATE_BUILD_JOB:?}"
: "${CANDIDATE_ARTIFACT:?}" "${CANDIDATE_DIGEST:?}"
[[ "$CANDIDATE_SOURCE" = /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/* ]]
[[ "$CANDIDATE_COMMIT" =~ ^[0-9a-f]{40}$ && "$CANDIDATE_TAG_OBJECT" =~ ^[0-9a-f]{40}$ ]]
[[ "$CANDIDATE_RUN" =~ ^[0-9]+$ && "$CANDIDATE_ATTEMPT" =~ ^[0-9]+$ ]]
[[ "$CANDIDATE_BUILD_JOB" =~ ^[0-9]+$ && "$CANDIDATE_ARTIFACT" =~ ^[0-9]+$ ]]
[[ "$CANDIDATE_DIGEST" =~ ^sha256:[0-9a-f]{64}$ ]]
test "$(git -C "$CANDIDATE_SOURCE" rev-parse HEAD)" = "$CANDIDATE_COMMIT"
git -C "$CANDIDATE_SOURCE" diff --quiet
git -C "$CANDIDATE_SOURCE" diff --cached --quiet
test "$(cat "$CANDIDATE_SOURCE/VERSION")" = 0.30.1

export CANDIDATE_EVIDENCE="/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/release-0.30.1-$CANDIDATE_RUN"
test ! -e "$CANDIDATE_EVIDENCE"
mkdir "$CANDIDATE_EVIDENCE"
mkdir "$CANDIDATE_EVIDENCE/original-artifacts"
gh api "repos/vpsfreecz/haveapi/git/ref/tags/v0.30.1" > "$CANDIDATE_EVIDENCE/tag-ref.json"
gh api "repos/vpsfreecz/haveapi/git/tags/$CANDIDATE_TAG_OBJECT" > "$CANDIDATE_EVIDENCE/tag-object.json"
gh api "repos/vpsfreecz/haveapi/actions/runs/$CANDIDATE_RUN/attempts/$CANDIDATE_ATTEMPT" > "$CANDIDATE_EVIDENCE/run-attempt.json"
gh api --paginate --slurp "repos/vpsfreecz/haveapi/actions/runs/$CANDIDATE_RUN/attempts/$CANDIDATE_ATTEMPT/jobs?per_page=100" > "$CANDIDATE_EVIDENCE/jobs.json"
gh api "repos/vpsfreecz/haveapi/actions/artifacts/$CANDIDATE_ARTIFACT" > "$CANDIDATE_EVIDENCE/artifact.json"

python3 - <<'PY'
import json, os, pathlib, subprocess
e = pathlib.Path(os.environ['CANDIDATE_EVIDENCE'])
get = lambda name: json.loads((e / name).read_text())
commit = os.environ['CANDIDATE_COMMIT']
tag = get('tag-ref.json')['object']
assert tag['type'] == 'tag' and tag['sha'] == os.environ['CANDIDATE_TAG_OBJECT']
annotated = get('tag-object.json')
assert annotated['tag'] == 'v0.30.1' and annotated['sha'] == tag['sha']
assert annotated['object']['type'] == 'commit' and annotated['object']['sha'] == commit
run = get('run-attempt.json')
assert str(run['id']) == os.environ['CANDIDATE_RUN']
assert str(run['run_attempt']) == os.environ['CANDIDATE_ATTEMPT']
assert run['event'] == 'push' and run['head_sha'] == commit and run['head_branch'] == 'v0.30.1'
assert run['path'] == '.github/workflows/release.yml'
jobs = [job for page in get('jobs.json') for job in page['jobs']]
matches = [job for job in jobs if str(job['id']) == os.environ['CANDIDATE_BUILD_JOB']]
assert len(matches) == 1
job = matches[0]
assert job['name'] == 'Validate, test and build' and job['head_sha'] == commit
assert str(job['run_id']) == os.environ['CANDIDATE_RUN']
assert str(job['run_attempt']) == os.environ['CANDIDATE_ATTEMPT']
assert job['status'] == 'completed' and job['conclusion'] == 'success'
for name in ['Test and build maintained packages', 'Retain release artifacts',
             'Verify retained artifacts', 'Summarize candidate release']:
    steps = [step for step in job['steps'] if step['name'] == name]
    assert len(steps) == 1 and steps[0]['conclusion'] == 'success', name
artifact = get('artifact.json')
assert str(artifact['id']) == os.environ['CANDIDATE_ARTIFACT']
assert artifact['name'] == 'release-' + os.environ['CANDIDATE_RUN'] and not artifact['expired']
assert artifact['digest'] == os.environ['CANDIDATE_DIGEST']
assert str(artifact['workflow_run']['id']) == os.environ['CANDIDATE_RUN']
assert artifact['workflow_run']['head_sha'] == commit
root = pathlib.Path(os.environ['CANDIDATE_SOURCE'])
paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
import hashlib
hashes = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in paths if name}
(e / 'source-before.json').write_text(json.dumps(hashes, indent=2, sort_keys=True) + '\n')
PY

gh api "repos/vpsfreecz/haveapi/actions/jobs/$CANDIDATE_BUILD_JOB/logs" > "$CANDIDATE_EVIDENCE/build-job.log"
gh api "repos/vpsfreecz/haveapi/actions/artifacts/$CANDIDATE_ARTIFACT/zip" > "$CANDIDATE_EVIDENCE/original-artifact.zip"
python3 - <<'PY'
import hashlib, json, os, pathlib, stat, zipfile
e = pathlib.Path(os.environ['CANDIDATE_EVIDENCE'])
archive = e / 'original-artifact.zip'
assert 'sha256:' + hashlib.sha256(archive.read_bytes()).hexdigest() == os.environ['CANDIDATE_DIGEST']
with zipfile.ZipFile(archive) as z:
    entries = z.infolist()
    assert len({i.filename for i in entries}) == len(entries)
    for i in entries:
        assert i.filename not in ['', '.', '..'] and pathlib.PurePosixPath(i.filename).name == i.filename
        assert not i.is_dir() and not stat.S_ISLNK(i.external_attr >> 16)
        (e / 'original-artifacts' / i.filename).write_bytes(z.read(i))
manifest = json.loads((e / 'original-artifacts/release-manifest.json').read_text())
assert [manifest[k] for k in ['schema', 'source', 'version', 'tag']] == [1, os.environ['CANDIDATE_COMMIT'], '0.30.1', 'v0.30.1']
assert str(manifest['run_id']) == os.environ['CANDIDATE_RUN']
assert set(manifest['tools']) == set('ruby gem node npm go php composer python uv cargo rustc rustfmt'.split())
assert all(isinstance(v, str) and v.strip() for v in manifest['tools'].values())
root = pathlib.Path(os.environ['CANDIDATE_SOURCE'])
tracked = json.loads((e / 'source-before.json').read_text())
locks = manifest['dependency_locks']
expected = ['Gemfile.lock', 'servers/ruby/Gemfile.lock', 'clients/ruby/Gemfile.lock',
            'clients/go/Gemfile.lock', 'clients/rust/Gemfile.lock', 'clients/rust/runtime/Cargo.lock',
            'clients/js/package-lock.json', 'clients/php/composer.lock', 'clients/python/uv.lock']
assert set(locks) == set(expected)
for name, content in locks.items():
    assert isinstance(content, str) and content.strip()
    if name in tracked:
        assert content.encode() == (root / name).read_bytes(), name
lock_hashes = {name: hashlib.sha256(content.encode()).hexdigest() for name, content in locks.items()}
(e / 'manifest-lock-sha256.json').write_text(json.dumps(lock_hashes, indent=2, sort_keys=True) + '\n')
lines = (e / 'build-job.log').read_text().splitlines()
(e / 'build-warning-inventory.txt').write_text('\n'.join(line for line in lines if 'warning' in line.lower() or 'deprecated' in line.lower()) + '\n')
PY

cd "$CANDIDATE_SOURCE"
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --no-write-lock-file --command ruby utils/release/cli.rb verify "$CANDIDATE_EVIDENCE/original-artifacts" > "$CANDIDATE_EVIDENCE/local-verify.log" 2>&1
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --no-write-lock-file --command ruby -I utils/release -r artifacts -r digest -r json -e '
  artifacts = HaveAPI::Release::Artifacts.new(Dir.pwd)
  directory = File.join(ENV.fetch("CANDIDATE_EVIDENCE"), "original-artifacts")
  expected = artifacts.names + ["release-manifest.json"]
  raise "Unexpected Actions-only files; retain and refer through lead" unless Dir.children(directory).sort == expected.sort
  gems = HaveAPI::Release::GEMS.keys.to_h do |name|
    package = Gem::Package.new(File.join(directory, "#{name}-#{artifacts.version}.gem"))
    [name, {version: package.spec.version.to_s, platform: package.spec.platform.to_s,
            required_ruby: package.spec.required_ruby_version.to_s,
            runtime_dependencies: package.spec.runtime_dependencies.to_h { |dep| [dep.name, dep.requirement.as_list] },
            contents: package.contents.sort}]
  end
  rust = Gem::Package.new(File.join(directory, "haveapi-rust-client-#{artifacts.version}.gem"))
  fiddle = rust.spec.runtime_dependencies.select { |dep| dep.name == "fiddle" }
  raise "Unexpected Fiddle requirement" unless fiddle.length == 1 && fiddle.first.requirement == Gem::Requirement.new("~> 1.1", ">= 1.1.8")
  raise "Unexpected Ruby requirement" unless rust.spec.required_ruby_version == Gem::Requirement.new(">= 3.2")
  output = {gems: gems, public_files: expected,
            rust_runtime_files: gems.fetch("haveapi-rust-client").fetch(:contents).grep(%r{\Aruntime/src/runtime/}),
            notes_equal_source: File.binread(File.join(directory, "release-notes.md")) == artifacts.notes}
  raise "Release notes differ from source" unless output[:notes_equal_source]
  File.write(File.join(ENV.fetch("CANDIDATE_EVIDENCE"), "package-inspection.json"), JSON.pretty_generate(output) + "\n")
' > "$CANDIDATE_EVIDENCE/package-inspection.log" 2>&1
git diff --quiet
git diff --cached --quiet
test "$(git rev-parse HEAD)" = "$CANDIDATE_COMMIT"
python3 - <<'PY'
import hashlib, json, os, pathlib, subprocess
e = pathlib.Path(os.environ['CANDIDATE_EVIDENCE'])
root = pathlib.Path(os.environ['CANDIDATE_SOURCE'])
before = json.loads((e / 'source-before.json').read_text())
assert all(hashlib.sha256((root / p).read_bytes()).hexdigest() == digest for p, digest in before.items())
paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
assert {p for p in paths if p} == set(before)
hashes = {p.relative_to(e).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(e.rglob('*')) if p.is_file()}
(e / 'retained-sha256.json').write_text(json.dumps(hashes, indent=2, sort_keys=True) + '\n')
PY
```

The helper's `verify` path reads/extracts package metadata and compares Rust
packaged source with the exact checkout. It does not install/import the retained
generator, run npm/Python consumers or compile Rust. Do not invoke `manifest`,
`smoke-npm`, `rust_smoke.rb`, `github-prepare`, `pypi-prepare` or `publish`.
Keep temporary inspection extraction within an operation-owned TMPDIR if later
granted; do not clean existing session/component caches. Resolved untracked lock
contents in the manifest are retained as build evidence, without claiming they
equal separately resolved local bundles. Tracked lock bytes must match source.

An unexpected extra Actions-only receipt is preserved and referred through lead;
it is never silently discarded or added to the eleven public assets. No such
extra filename is assumed in advance. Publication safeguards and destination
checks remain with owners2/1; build success is not publication evidence.

## Concise approval packet after execution

Provide the lead a candidate receipt linking the original tagged run/attempt,
successful build job/full log and warning inventory; annotated tag object and
commit; artifact ID/name/digest and retained ZIP SHA-256; manifest SHA-256,
source/version/run identity, tools and nine lock hashes; package identities and
dependencies, Fiddle requirement and embedded Rust runtime inventory; all eleven
catalog/manifest file hashes and any separately authorized Actions-only receipt.
Link owner0's final review/equivalence and automatic-CI reconciliation evidence.
State whether every inspection passed, any remaining unknown, and that protected
candidate approval remains with the lead. Never label a prepared packet approved.

After the wrapper exits, retain its exact exit/timing/readiness metadata and hash
the closed outer log and result files too; append that final inventory to the
candidate receipt. Do not hash an actively written outer log as final evidence.

Preparation checks: shell block, three embedded Python blocks and the Ruby
metadata snippet pass syntax checks only. No GitHub request, Nix evaluation,
artifact download, local package verification, install, build or registry action.
Existing 0.30.0/followup artifacts and downstream crate copies remain untouched.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
