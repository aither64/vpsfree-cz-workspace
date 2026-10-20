import datetime
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

OUT = Path(__file__).parent
OWNER = OUT.parent
PREVIOUS = OWNER / 'editorial-scope-followup'
HEAD = 'aa15ba719513d54c1e7942a085504777e4b7abfd'
ANCHOR = '3fab2eaff537024f8ec32db6cdb3b0546808420d'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
BRANCH = '2026-10-19-vpsadmin-kernel-cves'
DEFAULT = '2026-07-13-security-advisory-automation'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'


def git(*args):
    return subprocess.check_output(['git', *args])


def value(*args):
    return git(*args).decode().strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + '\n')


def operation(name, args):
    result = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(result.stdout + result.stderr)
    assert result.returncode == 0, f'{name} failed: exit{result.returncode}; stop without retry'
    return result.stdout


def local_refs():
    return dict(line.split('\t') for line in value('for-each-ref', '--format=%(refname)\t%(objectname)').splitlines() if not line.startswith('refs/remotes/'))


assert os.environ.get('IN_NIX_SHELL')
assert value('rev-parse', 'HEAD') == HEAD
assert value('branch', '--show-current') == BRANCH
assert value('remote', 'get-url', 'origin') == value('remote', 'get-url', '--push', 'origin') == 'git@github.com:vpsfreecz/security-advisories.git'
accepted = json.loads((PREVIOUS / 'commit-receipt.json').read_text())
assert accepted['head'] == HEAD and accepted['parent'] == ANCHOR
assert accepted['history']['complete_commits'] == 78
prefix = [line.split('\t')[0] for line in (OWNER / 'operator-period-final-publication/complete-series.tsv').read_text().splitlines()]
series = value('rev-list', '--reverse', BASE + '..' + HEAD).splitlines()
assert len(prefix) == 77 and len(series) == 78 and series[:-1] == prefix
assert value('rev-parse', HEAD + '^') == ANCHOR
assert set(value('diff', '--name-only', ANCHOR, HEAD).splitlines()) == set(accepted['exact9_path_sha256'])
baselines = json.loads((OWNER / 'operator-period-final-publication/baseline-integrity.json').read_text())['final']
assert len(baselines) == 111
boundaries = json.loads((OWNER / 'operator-period-final-publication/all66-boundary-proof.json').read_text())
assert len(boundaries) == 66 and all(row['checkpoint_sha'] in prefix for row in boundaries)
assert all(value('rev-parse', row['checkpoint_sha'] + '^') == row['source_commit'] for row in boundaries)
refs_before = local_refs()


def invariants():
    assert value('rev-parse', 'HEAD') == HEAD
    assert not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
    assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
    assert all(sha(Path(path).read_bytes()) == digest for path, digest in baselines.items())
    assert all(sha(Path(path).read_bytes()) == digest for path, digest in accepted['exact9_path_sha256'].items())
    refs = local_refs()
    assert all(refs.get(name) == digest for name, digest in refs_before.items())


invariants()
for key in ['OVERCOMMIT_DISABLE', 'SKIP', 'ONLY', 'OVERCOMMIT_UNSAFE']:
    assert not os.environ.get(key), key
hook = Path(value('rev-parse', '--git-path', 'hooks/pre-push'))
assert hook.is_file() and os.access(hook, os.X_OK) and 'overcommit' in hook.read_text().lower()
reused = {}
for name, metadata in accepted['artifacts'].items():
    path = PREVIOUS / name
    data = path.read_bytes()
    assert sha(data) == metadata['sha256'] and len(data) == metadata['bytes']
    assert git(*metadata['git_args']) == data, name
    shutil.copyfile(path, OUT / name)
    reused[name] = {**metadata, 'actual_git_byte_match': True}
