"""Observe one supervised serial merge batch through retained driver files."""
import json
import time
from pathlib import Path

tracking = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination')
results = []
for repository in ['dev-workspace', 'vpsfree-dev-workspace', 'vpsfree-cz-configuration', 'workspace']:
    for phase in ['prepare', 'execute']:
        prefix = tracking / f'bootstrap-integration-{repository}-{phase}'
        status = Path(str(prefix) + '.status')
        while not status.exists():
            time.sleep(5)
        code = int(status.read_text().strip())
        result = {'repository': repository, 'phase': phase, 'status': code}
        if code:
            result['failureTail'] = Path(str(prefix) + '.log').read_text(errors='replace')[-4096:]
        results.append(result)
        temporary = tracking / 'bootstrap-integration-observation.json.tmp'
        temporary.write_text(json.dumps({'results': results, 'complete': bool(code) or len(results) == 8}) + '\n')
        temporary.replace(tracking / 'bootstrap-integration-observation.json')
        print(json.dumps(result), flush=True)
        if code:
            raise SystemExit(0)
