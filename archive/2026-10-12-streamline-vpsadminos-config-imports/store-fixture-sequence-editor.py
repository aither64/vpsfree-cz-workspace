#!/usr/bin/env python3
import json,sys
from pathlib import Path
record=Path(__file__).resolve().parent
i=json.loads((record/'store-fixture-history-inputs.json').read_text())
p=Path(sys.argv[1]); rows=[l.split() for l in p.read_text().splitlines() if l.strip() and not l.startswith('#')]
expected=[i['selector'],i['owner'],i['old'],i['technical']]
assert len(rows)==4 and all(r[0]=='pick' and s.startswith(r[1]) for r,s in zip(rows,expected))
p.write_text('pick '+i['selector']+'\npick '+i['owner']+'\nfixup '+i['technical']+'\npick '+i['old']+'\n')