history = json.loads((PREVIOUS / 'history-migration-inventory.json').read_text())
assert history['head'] == HEAD and history['migrations'].startswith('NO migrations')
shutil.copyfile(PREVIOUS / 'history-migration-inventory.json', OUT / 'history-migration-inventory.json')
save('inventory-byte-proof.json', reused)
save('preflight.json', {'head': HEAD, 'anchor': ANCHOR, 'base': BASE, 'complete_commits': 78, 'consumed77_prefix_preserved': True, 'all66_boundaries_and_actual_parents_preserved': True, 'all111_submission_hashes_preserved': True, 'accepted9_path_hashes_preserved': True, 'frozen_evidence_sha256': EVIDENCE, 'clean': True, 'index_empty': True})
save('local-refs-before.json', refs_before)
print('PreflightPASS: clean exactaa15, accepted78 inventory byteproof, consumed77/all66/all111/frozen61904. SSH fetch next.', flush=True)
operation('fetch', ['git', 'fetch', 'origin'])


def remote(name):
    text = operation(name, ['git', 'ls-remote', '--symref', 'origin', 'HEAD', 'refs/heads/' + DEFAULT, 'refs/heads/' + BRANCH])
    refs = dict((ref, digest) for digest, ref in (line.split('\t') for line in text.splitlines() if '\t' in line and not line.startswith('ref:')))
    assert 'ref: refs/heads/' + DEFAULT + '\tHEAD' in text
    assert refs['HEAD'] == refs['refs/heads/' + DEFAULT] == BASE, refs
    return refs


before = remote('remote-before')
assert before['refs/heads/' + BRANCH] == ANCHOR, before
assert value('rev-parse', 'refs/remotes/origin/' + DEFAULT) == BASE
assert value('rev-parse', 'refs/remotes/origin/' + BRANCH) == ANCHOR
invariants()
print('Remote preconditionsPASS: defaultea624/feature3fab. Normal feature-onlyFFpush now.', flush=True)
operation('push', ['git', 'push', 'origin', 'refs/heads/' + BRANCH + ':refs/heads/' + BRANCH])
after = remote('remote-after')
assert after['refs/heads/' + BRANCH] == HEAD
assert value('rev-parse', 'refs/remotes/origin/' + BRANCH) == HEAD
invariants()
save('local-refs-after.json', local_refs())
args = ['gh', 'run', 'list', '--repo', 'vpsfreecz/security-advisories', '--branch', BRANCH, '--commit', HEAD, '--limit', '20', '--json', 'databaseId,url,status,conclusion,headSha,name,event,workflowName,createdAt']
runs = json.loads(operation('ci-run-list', args))
assert all(row['headSha'] == HEAD for row in runs)
save('ci-runs.json', runs)
receipt = {'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': HEAD, 'source_parent': ANCHOR, 'base': BASE, 'normal_single_owned_Nix_shell_SSH_fetch_and_feature_only_FFpush': 'PASS; hooks active; no bypass', 'remote_before': before, 'remote_after': after, 'whole_worktree_clean': True, 'index_empty': True, 'all_local_refs_preserved': True, 'all111_submission_hashes_preserved': True, 'consumed77_prefix_preserved': True, 'all66_external_boundaries_and_source_parents_preserved': True, 'frozen_evidence_sha256': EVIDENCE, 'complete_commits': 78, 'full_final_paths': 250, 'bounded_editorial_paths': 9, 'reviewed_inventory_byte_reuse': reused, 'migration_inventory': history, 'ci_runs': runs, 'CI_waited': False, 'slot_returned_to': 'lead', 'no_operations': ['advisoryAPI', 'sourcechanges', 'reevaluation', 'recollection', 'tests', 'rebase', 'amend', 'forcepush', 'defaultmerge', 'PR', 'lifecycle'], 'session_url': 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
save('publication-receipt.json', receipt)
print(json.dumps({'head': HEAD, 'remote_exact': True, 'clean': True, 'index_empty': True, 'ci_runs': runs, 'receipt': str(OUT / 'publication-receipt.json')}, indent=2), flush=True)
