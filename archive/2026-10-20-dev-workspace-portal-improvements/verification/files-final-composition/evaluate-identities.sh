#!/usr/bin/env bash
set -euo pipefail
umask 077
packet=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/files-final-composition
python3 "$packet/guards.py"
test ! -e "$packet/stage-derivation-identities.json"
python3 - "$packet" <<'EVALUATION'
import json,subprocess,sys
from pathlib import Path
p=Path(sys.argv[1]);spec=json.loads((p/'stage-evaluation-command.json').read_text())
with (p/'stage-evaluation.log').open('xb') as log:
 result=subprocess.run(spec['argv'],cwd=spec['workdir'],stdout=subprocess.PIPE,stderr=log,check=False)
 if result.returncode: raise SystemExit(result.returncode)
 values=json.loads(result.stdout)
 with (p/'stage-derivation-identities.json').open('x') as output: output.write(json.dumps(values,indent=2)+'\n')
 print(json.dumps(values,indent=2))
EVALUATION
