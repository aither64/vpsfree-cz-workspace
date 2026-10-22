import json, pathlib, subprocess, sys, time

head = sys.argv[1]
records = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-redesign-haveapi-github-releases')
repo = 'vpsfreecz/haveapi'
branch = '2026-10-12-redesign-haveapi-github-releases'
expected = {'release', 'servers/ruby RSpec', 'clients/js tests', 'i18n health', 'RuboCop'}
while True:
    raw = subprocess.check_output(['gh', 'run', 'list', '--repo', repo, '--branch', branch, '--commit', head, '--limit', '50', '--json', 'databaseId,workflowName,status,conclusion,headSha,event'])
    runs = [run for run in json.loads(raw) if run['headSha'] == head and run['event'] == 'push']
    if expected.issubset({run['workflowName'] for run in runs}):
        break
    time.sleep(10)
(records / 'ci-runs.json').write_text(json.dumps(runs, indent=2) + '\n')
failed = False
for run in runs:
    run_id = str(run['databaseId'])
    log = records / ('ci-' + run_id + '.log')
    with log.open('w') as output:
        result = subprocess.run(['gh', 'run', 'watch', run_id, '--repo', repo, '--exit-status', '--interval', '15'], stdout=output, stderr=subprocess.STDOUT)
    print(run['workflowName'], run_id, 'exit', result.returncode, flush=True)
    failed |= result.returncode != 0
    if result.returncode:
        with (records / ('ci-' + run_id + '-failed.log')).open('w') as output:
            subprocess.run(['gh', 'run', 'view', run_id, '--repo', repo, '--log-failed'], stdout=output, stderr=subprocess.STDOUT)
latest = subprocess.check_output(['gh', 'run', 'list', '--repo', repo, '--branch', branch, '--commit', head, '--limit', '50', '--json', 'databaseId,workflowName,status,conclusion,headSha,event'])
(records / 'ci-results.json').write_bytes(latest)
sys.exit(1 if failed else 0)
