import datetime, hashlib, json, os, re, subprocess
from pathlib import Path

OUT = Path(__file__).parent
OWNER = OUT.parent
SYNC = OWNER.parent / 'implementer1/draft-sync'
HEAD = 'e6ceb642878dd97546174217676d9861afc38d4e'
SOURCE = 'aa15ba719513d54c1e7942a085504777e4b7abfd'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
BRANCH = '2026-10-19-vpsadmin-kernel-cves'
DEFAULT = '2026-07-13-security-advisory-automation'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
LEDGER_SHA = '68997dd8a6f0cbc78cd77bb920b8d86ae26690526deacab2297ffeee24f382d8'
CHECKPOINTS = ['fc370709eba0c410d5bff9e73ec1fdb075c28361', '8cfb2f7140bde43a1e05ec99deb59b6469d52452', HEAD]
CVES = ['CVE-2026-53260', 'CVE-2026-72069', 'CVE-2026-64387']
PATHS = {f'advisories/{cve}/submission.yml' for cve in CVES}

def git(*args): return subprocess.check_output(['git', *args])
def value(*args): return git(*args).decode().strip()
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, data): (OUT / name).write_text(json.dumps(data, indent=2) + '\n')
def operation(name, args):
    r = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(r.stdout + r.stderr)
    assert r.returncode == 0, f'{name} exit{r.returncode}; stop without retry'
    return r.stdout
def fields(commit, path): return dict(re.findall(r'^([a-z_]+): (.*)$', value('show', commit + ':' + path), re.M))
def local_refs(): return dict(line.split('\t') for line in value('for-each-ref', '--format=%(refname)\t%(objectname)').splitlines() if not line.startswith('refs/remotes/'))

assert os.environ.get('IN_NIX_SHELL')
assert value('rev-parse', 'HEAD') == HEAD and value('branch', '--show-current') == BRANCH
assert value('remote', 'get-url', 'origin') == value('remote', 'get-url', '--push', 'origin') == 'git@github.com:vpsfreecz/security-advisories.git'
assert sha((SYNC / 'editorial-ledger.json').read_bytes()) == LEDGER_SHA
ledger = json.loads((SYNC / 'editorial-ledger.json').read_text())
completion = json.loads((SYNC / 'editorial-completion.json').read_text())
assert completion['released_source_head'] == SOURCE and completion['final_head'] == HEAD
assert completion['checkpoint_shas'] == CHECKPOINTS
assert completion['content_revisions'] == [17, 17, 27] and completion['draft_ids'] == [112, 113, 106]
assert ledger['count'] == len(ledger['rows']) == 3
prefix = [line.split('\t')[0] for line in (OWNER / 'editorial-source-publication/complete78-series.tsv').read_text().splitlines()]
series = value('rev-list', '--reverse', BASE + '..' + HEAD).splitlines()
assert len(prefix) == 78 and len(series) == 81 and series[:-3] == prefix and series[-3:] == CHECKPOINTS
assert value('rev-list', '--count', '--merges', BASE + '..' + HEAD) == '0'
assert set(value('diff', '--name-only', SOURCE, HEAD).splitlines()) == PATHS
checkpoints = []
for i, (cve, row, commit) in enumerate(zip(CVES, ledger['rows'], CHECKPOINTS)):
    parent = value('rev-parse', commit + '^')
    assert parent == (SOURCE if i == 0 else CHECKPOINTS[i - 1])
    assert row['cve'] == cve and row['checkpoint_sha'] == commit and row['state'] == 'draft'
    path = f'advisories/{cve}/submission.yml'
    assert value('diff-tree', '--no-commit-id', '--name-status', '-r', commit) == 'M\t' + path
    data = fields(commit, path)
    assert data['schema_version'] == '2' and data['source_commit'] == parent
    assert int(data['advisory_id']) == row['advisory_id'] and int(data['remote_content_revision']) == row['content_revision']
    evaluation = json.loads(Path(f'advisories/{cve}/evaluation.json').read_text())
    assert data['dossier_digest'] == evaluation['dossier_digest'] and row['node_counts'] == evaluation['completeness']['states']
    checkpoints.append({**row, 'actual_parent': parent, 'source_commit': parent, 'path': path, 'submission_sha256': sha(git('show', commit + ':' + path))})

