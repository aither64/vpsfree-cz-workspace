from pathlib import Path
import subprocess
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
for name in ['finish-e-public-ssh-stdin-pin1-generate1.py','finish-e-public-ssh-stdin-pin1-consolidate.py']:
 p=subprocess.run(['python3',str(T/name)],cwd=T)
 if p.returncode:raise SystemExit(p.returncode)
