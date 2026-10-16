#!/usr/bin/env python3
import sys
from pathlib import Path
p=Path(sys.argv[1]);s=p.read_text().splitlines();steps=[i for i,line in enumerate(s) if line.startswith('pick ')]
assert len(steps)==2
s[steps[1]]=s[steps[1]].replace('pick ','fixup -C ',1)
p.write_text('\n'.join(s)+'\n')
