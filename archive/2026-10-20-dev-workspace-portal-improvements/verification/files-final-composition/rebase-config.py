#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=p.read_text();lines=s.splitlines();found=0;out=[]
for line in lines:
 if line.startswith("pick 5a524d2"):
  found+=1;line="drop "+line.split(" ",1)[1]
 out.append(line)
assert found==1
p.write_text("\n".join(out)+"\n")
