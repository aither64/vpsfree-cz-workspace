#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path(sys.argv[1]); lines=p.read_text().splitlines(); pins=[]; result=[]
for line in lines:
 if line.startswith("pick 40b0c2b"):
  pins.append(line);result.append("drop "+line.split(" ",1)[1])
 else: result.append(line)
assert len(pins)==1
p.write_text("\n".join(result)+"\n")
