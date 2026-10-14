import json
from pathlib import Path
import subprocess
import sys

tracking = Path(__file__).resolve().parent
for name in ('plan-projection3', 'kernel-builder-proof3', 'closure-plan3', 'missing-closure-facts3'):
    print(json.dumps({'operation': name, 'state': 'starting'}), flush=True)
    result = subprocess.run([sys.executable, str(tracking / ('finish-working-delivery-' + name + '.py'))], cwd=tracking)
    if result.returncode:
        raise SystemExit(result.returncode)
