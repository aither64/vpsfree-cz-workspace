import copy
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves')
OUT = ROOT / 'assessment/implementer0/editorial-scope-followup'
BASE = '3fab2eaff537024f8ec32db6cdb3b0546808420d'
FEATURE_BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
CVES = ['CVE-2026-53260', 'CVE-2026-72069', 'CVE-2026-64387']


def git(*args):
    return subprocess.check_output(['git', *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


assert git('rev-parse', 'HEAD').decode().strip() == BASE
assert not git('diff', '--cached', '--name-only').strip()
assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
editorial = json.loads((ROOT / 'assessment/editorial-scope-lead-changes.json').read_text())
comparisons = []
for row in editorial['files']:
    cve = row['cve']
    path = f'advisories/{cve}/advisory.yml'
    assert sha(Path(path).read_bytes()) == row['sha256'], path
    assert Path(path).read_bytes().split(b'"texts"', 1)[0] == git('show', BASE + ':' + path).split(b'"texts"', 1)[0]

for cve in CVES:
    path = f'advisories/{cve}/evaluation.json'
    old = json.loads(git('show', BASE + ':' + path))
    new = json.loads(Path(path).read_text())
    comparable_old, comparable_new = copy.deepcopy(old), copy.deepcopy(new)
    for field in ['dossier_digest', 'evaluated_at']:
        comparable_old.pop(field)
        comparable_new.pop(field)
    removed = []
    if cve != 'CVE-2026-64387':
        for node in comparable_old['nodes']:
            if node['node_id'] == 161:
                assert set(node['notes']) == {'en', 'cs'}
                removed.append({'node_id': 161, 'notes': node.pop('notes')})
        assert len(removed) == 1
        assert all('notes' not in node for node in new['nodes'])
    assert comparable_old == comparable_new, cve
    assert old['dossier_digest'] != new['dossier_digest']
    comparisons.append({'cve': cve, 'complete_evaluation_equal_except_dossier_digest_evaluated_at_and_exact_removed_notes': True, 'all_states_reasons_dates_and_other_fields_unchanged': True, 'removed_notes': removed, 'old_digest': old['dossier_digest'], 'new_digest': new['dossier_digest'], 'states': new['completeness']['states']})

submissions = git('ls-files', 'advisories/*/submission.yml').decode().splitlines()
assert len(submissions) == 111
assert all(Path(path).read_bytes() == git('show', BASE + ':' + path) for path in submissions)
prefix = [line.split('\t')[0] for line in (ROOT / 'assessment/implementer0/operator-period-final-publication/complete-series.tsv').read_text().splitlines()]
assert len(prefix) == 77
assert git('rev-list', '--reverse', FEATURE_BASE + '..' + BASE).decode().splitlines() == prefix
boundaries = json.loads((ROOT / 'assessment/implementer0/operator-period-final-publication/all66-boundary-proof.json').read_text())
assert len(boundaries) == 66
assert all(row['checkpoint_sha'] in prefix for row in boundaries)
assert all(git('rev-parse', row['checkpoint_sha'] + '^').decode().strip() == row['source_commit'] for row in boundaries)
expected = {f'advisories/{cve}/{name}' for cve in CVES for name in ['advisory.yml', 'evaluation.json']}
expected |= {f'advisories/{cve}/analysis.md' for cve in CVES[:2]}
expected.add('spec/dossiers_spec.rb')
changed = set(git('diff', '--name-only', BASE).decode().splitlines())
assert changed == expected, changed
assert not git('status', '--porcelain=v1', '--untracked-files=normal').decode().count('??')
subprocess.run(['git', 'diff', '--check'], check=True)
inventory = {path: sha(Path(path).read_bytes()) for path in sorted(expected)}
(OUT / 'owned.diff').write_bytes(git('diff', BASE, '--', *sorted(expected)))
(OUT / 'comparison.json').write_text(json.dumps({'base': BASE, 'comparisons': comparisons, 'frozen_evidence_sha256': EVIDENCE, 'all111_submissions_unchanged': True, 'consumed77_prefix_and66_boundaries_preserved': True, 'other57_and_perf_unchanged': True, 'lead_public_YAML_hashes_preserved': True, 'technical_YAML_prefixes_unchanged': True, 'index_empty': True, 'exact9_owned_path_sha256': inventory}, indent=2) + '\n')
print(json.dumps({'comparison': 'PASS: complete evaluations equal except exact allowed changes', 'owned_paths': len(expected), 'states': {row['cve']: row['states'] for row in comparisons}, 'submissions_unchanged': len(submissions), 'frozen61904': True}, indent=2))
