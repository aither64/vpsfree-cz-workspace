from pathlib import Path
import subprocess, sys
r=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
with (r/'finish-w-options-timeout-hosted2.log').open('x') as log:
    p=subprocess.Popen([sys.executable,'-u',str(r/'finish-w-options-timeout-hosted2.py')],cwd=r,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
    for line in p.stdout:
        log.write(line);log.flush();print(line,end='',flush=True)
    code=p.wait()
with (r/'finish-w-options-timeout-hosted2.exit').open('x') as f:f.write(str(code)+'\n')
raise SystemExit(code)