prior_path = OWNER / 'operator-period-final-publication/all66-boundary-proof.json'
prior_receipt = json.loads((prior_path.parent / 'publication-receipt.json').read_text())
assert sha(prior_path.read_bytes()) == prior_receipt['evidence_artifact_sha256']['all66-boundary-proof.json']
prior = json.loads(prior_path.read_text())
assert len(prior) == 66
for row in prior:
    commit = row['checkpoint_sha']
    assert commit in prefix and value('rev-parse', commit + '^') == row['source_commit']
    data = fields(commit, f'advisories/{row["cve"]}/submission.yml')
    assert data['source_commit'] == row['source_commit']
    assert int(data['advisory_id']) == row['advisory_id'] and int(data['remote_content_revision']) == row['content_revision']
assert len({row['checkpoint_sha'] for row in prior + checkpoints}) == 69
approved = json.loads((SYNC / 'ledger.json').read_text())['rows']
assert len(approved) == 60 and len({row['cve'] for row in approved} - set(CVES)) == 57
old_baselines = json.loads((OWNER / 'operator-period-final-publication/baseline-integrity.json').read_text())['final']
final_baselines = {str(path): sha(path.read_bytes()) for path in Path('advisories').glob('*/submission.yml')}
assert len(old_baselines) == 111 and set(old_baselines) == set(final_baselines)
unchanged = {path: digest for path, digest in old_baselines.items() if path not in PATHS}
assert len(unchanged) == 108 and all(final_baselines[path] == digest for path, digest in unchanged.items())
refs_before = local_refs()
def invariants():
    assert value('rev-parse', 'HEAD') == HEAD
    assert not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
    assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
    assert all(sha(Path(path).read_bytes()) == digest for path, digest in final_baselines.items())
    refs = local_refs()
    assert all(refs.get(name) == digest for name, digest in refs_before.items())
invariants()
for key in ['OVERCOMMIT_DISABLE', 'SKIP', 'ONLY', 'OVERCOMMIT_UNSAFE']: assert not os.environ.get(key), key
hook = Path(value('rev-parse', '--git-path', 'hooks/pre-push'))
assert hook.is_file() and os.access(hook, os.X_OK) and 'overcommit' in hook.read_text().lower()
artifacts = {
    'complete81-series.tsv': ['log', '--reverse', '--format=%H%x09%P%x09%aI%x09%s', BASE + '..' + HEAD],
    'complete81-final.diff': ['diff', '--full-index', '--binary', BASE, HEAD],
    'complete81-final.stat': ['diff', '--stat', BASE, HEAD],
    'complete81-final.paths': ['diff', '--name-status', BASE, HEAD],
    'complete81-final.numstat': ['diff', '--numstat', BASE, HEAD],
    'three-checkpoint-series.tsv': ['log', '--reverse', '--format=%H%x09%P%x09%s', SOURCE + '..' + HEAD],
    'three-checkpoint.diff': ['diff', '--full-index', '--binary', SOURCE, HEAD],
    'three-checkpoint.stat': ['diff', '--stat', SOURCE, HEAD],
    'three-checkpoint.paths': ['diff', '--name-status', SOURCE, HEAD],
    'three-checkpoint.numstat': ['diff', '--numstat', SOURCE, HEAD],
}
manifest = {}
for name, args in artifacts.items():
    raw = git(*args); (OUT / name).write_bytes(raw)
    manifest[name] = {'sha256': sha(raw), 'bytes': len(raw), 'git_args': args}
