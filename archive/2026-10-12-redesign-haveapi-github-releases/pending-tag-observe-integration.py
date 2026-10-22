import json
import pathlib
import subprocess
import time

records = pathlib.Path(__file__).resolve().parent
session = '2026-10-12-redesign-haveapi-github-releases'
run = '44265246-96eb-4791-a5be-bbc594dd8f4d'
previous = None
while True:
    result = subprocess.run(['dev-session', 'coordination', 'integration-status', session, run, '--as-is', '--json'], capture_output=True, text=True)
    if result.returncode:
        print(result.stderr, flush=True)
        raise SystemExit(result.returncode)
    status = json.loads(result.stdout)
    (records / 'pending-tag-integration-observation.json').write_text(json.dumps(status, indent=2) + '\n')
    state = status.get('continuation', {}).get('state')
    value = (status['phase'], state, status.get('reason'), status.get('jobs'))
    if value != previous:
        print(json.dumps({'phase':status['phase'], 'state':state, 'reason':status.get('reason'), 'jobs':status.get('jobs')}), flush=True)
        previous = value
    if status['phase'] == 'complete':
        raise SystemExit(0)
    if state in ('needs_attention', 'paused', 'suspended'):
        raise SystemExit(2)
    time.sleep(15)
