#!/usr/bin/env python3
"""One bounded CI snapshot; no waits, dispatch or rerun; only superseded active cancellation."""
import hashlib
import json
from pathlib import Path
import subprocess
import time

HERE = Path(__file__).resolve().parent
SLUG = HERE.name
OUT = HERE / 'verification/c7-git-cache-publication'
FIELDS = 'databaseId,workflowName,name,headSha,headBranch,status,conclusion,url,event,createdAt,updatedAt'


def main():
    inventory = json.loads((HERE / 'package-c7-final-source-inventory.json').read_text())
    receipt = {'observed_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'repositories': [],
               'scope': 'Single bounded metadata observation; no CI wait, dispatch or rerun'}
    destination = OUT / 'ci-snapshot.json'
    assert not destination.exists()
    def save():
        destination.write_text(json.dumps(receipt, indent=2) + '\n')
    def call(argv, stem, required=True):
        result = subprocess.run(argv, capture_output=True)
        stdout, stderr = OUT / (stem + '.stdout'), OUT / (stem + '.stderr')
        stdout.write_bytes(result.stdout); stderr.write_bytes(result.stderr)
        if required:
            assert result.returncode == 0, 'CI metadata command failed; inspect captured output before another action'
        return result, str(stdout), str(stderr)
    save()
    for item in inventory['projects']:
        project = item['project']; repo = 'vpsfreecz/' + project
        publication = OUT / ('haveapi-signatures-2.json' if project == 'haveapi' else project + '.json')
        proof = json.loads(publication.read_text())
        assert proof['complete'] and proof['exit_status'] == 0 and proof['head'] == item['head']
        result, stdout, stderr = call(['gh', 'run', 'list', '--repo', repo, '--branch', SLUG, '--limit', '100', '--json', FIELDS], project + '-ci-list')
        runs = json.loads(result.stdout)
        current = [r for r in runs if r['headSha'] == item['head'] and r['headBranch'] == SLUG]
        record = {'project': project, 'reviewed_head': item['head'], 'runs_receipt': stdout, 'metadata_stderr': stderr,
                  'exact_head_runs': current, 'no_matching_head_runs': not current, 'superseded_cancellations': [],
                  'failed_head_logs': [], 'waiting_for_ci': False}
        receipt['repositories'].append(record); save()
        superseded = [r for r in runs if r['headBranch'] == SLUG and r['headSha'] != item['head'] and r['status'] in ('queued', 'in_progress')]
        if superseded:
            remote = subprocess.check_output(['git', '-C', item['worktree'], 'ls-remote', 'origin', 'refs/heads/' + SLUG], text=True).split()[0]
            assert remote == item['head'], 'Feature moved before cancellation; stop and report'
        for run in superseded:
            result, out, err = call(['gh', 'run', 'cancel', str(run['databaseId']), '--repo', repo], project + '-cancel-' + str(run['databaseId']), required=False)
            record['superseded_cancellations'].append({'run': run, 'exit_status': result.returncode, 'stdout': out, 'stderr': err,
                                                       'reason': 'Only this same branch old head was queued/in_progress after final successor publication'})
            save()
        for run in current:
            if run['status'] == 'completed' and run['conclusion'] in ('failure', 'timed_out', 'action_required', 'startup_failure'):
                result, out, err = call(['gh', 'run', 'view', str(run['databaseId']), '--repo', repo, '--log-failed'], project + '-failed-' + str(run['databaseId']), required=False)
                record['failed_head_logs'].append({'run_id': run['databaseId'], 'exit_status': result.returncode, 'stdout': out, 'stderr': err,
                                                   'sha256': hashlib.sha256(result.stdout).hexdigest(), 'owner_diagnosis_required': True})
                save()
        print(project + ': exact-head runs ' + str(len(current)) + ', prior active cancellations ' + str(len(superseded)), flush=True)
    receipt['complete'] = True; save()


if __name__ == '__main__':
    main()