operation('complete-diff-check', ['git', 'diff', '--check', BASE, HEAD])
operation('bounded-diff-check', ['git', 'diff', '--check', SOURCE, HEAD])
save('three-checkpoint-inventory.json', checkpoints)
save('prior66-boundary-proof.json', prior)
save('all69-boundary-proof.json', prior + checkpoints)
save('baseline-integrity.json', {'source': old_baselines, 'final': final_baselines, 'unchanged108': unchanged, 'other57_approved_baselines_unchanged': True})
save('inventory-manifest.json', manifest)
save('local-refs-before.json', refs_before)
preflight = {'head': HEAD, 'source': SOURCE, 'base': BASE, 'complete_commits': 81, 'unchanged_consumed_prefix': 78, 'all69_actual_parent_boundaries_preserved': True, 'source_unchanged_except_three_baselines': True, 'other108_and57_baselines_unchanged': True, 'editorial_ledger_sha256': LEDGER_SHA, 'frozen_evidence_sha256': EVIDENCE, 'whole_worktree_clean': True, 'index_empty': True}
save('preflight.json', preflight)
print('INVENTORY PASS: complete81, consumed78,69actualparents,108/57unrelated,frozen61904. SSHfetch next.', flush=True)
operation('fetch', ['git', 'fetch', 'origin'])
def remote(name):
    text = operation(name, ['git', 'ls-remote', '--symref', 'origin', 'HEAD', 'refs/heads/' + DEFAULT, 'refs/heads/' + BRANCH])
    refs = dict((ref, digest) for digest, ref in (line.split('\t') for line in text.splitlines() if '\t' in line and not line.startswith('ref:')))
    assert 'ref: refs/heads/' + DEFAULT + '\tHEAD' in text
    assert refs['HEAD'] == refs['refs/heads/' + DEFAULT] == BASE, refs
    return refs
before = remote('remote-before')
assert before['refs/heads/' + BRANCH] == SOURCE
assert value('rev-parse', 'refs/remotes/origin/' + DEFAULT) == BASE and value('rev-parse', 'refs/remotes/origin/' + BRANCH) == SOURCE
invariants()
print('Remote preconditionsPASS: defaultea624/featureaa15. NormalfeatureFFpush now.', flush=True)
operation('push', ['git', 'push', 'origin', 'refs/heads/' + BRANCH + ':refs/heads/' + BRANCH])
after = remote('remote-after'); assert after['refs/heads/' + BRANCH] == HEAD
assert value('rev-parse', 'refs/remotes/origin/' + BRANCH) == HEAD
invariants(); save('local-refs-after.json', local_refs())
ci_args = ['gh', 'run', 'list', '--repo', 'vpsfreecz/security-advisories', '--branch', BRANCH, '--commit', HEAD, '--limit', '20', '--json', 'databaseId,url,status,conclusion,headSha,name,event,workflowName,createdAt']
runs = json.loads(operation('ci-run-list', ci_args)); assert all(row['headSha'] == HEAD for row in runs)
save('ci-runs.json', runs)
receipt = {**preflight, 'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'normal_owned_Nix_SSH_fetch_feature_only_FFpush': 'PASS; active hooks, no bypass', 'remote_before': before, 'remote_after': after, 'all_local_refs_preserved': True, 'all111_final_baselines_unchanged_during_publication': True, 'inventory': manifest, 'new_three_checkpoints': checkpoints, 'ci_runs': runs, 'CI_waited': False, 'slot_returned_to': 'lead', 'no_operations': ['advisoryAPI', 'sourcechanges', 'tests', 'reevaluation', 'recollection', 'rewrite', 'defaultmerge', 'PR', 'lifecycle'], 'session_url': 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
save('publication-receipt.json', receipt)
print(json.dumps({'head': HEAD, 'remote_exact': True, 'clean': True, 'index_empty': True, 'complete_commits': 81, 'ci_runs': runs, 'receipt': str(OUT / 'publication-receipt.json')}, indent=2), flush=True)
