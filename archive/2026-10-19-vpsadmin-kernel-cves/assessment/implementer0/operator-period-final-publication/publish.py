import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SESSION = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves')
OWNER = SESSION / 'assessment/implementer0'
OUT = OWNER / 'operator-period-final-publication'
SYNC = SESSION / 'assessment/implementer1/draft-sync'
HEAD = '3fab2eaff537024f8ec32db6cdb3b0546808420d'
SOURCE = '57eea8950b38e22831f7ef87d0de2399b4783281'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
BRANCH = '2026-10-19-vpsadmin-kernel-cves'
DEFAULT = '2026-07-13-security-advisory-automation'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
LEDGER_SHA = '94c0047ff94cddcc7e6c32491360c1fae0e3e592b7e161dc72c094f05d8cd37a'
CHECKPOINTS = [
    '2d0c853e61ae3c3b1b9984507d2fb0f7b8e8f50f',
    'd2d9035e4eb61e1ca72795b632d92d0de36e9a2a',
    HEAD,
]
CVES = ['CVE-2026-53260', 'CVE-2026-72069', 'CVE-2026-64387']
PATHS = {f'advisories/{cve}/submission.yml' for cve in CVES}


def rawgit(*args):
    return subprocess.check_output(['git', *args])


def git(*args):
    return rawgit(*args).decode().strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def operation(name, args):
    result = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f'{name} exit {result.returncode}; stop, no automatic retry')
    return result.stdout


def fields(commit, path):
    return dict(re.findall(r'^([a-z_]+): (.*)$', git('show', commit + ':' + path), re.M))


def local_refs():
    rows = git('for-each-ref', '--format=%(refname)\t%(objectname)').splitlines()
    return dict(row.split('\t') for row in rows if not row.startswith('refs/remotes/'))


assert git('rev-parse', 'HEAD') == HEAD
assert git('branch', '--show-current') == BRANCH
assert not git('status', '--porcelain=v1')
assert not git('diff', '--cached', '--name-only')
assert git('remote', 'get-url', 'origin') == 'git@github.com:vpsfreecz/security-advisories.git'
assert git('remote', 'get-url', '--push', 'origin') == 'git@github.com:vpsfreecz/security-advisories.git'
assert sha((SYNC / 'final-three-ledger.json').read_bytes()) == LEDGER_SHA
ledger = json.loads((SYNC / 'final-three-ledger.json').read_text())
completion = json.loads((SYNC / 'final-three-completion.json').read_text())
assert completion['final_head'] == HEAD and completion['released_source_head'] == SOURCE
assert completion['checkpoint_shas'] == CHECKPOINTS
assert completion['content_revisions'] == [15, 15, 26]
assert completion['draft_ids'] == [112, 113, 106]
assert ledger['count'] == len(ledger['rows']) == 3
assert git('rev-list', '--reverse', SOURCE + '..' + HEAD).splitlines() == CHECKPOINTS
series = git('rev-list', '--reverse', BASE + '..' + HEAD).splitlines()
prefix = [row.split('\t')[0] for row in (OWNER / 'operator-period-source-publication/operator-period-full-series.tsv').read_text().splitlines()]
assert len(prefix) == 74 and len(series) == 77 and series[:74] == prefix
assert git('rev-list', '--count', '--merges', BASE + '..' + HEAD) == '0'
assert set(git('diff', '--name-only', SOURCE, HEAD).splitlines()) == PATHS

checkpoints = []
for i, (cve, row, checkpoint) in enumerate(zip(CVES, ledger['rows'], CHECKPOINTS)):
    parent = git('rev-parse', checkpoint + '^')
    assert parent == (SOURCE if i == 0 else CHECKPOINTS[i - 1])
    assert row['cve'] == cve and row['checkpoint_sha'] == checkpoint and row['state'] == 'draft'
    path = f'advisories/{cve}/submission.yml'
    assert git('diff-tree', '--no-commit-id', '--name-status', '-r', checkpoint) == 'M\t' + path
    data = fields(checkpoint, path)
    assert data['schema_version'] == '2' and data['source_commit'] == parent
    assert int(data['advisory_id']) == row['advisory_id']
    assert int(data['remote_content_revision']) == row['content_revision']
    evaluation = json.loads(Path(f'advisories/{cve}/evaluation.json').read_text())
    assert data['dossier_digest'] == evaluation['dossier_digest']
    assert row['node_counts'] == evaluation['completeness']['states']
    checkpoints.append({**row, 'actual_parent': parent, 'source_commit': data['source_commit'], 'path': path, 'schema_version': 2, 'submission_sha256': sha(rawgit('show', checkpoint + ':' + path))})

