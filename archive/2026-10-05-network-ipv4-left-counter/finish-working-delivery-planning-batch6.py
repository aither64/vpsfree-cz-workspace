import json
from pathlib import Path
import subprocess
import sys

tracking = Path(__file__).resolve().parent
for name in ('plan-projection6', 'kernel-builder-proof6', 'closure-plan6', 'missing-closure-facts6'):
    print(json.dumps({'operation': name, 'state': 'starting'}), flush=True)
    result = subprocess.run([sys.executable, str(tracking / ('finish-working-delivery-' + name + '.py'))], cwd=tracking)
    if result.returncode:
        raise SystemExit(result.returncode)
