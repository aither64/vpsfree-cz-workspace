from pathlib import Path
import subprocess,sys
T=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter')
with(T/'finish-shutdown-owner-hosted1.log').open('x')as log:
 p=subprocess.Popen([sys.executable,'-u',str(T/'finish-shutdown-owner-hosted1.py')],cwd=T,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
 for line in p.stdout:
  log.write(line);log.flush();print(line,end='',flush=True)
 code=p.wait()
with(T/'finish-shutdown-owner-hosted1.exit').open('x')as f:f.write(str(code)+'\n')
sys.exit(code)
