import json
from pathlib import Path
import subprocess
import sys

tracking = Path(__file__).resolve().parent
for name in ('plan-projection5', 'kernel-builder-proof5', 'closure-plan5', 'missing-closure-facts5'):
    print(json.dumps({'operation': name, 'state': 'starting'}), flush=True)
    result = subprocess.run([sys.executable, str(tracking / ('finish-working-delivery-' + name + '.py'))], cwd=tracking)
    if result.returncode:
        raise SystemExit(result.returncode)
