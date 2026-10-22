import json
import pathlib
import subprocess
import sys
import time

head, branch, prefix = sys.argv[1:4]
records = pathlib.Path(__file__).resolve().parent
repo = 'vpsfreecz/haveapi'
expected = {'release', 'servers/ruby RSpec', 'clients/ruby RSpec', 'clients/go RSpec', 'clients/js tests', 'clients/php PHPUnit', 'i18n health', 'RuboCop'}

if len(sys.argv) > 4:
    expected = set(json.loads(sys.argv[4]))


def runs_for_head():
    raw = subprocess.check_output([
        'gh', 'run', 'list', '--repo', repo, '--branch', branch,
        '--commit', head, '--limit', '50', '--json',
        'databaseId,workflowName,status,conclusion,headSha,event',
    ])
    return [run for run in json.loads(raw)
            if run['headSha'] == head and run['event'] == 'push']


while True:
    runs = runs_for_head()
    if expected.issubset({run['workflowName'] for run in runs}):
        break
    time.sleep(10)

(records / (prefix + '-ci-runs.json')).write_text(json.dumps(runs, indent=2) + '\n')
failed = False
for run in runs:
    run_id = str(run['databaseId'])
    with (records / (prefix + '-ci-' + run_id + '.log')).open('w') as output:
        result = subprocess.run([
            'gh', 'run', 'watch', run_id, '--repo', repo, '--exit-status',
            '--interval', '15',
        ], stdout=output, stderr=subprocess.STDOUT)
    print(run['workflowName'], run_id, 'exit', result.returncode, flush=True)
    failed |= result.returncode != 0
    if result.returncode:
        with (records / (prefix + '-ci-' + run_id + '-failed.log')).open('w') as output:
            subprocess.run(['gh', 'run', 'view', run_id, '--repo', repo, '--log-failed'],
                           stdout=output, stderr=subprocess.STDOUT)

(records / (prefix + '-ci-results.json')).write_text(
    json.dumps(runs_for_head(), indent=2) + '\n')
sys.exit(1 if failed else 0)
