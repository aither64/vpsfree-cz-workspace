#!/usr/bin/env python3
import sys
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text();lines=s.splitlines();cmd=[x for x in lines if x.startswith('pick ')];assert len(cmd)==2 and cmd[0].split()[1].startswith('40172e5') and cmd[1].split()[1].startswith('ebfade99');lines[lines.index(cmd[1])]=cmd[1].replace('pick ','fixup -C ',1);p.write_text('\n'.join(lines)+'\n')
