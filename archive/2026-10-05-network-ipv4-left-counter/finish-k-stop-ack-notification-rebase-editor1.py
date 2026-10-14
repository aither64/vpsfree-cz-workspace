import sys,shlex
from pathlib import Path
p=Path(sys.argv[1]);lines=p.read_text().splitlines();result=[];count=0
for line in lines:
 if line.startswith('pick ') and '29b17bf4bb151fbbb6b693c559cb16a196fa41c5'.startswith(line.split()[1]):
  result.append('exec git commit --amend -F '+shlex.quote('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/finish-k-stop-ack-notification-runtime-amend1.message'));count+=1
 result.append(line)
assert count==1,count
p.write_text('\n'.join(result)+'\n')
