#!/usr/bin/env python3
import shlex,sys
from pathlib import Path
p=Path(sys.argv[1]); lines=p.read_text().splitlines(); active=[l for l in lines if l and not l.startswith('#')]
assert len(active)==2 and all(l.startswith('pick ') for l in active),active
record=Path(__file__).resolve().parent
command='git commit --amend -F '+shlex.quote(str(record/'selector-message.txt'))
p.write_text(active[0]+'\nexec '+command+'\n'+active[1]+'\n')
