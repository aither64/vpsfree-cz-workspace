import hashlib, json, os, subprocess, uuid
from pathlib import Path

OUT = Path(__file__).parent
OWNER = OUT.parent
SESSION = OWNER.parents[1]
HEAD = 'e6ceb642878dd97546174217676d9861afc38d4e'
BASE = 'ea6247687fd02417f87e1e5593fecd8b9055925d'
LOCAL = 'ad64a0524b1e0e9e628c444340b10680d7292185'
TARGET = 'refs/heads/2026-07-13-security-advisory-automation'
EVIDENCE = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'

def git(*args): return subprocess.check_output(['git', *args])
def value(*args): return git(*args).decode().strip()
def sha(data): return hashlib.sha256(data).hexdigest()
def save(name, data): (OUT / name).write_text(json.dumps(data, indent=2) + '\n')

snapshot = json.loads((OUT / 'coordinator-prepare-receipt.json').read_text())
op = snapshot['operation']
assert snapshot['id'] == 'sha256:6a0844d859ba4c4dbc94af4ca8373cea4467f0421068ad6664f68dd115905fc2'
assert op['featureHead'] == HEAD and op['expectedRemoteHead'] == BASE and op['target'] == TARGET
assert op['expectedLocalTargetHead'] == LOCAL and value('rev-parse', TARGET) == LOCAL
assert value('rev-parse', op['sourceRef']) == HEAD
subprocess.run(['git', 'merge-base', '--is-ancestor', LOCAL, BASE], check=True)
subprocess.run(['git', 'merge-base', '--is-ancestor', BASE, HEAD], check=True)
assert value('rev-parse', 'HEAD') == HEAD and not value('status', '--porcelain=v1') and not value('diff', '--cached', '--name-only')
assert sha(Path('.state/evidence.json').read_bytes()) == EVIDENCE
baselines = json.loads((OWNER / 'editorial-final-publication/baseline-integrity.json').read_text())['final']
assert len(baselines) == 111 and all(sha(Path(path).read_bytes()) == digest for path, digest in baselines.items())
hook_id = op['hookArtifact']
artifact_path = Path('/home/aither/.local/state/dev-workspaces/coordination/sources') / hook_id.removeprefix('sha256:') / 'artifact.json'
artifact = json.loads(artifact_path.read_text())
assert artifact['id'] == hook_id and artifact['kind'] == 'merge_hooks' and artifact['repository'] == 'security-advisories' and artifact['featureHead'] == HEAD
allowed = {'PATH', 'GEM_HOME', 'GEM_PATH', 'BUNDLE_GEMFILE', 'BUNDLE_PATH', 'BUNDLE_APP_CONFIG', 'BUNDLER_VERSION', 'NIX_SSL_CERT_FILE', 'SSL_CERT_FILE'}
assert set(artifact['environment']) <= allowed and artifact['environment']['PATH']
assert not any(key in artifact['environment'] for key in ['RUBYOPT', 'OVERCOMMIT_DISABLE', 'SKIP', 'ONLY'])
assert os.access(Path(value('rev-parse', '--git-path', 'hooks/pre-push')), os.X_OK)
hook_proof = {'artifact_id': hook_id, 'artifact_path': str(artifact_path), 'artifact_file_sha256': sha(artifact_path.read_bytes()), 'repository': artifact['repository'], 'featureHead': artifact['featureHead'], 'kind': artifact['kind'], 'sealed_environment_keys_only': sorted(artifact['environment']), 'caller_preload_not_retained_in_worker_environment': True, 'no_hook_skip_keys': True, 'preparation_probe_loaded_locked_bundle_and_Overcommit': json.loads((OUT / 'environment-diagnosis.json').read_text())['retained_declared_Nix_shell_exact_probe_with_preload']}
save('hook-artifact-proof.json', hook_proof)
lineage = {'local_target_before': LOCAL, 'remote_target': BASE, 'feature': HEAD, 'local_is_ancestor_of_remote': True, 'commits_between_local_and_remote': int(value('rev-list', '--count', LOCAL + '..' + BASE)), 'remote_is_ancestor_of_feature': True, 'local_ref_unchanged_during_preparation': True, 'supported_handling': 'Coordinator prepare explicitly requires local target to be an ancestor of remote target. It retains the exact old local target as a stale-state guard, creates the private checkout at remote ea624, and later merges ff-only to e6ceb. Worker checks the local target still equals ad64, then compare-and-swap advances it to e6ceb. Both ad64 and ea624 remain ancestors; no reset, rewrite or lost commits.', 'runtime_reference': 'selected workspace-coordination-execution.rb293-319 and919-950', 'no_target_mutation_executed': True}
save('local-target-lineage.json', lineage)
approval = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': 'merge', 'scope': [{'repository': 'security-advisories', 'target': TARGET}], 'reviewedSnapshot': snapshot['id'], 'source': {'kind': 'user_instruction', 'reference': str(SESSION / 'assessment/publication-and-merge-user-authorization.json'), 'quote': 'and merge the changes'}}
submission = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': 'merge', 'dependsOn': [], 'approvalId': None, 'reservationId': None, 'snapshot': snapshot}
save('approval-request.json', approval)
save('submit-request-template.json', submission)
status = subprocess.run(['dev-session', 'coordination', 'status', '2026-10-19-vpsadmin-kernel-cves', '--as-is', '--json'], text=True, capture_output=True)
(OUT / 'coordinator-status.log').write_text(status.stdout + status.stderr)
assert status.returncode == 0
state = json.loads(status.stdout)
assert not state['jobs'] and not state['reservations']
receipt = {'schema': 1, 'head': HEAD, 'base': BASE, 'prepared_snapshot_id': snapshot['id'], 'prepared_snapshot_path': str(OUT / 'coordinator-prepare-receipt.json'), 'snapshot_sha256': sha((OUT / 'coordinator-prepare-receipt.json').read_bytes()), 'integration_evidence_path': str(OUT / 'integration-evidence.json'), 'integration_evidence_sha256': sha((OUT / 'integration-evidence.json').read_bytes()), 'normal_coordinator_prepare': 'PASS using subprocess-only RUBYOPT=-rbundler/setup; original request identity/input preserved', 'failed_attempt_preserved': str(OUT / 'coordinator-prepare-gem-conflict.log'), 'normal_hook_artifact': hook_proof, 'local_target_lineage': lineage, 'approval_request_prepared_not_executed': str(OUT / 'approval-request.json'), 'submit_template_not_executed': str(OUT / 'submit-request-template.json'), 'submit_approvalId_must_be_filled_from_normal_approval_receipt': True, 'reservationId': None, 'all81_consumed_commits_and69_boundaries_preserved': True, 'all111_submission_baselines_preserved': True, 'frozen_evidence_sha256': EVIDENCE, 'whole_worktree_clean': True, 'index_empty': True, 'source_feature_and_remote_default_unchanged': True, 'coordinator_jobs': [], 'approved': False, 'submitted': False, 'slot_returned_to': 'lead', 'next_gate': 'All60 publication success and explicit lead merge release, then public approve and submit of this exact snapshot; no direct Git integration.', 'no_source_runtime_or_lock_edits': True, 'no_deployment_email_or_lifecycle': True}
save('preparation-receipt.json', receipt)
print(json.dumps({'snapshot': snapshot['id'], 'head': HEAD, 'local_target_ancestor_commits': lineage['commits_between_local_and_remote'], 'hook_artifact': hook_id, 'prepared_not_approved_or_submitted': True, 'clean': True, 'index_empty': True, 'receipt': str(OUT / 'preparation-receipt.json')}, indent=2))
