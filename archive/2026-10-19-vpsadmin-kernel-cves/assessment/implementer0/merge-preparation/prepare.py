import datetime, hashlib, json, os, shutil, subprocess, sys, uuid
from pathlib import Path

OUT = Path(__file__).parent
OWNER = OUT.parent
SESSION = OWNER.parents[1]
WORKSPACE = SESSION.parents[1]
HEAD = 'e6ceb642878dd97546174217676d9861afc38d4e'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
SOURCE = 'aa15ba719513d54c1e7942a085504777e4b7abfd'
BRANCH = '2026-10-19-vpsadmin-kernel-cves'
DEFAULT = '2026-07-13-security-advisory-automation'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
PACKAGE = Path('/nix/store/1i1g6rp8ind51qqayzpww7cn1xp1k1gq-dev-workspace-0.2.0')
RESUME = '--resume-admission' in sys.argv

def git(*args): return subprocess.check_output(['git', *args])
def value(*args): return git(*args).decode().strip()
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, data): (OUT / name).write_text(json.dumps(data, indent=2) + '\n')
def operation(name, args):
    r = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(r.stdout + r.stderr)
    assert r.returncode == 0, f'{name} exit{r.returncode}; stop and report, no retry'
    return r.stdout
def local_refs(): return dict(line.split('\t') for line in value('for-each-ref', '--format=%(refname)\t%(objectname)').splitlines() if not line.startswith('refs/remotes/'))

assert os.environ.get('IN_NIX_SHELL')
assert value('rev-parse', 'HEAD') == HEAD and value('branch', '--show-current') == BRANCH
assert value('remote', 'get-url', 'origin') == value('remote', 'get-url', '--push', 'origin') == 'git@github.com:vpsfreecz/security-advisories.git'
assert Path(shutil.which('dev-session')).resolve() == PACKAGE / 'bin/dev-session'
catalog_path = PACKAGE / 'share/dev-workspace/coordination.json'
catalog = json.loads(catalog_path.read_text())
mapping = catalog['repositories']['security-advisories']
assert mapping == {'defaultTarget': 'refs/heads/' + DEFAULT, 'remote': 'git@github.com:vpsfreecz/security-advisories.git'}
prior = OWNER / 'editorial-final-publication'
publication = json.loads((prior / 'publication-receipt.json').read_text())
assert publication['head'] == HEAD
refs = local_refs()
baseline = json.loads((prior / 'baseline-integrity.json').read_text())['final']
assert len(baseline) == 111
def invariants():
    assert value('rev-parse', 'HEAD') == HEAD
    assert not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
    assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
    assert all(sha(Path(path).read_bytes()) == digest for path, digest in baseline.items())
    current = local_refs()
    assert all(current.get(ref) == digest for ref, digest in refs.items())
invariants()
inventory = {}
for name, metadata in publication['inventory'].items():
    raw = (prior / name).read_bytes()
    assert sha(raw) == metadata['sha256'] and git(*metadata['git_args']) == raw
    inventory[name] = {**metadata, 'actual_git_byte_match': True, 'path': str(prior / name)}
series = value('rev-list', '--reverse', BASE + '..' + HEAD).splitlines()
assert len(series) == 81 and value('rev-list', '--count', '--merges', BASE + '..' + HEAD) == '0'
boundaries = json.loads((prior / 'all69-boundary-proof.json').read_text())
assert len(boundaries) == 69
assert all(row['checkpoint_sha'] in series and value('rev-parse', row['checkpoint_sha'] + '^') == row['source_commit'] for row in boundaries)
authorization = SESSION / 'assessment/publication-and-merge-user-authorization.json'
approval = json.loads(authorization.read_text())
assert approval['merge']['approved_feature_head'] == HEAD
assert approval['merge']['repository'] == 'security-advisories' and approval['merge']['target'] == 'refs/heads/' + DEFAULT
reviews = [SESSION / 'assessment/editorial-review-result.md', SESSION / 'assessment/editorial-final-history-review-result.md']
assert all('NO FINDINGS' in path.read_text() for path in reviews)
ci = []
for name, commit in [('source', SOURCE), ('final', HEAD)]:
    receipt = SESSION / ('assessment/editorial-' + name + '-ci-result.json')
    stored = json.loads(receipt.read_text())
    assert stored['result'] == 'PASS' and stored['head'] == commit
    assert all(row['headSha'] == commit and row['status'] == 'completed' and row['conclusion'] == 'success' for row in stored['runs'])
    actual = json.loads((OUT / (name + '-ci-current.log')).read_text()) if RESUME else json.loads(operation(name + '-ci-current', ['gh', 'run', 'list', '--repo', 'vpsfreecz/security-advisories', '--branch', BRANCH, '--commit', commit, '--limit', '20', '--json', 'databaseId,url,status,conclusion,headSha,name']))
    assert {row['name'] for row in actual} >= {'RSpec', 'RuboCop'}
    assert all(row['headSha'] == commit and row['status'] == 'completed' and row['conclusion'] == 'success' for row in actual)
    ci.append({'scope': name, 'head': commit, 'runs': actual, 'retained_receipt': str(receipt), 'retained_sha256': sha(receipt.read_bytes())})
