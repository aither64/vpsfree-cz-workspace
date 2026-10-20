import datetime, hashlib, json, os, re, shutil, subprocess
from pathlib import Path

OUT = Path(__file__).parent
OWNER = OUT.parent
PREP = OWNER / 'merge-preparation'
SESSION = OWNER.parents[1]
HEAD = 'e6ceb642878dd97546174217676d9861afc38d4e'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
LOCAL = 'ad64a0524b1e0e9e628c444340b10680d7292185'
TARGET = 'refs/heads/2026-07-13-security-advisory-automation'
BRANCH = '2026-10-19-vpsadmin-kernel-cves'
FROZEN = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
SNAPSHOT_ID = 'sha256:6a0844d859ba4c4dbc94af4ca8373cea4467f0421068ad6664f68dd115905fc2'

def git(*args): return subprocess.check_output(['git', *args])
def value(*args): return git(*args).decode().strip()
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, data): (OUT / name).write_text(json.dumps(data, indent=2) + '\n')
def operation(name, args):
    r = subprocess.run(args, text=True, capture_output=True)
    (OUT / (name + '.log')).write_text(r.stdout + r.stderr)
    assert r.returncode == 0, f'{name} exit{r.returncode}; inspect original request/status, no competing retry'
    return r.stdout

assert os.environ.get('IN_NIX_SHELL') and not os.environ.get('RUBYOPT')
assert value('rev-parse', 'HEAD') == HEAD and value('branch', '--show-current') == BRANCH
assert value('rev-parse', TARGET) == LOCAL
assert value('remote', 'get-url', 'origin') == value('remote', 'get-url', '--push', 'origin') == 'git@github.com:vpsfreecz/security-advisories.git'
assert not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
assert sha(Path('.state/evidence.json').read_bytes()) == FROZEN
baselines = json.loads((OWNER / 'editorial-final-publication/baseline-integrity.json').read_text())['final']
assert len(baselines) == 111 and all(sha(Path(path).read_bytes()) == digest for path, digest in baselines.items())
snapshot_path = PREP / 'coordinator-prepare-receipt.json'
assert sha(snapshot_path.read_bytes()) == '3007f4a06bac67c6114c98acd3b1b34e51ccd14d932c3954cc6cc4f95c9745db'
snapshot = json.loads(snapshot_path.read_text()); assert snapshot['id'] == SNAPSHOT_ID
evidence = PREP / 'integration-evidence.json'
assert sha(evidence.read_bytes()) == 'f53af5460b042e50bd517cc49ee4061aa928ab85570b858b59c42b45bd3d0257'
assert value('rev-parse', snapshot['operation']['sourceRef']) == HEAD
assert value('rev-list', '--count', BASE + '..' + HEAD) == '81'
hook_proof = json.loads((PREP / 'hook-artifact-proof.json').read_text())
assert sha(Path(hook_proof['artifact_path']).read_bytes()) == hook_proof['artifact_file_sha256']
accepted = json.loads((SESSION / 'assessment/merge-lead-preparation-acceptance.json').read_text())
assert accepted['snapshot_id'] == SNAPSHOT_ID and accepted['feature_head'] == HEAD
assert 'parallel with API-only publication' in accepted['execution_release']
remote_text = operation('remote-before', ['git', 'ls-remote', '--symref', 'origin', 'HEAD', TARGET, 'refs/heads/' + BRANCH])
refs = dict((ref, digest) for digest, ref in (line.split('\t') for line in remote_text.splitlines() if '\t' in line and not line.startswith('ref:')))
assert refs['HEAD'] == refs[TARGET] == BASE and refs['refs/heads/' + BRANCH] == HEAD, refs
approve_path = PREP / 'approval-request.json'
assert sha(approve_path.read_bytes()) == 'c66a470c8135f07e2d7efd34745bc4fd94b09814ebbeea51a25c5d26b3b8649a'
request = json.loads(approve_path.read_text()); assert request['reviewedSnapshot'] == SNAPSHOT_ID and request['source']['quote'] == 'and merge the changes'
shutil.copyfile(approve_path, OUT / 'approval-request.json')
save('execution-preflight.json', {'head': HEAD, 'snapshot_id': SNAPSHOT_ID, 'remote_before': refs, 'local_target_before': LOCAL, 'all111_baselines_preserved': True, 'frozen_evidence_sha256': FROZEN, 'whole_clean': True, 'index_empty': True, 'caller_RUBYOPT_absent': True, 'normal_sealed_hook_artifact': snapshot['operation']['hookArtifact']})
print('Input guardsPASS; public coordinator approval now.', flush=True)
approval = json.loads(operation('approval', ['dev-session', 'coordination', 'approve', BRANCH, '--as-is', '--request', str(OUT / 'approval-request.json'), '--json']))
save('approval-receipt.json', approval)
assert re.fullmatch(r'[0-9a-f-]{36}', approval['id'])
submission = json.loads((PREP / 'submit-request-template.json').read_text())
assert submission['snapshot'] == snapshot and submission['reservationId'] is None and submission['dependsOn'] == [] and submission['approvalId'] is None
submission['approvalId'] = approval['id']
save('submit-request.json', submission)
print('Approval recorded ' + approval['id'] + '; public coordinator submit exactsnapshot now.', flush=True)
submitted = json.loads(operation('submit', ['dev-session', 'coordination', 'submit', BRANCH, '--as-is', '--request', str(OUT / 'submit-request.json'), '--json']))
save('submission-receipt.json', submitted)
job_id = submitted['id']; assert re.fullmatch(r'[0-9a-f-]{36}', job_id)
status = json.loads(operation('status-after-submit', ['dev-session', 'coordination', 'status', BRANCH, '--as-is', '--json']))
job = next(row for row in status['jobs'] if row['id'] == job_id)
save('job-status.json', job)
assert value('rev-parse', 'HEAD') == HEAD and not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
assert sha(Path('.state/evidence.json').read_bytes()) == FROZEN
assert all(sha(Path(path).read_bytes()) == digest for path, digest in baselines.items())
receipt = {'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': HEAD, 'target': TARGET, 'snapshot_id': SNAPSHOT_ID, 'approval_id': approval['id'], 'approval_request_id': request['requestId'], 'submission_request_id': submission['requestId'], 'job_id': job_id, 'attempt_id': job.get('attempt'), 'job_state': job['state'], 'job_result': job.get('result'), 'normal_public_approve_and_submit': True, 'reservationId': None, 'dependsOn': [], 'caller_RUBYOPT_absent': True, 'sealed_normal_hooks': snapshot['operation']['hookArtifact'], 'all111_baselines_preserved': True, 'frozen_evidence_sha256': FROZEN, 'whole_worktree_clean': True, 'index_empty': True, 'native_coordinator_owns_remaining_mutation': job['state'] not in ['succeeded', 'failed', 'cancelled'], 'no_long_poll_or_CI_wait': True, 'slot_returned_to': 'lead/native coordinator', 'no_direct_merge_or_push_bypass': True, 'no_API_tests_reevaluation_deployment_email_lifecycle': True}
save('execution-receipt.json', receipt)
print(json.dumps(receipt, indent=2), flush=True)
