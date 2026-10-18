import json
import os
from pathlib import Path
import subprocess
import time

root = Path('/home/aither/workspace/ai/vpsfree.cz')
records = root / 'work/2026-10-16-idle-coordination-worker'
env = os.environ.copy()
env.update(DEV_SESSION_SLUG='2026-10-16-idle-coordination-worker', DEV_SESSION_WORKSPACE=str(root))
manual = Path('/home/aither/.local/state/dev-workspaces/coordination/integrations/1ff62d7b-911b-4551-82ed-be4a0f6d2460.json')
profile = Path('/home/aither/.local/state/dev-workspaces/profile')
previous = None
started = time.monotonic()
while True:
    result = subprocess.run(['dev-session', 'coordination', 'status', '2026-10-16-idle-coordination-worker', '--as-is', '--json'], cwd=root, env=env, capture_output=True, text=True)
    if result.returncode:
        print(json.dumps({'event': 'status_error', 'exit': result.returncode, 'error': result.stderr[-1500:]}), flush=True)
        raise SystemExit(result.returncode)
    data = json.loads(result.stdout)
    old_run = json.loads(manual.read_text()) if manual.exists() else None
    projection = {
        'jobs': [{k: j.get(k) for k in ['id', 'state', 'revision', 'reason']} for j in data['jobs']],
        'reservations': [{k: r.get(k) for k in ['id', 'state', 'revision']} for r in data['reservations']],
        'profile': str(profile.resolve()),
        'manual': {k: old_run.get(k) for k in ['schema', 'phase', 'reason']} if old_run else None,
    }
    if projection != previous:
        (records / 'wait-status.json').write_text(result.stdout)
        print(json.dumps({'event': 'baseline' if previous is None else 'changed', 'elapsedSeconds': round(time.monotonic()-started), 'projection': projection}), flush=True)
        if previous is not None:
            break
        previous = projection
    time.sleep(60)
