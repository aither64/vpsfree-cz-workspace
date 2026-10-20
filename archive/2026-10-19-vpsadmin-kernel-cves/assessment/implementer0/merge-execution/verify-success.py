import datetime, hashlib, json, subprocess
from pathlib import Path

OUT = Path(__file__).parent
OWNER = OUT.parent
PREP = OWNER / 'merge-preparation'
HEAD = 'e6ceb642878dd97546174217676d9861afc38d4e'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
OLD_LOCAL = 'ad64a0524b1e0e9e628c444340b10680d7292185'
BRANCH = '2026-10-19-vpsadmin-kernel-cves'
DEFAULT = '2026-07-13-security-advisory-automation'
TARGET = 'refs/heads/' + DEFAULT
JOB = 'c2e1d761-4371-4208-a13a-aa179357b448'
ATTEMPT = '674f1c31-8b3f-45f4-94b6-c5766153740d'
FROZEN = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'

def value(*args): return subprocess.check_output(['git', *args], text=True).strip()
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, data): (OUT / name).write_text(json.dumps(data, indent=2) + '\n')
def operation(name, args):
    result = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(result.stdout + result.stderr)
    assert result.returncode == 0, f'{name} exit{result.returncode}; read-only verification failed, no mutation retry'
    return result.stdout

state = json.loads((OUT / 'status-succeeded.log').read_text()) if (OUT / 'status-succeeded.log').exists() else json.loads(operation('status-succeeded', ['dev-session', 'coordination', 'status', BRANCH, '--as-is', '--json']))
job = next(row for row in state['jobs'] if row['id'] == JOB)
assert job['state'] == 'succeeded' and job['attempt'] == ATTEMPT
assert job['result']['outcome'] == 'applied'
assert job['result']['observed']['head'] == job['result']['observed']['remoteHead'] == HEAD
save('succeeded-job.json', job)
snapshot = json.loads((PREP / 'coordinator-prepare-receipt.json').read_text())
assert value('rev-parse', 'HEAD') == value('rev-parse', TARGET) == value('rev-parse', 'refs/heads/' + BRANCH) == HEAD
assert value('rev-parse', snapshot['operation']['sourceRef']) == HEAD
assert not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
checkout = snapshot['operation']['targetCheckout']
target_payload_present = Path(checkout).is_dir()
if target_payload_present:
    assert value('-C', checkout, 'rev-parse', 'HEAD') == HEAD and not value('-C', checkout, 'status', '--porcelain=v1')
assert sha(Path('.state/evidence.json').read_bytes()) == FROZEN
baselines = json.loads((OWNER / 'editorial-final-publication/baseline-integrity.json').read_text())['final']
assert len(baselines) == 111 and all(sha(Path(path).read_bytes()) == digest for path, digest in baselines.items())
subprocess.run(['git', 'merge-base', '--is-ancestor', BASE, HEAD], check=True)
subprocess.run(['git', 'merge-base', '--is-ancestor', OLD_LOCAL, HEAD], check=True)
prefix = [line.split('\t')[0] for line in (OWNER / 'editorial-final-publication/complete81-series.tsv').read_text().splitlines()]
assert len(prefix) == 81 and value('rev-list', '--reverse', BASE + '..' + HEAD).splitlines() == prefix
boundaries = json.loads((OWNER / 'editorial-final-publication/all69-boundary-proof.json').read_text())
assert len(boundaries) == 69 and all(row['checkpoint_sha'] in prefix for row in boundaries)
remote_text = operation('remote-merged', ['git', 'ls-remote', '--symref', 'origin', 'HEAD', TARGET, 'refs/heads/' + BRANCH])
refs = dict((ref, digest) for digest, ref in (line.split('\t') for line in remote_text.splitlines() if '\t' in line and not line.startswith('ref:')))
assert 'ref: ' + TARGET + '\tHEAD' in remote_text
assert refs['HEAD'] == refs[TARGET] == refs['refs/heads/' + BRANCH] == HEAD
old_refs = json.loads((OWNER / 'editorial-final-publication/local-refs-after.json').read_text())
current_refs = dict(line.split('\t') for line in value('for-each-ref', '--format=%(refname)\t%(objectname)').splitlines())
assert all(current_refs.get(ref) == (HEAD if ref == TARGET else digest) for ref, digest in old_refs.items())
runs = json.loads(operation('default-head-ci', ['gh', 'run', 'list', '--repo', 'vpsfreecz/security-advisories', '--branch', DEFAULT, '--commit', HEAD, '--limit', '20', '--json', 'databaseId,url,status,conclusion,headSha,headBranch,name,event,workflowName,createdAt']))
assert all(row['headSha'] == HEAD and row['headBranch'] == DEFAULT for row in runs)
save('default-head-ci.json', runs)
receipt = {'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'result': 'MERGED_VERIFIED', 'repository': 'security-advisories', 'target': TARGET, 'head': HEAD, 'remote_target_and_feature': refs, 'local_default_and_feature': HEAD, 'approval_id': job['approvalId'], 'job_id': JOB, 'attempt_id': ATTEMPT, 'snapshot_id': job['snapshot']['id'], 'coordinator_state': job['state'], 'coordinator_result': job['result'], 'normal_coordinator_ff_only_SSH_merge': True, 'normal_sealed_hooks': snapshot['operation']['hookArtifact'], 'no_caller_RUBYOPT_or_hook_bypass': True, 'prior_local_and_remote_targets_remain_ancestors': [OLD_LOCAL, BASE], 'all81_consumed_commits_and69_external_boundaries_preserved': True, 'all111_baseline_hashes_preserved': True, 'frozen_evidence_sha256': FROZEN, 'feature_ref_retained': True, 'all_other_existing_refs_preserved': True, 'feature_worktree_and_index_clean': True, 'private_target_payload_present_after_completed_operation': target_payload_present, 'private_target_payload_note': 'Disposable coordinator target already absent after success, consistent with documented completed-payload retention; agent performed no cleanup, deletion or recreation. Registered session feature worktree remains retained and clean.', 'default_head_ci_runs': runs, 'CI_waited': False, 'slot_returned_to': 'lead', 'publication_separate_outcome': True, 'no_API_tests_reevaluation_source_edits_deployment_email_lifecycle_cleanup': True, 'session_url': 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/'}
save('final-merge-receipt.json', receipt)
print(json.dumps(receipt, indent=2), flush=True)
