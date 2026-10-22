import json
import pathlib
import subprocess
import sys
import time

records = pathlib.Path(__file__).resolve().parent
repository = 'vpsfreecz/haveapi'
head = 'b27a031fa03d8d985a3abd2679ce2fc14fe53602'
minimum_attempt = int(sys.argv[1]) if len(sys.argv) > 1 else 1


def gh(*args):
    return json.loads(subprocess.check_output(['gh', *args], text=True))


while True:
    runs = gh('run', 'list', '--repo', repository, '--branch', 'v0.29.10',
              '--commit', head, '--workflow', 'release.yml', '--limit', '10',
              '--json', 'databaseId,headSha,headBranch,event,url,status,conclusion')
    runs = [run for run in runs if run['headSha'] == head and run['event'] == 'push']
    if runs:
        assert len(runs) == 1, runs
        run_id = str(runs[0]['databaseId'])
        (records / 'release-tag-run.json').write_text(json.dumps(runs[0], indent=2) + '\n')
        print('RELEASE_RUN', run_id, runs[0]['url'], flush=True)
        break
    time.sleep(10)

while True:
    current = gh('api', f'repos/{repository}/actions/runs/{run_id}')
    if current['run_attempt'] < minimum_attempt:
        time.sleep(15)
        continue
    run = gh('run', 'view', run_id, '--repo', repository, '--json',
             'databaseId,headSha,headBranch,event,url,status,conclusion,jobs')
    assert run['headSha'] == head and run['headBranch'] == 'v0.29.10', run
    (records / 'release-tag-status.json').write_text(json.dumps(run, indent=2) + '\n')
    if run['status'] == 'completed':
        result = 0 if run['conclusion'] == 'success' else 1
        if result:
            with (records / f'release-tag-attempt{current["run_attempt"]}-failed.log').open('w') as output:
                subprocess.run(['gh', 'run', 'view', run_id, '--repo', repository,
                                '--log-failed'], stdout=output, stderr=subprocess.STDOUT)
        print('RELEASE_COMPLETED', run['conclusion'], run['url'], flush=True)
        raise SystemExit(result)
    if any(job['name'] == 'Validate, test and build' and job['conclusion'] == 'success'
           for job in run['jobs']):
        pending = gh('api', f'repos/{repository}/actions/runs/{run_id}/pending_deployments')
        (records / 'release-tag-pending.json').write_text(json.dumps(pending, indent=2) + '\n')
        if any(item['environment']['name'] == 'release' for item in pending):
            print('APPROVAL_REQUIRED', run['url'], flush=True)
            raise SystemExit(0)
    time.sleep(15)