prior_ledgers = [('ledger.json', '509aadea80374705f3ca392f27064228ed3a8ed9ffce249ba7b898351ca244bf', 60), ('updates-ledger.json', 'c07a5fc8a891cc71938c79774bcc67139cfda2412097f616f34477dd8146f815', 3)]
prior = []
approved_cves = []
for name, digest, count in prior_ledgers:
    assert sha((SYNC / name).read_bytes()) == digest
    rows = json.loads((SYNC / name).read_text())['rows']
    assert len(rows) == count
    if count == 60:
        approved_cves = [row['cve'] for row in rows]
    for row in rows:
        checkpoint = row['checkpoint_sha']
        assert checkpoint in prefix
        path = f'advisories/{row["cve"]}/submission.yml'
        data = fields(checkpoint, path)
        parent = git('rev-parse', checkpoint + '^')
        assert data['source_commit'] == parent
        assert int(data['advisory_id']) == row['advisory_id']
        assert int(data['remote_content_revision']) == row['content_revision']
        prior.append({**row, 'actual_parent': parent, 'source_commit': parent, 'submission_sha256': sha(rawgit('show', checkpoint + ':' + path)), 'retained_in_consumed_prefix': True})
assert len(prior) == 63 and len({row['checkpoint_sha'] for row in prior + checkpoints}) == 66
assert len(set(approved_cves) - set(CVES)) == 57
old_baselines = json.loads((OWNER / 'operator-period-baseline-submissions.json').read_text())
assert len(old_baselines) == 111
final_baselines = {str(path): sha(path.read_bytes()) for path in Path('advisories').glob('*/submission.yml')}
assert set(final_baselines) == set(old_baselines)
unchanged = {path: digest for path, digest in old_baselines.items() if path not in PATHS}
assert len(unchanged) == 108
assert all(final_baselines[path] == digest for path, digest in unchanged.items())
refs_before = local_refs()


def invariants():
    assert git('rev-parse', 'HEAD') == HEAD
    assert not git('status', '--porcelain=v1') and not git('diff', '--cached', '--name-only')
    assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
    assert all(sha(Path(path).read_bytes()) == digest for path, digest in final_baselines.items())
    refs = local_refs()
    assert all(refs.get(name) == value for name, value in refs_before.items())


invariants()
assert os.environ.get('IN_NIX_SHELL'), 'repository Nix environment required'
for key in ('OVERCOMMIT_DISABLE', 'SKIP', 'ONLY', 'OVERCOMMIT_UNSAFE'):
    assert not os.environ.get(key), key
hook = Path(git('rev-parse', '--git-path', 'hooks/pre-push'))
assert hook.is_file() and os.access(hook, os.X_OK) and 'overcommit' in hook.read_text().lower()

artifacts = {
    'complete-series.tsv': ['log', '--reverse', '--format=%H%x09%P%x09%aI%x09%s', BASE + '..' + HEAD],
    'complete-final.diff': ['diff', '--full-index', '--binary', BASE, HEAD],
    'complete-final.stat': ['diff', '--stat', BASE, HEAD],
    'complete-final.paths': ['diff', '--name-status', BASE, HEAD],
    'complete-final.numstat': ['diff', '--numstat', BASE, HEAD],
    'three-checkpoints-series.tsv': ['log', '--reverse', '--format=%H%x09%P%x09%s', SOURCE + '..' + HEAD],
    'three-submission.diff': ['diff', '--full-index', '--binary', SOURCE, HEAD],
    'three-submission.stat': ['diff', '--stat', SOURCE, HEAD],
    'three-submission.paths': ['diff', '--name-status', SOURCE, HEAD],
    'three-submission.numstat': ['diff', '--numstat', SOURCE, HEAD],
}
inventory = {}
for name, args in artifacts.items():
    data = rawgit(*args)
    (OUT / name).write_bytes(data)
    inventory[name] = {'sha256': sha(data), 'bytes': len(data), 'git_args': args}
