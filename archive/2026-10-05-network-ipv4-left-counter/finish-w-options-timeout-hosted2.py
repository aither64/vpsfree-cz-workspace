from pathlib import Path
import subprocess, json, time, datetime, hashlib, sys
T = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
OUT = T / 'finish-w-options-timeout-hosted2'
OUT.mkdir()
GH = '/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh'
REPO = 'vpsfreecz/vpsadmin-webui'
HEAD = 'cce681424b866f6a51cbc0a1e4daa226ed33fc07'
WORKFLOWS = {'ci': 369520612, 'smoke': 369520616}
def save(path, data):
    with path.open('xb') as stream: stream.write(data)
def api(path):
    return subprocess.check_output([GH, 'api', 'repos/' + REPO + '/actions/' + path])
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
missing = dict(WORKFLOWS)
pending = {}
results = []
reported_missing = set()
while missing:
    for key, workflow in list(missing.items()):
        raw = api(f'workflows/{workflow}/runs?head_sha={HEAD}&event=pull_request&per_page=100')
        runs = [r for r in json.loads(raw)['workflow_runs'] if r['head_sha'] == HEAD and r['event'] == 'pull_request' and r['head_branch'] == 'dev/ip-suggestions-timeout']
        if not runs:
            if key not in reported_missing:
                print(json.dumps({"awaiting_workflow": key, "head": HEAD}), flush=True)
                reported_missing.add(key)
            continue
        run = min(runs, key=lambda value: value['id'])
        directory = OUT / key
        directory.mkdir()
        save(directory / 'selection.json', raw)
        save(directory / 'initial.json', api('runs/' + str(run['id'])))
        save(directory / 'initial-jobs.json', api('runs/' + str(run['id']) + '/jobs?per_page=100'))
        pending[key] = (run['id'], directory)
        del missing[key]
        print(json.dumps({'selected': key, 'run_id': run['id'], 'head': HEAD}), flush=True)
    if missing: time.sleep(30)
while pending:
    for key, (run_id, directory) in list(pending.items()):
        raw = api('runs/' + str(run_id))
        run = json.loads(raw)
        assert run['head_sha'] == HEAD
        if run['status'] != 'completed': continue
        save(directory / 'final.json', raw)
        save(directory / 'final-jobs.json', api(f'runs/{run_id}/jobs?per_page=100'))
        artifacts = api(f'runs/{run_id}/artifacts?per_page=100')
        save(directory / 'artifacts.json', artifacts)
        log = subprocess.run([GH, 'run', 'view', str(run_id), '--repo', REPO, '--log'], capture_output=True)
        save(directory / 'full.log', log.stdout)
        save(directory / 'log-command.stderr', log.stderr)
        archive = subprocess.run([GH, 'api', f'repos/{REPO}/actions/runs/{run_id}/logs'], capture_output=True)
        save(directory / 'logs.zip', archive.stdout)
        save(directory / 'zip-command.stderr', archive.stderr)
        downloads = []
        for artifact in json.loads(artifacts)['artifacts']:
            if not artifact['name'].startswith('playwright-test-results-') or artifact['expired']: continue
            data = subprocess.run([GH, 'api', f"repos/{REPO}/actions/artifacts/{artifact['id']}/zip"], capture_output=True)
            save(directory / (artifact['name'] + '.zip'), data.stdout)
            save(directory / (artifact['name'] + '.stderr'), data.stderr)
            downloads.append({'id': artifact['id'], 'name': artifact['name'], 'exit': data.returncode})
        result = {'key': key, 'run_id': run_id, 'head': HEAD, 'conclusion': run['conclusion'], 'log_exit': log.returncode, 'zip_exit': archive.returncode, 'downloads': downloads}
        results.append(result)
        del pending[key]
        print(json.dumps(result), flush=True)
    if pending: time.sleep(30)
summary = {'started_at': started, 'finished_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'head': HEAD, 'runs': results, 'sha256': {str(path.relative_to(OUT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(OUT.rglob('*')) if path.is_file()}}
save(OUT / 'summary.json', (json.dumps(summary, indent=2) + '\n').encode())
print('Native hosted evidence retained; no retry or acceptance', flush=True)
sys.exit(0 if all(r['conclusion'] == 'success' and r['log_exit'] == r['zip_exit'] == 0 and all(d['exit'] == 0 for d in r['downloads']) for r in results) else 1)
