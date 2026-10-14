import json
from pathlib import Path
import subprocess
import sys

tracking = Path(__file__).resolve().parent
for name in ('plan-projection4', 'kernel-builder-proof4', 'closure-plan4', 'missing-closure-facts4'):
    print(json.dumps({'operation': name, 'state': 'starting'}), flush=True)
    result = subprocess.run([sys.executable, str(tracking / ('finish-working-delivery-' + name + '.py'))], cwd=tracking)
    if result.returncode:
        raise SystemExit(result.returncode)