if not RESUME:
    operation('fetch', ['git', 'fetch', 'origin'])
remote_text = (OUT / 'remote-current.log').read_text() if RESUME else operation('remote-current', ['git', 'ls-remote', '--symref', 'origin', 'HEAD', 'refs/heads/' + DEFAULT, 'refs/heads/' + BRANCH])
remote = dict((ref, digest) for digest, ref in (line.split('\t') for line in remote_text.splitlines() if '\t' in line and not line.startswith('ref:')))
assert 'ref: refs/heads/' + DEFAULT + '\tHEAD' in remote_text
assert remote['HEAD'] == remote['refs/heads/' + DEFAULT] == BASE, remote
assert remote['refs/heads/' + BRANCH] == HEAD, remote
assert value('rev-parse', 'refs/remotes/origin/' + DEFAULT) == BASE and value('rev-parse', 'refs/remotes/origin/' + BRANCH) == HEAD
subprocess.run(['git', 'merge-base', '--is-ancestor', BASE, HEAD], check=True)
invariants()
if RESUME:
    shutil.copyfile(OUT / 'capture-comparison.log', OUT / 'capture-admission-contention.log')
capture = operation('capture-comparison', ['dev-session', 'worktree', 'capture-comparison', BRANCH, 'security-advisories', '--as-is'])
invariants()
evidence = {'schema': 1, 'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'repository': 'security-advisories', 'target': 'refs/heads/' + DEFAULT, 'head': HEAD, 'expected_remote_target': BASE, 'source_and_final_CI': ci, 'review_artifacts': [{'path': str(path), 'sha256': sha(path.read_bytes())} for path in reviews], 'reviewed81_inventory_actual_git_byte_proof': inventory, 'migration_conclusion': 'NO migrations; accepted full81 history retained; all69 externally consumed recovery boundaries and source parents immutable', 'all111_submission_hashes_preserved': True, 'frozen_evidence_sha256': EVIDENCE, 'whole_clean': True, 'index_empty': True, 'remote': remote, 'catalog': {'path': str(catalog_path), 'sha256': sha(catalog_path.read_bytes()), 'mapping': mapping}, 'selected_runtime': str(PACKAGE), 'catalog_covered': True, 'route': 'documented individual prepare, later approve+submit after lead release; merge-only; no machine reservation', 'guide_mismatch': 'Installed integration.md and guide entry absent; lead authorized documented individual route; no driver invocation or bypass.', 'user_authorization': {'path': str(authorization), 'sha256': sha(authorization.read_bytes()), 'quote': 'and merge the changes'}, 'comparison_capture': capture, 'no_merge_or_default_push_submitted': True}
save('integration-evidence.json', evidence)
request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': 'merge', 'repository': 'security-advisories', 'evidence': [{'kind': 'review', 'path': str(OUT / 'integration-evidence.json'), 'sha256': sha((OUT / 'integration-evidence.json').read_bytes())}]}
save('prepare-request.json', request)
print('Preparation evidence PASS: no drift, reviewed81/all69/all111/frozen61904, both source/final CI success; coordinator prepare only next.', flush=True)
reply = json.loads(operation('coordinator-prepare', ['dev-session', 'coordination', 'prepare', BRANCH, '--as-is', '--request', str(OUT / 'prepare-request.json'), '--json']))
save('coordinator-prepare-receipt.json', reply)
invariants()
save('preparation-receipt.json', {'schema': 1, 'head': HEAD, 'base': BASE, 'prepared': reply, 'evidence_path': str(OUT / 'integration-evidence.json'), 'evidence_sha256': sha((OUT / 'integration-evidence.json').read_bytes()), 'remote': remote, 'whole_clean': True, 'index_empty': True, 'all_refs_preserved': True, 'submitted': False, 'approved_in_coordinator': False, 'default_unchanged': True, 'slot_returned_to': 'lead', 'next_action': 'Lead release then ordinary approval+submission of exact returned snapshot; no reservation/deployment/email/lifecycle.'})
print(json.dumps({'head': HEAD, 'target': 'refs/heads/' + DEFAULT, 'remote_target': BASE, 'prepared_not_submitted': True, 'receipt': str(OUT / 'preparation-receipt.json'), 'coordinator': reply}, indent=2), flush=True)