subprocess.run(['git', 'diff', '--check', BASE, HEAD], check=True)
subprocess.run(['git', 'diff', '--check', SOURCE, HEAD], check=True)
save('three-checkpoint-inventory.json', checkpoints)
save('prior63-boundary-proof.json', prior)
save('all66-boundary-proof.json', prior + checkpoints)
save('baseline-integrity.json', {'before': old_baselines, 'final': final_baselines, 'unchanged108': unchanged, 'other57_approved_baselines_unchanged': True})
save('local-refs-before.json', refs_before)
save('inventory-manifest.json', inventory)
preflight = {'head': HEAD, 'source': SOURCE, 'base': BASE, 'complete_commits': 77, 'unchanged_consumed_prefix': 74, 'new_external_checkpoints': 3, 'prior63_boundaries_preserved': True, 'all66_source_parents_verified': True, 'other108_baselines_unchanged': True, 'other57_approved_baselines_unchanged': True, 'source_unchanged_except_three_baselines': True, 'ledger_sha256': LEDGER_SHA, 'frozen_evidence_sha256': EVIDENCE, 'whole_worktree_clean': True, 'index_empty': True, 'inventory': inventory}
save('preflight.json', preflight)
print('PREFLIGHT PASS: complete77 inventory, unchanged74 prefix, all66 source parents, unchanged108/other57 baselines, frozen61904; SSH fetch next.', flush=True)
if '--preflight-only' in sys.argv:
    sys.exit(0)

operation('fetch', ['git', 'fetch', 'origin'])


def remote(name):
    text = operation(name, ['git', 'ls-remote', '--symref', 'origin', 'HEAD', 'refs/heads/' + DEFAULT, 'refs/heads/' + BRANCH])
    refs = dict((ref, digest) for digest, ref in (line.split('\t') for line in text.splitlines() if '\t' in line and not line.startswith('ref:')))
    assert 'ref: refs/heads/' + DEFAULT + '\tHEAD' in text
    assert refs['HEAD'] == refs['refs/heads/' + DEFAULT] == BASE, refs
    return refs


before = remote('remote-before')
assert before['refs/heads/' + BRANCH] == SOURCE, before
assert git('rev-parse', 'refs/remotes/origin/' + DEFAULT) == BASE
assert git('rev-parse', 'refs/remotes/origin/' + BRANCH) == SOURCE
subprocess.run(['git', 'merge-base', '--is-ancestor', SOURCE, HEAD], check=True)
invariants()
print('REMOTE PRECONDITIONS PASS: unchanged default ea624 and feature57ee; normal feature-only FF push now.', flush=True)
operation('push', ['git', 'push', 'origin', 'refs/heads/' + BRANCH + ':refs/heads/' + BRANCH])
after = remote('remote-after')
assert after['refs/heads/' + BRANCH] == HEAD, after
assert git('rev-parse', 'refs/remotes/origin/' + BRANCH) == HEAD
invariants()
save('local-refs-after.json', local_refs())
print('PUSH PASS: exact remote3fab, unchanged default, local refs preserved and worktree clean; CI metadata only next.', flush=True)
runs = json.loads(operation('ci-run-list', ['gh', 'run', 'list', '--repo', 'vpsfreecz/security-advisories', '--branch', BRANCH, '--commit', HEAD, '--limit', '20', '--json', 'databaseId,url,status,conclusion,headSha,name,event,workflowName,createdAt']))
assert all(row['headSha'] == HEAD for row in runs)
save('ci-runs.json', runs)
receipt = {**preflight, 'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'origin': 'git@github.com:vpsfreecz/security-advisories.git', 'normalSSH_fetch_and_feature_only_FFpush': 'PASS; single repository Nix environment; active hooks; no bypass', 'remote_before': before, 'remote_after': after, 'all_final_baseline_hashes_preserved_during_publication': True, 'all_local_refs_preserved': True, 'diff_checks': 'PASS', 'ci_runs': runs, 'CI_waited': False, 'slot_returned_to': 'lead', 'no_operations': ['advisoryAPI', 'source_edits', 'reevaluation', 'recollection', 'tests', 'rebase', 'amend', 'squash', 'forcepush', 'defaultmerge', 'PR', 'lifecycle'], 'session_url': 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
save('publication-receipt.json', receipt)
print(json.dumps({'head': HEAD, 'remote_exact': True, 'complete_commits': 77, 'clean': True, 'index_empty': True, 'ci_runs': runs, 'receipt': str(OUT / 'publication-receipt.json')}, indent=2), flush=True)
