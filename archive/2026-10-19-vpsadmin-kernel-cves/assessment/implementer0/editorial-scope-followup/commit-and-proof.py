import datetime
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

OUT = Path(__file__).parent
ROOT = OUT.parents[2]
PARENT = '3fab2eaff537024f8ec32db6cdb3b0546808420d'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
CVES = ['CVE-2026-53260', 'CVE-2026-72069', 'CVE-2026-64387']
ready = json.loads((OUT / 'ready-receipt.json').read_text())
hashes = ready['comparison']['exact9_owned_path_sha256']
paths = sorted(hashes)


def git(*args):
    return subprocess.check_output(['git', *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def command(name, args):
    result = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(result.stdout + result.stderr)
    assert result.returncode == 0, f'{name} exit {result.returncode}; stop and inspect log'
    return result.stdout


def invariant_hashes():
    assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
    assert all(sha(Path(path).read_bytes()) == digest for path, digest in hashes.items())


assert os.environ.get('IN_NIX_SHELL')
assert git('rev-parse', 'HEAD').decode().strip() == PARENT
assert git('branch', '--show-current').decode().strip() == '2026-10-19-vpsadmin-kernel-cves'
assert not git('diff', '--cached', '--name-only').strip()
assert set(git('diff', '--name-only').decode().splitlines()) == set(paths) and len(paths) == 9
invariant_hashes()
for key in ('OVERCOMMIT_DISABLE', 'SKIP', 'ONLY', 'OVERCOMMIT_UNSAFE'):
    assert not os.environ.get(key), key
hooks = {}
for name in ['pre-commit', 'commit-msg']:
    hook = Path(git('rev-parse', '--git-path', 'hooks/' + name).decode().strip())
    assert hook.is_file() and os.access(hook, os.X_OK) and 'overcommit' in hook.read_text().lower()
    hooks[name] = {'path': str(hook), 'sha256': sha(hook.read_bytes()), 'active': True}

message = '''Clarify operator-confirmed RT and CIFS applicability

Replace build-limited and period-qualified public caveats with the
operator's confirmed scope, and remove redundant RT storage notes.

Keep runtime rules and all per-node states, reasons and dates unchanged.
Reconcile RT provenance and regenerate the three digest-bound evaluations.
'''
assert all(len(line) <= 80 for line in message.splitlines())
with tempfile.NamedTemporaryFile(mode='w', prefix='kernel-cve-editorial-', suffix='.txt', delete=False) as stream:
    stream.write(message)
    message_path = stream.name
command('stage-exact9', ['git', 'add', '--', *paths])
assert set(git('diff', '--cached', '--name-only').decode().splitlines()) == set(paths)
command('staged-diff-check', ['git', 'diff', '--cached', '--check'])
(OUT / 'staged9.paths').write_bytes(git('diff', '--cached', '--name-status'))
save('commit-preflight.json', {'parent': PARENT, 'exact9_path_sha256': hashes, 'hooks': hooks, 'temporary_message_file': message_path, 'message': message, 'frozen_evidence_sha256': EVIDENCE})
print('Exact9 hashes/staged paths/normal hooks/frozen snapshot PASS; normal commit now.', flush=True)
command('normal-commit', ['git', 'commit', '-F', message_path])
head = git('rev-parse', 'HEAD').decode().strip()
assert git('rev-parse', head + '^').decode().strip() == PARENT
assert set(git('diff', '--name-only', PARENT, head).decode().splitlines()) == set(paths)
assert not git('status', '--porcelain=v1').strip()
assert not git('diff', '--cached', '--name-only').strip()
invariant_hashes()
print('Normal commit PASS: ' + head + '; nonpersisting Reconciler comparison next.', flush=True)

ruby = '''require 'json'
r = SecurityAdvisories::Reconciler.new(client: nil)
rows = ARGV.map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve)
  committed = r.load_evaluation(advisory)
  reproduced = r.evaluate(advisory, persist: false)
  committed.delete('evaluated_at')
  reproduced.delete('evaluated_at')
  raise "complete evaluation mismatch: #{cve}" unless committed == reproduced
  { cve: cve, dossier_digest: advisory.digest,
    complete_result_equal_except_evaluated_at: true,
    loader_digest_verified: true, persisted: false,
    states: reproduced.fetch('completeness').fetch('states') }
end
puts JSON.pretty_generate(rows)
'''
(OUT / 'postcommit-nonpersisting-proof.rb').write_text(ruby)
result = command('postcommit-nonpersisting-proof', ['bundle', 'exec', 'ruby', '-r', './lib/security_advisories', str(OUT / 'postcommit-nonpersisting-proof.rb'), *CVES])
reproduced = json.loads(result)
invariant_hashes()
assert not git('status', '--porcelain=v1').strip()
assert not git('diff', '--cached', '--name-only').strip()

baseline = json.loads((OUT.parent / 'operator-period-final-publication/baseline-integrity.json').read_text())['final']
assert len(baseline) == 111
assert all(sha(Path(path).read_bytes()) == digest for path, digest in baseline.items())
prefix = [line.split('\t')[0] for line in (OUT.parent / 'operator-period-final-publication/complete-series.tsv').read_text().splitlines()]
series = git('rev-list', '--reverse', BASE + '..' + head).decode().splitlines()
assert len(prefix) == 77 and len(series) == 78 and series[:-1] == prefix
assert git('rev-list', '--count', '--merges', BASE + '..' + head).decode().strip() == '0'
boundaries = json.loads((OUT.parent / 'operator-period-final-publication/all66-boundary-proof.json').read_text())
assert len(boundaries) == 66
assert all(row['checkpoint_sha'] in prefix for row in boundaries)
assert all(git('rev-parse', row['checkpoint_sha'] + '^').decode().strip() == row['source_commit'] for row in boundaries)
artifacts = {
    'complete78-series.tsv': ['log', '--reverse', '--format=%H%x09%P%x09%aI%x09%s', BASE + '..' + head],
    'complete78-final.diff': ['diff', '--full-index', '--binary', BASE, head],
    'complete78-final.stat': ['diff', '--stat', BASE, head],
    'complete78-final.paths': ['diff', '--name-status', BASE, head],
    'complete78-final.numstat': ['diff', '--numstat', BASE, head],
    'bounded-editorial.diff': ['diff', '--full-index', '--binary', PARENT, head],
    'bounded-editorial.stat': ['diff', '--stat', PARENT, head],
    'bounded-editorial.paths': ['diff', '--name-status', PARENT, head],
    'bounded-editorial.numstat': ['diff', '--numstat', PARENT, head],
}
artifact_manifest = {}
for name, args in artifacts.items():
    data = git(*args)
    (OUT / name).write_bytes(data)
    artifact_manifest[name] = {'sha256': sha(data), 'bytes': len(data), 'git_args': args}
command('complete78-diff-check', ['git', 'diff', '--check', BASE, head])
command('bounded-diff-check', ['git', 'diff', '--check', PARENT, head])
changed_paths = git('diff', '--name-only', BASE, head).decode().splitlines()
migrations = [path for path in changed_paths if re.search(r'(^|/)(migrate|migrations)(/|$)', path)]
assert not migrations
history = {'base': BASE, 'parent': PARENT, 'head': head, 'complete_commits': 78, 'unchanged_consumed_prefix': 77, 'new_logical_source_commits': 1, 'all66_external_boundaries_and_actual_parents_preserved': True, 'migrations': 'NO migrations in complete range or bounded unit', 'migration_paths': migrations, 'no_rewrite': True, 'full_diff_path_count': len(changed_paths)}
save('history-migration-inventory.json', history)
save('inventory-manifest.json', artifact_manifest)
receipt = {'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': head, 'parent': PARENT, 'owned_path_count': 9, 'exact9_path_sha256': hashes, 'normal_Nix_Overcommit_hooks': 'PASS; no bypass', 'active_hooks': hooks, 'normal_commit_log_sha256': sha((OUT / 'normal-commit.log').read_bytes()), 'postcommit_full_nonpersisting_Reconciler_comparisons': reproduced, 'all111_submission_hashes_preserved': True, 'frozen_evidence_sha256': EVIDENCE, 'all_owned_file_hashes_unchanged_by_commit_or_postcommit_proof': True, 'whole_worktree_clean': True, 'index_empty': True, 'history': history, 'artifacts': artifact_manifest, 'slot_returned_to': 'lead', 'no_operations': ['API', 'push', 'fetch', 'rebase', 'amend', 'defaultmerge', 'lifecycle', 'extra_tests']}
save('commit-receipt.json', receipt)
print(json.dumps({'head': head, 'parent': PARENT, 'paths': len(paths), 'complete_commits': len(series), 'postcommit_nonpersisting_reproduction': 'PASS all3', 'normal_hooks': 'PASS', 'whole_clean': True, 'index_empty': True, 'receipt': str(OUT / 'commit-receipt.json')}, indent=2), flush=True)
