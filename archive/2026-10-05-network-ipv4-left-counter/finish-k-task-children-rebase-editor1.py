import sys,shlex
from pathlib import Path
p=Path(sys.argv[1]); lines=p.read_text().splitlines(); result=[]; added=0
for line in lines:
 if line.startswith('pick ') and '3bb675f1e730ee9f18416363f6700f4000e44d0c'.startswith(line.split()[1]):
  result.append('exec git commit --amend -F '+shlex.quote('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-k-task-children-runtime-amend1.message'));added+=1
 result.append(line)
assert added==1, added
p.write_text('\n'.join(result)+'\n')
